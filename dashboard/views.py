from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import action, api_view, schema
from rest_framework.views import APIView
from rest_framework.response import Response

from Articles.models import article
from Region.models import statistiqueRegion

@api_view(['GET'])
@schema(None)
def get(request):
    stats = {}
    stats['nbr_articles'] = list(article.objects.all().values('dateAr').annotate(
        total=Count('idArticle')).order_by('dateAr'))
    stats['nbr_articles_valid'] = list(article.objects.filter(validerAR=True).values('dateAr').annotate(
        total=Count('idArticle')).order_by('dateAr'))
    stats['nbr_articles_refus'] = list(article.objects.filter(validerAR=False).values('dateAr').annotate(
        total=Count('idArticle')).order_by('dateAr'))
    stats['nbr_stat'] = list(statistiqueRegion.objects.all().values('dateSt').annotate(
        total=Count('idStatistique')).order_by('dateSt'))
    stats['nbr_stat_valid'] = list(statistiqueRegion.objects.filter(validerSt=True).values('dateSt').annotate(
        total=Count('idStatistique')).order_by('dateSt'))
    stats['nbr_stat_refus'] = list(statistiqueRegion.objects.filter(validerSt=False).values('dateSt').annotate(
        total=Count('idStatistique')).order_by('dateSt'))

    stats['redacteurs'] = list(article.objects.all().values('idRedacteurAr').annotate(
        total=Count('idArticle')).order_by('total'))
    stats['agents'] = list(statistiqueRegion.objects.all().values('idAgentSt').annotate(
        total=Count('idStatistique')).order_by('total'))

    return Response(stats)