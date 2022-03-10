
from dataclasses import fields
from pyexpat import model
from stat import FILE_ATTRIBUTE_NOT_CONTENT_INDEXED
from django import forms 
from Educ8.models import Teacher, Student, Course, Flashcard, CourseFile
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


class CourseForm(forms.ModelForm):
    courseName = forms.CharField(max_length=128)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Course
        fields = ('courseName',)


class FlashcardForm(forms.ModelForm):
    title = forms.CharField(max_length=32)
    question = forms.CharField(max_length=256)
    answer = forms.CharField(max_length=256)

    class Meta:
        model = Flashcard
        fields = ('title', 'question', 'answer')
        
class CourseFileForm(forms.ModelForm):
    file = forms.FileField()

    class Meta:
        model = CourseFile
        fields = ('file', 'course')