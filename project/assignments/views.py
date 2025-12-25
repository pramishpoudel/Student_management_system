#  Create your views here.

from django.forms import ValidationError
from rest_framework import generics
from .models import Assignment, StudentAssignment, Submission, Progress
from .serializers import *


class AssignmentCreateView(generics.CreateAPIView):
    serializer_class = AssignmentSerializer


class StudentAssignmentCreateView(generics.CreateAPIView):
    serializer_class = StudentAssignmentSerializer

class SubmissionCreateView(generics.CreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

class MentorSubmissionListView(generics.ListAPIView):
    serializer_class = SubmissionSerializer
    def get_queryset(self):
        mentor_id = self.request.GET.get('mentor_id')
        if not mentor_id:
            raise ValidationError({"mentor_id": "This parameter is required"})
        return Submission.objects.filter(mentor_id=mentor_id)

    def get_queryset(self):
        mentor_id = self.request.query_params.get("mentor_id")
        return Submission.objects.filter(
            student_assignment__assignment__mentor_id=mentor_id
        )


class ProgressCreateView(generics.CreateAPIView):
    serializer_class = ProgressSerializer
