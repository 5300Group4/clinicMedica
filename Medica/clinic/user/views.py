from django.shortcuts import render

# Create your views here.


def payment(request):
    return render(request, 'payment.html', {})

def doctor(request):
    return render(request, 'doctor.html', {})

def appointment(request):
    return render(request, 'appointment.html', {})
