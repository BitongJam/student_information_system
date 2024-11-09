from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('students/', views.students, name='Students'),
    path('students/details/<int:id>', views.details, name='Details'),
]