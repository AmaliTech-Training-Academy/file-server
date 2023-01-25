from django.urls import path
from fileapp import views
from .views import FileListView


urlpatterns = [
    path('upload_file/', views.upload_file, name='upload_file'),
    path('download_file/<int:file_id>/', views.download_file, name='download_file'),
    path('send_file/<int:file_id>/', views.send_file_email, name='send_file_email'),
    path('files/', FileListView.as_view(), name='upload_list')
]