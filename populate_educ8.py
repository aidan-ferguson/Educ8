import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_group_project.settings')

import django
django.setup()

from django.contrib.auth.models import User
from Educ8.models import Student, Teacher#, Course, Flashcard

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

    student = {"Dom1": {"password":"Password", "first_name":"Dom", "last_name":"Jina"},
               'Dom2': {"password":"Password", "first_name":"Dom", "last_name":"Jina"},
               'Dom3': {"password":"Password", "first_name":"Dom", "last_name":"Jina"},
               'Dom4': {"password":"Password", "first_name":"Dom", "last_name":"Jina"}}

    Teacher = [{"username":"Bob1", "password":"Password", "first_name":"Dom", "last_name":"Jina"},
               {"username":"Bob2", "password":"Password", "first_name":"Dom", "last_name":"Jina"},
               {"username":"Bob3", "password":"Password", "first_name":"Dom", "last_name":"Jina"},
               {"username":"Bob4", "password":"Password", "first_name":"Dom", "last_name":"Jina"}]

    Course = [{"courseName":"Maths", "createdBy":"Bob1", "students":[]}]

    Flashcard = [{"title":"addition1", "question":"What is 1 + 1?", "answer": "2", "createdBy":"Dom1", "Course":"Maths"}]

    for students, student_data in student.items():
        add_student(students, student_data["password"], student_data["first_name"], student_data["last_name"])

    """ for teacher, teacher_data in Teacher.items():
        add_teacher(teacher, teacher_data["password"], teacher_data["first_name"], teacher_data["last_name"])
    
    for course, course_data in Course:
        add_course(course, course_data["createdBy"], course_data["students"])
    
    for flashcards, flashcard_data in Flashcard:
        add_flashcard(flashcards, flashcard_data["question"], flashcard_data["answer"], flashcard_data["createdBy"], flashcard_data["Course"]) """

def add_student(Username: str, Password: str, first_name: str, last_name: str) -> object:
    s = User.objects.create(username=Username,
                                    first_name = first_name,
                                    last_name = last_name,
                                    password = Password)
    """s = Student(username=Username,
                                    first_name = first_name,
                                    last_name = last_name,
                                    password = Password)"""
    # s = Student()
    # s.username = Username
    # s.first_name = first_name
    # s.last_name = last_name
    # s.password = Password
    Student.objects.get_or_create(user=s)
    # s.save()
    return s

""" def add_teacher(Username: str, Password: str, first_name: str, last_name: str) -> object:
    t = Teacher.objects.create(username=Username)
    t.first_name = first_name
    t.last_name = last_name
    t.password = Password
    t.save()
    return t

def add_course(CourseName: str, createdBy: str, students: list) -> object:
    c = Course.objects.create(name=CourseName)
    c.createdBy = createdBy
    c.save()
    for student in students:
        c.students.add(student)
    c.save()
    return c

def add_flashcard(title: str, question: str, answer: str, createdBy: str, Course: str) -> object:
    f = Flashcard.objects.create(title=title, createdBy=createdBy, Course=Course)
    f.question = question
    f.answer = answer
    f.save()
    return f """


if __name__ == '__main__':
    print('Starting Educ8 population script...')
    populate()
