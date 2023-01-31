from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Sign Up Form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    password = forms.CharField(max_length=200)


    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password1', 
            'password2', 
            ]
# Login Form
class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            ]
