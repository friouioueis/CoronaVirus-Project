from django.http import JsonResponse
from rest_framework import viewsets

from .policies import SignalAccessPolicy
from .serializers import *
from .models import *


class signalementView(viewsets.ModelViewSet):
    permission_classes          = SignalAccessPolicy
    serializer_class            = signalementSerializer
    queryset                    = signalement.objects.filter(validerSg=None)

    def perform_create(self, serializer):
        serializer.save(idUtilisateurSg=self.request.user,validerSg=None,idModerateurSg=None)

    def partial_update(self, request, pk=None):
        s=self.get_object()
        s.validerSg=request.data["validerSg"]
        s.idModerateurSg_id=request.user.id
        s.save()
        return JsonResponse({"idSignal":s.idSignal,"validerSg":s.validerSg})

    def update(self, request, pk=None):
        s=self.get_object()
        s.descriptionSg=request.data["descriptionSg"]
        s.typeSg=request.data["typeSg"]
        s.lienSg=request.data["lienSg"]
        s.save()
        return JsonResponse({"idSignal": s.idSignal, "descriptionSg": s.descriptionSg,"typeSg":s.typeSg,"lienSg":s.lienSg})



class utilisateurSignalsView(viewsets.ReadOnlyModelViewSet):
    permission_classes = SignalAccessPolicy
    serializer_class            = signalementSerializer

    def get_queryset(self):
        idUtilisateurSg         = self.kwargs['id']
        return signalement.objects.filter(idUtilisateurSg=idUtilisateurSg)


class SignalModerValidView(viewsets.ReadOnlyModelViewSet):
    permission_classes = SignalAccessPolicy
    serializer_class            = signalementSerializer

    def get_queryset(self):
        idModerateur            = self.kwargs['id']
        return signalement.objects.filter(idModerateurSg=idModerateur, validerSg=True)

class SignalModerRefusView(viewsets.ReadOnlyModelViewSet):
    permission_classes = SignalAccessPolicy
    serializer_class            = signalementSerializer

    def get_queryset(self):
        idModerateur            = self.kwargs['id']
        return signalement.objects.filter(idModerateurSg=idModerateur, validerSg=False)

class SignalementValidView(viewsets.ReadOnlyModelViewSet):
    permission_classes = SignalAccessPolicy
    serializer_class            = signalementSerializer
    queryset                    = signalement.objects.filter(validerSg=True)

class SignalementRefusView(viewsets.ReadOnlyModelViewSet):
    permission_classes = SignalAccessPolicy
    serializer_class            = signalementSerializer
    queryset                    = signalement.objects.filter(validerSg=False)


class selfPhotoView(viewsets.ModelViewSet):
    serializer_class            = selfPhotoSerializer
    queryset                    = selfPhoto.objects.all()


class utilisateurPhotosView(viewsets.ReadOnlyModelViewSet):
    serializer_class            = selfPhotoSerializer

    def get_queryset(self):
        idUtilisateurSph        = self.kwargs['id']
        return selfPhoto.objects.filter(idUtilisateurSph=idUtilisateurSph)