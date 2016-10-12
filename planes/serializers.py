from rest_framework import serializers
from planes.models import AirbusPlane

class AirbusPlaneSerializer(serializers.ModelSerializer):
    engines = serializers.StringRelatedField(many=True)

    class Meta:
        model = AirbusPlane
        fields = '__all__'