
from dataclasses import fields
from pyexpat import model
from django import forms 
from Educ8.models import Teacher, Student, Course, Flashcard
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')
        

class TeacherForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')
