from rest_framework import serializers
from .models import Mentor, Student

 
class MentorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Mentor
        fields = ['id', 'name', 'email', 'password']
    def validate_email(self, value):
        # Normalize email
        email = value.lower().strip()

        # Check if already exists
        if Mentor.objects.filter(email=email).exists():
            raise serializers.ValidationError("This email is already registered.")

        # Optional: enforce domain or format rules
        # if not email.endswith(('.com', '.org', '.edu', '.net')):
        #     raise serializers.ValidationError("Invalid email domain.")

        return email

    def create(self, validated_data):
        password = validated_data.pop('password')
        mentor = Mentor(**validated_data)
        mentor.set_password(password)
        mentor.save()
        return mentor


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'mentor', 'name', 'email']