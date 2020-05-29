from rest_framework import routers

from Robots import views

router = routers.DefaultRouter()
router.register(r'facebook', views.pubFacebookView,basename='facebook')
router.register(r'youtube', views.pubYoutubeView, basename='youtube')
router.register(r'web', views.pubSiteWebView, basename='web')
router.register(r'pub/facebook/sorted', views.SortedpubFacebookView, basename='facebook-sorted')
router.register(r'pub/youtube/sorted', views.SortedpubYoutubeView, basename='youtube-sorted')
router.register(r'pub/web/sorted', views.SortedpubSiteWebView, basename='web-sorted')
router.register(r'spider', views.RunSpiderView, basename='spider')



urlpatterns = router.urls
