from django.test import TestCase
from Educ8.models import Course
from django.urls import reverse


class CourseMethodTests(TestCase):
    def test_slug_line_creation(self):
        
        course = Course(courseName='Example Course')
        course.save()
        
        self.assertEqual(course.slug, 'example-course')

class IndexViewTests(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('Educ8:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to Educ8')
        self.assertContains(response, 'The Greatest Online Learning Platform (GOLP)')
        self.assertContains(response, 'Login')
        self.assertContains(response, 'Register')