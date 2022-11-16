

from django.shortcuts import render
from django.template import context

from database import models


# Create your views here.

def database_student(request):
    data = models.Student.objects.all()
    return render(request, 'index.html',{'data':data})

