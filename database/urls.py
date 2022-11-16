from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.database_student, name = 'database' ),
]
