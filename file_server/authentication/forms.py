from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser



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
