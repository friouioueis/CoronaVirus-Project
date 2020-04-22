import json

from django.contrib.auth.models import Group
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
        expected = 2

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
        response=self.client.put(url,{'contenuAr':ar.contenuAr,'dateAr':ar.dateAr})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('contenuAr'), ar.contenuAr)
        self.assertEqual(response.json().get('dateAr'), ar.dateAr)

    def test_article_update_unauthorized(self):

        ar = ArticleFactory(idArticle=4,idRedacteurAr=self.user)

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
        ar.refuserAR = 'False'
        url = reverse('articles-detail', kwargs={'pk': ar.idArticle})
        self.client.force_authenticate(user=self.user)
        response=self.client.patch(url,{'validerAR':ar.validerAR,'refuserAR':ar.refuserAR})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('validerAR'), ar.validerAR)
        self.assertEqual(response.json().get('refuserAR'), ar.refuserAR)



    def test_article_validate_unauthorized(self):

        Group.objects.get_or_create(name='rd')
        role.addRole(self.user.id,'rd')
        ar = ArticleFactory(idArticle=6)

        ar.validerAR = True
        ar.refuserAR = False
        url = reverse('articles-detail', kwargs={'pk': ar.idArticle})
        self.client.force_authenticate(user=self.user)
        response=self.client.patch(url,{'validerAR':ar.validerAR,'refuserAR':ar.refuserAR})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

