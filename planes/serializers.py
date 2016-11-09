from rest_framework import serializers
from planes.models import AirbusPlane
from planes.models import BoeingPlane


class AirbusPlaneSerializer(serializers.ModelSerializer):
    engines = serializers.StringRelatedField(many=True)

    class Meta:
        model = AirbusPlane
        fields = '__all__'

class BoeingPlaneSerializer(serializers.ModelSerializer):
    engines = serializers.StringRelatedField(many=True)

    class Meta:
        model = BoeingPlane
        fields = '__all__'
