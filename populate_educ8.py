import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_group_project.settings')

import django
django.setup()

from django.contrib.auth.models import User
from Educ8.models import Student, Teacher, Course, Flashcard

"""
Things to do:
    Comment functions.
    Create 4 loops for filling database in populate().
    Get someone to check everything.
"""

def populate() -> None:
    """ student = [{"username":'Dom1', "password":"Password", "first_name":"Dom", "last_name":"Jina"},
               {"username":'Dom2', "password":"Password", "first_name":"Dom", "last_name":"Jina"},
               {"username":'Dom3', "password":"Password", "first_name":"Dom", "last_name":"Jina"},
               {"username":'Dom4', "password":"Password", "first_name":"Dom", "last_name":"Jina"}]

    Teacher = [{"username":"Bob1", "password":"Password", "first_name":"Dom", "last_name":"Jina"},
               {"username":"Bob2", "password":"Password", "first_name":"Dom", "last_name":"Jina"},
               {"username":"Bob3", "password":"Password", "first_name":"Dom", "last_name":"Jina"},
               {"username":"Bob4", "password":"Password", "first_name":"Dom", "last_name":"Jina"}]

    Course = [{"courseName":"Maths", "createdBy":"Bob1", "students":[]}]

    Flashcard = [{"title":"addition1", "question":"What is 1 + 1?", "answer": "2", "createdBy":"Dom1", "Course":"Maths"}] """

    students = {"Dom1": {"password":"Password", "first_name":"Dom", "last_name":"Jina", "object":None},
                "Dom2": {"password":"Password", "first_name":"Dom", "last_name":"Jina", "object":None},
                "Dom3": {"password":"Password", "first_name":"Dom", "last_name":"Jina", "object":None},
                "Dom4": {"password":"Password", "first_name":"Dom", "last_name":"Jina", "object":None}}

    teachers = {"Bob1" : {"password":"Password", "first_name":"Dom", "last_name":"Jina", "object":None},
                "Bob2" : {"password":"Password", "first_name":"Dom", "last_name":"Jina", "object":None},
                "Bob3" : {"password":"Password", "first_name":"Dom", "last_name":"Jina", "object":None},
                "Bob4" : {"password":"Password", "first_name":"Dom", "last_name":"Jina", "object":None}}

    courses = {"Maths" : {"createdBy":"Bob1", "students":[]},
               "Extreme Cake Baking" : {"createdBy":"Bob3", "students":[]},
               "English" : {"createdBy":"Bob4", "students":[]}}

    Flashcard = [{"title":"addition1", "question":"What is 1 + 1?", "answer": "2", "createdBy":"Dom1", "Course":"Maths"}]

    for student, student_data in students.items():
        student_data["object"] = add_student(student, student_data["password"], student_data["first_name"], student_data["last_name"])

    for teacher, teacher_data in teachers.items():
        teacher_data["object"] = add_teacher(teacher, teacher_data["password"], teacher_data["first_name"], teacher_data["last_name"])

    for course, course_data in courses.items():
        # We access the actual object of the teacher so it can link to the teacher in the database 
        print(teachers[course_data["createdBy"]]["object"])
        add_course(course, teachers[course_data["createdBy"]]["object"], course_data["students"])
    
    """
    for flashcards, flashcard_data in Flashcard:
        add_flashcard(flashcards, flashcard_data["question"], flashcard_data["answer"], flashcard_data["createdBy"], flashcard_data["Course"]) """

def add_student(Username: str, Password: str, first_name: str, last_name: str) -> object:
    user = User.objects.get_or_create(username=Username,
                                    first_name = first_name,
                                    last_name = last_name,
                                    password = Password)[0]
    s = Student.objects.get_or_create(user=user)[0]
    return s

def add_teacher(Username: str, Password: str, first_name: str, last_name: str) -> object:
    user = User.objects.get_or_create(username=Username,
                            first_name = first_name,
                            last_name = last_name,
                            password = Password)[0]
    t = Teacher.objects.get_or_create(user=user)[0]
    return t


def add_course(CourseName: str, createdBy: object, studentsToAdd: list) -> object:
    c = Course.objects.get_or_create(courseName=CourseName, createdBy=createdBy)[0]
    for student in studentsToAdd:
        c.students.add(student)
    c.save()
    return c

"""
def add_flashcard(title: str, question: str, answer: str, createdBy: str, Course: str) -> object:
    f = Flashcard.objects.create(title=title, createdBy=createdBy, Course=Course)
    f.question = question
    f.answer = answer
    f.save()
    return f """


if __name__ == '__main__':
    print('Starting Educ8 population script...')
    populate()
