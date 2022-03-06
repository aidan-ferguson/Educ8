from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime

def index(request):
    response = render(request, 'rango/index.html')
    visitor_cookie_handler(request, response)
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

@login_required
def add_student(request, course_name_slug):
    pass

def register(request):
    pass

def user_login(request):
    pass

def restricted(request):
    pass

@login_required
def logout(request):
    pass

def visitor_cookie_handler(request, response):
    visits = int(request.COOKIES.get('visits', '1'))
    last_visit_cookie = request.COOKIES.get('last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
    '%Y-%m-%d %H:%M:%S')
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        response.set_cookie('last_visit', str(datetime.now()))
    else:
        response.set_cookie('last_visit', last_visit_cookie)
    response.set_cookie('visits', visits)