from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView, CreateAPIView
from django.contrib.auth import get_user_model

from .models import (
    AssignmentActivity,
    StudentsGroup,
    AssignmentDelivery
)

from .serializers import (
    AssignmentActivitySerializer,
    AssignmentDeliverySimpleSerializer,
    AssignmentActivityStudentSerializer
)


class AssignmentActivityRetrieve (RetrieveAPIView):
    serializer_class = AssignmentActivityStudentSerializer
    queryset = AssignmentActivity.objects.all()


class AssignmentDeliveryCreate (CreateAPIView):
    queryset = AssignmentDelivery.objects.all()
    serializer_class = AssignmentDeliverySimpleSerializer