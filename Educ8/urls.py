from django.urls import path
from Educ8 import views

app_name = 'Educ8'

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/<slug:course_name_slug>/',
         views.show_course, name='show_course'),
    path('courses/add_course/',
         views.add_course, name='add_course'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    
]