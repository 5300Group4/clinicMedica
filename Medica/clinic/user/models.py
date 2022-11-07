from django.db import models

# Create your models here.

class Appointment(models.Model):
    email = models.EmailField(max_length=32)
    phone_number = models.CharField(max_length=32)
    date = models.DateField()
    comment = models.CharField(max_length=64)

class Doctor(models.Model):
    name = models.EmailField(max_length = 32)
    