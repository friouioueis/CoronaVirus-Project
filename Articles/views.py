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


class redacteurArticlesView(viewsets.ModelViewSet):
    serializer_class = articleSerializer

    def get_queryset(self):
        idRedacteurAr = self.kwargs['id']
        return article.objects.filter(idRedacteurAr=idRedacteurAr)


class videoThematiqueView(viewsets.ModelViewSet):
    serializer_class = videoThematiqueSerializer
    queryset = videoThematique.objects.all()