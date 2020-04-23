from rest_framework import viewsets
from .serializers import *
from .models import *


class notifUtilisateurView(viewsets.ModelViewSet):
    serializer_class                    = notifUtilisateurSerializer
    queryset                            = notifUtilisateur.objects.all()


class utilisateurNotifsView(viewsets.ModelViewSet):
    serializer_class                    = notifUtilisateurSerializer

    def get_queryset(self):
        idUtilisateurNf                 = self.kwargs['id']
        return notifUtilisateur.objects.filter(idUtilisateurNf=idUtilisateurNf)