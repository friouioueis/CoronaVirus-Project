from rest_framework import serializers
from rest_framework_serializer_field_permissions.serializers import FieldPermissionSerializerMixin

from Articles.models import *

class videoArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model                = videoArticle
        fields               = '__all__'


class photoArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model                = photoArticle
        fields               = '__all__'


class articleSerializer(serializers.ModelSerializer,FieldPermissionSerializerMixin):
    photos = photoArticleSerializer(many=True, required=False)
    videos = videoArticleSerializer(many=True, required=False)

    class Meta:
        model                                          = article
        fields                                         = '__all__'




class commentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model                = commentaire
        fields               = '__all__'


class videoThematiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model                = videoThematique
        fields               = '__all__'

