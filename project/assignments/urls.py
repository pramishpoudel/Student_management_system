from django.contrib import admin
from django.urls import path
from .views import *  
urlpatterns = [ 
    path('assignments/create/', AssignmentCreateView.as_view()),
    path('assignments/assign/', StudentAssignmentCreateView.as_view()),
    path('submissions/create/', SubmissionCreateView.as_view()),
    path('mentor/submissions/', MentorSubmissionListView.as_view()),
    path('progress/create/', ProgressCreateView.as_view()),
      
    ]