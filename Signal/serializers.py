from rest_framework import serializers

from Signal.models import *
from Utilisateurs.serializers import compteUtilisateurSerializer


class signalementSerializer(serializers.ModelSerializer):
    idUtilisateurSg=compteUtilisateurSerializer(many=False, read_only=True)
    class Meta:
        model                = signalement
        fields               = ('idSignal','idUtilisateurSg','idModerateurSg','descriptionSg','validerSg','dateSg','typeSg','lienSg')


class selfPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model                = selfPhoto
        fields               = '__all__'



