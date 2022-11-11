from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    # access through http://127.0.0.1:8000/login/register/
    path('register/',views.register,name='register')
]
