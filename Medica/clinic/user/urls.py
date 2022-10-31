from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.payment, name='payment'),
    path('doctor/', views.doctor, name='doctor'),
    path('appointment/', views.appointment, name='appointment'),
]
