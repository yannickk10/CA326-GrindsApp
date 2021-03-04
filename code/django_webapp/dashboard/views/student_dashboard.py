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


class CourseListView(ListView):
    model = Course
    template_name = 'dashboard/students/home.html'
    context_object_name = 'courses'

class CourseDetailView(FormMixin, DetailView):
    model = Course
    template_name = 'dashboard/students/course_detail.html'
    form_class = EnrollForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        course = form.save(commit=False)
        user = self.request.user
        course.student.add(user)
        course.save()
        messages.success(self.request, 'You have been added to the course')
        return redirect('students:course_home')
