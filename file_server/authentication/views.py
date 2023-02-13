from django.contrib.auth import authenticate, login,logout
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from .forms import LogInForm
from django.contrib.auth.forms import PasswordResetForm
from .models import CustomUser
from django.conf import settings
from django.core.mail import send_mail
from django.utils.encoding import force_str


def home_view(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = CustomUser.objects.create_user(
            username = email,
            password=password,
            is_active=False
        )
        current_site = get_current_site(request)
        message = render_to_string('accounts/account_activation.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        mail_subject = 'Activate your account.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.username]
        send_mail( mail_subject, message, email_from, recipient_list )
        return render(request, 'accounts/email_verification.html')
    else:
        return render(request, 'accounts/signup.html')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_verified = True
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
        
    else:
        return render(request, 'accounts/activation_invalid.html')
    
    


def login_view(request):
    form = LogInForm()
    if request.method == 'POST':
        form = LogInForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('fileapp:upload_list')
                
            else:
                return render(request, 'login.html', {'error': 'Invalid login credentials'})
        else:
            form = LogInForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')
    



def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = CustomUser.objects.get(username=email)
                current_site = get_current_site(request)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)
                email_body = render_to_string('passwords/password_reset_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': uid,
                    'token': token,
                })
                email_subject = 'Password reset on ' + current_site.domain
                email = EmailMessage(email_subject, email_body, to=[user.username])
                email.send()
                return redirect('authentication:password_reset_done')
                
            except CustomUser.DoesNotExist:
                form.add_error(None, 'Email address not found, try again')
    else:
        form = PasswordResetForm()
    return render(request, 'passwords/password_reset_form.html', {'form': form})

def password_reset_done(request):
    return render(request, 'passwords/password_reset_done.html')

def reset_password_confirm(request, uidb64, token):
    try:
        uid =force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):

        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            user.set_password(new_password)
            user.save()
            user = authenticate(request, username=user.username, password=new_password)
            login(request, user)
            return render(request, 'passwords/password_reset_complete.html')
        

        return render(request, 'passwords/password_reset_confirm.html', {'user': user})
    else:
        return render(request,'passwords/reset_invalid.html')
    