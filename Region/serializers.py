from rest_framework import serializers

from Region.models import *


class regionSerializer(serializers.ModelSerializer):
    class Meta:
        model                = region
        fields               = '__all__'


class statistiqueRegionSerializer(serializers.ModelSerializer):

    class Meta:
        model                = statistiqueRegion
        fields               = '__all__'