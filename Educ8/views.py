from xml.dom.domreg import registered
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect
from Educ8.forms import CourseForm, FlashcardForm, TeacherForm, StudentForm, FileForm
from datetime import datetime
from Educ8.models import Course
from Educ8.models import Flashcard
from Educ8.models import CourseFile

def index(request):

    """calls cookie handling function,
    renders a response template."""

    visitor_cookie_handler(request)
    response = render(request, 'Educ8/index.html')
    return response

@login_required
def my_courses(request):
    context_dict = {}

    form = StudentForm()
    if request.method == 'GET':
        form = StudentForm(request.GET)

        if form.is_valid():
            student = form.save()
            course_list = []
            for course in Course.objects.get():
                if student.username in course.students:
                    course_list.append(course)
            context_dict['courses'] = course_list

    return render(request, 'Educ8/my_courses.html', context=context_dict)


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

@login_required
def add_files(request, course_name_slug):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        print("here")
        if form.is_valid():
            print("here2")
            course = Course.objects.get(slug=course_name_slug)
            # course_file = CourseFile(course=course)
            print(type(request.FILES['file']))
            # course_file.file.save(filename, File(open(f'static/population_files/{filename}', 'rb')))
            # course_file.save()
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

    try:
        course = Course.objects.get(slug=course_name_slug)
    except Course.DoesNotExist:
        course = None

    if course is None:
        return redirect('/Educ8/')

    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            if course:
                student = form.save(commit=False)
                student.course = course
                student.save()

                return redirect('/Educ8/')

        else:
            print(form.errors)

    return render(request, 'Educ8/add_students.html', {'form' : form})


def register(request):

    """view to register a student/teacher,
    check if the form is valid and
    direct them to the signup page
    """

    registered = False

    if request.method == 'POST':
        userType = request.POST.get('user_type')
        if userType == 'teacher':

            teacher_form = TeacherForm(request.POST)


            if teacher_form.is_valid():
                student = teacher_form.save()
                student.set_password(student.password)
                student.save()

                registered = True
            else:
                print(teacher_form.error_class)

        elif userType == 'student':

            student_form = StudentForm(request.POST)


        if student_form.is_valid():
            student = student_form.save()
            student.set_password(student.password)
            student.save()

            registered = True
        else:
            print(student_form.error_class)


    else:
        teacher_form = TeacherForm()
        student_form = StudentForm()

    return render(request, 'Educ8/forms/register.html', context={'registered' : registered})


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
def logout(request):
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
