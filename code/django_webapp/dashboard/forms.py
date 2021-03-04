from django import forms
from dashboard.models import Course


class EnrollForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = '__all__'
