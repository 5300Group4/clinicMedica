from django.shortcuts import render, HttpResponse
from user.models import Payment
from django.contrib.auth import authenticate, login
from user.models import Appointment
from user.models import Doctor
from user.models import Location
from django.shortcuts import get_object_or_404, render

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
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Doctor.objects.all()
         
    return render(request, 'doctor.html', context)

def appointment(request,id):
    obj = get_object_or_404(Doctor, id = id)
    context ={}
    context["doctor"] = obj.name
    if request.method == 'POST':   # 判断采用的是何种请求
        # fetch the object related to passed id
        # request.POST[]或request.POST.get()获取数据
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        date = request.POST['date']

        new_appointment = Appointment()
        new_appointment.email =  email
        new_appointment.phone_number = phone_number
        new_appointment.date = date
        new_appointment.doctor = obj.name

        new_appointment.save()

        message = "test"
        send_mail(
            'Test',
            'Here is the test.',
            '912675127@qq.com',
            [email],
        )
    return render(request, 'appointment.html', context)


def location(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Location.objects.all()

    return render(request, 'location.html', context)
