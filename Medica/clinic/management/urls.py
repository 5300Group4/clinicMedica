from django.urls import path
from . import views

urlpatterns = [
    path('payment_mag/', views.payment, name='payment_mag'),
    path('<id>/payment_edit/', views.payment_edit, name='payment_edit'),
    path('<id>/payment_delete/', views.payment_delete, name='payment_delete'),
    path('appointment_mag/', views.appointment_mag, name='appointment_mag'),
    path('location_mag/', views.location_mag, name='location_mag'),
    path('location_add/', views.location_add, name='location_add'),
    path('<id>/appointment_edit/', views.appointment_edit, name='appointment_edit'),
    path('<id>/appointment_delete/', views.appointment_delete, name='appointment_delete'),
    path('<address>/location_edit/', views.location_edit, name='location_edit'),
    path('<id>/location_delete/', views.location_delete, name='location_delete'),
]
