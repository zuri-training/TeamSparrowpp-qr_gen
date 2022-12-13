from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def homePage(request):
    return render(request, "pages/landing_page.html")

@login_required(login_url="login")
def dashboard(request):
    return render(request, "pages/dashboard.html")    

@login_required(login_url="login")
def type(request):
    return render(request, "pages/types.html")   