from django.contrib import admin

from Educ8.models import Teacher, Student, Course, Flashcard

# Register following models with the admin interface
TO_REGISTER = [Teacher, Student, Course, Flashcard]
list(map(lambda x: admin.site.register(x), TO_REGISTER))

class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')