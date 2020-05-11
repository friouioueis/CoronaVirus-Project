from rest_framework import routers

from Region import views

router = routers.DefaultRouter()
router.register(r'regions', views.regionView,basename='regions')
router.register(r'stat_regions', views.statistiqueRegionView, basename='stat_regions')
router.register(r'stat_valid_regions', views.statistiqueRegionValideView, basename='stat_valid_regions')
router.register(r'region/(?P<id>.+)/statistics',views.regionStatsView,basename='regionStats')


urlpatterns = router.urls
