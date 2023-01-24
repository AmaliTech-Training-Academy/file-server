from django.urls import path
from fileapp import views


urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    path('send_file/<int:file_id>/', views.send_file_email, name='send_file_email')

    
]