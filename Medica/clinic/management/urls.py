from django.urls import path
from . import views

urlpatterns = [
    path('payment', views.payment, name='payment'),
    path('appointment_mag/', views.appointment_mag, name='appointment_mag'),
]
