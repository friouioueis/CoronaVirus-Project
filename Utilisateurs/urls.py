from rest_framework import routers

from Utilisateurs import views

router = routers.DefaultRouter()
router.register(r'comptes', views.compteUtilisateurView,basename='comptes')
router.register(r'roles', views.roleView, basename='roles')
router.register(r'infos', views.infoPersonelView, basename='infos')
router.register(r'utilisateurRoles/(?P<id>.+)',views.utilisateurRolesView,basename='utilisateurRoles')
router.register(r'utilisateurInfos/(?P<id>.+)',views.utilisateurInfosView,basename='utilisateurInfos')


urlpatterns = router.urls
