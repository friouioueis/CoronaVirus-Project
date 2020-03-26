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
