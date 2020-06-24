from rest_framework import routers

from Signal import views

router = routers.DefaultRouter()
router.register(r'signal', views.signalementView,basename='signal')
router.register(r'signal_non_valide', views.signalementNonValideView,basename='signal_non_valide')
router.register(r'self_photo', views.selfPhotoView, basename='self_photo')
router.register(r'utilisateur/(?P<id>.+)/signals',views.utilisateurSignalsView,basename='utilisateurSignals')
router.register(r'utilisateur/(?P<id>.+)/photos',views.utilisateurPhotosView,basename='utilisateurPhotos')
router.register(r'moderateur/(?P<id>.+)/signals', views.SignalModerView, basename='moderateur-signals')
router.register(r'valid', views.SignalementValidView, basename='signal-valid')
router.register(r'refus', views.SignalementRefusView, basename='signal-refus')
router.register(r'email',views.emailView,basename='email')

urlpatterns = router.urls
