from Educ8.models import Course
from django.shortcuts import render
from django.utils.text import slugify

def is_student(user):
    return user.is_active and user.is_student

def is_teacher(user):
    return user.is_active and user.is_teacher

def can_access_course(wrapped_function):
    def wrap(request, *args, **kwargs):
        # Check if the current user can see the available course
        try:
            course = Course.objects.get(slug=slugify(kwargs['course_name_slug']))
        except Course.DoesNotExist:
            return internal_server_error(request, "That course does not exist")

        user_enrolled_in_course = request.user in course.students.all()
        user_created_course = request.user == course.createdBy

        if user_created_course or user_enrolled_in_course:
            # User can access course, so return the view function
            return wrapped_function(request, *args, **kwargs)
        else:
            return resource_forbidden(request)
    return wrap

# The reason these views are in here is because there was a circular dependancy between views and decorators

# For 500 server errors (mainly for database not found errors)
def internal_server_error(request, exception):
    response = render(request, "Educ8/500.html", context={"error_message":exception})
    response.status_code = 500
    return response

# For 403 server errors (mainly for database not found errors)
def resource_forbidden(request):
    response = render(request, "Educ8/403.html")
    response.status_code = 403
    return response