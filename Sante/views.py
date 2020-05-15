from rest_framework import viewsets

from .policies import *
from .serializers import *
from .models import *


class infoSanteView(viewsets.ModelViewSet):
    permission_classes = (InfoSanteAccessPolicy,)
    serializer_class                    = infoSanteSerializer
    queryset                            = infoSante.objects.all()

    def perform_create(self, serializer):
        serializer.save(idUtilisateurIs=self.request.user)

class utilisateurInfoSanteView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (UtilisateurInfoSanteAccessPolicy,)
    serializer_class                    = infoSanteSerializer

    def get_queryset(self):
        idUtilisateurIs                 = self.kwargs['id']
        return infoSante.objects.filter(idUtilisateurIs=idUtilisateurIs).order_by('dateSaisie')
