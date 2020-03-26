from rest_framework import viewsets
from .serializers import *
from .models import *


class notifUtilisateurView(viewsets.ModelViewSet):
    serializer_class = notifUtilisateurSerializer
    queryset = notifUtilisateur.objects.all()