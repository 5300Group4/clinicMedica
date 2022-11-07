from django.db import models

# Create your models here.

class Appointment(models.Model):
    email = models.EmailField(max_length=32)
    phone_number = models.CharField(max_length=32)
    date = models.DateField()
    comment = models.CharField(max_length=64)

class Payment(models.Model):
    paymentid = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    value = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    doctor = models.CharField(max_length=32)
    # contact=models.CharField(max_length=255)
    # objects=models.Manager()
    #image = models.ImageField(upload_to='images/%Y/%m', default='images/default.png', max_length=100, verbose_name='用户头像')

class Doctor(models.Model):
    name = models.CharField(max_length=32)
    introduction = models.CharField(max_length=255)
    picture = models.CharField(max_length=255)
