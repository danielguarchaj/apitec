from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from django.contrib.auth import get_user_model

from .models import (
    AssignmentActivity,
    StudentsGroup
)

from .serializers import (
    AssignmentActivitySerializer,
    AssignmentActivityPatchSerializer
)


class AssignmentActivityRetrieveUpdate (RetrieveUpdateAPIView):
    queryset = AssignmentActivity.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AssignmentActivitySerializer
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return AssignmentActivityPatchSerializer
        
    def get_object(self):
        try:
            return AssignmentActivity.objects.get(pk=self.kwargs['asgmt_id'], student__pk=self.kwargs['user_id'])
        except:
            return None