# from django.conf.urls import url
# from django.contrib import admin
from django.urls import path
from .views import searchposts

app_name = 'file_search'


urlpatterns = [
     path('search/', searchposts, name='search'),

]