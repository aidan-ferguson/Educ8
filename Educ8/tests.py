from http import client
from django.test import TestCase
from Educ8.models import Course
from django.urls import reverse
from Educ8.models import Flashcard
from Educ8.models import Account
from django.test import Client

### method tests ###
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
        
### view tests ###
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

class MyCoursesViewTest(TestCase):
    def test_with_no_courses(self):
        self.client.force_login(Account.objects.get_or_create(username='testuser', first_name="test")[0])
        response = self.client.get(reverse('Educ8:my_courses'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test's Courses")
        self.assertContains(response, "You are not enrolled in any courses.")
    def test_with_courses(self):
        user = Account.objects.get_or_create(username='testuser', first_name="test")[0]
        user.save()
        c = Course.objects.get_or_create(courseName="testcourse")[0]
        c.students.add(user)
        c.save()
        self.client.force_login(user)
        response = self.client.get(reverse('Educ8:my_courses'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test's Courses")
        self.assertContains(response, "testcourse")
