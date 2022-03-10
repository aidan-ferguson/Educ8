from django.db import models
from django.contrib.auth.models import User


"""
Things to do:
    Create a function which checks if a Student exists.
    Create a function which checks if a Teacher exists.
    Get someone to check everything.
"""

MINIMUM_LENGTH = 4
MAX_LENGTH_USERNAME = 32

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
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, min_length=MINIMUM_LENGTH, max_length=MAX_LENGTH_USERNAME)

    def __str__(self):
        return self.user.username

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
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, min_length=MINIMUM_LENGTH, max_length=MAX_LENGTH_USERNAME)

    def __str__(self):
        return self.user.username


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
    createdBy = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.courseName
    
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
    title = models.CharField(max_length=128)
    question = models.CharField(max_length=1024)
    answer = models.CharField(max_length=1024)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    createdBy = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

"""
    Method for generating filepaths based on the course they are uploaded to
"""
def generate_file_path(instance, filename):
    return f'files/{instance.course.courseName}/{filename}'

class CourseFile(models.Model):
    """CourseFile class: This is a model for the File table in the database

    Attributes:
        file (FileField): This will hold the file which will be uploaded to the media directory (access this in templates using Object.file.url for the absolute URL)
        course (ForeignKey): Holds the foreign key to the course which the files have been uploaded to
    """

    file = models.FileField(upload_to=generate_file_path)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
