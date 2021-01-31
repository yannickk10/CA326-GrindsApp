from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=50)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
