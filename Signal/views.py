from rest_framework import viewsets
from .serializers import *
from .models import *


class signalementView(viewsets.ModelViewSet):
    serializer_class            = signalementSerializer
    queryset                    = signalement.objects.all()


class selfPhotoView(viewsets.ModelViewSet):
    serializer_class            = selfPhotoSerializer
    queryset                    = selfPhoto.objects.all()


class utilisateurSignalsView(viewsets.ModelViewSet):
    serializer_class            = signalementSerializer

    def get_queryset(self):
        idUtilisateurSg         = self.kwargs['id']
        return signalement.objects.filter(idUtilisateurSg=idUtilisateurSg)


class utilisateurPhotosView(viewsets.ModelViewSet):
    serializer_class            = selfPhotoSerializer

    def get_queryset(self):
        idUtilisateurSph        = self.kwargs['id']
        return selfPhoto.objects.filter(idUtilisateurSph=idUtilisateurSph)


class SignalModerValidView(viewsets.ModelViewSet):
    serializer_class            = signalementSerializer

    def get_queryset(self):
        idModerateur            = self.kwargs['id']
        return signalement.objects.filter(idModerateurSg=idModerateur, validerSg=True)

class SignalModerRefusView(viewsets.ModelViewSet):
    serializer_class            = signalementSerializer

    def get_queryset(self):
        idModerateur            = self.kwargs['id']
        return signalement.objects.filter(idModerateurSg=idModerateur, refuserSg=True)

class SignalementValidView(viewsets.ModelViewSet):
    serializer_class            = signalementSerializer
    queryset                    = signalement.objects.filter(validerSg=True)

class SignalementRefusView(viewsets.ModelViewSet):
    serializer_class            = signalementSerializer
    queryset                    = signalement.objects.filter(refuserSg=True)
