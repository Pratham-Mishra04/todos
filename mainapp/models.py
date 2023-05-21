from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class CompleteUser(models.Model):
    
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    age=models.IntegerField()

    def __str__(self):
        return self.user.name

class Userdata(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=100)
    status=models.CharField(max_length=10)
    box_status=models.CharField(max_length=20,null=True)
    due_time=models.TimeField(default=datetime.datetime.now())
    due_date=models.DateField(default=datetime.datetime.now().time())
    
    def __str__(self):
        return str(self.user)