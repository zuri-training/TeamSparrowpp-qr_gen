from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import CustomUser

class UserCreateForm(UserCreationForm):
    # password1 = forms.CharField(
    #     label=_("Password"),
    #     strip=False,
    #     widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    #     help_text=password_validation.password_validators_help_text_html(),
    # )
    # password2 = forms.CharField(
    #     label=_("Password confirmation"),
    #     widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    #     strip=False,
    #     help_text=_("Enter the same password as before, for verification."),
    # )
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
        # widgets = {
        #     "email": Input(attrs)
        # }