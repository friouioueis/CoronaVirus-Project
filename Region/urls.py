from rest_framework import routers

from Region import views

router = routers.DefaultRouter()
router.register(r'regions', views.regionView,basename='regions')
router.register(r'stat_regions', views.statistiqueRegionView, basename='stat_regions')



urlpatterns = router.urls
