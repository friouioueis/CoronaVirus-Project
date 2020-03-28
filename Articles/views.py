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


class articleCommentairesView(viewsets.ModelViewSet):
    serializer_class = commentaireSerializer

    def get_queryset(self):
        idArticleCom = self.kwargs['id']
        return commentaire.objects.filter(idArticleCom=idArticleCom)


class articleVideosView(viewsets.ModelViewSet):
    serializer_class = videoArticleSerializer

    def get_queryset(self):
        idArticleVd = self.kwargs['id']
        return videoArticle.objects.filter(idArticleVd=idArticleVd)


class articlePhotosView(viewsets.ModelViewSet):
    serializer_class = photoArticleSerializer

    def get_queryset(self):
        idArticlePh = self.kwargs['id']
        return photoArticle.objects.filter(idArticlePh=idArticlePh)


class videoThematiqueView(viewsets.ModelViewSet):
    serializer_class = videoThematiqueSerializer
    queryset = videoThematique.objects.all()
