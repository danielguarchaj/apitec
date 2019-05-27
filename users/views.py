from rest_framework.generics import RetrieveAPIView

from django.contrib.auth import get_user_model

from .serializers import UserGroupsSerializer, UserStudentSerializer

class UserRetrieve(RetrieveAPIView):
    serializer_class = UserStudentSerializer
    queryset = get_user_model().objects.all()


class UserGroupsRetrieve(RetrieveAPIView):
    serializer_class = UserGroupsSerializer
    queryset = get_user_model().objects.all()