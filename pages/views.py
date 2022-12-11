from django.shortcuts import render
from django.http import HttpResponse

def homePage(request):
    return render(request, "pages/landing_page.html")

def dashboard(request):
    return render(request, "pages/dashboard.html")    