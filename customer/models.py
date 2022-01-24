from django.db import models

# Create your models here.
class customermodels(models.Model):
    cname=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.BigIntegerField()
    dob=models.DateField()
    li=[['Male','MALE'],['Female','FEMALE']]
    gender=models.CharField(max_length=15, choices=li)
    password=models.CharField(max_length=50)
    dor=models.DateTimeField()
