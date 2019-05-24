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
    
    def get_queryset(self):
        return AssignmentActivity.objects.filter(student__pk=self.kwargs['user_id'])


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
    
    # def update(self):
    #     instance = self.get_object()
    #     instance.
    #     instance.save()

    #     serializer = self.get_serializer(instance)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)

    #     return Response(serializer.data)