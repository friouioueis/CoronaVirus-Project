from rest_framework import serializers

from Notifications.models import *


class notifUtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model                = notifUtilisateur
        fields               = '__all__'
