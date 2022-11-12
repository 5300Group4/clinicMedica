from django.urls import path
from . import views


urlpatterns = [
    path('',views.redir,name ="redir"),
    path('doctor/', views.doctor, name='doctor'),
    path('<id>/appointment/', views.appointment, name='appointment'),

    # 主界面
    path('main/',views.homepage, name ='homepage'),

    # 登录后的界面

    path('main/<int:nid>/homepage/',views.homepageAfterLoginIn,name = "homepageAfterLoginIn"),

    # user自己的更新界面

    path('main/<int:nid>/update/', views.personalEdit, name='personalEdit'),
    # 登出



    # 这些是admin的操作
    path('ad/info/',views.adminTable,name = 'adminTable'),
    path('ad/<int:nid>/delete/',views.adminTableDel,name='adminTableDel'),
    path('ad/info/add/',views.adminTableAdd,name='adminTableAdd'),
    path('ad/<int:nid>/edit/',views.adminTableEdit,name='adminTableEdit'),


    path('location/', views.location, name='location'),
    path('<city>/doctor/', views.doctor, name='show_doctor'),

]

