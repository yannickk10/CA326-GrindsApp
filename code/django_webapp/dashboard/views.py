from django.shortcuts import render, redirect
from django.http import HttpResponse

def student_dash_view(request):
    return render(request, "dashboard/studentDashboard.html")

def tutor_dash_view(request):
    return render(request, "dashboard/tutorDashboard.html")
