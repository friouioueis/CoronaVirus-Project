from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from .policies import *
from .serializers import *
from .models import *


class regionView(viewsets.ModelViewSet):
    permission_classes = (RegionAccessPolicy,)
    serializer_class                = regionSerializer
    queryset                        = region.objects.all()

    @action(detail=True, methods=['PATCH'], name='region risque')
    def isRisque(self, request, pk=None):
        reg = self.get_object()
        reg.is_risque= request.data["is_risque"]
        reg.save()
        return JsonResponse({"idRegion": reg.idRegion, "is_risque": reg.is_risque})


class statistiqueRegionView(viewsets.ModelViewSet):
    permission_classes = (StatistiquesAccessPolicy,)
    serializer_class                = statistiqueRegionSerializer
    queryset                        = statistiqueRegion.objects.all()

    def partial_update(self, request, pk=None):
        stat=self.get_object()
        stat.validerSt=request.data["validerSt"]
        stat.idModerateurSt_id=request.data["idModerateurSt"]
        stat.save()
        return JsonResponse({"idStatistique":stat.idStatistique,"validerSt":stat.validerSt})

    def update(self, request, pk=None):
        stat = self.get_object()
        stat.validerSt = request.data["validerSt"]
        stat.idModerateurSt_id = request.data["idModerateurSt"]
        stat.save()
        return JsonResponse({"idStatistique": stat.idStatistique, "validerSt": stat.validerSt})


class statistiqueRegionValideView(viewsets.ReadOnlyModelViewSet):
    serializer_class                = statistiqueRegionSerializer
    def get_queryset(self):
        return statistiqueRegion.objects.filter(validerSt=True)


class regionStatsView(viewsets.ReadOnlyModelViewSet):
    serializer_class                = statistiqueRegionSerializer

    def get_queryset(self):
        idRegionSt                  = self.kwargs['id']
        return statistiqueRegion.objects.filter(validerSt=True,idRegionSt=idRegionSt).order_by('dateSt')
