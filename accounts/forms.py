from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import CustomUser

class UserCreateForm(UserCreationForm):
    username = forms.CharField(
        label=("Username"),
        strip=False,
        widget=forms.TextInput(attrs={"id": "username", "placeholder": "Username"}),
    )
    email = forms.CharField(
        label=("Email address"),
        strip=False,
        widget=forms.EmailInput(attrs={'autocomplete': 'new-email', "id": "email", "placeholder": "sample@gmail.com"}),
    )
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', "id": "password1", "placeholder": "Enter password here"}),
    )
    password2 = forms.CharField(
        label= ("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', "id": "password2", "placeholder": "Enter password here"}),
        strip=False,
    )
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
        # widgets = {
        #     "email": Input(attrs)
        # }