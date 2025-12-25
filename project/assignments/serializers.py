from rest_framework import serializers
from .models import (
    Assignment,
    StudentAssignment,
    Submission,
    Progress
)


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'mentor', 'title', 'description', 'due_date']


class StudentAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAssignment
        fields = ['id', 'student', 'assignment', 'assigned_at']
        read_only_fields = ['assigned_at']

# class SubmissionSerializer(serializers.ModelSerializer):
#     student_assignment = serializers.PrimaryKeyRelatedField( queryset=StudentAssignment.objects.all() )
#     class Meta:
#         model = Submission
#         fields = ['id', 'student_assignment', 'file', 'submitted_at']
#         read_only_fields = ['submitted_at']

class SubmissionSerializer(serializers.ModelSerializer):
    # Read-only fields for displaying details in the list view
    student_name = serializers.CharField(source='student_assignment.student.name', read_only=True)
    assignment_title = serializers.CharField(source='student_assignment.assignment.title', read_only=True)
    mentor_name = serializers.CharField(source='student_assignment.assignment.mentor.name', read_only=True)
    feedback = serializers.CharField(source='progress.feedback', read_only=True, allow_null=True)  # From Progress model, null if no progress exists
    
    # Keep the writable field for creation (if needed elsewhere)
    student_assignment = serializers.PrimaryKeyRelatedField(queryset=StudentAssignment.objects.all())
    
    class Meta:
        model = Submission
        fields = [
            'id', 
            'student_assignment',  # For creation/updates (if applicable)
            'student_name',        # Student name
            'assignment_title',    # Assignment submitted (title)
            'mentor_name',         # Mentor name
            'feedback',            # Feedback from Progress
            'file', 
            'submitted_at'
        ]
        read_only_fields = ['submitted_at', 'student_name', 'assignment_title', 'mentor_name', 'feedback']

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ['id', 'submission', 'status', 'feedback', 'reviewed_at']
        read_only_fields = ['reviewed_at']
