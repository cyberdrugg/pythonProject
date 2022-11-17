from django.db import models


# Create your models here.

class Student(models.Model):
    image = models.ImageField(upload_to='', null=True)
    name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    point = models.CharField(max_length=50, null=True)
    group = models.CharField(max_length=100, null=True)

class Tabel(models.Model):
    subject = models.CharField(max_length=50, null=True)
    semestr1 = models.CharField(max_length=50, null=True)
    semestr2 = models.CharField(max_length=50, null=True)
    average = models.CharField(max_length=50, null=True)


