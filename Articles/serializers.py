from rest_framework import serializers

from Articles.models import *



class videoArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model                = videoArticle
        fields               = '__all__'


class photoArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model                = photoArticle
        fields               = '__all__'


class articleSerializer(serializers.ModelSerializer):
    photos = photoArticleSerializer(many=True, required=False)
    videos = videoArticleSerializer(many=True, required=False)
    class Meta:
        model                = article
        fields               = ['idArticle', 'idRedacteurAr', 'idModerateurAr', 'dateAr', 'validerAR', 'refuserAR', 'contenuAr', 'photos', 'videos']




class commentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model                = commentaire
        fields               = '__all__'


class videoThematiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model                = videoThematique
        fields               = '__all__'

