from rest_framework import routers

from Articles import views

router = routers.DefaultRouter()
router.register(r'articles', views.articleView,basename='articles')
router.register(r'videos_articles', views.articleView, basename='videos_articles')
router.register(r'photos_articles', views.articleView, basename='photos_articles')
router.register(r'commentaires', views.articleView, basename='commentaires')
router.register(r'video', views.videoThematiqueView, basename='video')
router.register(r'redacteurArticles/(?P<id>.+)',views.redacteurArticlesView,basename='redacteurArticles')
router.register(r'articleComs/(?P<id>.+)',views.articleCommentairesView,basename='articleComs')
router.register(r'articleVideoss/(?P<id>.+)',views.articleVideosView,basename='articleVideoss')
router.register(r'articlePhotos/(?P<id>.+)',views.articlePhotosView,basename='articlePhotos')

urlpatterns = router.urls
