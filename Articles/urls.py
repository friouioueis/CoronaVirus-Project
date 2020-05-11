from rest_framework import routers

from Articles import views

router = routers.DefaultRouter()
router.register(r'articles', views.articleView, basename='articles')
router.register(r'articlesTermines',views.articleTermineView,basename='articlesTermines')
router.register(r'articlesValides',views.articleValideView,basename='articlesValides')
router.register(r'videos_articles', views.videoArticleView, basename='videos_articles')
router.register(r'photos_articles', views.photoArticleView, basename='photos_articles')
router.register(r'commentaires', views.commentaireView, basename='commentaires')
router.register(r'video', views.videoThematiqueView, basename='video')
router.register(r'redacteur/(?P<id>.+)/articles', views.redacteurArticlesView, basename='redacteurArticles')
router.register(r'article/(?P<id>.+)/commentaires', views.articleCommentairesView, basename='articleComs')
router.register(r'article/(?P<id>.+)/videos', views.articleVideosView, basename='articleVideos')
router.register(r'article/(?P<id>.+)/photos', views.articlePhotosView, basename='articlePhotos')
router.register(r'moderateur/(?P<id>.+)/valid', views.ModerateurValidView, basename='moderateur-valid')
router.register(r'moderateur/(?P<id>.+)/refus', views.ModerateurRefusView, basename='moderateur-refus')
router.register(r'valid', views.ArticleValidView, basename='articles-valid')
router.register(r'refus', views.ArticleRefusView, basename='articles-refus')
router.register(r'utilisateur/(?P<id>.+)/videos', views.VideoUtilisateurView, basename='utilisateur-videos')


urlpatterns = router.urls
