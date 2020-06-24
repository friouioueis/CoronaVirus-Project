from rest_framework import routers

from Region import views

router = routers.DefaultRouter()
router.register(r'regions', views.regionView,basename='regions')
router.register(r'stat_regions', views.statistiqueRegionView, basename='stat_regions')
router.register(r'stat_regions_non_valid', views.statistiqueRegionNonValideView, basename='stat_regions_non_valid')
router.register(r'stat_valid_regions', views.statistiqueRegionValideView, basename='stat_valid_regions')
router.register(r'stat_refus_regions', views.statistiqueRegionRefuseView, basename='stat_refuse_regions')
router.register(r'region/(?P<id>.+)/statistics',views.regionStatsView,basename='regionStats')
router.register(r'moderateur/(?P<id>.+)/stats',views.ModerateurStatsView,basename='moderateur_stats')
router.register(r'agent/(?P<id>.+)/stats_refus',views.AgentStatsView,basename='agent_stats')


urlpatterns = router.urls
