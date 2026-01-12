# apps/programs/urls.py

from django.urls import path
from . import views

app_name = 'programs'

urlpatterns = [
    path('', views.program_list, name='program_list'),  # List all programs
    path('<slug:program_slug>/', views.term_list, name='term_list'),  # Terms for a program
    path('<slug:program_slug>/<slug:term_slug>/', views.lesson_list, name='lesson_list'),  # Lessons for a term
]
