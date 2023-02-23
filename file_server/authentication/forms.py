from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
import re

class CustomPasswordValidator:
    def validate(self, password, user=None):
        # Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        if not re.match(pattern, password):
            raise forms.ValidationError(
                'Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character'
            )

    def get_help_text(self):
        return 'Your password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.'


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    

    class Meta:
        model = CustomUser
        fields = ['email']

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError('Passwords do not match')
            
        validator = CustomPasswordValidator()
        validator.validate(password)
        
        return password
    

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.is_active = False
            user.save()
        return user

class LogInForm(AuthenticationForm):
    pass
