from django.db import models
from accounts.models import Student, Mentor
# Create your models here.

class Assignment(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    due_date = models.DateField()

    def __str__(self):
        return self.title
    
    
class StudentAssignment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student.name} - {self.assignment.title}"
    
    

class Submission(models.Model):
    student_assignment = models.ForeignKey(StudentAssignment, on_delete=models.CASCADE)
    file = models.FileField(upload_to="submissions/")
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.student_assignment.student.name} for {self.student_assignment.assignment.title}"

class Progress(models.Model):
    submission = models.OneToOneField(Submission, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[("COMPLETED", "Completed"), ("INCOMPLETE", "Incomplete")]
    )
    feedback = models.TextField()
    reviewed_at = models.DateTimeField(auto_now_add=True)

