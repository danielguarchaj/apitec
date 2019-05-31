from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView, UpdateAPIView

from django.contrib.auth import get_user_model

from .serializers import UserGroupsSerializer, UserStudentSerializer, UserSimpleSerializer, StudentSimpleSerializer

class UserRetrieve(RetrieveUpdateAPIView):
    queryset = get_user_model().objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserStudentSerializer
        if self.request.method == 'PATCH' or self.request.method == 'PUT':
            return UserSimpleSerializer


class UserGroupsRetrieve(RetrieveAPIView):
    serializer_class = UserGroupsSerializer
    queryset = get_user_model().objects.all()


class StudentUpdate(UpdateAPIView):
    serializer_class = StudentSimpleSerializer


class UserUpdate (UpdateAPIView):
    serializer_class = UserSimpleSerializer
    