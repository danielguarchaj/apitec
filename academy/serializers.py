from rest_framework import serializers

from .models import (
    Language,
    Module,
    Activity,
    SupportMaterial,
    AssignmentActivity,
    StudentsGroup,
    AssignmentDelivery,
    Project,
)


class SupportMaterialSerializer (serializers.ModelSerializer):
    class Meta:
        model = SupportMaterial
        exclude = ('activity',)


class ActivitySerializer (serializers.ModelSerializer):
    support_materials = SupportMaterialSerializer(source='supportmaterial_set', many=True)
    class Meta:
        model = Activity
        fields = '__all__'
        depth = 1


class AssignmentDeliverySerializer (serializers.ModelSerializer):
    class Meta:
        model = AssignmentDelivery
        fields = '__all__'


class AssignmentActivitySerializer (serializers.ModelSerializer):
    activity = ActivitySerializer()
    assignment_deliveries = serializers.SerializerMethodField()
    class Meta:
        model = AssignmentActivity
        fields = '__all__'

    def get_assignment_deliveries(self, obj):
        view = self.context['view']
        user_pk = int(view.kwargs['pk'])
        deliveries = AssignmentDelivery.objects.filter(assignment_activity__id=obj.id, student__pk=user_pk)
        serializer = AssignmentDeliverySerializer(data=deliveries, many=True)
        serializer.is_valid()

        return serializer.data


class AssignmentActivityStudentSerializer (serializers.ModelSerializer):
    activity = ActivitySerializer()
    assignment_deliveries = serializers.SerializerMethodField()
    class Meta:
        model  = AssignmentActivity
        fields = '__all__'

    def get_assignment_deliveries(self, obj):
        view = self.context['view']
        user_pk = int(view.kwargs['user_pk'])
        deliveries = AssignmentDelivery.objects.filter(assignment_activity__id=obj.id, student__pk=user_pk)
        serializer = AssignmentDeliverySerializer(data=deliveries, many=True)
        serializer.is_valid()

        return serializer.data


class StudentsGroupSerializer(serializers.ModelSerializer):
    group_assignments = AssignmentActivitySerializer(many=True)
    class Meta:
        model = StudentsGroup
        fields = '__all__'


class AssignmentDeliverySimpleSerializer (serializers.ModelSerializer):    
    class Meta:
        model = AssignmentDelivery
        fields = '__all__'


class ProjectSerializer (serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectSimpleSerializer (serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'