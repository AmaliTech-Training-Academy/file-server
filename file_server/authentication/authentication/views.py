from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from authentication.forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from djano.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_
from django .template.loader import render_to_string
from tokens import account_activation_token_generator
from django.core.mail import EmailMessage

#Sign up view
class SignUpView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name ='registration/signup.html'

#Edit profile
class LoginView(UpdateView):
    model = Userl
    form_class = LoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('profile')

    def signup(self,request):
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                form.save()

#to get the domain of the current site
            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email'
            message = render_to_string('registration/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete registration')
        else:
            form = SignupForm()
            return render(request,'registration/login.html', {'form': form})

#Activate account
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for activating your account. Now you can log in')
    else:
        return HttpResponse('Activation link is invalid!')

#Login view
class LoginView(FormView):
    form_class = LoginForm

