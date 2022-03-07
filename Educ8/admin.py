from django.contrib import admin

from Educ8.models import Teacher, Student, Course, Flashcard, CourseFile

class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')

# Register following models with the admin interface
TO_REGISTER = [Teacher, Student, StudentAdmin, Course, CourseFile, Flashcard]
list(map(lambda x: admin.site.register(x), TO_REGISTER))

