from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from constants import SEMESTERS
from payment.models import Payment


@method_decorator(login_required, name='dispatch')
class Home(View):
    def get(self, *args, **kwargs):
        def get_payments():
            semester = self.request.GET.get('semester', 'one')
            department = self.request.user.department
            if department:
                return Payment.objects.filter(department=department, semester=semester)
            return []

        buttons = (('btn-primary', f"{reverse('ea:home')}?semester={key}", f'{value} Semester')
                   for key, value in SEMESTERS)

        return render(self.request, 'easy_admin/home.html', context={
            'payments': get_payments(),
            'buttons': buttons,
            'semester': self.request.GET.get('semester', 'one')
        })


@login_required
def accept_payment(request, pid, red):
    payment = get_object_or_404(Payment, pk=pid)
    payment.verified = True
    payment.save()
    send_mail('Payment verified', 'Your payment is verified.', EMAIL_HOST_USER, [payment.email])
    return redirect(f"{reverse('ea:home')}?semester={red}")


@login_required
def deny_payment(request, pid, red):
    payment = get_object_or_404(Payment, pk=pid)
    payment.verified = False
    payment.save()
    send_mail('Payment denied', 'Your payment is denied.', EMAIL_HOST_USER, [payment.email])
    return redirect(f"{reverse('ea:home')}?semester={red}")
