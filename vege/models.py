from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Recipie(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)#if user deleted then all its recipies will be deleted 
    r_name=models.CharField(max_length=100)
    r_des=models.TextField()
    r_image=models.ImageField(upload_to="recipies/")

