from rest_framework import serializers

from django.contrib.auth import get_user_model
from .models import Student

class StudentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class UserSerializer (serializers.ModelSerializer):
    student = StudentSerializer()
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'student')


class UserSimpleSerializer (serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'