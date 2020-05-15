import json

from django.contrib.auth.models import Group
from django.forms import model_to_dict
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from Utilisateurs.models import role
from .factories import *
from .models import *

class ArticleList(APITestCase):

    def setUp(self):
        self.user = compteUtilisateurFactory()
        self.user2 = compteUtilisateurFactory()
        Group.objects.get_or_create(name='rd')
        role.addRole(self.user.id, 'rd')
        Group.objects.get_or_create(name='md')
        role.addRole(self.user2.id, 'md')
        for i in range(2):
            ArticleFactory()

    def test_article_list_authorized(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            reverse('articles-list')
        )
        expected = 2

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)

    def test_article_list_unauthorized(self):
        self.client.force_authenticate(user=self.user2)
        response = self.client.get(
                reverse('articles-list')
            )
        expected = 2

        self.assertEqual(
                response.status_code, status.HTTP_403_FORBIDDEN)

class ArticleTermineList(APITestCase):

    def setUp(self):
        self.user = compteUtilisateurFactory()
        self.user2= compteUtilisateurFactory()
        Group.objects.get_or_create(name='md')
        role.addRole(self.user.id, 'md')
        ArticleFactory(terminerAR=False)
        for i in range(2):
            ArticleFactory(terminerAR=True)

    def test_article_termine_list_authorized(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            reverse('articlesTermines-list')
        )
        expected = 2

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)
    def test_article_termine_list_unauthorized(self):
        self.client.force_authenticate(user=self.user2)
        response = self.client.get(
            reverse('articlesTermines-list')
        )

        self.assertEqual(
            response.status_code, status.HTTP_403_FORBIDDEN)

class ArticleValideList(APITestCase):

    def setUp(self):
        self.user = compteUtilisateurFactory()
        ArticleFactory(validerAR=False)
        for i in range(2):
            ArticleFactory(validerAR=True)

    def test_article_valide_list(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            reverse('articlesValides-list')
        )
        expected = 2

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)

class ArticleGet(APITestCase):

    def setUp(self):
        self.user = compteUtilisateurFactory()
        Group.objects.get_or_create(name='rd')
        role.addRole(self.user.id, 'rd')
        self.article = ArticleFactory(contenuAr='contenu')

    def test_article_found(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('articles-detail',  kwargs={'pk':self.article.idArticle}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('contenuAr'), self.article.contenuAr)

    def test_article_not_found(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('articles-detail',  kwargs={'pk':10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class ArticleDelete(APITestCase):
    def setUp(self):
        self.user1 = compteUtilisateurFactory()
        self.user2 = compteUtilisateurFactory()
        Group.objects.get_or_create(name='rd')
        role.addRole(self.user2.id, 'rd')
        self.article = ArticleFactory(idRedacteurAr=self.user2)

    def test_article_delete_authorized(self):

        before_list_amount = article.objects.count()
        url = reverse('articles-detail', kwargs={'pk': self.article.idArticle})
        self.client.force_authenticate(user=self.user2)
        response=self.client.delete(url)
        after_list_amount = article.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(before_list_amount-after_list_amount, 1)

    def test_article_delete_unauthorized(self):

        before_list_amount = article.objects.count()
        url = reverse('articles-detail', kwargs={'pk': self.article.idArticle})
        self.client.force_authenticate(user=self.user1)
        response=self.client.delete(url)
        after_list_amount = article.objects.count()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(before_list_amount-after_list_amount, 0)

class ArticleUpdate(APITestCase):
    def setUp(self):
        self.user1 = compteUtilisateurFactory()
        self.user2 = compteUtilisateurFactory()
        self.user3 = compteUtilisateurFactory()
        Group.objects.get_or_create(name='rd')
        role.addRole(self.user2.id, 'rd')
        role.addRole(self.user3.id,'rd')
        self.article = ArticleFactory(idRedacteurAr=self.user2)

    def test_article_update_authorized(self):

        self.article.contenuAr = "updated"
        url = reverse('articles-detail', kwargs={'pk': self.article.idArticle})
        self.client.force_authenticate(user=self.user2)
        response=self.client.put(url,{'contenuAr':self.article.contenuAr,'dateAr':self.article.dateAr,'terminerAR':self.article.terminerAR})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('contenuAr'), self.article.contenuAr)


    def test_article_update_unauthorized1(self):

        self.article.contenuAr = "updated"
        url = reverse('articles-detail', kwargs={'pk': self.article.idArticle})
        self.client.force_authenticate(user=self.user1)
        response=self.client.put(url,{'contenuAr':self.article.contenuAr,'dateAr':self.article.dateAr})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_article_update_unauthorized2(self):

        self.article.contenuAr = "updated"
        url = reverse('articles-detail', kwargs={'pk': self.article.idArticle})
        self.client.force_authenticate(user=self.user3)
        response=self.client.put(url,{'contenuAr':self.article.contenuAr,'dateAr':self.article.dateAr,'terminerAR':self.article.terminerAR})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class ArticleValider(APITestCase):

    def setUp(self):
        self.user = compteUtilisateurFactory()
        self.user1 = compteUtilisateurFactory()
        Group.objects.get_or_create(name='md')
        role.addRole(self.user.id, 'md')
        self.article = ArticleFactory()

    def test_article_validate_authorized(self):

        self.article.validerAR = 'True'
        url = reverse('articles-detail', kwargs={'pk': self.article.idArticle})
        self.client.force_authenticate(user=self.user)
        response=self.client.patch(url,{'validerAR':self.article.validerAR,'idModerateurAr':self.user.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('validerAR'), self.article.validerAR)

    def test_article_validate_unauthorized(self):

        self.article.validerAR = True
        url = reverse('articles-detail', kwargs={'pk': self.article.idArticle})
        self.client.force_authenticate(user=self.user1)
        response=self.client.patch(url,{'validerAR':self.article.validerAR,'idModerateurAr':self.user1.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class ArticleCreate(APITestCase):

    def setUp(self):
        self.user1 = compteUtilisateurFactory()
        self.user2 = compteUtilisateurFactory()
        Group.objects.get_or_create(name='rd')
        role.addRole(self.user2.id, 'rd')

    def test_article_create_authorized(self):
        article1 = ArticleFactory(idRedacteurAr=self.user2)
        dict=model_to_dict(article1)

        url = reverse('articles-list')
        self.client.force_authenticate(user=self.user2)
        before_list_amount = article.objects.count()
        response = self.client.post(url,dict,format='json')
        after_list_amount = article.objects.count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(after_list_amount - before_list_amount, 1)


    def test_article_create_unauthorized(self):
        article2 = ArticleFactory(idArticle=5)
        dict=model_to_dict(article2)

        url = reverse('articles-list')
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(url,dict,format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class VideoArticleList(APITestCase):

    def setUp(self):
        for i in range(4):
            VideoArticleFactory()

    def test_videoArticle_list(self):
        response = self.client.get(
            reverse('videos_articles-list')
        )
        expected = 4

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)

class VideoArticleGet(APITestCase):

    def setUp(self):
        self.article = ArticleFactory()
        self.video = VideoArticleFactory(idArticleVd=self.article)

    def test_videoArticle_found(self):
        response = self.client.get(reverse('videos_articles-detail', kwargs={'pk': self.video.idVideo}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('idVideo'), self.video.idVideo)

    def test_videoArticle_not_found(self):
        response = self.client.get(reverse('videos_articles-detail', kwargs={'pk': 10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class VideoArticleDelete(APITestCase):
    def setUp(self):
        self.user1 = compteUtilisateurFactory()
        self.user2 = compteUtilisateurFactory()
        Group.objects.get_or_create(name='rd')
        role.addRole(self.user2.id, 'rd')
        self.article = ArticleFactory(idRedacteurAr=self.user2)
        self.video = VideoArticleFactory(idArticleVd=self.article)

    def test_videoArticle_delete_authorized(self):

        before_list_amount = videoArticle.objects.count()
        url = reverse('videos_articles-detail', kwargs={'pk': self.video.idVideo})
        self.client.force_authenticate(user=self.user2)
        response = self.client.delete(url)
        after_list_amount = videoArticle.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(before_list_amount - after_list_amount, 1)

    def test_videoArticle_delete_unauthorized(self):

        before_list_amount = videoArticle.objects.count()
        url = reverse('videos_articles-detail', kwargs={'pk': self.video.idVideo})
        self.client.force_authenticate(user=self.user1)
        response = self.client.delete(url)
        after_list_amount = videoArticle.objects.count()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(before_list_amount - after_list_amount, 0)

class PhotoArticleList(APITestCase):

    def setUp(self):
        for i in range(4):
            PhotoArticleFactory()

    def test_photoArticle_list(self):
        response = self.client.get(
            reverse('photos_articles-list')
        )
        expected = 4

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)

class PhotoArticleGet(APITestCase):

    def setUp(self):
        self.article = ArticleFactory()
        self.photo = PhotoArticleFactory(idArticlePh=self.article)

    def test_photoArticle_found(self):
        response = self.client.get(reverse('photos_articles-detail', kwargs={'pk': self.photo.idPhoto}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('idPhoto'), self.photo.idPhoto)

    def test_photoArticle_not_found(self):
        response = self.client.get(reverse('photos_articles-detail', kwargs={'pk': 10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class PhotoArticleDelete(APITestCase):
    def setUp(self):
        self.user1 = compteUtilisateurFactory()
        self.user2 = compteUtilisateurFactory()
        Group.objects.get_or_create(name='rd')
        role.addRole(self.user2.id, 'rd')
        self.article = ArticleFactory(idRedacteurAr=self.user2)
        self.photo = PhotoArticleFactory(idArticlePh=self.article)

    def test_videoArticle_delete_authorized(self):

        before_list_amount = photoArticle.objects.count()
        url = reverse('photos_articles-detail', kwargs={'pk': self.photo.idPhoto})
        self.client.force_authenticate(user=self.user2)
        response = self.client.delete(url)
        after_list_amount = photoArticle.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(before_list_amount - after_list_amount, 1)

    def test_videoArticle_delete_unauthorized(self):

        before_list_amount = photoArticle.objects.count()
        url = reverse('videos_articles-detail', kwargs={'pk': self.photo.idPhoto})
        self.client.force_authenticate(user=self.user1)
        response = self.client.delete(url)
        after_list_amount = photoArticle.objects.count()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(before_list_amount - after_list_amount, 0)

class CommentaireList(APITestCase):

    def setUp(self):
        for i in range(4):
            CommentaireFactory()

    def test_article_list(self):
        response = self.client.get(
            reverse('commentaires-list')
        )
        expected = 4

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)

class CommentaireGet(APITestCase):

    def setUp(self):
        self.commentaire = CommentaireFactory()

    def test_commentaire_found(self):
        response = self.client.get(reverse('commentaires-detail', kwargs={'pk': self.commentaire.idCommentaire}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('contenuCom'), self.commentaire.contenuCom)

    def test_commentaire_not_found(self):
        response = self.client.get(reverse('commentaires-detail', kwargs={'pk': 10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CommentaireDelete(APITestCase):
    def setUp(self):
        self.user = compteUtilisateurFactory()
        self.user2 = compteUtilisateurFactory()
        self.commentaire = CommentaireFactory(idUtilisateurCom=self.user)

    def test_commentaire_delete_authorized(self):
        before_list_amount = commentaire.objects.count()
        url = reverse('commentaires-detail', kwargs={'pk': self.commentaire.idCommentaire})
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        after_list_amount = commentaire.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(before_list_amount - after_list_amount, 1)

    def test_commentaire_delete_unauthorized(self):
        before_list_amount = commentaire.objects.count()
        url = reverse('commentaires-detail', kwargs={'pk': self.commentaire.idCommentaire})
        self.client.force_authenticate(user=self.user2)
        response = self.client.delete(url)
        after_list_amount = commentaire.objects.count()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(before_list_amount - after_list_amount, 0)

class CommentaireModifier(APITestCase):
    def setUp(self):
        self.user = compteUtilisateurFactory()
        self.user2 = compteUtilisateurFactory()
        self.commentaire = CommentaireFactory(idUtilisateurCom=self.user)

    def test_commentaire_modifier_authorized(self):
        self.commentaire.contenuCom = "nouveau contenu"
        url = reverse('commentaires-modifier', kwargs={'pk': self.commentaire.idCommentaire})
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, {'contenuCom': self.commentaire.contenuCom})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('contenuCom'), self.commentaire.contenuCom)

    def test_commentaire_modifier_unauthorized(self):
        self.commentaire.contenuCom = "nouveau contenu"
        url = reverse('commentaires-modifier', kwargs={'pk': self.commentaire.idCommentaire})
        self.client.force_authenticate(user=self.user2)
        response = self.client.patch(url, {'contenuCom': self.commentaire.contenuCom})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class CommentaireSignaler(APITestCase):

    def setUp(self):
        self.user = compteUtilisateurFactory()
        self.commentaire = CommentaireFactory()

    def test_commentaire_signaler(self):

        self.commentaire.signalerCom=True
        url = reverse('commentaires-signaler', kwargs={'pk': self.commentaire.idCommentaire})
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, {'signalerCom': self.commentaire.signalerCom})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('signalerCom'), str(self.commentaire.signalerCom))

class CommentaireUpdate(APITestCase):

    def setUp(self):
        self.user = compteUtilisateurFactory()
        self.commentaire = CommentaireFactory()

    def test_commentaire_update_unauthorized(self):
        c = CommentaireFactory(idCommentaire=19, idUtilisateurCom=self.user)

        c.contenuCom = "nouveau contenu"
        url = reverse('commentaires-detail', kwargs={'pk': c.idCommentaire})
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, {'contenuCom': c.contenuCom})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class CommentaireCreate(APITestCase):

    def setUp(self):
        self.user = compteUtilisateurFactory()

    def test_commentaire_create(self):
        c = CommentaireFactory(idUtilisateurCom=self.user)
        dict = model_to_dict(c)

        url = reverse('commentaires-list')
        self.client.force_authenticate(user=self.user)
        before_list_amount = commentaire.objects.count()
        response = self.client.post(url, dict, format='json')
        after_list_amount = commentaire.objects.count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(after_list_amount - before_list_amount, 1)

class RedacteurArticleList(APITestCase):

    def setUp(self):
        self.user = compteUtilisateurFactory()
        Group.objects.get_or_create(name='rd')
        role.addRole(self.user.id, 'rd')
        for i in range(4):
            ArticleFactory(idRedacteurAr=self.user)

    def test_redacteur_article_list(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            reverse('redacteurArticles-list', kwargs={'id': self.user.id})
        )
        expected = 4

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)

class RedacteurArticleGet(APITestCase):

    def setUp(self):
        self.user = compteUtilisateurFactory()
        Group.objects.get_or_create(name='rd')
        role.addRole(self.user.id, 'rd')
        self.article = ArticleFactory(contenuAr='contenu',idRedacteurAr=self.user)

    def test_redacteur_article_found(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('redacteurArticles-detail',  kwargs={'id':self.user.id,'pk':self.article.idArticle}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('contenuAr'), self.article.contenuAr)

    def test_redacteur_article_not_found(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('redacteurArticles-detail',  kwargs={'id':self.user.id,'pk':20}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class ArticleCommentaireList(APITestCase):

    def setUp(self):
        self.article=ArticleFactory()
        for i in range(4):
            CommentaireFactory(idArticleCom=self.article)

    def test_article_commentaires_list(self):
        response = self.client.get(
            reverse('articleComs-list', kwargs={'id': self.article.idArticle})
        )
        expected = 4

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)

class ArticleCommentaireGet(APITestCase):

    def setUp(self):
        self.article = ArticleFactory()
        self.commentaire = CommentaireFactory(idArticleCom=self.article)

    def test_commentaire_found(self):
        response = self.client.get(reverse('articleComs-detail', kwargs={'id': self.article.idArticle,'pk': self.commentaire.idCommentaire}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('contenuCom'), self.commentaire.contenuCom)

    def test_commentaire_not_found(self):
        response = self.client.get(reverse('articleComs-detail',kwargs={'id': self.article.idArticle,'pk': 10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class ArticlePhotosList(APITestCase):

    def setUp(self):
        self.article=ArticleFactory()
        for i in range(4):
            PhotoArticleFactory(idArticlePh=self.article)

    def test_article_list(self):
        response = self.client.get(
            reverse('articlePhotos-list', kwargs={'id': self.article.idArticle})
        )
        expected = 4

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)

class ArticlePhotosGet(APITestCase):

    def setUp(self):
        self.article = ArticleFactory()
        self.photo = PhotoArticleFactory(idArticlePh=self.article)

    def test_article_video_found(self):
        response = self.client.get(reverse('articlePhotos-detail', kwargs={'id': self.article.idArticle,'pk': self.photo.idPhoto}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_article_video_not_found(self):
        response = self.client.get(reverse('articlePhotos-detail', kwargs={'id': self.article.idArticle,'pk': 10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class ArticleVideosList(APITestCase):

    def setUp(self):
        self.article=ArticleFactory()
        for i in range(4):
            VideoArticleFactory(idArticleVd=self.article)

    def test_article_list(self):
        response = self.client.get(
            reverse('articleVideos-list', kwargs={'id': self.article.idArticle})
        )
        expected = 4

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)

class ArticleVideosGet(APITestCase):

    def setUp(self):
        self.article = ArticleFactory()
        self.video = VideoArticleFactory(idArticleVd=self.article)

    def test_commentaire_found(self):
        response = self.client.get(reverse('articleVideos-detail', kwargs={'id': self.article.idArticle,'pk': self.video.idVideo}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_commentaire_not_found(self):
        response = self.client.get(reverse('articleVideos-detail', kwargs={'id': self.article.idArticle,'pk': 10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class ModerateurArticlesVList(APITestCase):
    def setUp(self):
        self.user=compteUtilisateurFactory()
        Group.objects.get_or_create(name='md')
        role.addRole(self.user.id, 'md')
        for i in range(4):
            ArticleFactory(idModerateurAr=self.user,validerAR=True)

    def test_moderateur_articleV_list(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            reverse('moderateur-valid-list', kwargs={'id': self.user.id})
        )
        expected = 4
        print(article.objects.count())
        print(self.ar.validerAR)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)

class ModerateurArticlesRList(APITestCase):
    def setUp(self):
        self.user = compteUtilisateurFactory()
        Group.objects.get_or_create(name='md')
        role.addRole(self.user.id, 'md')
        for i in range(4):
            ArticleFactory(idModerateurAr=self.user, validerAR=False)
    def test_moderateur_articleR_list(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            reverse('moderateur-refus-list', kwargs={'id': self.user.id})
        )
        expected = 4

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)



