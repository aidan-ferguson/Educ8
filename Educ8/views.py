from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Educ8 says aight!")