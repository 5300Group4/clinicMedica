from django.shortcuts import render
from user.models import Payment
# Create your views here.


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
    return render(request, 'appointment.html', {})
