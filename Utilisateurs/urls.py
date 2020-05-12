from django.conf.urls import url
from django.urls import path
from django.urls import include
from rest_framework import routers

from Utilisateurs import views

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


router = routers.DefaultRouter()
router.register(r'comptes', views.compteUtilisateurView,basename='comptes')
router.register(r'roles', views.roleView, basename='roles')
router.register(r'infos', views.infoPersonelView, basename='infos')
router.register(r'utilisateur/(?P<id>.+)/roles', views.utilisateurRolesView,basename='utilisateurRoles')
router.register(r'utilisateur/(?P<id>.+)/infos', views.utilisateurInfosView,basename='utilisateurInfos')


urlpatterns = [
    path('gestionComptes/', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
]
