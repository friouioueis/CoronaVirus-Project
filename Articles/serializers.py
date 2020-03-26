from rest_framework import serializers

from Articles.models import *


class articleSerializer(serializers.ModelSerializer):
    class Meta:
        model                = article
        fields               = '__all__'


class videoArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model                = videoArticle
        fields               = '__all__'


class photoArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model                = photoArticle
        fields               = '__all__'


class commentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model                = commentaire
        fields               = '__all__'
