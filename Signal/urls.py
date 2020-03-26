from rest_framework import routers

from Signal import views

router = routers.DefaultRouter()
router.register(r'signal', views.signalementView,basename='signal')
router.register(r'self_photo', views.selfPhotoView, basename='self_photo')
router.register(r'video', views.videoThematiqueView, basename='video')


urlpatterns = router.urls
