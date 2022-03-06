from django.contrib import admin

from Educ8.models import Teacher, Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')

admin.site.register(Teacher)
admin.site.register(Student, StudentAdmin)