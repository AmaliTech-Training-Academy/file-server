from django.urls import path
from authentication.views import SignUpView, LoginView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', LoginView.as_view(), name='profile'),
]

