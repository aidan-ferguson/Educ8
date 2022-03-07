from xml.dom.domreg import registered
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Educ8.forms import TeacherForm, StudentForm
from datetime import datetime

def index(request):
    visitor_cookie_handler(request)
    response = render(request, 'Educ8/index.html')
    return response

@login_required
def courses(request):
    pass

@login_required
def show_course(request, course_name_slug):
    pass

@login_required
def add_course(request):
    pass

@login_required
def add_file(request, course_name_slug):
    pass

@login_required
def add_or_edit_flashcard(request, course_name_slug):
    pass

@login_required
def show_flashcard(request, course_name_slug, flashcardID):
    pass

def add_student(request, course_name_slug):
    pass

def register(request):

    """view to register a student, 
    check if the form is valid and 
    direct them to the signup page
    """

    registered = False
    
    # if user selects student:

    if request.method == 'POST':
        student_form = StudentForm(request.POST)
    

        if student_form.is_valid():
            student = student_form.save()
            student.set_password(student.password)
            student.save()

            registered = True
        else:
            print(student_form.error_class)

    else:
        student_form = StudentForm()

    return render(request, 'Educ8/signup.html', context={'student_form' : student_form, 'registered' : registered})

    # else if user selects teacher:

    """
    if request.method == 'POST':
        teacher_form = TeacherForm(request.POST)
    

        if teacher_form.is_valid():
            student = teacher_form.save()
            student.set_password(student.password)
            student.save()

            registered = True
        else:
            print(teacher_form.error_class)

    else:
        teacher_form = TeacherForm()

    return render(request, 'Educ8/signup.html', context={'teacher_form' : teacher_form, 'registered' : registered})
    """

def user_login(request):
    pass

def restricted(request):
    pass

@login_required
def logout(request):
    pass

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