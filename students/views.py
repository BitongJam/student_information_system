from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from . models import Students
from .forms import StudentsForm

def students(request):
    # Handle form submission
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data if valid
            return redirect('students')  # Redirect to the same page or a success page
    
    else:
        form = StudentsForm()  # Create a new, empty form instance

    # Retrieve all students for display
    students_list = Students.objects.all().values()
    
    # Prepare context with the form and students data
    context = {
        'form': form,
        'students': students_list
    }

    # Render the template
    return render(request, 'index.html', context)

def details(request,id):
    student = Students.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'student' : student
    }

    return HttpResponse(template.render(context,request))

def save(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            # Get the cleaned data from the form
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']

            # Combine fname and lname into a single name field
            name = f'{fname} {lname}'  # Combine first and last names

            # Create and save a new Student object with the combined name
            student = Students(name=name)
            student.save()  # Save the student to the database

            return redirect('student_app:students')  # Redirect to the students list or another page

    else:
        form = StudentsForm()  # Display an empty form for GET requests

    return render(request, 'student_form.html', {'form': form})


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())