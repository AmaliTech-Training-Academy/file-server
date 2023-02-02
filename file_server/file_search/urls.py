from django.urls import path
from .views import searchposts

fileapp = 'file_search'

urlpatterns = [
    path('', searchposts, name='searchposts'),
]