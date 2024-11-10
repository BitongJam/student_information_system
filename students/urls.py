from django.urls import path
from . import views

app_name = 'student_app'

urlpatterns = [
    path('', views.main, name='main'),
    path('students/', views.students, name='students'),
    path('student/save',views.save,name='save'),
    path('students/details/<int:id>', views.details, name='Details'),
]