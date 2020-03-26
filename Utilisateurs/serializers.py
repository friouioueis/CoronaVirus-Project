from rest_framework import serializers

from Utilisateurs.models import *


class compteUtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model                = compteUtilisateur
        fields               = '__all__'

class roleSerializer(serializers.ModelSerializer):
    class Meta:
        model                = role
        fields               = '__all__'


class infoPersonelSerializer(serializers.ModelSerializer):
    class Meta:
        model                = infoPersonel
        fields               = '__all__'