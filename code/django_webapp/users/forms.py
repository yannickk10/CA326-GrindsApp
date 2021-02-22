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

class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=50)
    email = forms.EmailField(required=True)
    interests = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.interests.add(*self.cleaned_data.get('interests'))
        return user
