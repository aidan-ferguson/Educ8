from django.urls import path
from Educ8 import views

app_name = 'Educ8'

urlpatterns = [ #Maps a url to its respective view and form
     path('', views.index, name='index'),
     path('my_courses/',
         views.my_courses, name='my_courses'),
     path('my_courses/<slug:course_name_slug>/',
         views.show_course, name='show_course'),
     path('add_course/',
         views.add_course, name='forms/add_course'),
     path('my_courses/<slug:course_name_slug>/add_file/',
         views.add_files, name='forms/add_files'),
     path('my_courses/<slug:course_name_slug>/add_or_edit_flashcard',
         views.add_or_edit_flashcard, name='forms/add_flashcard'),
     path('my_courses/<slug:course_name_slug>/add_or_edit_flashcard/<flashcard_id>',
         views.add_or_edit_flashcard, name='forms/edit_flashcard'),
     path('my_courses/<slug:course_name_slug>/delete_flashcard/<flashcard_id>',
         views.delete_flashcard, name='delete_flashcard'),
     path('my_courses/<slug:course_name_slug>/flashcard',
         views.show_flashcard, name='show_flashcard'),
     path('my_courses/<slug:course_name_slug>/students',
         views.edit_students, name='forms/edit_students'),
     path('register/', views.register, name='forms/register'),
     path('login/', views.user_login, name='forms/login'),
     path('logout/', views.user_logout, name='forms/logout'),
     path('terms/', views.terms, name='terms'),
     path('my_courses/<slug:course_name_slug>/flashcard/next_card/', views.next_card_ajax, name='next_card'),
     path('my_courses/<slug:course_name_slug>/students/add_student/', views.add_student_ajax, name='add_student'),
     path('my_courses/<slug:course_name_slug>/students/remove_student/', views.remove_student_ajax, name='remove_student'),
     path('my_courses/<slug:course_name_slug>/delete_file/<file_id>', views.delete_file, name='delete_file'),
     path('my_courses/<slug:course_name_slug>/delete_course', views.delete_course, name='forms/delete_course'),
]
