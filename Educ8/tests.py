from django.test import TestCase
from Educ8.models import Course

class CourseMethodTests(TestCase):
    def test_slug_line_creation(self):
        
        course = Course(courseName='Example Course')
        course.save()
        
        self.assertEqual(course.slug, 'example-course')
        
    def test_created_by_someone(self):
        
        course = Course(createdBy=)
        