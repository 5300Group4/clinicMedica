# Generated by Django 4.1.2 on 2022-11-11 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_appointment_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='name')),
                ('password', models.CharField(max_length=64, verbose_name='password')),
                ('age', models.IntegerField(verbose_name='age')),
                ('email', models.CharField(max_length=64, verbose_name='email')),
                ('gender', models.SmallIntegerField(choices=[(1, 'male'), (2, 'female'), (3, 'unknown')], verbose_name='gender')),
                ('appointment', models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to='user.doctor', verbose_name='appointment')),
            ],
        ),
    ]