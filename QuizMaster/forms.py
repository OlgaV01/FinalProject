from django import forms

from QuizMaster.models import StudySet


# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
#
#
# class RegisterUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']
class StudyForm(forms.ModelForm):
    class Meta:
        model = StudySet
        exclude = ['user']


