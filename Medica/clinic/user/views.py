from django.shortcuts import render, HttpResponse
import user.models
from user.models import Appointment
from user.models import Doctor
from user.models import Location
from user.models import Payment
from django.shortcuts import get_object_or_404, render
from user.models import UserInfo
from django.core.mail import send_mail
from django.shortcuts import redirect


# Create your views here.

def redir(request):
    return redirect('http://127.0.0.1:8000/main/')


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
    data_checkout = {}
    context["doctor"] = obj
    if request.method == 'POST':   # 判断采用的是何种请求
        # fetch the object related to passed id
        # request.POST[]或request.POST.get()获取数据
        name = request.POST['name']
        email = request.POST['email']
        date = request.POST['date']
        comment = request.POST['comment']

        data_checkout["email"] = email

        #存储user_appointment数据 - Qi
        new_appointment = Appointment()
        new_appointment.name =  name
        new_appointment.location = obj.location
        new_appointment.email =  email
        new_appointment.comment = comment
        new_appointment.date = date
        new_appointment.doctor = obj.name

        new_appointment.save()

        #payment存储 - Qi
        order = Payment()
        order.email = email
        order.username=name
        order.status = 'processing'
        order.pdate = date
        order.save()

        send_mail(
            'Appointment Notification',
            'Dear Patient, this email is to inform you that you have successfully booked an offline consultation service, please arrive at the clinic at the appointment time. Thank you for your support.',
            'Medica Center', #Email Send Title
            [email],
        )
        return render(request, 'home.html', data_checkout)

    return render(request, 'appointment.html', context)


# 下面都是吴志洋写的
def redir(request):
    return redirect('http://127.0.0.1:8000/main/')

# homepage
def homepage(request):
    return render(request,'homepage.html')

# 登录后的homepage()


def homepageAfterLoginIn(request, nid):
    user_name = UserInfo.objects.filter(id=nid).filter().first()
    return render(request, 'homepageAfterLoginIn.html', {'user_name': user_name, 'nid': nid})


def personalEdit(request, nid):
    sNid = str(nid)
    new_User = user.models.UserInfo.objects.filter(id=nid).filter().first()
    # new_User = user.models.UserInfo
    if request.method == "GET":
        form = UserForm(instance=new_User)
        return render(request, 'userSurface.html', {'form': form})
    form = UserForm(data=request.POST, instance=new_User)
    if form.is_valid():
        form.save()
        return redirect('http://127.0.0.1:8000/main/'+sNid+'/homepage/')


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


# 登录后的homepage()
def homepageAfterLoginIn(request, nid):
    user_name = UserInfo.objects.filter(id=nid).filter().first()
    return render(request, 'homepageAfterLoginIn.html',{'user_name':user_name,'nid':nid})


def personalEdit(request,nid):
    sNid = str(nid)
    new_User = user.models.UserInfo.objects.filter(id=nid).filter().first()
    # new_User = user.models.UserInfo
    if request.method == "GET":
        form = UserForm(instance=new_User)
        return render(request, 'userSurface.html', {'form': form})
    form = UserForm(data=request.POST, instance=new_User)
    if form.is_valid():
        form.save()
        return redirect('http://127.0.0.1:8000/main/'+sNid+'/homepage/')

  # userSurface
# def userSurface(request):
#     return render(request, 'userSurface.html')


# 管理员的界面
def adminTable(request):
    # user_list = UserForm()
    user_list = UserInfo.objects.all()
    return render(request, 'admin-tables.html', {'user_list':user_list})


def adminTableDel(request,nid):
    # nid = request.GET.get('nid')
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
    # new_User = user.models.UserInfo
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
