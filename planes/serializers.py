from rest_framework import serializers
from planes.models import AirbusPlane
from planes.models import BoeingPlane
from planes.models import CessnaPlane

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

class CessnaPlaneSerializer(serializers.ModelSerializer):
    engines = serializers.StringRelatedField(many=True)

    class Meta:
        model = CessnaPlane
        fields = '__all__'