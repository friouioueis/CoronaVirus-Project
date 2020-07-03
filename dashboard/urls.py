from rest_framework import routers

from dashboard import views

router = routers.DefaultRouter()
router.register(r'dashboard', views.dashboard, basename='stats')
urlpatterns = router.urls