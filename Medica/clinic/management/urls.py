from django.urls import path
from . import views

urlpatterns = [
    path('payment_mag/', views.payment, name='payment_mag'),
    path('<ename>/payment_edit/', views.payment_edit, name='payment_edit'),
    path('<ename>/payment_del/', views.payment_delete, name='payment_delete'),
    path('appointment_mag/', views.appointment_mag, name='appointment_mag'),
    path('<ename>/appointment_edit/', views.appointment_edit, name='appointment_edit'),
    path('<ename>/appointment_delete/', views.appointment_delete, name='appointment_delete'),
]
