from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .forms import UserCreateForm
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth import get_user_model

def signupPage(request):
    form = UserCreateForm()
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        if request.method == "POST":
            form = UserCreateForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                email = user.email
                if CustomUser.objects.filter(email=email).exists():
                    messages.error(request, 'That email already exists!')
                    return reverse('signup')
                else:
                    messages.success(request, f"Account has been successfully created for {user}.")
                    user.save()
                    return redirect('login')
    context = {'form': form}
    return render(request, "account/signup.html", context)

def loginPage(request):
    form = AuthenticationForm()
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            try:
                user = get_user_model().objects.get(email=email)
            except:
                messages.error(request, 'User does not exist')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Logged in as {request.user}')
                return redirect('dashboard')
            else:
                messages.error(request, 'Account does not exist.')
        else:
            form = AuthenticationForm()
    context = {'form': form}
    return render(request, "account/login.html", context)

def logoutView(request):
    logout(request)
    return redirect('login')