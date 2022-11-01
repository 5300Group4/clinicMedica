from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from login.models import User
# Create your views here.


def login_view(request):
    if request.method == 'POST':   # 判断采用的是何种请求
        # request.POST[]或request.POST.get()获取数据
        username = request.POST['username']
        password = request.POST['password']
        # 与数据库中的用户名和密码比对，django默认保存密码是以哈希形式存储，并不是明文密码，这里的password验证默认调用的是User类的check_password方法，以哈希值比较。
        ''' User = authenticate(request, username=username, password=password)
        # 验证如果用户不为空
        if User is not None:
            # login方法登录,Django 自带
            login(request, User)
            # 返回登录成功信息
            return HttpResponse('登陆成功')
        else:
            # 返回登录失败信息
            return HttpResponse('登陆失败')'''
        user=User.objects.get(username=username)
        if password==user.password:
            return HttpResponse('登陆成功')
        else:
            return HttpResponse('登陆失败')

    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User()
        user.username = username
        user.email = email
        user.password = password
        user.save()
    return render(request,'register.html')