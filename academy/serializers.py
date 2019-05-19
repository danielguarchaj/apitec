from rest_framework import serializers

from .models import (
    Language,
    Module,
    Activity,
    SupportMaterial,
    AssignmentActivity
)

from users.serializers import UserSerializer

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
    student = UserSerializer()
    activity = ActivitySerializer()
    class Meta:
        model = AssignmentActivity
        fields = '__all__'
        depth = 2


class AssignmentActivityPatchSerializer (serializers.ModelSerializer):
    class Meta:
        model = AssignmentActivity
        fields = ['file_assignment', 'url_assignment', 'student', 'delivered']