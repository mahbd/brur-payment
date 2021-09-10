from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('payment/', views.PaymentView.as_view(), name='payment'),
    path('success/<int:pay_code>/', views.payment_success, name='success'),
    path('pay-code/', views.AskPayCode.as_view(), name='pay_code'),
    path('edit-payment/<int:slug>/', views.EditPaymentView.as_view(), name='edit_payment'),
    path('recover-code/', views.recover_code, name='recover_code'),
]
