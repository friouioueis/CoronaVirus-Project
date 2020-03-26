from rest_framework import routers

from Sante import views

router = routers.DefaultRouter()
router.register(r'info_sante', views.infoSanteView,basename='info_sante')

urlpatterns = router.urls
