from cgi import test
from xml.dom.domreg import registered
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.template.defaultfilters import slugify
from datetime import datetime
from Educ8.forms import CourseForm, FlashcardForm, AccountForm, CourseFileForm
from Educ8.models import Course, Flashcard, CourseFile, Account
from Educ8.decorators import is_teacher, is_student

def index(request):

    """calls cookie handling function,
    renders a response template."""

    visitor_cookie_handler(request)
    response = render(request, 'Educ8/index.html')
    return response


# Method for getting all of the courses a student is enrolled into
# and then returns the list to the my_courses page.
@login_required
def my_courses(request):
    context_dict = {}

    # This took too long
    courses = Course.objects.filter(students__username='Dom1')
    if len(courses) > 0:
        context_dict["courses"] = []
        for course in courses:
            context_dict["courses"].append(course)

    # TODO
    # form = StudentForm()
    # if request.method == 'GET':
    #     form = StudentForm(request.GET)

    #     if form.is_valid():
    #         student = form.save()
    #         course_list = []
    #         for course in Course.objects.get():
    #             if student.username in course.students:
    #                 course_list.append(course)
    #         context_dict['courses'] = course_list

    return render(request, 'Educ8/my_courses.html', context=context_dict)

#Method for getting all of the flashcards and files for a single course
#and then returning them to "course"
@login_required
def show_course(request, course_name_slug):
    context_dict = {}

    try:
        course = Course.objects.get(slug=course_name_slug)
        flashCards = Flashcard.objects.get(course=course)
        files = CourseFile.objects.filter(course=course)
        context_dict['files'] = files
        context_dict['flashCards'] = flashCards
        context_dict['course'] = course
    except Course.DoesNotExist:
        context_dict['course'] = None
        context_dict['flashCards'] = None
        context_dict['files'] = None

    return render(request, 'Educ8/course.html', context=context_dict)

#method for allowing a teacher to create a course
@login_required
def add_course(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/Educ8/')
        else:
            print(form.errors)

    return render(request, 'rango/add_course.html', {'form' : form})

# TODO: Error handling, max file size?
@login_required
@user_passes_test(is_teacher)
def add_files(request, course_name_slug):
    if request.method == 'POST':
        form = CourseFileForm(request.POST, request.FILES)
        if form.is_valid():
            course = Course.objects.get(slug=course_name_slug)
            course_file = CourseFile(course=course)
            file = request.FILES['file']
            course_file.file.save(file.name, file)
            course_file.save()
            return redirect(f'/Educ8/my_courses/{course_name_slug}')
    return render(request, 'Educ8/forms/add_files.html')

@login_required
def add_or_edit_flashcard(request, course_name_slug):
    try:
        course = Course.objects.get(slug=course_name_slug)
    except Course.DoesNotExist:
        course = None

    if course is None:
        return redirect('/Educ8/')

    form = FlashcardForm()

    if request.method == 'POST':
        form = FlashcardForm(request.POST)

        if form.is_valid():
            if course:
                flashCard = form.save(commit=False)
                flashCard.course  = course
                flashCard.views = 0
                flashCard.save()

                return redirect(reverse('Educ8:show_course', kwargs={'course_name_slug' : course_name_slug}))

        else:
            print(form.errors)

    context_dict = {'form' : form, 'course' : course}
    return render(request, 'Educ8/add_or_edit_flashcard.html', context=context_dict)

@login_required
def show_flashcard(request, course_name_slug, flashcardID):
    context_dict={}
    try:
        course = Course.objects.get(slug=course_name_slug)
        flashcard = Course.objects.get(slug=flashcardID)
        context_dict['flashCards'] = flashcard
        context_dict['course'] = course
    except Course.DoesNotExist:
        course = None
        flashcard = None
        context_dict['flashCards'] = None
        context_dict['course'] = None
    return render(request, 'Educ8/course/flashCards', context=context_dict)

def add_students(request, course_name_slug):

    """conditional to check course exists.
    code to add students to specific courses"""
    # Will be useful for querying current students:
    # test1 = Account.objects.filter(course__)
    
    # TODO
    # try:
    #     course = Course.objects.get(slug=course_name_slug)
    # except Course.DoesNotExist:
    #     course = None

    # if course is None:
    #     return redirect('/Educ8/')

    # form = StudentForm()

    # if request.method == 'POST':
    #     form = StudentForm(request.POST)

    #     if form.is_valid():
    #         if course:
    #             student = form.save(commit=False)
    #             student.course = course
    #             student.save()

    #             return redirect('/Educ8/')

    #     else:
    #         print(form.errors)

    # return render(request, 'Educ8/add_students.html', {'form' : form})

# Need to verify passwords are the same and return any form errors
def register(request):

    """view to register a student/teacher,
    check if the form is valid and
    direct them to the signup page
    """

    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        form = AccountForm(request.POST)
        if form.is_valid() and user_type in ['student', 'teacher']:
            user = None
            if user_type == 'student':
                user = form.save(is_student=True)
            elif user_type == 'teacher':
                user = form.save(is_teacher=True)

            # Now user has been created, login and redirect to home page
            login(request, user)

            return redirect(reverse('Educ8:index'))
        else:
            print(form.errors.as_data())

    return render(request, 'Educ8/forms/register.html')

# Can we pass the 'next' GET variable to the register view?
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('Educ8:index'))
            else:
                return HttpResponse("Your Educ8 account is disabled.")

        else:
            print(f"Invalid login detals: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'Educ8/forms/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('Educ8:index'))

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
    request.session['visits'] = visits


def terms(request):
    return render(request, "Educ8/terms.html")

# HTTP 404 Error (Page not found)
def page_not_found(request, exception):
    return render(request, "Educ8/404.html")
