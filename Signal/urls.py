from rest_framework import routers

from Signal import views

router = routers.DefaultRouter()
router.register(r'signal', views.signalementView,basename='signal')
router.register(r'self_photo', views.selfPhotoView, basename='self_photo')
router.register(r'utilisateur/(?P<id>.+)/signals',views.utilisateurSignalsView,basename='utilisateurSignals')
router.register(r'utilisateur/(?P<id>.+)/photos',views.utilisateurPhotosView,basename='utilisateurPhotos')
router.register(r'moderateur/(?P<id>.+)/valid', views.SignalModerValidView, basename='moderateur-valid')
router.register(r'moderateur/(?P<id>.+)/refus', views.SignalModerRefusView, basename='moderateur-refus')
router.register(r'valid', views.SignalementValidView, basename='signal-valid')
router.register(r'refus', views.SignalementRefusView, basename='signal-refus')

urlpatterns = router.urls
