from rest_framework import generics, status
from rest_framework.response import Response
from .models import Mentor, Student
from .serializers import MentorSerializer, StudentSerializer
from rest_framework.permissions import IsAuthenticated


class MentorSignupView(generics.CreateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mentor = serializer.save()
        return Response(
            {
                "message": "Mentor account created successfully",
                "mentor": {
                    "id": mentor.id,
                    "name": mentor.name,
                    "email": mentor.email,
                }
            },
            status=status.HTTP_201_CREATED
        )


class MentorLoginView(generics.GenericAPIView):
    serializer_class = MentorSerializer

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            mentor = Mentor.objects.get(email=email)
        except Mentor.DoesNotExist:
            return Response({"error": "Invalid credentials"}, status=400)

        if not mentor.check_password(password):
            return Response({"error": "Invalid credentials"}, status=400)

        return Response({
            "message": "Login successful",
            "mentor_id": mentor.id,
            "name": mentor.name
        })


class MentorStudentListView(generics.ListAPIView):
    serializer_class = StudentSerializer
    def get_queryset(self):
        # mentor_id = self.request.query_params.get('mentor_id')
        # return Student.objects.filter(mentor_id=mentor_id)
        mentor_id = self.kwargs.get('id')  # get from path
        return Student.objects.filter(mentor_id=mentor_id)

class StudentCreateView(generics.CreateAPIView):
    serializer_class = StudentSerializer

class StudentUpdateView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'



class StudentDeleteView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'
    def get(self, request, *args, **kwargs):
        student = self.get_object()
        serializer = self.get_serializer(student)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        student_name = instance.name  # Capture name before deleting
        self.perform_destroy(instance)
        
        # Return a custom message and 200 OK status
        return Response(
            {"message": f"Student '{student_name}' has been deleted successfully."},
            status=status.HTTP_200_OK
        )


