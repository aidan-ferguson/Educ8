from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime

def index(request):
    visitor_cookie_handler(request)
    response = render(request, 'rango/index.html')
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
    pass

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