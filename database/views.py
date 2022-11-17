from django.shortcuts import render, get_object_or_404
from django.template import context

from database import models


# Create your views here.

def database_student(request):
    data = models.Student.objects.all()
    return render(request, 'index.html', {'data': data})


def student_detail(request, id):
    data = get_object_or_404(models.Student, id=id)
    return render(request, 'info.html', {'data': data})


def tabel(request):
    tabel = get_object_or_404(models.Student, id=id)
    return render(request, 'info.html', {'tabel': tabel})
