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

def home(request):
    context = {}
    return render(request, 'dashboard/tutors/home.html', context)

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
