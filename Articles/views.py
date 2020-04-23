from django.http import HttpResponse, JsonResponse
from requests import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from .policies import *
from .serializers import *
from .models import *


class articleView(viewsets.ModelViewSet):
    permission_classes              = (ArticleAccessPolicy,)
    serializer_class                = articleSerializer
    queryset                        = article.objects.all()


    def partial_update(self, request, pk=None):
        article=self.get_object()
        article.validerAR=request.data["validerAR"]
        article.refuserAR = request.data["refuserAR"]
        article.save()
        return JsonResponse({"idArticle":article.idArticle,"validerAR":article.validerAR,'refuserAR':article.refuserAR})

    def update(self, request, pk=None):
        article=self.get_object()
        article.contenuAr=request.data['contenuAr']
        article.dateAr=request.data['dateAr']
        article.save()
        return  JsonResponse({"idArticle":article.idArticle,"contenuAr":article.contenuAr,'dateAr':article.dateAr})


class videoArticleView(viewsets.ModelViewSet):
    permission_classes              = (ArticleAccessPolicy,)
    serializer_class                = videoArticleSerializer

    def get_queryset(self):
        return article.objects.filter(terminerAR=True)

class photoArticleView(viewsets.ModelViewSet):
    permission_classes              = (ArticleAccessPolicy,)
    serializer_class                = photoArticleSerializer
    queryset                        = photoArticle.objects.all()


class commentaireView(viewsets.ModelViewSet):
    permission_classes = (CommentaireAccessPolicy,)
    serializer_class                = commentaireSerializer
    queryset                        = commentaire.objects.all()

    @action(detail=True, methods=['PATCH'], name='modifier commentaire')
    def modifier(self, request,pk=None):
        comm=self.get_object()
        comm.contenuCom=request.data["contenuCom"]
        comm.save()
        return JsonResponse({"idCommentaire": comm.idCommentaire, "contenuCom": comm.contenuCom})


    @action(detail=True, methods=['PATCH'], name='signaler commentaire')
    def signaler(self, request, pk=None):
        comm = self.get_object()
        comm.signalerCom = request.data["signalerCom"]
        comm.save()
        return JsonResponse({"idCommentaire": comm.idCommentaire, "signalerCom": comm.signalerComCom})

class redacteurArticlesView(viewsets.ModelViewSet):
    permission_classes = (ArticleAccessPolicy,)
    serializer_class                = articleSerializer

    def get_queryset(self):
        idRedacteurAr               = self.kwargs['id']
        return article.objects.filter(idRedacteurAr=idRedacteurAr)


class articleCommentairesView(viewsets.ModelViewSet):
    permission_classes = (CommentaireAccessPolicy,)
    serializer_class                = commentaireSerializer

    def get_queryset(self):
        idArticleCom                = self.kwargs['id']
        return commentaire.objects.filter(idArticleCom=idArticleCom)


    @action(detail=True, methods=['PATCH'], name='modifier commentaire')
    def modifier(self, request, *args, **kwargs):
        comm=self.get_object()
        comm.contenuCom=request.data["contenuCom"]
        comm.save()


    @action(detail=True, methods=['PATCH'], name='signaler commentaire')
    def signaler(self, request, *args, **kwargs):
        comm=self.get_object()
        comm.signalerCom=request.data["signalerCom"]
        comm.save()


class articleVideosView(viewsets.ModelViewSet):
    permission_classes = (ArticleAccessPolicy,)
    serializer_class                = videoArticleSerializer

    def get_queryset(self):
        idArticleVd                 = self.kwargs['id']
        return videoArticle.objects.filter(idArticleVd=idArticleVd)


class articlePhotosView(viewsets.ModelViewSet):
    permission_classes = (ArticleAccessPolicy,)
    serializer_class                = photoArticleSerializer

    def get_queryset(self):
        idArticlePh                 = self.kwargs['id']
        return photoArticle.objects.filter(idArticlePh=idArticlePh)


class videoThematiqueView(viewsets.ModelViewSet):
    serializer_class                = videoThematiqueSerializer
    queryset = videoThematique.objects.all()


class ModerateurValidView(viewsets.ModelViewSet):
    permission_classes = (ModerateurAccessPolicy,)
    serializer_class            = articleSerializer

    def get_queryset(self):
        idModerateur            = self.kwargs['id']
        return article.objects.filter(idModerateurAr=idModerateur, validerAR=True)

class ModerateurRefusView(viewsets.ModelViewSet):
    permission_classes = (ModerateurAccessPolicy,)
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

