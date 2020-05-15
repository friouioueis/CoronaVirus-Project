import json

from django.forms import model_to_dict
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .factories import *
from .models import *

class InfoSanteList(APITestCase):

    def setUp(self):
        self.user = compteUtilisateurFactory()
        for i in range(2):
            InfoSanteFactory()

    def test_infoSante_list_unauthorized(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            reverse('info_sante-list')
        )

        self.assertEqual(
                response.status_code, status.HTTP_403_FORBIDDEN)

class InfoSanteGet(APITestCase):

    def setUp(self):
        self.user = compteUtilisateurFactory()
        self.user2=compteUtilisateurFactory()
        self.info = InfoSanteFactory(temperature=40,idUtilisateurIs=self.user)

    def test_info_found_authorized(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('info_sante-detail',  kwargs={'pk':self.info.idInfoSante}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('temperature'),self.info.temperature)

    def test_info_not_found(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('info_sante-detail',  kwargs={'pk':10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_info_found_unauthorized(self):
        self.client.force_authenticate(user=self.user2)
        response = self.client.get(reverse('info_sante-detail',  kwargs={'pk':self.info.idInfoSante}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class InfoSanteDelete(APITestCase):
    def setUp(self):
        self.user1 = compteUtilisateurFactory()
        self.user2 = compteUtilisateurFactory()
        self.info = InfoSanteFactory(idUtilisateurIs=self.user1)

    def test_info_delete_authorized(self):

        before_list_amount = infoSante.objects.count()
        url = reverse('info_sante-detail', kwargs={'pk': self.info.idInfoSante})
        self.client.force_authenticate(user=self.user1)
        response=self.client.delete(url)
        after_list_amount = infoSante.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(before_list_amount-after_list_amount, 1)

    def test_info_delete_unauthorized(self):

        before_list_amount = infoSante.objects.count()
        url = reverse('info_sante-detail', kwargs={'pk': self.info.idInfoSante})
        self.client.force_authenticate(user=self.user2)
        response=self.client.delete(url)
        after_list_amount = infoSante.objects.count()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(before_list_amount-after_list_amount, 0)

class InfoSanteUpdate(APITestCase):
    def setUp(self):
        self.user1 = compteUtilisateurFactory()
        self.user2 = compteUtilisateurFactory()
        self.info = InfoSanteFactory(idUtilisateurIs=self.user1)

    def test_info_update_authorized(self):

        self.info.temperature=41
        dict = model_to_dict(self.info)
        url = reverse('info_sante-detail', kwargs={'pk': self.info.idInfoSante})
        self.client.force_authenticate(user=self.user1)
        response=self.client.put(url,dict)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('temperature'), self.info.temperature)


    def test_info_update_unauthorized(self):

        self.info.temperature = 41
        dict = model_to_dict(self.info)
        url = reverse('info_sante-detail', kwargs={'pk': self.info.idInfoSante})
        self.client.force_authenticate(user=self.user2)
        response = self.client.put(url, dict)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class ArticleCreate(APITestCase):

    def setUp(self):
        self.user1 = compteUtilisateurFactory()
        self.user2 = compteUtilisateurFactory()

    def test_article_create(self):
        info = InfoSanteFactory(idUtilisateurIs=self.user1)
        dict=model_to_dict(info)

        url = reverse('info_sante-list')
        self.client.force_authenticate(user=self.user1)
        before_list_amount = infoSante.objects.count()
        response = self.client.post(url,dict,format='json')
        after_list_amount = infoSante.objects.count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(after_list_amount - before_list_amount, 1)

class UtilisateurInfoSanteList(APITestCase):

    def setUp(self):
        self.user = compteUtilisateurFactory()
        self.user2= compteUtilisateurFactory()
        for i in range(2):
            InfoSanteFactory(idUtilisateurIs=self.user)

    def test_infoSante_list_authorized(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            reverse('utilisateurInfoSante-list',kwargs={'id':self.user.id})
        )
        expected = 2

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)

    def test_infoSante_list_unauthorized(self):
        self.client.force_authenticate(user=self.user2)
        response = self.client.get(
            reverse('utilisateurInfoSante-list',kwargs={'id':self.user.id})
        )

        self.assertEqual(
                response.status_code, status.HTTP_403_FORBIDDEN)

class UtilisateurInfoSanteGet(APITestCase):

    def setUp(self):
        self.user = compteUtilisateurFactory()
        self.user2=compteUtilisateurFactory()
        self.info = InfoSanteFactory(temperature=40,idUtilisateurIs=self.user)

    def test_info_found_authorized(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('utilisateurInfoSante-detail',  kwargs={'id':self.user.id,'pk':self.info.idInfoSante}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('temperature'),self.info.temperature)

    def test_info_not_found(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('utilisateurInfoSante-detail',  kwargs={'id':self.user.id,'pk':10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_info_found_unauthorized(self):
        self.client.force_authenticate(user=self.user2)
        response = self.client.get(reverse('utilisateurInfoSante-detail',  kwargs={'id':self.user.id,'pk':self.info.idInfoSante}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)