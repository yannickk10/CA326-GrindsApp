from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from ..models import Course
from quiz.models import User
from quiz.decorators import tutor_required

@method_decorator([login_required, tutor_required], name='dispatch')
class CourseCreateView(CreateView):
    model = Course
    fields = ('name', 'description', 'subject', )
    template_name = 'dashboard/tutors/course_add.html'

    def form_valid(self, form):
        course = form.save(commit=False)
        course.tutor = self.request.user
        course.save()
        messages.success(self.request, 'The course was created with success!')
        return redirect('tutordash:home')

@method_decorator([login_required, tutor_required], name='dispatch')
class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'dashboard/tutors/home.html'

    def get_queryset(self):
        queryset = self.request.user.courses
        return queryset

@method_decorator([login_required, teacher_required], name='dispatch')
class StudentListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'quiz/tutors/student_detail.html'

    def get_queryset(self):
        queryset = self.request.user.courses
        return queryset
