from django import forms

from QuizMaster.models import StudySet
from QuizMaster.models import StudySetTerms


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


class TermForm(forms.ModelForm):
    class Meta:
        model = StudySetTerms
        fields = "__all__"


