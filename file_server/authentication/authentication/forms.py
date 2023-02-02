from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#Sign up form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=250, help_text='Enter a valid email address')
    password1 = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

#Sign in form
class SignInForm(forms.Form):
    email = forms.EmailField(max_length=250, help_text='Enter a valid email address')
    password = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ('email', 'password')

