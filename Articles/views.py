from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from .policies import *
from .serializers import *
from .models import *


class articleView(viewsets.ModelViewSet):
    permission_classes              = (ArticleAccessPolicy,)
    serializer_class                = articleSerializer
    queryset                        = article.objects.all()

    def perform_create(self, serializer):
        serializer.save(idRedacteurAr=self.request.user)

    def partial_update(self, request, pk=None):
        article=self.get_object()
        article.validerAR=request.data["validerAR"]
        article.idModerateurAr_id=request.user.id
        article.save()
        return JsonResponse({"idArticle":article.idArticle,"validerAR":article.validerAR})

    def update(self, request, pk=None):
        article=self.get_object()
        article.contenuAr=request.data['contenuAr']
        article.dateAr=request.data['dateAr']
        article.terminerAR=request.data['terminerAR']
        article.save()
        return  JsonResponse({"idArticle":article.idArticle,"contenuAr":article.contenuAr,'dateAr':article.dateAr})


class articleTermineView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (ArticleAccessPolicy,)
    serializer_class = articleSerializer
    def get_queryset(self):
        return article.objects.filter(terminerAR=True)

class articleNonTermineView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (ArticleTermineAccessPolicy,)
    serializer_class = articleSerializer
    def get_queryset(self):
        return article.objects.filter(terminerAR=None)


class articleValideView(viewsets.ReadOnlyModelViewSet):
    serializer_class = articleSerializer
    def get_queryset(self):
        return article.objects.filter(validerAR=True)


class videoArticleView(viewsets.ModelViewSet):
    permission_classes              = (VideoArticleAccessPolicy,)
    serializer_class                = videoArticleSerializer
    queryset                        = videoArticle.objects.all()


class photoArticleView(viewsets.ModelViewSet):
    permission_classes              = (PhotoArticleAccessPolicy,)
    serializer_class                = photoArticleSerializer
    queryset                        = photoArticle.objects.all()


class commentaireView(viewsets.ModelViewSet):
    permission_classes = (CommentaireAccessPolicy,)
    serializer_class                = commentaireSerializer
    queryset                        = commentaire.objects.all()


    def perform_create(self, serializer):
        serializer.save(idUtilisateurCom=self.request.user)

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
        return JsonResponse({"idCommentaire": comm.idCommentaire, "signalerCom": comm.signalerCom})


class redacteurArticlesView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (ArticleAccessPolicy,)
    serializer_class                = articleSerializer

    def get_queryset(self):
        idRedacteurAr               = self.kwargs['id']
        return article.objects.filter(idRedacteurAr=idRedacteurAr)


class articleCommentairesView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (CommentaireAccessPolicy,)
    serializer_class                = commentaireSerializer

    def get_queryset(self):
        idArticleCom                = self.kwargs['id']
        return commentaire.objects.filter(idArticleCom=idArticleCom)


class articleVideosView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (VideoArticleAccessPolicy,)
    serializer_class                = videoArticleSerializer

    def get_queryset(self):
        idArticleVd                 = self.kwargs['id']
        return videoArticle.objects.filter(idArticleVd=idArticleVd)


class articlePhotosView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (PhotoArticleAccessPolicy,)
    serializer_class                = photoArticleSerializer

    def get_queryset(self):
        idArticlePh                 = self.kwargs['id']
        return photoArticle.objects.filter(idArticlePh=idArticlePh)


class ModerateurValidView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (ModerateurAccessPolicy,)
    serializer_class            = articleSerializer

    def get_queryset(self):
        idModerateur            = self.kwargs['id']
        return article.objects.filter(idModerateurAr=idModerateur, validerAR=True)


class ModerateurRefusView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (ModerateurAccessPolicy,)
    serializer_class            = articleSerializer

    def get_queryset(self):
        idModerateur            = self.kwargs['id']
        return article.objects.filter(idModerateurAr=idModerateur, validerAR=False)


class ArticleValidView(viewsets.ReadOnlyModelViewSet):
    serializer_class            = articleSerializer
    queryset                    =  article.objects.filter(validerAR=True)

class ArticleRefusView(viewsets.ReadOnlyModelViewSet):
    serializer_class            = articleSerializer
    queryset                    = article.objects.filter(validerAR=False)


class videoThematiqueView(viewsets.ModelViewSet):
    serializer_class                = videoThematiqueSerializer
    queryset = videoThematique.objects.all()
    def perform_create(self, serializer):
        serializer.save(idUtilisateurVThema=self.request.user)

    def partial_update(self, request, pk=None):
        article=self.get_object()
        article.validerVthema=request.data["validerVthema"]
        article.idModerateurVthema_id=request.user.id
        article.save()
        return JsonResponse({"idVideoThema":article.idVideoThema,"validerVthema":article.validerVthema})

    def update(self, request, pk=None):
        article=self.get_object()
        article.lienVthema=request.data['lienVthema']
        article.titreVthema=request.data['titreVthema']
        article.descriptionVthema=request.data['descriptionVthema']
        article.save()
        return JsonResponse({"idVideoThema": article.idVideoThema,"titreVthema":article.titreVthema,"descriptionVthema":article.descriptionVthema,"lienVthema":article.lienVthema})

class VideoUtilisateurView(viewsets.ReadOnlyModelViewSet):
    serializer_class            = videoThematiqueSerializer
    def get_queryset(self):
        idUtilisateur           = self.kwargs['id']
        return videoThematique.objects.filter(idUtilisateurVThema=idUtilisateur)

