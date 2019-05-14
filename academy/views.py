from rest_framework.generics import ListAPIView

from .models import (
    AssignmentActivity
)

from .serializers import (
    AssignmentActivitySerializer
)


class AssignmentActivityList (ListAPIView):
    serializer_class = AssignmentActivitySerializer
    queryset = AssignmentActivity.objects.all()