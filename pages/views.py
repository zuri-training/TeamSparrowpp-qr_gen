from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import qrcode

def homePage(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request, "pages/landing_page.html")

@login_required(login_url="login")
def dashboard(request):
    return render(request, "pages/dashboard.html")    

@login_required(login_url="login")
def types(request):
    return render(request, "pages/types.html")   