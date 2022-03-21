import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_group_project.settings')

import django
django.setup()
from django.contrib.auth.models import User
from django.core.files import File

from Educ8.models import CourseFile, Course, Flashcard, CourseFile, Account#, AccountManager

"""
Things to do:
    Comment functions.
    Create 4 loops for filling database in populate().
    Get someone to check everything.
"""

def populate() -> None:

    """
        Define the mock data to be inserted into the database.
        All object attributes will be replaced with the actual database objects after creation
        this is due to the fact that they need to be inserted into other tables
    """

    students = {
        "Dom1": {"password":"Password", "first_name":"Dom", "last_name":"Jina", "object":None},
        "Dom2": {"password":"Password", "first_name":"Dom", "last_name":"Jina", "object":None},
        "Dom3": {"password":"Password", "first_name":"Dom", "last_name":"Jina", "object":None},
        "Dom4": {"password":"Password", "first_name":"Dom", "last_name":"Jina", "object":None},
        # "": {"password":"", "first_name":"", "last_name":"", "object":None},
        "ChairLover87": {"password": "i<3chairz", "first_name":"Humphrey", "last_name":"Funnel", "object":None},
        "Lumperdumper": {"password":"S3CUr3P4SSw0rd", "first_name":"Geoff", "last_name":"Henningtonsworths", "object":None},
        "DolpyWolpy": {"password":"6LargeEggs", "first_name":"Sheeby", "last_name":"Deep", "object":None},
        "Tickles06": {"password":"tIcket2rIde", "first_name":"Mubble", "last_name":"Finth", "object":None},
        "Flumper1": {"password":"inst4nt_n00dles", "first_name":"Keith", "last_name":"Flump", "object":None},
        "catcatcatcat": {"password":"i_love_CATS", "first_name":"Catty", "last_name":"Catterson", "object":None},
        "AAAAAAAA": {"password":"the_l3tter_A", "first_name":"AAAAAAAAAdam", "last_name":"AAAAAAAnderson", "object":None},
        "ALLTHECOURSES": {"password":"enroll_m3", "first_name":"Johnny", "last_name":"Table", "object":None},
        }

    teachers = {
        "Bob1" : {"password":"Password", "first_name":"Dom", "last_name":"Jina", "object":None},
        "Bob2" : {"password":"Password", "first_name":"Dom", "last_name":"Jina", "object":None},
        "Bob3" : {"password":"Password", "first_name":"Dom", "last_name":"Jina", "object":None},
        "Bob4" : {"password":"Password", "first_name":"Dom", "last_name":"Jina", "object":None},
        # "": {"password":"", "first_name":"", "last_name":"", "object":None},
        "Henry79": {"password":"sucks_to_be_m3", "first_name":"Henry", "last_name":"Hoover (Not associated)", "object":None},
        "Chairbert": {"password":"chairz_R_gr8", "first_name":"Egbert", "last_name":"Mumples", "object":None},
        "TheMadDivisor": {"password":"pi_R_squ4red", "first_name":"Matic", "last_name":"Mathsman", "object":None},
        "HandymanDan": {"password":"max_p0wer!", "first_name":"Danny", "last_name":"Manny", "object":None},
        }

    courses = {
        "Maths" : {"createdBy":"TheMadDivisor", "students":["Dom1", "Dom2", "ALLTHECOURSES"], "object":None},
        "Extreme Cake Baking" : {"createdBy":"Bob3", "students":["Dom4", "Dom1", "ALLTHECOURSES"], "object":None},
        "English" : {"createdBy":"Bob4", "students":["ALLTHECOURSES"], "object":None},
        # "" : {"createdBy":"", "students":["ALLTHECOURSES"], "object":None},
        "Advanced Chair Building" : {"createdBy":"Chairbert", "students":["ALLTHECOURSES", "ChairLover87", "Flumper1", "Lumperdumper", "catcatcatcat"], "object":None},
        "Knitting Essentials" : {"createdBy":"Henry79", "students":["ALLTHECOURSES", "DolpyWolpy", "Tickles06", "AAAAAAAA", "catcatcatcat", "ChairLover87"], "object":None},
        "Horse Assembly (Intermediate)" : {"createdBy":"HandymanDan", "students":["ALLTHECOURSES", "DolpyWolpy", "Flumper1", "Tickles06", "catcatcatcat"], "object":None},
        "Fasting on a Budget" : {"createdBy":"Henry79", "students":["ALLTHECOURSES", "Lumperdumper", "AAAAAAAA", "Flumper1", "Tickles06", "ChairLover87"], "object":None},
        }

    flashcards = {
        "Addition Flashcard" : {"question":"What is 1 + 1?", "answer": "2", "createdBy":"Dom1", "Course":"Maths"},
        "Showdown Winner" : {"question":"Who won the 2008 Jumper Knitting competition?", "answer": "My Gran", "createdBy":"Dom4", "Course":"Extreme Cake Baking"},
        "Crochet is 4 nerdz" : {"question":"What is better crochet or knitting?", "answer": "Knitting", "createdBy":"Dom2", "Course":"Maths"},
        "Best Course" : {"question":"Best 2nd year GofU CS course", "answer": "OOSE2", "createdBy":"Dom1", "Course":"Extreme Cake Baking"},
        # "" : {"question":"", "answer": "", "createdBy":"", "Course":""},

        # Intro to Knitting
        "Knitting & Purling" : {"question":"What is the difference between a knit stitch and a purl stitch?", "answer": "fill this in later tim", "createdBy":"ALLTHECOURSES", "Course":"Knitting Essentials"},
        "crotchet bad" : {"question":"What are the main 25 disadvantages of crochet compared to knitting?", "answer": "fill this in later tim", "createdBy":"ALLTHECOURSES", "Course":"Knitting Essentials"},
        "Needle Length" : {"question":"What is the correct length of needle according to 'Gunther's Sock Guide' for children-size socks?", "answer": "fill this in later tim", "createdBy":"ALLTHECOURSES", "Course":"Knitting Essentials"},
        "Showdown Winner" : {"question":"Who won the 2008 Jumper Knitting competition?", "answer": "fill this in later tim", "createdBy":"ALLTHECOURSES", "Course":"Knitting Essentials"},
        "Cochet is 4 nerdz" : {"question":"Why is crochet objectively worse than knitting?", "answer": "fill this in later tim", "createdBy":"ALLTHECOURSES", "Course":"Knitting Essentials"},
        "Dangers of Crotchet" : {"question":"How many accidents are caused by crochet each month globally?", "answer": "fill this in later tim", "createdBy":"ALLTHECOURSES", "Course":"Knitting Essentials"},

        }

    files = {
        "important course notice.png": {"course":"Extreme Cake Baking"},
        "Assignment Instructions.pdf": {"course":"Maths"},
        "Assessed Excerise 1.txt": {"course":"English"},
        # "": {"course":""},

        # Intro to Knitting
        "guide_to_yarn.pdf": {"course":"Knitting Essentials"},
        "essential_knitting_patterns.pdf": {"course":"Knitting Essentials"},
        "why_crochet_sucks.docx": {"course":"Knitting Essentials"},
        "gunthers_sock_guide.png": {"course":"Knitting Essentials"},
        "what_wool_is_right_for_you.pptx": {"course":"Knitting Essentials"},
        "thread_density_chart.jpg": {"course":"Knitting Essentials"},
        "professional_purling_tutorial.mp4": {"course":"Knitting Essentials"},
        "synthetic_vs_natural_fabrics.pdf": {"course":"Knitting Essentials"},
        "top_10_knitting_needles_of_all_time.pdf": {"course":"Knitting Essentials"},
        "jumper_knitting_finalist_showdown.mov": {"course":"Knitting Essentials"},
        
        }

    """
        Simple loop over all student and teacher data to insert into the database
    """
    for student, student_data in students.items():
        student_data["object"] = add_student(student, student_data["password"], student_data["first_name"], student_data["last_name"])

    for teacher, teacher_data in teachers.items():
        teacher_data["object"] = add_teacher(teacher, teacher_data["password"], teacher_data["first_name"], teacher_data["last_name"])

    """
        We need to determine the actual objects of the students to be added, that is the purpose of the list comprehension
        We also get the actual teacher object in the add_course() call
    """
    for course, course_data in courses.items():
        students_to_add = [students[student]["object"] for student in course_data["students"]]
        course_data["object"] = add_course(course, teachers[course_data["createdBy"]]["object"], students_to_add)

    """
        Once again, determine the actual objects of the students and flashcards from their string representation
    """
    for flashcard, flashcard_data in flashcards.items():
        add_flashcard(flashcard, flashcard_data["question"], flashcard_data["answer"], students[flashcard_data["createdBy"]]["object"], courses[flashcard_data["Course"]]["object"])

    for file, file_data in files.items():
        add_file(file, courses[file_data["course"]]["object"])


"""
    For both student and teacher first create the underlying user object and then add a student object to the database
"""
def add_student(Username: str, Password: str, first_name: str, last_name: str) -> Account:
    student = Account.objects.create_user(username=Username,
                                        password=Password,
                                        first_name=first_name,
                                        last_name=last_name,
                                        is_student=True)
    return student

def add_teacher(Username: str, Password: str, first_name: str, last_name: str) -> Account:
    teacher = Account.objects.create_user(username=Username,
                                        password=Password,
                                        first_name=first_name,
                                        last_name=last_name,
                                        is_teacher=True)
    return teacher

"""
    Create a course in the database and add the students to it
"""
def add_course(CourseName: str, createdBy: Account, studentsToAdd: list) -> Course:
    c = Course.objects.get_or_create(courseName=CourseName, createdBy=createdBy)[0]
    for student in studentsToAdd:
        c.students.add(student)
    c.save()
    return c

"""
    Create a flashcard in the database
"""
def add_flashcard(title: str, question: str, answer: str, createdBy: Account, Course: Course) -> Flashcard:
    f = Flashcard.objects.get_or_create(title=title, question=question, createdBy=createdBy, course=Course)[0]
    f.title = title
    f.question = question
    f.answer = answer
    f.save()
    return f

def add_file(filename: str, course: Course):
    course_file = CourseFile(
        course = course
    )
    course_file.file.save(filename, File(open(f'static/population_files/{filename}', 'rb')))
    course_file.save()

if __name__ == '__main__':
    print('Starting Educ8 population script...')
    populate()
    print("Finished populating")
