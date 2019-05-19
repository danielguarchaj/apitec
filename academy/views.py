from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView

from .models import (
    AssignmentActivity
)

from .serializers import (
    AssignmentActivitySerializer,
    AssignmentActivityPatchSerializer
)


class AssignmentActivityList (ListAPIView):
    serializer_class = AssignmentActivitySerializer
    queryset = AssignmentActivity.objects.all()


class AssignmentActivityRetrieveUpdate (RetrieveUpdateAPIView):
    queryset = AssignmentActivity.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AssignmentActivitySerializer
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return AssignmentActivityPatchSerializer