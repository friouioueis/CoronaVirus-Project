from rest_framework import viewsets
from .serializers import *
from .models import *


class regionView(viewsets.ModelViewSet):
    serializer_class = regionSerializer
    queryset = region.objects.all()


class statistiqueRegionView(viewsets.ModelViewSet):
    serializer_class = statistiqueRegionSerializer
    queryset = statistiqueRegion.objects.all()