from rest_framework import serializers

from Robots.models import *


class pubFacebookSerializer(serializers.ModelSerializer):
    class Meta:
        model                = pubFacebook
        fields               = '__all__'



class pubYoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model                = pubYoutube
        fields               = '__all__'


class pubSiteWebSerializer(serializers.ModelSerializer):
    class Meta:
        model                = pubSiteWeb
        fields               = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model                = Article
        fields               = '__all__'