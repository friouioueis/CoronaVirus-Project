from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from .SpidersManager import SpidersManager

from .serializers import *
from .models import *


class pubYoutubeView(viewsets.ModelViewSet):
    serializer_class                = pubYoutubeSerializer
    queryset                        = pubYoutube.objects.all()

    def update(self, request, pk=None):
        article=self.get_object()
        article.validerYt=request.data['validerYt']
        article.idModerateurYt_id=request.user.id
        article.save()
        return  JsonResponse({"idPubYoutube":article.idPubYoutube,"validerYt":article.validerYt,'idModerateurYt':article.idModerateurYt.id})

class SortedpubYoutubeView(viewsets.ModelViewSet):
    serializer_class                = pubYoutubeSerializer
    queryset                        = pubYoutube.objects.all().order_by('-dateYt')

    def update(self, request, pk=None):
        article=self.get_object()
        article.validerYt=request.data['validerYt']
        article.idModerateurYt_id=request.user.id
        article.save()
        return  JsonResponse({"idPubYoutube":article.idPubYoutube,"validerYt":article.validerYt,'idModerateurYt':article.idModerateurYt.id})

class pubGNView(viewsets.ModelViewSet):
    serializer_class                = pubGNSerializer
    queryset                        = pubGoogleNews.objects.all()

    def update(self, request, pk=None):
        article=self.get_object()
        article.validerGN=request.data['validerGN']
        article.idModerateurGN_id=request.user.id
        article.save()
        return  JsonResponse({"idPubGN":article.idPubGN,"validerGN":article.validerGN,'idModerateurGN':article.idModerateurGN.id})


class SortedpubGNView(viewsets.ModelViewSet):
    serializer_class                = pubGNSerializer
    queryset                        = pubGoogleNews.objects.all().order_by('-dateExt')

    def update(self, request, pk=None):
        article=self.get_object()
        article.validerGN=request.data['validerGN']
        article.idModerateurGN_id=request.user.id
        article.save()
        return  JsonResponse({"idPubGN":article.idPubGN,"validerGN":article.validerGN,'idModerateurGN':article.idModerateurGN.id})


class ArticlesView(viewsets.ModelViewSet):
    serializer_class                = ArticleSerializer
    queryset                        = Article.objects.all()

    def update(self, request, pk=None):
        article=self.get_object()
        article.validerAr=request.data['validerAr']
        article.idModerateurSw_id=request.user.id
        article.save()
        return  JsonResponse({"id":article.id,"validerAr":article.validerAr,'idModerateurSw':article.idModerateurSw.id})


class SortedArticlesView(viewsets.ModelViewSet):
    serializer_class                = ArticleSerializer
    queryset                        = Article.objects.all().order_by('-dateExt')


class RunSpiderView(viewsets.ViewSet):
    serializer_class=RunSpiderSerializer
    
    @action(detail=False, methods=['POST'], name='spider-run')
    def run(self, request, pk=None):
        params=request.POST
        SpidersManager(params.get('langue'),params.get('source').split(','),params.get('dateDebut'),params.get('dateFin'))
        return HttpResponse('')
