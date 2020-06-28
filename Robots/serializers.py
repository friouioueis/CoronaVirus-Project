from rest_framework import serializers

from Robots.models import *


LANGUE_CHOICES = (
    ('ar', 'arabe'),
    ('fr', 'français')
)

class pubGNSerializer(serializers.ModelSerializer):
    class Meta:
        model                = pubGoogleNews
        fields               = '__all__'



class pubYoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model                = pubYoutube
        fields               = '__all__'



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model                = Article
        fields               = '__all__'

class RunSpiderSerializer(serializers.Serializer):
    langue= serializers.CharField(max_length=2)
    #source=serializers.ListField(child=serializers.CharField(max_length=512))
    source=serializers.CharField(max_length=512)
    dateDebut=serializers.DateTimeField()
    dateFin=serializers.DateTimeField()
