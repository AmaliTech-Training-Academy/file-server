from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

class LogInForm(AuthenticationForm):
    # username = forms.CharField(max_length=100)
    # password = forms.CharField(widget=forms.PasswordInput)
    pass
