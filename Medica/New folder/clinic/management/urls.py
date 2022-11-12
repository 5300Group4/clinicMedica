from django.urls import path
from . import views

urlpatterns = [
    path('payment_mag/', views.payment, name='payment_mag'),
    path('appointment_mag/', views.appointment_mag, name='appointment_mag'),
]
