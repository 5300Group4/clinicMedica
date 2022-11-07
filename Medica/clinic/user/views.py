from django.shortcuts import render, HttpResponse
from user.models import Payment
from django.contrib.auth import authenticate, login
from user.models import Appointment

# Create your views here.
from django.core.mail import send_mail


def payment(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email=request.POST.get('email')
        value = request.POST.get('value')
        doctor = request.POST.get('email')
        order=Payment()
        order.username=username
        order.email=email
        order.value=value
        order.doctor=doctor
        order.save()
    return render(request, 'payment.html', {})

def doctor(request):
    return render(request, 'doctor.html', {})

def appointment(request):
    if request.method == 'POST':   # 判断采用的是何种请求
        # request.POST[]或request.POST.get()获取数据
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        date = request.POST['date']

        new_appointment = Appointment()
        new_appointment.email =  email
        new_appointment.phone_number = phone_number
        new_appointment.date = date

        new_appointment.save()

        message = "test"
        send_mail(
            'Test',
            'Here is the test.',
            '912675127@qq.com',
            [email],
        )
    return render(request, 'appointment.html', {})

