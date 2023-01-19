from django.urls import path
from fileapp.views import upload_file, download_file


urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('download/<int:file_id>/', download_file, name='download_file')
]