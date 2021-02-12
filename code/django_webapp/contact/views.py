from django.shortcuts import render, redirect
from django.http import HttpResponse

def contact_view(request):
    return render(request, "contact/contact_page.html")
