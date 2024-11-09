from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import Students

def students(request):
    students_list = Students.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'students' : students_list
    }
    return HttpResponse(template.render(context,request))

def details(request,id):
    student = Students.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'student' : student
    }

    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())