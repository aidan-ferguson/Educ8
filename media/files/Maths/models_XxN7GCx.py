from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    username = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)

    def __str__(self):
        return self.username

class Student(models.Model):
    username = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    
    def __str__(self):
        return self.username

class Flashcard(models.Model):
    title = models.CharField(max_length=32, primary_key=True)
    question = models.CharField(max_length=256)
    answer = models.CharField(max_length=256)
    createdBy = models.ManyToManyField(Student)

class Course(models.Model):
    courseName = models.CharField(max_length=256, primary_key=True)
    createdBy = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    students = models.ManyToManyField(Student)