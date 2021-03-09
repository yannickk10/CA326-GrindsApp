from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
from .forms import TutorSignUpForm, StudentSignUpForm
from quiz.models import User
from django.contrib import messages

def student_register(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            usern = form.cleaned_data.get('first_name')
            messages.success(request, 'Account was created for ' + usern)
            login(request, user)
            return redirect('studentdash:course_home')
    else:
        form = StudentSignUpForm()

    context = {'form': form}
    return render(request, 'users/student_register.html', context)

def tutor_register(request):
    if request.method == 'POST':
        form = TutorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            usern = form.cleaned_data.get('first_name')
            messages.success(request, 'Account was created for ' + usern)
            login(request, user)
            return redirect('tutordash:home')
    else:
        form = TutorSignUpForm()

    context = {'form': form}
    return render(request, 'users/tutor_register.html', context)

def login_page(request):
    if request.user.is_authenticated:
        if request.user.is_tutor:
            return redirect('tutordash:home')
        else:
            return redirect('studentdash:course_home')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_student == True:
                    login(request, user)
                    return redirect('studentdash:course_home')
                else:
                    login(request, user)
                    return redirect('tutordash:home')
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'users/login.html', context)
