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
<<<<<<< HEAD
    # == == == =
    location = models.CharField(max_length=20, null=True)
    # 吴志洋加，这行可以让我返回name
    def __str__(self):
        return self.name


class Location(models.Model):
    address = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    clinic_number = models.CharField(max_length=255)
    clinic_picture = models.CharField(max_length=255)

# >> >> >> >
# b9a17a0d207bc5c3aeac28de2f23f9f8a37f5ec
# <<<<<<< HEAD





=======
    location = models.CharField(max_length=20, null=True)


    # 吴志洋加，这行可以让我返回name
    # def __str__(self):
    #     return self.name
>>>>>>> a82b33ef6fd631a2d8ced501f30a2dc42c2b4ee4
class UserInfo(models.Model):
    # 姓名、密码、年龄、email、性别、预约大夫
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(verbose_name="name",max_length=32)
    password = models.CharField(verbose_name="password",max_length=64)
    age = models.IntegerField(verbose_name="age")
    email = models.CharField(verbose_name="email",max_length=64)
    # 性别是元组
    gender_choice = ((1,"male"),(2,"female"),(3,"unknown"))
    gender = models.SmallIntegerField(verbose_name="gender",choices=gender_choice)
#     # 连级删除
#     # 等数据库连上再说
    appointment = models.ForeignKey(verbose_name="appointment",to="Doctor",to_field="id",on_delete=models.CASCADE,default="none")


<<<<<<< HEAD

=======


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

>>>>>>> a82b33ef6fd631a2d8ced501f30a2dc42c2b4ee4
