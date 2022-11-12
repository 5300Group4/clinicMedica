from django.shortcuts import render
from user.models import Appointment
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect

from user.models import Payment
# Create your views here.

def payment(request):
    payment_list = Payment.objects.all()
    return render(request, 'payment_mag.html', {'payment_list': payment_list})

def payment_edit(request):
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Payment.objects.all()
    return render(request, 'payment_edit.html', context)


def payment_delete(request):
    return render(request, 'payment_delete.html', {})

def appointment_mag(request):
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Appointment.objects.all()
    return render(request, 'appointment_mag.html', context)

def appointment_edit(request, ename):
    context ={}
    # add the dictionary during initialization
    context["patient"] = Appointment.objects.filter(name = ename)

    if request.method == 'POST':   # 判断采用的是何种请求
        obj = get_object_or_404(Appointment, name = ename)
        # fetch the object related to passed id
        # request.POST[]或request.POST.get()获取数据

        #update the new info
        obj.name = request.POST['name']
        obj.email = request.POST['email']
        obj.date = request.POST['date']
        obj.comment = request.POST['comment']
        #save
        obj.save()
        #messages.success(request, 'Successfully!')
        return redirect("http://127.0.0.1:8000/appointment_mag/")
         
    return render(request, 'appointment_edit.html', context)


def appointment_delete(request,ename):
    obj = get_object_or_404(Appointment, name = ename)
    context ={}
    context["patient"] = Appointment.objects.filter(name = ename)

    if request.method == 'POST':   # 判断采用的是何种请求
        obj.delete()
        return redirect("http://127.0.0.1:8000/appointment_mag/")

    return render(request, 'appointment_delete.html', context)
