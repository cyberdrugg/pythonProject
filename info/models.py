from django.db import models

# Create your models here.
class Profile(models.Model):
    subject = models.CharField(max_length=50, null=True)
    semestr1 = models.CharField(max_length=50, null=True)
    semestr2 = models.CharField(max_length=50, null=True)
    average = models.CharField(max_length=50, null=True)



