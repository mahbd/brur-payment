from random import randint

from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.urls import reverse
from django.views.generic import CreateView, TemplateView, UpdateView

from payment.models import Payment


@receiver(post_save, sender=Payment)
def post_payment(instance: Payment, created, *args, **kwargs):
    if created:
        instance.pay_code = str(randint(10_000_000, 99_999_999))
        instance.save()
        instance.refresh_from_db()
        html_content = get_template('created_email.html')
        d = {'payment': instance}
        msg_plain = f'Your payment code is: {instance.pay_code}'
        html_content = html_content.render(d)
        send_mail(subject='Payment Successful', html_message=html_content, recipient_list=[instance.email],
                  fail_silently=False, message=msg_plain, from_email=EMAIL_HOST_USER)


class Home(TemplateView):
    template_name = 'payment/index.html'


def payment_success(request, pay_code, *args, **kwargs):
    return render(request, 'payment/success.html', {'pay_code': pay_code})


class AskPayCode(TemplateView):
    template_name = 'payment/ask_pay_code.html'


class PaymentView(CreateView):
    def get_success_url(self):
        return reverse('success', args=[self.object.pay_code])

    model = Payment
    fields = ('name', 'email', 'roll', 'registration_number', 'department', 'semester',
              'method', 'account', 'amount', 'transaction_id')

    def get_initial(self):
        self.initial['method'] = self.request.GET.get('method')
        return super().get_initial()


class EditPaymentView(UpdateView):
    def get_success_url(self):
        send_mail('Payment updated', 'Your payment is updated', EMAIL_HOST_USER, [self.object.email])
        return reverse('success', args=[self.object.pay_code])

    slug_field = 'pay_code'
    context_object_name = 'repay'
    template_name = 'payment/edit_payment.html'
    model = Payment
    fields = ('name', 'email', 'roll', 'registration_number', 'department', 'semester',
              'method', 'account', 'amount', 'transaction_id', 'extra_transactions',)


def recover_code(request, *args, **kwargs):
    if request.method == 'POST':
        email = request.POST.get('email')
        payment = Payment.objects.filter(email=email)
        if payment and email:
            send_mail('Payment code', f'Your payment code is {payment.first().pay_code}', EMAIL_HOST_USER, [email])
            return HttpResponse('<h1>An email has been sent with payment code. Please don\'t forget to check '
                                'your spam folder</h1>')
        return HttpResponse('<h1>Invalid email or no payment made using this email</h1>')
