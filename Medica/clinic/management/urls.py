from django.urls import path
from . import views

urlpatterns = [
    path('payment_mag/', views.payment, name='payment_mag'),
    path('appointment_mag/', views.appointment_mag, name='appointment_mag'),
    path('<ename>/appointment_edit/', views.appointment_edit, name='appointment_edit'),
    path('<ename>/appointment_delete/', views.appointment_delete, name='appointment_delete'),
]
