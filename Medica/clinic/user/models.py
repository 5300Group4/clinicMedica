from django.db import models

# Create your models here.

class Appointment(models.Model):
    email = models.EmailField(max_length=32)
    phone_number = models.CharField(max_length=32)
    date = models.DateField()
    doctor = models.CharField(max_length=32, null=True)
    comment = models.CharField(max_length=64)


class Doctor(models.Model):
    name = models.CharField(max_length=32)
    introduction = models.CharField(max_length=255)
    picture = models.CharField(max_length=255)
    location = models.CharField(max_length=20, null=True)

class Location(models.Model):
    address = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    clinic_number = models.CharField(max_length=255)
    clinic_picture = models.CharField(max_length=255)


class Payment(models.Model):
    date = models.DateField()
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    status = models.CharField(max_length=32)

    # contact=models.CharField(max_length=255)
    # objects=models.Manager()
    #image = models.ImageField(upload_to='images/%Y/%m', default='images/default.png', max_length=100, verbose_name='用户头像')
