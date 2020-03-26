from rest_framework import serializers

from Signal.models import *


class signalementSerializer(serializers.ModelSerializer):
    class Meta:
        model                = signalement
        fields               = '__all__'


class selfPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model                = selfPhoto
        fields               = '__all__'


class videoThematiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model                = videoThematique
        fields               = '__all__'

