from django.shortcuts import render, HttpResponse,redirect
from user.models import UserInfo
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login
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
        user = UserInfo.objects.get(name=username)
        uid = str(user.id)
        if (password == user.password) and(user.id==1) :
            return redirect('http://127.0.0.1:8000/ad/info/')
        elif (password == user.password) and (uid != 1):
            return redirect('http://127.0.0.1:8000/main/'+uid+'/homepage/')
            
        else:
            return HttpResponse('登陆失败')

    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = UserInfo()
        user.name = username
        user.email = email
        user.password = password
        user.save()
        logintest = UserInfo.objects.get(name=username)
        if password == logintest.password:
            return HttpResponseRedirect('/main')
        else:
            return HttpResponse('注册失败')

    return render(request,'register.html')