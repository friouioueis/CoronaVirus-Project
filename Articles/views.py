from rest_framework import viewsets
from .serializers import *
from .models import *


class articleView(viewsets.ModelViewSet):
    serializer_class                = articleSerializer
    queryset                        = article.objects.all()


class videoArticleView(viewsets.ModelViewSet):
    serializer_class                = videoArticleSerializer
    queryset                        = videoArticle.objects.all()


class photoArticleView(viewsets.ModelViewSet):
    serializer_class                = photoArticleSerializer
    queryset                        = photoArticle.objects.all()


class commentaireView(viewsets.ModelViewSet):
    serializer_class                = commentaireSerializer
    queryset                        = commentaire.objects.all()

class redacteurArticlesView(viewsets.ModelViewSet):
    serializer_class                = articleSerializer

    def get_queryset(self):
        idRedacteurAr               = self.kwargs['id']
        return article.objects.filter(idRedacteurAr=idRedacteurAr)


class articleCommentairesView(viewsets.ModelViewSet):
    serializer_class                = commentaireSerializer

    def get_queryset(self):
        idArticleCom                = self.kwargs['id']
        return commentaire.objects.filter(idArticleCom=idArticleCom)


class articleVideosView(viewsets.ModelViewSet):
    serializer_class                = videoArticleSerializer

    def get_queryset(self):
        idArticleVd                 = self.kwargs['id']
        return videoArticle.objects.filter(idArticleVd=idArticleVd)


class articlePhotosView(viewsets.ModelViewSet):
    serializer_class                = photoArticleSerializer

    def get_queryset(self):
        idArticlePh                 = self.kwargs['id']
        return photoArticle.objects.filter(idArticlePh=idArticlePh)


class videoThematiqueView(viewsets.ModelViewSet):
    serializer_class                = videoThematiqueSerializer
    queryset = videoThematique.objects.all()


class ModerateurValidView(viewsets.ModelViewSet):
    serializer_class            = articleSerializer

    def get_queryset(self):
        idModerateur            = self.kwargs['id']
        return article.objects.filter(idModerateurAr=idModerateur, validerAR=True)

class ModerateurRefusView(viewsets.ModelViewSet):
    serializer_class            = articleSerializer

    def get_queryset(self):
        idModerateur            = self.kwargs['id']
        return article.objects.filter(idModerateurAr=idModerateur, refuserAR=True)

class ArticleValidView(viewsets.ModelViewSet):
    serializer_class            = articleSerializer
    queryset                    =  article.objects.filter(validerAR=True)

class ArticleRefusView(viewsets.ModelViewSet):
    serializer_class            = articleSerializer
    queryset                    = article.objects.filter(refuserAR=True)

class VideoUtilisateurView(viewsets.ModelViewSet):
    serializer_class            = videoThematiqueSerializer
    def get_queryset(self):
        idUtilisateur           = self.kwargs['id']
        return videoThematique.objects.filter(idUtilisateurVThema=idUtilisateur)

