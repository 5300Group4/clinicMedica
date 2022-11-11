"""clinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

#Please be specific when you writing the PATH unless it's mainpage
urlpatterns = [
    path('admin/', admin.site.urls),
    # access through http://127.0.0.1:8000/login/
    #login includes login function and register function
    path('login/', include('login.urls')), 
    path('', include('user.urls')),
    path('', include('payment.urls')),
    path('', include('management.urls')),


]
