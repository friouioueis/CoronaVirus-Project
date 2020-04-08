from rest_framework import serializers
from Utilisateurs.models import *




class compteUtilisateurSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        obj = compteUtilisateur.objects.create(**validated_data)
        obj.save()
        return obj
    class Meta:
        model                = compteUtilisateur
        fields               = '__all__'
        read_only_fields = ('is_admin', 'is_staff', 'is_superuser', 'is_active')


class roleSerializer(serializers.ModelSerializer):
    class Meta:
        model                = role
        fields               = ['Type']


class infoPersonelSerializer(serializers.ModelSerializer):
    class Meta:
        model                = infoPersonel
        fields               = '__all__'

