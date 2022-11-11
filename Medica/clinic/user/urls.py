from django.urls import path
from . import views

urlpatterns = [
    # path('doctor/', views.doctor, name='doctor'),
    path('<id>/appointment/', views.appointment, name='appointment'),
<<<<<<< HEAD
    # 主界面
    path('main/',views.homepage, name ='homepage'),
    # user自己的更新界面
    path('update/',views.userSurface,name = 'userSurface'),
    # 这些是admin的操作
    path('ad/info/',views.adminTable,name = 'adminTable'),
    path('ad/info/delete/',views.adminTableDel,name='adminTableDel'),
    path('ad/info/add/',views.adminTableAdd,name='adminTableAdd'),
    path('ad/<int:nid>/edit/',views.adminTableEdit,name='adminTableEdit')


=======
    path('location/', views.location, name='location'),
    path('<city>/doctor/', views.doctor, name='show_doctor'),
>>>>>>> 2b9a17a0d207bc5c3aeac28de2f23f9f8a37f5ec
]
