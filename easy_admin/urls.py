from django.urls import path

from . import views

app_name = 'ea'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accept/<int:pid>/<str:red>/', views.accept_payment, name='accept'),
    path('deny/<int:pid>/<str:red>/', views.deny_payment, name='deny'),
]
