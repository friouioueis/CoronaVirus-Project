import json
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .factories import *
from .models import *


class UserList(APITestCase):

    def setUp(self):
        for i in range(4):
            compteUtilisateurFactory()

    def test_photoArticle_list(self):
        response = self.client.get(
            reverse('comptes-list')
        )
        expected = 4

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)


class UserGet(APITestCase):

    def setUp(self):
        self.user = compteUtilisateurFactory()

    def test_user_found(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('comptes-detail',  kwargs={'pk': self.user.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_not_found(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('comptes-detail',  kwargs={'pk': 3}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UserDelete(APITestCase):

    def setUp(self):
        self.user = compteUtilisateurFactory()

    def test_user_delete(self):

        before_list_amount = compteUtilisateur.objects.count()
        url = reverse('comptes-detail', kwargs={'pk': self.user.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        after_list_amount = compteUtilisateur.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(before_list_amount-after_list_amount, 1)


class UserUpdate(APITestCase):
    def setUp(self):
        self.user = compteUtilisateurFactory()

    def test_user_update(self):

        self.user.username = "updated"
        url = reverse('comptes-detail', kwargs={'pk': self.user.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, {'username': self.user.username, 'id': self.user.id, 'password': self.user.password, 'email': self.user.email})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('username'), self.user.username)


class RoleList(APITestCase):

    def setUp(self):
        self.user = compteUtilisateurFactory()
        for i in range(4):
            roleFactory()

    def test_role_list(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            reverse('roles-list')
        )
        expected = 4

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)

class roleGet(APITestCase):

    def setUp(self):
        self.user = compteUtilisateurFactory()
        Group.objects.get_or_create(name='rd')
        self.role = roleFactory()

    def test_role_found(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('roles-detail',  kwargs={'pk': self.role.idRole}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('Type'), self.role.Type)

    def test_role_not_found(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('roles-detail',  kwargs={'pk': 3}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class RoleDelete(APITestCase):
    def setUp(self):
        self.user = compteUtilisateurFactory()
        Group.objects.get_or_create(name='rd')
        self.role = roleFactory(Type='rd')

    def test_role_delete(self):
        before_list_amount = role.objects.count()
        url = reverse('roles-detail', kwargs={'pk': self.role.idRole})
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        after_list_amount = role.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(before_list_amount-after_list_amount, 1)


class RoleUpdate(APITestCase):
    def setUp(self):
        self.user = compteUtilisateurFactory()
        Group.objects.get_or_create(name='rd')
        self.role = roleFactory(idUtilisateurR=self.user)

    def test_role_update(self):
        self.role.Type = 'rd'
        url = reverse('roles-detail', kwargs={'pk': self.role.idRole})
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, {'idRole': self.role.idRole, 'Type': self.role.Type, 'idUtilisateurR': self.role.idUtilisateurR.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('Type'), self.role.Type)


class infoList(APITestCase):

    def setUp(self):
        self.user = compteUtilisateurFactory()
        for i in range(4):
            infoFactory()

    def test_info_list(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            reverse('infos-list')
        )
        expected = 4

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)


class infoGet(APITestCase):

    def setUp(self):
        self.user = compteUtilisateurFactory()
        self.info = infoFactory()

    def test_info_found(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('infos-detail',  kwargs={'pk': self.info.idInfoPer}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('nom'), self.info.nom)

    def test_info_not_found(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('infos-detail',  kwargs={'pk': 3}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class InfoDelete(APITestCase):

    def setUp(self):
        self.user = compteUtilisateurFactory()
        self.info = infoFactory()

    def test_info_delete(self):
        before_list_amount = infoPersonel.objects.count()
        url = reverse('infos-detail', kwargs={'pk': self.info.idInfoPer})
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        after_list_amount = infoPersonel.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(before_list_amount-after_list_amount, 1)


class infoUpdate(APITestCase):
    def setUp(self):
        self.user = compteUtilisateurFactory()
        self.info = infoFactory(idUtilisateurIp=self.user)

    def test_info_update(self):
        self.info.nom = 'updated'
        url = reverse('infos-detail', kwargs={'pk': self.info.idRole})
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, {'idInfoPer': self.info.idInfoPer, 'nom': self.info.nom, 'idUtilisateurIp': self.info.idUtilisateurR.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('nom'), self.info.nom)