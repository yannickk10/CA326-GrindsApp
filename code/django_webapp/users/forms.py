from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from quiz.models import User, Subject


class TutorSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=50)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user
