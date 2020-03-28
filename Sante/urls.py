from rest_framework import routers

from Sante import views

router = routers.DefaultRouter()
router.register(r'info_sante', views.infoSanteView,basename='info_sante')
router.register(r'utilisateurInfoSante/(?P<id>.+)',views.utilisateurInfoSanteView,basename='utilisateurInfoSante')
urlpatterns = router.urls
