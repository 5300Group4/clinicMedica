from django.db import models

# Create your models here.

# 不需要了 直接引用User的Appointment 
# class Appointment(models.Model):
#     name = models.CharField(max_length=32)
#     description = models.CharField(max_length=255)
#     doctor = models.CharField(max_length=32, null=True)
#     location = models.CharField(max_length=20, null=True)
#     date = models.DateField()
