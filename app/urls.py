from django.urls import path
from . import views

urlpatterns = [
    path('', views.slang_list, name='slang_list'),
    path('add/', views.add_slang, name='add_slang'),

] 