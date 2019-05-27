from rest_framework import serializers

from django.contrib.auth import get_user_model
from .models import Student

from academy.serializers import StudentsGroupSerializer



class StudentSerializer (serializers.ModelSerializer):
    groups = StudentsGroupSerializer(many=True)
    class Meta:
        model = Student
        fields = ['groups']

class StudentSimpleSerializer (serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class UserGroupsSerializer (serializers.ModelSerializer):
    student = StudentSerializer()
    class Meta:
        model = get_user_model()
        fields = ['id', 'student']


class UserStudentSerializer (serializers.ModelSerializer):
    student = StudentSimpleSerializer()
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'student')


class UserSimpleSerializer (serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'