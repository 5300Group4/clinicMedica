from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.payment, name='payment'),
    # path('doctor/', views.doctor, name='doctor'),
    path('<id>/appointment/', views.appointment, name='appointment'),
    path('location/', views.location, name='location'),
    path('<city>/doctor/', views.doctor, name='show_doctor'),
]
