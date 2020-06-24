from rest_framework import routers

from Robots import views

router = routers.DefaultRouter()
router.register(r'youtube', views.pubYoutubeView, basename='youtube')
router.register(r'pub/youtube/sorted', views.SortedpubYoutubeView, basename='youtube-sorted')
router.register(r'googleNews', views.pubGNView, basename='googleNews')
router.register(r'pub/googleNews/sorted', views.SortedpubGNView, basename='googleNews-sorted')
router.register(r'articles', views.ArticlesView, basename='articles')
router.register(r'articles/sorted', views.SortedArticlesView, basename='articles-sorted')
router.register(r'spider', views.RunSpiderView, basename='spider')



urlpatterns = router.urls
