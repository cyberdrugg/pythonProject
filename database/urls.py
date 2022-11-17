from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.database_student, name = 'database' ),
    path('student_detail/<int:id>/', views.student_detail, name='student_detail'),
]
