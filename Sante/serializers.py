from rest_framework import serializers

from Sante.models import *


class infoSanteSerializer(serializers.ModelSerializer):
    class Meta:
        model                = infoSante
        fields               = '__all__'
