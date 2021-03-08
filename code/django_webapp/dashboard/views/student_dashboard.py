from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormMixin
from django.views.generic import (CreateView, ListView, UpdateView, DetailView)

from ..models import Course
from dashboard.forms import EnrollForm
from quiz.decorators import student_required


@method_decorator([login_required, student_required], name='dispatch')
class CourseListView(ListView):
    model = Course
    template_name = 'dashboard/students/home.html'
    context_object_name = 'courses'

@method_decorator([login_required, student_required], name='dispatch')
class CourseDetailView(DetailView):
    model = Course
    template_name = 'dashboard/students/course_detail.html'

@login_required
@student_required
def course_show(request, courseid):
    user = request.user
    course = Course.objects.get(pk=courseid)
    if course.student.filter(username=user).exists() == True:
        messages.info(request, 'You are already part of this course')
        return redirect('studentdash:course_home')
    else:
        course.student.add(user)
        messages.success(request, 'You have been added to the course')
        return redirect('studentdash:course_home')
