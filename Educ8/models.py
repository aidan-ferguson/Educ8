from django.db import models
from django.contrib.auth.models import User

"""
Things to do:
    Create a function which checks if a Student exists.
    Create a function which checks if a Teacher exists.
    Get someone to check everything.
"""


class Teacher(models.Model):
    """Teacher class: This is a model for our Teacher table in our database.

    Attributes:
        username (str): This is the username of the Teacher.
        password (str): This is the password of the Teacher.
        first_name (str): This is the first name of the Teacher.
        last_name (str): This is the last name of the Teacher.

    Methods:
    __str__ : Returns the username of the Teacher. This makes debugging easier.
    """
    username = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True, unique=True)

    def __str__(self):
        return self.username

class Student(models.Model):
    """Student class: This is a model for our Student table in our database.

    Attributes:
        username (str): This is the username of the Student.
        password (str): This is the password of the Student.
        first_name (str): This is the first name of the Student.
        last_name (str): This is the last name of the Student.

    Methods:
    __str__ : Returns the username of the Student. This makes debugging easier.
    """
    username = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True, unique=True)
    
    def __str__(self):
        return self.username

class Flashcard(models.Model):
    """Flashcard class: This is a model for our Flashcard table in our database.

    Attributes:
        title (str): This is the title of the Flashcard.
        question (str): This is the question of the Flashcard.
        answer (str): This is the answer of the Flashcard.
        createdBy (str): This is the username of the Student who created the Flashcard.
        Course (str): This is the Course of the Student, for which this Flashcard belongs to.

    Methods:
    __str__ : Returns the title of the Flashcard. This makes debugging easier.
    """
    title = models.CharField(max_length=32, primary_key=True, unique=True)
    question = models.CharField(max_length=256)
    answer = models.CharField(max_length=256)
    createdBy = models.ForeignKey(Student, on_delete=models.CASCADE)
    Course = models.CharField(Student, max_length=256)

    def __str__(self):
        return self.title

class Course(models.Model):
    """Course class: This is a model for our Course table in our database.

    Attributes:
        courseName (str): This is the name of the Course.
        createdBy (str): This is the username of the Teacher that created the Course.
        students (list of strings): This is a list of the usernames of the Students that have been enrolled on the Course.

    Methods:
    __str__ : Returns the name of the Course. This makes debugging easier.
    """
    courseName = models.CharField(max_length=256, primary_key=True)
    createdBy = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.courseName