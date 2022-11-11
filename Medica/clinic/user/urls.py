from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.payment, name='payment'),
    path('doctor/', views.doctor, name='doctor'),
    path('<id>/appointment/', views.appointment, name='appointment'),
    # 主界面
    path('main/',views.homepage, name ='homepage'),
    # user自己的更新界面
    path('update/',views.userSurface,name = 'userSurface'),
    # 这些是admin的操作
    path('ad/info/',views.adminTable,name = 'adminTable'),
    path('ad/info/delete/',views.adminTableDel,name='adminTableDel'),
    path('ad/info/add/',views.adminTableAdd,name='adminTableAdd'),
    path('ad/<int:nid>/edit/',views.adminTableEdit,name='adminTableEdit')


]
