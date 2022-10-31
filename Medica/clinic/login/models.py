from django.db import models

# Create your models here.


class User(models.Model):
    id = models.UUIDField(max_length=10)
    pub_date = models.DateTimeField('date published')
