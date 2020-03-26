from rest_framework import viewsets
from .serializers import *
from .models import *


class signalementView(viewsets.ModelViewSet):
    serializer_class = signalementSerializer
    queryset = signalement.objects.all()


class selfPhotoView(viewsets.ModelViewSet):
    serializer_class = selfPhotoSerializer
    queryset = selfPhoto.objects.all()


class videoThematiqueView(viewsets.ModelViewSet):
    serializer_class = videoThematiqueSerializer
    queryset = videoThematique.objects.all()
