from django.db import models

# Create your models here.
class Student(models.Model):
    #id=models.AutoField()
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    adrress=models.TextField(null=True,blank=True)
    #image=models.ImageField()
    file=models.FileField()

class Car(models.Model):
    car_name=models.CharField(max_length=50)
    speed=models.IntegerField(default=50)