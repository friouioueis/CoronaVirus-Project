from rest_framework import routers

from Articles import views

router = routers.DefaultRouter()
router.register(r'articles', views.articleView, basename='articles')
router.register(r'videos_articles', views.articleView, basename='videos_articles')
router.register(r'photos_articles', views.articleView, basename='photos_articles')
router.register(r'commentaires', views.articleView, basename='commentaires')
router.register(r'video', views.videoThematiqueView, basename='video')
router.register(r'redacteurArticles/(?P<id>.+)', views.redacteurArticlesView,basename='redacteurArticles')
router.register(r'articleComs/(?P<id>.+)', views.articleCommentairesView,basename='articleComs')
router.register(r'articleVideoss/(?P<id>.+)', views.articleVideosView,basename='articleVideoss')
router.register(r'articlePhotos/(?P<id>.+)', views.articlePhotosView,basename='articlePhotos')
router.register(r'moderateur/(?P<id>.+)/valid', views.ModerateurValidView, basename='moderateur-valid')
router.register(r'moderateur/(?P<id>.+)/refus', views.ModerateurRefusView, basename='moderateur-refus')
router.register(r'valid', views.ArticleValidView, basename='articles-valid')
router.register(r'refus', views.ArticleRefusView, basename='articles-refus')
router.register(r'utilisateur/(?P<id>.+)/videos', views.VideoUtilisateurView, basename='utilisateur-videos')

urlpatterns = router.urls
