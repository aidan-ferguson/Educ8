from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'Educ8/index.html') 

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
def add_flashcard(request, course_name_slug):
    pass

@login_required
def show_flashcard(request, flashcardID):
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

