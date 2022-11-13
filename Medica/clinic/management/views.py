from django.shortcuts import render
from user.models import Appointment
from user.models import Location
from user.models import Payment
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.

def payment(request):
    context = {}
    context["payment"] = Payment.objects.all()
    return render(request, 'payment_mag.html', context)


def payment_edit(request, id):
    context = {}
    # add the dictionary during initialization
    context["payment"] = Payment.objects.filter(id=id)

    if request.method == 'POST':   # 判断采用的是何种请求
        obj = get_object_or_404(Payment, id=id)
        # fetch the object related to passed id
        # request.POST[]或request.POST.get()获取数据

        # update the new info
        obj.username = request.POST['username']
        obj.email = request.POST['email']
        obj.pdate = request.POST['date']
        obj.status = request.POST['status']
        # save
        obj.save()
        #messages.success(request, 'Successfully!')
        return redirect("http://127.0.0.1:8000/payment_mag/")

    return render(request, 'payment_edit.html', context)


def payment_delete(request,id):
    obj = get_object_or_404(Payment, id=id)
    context = {}
    context["payment"] = Payment.objects.filter(id=id)

    if request.method == 'POST':   # 判断采用的是何种请求
        obj.delete()
        return redirect("http://127.0.0.1:8000/payment_mag/")

    return render(request, 'payment_delete.html', context)

def appointment_mag(request):
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Appointment.objects.all()
    return render(request, 'appointment_mag.html', context)

def appointment_edit(request, id):
    context ={}
    # add the dictionary during initialization
    context["patient"] = Appointment.objects.filter(id = id)

    if request.method == 'POST':   # 判断采用的是何种请求
        obj = get_object_or_404(Appointment, id = id)
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


def appointment_delete(request, id):
    obj = get_object_or_404(Appointment, id = id)
    context ={}
    context["patient"] = Appointment.objects.filter(id = id)

    if request.method == 'POST':   # 判断采用的是何种请求
        obj.delete()
        return redirect("http://127.0.0.1:8000/appointment_mag/")

    return render(request, 'appointment_delete.html', context)


def location_mag(request):
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Location.objects.all()
    return render(request, 'location_mag.html', context)


def location_edit(request, address):
    context = {}
    # add the dictionary during initialization
    context["location"] = Location.objects.filter(address=address)

    if request.method == 'POST':  # 判断采用的是何种请求
        obj = get_object_or_404(Location, address=address)
        # fetch the object related to passed id
        # request.POST[]或request.POST.get()获取数据

        # update the new info
        obj.address = request.POST['address']
        obj.city = request.POST['city']
        obj.clinic_number = request.POST['number']
        obj.clinic_picture = request.POST['picture']
        # save
        obj.save()
        # messages.success(request, 'Successfully!')
        return redirect("http://127.0.0.1:8000/location_mag/")

    return render(request, 'location_edit.html', context)

def location_delete(request,id):
    obj = get_object_or_404(Location, id=id)
    context ={}
    context["location"] = Location.objects.filter(id=id)

    if request.method == 'POST':   # 判断采用的是何种请求
        obj.delete()
        return redirect("http://127.0.0.1:8000/location_mag/")

    return render(request, 'location_delete.html', context)

def location_add(request):
    context = {}
    if request.method == 'POST':  # 判断采用的是何种请求
        # fetch the object related to passed id
        # request.POST[]或request.POST.get()获取数据
        address = request.POST['address']
        city = request.POST['city']
        clinic_number = request.POST['number']
        clinic_picture = request.POST['picture']


        # 存储user_appointment数据 - Qi
        new_location = Location()
        new_location.address = address
        new_location.city = city
        new_location.clinic_number = clinic_number
        new_location.clinic_picture = clinic_picture

        new_location.save()


        return redirect("http://127.0.0.1:8000/location_mag/")

    return render(request, 'location_add.html', context)
