## project/project/urls.py
from django.contrib import admin
from django.urls import path, include

from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', slang_list, name='slang_list'),  # Home page listing slang words
    path('add/', add_slang, name='add_slang'),
]