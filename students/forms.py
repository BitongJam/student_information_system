from django import forms

class StudentsForm(forms.Form):
    fname = forms.CharField(max_length=100,label='First Name')
    lname = forms.CharField(max_length=100,label='Last Name')