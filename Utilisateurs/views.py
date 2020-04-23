from django.contrib.auth.models import Group
from rest_framework import viewsets
from .serializers import *
from .models import *


class compteUtilisateurView(viewsets.ModelViewSet):
    serializer_class                    = compteUtilisateurSerializer
    queryset                            = compteUtilisateur.objects.all()

class roleView(viewsets.ModelViewSet):
    serializer_class                    = roleSerializer
    queryset                            = role.objects.all()

    def create(self, request):
        role.addRole(request.data['idUtilisateurR'], request.data['Type'])
        return super().create(request)

    def destroy(self, request, *args, **kwargs):
        role.deleteRole(self.get_object().idUtilisateurR,self.get_object().Type)
        return super().destroy(request)


class infoPersonelView(viewsets.ModelViewSet):
    serializer_class                    = infoPersonelSerializer
    queryset                            = infoPersonel.objects.all()


class utilisateurRolesView(viewsets.ModelViewSet):
    serializer_class                    = roleSerializer

    def get_queryset(self):
        idUtilisateurR                  = self.kwargs['id']
        return role.objects.filter(idUtilisateurR=idUtilisateurR)

    def create(self, request, *args, **kwargs):
        group = Group.objects.get(name=request.data['Type'])
        compteUtilisateur.objects.get(id=request.data['idUtilisateurR']).groups.add(group)
        return super().create(request)

    def destroy(self, request, *args, **kwargs):
        group = Group.objects.get(name=self.get_object().Type)
        group.user_set.remove(self.get_object().idUtilisateurR)
        return super().destroy(request)


class utilisateurInfosView(viewsets.ModelViewSet):
    serializer_class                    = infoPersonelSerializer

    def get_queryset(self):
        idUtilisateurR                  = self.kwargs['id']
        return infoPersonel.objects.filter(idUtilisateurR=idUtilisateurR)