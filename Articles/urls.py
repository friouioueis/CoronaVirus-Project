from rest_framework import routers

from Articles import views

router = routers.DefaultRouter()
router.register(r'articles', views.articleView,basename='articles')
router.register(r'videos_articles', views.articleView, basename='videos_articles')
router.register(r'photos_articles', views.articleView, basename='photos_articles')
router.register(r'commentaires', views.articleView, basename='commentaires')


urlpatterns = router.urls
