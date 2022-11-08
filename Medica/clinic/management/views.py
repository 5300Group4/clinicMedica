from django.shortcuts import render

# Create your views here.

def payment(request):
    return render(request, 'payment.html', {})

def appointment_mag(request):
    return render(request, 'appointment_mag.html', {})
