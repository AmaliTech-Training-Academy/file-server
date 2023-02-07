from django.urls import path
from authentication import views


app_name = 'authentication'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('verify/<str:key>/', views.activate, name='email_verification'),
    path('reset/<uidb64>/<token>/', views.reset_password_confirm, name='reset_password_confirm'),
    path('password_reset/', views.password_reset, name='password_reset'),
    # path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    # path('reset/done/', views.password_reset_complete, name='password_reset_complete'),
]