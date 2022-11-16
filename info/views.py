from django.shortcuts import render

from info import models


# Create your views here.

def profile(request):
    profile = models.Profile.objects.all()
    return render(request, 'info.html',{'profile':profile})

