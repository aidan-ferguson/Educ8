from django.urls import path
from Educ8 import views

app_name = 'Educ8'

urlpatterns = [
    path('', views.index, name='index'),
]