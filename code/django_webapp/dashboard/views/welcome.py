from django.shortcuts import render, redirect
from django.http import HttpResponse

def welcome_view(request):
    return render(request, "dashboard/welcome.html")

def contact_view(request):
    return render(request, "dashboard/contact.html")
