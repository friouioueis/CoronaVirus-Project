from rest_framework import routers

from Notifications import views

router = routers.DefaultRouter()
router.register(r'notifs', views.notifUtilisateurView,basename='notifs')

urlpatterns = router.urls
