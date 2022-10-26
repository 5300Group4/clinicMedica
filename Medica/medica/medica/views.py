from django.shortcuts import render

def runoob(request):
  views_name = "hello"
  return  render(request,"helloworld.html", {"name":views_name})