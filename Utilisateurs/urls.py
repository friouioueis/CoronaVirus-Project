from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from Utilisateurs import views

router = routers.DefaultRouter()
router.register(r'comptes', views.compteUtilisateurView,basename='comptes')
router.register(r'roles', views.roleView, basename='roles')
router.register(r'infos', views.infoPersonelView, basename='infos')
router.register(r'utilisateur/(?P<id>.+)/roles',views.utilisateurRolesView,basename='utilisateurRoles')
router.register(r'utilisateur/(?P<id>.+)/infos',views.utilisateurInfosView,basename='utilisateurInfos')


urlpatterns = router.urls
urlpatterns = [
    url(r'gestionComptes',include(router.urls)),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
]