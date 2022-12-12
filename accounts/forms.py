from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from accounts.models import CustomUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = CustomUser
        fields = ('email', 'password')


class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = CustomUser
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")


class AccountUpdateForm(forms.ModelForm):

	class Meta:
		model = CustomUser
		fields = ('email','password')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			account = CustomUser.objects.exclude(pk=self.instance.pk).get(email=email)
		except CustomUser.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % account)

	

