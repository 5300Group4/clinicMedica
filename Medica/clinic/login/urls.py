from django.urls import path
from login import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
