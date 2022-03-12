from base64 import standard_b64decode
from django.db import models
from django.forms import CharField

class Student(models.Model):
  name=models.CharField(max_length=40)
  standard = models.CharField(max_length=30,blank=True,default='not mention')
  email=models.EmailField()
  password=models.CharField(max_length=50)
  date=models.DateField(blank=True)

# Create your models here.
