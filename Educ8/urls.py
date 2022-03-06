from django.urls import path
from Educ8 import views

app_name = 'Educ8'

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/',
         views.courses, name='courses'),
    path('courses/<slug:course_name_slug>/',
         views.show_course, name='show_course'),
    path('courses/add_course/',
         views.add_course, name='add_course'),
    path('course/<slug:course_name_slug>/add_file/',
         views.add_file, name='add_file'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.logout, name='logout'),
    
]