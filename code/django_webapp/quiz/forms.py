from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from quiz.models import (Answer, Question, StudentAnswer, Subject, User)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('text', )
