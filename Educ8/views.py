from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Educ8 says aight!")

def home(request):
    pass

def show_course(request, category_name_slug):
    pass

def add_course(request):
    pass

def add_flashcard(request):
    pass


