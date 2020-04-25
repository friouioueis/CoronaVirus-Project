import json

from django.contrib.auth.models import Group
from django.forms import model_to_dict
from django.urls import path, include
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status

from Utilisateurs.models import role
from .factories import *
from .models import *


class TestArticle(APITestCase,URLPatternsTestCase):
    urlpatterns = [
        path('articles/', include('Articles.urls')),
    ]

    def setUp(self):
        self.user = compteUtilisateurFactory()

    def test_article_list(self):

        response = self.client.get(
            reverse('articles-list')
        )
        expected = 5

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)

    def test_article_found(self):

        ar=ArticleFactory(idArticle=1,contenuAr='contenu')

        response = self.client.get(reverse('articles-detail',  kwargs={'pk':ar.idArticle}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('contenuAr'), ar.contenuAr)

    def test_article_not_found(self):

        response = self.client.get(reverse('articles-detail',  kwargs={'pk':10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_article_delete_authorized(self):


        Group.objects.get_or_create(name='rd')
        role.addRole(self.user.id,'rd')
        ar = ArticleFactory(idArticle=2,idRedacteurAr=self.user)

        before_list_amount = article.objects.count()
        url = reverse('articles-detail', kwargs={'pk': ar.idArticle})
        self.client.force_authenticate(user=self.user)
        response=self.client.delete(url)
        after_list_amount = article.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(before_list_amount-after_list_amount, 1)

    def test_article_delete_unauthorized(self):

        ar = ArticleFactory()

        before_list_amount = article.objects.count()
        url = reverse('articles-detail', kwargs={'pk': ar.idArticle})
        self.client.force_authenticate(user=self.user)
        response=self.client.delete(url)
        after_list_amount = article.objects.count()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(before_list_amount-after_list_amount, 0)

    def test_article_update_authorized(self):

        Group.objects.get_or_create(name='rd')
        role.addRole(self.user.id,'rd')
        ar = ArticleFactory(idArticle=3,idRedacteurAr=self.user)

        ar.contenuAr = "updated"
        url = reverse('articles-detail', kwargs={'pk': ar.idArticle})
        self.client.force_authenticate(user=self.user)
        response=self.client.put(url,{'contenuAr':ar.contenuAr,'dateAr':ar.dateAr,'terminerAR':ar.terminerAR})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('contenuAr'), ar.contenuAr)


    def test_article_update_unauthorized(self):

        ar = ArticleFactory(idArticle=14,idRedacteurAr=self.user)

        ar.contenuAr = "updated"
        url = reverse('articles-detail', kwargs={'pk': ar.idArticle})
        self.client.force_authenticate(user=self.user)
        response=self.client.put(url,{'contenuAr':ar.contenuAr,'dateAr':ar.dateAr})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)



    def test_article_validate_authorized(self):

        Group.objects.get_or_create(name='md')
        role.addRole(self.user.id,'md')
        ar = ArticleFactory(idArticle=5)

        ar.validerAR = 'True'
        url = reverse('articles-detail', kwargs={'pk': ar.idArticle})
        self.client.force_authenticate(user=self.user)
        response=self.client.patch(url,{'validerAR':ar.validerAR,'idModerateurAr':self.user.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('validerAR'), ar.validerAR)



    def test_article_validate_unauthorized(self):

        Group.objects.get_or_create(name='si')
        role.addRole(self.user.id,'si')
        ar = ArticleFactory(idArticle=6)

        ar.validerAR = True
        url = reverse('articles-detail', kwargs={'pk': ar.idArticle})
        self.client.force_authenticate(user=self.user)
        response=self.client.patch(url,{'validerAR':ar.validerAR,'idModerateurAr':self.user.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_article_create_authorized(self):

        Group.objects.get_or_create(name='rd')
        role.addRole(self.user.id, 'rd')
        ar = ArticleFactory(idArticle=7, idRedacteurAr=self.user)
        dict=model_to_dict(ar)
        dict['dateAr']=dict['dateAr'].strftime("%Y-%m-%dT%H:%M:%S.%f")

        url = reverse('articles-list')
        self.client.force_authenticate(user=self.user)
        before_list_amount = article.objects.count()
        response = self.client.post(url,dict,format='json')
        print(response)
        after_list_amount = article.objects.count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(after_list_amount - before_list_amount, 1)


    def test_article_create_unauthorized(self):

        Group.objects.get_or_create(name='rd')
        role.deleteRole(self.user.id, 'rd')
        ar = ArticleFactory(idArticle=18)
        dict=model_to_dict(ar)
        dict['dateAr']=dict['dateAr'].strftime("%Y-%m-%dT%H:%M:%S.%f")

        url = reverse('articles-list')
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url,dict,format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestVideoArticle(APITestCase,URLPatternsTestCase):
    urlpatterns = [
        path('articles/', include('Articles.urls')),
    ]

    def setUp(self):
        self.user = compteUtilisateurFactory()
        self.ar = ArticleFactory()

    def test_video_list(self):

        for i in range(2):
            VideoArticleFactory(idVideo=1+i,idArticleVd=self.ar)


        response = self.client.get(
            reverse('videos_articles-list')
        )
        expected = 4
        print(response.content)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)

    def test_video_found(self):

        v=VideoArticleFactory(idVideo=3,idArticleVd=self.ar)
        print(v.idVideo)
        response = self.client.get(reverse('videos_articles-detail',  kwargs={'pk':v.idVideo}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('idArticleVd'), self.ar.idArticle)

    def test_video_not_found(self):

        response = self.client.get(reverse('videos_articles-detail',  kwargs={'pk':10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_video_delete_authorized(self):

        Group.objects.get_or_create(name='rd')
        role.addRole(self.user.id,'rd')
        ar = ArticleFactory(idArticle=12, idRedacteurAr=self.user)
        v = VideoArticleFactory(idVideo=4, idArticleVd=ar)

        before_list_amount = videoArticle.objects.count()
        url = reverse('videos_articles-detail', kwargs={'pk': v.idVideo})
        self.client.force_authenticate(user=self.user)
        response=self.client.delete(url)
        after_list_amount = videoArticle.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(before_list_amount-after_list_amount, 1)

    def test_video_delete_unauthorized(self):

        v = VideoArticleFactory(idVideo=5)

        before_list_amount = videoArticle.objects.count()
        url = reverse('videos_articles-detail', kwargs={'pk': v.idVideo})
        self.client.force_authenticate(user=self.user)
        response=self.client.delete(url)
        after_list_amount = videoArticle.objects.count()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(before_list_amount-after_list_amount, 0)



class TestPhotoArticle(APITestCase,URLPatternsTestCase):
    urlpatterns = [
        path('articles/', include('Articles.urls')),
    ]

    def setUp(self):
        self.user = compteUtilisateurFactory()
        self.ar = ArticleFactory()

    def test_video_list(self):

        for i in range(2):
            PhotoArticleFactory(idPhoto=1+i,idArticlePh=self.ar)


        response = self.client.get(
            reverse('photos_articles-list')
        )
        expected = 4
        print(response.content)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)

    def test_video_found(self):

        v=PhotoArticleFactory(idPhoto=3,idArticlePh=self.ar)
        response = self.client.get(reverse('photos_articles-detail',  kwargs={'pk':v.idPhoto}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('idArticlePh'), self.ar.idArticle)

    def test_video_not_found(self):

        response = self.client.get(reverse('photos_articles-detail',  kwargs={'pk':10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_video_delete_authorized(self):

        Group.objects.get_or_create(name='rd')
        role.addRole(self.user.id,'rd')
        ar = ArticleFactory(idArticle=12, idRedacteurAr=self.user)
        v = PhotoArticleFactory(idPhoto=4, idArticlePh=ar)

        before_list_amount = photoArticle.objects.count()
        url = reverse('photos_articles-detail', kwargs={'pk': v.idPhoto})
        self.client.force_authenticate(user=self.user)
        response=self.client.delete(url)
        after_list_amount = photoArticle.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(before_list_amount-after_list_amount, 1)

    def test_video_delete_unauthorized(self):

        v = PhotoArticleFactory(idPhoto=5)

        before_list_amount = photoArticle.objects.count()
        url = reverse('photos_articles-detail', kwargs={'pk': v.idPhoto})
        self.client.force_authenticate(user=self.user)
        response=self.client.delete(url)
        after_list_amount = photoArticle.objects.count()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(before_list_amount-after_list_amount, 0)



class TestCommentaire(APITestCase,URLPatternsTestCase):
    urlpatterns = [
        path('articles/', include('Articles.urls')),
    ]

    def setUp(self):
        self.user = compteUtilisateurFactory()
        self.ar = ArticleFactory()

    def test_commentaire_list(self):

        for i in range(2):
            CommentaireFactory(idCommentaire=1+i)


        response = self.client.get(
            reverse('commentaires-list')
        )
        expected = 4
        print(response.content)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)

    def test_commentaire_found(self):

        c=CommentaireFactory(idCommentaire=3)
        response = self.client.get(reverse('commentaires-detail',  kwargs={'pk':c.idCommentaire}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('contenuCom'), c.contenuCom)

    def test_commentaire_not_found(self):

        response = self.client.get(reverse('commentaires-detail',  kwargs={'pk':10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_commentaire_delete_authorized(self):

        Group.objects.get_or_create(name='si')
        role.addRole(self.user.id,'si')
        c = CommentaireFactory(idCommentaire=4, idUtilisateurCom=self.user)

        before_list_amount = commentaire.objects.count()
        url = reverse('commentaires-detail', kwargs={'pk': c.idCommentaire})
        self.client.force_authenticate(user=self.user)
        response=self.client.delete(url)
        after_list_amount = commentaire.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(before_list_amount-after_list_amount, 1)

    def test_commentaire_delete_unauthorized(self):

        c = CommentaireFactory(idCommentaire=5)

        before_list_amount = commentaire.objects.count()
        url = reverse('commentaires-detail', kwargs={'pk': c.idCommentaire})
        self.client.force_authenticate(user=self.user)
        response=self.client.delete(url)
        after_list_amount = commentaire.objects.count()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(before_list_amount-after_list_amount, 0)

    def test_commentaire_modifier_authorized(self):

        Group.objects.get_or_create(name='si')
        role.addRole(self.user.id, 'si')
        c = CommentaireFactory(idCommentaire=15,idUtilisateurCom=self.user)

        c.contenuCom="nouveau contenu"
        url = reverse('commentaires-modifier', kwargs={'pk': c.idCommentaire})
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, {'contenuCom': c.contenuCom})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('contenuCom'), c.contenuCom)

    def test_commentaire_modifier_unauthorized(self):
        Group.objects.get_or_create(name='si')
        role.addRole(self.user.id, 'si')
        c = CommentaireFactory(idCommentaire=6)

        c.contenuCom = "nouveau contenu"
        url = reverse('commentaires-modifier', kwargs={'pk': c.idCommentaire})
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, {'contenuCom': c.contenuCom})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_commentaire_signaler_authorized(self):

        Group.objects.get_or_create(name='si')
        role.addRole(self.user.id, 'si')
        c = CommentaireFactory(idCommentaire=17)

        c.signalerCom=True
        url = reverse('commentaires-signaler', kwargs={'pk': c.idCommentaire})
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, {'signalerCom': c.signalerCom})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('signalerCom'), str(c.signalerCom))

    def test_commentaire_update_unauthorized(self):

        Group.objects.get_or_create(name='si')
        role.addRole(self.user.id, 'si')
        c = CommentaireFactory(idCommentaire=19,idUtilisateurCom=self.user)

        c.contenuCom = "nouveau contenu"
        url = reverse('commentaires-detail', kwargs={'pk': c.idCommentaire})
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, {'contenuCom': c.contenuCom})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_commentaire_update(self):
        Group.objects.get_or_create(name='si')
        role.addRole(self.user.id, 'si')
        c = CommentaireFactory(idCommentaire=7, idUtilisateurCom=self.user)
        dict = model_to_dict(c)

        url = reverse('commentaires-list')
        self.client.force_authenticate(user=self.user)
        before_list_amount = commentaire.objects.count()
        response = self.client.post(url, dict, format='json')
        after_list_amount = commentaire.objects.count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(after_list_amount - before_list_amount, 1)


class TestRedacteurArticles(APITestCase,URLPatternsTestCase):
    urlpatterns = [
        path('articles/', include('Articles.urls')),
    ]

    def setUp(self):
        self.user = compteUtilisateurFactory()

    def test_redacteur_articles_list(self):
        ArticleFactory(idArticle=1, idRedacteurAr=self.user)

        response = self.client.get(
            reverse('redacteurArticles-list',kwargs={'id':self.user.id})
        )
        expected = 1

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)

    def test_redacteur_article_found(self):

        ar=ArticleFactory(idArticle=2,contenuAr='contenu',idRedacteurAr=self.user)

        response = self.client.get(reverse('redacteurArticles-detail',  kwargs={'id':self.user.id,'pk':ar.idArticle}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('contenuAr'), ar.contenuAr)

    def test_article_not_found(self):

        response = self.client.get(reverse('redacteurArticles-detail',  kwargs={'id':self.user.id,'pk':20}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_redacteur_article_delete_authorized(self):


        Group.objects.get_or_create(name='rd')
        role.addRole(self.user.id,'rd')
        ar = ArticleFactory(idArticle=2,idRedacteurAr=self.user)

        before_list_amount = article.objects.count()
        url = reverse('redacteurArticles-detail', kwargs={'id':self.user.id,'pk': ar.idArticle})
        self.client.force_authenticate(user=self.user)
        response=self.client.delete(url)
        after_list_amount = article.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(before_list_amount-after_list_amount, 1)

    def test_redacteur_article_delete_unauthorized(self):

        ar = ArticleFactory()

        before_list_amount = article.objects.count()
        url = reverse('redacteurArticles-detail', kwargs={'id':self.user.id,'pk': ar.idArticle})
        self.client.force_authenticate(user=self.user)
        response=self.client.delete(url)
        after_list_amount = article.objects.count()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(before_list_amount-after_list_amount, 0)

    def test_redacteur_article_update_authorized(self):

        Group.objects.get_or_create(name='rd')
        role.addRole(self.user.id,'rd')
        ar = ArticleFactory(idArticle=3,idRedacteurAr=self.user)
        ar.contenuAr = "updated"

        url = reverse('redacteurArticles-detail', kwargs={'id': self.user.id, 'pk': ar.idArticle})
        self.client.force_authenticate(user=self.user)
        response=self.client.put(url,{'contenuAr':ar.contenuAr,'dateAr':ar.dateAr})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('contenuAr'), ar.contenuAr)


    def test_redacteur_article_update_unauthorized(self):

        ar = ArticleFactory(idArticle=14,idRedacteurAr=self.user)

        ar.contenuAr = "updated"
        dict = model_to_dict(ar)
        dict['dateAr'] = dict['dateAr'].strftime("%Y-%m-%dT%H:%M:%S.%f")
        url = reverse('redacteurArticles-detail', kwargs={'id': self.user.id, 'pk': ar.idArticle})
        self.client.force_authenticate(user=self.user)
        response=self.client.put(url,{'contenuAr':dict['contenuAr'],'dateAr':dict['dateAr']})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)



    def test_redacteur_article_validate_authorized(self):

        Group.objects.get_or_create(name='md')
        role.addRole(self.user.id,'md')
        ar = ArticleFactory(idArticle=25,idRedacteurAr=self.user)

        ar.validerAR = True
        url = reverse('redacteurArticles-detail', kwargs={'id': self.user.id, 'pk': ar.idArticle})
        self.client.force_authenticate(user=self.user)
        response=self.client.patch(url,{'validerAR':ar.validerAR})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('validerAR'), ar.validerAR)



    def test_article_validate_unauthorized(self):

        Group.objects.get_or_create(name='rd')
        role.addRole(self.user.id,'rd')
        ar = ArticleFactory(idArticle=6)


        ar.validerAR = True
        url = reverse('redacteurArticles-detail', kwargs={'id': self.user.id, 'pk': ar.idArticle})
        self.client.force_authenticate(user=self.user)
        response=self.client.patch(url,{'validerAR':ar.validerAR})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_article_create_authorized(self):

        Group.objects.get_or_create(name='rd')
        role.addRole(self.user.id, 'rd')
        ar = ArticleFactory(idArticle=7, idRedacteurAr=self.user)
        dict=model_to_dict(ar)
        dict['dateAr']=dict['dateAr'].strftime("%Y-%m-%dT%H:%M:%S.%f")

        url = reverse('redacteurArticles-list',kwargs={'id': self.user.id})
        self.client.force_authenticate(user=self.user)
        before_list_amount = article.objects.count()
        response = self.client.post(url,dict,format='json')
        print(response)
        after_list_amount = article.objects.count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(after_list_amount - before_list_amount, 1)


    def test_article_create_unauthorized(self):

        Group.objects.get_or_create(name='rd')
        role.deleteRole(self.user.id, 'rd')
        ar = ArticleFactory(idArticle=18)
        dict=model_to_dict(ar)
        dict['dateAr']=dict['dateAr'].strftime("%Y-%m-%dT%H:%M:%S.%f")

        url = reverse('redacteurArticles-list', kwargs={'id': self.user.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url,dict,format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

