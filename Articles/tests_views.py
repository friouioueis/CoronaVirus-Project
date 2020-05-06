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

class ArticleList(APITestCase):

    def setUp(self):
        for i in range(4):
            ArticleFactory()

    def test_article_list(self):
        response = self.client.get(
            reverse('articles-list')
        )
        expected = 4

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)

class ArticleGet(APITestCase):

    def setUp(self):
        self.article = ArticleFactory(contenuAr='contenu')

    def test_article_found(self):
        response = self.client.get(reverse('articles-detail',  kwargs={'pk':self.article.idArticle}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('contenuAr'), self.article.contenuAr)

    def test_article_not_found(self):
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
