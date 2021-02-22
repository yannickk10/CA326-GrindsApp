from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .forms import TutorSignUpForm, StudentSignUpForm
from django.contrib import messages

def student_register(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            usern = form.cleaned_data.get('first_name')
            messages.success(request, 'Account was created for ' + usern)
            login(request, user)
            return redirect('students:quiz_list')
    else:
        form = TutorSignUpForm()

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
            return redirect('tutor:quiz_change_list')
    else:
        form = TutorSignUpForm()

    context = {'form': form}
    return render(request, 'users/tutor_register.html', context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'users/login.html', context)
