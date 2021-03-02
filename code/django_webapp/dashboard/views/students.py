from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, ListView, UpdateView, DetailView)

from ..models import Course

class CourseListView(ListView):
    model = Course
    template_name = 'quiz/students/home.html'
    context_object_name = 'courses'
