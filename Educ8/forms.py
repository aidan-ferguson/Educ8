from django.core.exceptions import ValidationError
from django import forms 
from Educ8.models import Course, Flashcard, CourseFile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class AccountRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
        
    def save(self, is_student=False, is_teacher=False, commit=True):
        user = super().save(commit=False)
        user.is_student = is_student
        user.is_teacher = is_teacher
        if commit:
            user.save()
        return user

class CourseForm(forms.ModelForm):
    courseName = forms.CharField(max_length=128)

    class Meta:
        model = Course
        fields = ('courseName',)

class FlashcardForm(forms.ModelForm):
    title = forms.CharField(max_length=32)
    question = forms.CharField(max_length=256)
    answer = forms.CharField(max_length=256)

    class Meta:
        model = Flashcard
        fields = ('title', 'question', 'answer')
        
# For checking that the file size is not too large
def file_size_validator(file):
    max_file_size = 100 * 1024 * 1024
    if file.size > max_file_size:
        raise ValidationError('File too large. Size should not exceed 100 MB.')

class CourseFileForm(forms.ModelForm):
    file = forms.FileField(validators=[file_size_validator])

    class Meta:
        model = CourseFile
        fields = ('file',)
