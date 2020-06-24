from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import viewsets

from .policies import SignalAccessPolicy, EmailAccessPolicy
from .serializers import *
from .models import *

from django.core.mail import send_mail, EmailMessage
from django.conf import settings

class emailView(viewsets.ModelViewSet):
    permission_classes = (EmailAccessPolicy,)
    serializer_class = emailSerializer
    queryset = emailCCC.objects.all()
    def perform_create(self, serializer):
        serializer.save()
        subject = serializer.data['subject']
        message = serializer.data['message']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = serializer.data['recipient_list'].split(',')
        email = EmailMessage(
            subject,
            message,
            email_from,
            recipient_list
        )
        email.attach_file(serializer.data['attach'])
        email.send()


class signalementView(viewsets.ModelViewSet):
    permission_classes          = (SignalAccessPolicy,)
    serializer_class            = signalementSerializer
    queryset                    = signalement.objects.all()

    def perform_create(self, serializer):
        serializer.save(idUtilisateurSg=self.request.user,validerSg=None,idModerateurSg=None)

    def partial_update(self, request, pk=None):
        s=self.get_object()
        s.validerSg=request.data["validerSg"]
        s.idModerateurSg_id=request.user.id
        s.save()
        return JsonResponse({"idSignal":s.idSignal,"validerSg":s.validerSg})

    def update(self, request, pk=None):
        s=self.get_object()
        s.descriptionSg=request.data["descriptionSg"]
        s.typeSg=request.data["typeSg"]
        s.lienSg=request.data["lienSg"]
        s.save()
        return JsonResponse({"idSignal": s.idSignal, "descriptionSg": s.descriptionSg,"typeSg":s.typeSg,"lienSg":s.lienSg})


class signalementNonValideView(viewsets.ReadOnlyModelViewSet):
    permission_classes          = (SignalAccessPolicy,)
    serializer_class            = signalementSerializer
    queryset                    = signalement.objects.filter(validerSg=None)


class utilisateurSignalsView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (SignalAccessPolicy,)
    serializer_class            = signalementSerializer

    def get_queryset(self):
        idUtilisateurSg         = self.kwargs['id']
        return signalement.objects.filter(idUtilisateurSg=idUtilisateurSg)


class SignalModerView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (SignalAccessPolicy,)
    serializer_class            = signalementSerializer

    def get_queryset(self):
        idModerateur            = self.kwargs['id']
        return signalement.objects.filter(idModerateurSg=idModerateur)


class SignalementValidView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (SignalAccessPolicy,)
    serializer_class            = signalementSerializer
    queryset                    = signalement.objects.filter(validerSg=True)

class SignalementRefusView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (SignalAccessPolicy,)
    serializer_class            = signalementSerializer
    queryset                    = signalement.objects.filter(validerSg=False)


class selfPhotoView(viewsets.ModelViewSet):
    serializer_class            = selfPhotoSerializer
    queryset                    = selfPhoto.objects.all()


class utilisateurPhotosView(viewsets.ReadOnlyModelViewSet):
    serializer_class            = selfPhotoSerializer

    def get_queryset(self):
        idUtilisateurSph        = self.kwargs['id']
        return selfPhoto.objects.filter(idUtilisateurSph=idUtilisateurSph)