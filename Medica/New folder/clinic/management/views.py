from django.shortcuts import render
from user.models import Payment
# Create your views here.

def payment(request):
    payment_list = Payment.objects.all()
    return render(request, 'payment_mag.html', {'payment_list': payment_list})
    


def appointment_mag(request):
    return render(request, 'appointment_mag.html', {})
