from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView
from django.contrib.auth import get_user_model

from .models import (
    AssignmentActivity,
    StudentsGroup,
    AssignmentDelivery,
    Project
)

from .serializers import (
    AssignmentActivitySerializer,
    AssignmentDeliverySimpleSerializer,
    AssignmentActivityStudentSerializer,
    ProjectSerializer,
    ProjectSimpleSerializer
)


class AssignmentActivityRetrieve (RetrieveAPIView):
    serializer_class = AssignmentActivityStudentSerializer
    queryset = AssignmentActivity.objects.all()


class AssignmentDeliveryCreate (CreateAPIView):
    queryset = AssignmentDelivery.objects.all()
    serializer_class = AssignmentDeliverySimpleSerializer


class ProjectListCreate (ListCreateAPIView):    
    def get_serializer_class (self):
        if self.request.method == 'POST':
            return ProjectSimpleSerializer
        if self.request.method == 'GET':
            return ProjectSerializer
    
    def get_queryset(self):
        return Project.objects.filter(owner__pk=self.kwargs['owner_pk'])


class ProjectRetrieveUpdate (RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'PATCH' or self.request.method == 'PUT':
            return ProjectSimpleSerializer
        if self.request.method == 'GET':
            return ProjectSerializer