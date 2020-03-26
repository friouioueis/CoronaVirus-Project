from rest_framework import viewsets
from .serializers import *
from .models import *


class articleView(viewsets.ModelViewSet):
    serializer_class = articleSerializer
    queryset = article.objects.all()


class videoArticleView(viewsets.ModelViewSet):
    serializer_class = videoArticleSerializer
    queryset = article.objects.all()

class photoArticleView(viewsets.ModelViewSet):
    serializer_class = photoArticleSerializer
    queryset = article.objects.all()


class commentaireView(viewsets.ModelViewSet):
    serializer_class = commentaireSerializer
    queryset = article.objects.all()