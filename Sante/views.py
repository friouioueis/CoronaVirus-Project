from rest_framework import viewsets
from .serializers import *
from .models import *


class infoSanteView(viewsets.ModelViewSet):
    serializer_class = infoSanteSerializer
    queryset = infoSante.objects.all()
