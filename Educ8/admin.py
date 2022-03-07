from django.contrib import admin

from Educ8.models import Teacher, Student, Course, Flashcard, CourseFile

# Register following models with the admin interface
# TO_REGISTER = [Teacher, Student, Course, CourseFile, Flashcard]
# list(map(lambda x: admin.site.register(x), TO_REGISTER))

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(CourseFile)
admin.site.register(Flashcard)