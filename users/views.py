from rest_framework.generics import RetrieveAPIView

from django.contrib.auth import get_user_model

from .serializers import UserSerializer

class UserRetrieve(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()