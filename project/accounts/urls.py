from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    
    path('mentor/login/', MentorLoginView.as_view()),
    path('mentor/signup/', MentorSignupView.as_view()),
    path('students/<int:id>/', MentorStudentListView.as_view()),
    path('students/add/', StudentCreateView.as_view()),
    path('students/<int:pk>/edit/', StudentUpdateView.as_view()),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view()),
]