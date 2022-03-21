from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect, render
from datetime import datetime
from Educ8.forms import CourseForm, FlashcardForm, AccountForm, CourseFileForm
from Educ8.models import Course, Flashcard, CourseFile, Account
from Educ8.decorators import is_teacher, is_student

def index(request):

    """calls cookie handling function,
    renders a response template."""

    visitor_cookie_handler(request)
    response = render(request, 'Educ8/index.html')
    return response


# Method for getting all of the courses a student is enrolled into
# and then returns the list to the my_courses page.
@login_required
def my_courses(request):
    context_dict = {"current_user":request.user}

    # Display all courses in which this user is enrolled in (can only be students)
    courses = Course.objects.filter(students__username=request.user.username)
    if len(courses) > 0:
        context_dict["courses"] = [course for course in courses]

    # Display all courses created by this user (can only be teachers)
    courses = Course.objects.filter(createdBy__username__exact=request.user.username)
    if len(courses) > 0:
        context_dict["courses"] = [course for course in courses]

    # User's First name
    if request.user.first_name == "":
        name = "Your"
    else:
        name = request.user.first_name
    context_dict["name"] = name

    return render(request, 'Educ8/my_courses.html', context=context_dict)

#Method for getting all of the flashcards and files for a single course
#and then returning them to "course"
@login_required
def show_course(request, course_name_slug):
    context_dict = {}

    try:
        course = Course.objects.get(slug=course_name_slug)
        flashCards = Flashcard.objects.filter(course=course)
        files = CourseFile.objects.filter(course=course)
        context_dict['files'] = files
        context_dict['flashCards'] = flashCards
        context_dict['course'] = course
        context_dict['current_user'] = request.user
    except Course.DoesNotExist:
        page_not_found(request, "Course not found")

    return render(request, 'Educ8/course.html', context=context_dict)

#method for allowing a teacher to create a course
@login_required
@user_passes_test(is_teacher)
def add_course(request):

    if request.method == 'POST':
        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()
            course = Course.objects.get(courseName=request.POST["courseName"])
            course.createdBy = request.user
            course.save()
            return redirect(reverse('Educ8:show_course', kwargs={'course_name_slug' : course.slug}))
        else:
            print(form.errors)

    return render(request, 'Educ8/forms/add_course.html')

# TODO: Error handling, max file size?
@login_required
@user_passes_test(is_teacher)
def add_files(request, course_name_slug):
    if request.method == 'POST':
        form = CourseFileForm(request.POST, request.FILES)
        if form.is_valid():
            course = Course.objects.get(slug=course_name_slug)
            course_file = CourseFile(course=course)
            file = request.FILES['file']
            course_file.file.save(file.name, file)
            course_file.save()
            return redirect(f'/Educ8/my_courses/{course_name_slug}')
    return render(request, 'Educ8/forms/add_files.html')

@login_required
@user_passes_test(is_student)
def add_or_edit_flashcard(request, course_name_slug, flashcard_id=None):
    form = FlashcardForm()
    user_can_edit_flashcard = False
    if flashcard_id != None:
        existing_flashcard = Flashcard.objects.get(id=flashcard_id)
        user_can_edit_flashcard = existing_flashcard.createdBy == request.user

    if request.method == 'POST':
        form = FlashcardForm(request.POST)

        if form.is_valid():
            if user_can_edit_flashcard:
                Flashcard.objects.filter(id=flashcard_id).update(title=request.POST['title'], 
                                                                question=request.POST['question'], 
                                                                answer=request.POST['answer']) 
            else:
                flashCard = form.save(commit=False)
                flashCard.course  = Course.objects.get(slug=course_name_slug)
                flashCard.createdBy = request.user
                flashCard.save()

            return redirect(reverse('Educ8:show_course', kwargs={'course_name_slug' : course_name_slug}))

        else:
            print(form.errors)

    context_dict = {'flashcard_id':flashcard_id, 'form' : form, 'existing_flashcard':None}
    if user_can_edit_flashcard:
        context_dict['existing_flashcard'] = existing_flashcard

    return render(request, 'Educ8/forms/add_or_edit_flashcard.html', context=context_dict)

@login_required
def delete_flashcard(request, course_name_slug, flashcard_id):
    # Check that the user has the authority to delete the flashcard
    flashcard = Flashcard.objects.get(id=flashcard_id)
    course = Course.objects.get(slug=course_name_slug)
    
    # If either the teacher of the course or the student that created the flashcard, then allow deletion
    if (request.user.is_teacher and course.createdBy == request.user) or (flashcard.createdBy == request.user):
        Flashcard.objects.filter(id=flashcard_id).delete()
        return redirect(reverse('Educ8:show_course', kwargs={'course_name_slug' : course_name_slug}))
    else:
        return HttpResponseForbidden('You are not allowed to perform this action')

@login_required
def show_flashcard(request, course_name_slug, flashcard_id):
    context_dict={}
    try:
        course = Course.objects.get(slug=course_name_slug)
        flashcard = Flashcard.objects.get(id=flashcard_id)
        context_dict['flashCard'] = flashcard
        context_dict['course'] = course
    except Course.DoesNotExist:
        course = None
        flashcard = None
        context_dict['flashCards'] = None
        context_dict['course'] = None
    return render(request, 'Educ8/flashcard.html', context=context_dict)

@login_required
@user_passes_test(is_teacher)
def add_students(request, course_name_slug):
    context_dict = {}
    """conditional to check course exists.
    code to add students to specific courses"""

    # Need to validate user exists etc...
    if request.method == 'POST':
        student_to_add = request.POST.get('add')
        course = Course.objects.get(slug=course_name_slug)
        course.students.add(Account.objects.get(username=student_to_add))
    
    # Return all available users we can add and all users already in the course
    enrolled_students = Course.objects.get(slug=course_name_slug).students.all()
    all_students = Account.objects.filter(is_student=True)
    context_dict["available_students"] = set(all_students) - set(enrolled_students)
    context_dict["enrolled_students"] = enrolled_students

    return render(request, 'Educ8/forms/add_students.html', context=context_dict)

# Need to verify passwords are the same and return any form errors
def register(request):

    """view to register a student/teacher,
    check if the form is valid and
    direct them to the signup page
    """

    if request.method == 'POST':
        user_type = request.POST.get('user_type', None)
        terms_conditions = request.POST.get('terms', None)

        form = AccountForm(request.POST)
        if (form.is_valid()) and (user_type in ['student', 'teacher']) and (terms_conditions != None):
            user = None
            if user_type == 'student':
                user = form.save(is_student=True)
            elif user_type == 'teacher':
                user = form.save(is_teacher=True)

            # Now user has been created, login and redirect to home page
            login(request, user)

            return redirect(reverse('Educ8:index'))
        else:
            print(form.errors.as_data())

    return render(request, 'Educ8/forms/register.html')

# Can we pass the 'next' GET variable to the register view?
def user_login(request):
    if request.method == 'POST':
        # Determine if we should redirect the user based on GET parameters
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        redirect_to = request.POST.get('next', reverse('Educ8:index'))

        if user:
            if user.is_active:
                login(request, user)
                return redirect(redirect_to)
            else:
                return HttpResponse("Your Educ8 account is disabled.")

        else:
            print(f"Invalid login detals: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'Educ8/forms/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('Educ8:index'))

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
    request.session['visits'] = visits


def terms(request):
    return render(request, "Educ8/terms.html")

# HTTP 404 Error (Page not found)
def page_not_found(request, exception):
    return render(request, "Educ8/404.html")
