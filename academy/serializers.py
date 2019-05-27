from rest_framework import serializers

from .models import (
    Language,
    Module,
    Activity,
    SupportMaterial,
    AssignmentActivity,
    StudentsGroup
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


class AssignmentActivitySerializer (serializers.ModelSerializer):
    activity = ActivitySerializer()
    class Meta:
        model = AssignmentActivity
        fields = '__all__'


class AssignmentActivityPatchSerializer (serializers.ModelSerializer):
    class Meta:
        model = AssignmentActivity
        fields = ['file_assignment', 'url_assignment', 'delivered']


class StudentsGroupSerializer(serializers.ModelSerializer):
    group_assignments = AssignmentActivitySerializer(many=True)
    class Meta:
        model = StudentsGroup
        fields = '__all__'