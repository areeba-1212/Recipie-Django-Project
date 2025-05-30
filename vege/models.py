from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models here.

class Recipie(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)#if user deleted then all its recipies will be deleted 
    r_name=models.CharField(max_length=100)
    r_des=models.TextField()
    r_image=models.ImageField(upload_to="recipies/")



class Department(models.Model):
    department=models.CharField(max_length=100)

    def _str_(self) ->str:
        return self.department
    
    class Meta:
        ordering=['department']


class StudentID(models.Model):
    studentID=models.CharField(max_length=100)

    def _str_(self) ->str:
        return self.studentID
    

class Student(models.Model): 
    department = models. ForeignKey (Department, related_name="depart", on_delete=models.CASCADE)
    student_id = models.OneToOneField (StudentID, related_name="studentid",on_delete=models.CASCADE)
    student_name = models. CharField(max_length=100) 
    student_email = models. EmailField (unique=True) 
    student_age = models. IntegerField (default=18) 
    student_address = models. TextField() 

    def str_(self) -> str: 
        return self.student_name 
    

    class Meta: 
        ordering = ['student_name'] 
        verbose_name = "student"