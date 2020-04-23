from rest_framework import routers

from Notifications import views

router = routers.DefaultRouter()
router.register(r'notifs', views.notifUtilisateurView, basename='notifs')
router.register(r'Utilisateur/(?P<id>.+)/notifs', views.utilisateurNotifsView, basename='UtilisateurNotifs')

urlpatterns = router.urls
