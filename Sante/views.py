from rest_framework import viewsets
from .serializers import *
from .models import *


class infoSanteView(viewsets.ModelViewSet):
    serializer_class = infoSanteSerializer
    queryset = infoSante.objects.all()


class utilisateurInfoSanteView(viewsets.ModelViewSet):
    serializer_class = infoSanteSerializer

    def get_queryset(self):
        idUtilisateurIs = self.kwargs['id']
        return infoSante.objects.filter(idUtilisateurIs=idUtilisateurIs).order_by('dateSaisie')
