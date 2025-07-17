from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.CharField(max_length=30)
    
class Student(models.Model):
    Student_name = models.CharField(max_length=50)
    Student_Subject = models.CharField(max_length=50)
    Student_Mark = models.IntegerField()
    
class Employee(models.Model):
    first_name =models.CharField(max_length=50)
    last_name  =models.CharField(max_length=20)
    email      =models.CharField(max_length=20)
    department =models.CharField(max_length=50)
    salary     =models.IntegerField()
    
class product(models.Model):
    name             = models.CharField(max_length=50)
    category         = models.CharField(max_length=20)
    price            = models.IntegerField()
    stock_quantity   = models.IntegerField()
    description      = models.TextField(max_length=100)
   

    
    
    
    