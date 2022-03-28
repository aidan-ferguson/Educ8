from http import client
from tkinter.messagebox import QUESTION
from turtle import title
from django.test import TestCase
from Educ8.decorators import is_student, is_teacher
from Educ8.forms import FlashcardForm
from Educ8.models import Course
from django.urls import reverse
from Educ8.models import Flashcard
from Educ8.models import Account
from django.test import Client
from Educ8.models import CourseFile
from django.core.files import File

### Method Tests ###

class CourseMethodTests(TestCase):

    def test_slug_line_creation(self):

        course = Course(courseName='Example Course')
        course.save()

        self.assertEqual(course.slug, 'example-course')
    
class AccountMethodTests(TestCase):
    def test_account_is_not_both_student_and_teacher(self):

        account = Account(is_student=True, is_teacher=True)
        account.save()

        self.assertFalse(account.is_student and account.is_teacher)

### View Tests ###

class IndexViewTests(TestCase):

    def test_index_view(self):

        response = self.client.get(reverse('Educ8:index'))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Welcome to Educ8')
        self.assertContains(response, 'The Greatest Online Learning Platform (GOLP)')
        self.assertContains(response, 'Login')
        self.assertContains(response, 'Register')

class RegisterViewTests(TestCase):

    def test_register_view(self):

        response = self.client.get(reverse('Educ8:forms/register'))
        self.assertEqual(response.status_code, 200)
        
        self.assertContains(response, 'Create an Account')
        self.assertContains(response, 'Forename(s):')
        self.assertContains(response, 'Surname(s):')
        self.assertContains(response, 'Username:')
        self.assertContains(response, 'Create a Password:')
        self.assertContains(response, 'Confirm Password:')
        self.assertContains(response, 'I am a...')
        self.assertContains(response, 'Student')
        self.assertContains(response, 'Teacher')

class LoginViewTests(TestCase):

    def test_login_view(self):

        response = self.client.get(reverse('Educ8:forms/login'))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Login')
        self.assertContains(response, 'Username:')
        self.assertContains(response, 'Password:')
        self.assertContains(response, 'I am a...')
        self.assertContains(response, 'Student')
        self.assertContains(response, 'Teacher')
        self.assertContains(response, "Don't have an account? Register")

class TermsViewTests(TestCase):

    def test_terms_view(self):
        
        response = self.client.get(reverse('Educ8:terms'))
        self.assertEqual(response.status_code, 200)

class MyCoursesViewTests(TestCase):

    def test_with_no_courses(self):

        user = Account.objects.get_or_create(username = 'teststudent', first_name = "student", is_student = True)[0]
        user.save()

        self.client.force_login(user)

        response = self.client.get(reverse('Educ8:my_courses'))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "student's Courses")
        self.assertContains(response, "You are not enrolled in any courses.")

        self.assertEqual(response.context.get('courses', []), [])
    
    def test_with_course(self):

        user = Account.objects.get_or_create(username = 'teststudent', first_name = "student", is_student = True)[0]
        user.save()

        course = Course.objects.get_or_create(courseName = "testcourse")[0]
        course.students.add(user)
        course.save()

        self.client.force_login(user)

        response = self.client.get(reverse('Educ8:my_courses'))
        self.assertEqual(response.status_code, 200)
        
        self.assertContains(response, "student's Courses")
        self.assertContains(response, "testcourse")
        
        self.assertEqual(response.context['courses'][0].courseName, 'testcourse')

class ShowCourseViewTests(TestCase):

    def test_empty(self):

        user = Account.objects.get_or_create(username = 'teststudent', first_name = "student", is_student = True)[0]
        user.save()

        course = Course.objects.get_or_create(courseName = "testcourse")[0]
        course.students.add(user)
        course.save()

        self.client.force_login(user)

        response = self.client.get(reverse('Educ8:show_course', kwargs={'course_name_slug' : "testcourse"}))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "No files have been added to this course yet.")

        self.assertQuerysetEqual(response.context['files'], [])
        self.assertQuerysetEqual(response.context['flashCards'], [])

    def test_with_file(self):

        user = Account.objects.get_or_create(username = 'teststudent', first_name = "student", is_student = True)[0]
        user.save()

        course = Course.objects.get_or_create(courseName = "testcourse")[0]
        course.students.add(user)
        course.save()

        courseFile = CourseFile(course=course)
        courseFile.file.save('why_crochet_sucks', File(open('static/population_files/why_crochet_sucks.docx', 'rb')))
        courseFile.save()

        self.client.force_login(user)

        response = self.client.get(reverse('Educ8:show_course', kwargs={'course_name_slug' : "testcourse"}))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "why_crochet_sucks")

        self.assertIn('why_crochet_sucks', response.context['files'][0].filename())
        self.assertQuerysetEqual(response.context['flashCards'], [])
    
    def test_with_flashcard(self):

        user = Account.objects.get_or_create(username = 'teststudent', first_name = "student", is_student = True)[0]
        user.save()

        course = Course.objects.get_or_create(courseName = "testcourse")[0]
        course.students.add(user)
        course.save()

        Flashcard.objects.get_or_create(title = "test", question = "test?", answer = "passed", course = course, createdBy = user)[0]
        
        self.client.force_login(user)

        response = self.client.get(reverse('Educ8:show_course', kwargs={'course_name_slug' : "testcourse"}))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "test")

        self.assertQuerysetEqual(response.context['files'], [])
        self.assertEqual('test', response.context['flashCards'][0].title)

    def test_with_both(self):

        user = Account.objects.get_or_create(username = 'teststudent', first_name = "student", is_student = True)[0]
        user.save()

        course = Course.objects.get_or_create(courseName = "testcourse")[0]
        course.students.add(user)
        course.save()

        courseFile = CourseFile(course=course)
        courseFile.file.save('why_crochet_sucks', File(open('static/population_files/why_crochet_sucks.docx', 'rb')))
        courseFile.save()

        Flashcard.objects.get_or_create(title = "test", question = "test?", answer = "passed", course = course, createdBy = user)[0]

        self.client.force_login(user)

        response = self.client.get(reverse('Educ8:show_course', kwargs={'course_name_slug' : "testcourse"}))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "why_crochet_sucks")
        self.assertContains(response, "test")

        self.assertIn('why_crochet_sucks', response.context['files'][0].filename())
        self.assertEqual('test', response.context['flashCards'][0].title)

class AddCourseViewTests(TestCase):
    
    def test_add_course_view(self):

        user = Account.objects.get_or_create(username = 'testteacher', first_name = "teacher", is_teacher = True)[0]
        user.save()

        self.client.force_login(user)

        response = self.client.get(reverse('Educ8:forms/add_course'))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Create a Course")
        self.assertContains(response, "Course Name:")

class DeleteCourseViewTests(TestCase):

    def test_delete_course_view(self):

        pass

