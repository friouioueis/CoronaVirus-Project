from rest_framework import viewsets
from .serializers import *
from .models import *


class compteUtilisateurView(viewsets.ModelViewSet):
    serializer_class = compteUtilisateurSerializer
    queryset = compteUtilisateur.objects.all()


class roleView(viewsets.ModelViewSet):
    serializer_class = roleSerializer
    queryset = role.objects.all()


class infoPersonelView(viewsets.ModelViewSet):
    serializer_class = infoPersonelSerializer
    queryset = infoPersonel.objects.all()


class utilisateurRolesView(viewsets.ModelViewSet):
    serializer_class = roleSerializer

    def get_queryset(self):
        idUtilisateurR = self.kwargs['id']
        return role.objects.filter(idUtilisateurR=idUtilisateurR)


class utilisateurInfosView(viewsets.ModelViewSet):
    serializer_class = infoPersonelSerializer

    def get_queryset(self):
        idUtilisateurR = self.kwargs['id']
        return infoPersonel.objects.filter(idUtilisateurR=idUtilisateurR)
