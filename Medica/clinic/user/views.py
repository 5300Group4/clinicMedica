from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from user.models import Appointment
from user.models import Doctor
from user.models import Location
from user.models import Payment
from django.shortcuts import get_object_or_404, render
from user.models import UserInfo
from django.core.mail import send_mail
from django.shortcuts import redirect




# Create your views here.




def doctor(request, city):

    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Doctor.objects.filter(location = city)
         
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

        order = Payment()
        order.email = email
        order.status = 'processing'
        order.date = date
        order.save()

        message = "test"

        send_mail(
            'Test',
            'Here is the test.',
            '912675127@qq.com',
            [email],
        )
    return render(request, 'appointment.html', context)

# 下面都是吴志洋写的
# homepage
def homepage(request):
    return render(request,'homepage.html')

# userSurface
def userSurface(request):

    return render(request,'userSurface.html')

# 用组件编写

from django import forms

class UserForm(forms.ModelForm):
    # 对name加限制
    name = forms.CharField(min_length=3,label="username")

    class Meta:
        model= user.models.UserInfo
        fields=["name","password","age","email","gender","appointment"]
        # 仅供测试用，到时候用上面的哪一个
        # fields=["name","password","age","email","gender"]

    #     别问我这行代码，我也不知道为什么
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs = {"class":"form-control","placeholder":field.label}


def adminTable(request):
    user_list = UserInfo.objects.all()
    return render(request, 'admin-tables.html', {'user_list':user_list})


def adminTableDel(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    return redirect("http://127.0.0.1:8000/ad/info/")

def adminTableAdd(request):
    # 传新版本的添加
    if request.method == "GET":
        form = UserForm()
        return render(request,'admin-tables-add.html',{"form":form})

    form = UserForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("http://127.0.0.1:8000/ad/info/")
    return render(request,'admin-tables-add.html',{"form":form})

    # id = request.POST.get("id")
    # name = request.POST.get("name")
    # psw = request.POST.get("password")
    # email = request.POST.get("email")
    # age = request.POST.get("age")

    # UserInfo.objects.create(name=name,password=psw,email=email,age=age)
def adminTableEdit(request,nid):
    new_User = user.models.UserInfo.objects.filter(id=nid).filter().first()
    if request.method=="GET":
        form = UserForm(instance=new_User)
        return render(request,'admin-tables-edit.html',{'form':form})
    form = UserForm(data=request.POST,instance=new_User)
    if form.is_valid():
        form.save()
        return redirect('http://127.0.0.1:8000/ad/info/')




def location(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Location.objects.all()

    return render(request, 'location.html', context)


