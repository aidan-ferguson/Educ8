from multiprocessing.sharedctypes import Value
from django.db import models
from django.contrib.auth.models import AbstractUser#, BaseUserManager
from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify
import os

MINIMUM_LENGTH = 4
MAX_LENGTH_USERNAME = 32

"""
    We need to have a user manager for the account model because we have custom fields and
    need to access the .set_password() method in AbstractBaseUser, this is used in the population script
"""
"""class AccountManager(BaseUserManager):
    def create_user(self, username, is_teacher, is_student, password=None):
        if not is_teacher and not is_student:
            raise ValueError("Users must be a teacher or a student")

        user = self.model(username, is_teacher, is_student)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, is_teacher, is_student, password=None):
        user = self.create_user(username, is_teacher, is_student,
            password
        )
        user.is_admin = True
        user.save()
        return user"""

class Account(AbstractUser):
    # We have both boolean flags so that the code is easier to read
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if self.is_teacher and self.is_student:
            self.is_teacher = False
            self.is_student = False
        super(Account, self).save(*args, **kwargs)    
            

    def __str__(self):
        return self.username


class Course(models.Model):
    """Course class: This is a model for our Course table in our database.

    Attributes:
        courseName (str): This is the name of the Course.
        createdBy (str): This is the username of the Teacher that created the Course.
        students (list of strings): This is a list of the usernames of the Students that have been enrolled on the Course.
        sluf (slug field): slugifies the field name

    Methods:
    __str__ : Returns the name of the Course. This makes debugging easier.
    """
    courseName = models.CharField(max_length=256, primary_key=True, validators=[MinLengthValidator(4)])
    createdBy = models.ForeignKey(Account, related_name='course_creator', on_delete=models.CASCADE, null=True)
    students = models.ManyToManyField(Account, related_name='course')
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.courseName)
        super(Course, self).save(*args, **kwargs)

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
    title = models.CharField(max_length=128,validators=[MinLengthValidator(1)])
    question = models.CharField(max_length=1024, validators=[MinLengthValidator(1)])
    answer = models.CharField(max_length=1024, validators=[MinLengthValidator(1)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    createdBy = models.ForeignKey(Account, related_name='flashcard_creator', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

"""
    Method for generating filepaths based on the course they are uploaded to
"""
def generate_file_path(instance, filename):
    return f'files/{instance.course.slug}/{filename}'

class CourseFile(models.Model):
    """CourseFile class: This is a model for the File table in the database

    Attributes:
        file (FileField): This will hold the file which will be uploaded to the media directory (access this in templates using Object.file.url for the absolute URL)
        course (ForeignKey): Holds the foreign key to the course which the files have been uploaded to
    """

    file = models.FileField(upload_to=generate_file_path)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def filename(self):
        return os.path.basename(self.file.name)
