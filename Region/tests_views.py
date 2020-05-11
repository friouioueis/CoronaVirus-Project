import json

from django.contrib.auth.models import Group
from django.forms import model_to_dict
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from Utilisateurs.models import role
from .factories import *
from .models import *

class RegionList(APITestCase):

    def setUp(self):
        for i in range(2):
            RegionFactory()

    def test_region_list(self):
        response = self.client.get(
            reverse('regions-list')
        )
        expected = 2

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)

class RegionGet(APITestCase):

    def setUp(self):
        self.region = RegionFactory(nomRegion='region')

    def test_region_found(self):
        response = self.client.get(reverse('regions-detail',  kwargs={'pk':self.region.idRegion}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('nomRegion'), self.region.nomRegion)

    def test_region_not_found(self):
        response = self.client.get(reverse('regions-detail',  kwargs={'pk':10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class RegionDelete(APITestCase):
    def setUp(self):
        self.user1 = compteUtilisateurFactory()
        self.user2 = compteUtilisateurFactory()
        Group.objects.get_or_create(name='ad')
        role.addRole(self.user2.id, 'ad')
        self.region = RegionFactory()

    def test_region_delete_authorized(self):

        before_list_amount = region.objects.count()
        url = reverse('regions-detail', kwargs={'pk': self.region.idRegion})
        self.client.force_authenticate(user=self.user2)
        response=self.client.delete(url)
        after_list_amount = region.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(before_list_amount-after_list_amount, 1)

    def test_region_delete_unauthorized(self):

        before_list_amount = region.objects.count()
        url = reverse('regions-detail', kwargs={'pk': self.region.idRegion})
        self.client.force_authenticate(user=self.user1)
        response=self.client.delete(url)
        after_list_amount = region.objects.count()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(before_list_amount-after_list_amount, 0)

class RegionUpdate(APITestCase):
    def setUp(self):
        self.user1 = compteUtilisateurFactory()
        self.user2 = compteUtilisateurFactory()
        Group.objects.get_or_create(name='ad')
        role.addRole(self.user2.id, 'ad')
        self.region = RegionFactory()

    def test_region_update_authorized(self):

        self.region.nomRegion = "updated"
        url = reverse('regions-detail', kwargs={'pk': self.region.idRegion})
        self.client.force_authenticate(user=self.user2)
        response=self.client.put(url,{'nomRegion':self.region.nomRegion,"is_risque":self.region.is_risque})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('nomRegion'), self.region.nomRegion)


    def test_region_update_unauthorized(self):

        self.region.nomRegion = "updated"
        url = reverse('regions-detail', kwargs={'pk': self.region.idRegion})
        self.client.force_authenticate(user=self.user1)
        response = self.client.put(url, {'nomRegion': self.region.nomRegion, "is_risque": self.region.is_risque})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class RegionIsRisque(APITestCase):

    def setUp(self):
        self.user = compteUtilisateurFactory()
        self.user1 = compteUtilisateurFactory()
        Group.objects.get_or_create(name='as')
        role.addRole(self.user.id, 'as')
        self.region = RegionFactory()

    def test_region_isRisque_authorized(self):

        self.region.is_risque = 'True'
        url = reverse('regions-isRisque', kwargs={'pk': self.region.idRegion})
        self.client.force_authenticate(user=self.user)
        response=self.client.patch(url,{'is_risque':self.region.is_risque})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('is_risque'), self.region.is_risque)

    def test_region_isRisque_unauthorized(self):

        self.region.is_risque = True
        url = reverse('regions-isRisque', kwargs={'pk': self.region.idRegion})
        self.client.force_authenticate(user=self.user1)
        response = self.client.patch(url, {'is_risque': self.region.is_risque})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class RegionCreate(APITestCase):

    def setUp(self):
        self.user1 = compteUtilisateurFactory()
        self.user2 = compteUtilisateurFactory()
        Group.objects.get_or_create(name='ad')
        role.addRole(self.user2.id, 'ad')

    def test_region_create_authorized(self):
        reg = RegionFactory(idRegion=1)
        dict=model_to_dict(reg)

        url = reverse('regions-list')
        self.client.force_authenticate(user=self.user2)
        before_list_amount = region.objects.count()
        response = self.client.post(url,dict,format='json')
        after_list_amount = region.objects.count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(after_list_amount - before_list_amount, 1)

    def test_region_create_unauthorized(self):
        reg = RegionFactory(idRegion=3)
        dict=model_to_dict(reg)

        url = reverse('regions-list')
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(url,dict,format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class StatistiqueList(APITestCase):

    def setUp(self):
        self.user1 = compteUtilisateurFactory()
        self.user2 = compteUtilisateurFactory()
        Group.objects.get_or_create(name='md')
        role.addRole(self.user1.id, 'md')
        for i in range(2):
            StatistiqueFactory()

    def test_statistique_list_authorized(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(
            reverse('stat_regions-list')
        )
        expected = 2

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)

    def test_statistique_list_unauthorized(self):
        self.client.force_authenticate(user=self.user2)
        response = self.client.get(
                reverse('stat_regions-list')
            )
        self.assertEqual(
            response.status_code, status.HTTP_403_FORBIDDEN)

class StatistiqueGet(APITestCase):

    def setUp(self):
        self.user1 = compteUtilisateurFactory()
        self.user2 = compteUtilisateurFactory()
        Group.objects.get_or_create(name='md')
        role.addRole(self.user1.id, 'md')
        self.statistique = StatistiqueFactory()

    def test_region_found(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(reverse('stat_regions-detail',  kwargs={'pk':self.statistique.idStatistique}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_region_not_found(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(reverse('stat_regions-detail',  kwargs={'pk':10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_region_found_unauthorized(self):
        self.client.force_authenticate(user=self.user2)
        response = self.client.get(reverse('stat_regions-detail',  kwargs={'pk':self.statistique.idStatistique}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class StatistiqueDelete(APITestCase):
    def setUp(self):
        self.user1 = compteUtilisateurFactory()
        self.user2 = compteUtilisateurFactory()
        Group.objects.get_or_create(name='as')
        role.addRole(self.user2.id, 'as')
        self.statistique = StatistiqueFactory()

    def test_statistique_delete_authorized(self):

        before_list_amount = statistiqueRegion.objects.count()
        url = reverse('stat_regions-detail', kwargs={'pk': self.statistique.idStatistique})
        self.client.force_authenticate(user=self.user2)
        response=self.client.delete(url)
        after_list_amount = statistiqueRegion.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(before_list_amount-after_list_amount, 1)

    def test_statistique_delete_unauthorized(self):

        before_list_amount = statistiqueRegion.objects.count()
        url = reverse('stat_regions-detail', kwargs={'pk': self.statistique.idStatistique})
        self.client.force_authenticate(user=self.user1)
        response=self.client.delete(url)
        after_list_amount = statistiqueRegion.objects.count()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(before_list_amount-after_list_amount, 0)

class StatistiqueValider(APITestCase):
    def setUp(self):
        self.user1 = compteUtilisateurFactory()
        self.user2 = compteUtilisateurFactory()
        Group.objects.get_or_create(name='md')
        role.addRole(self.user2.id, 'md')
        self.statistique = StatistiqueFactory()

    def test_statistique_partial_update_authorized(self):

        self.statistique.validerSt="True"

        url = reverse('stat_regions-detail', kwargs={'pk': self.statistique.idStatistique})
        self.client.force_authenticate(user=self.user2)
        response=self.client.patch(url,{"validerSt":self.statistique.validerSt,"idModerateurSt":self.user2.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('validerSt'), self.statistique.validerSt)

    def test_statistique_partial_update_unauthorized(self):
        self.statistique.validerSt = "True"

        url = reverse('stat_regions-detail', kwargs={'pk': self.statistique.idStatistique})
        self.client.force_authenticate(user=self.user1)
        response = self.client.patch(url, {"validerSt": self.statistique.validerSt, "idModerateurSt": self.user1.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_statistique_update_authorized(self):

        self.statistique.validerSt="True"

        url = reverse('stat_regions-detail', kwargs={'pk': self.statistique.idStatistique})
        self.client.force_authenticate(user=self.user2)
        response=self.client.put(url,{"validerSt":self.statistique.validerSt,"idModerateurSt":self.user2.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('validerSt'), self.statistique.validerSt)

    def test_statistique_update_unauthorized(self):
        self.statistique.validerSt = "True"

        url = reverse('stat_regions-detail', kwargs={'pk': self.statistique.idStatistique})
        self.client.force_authenticate(user=self.user1)
        response = self.client.put(url, {"validerSt": self.statistique.validerSt, "idModerateurSt": self.user1.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class StatistiqueCreate(APITestCase):

    def setUp(self):
        self.user1 = compteUtilisateurFactory()
        self.user2 = compteUtilisateurFactory()
        Group.objects.get_or_create(name='as')
        role.addRole(self.user2.id, 'as')

    def test_statistique_create_authorized(self):
        reg = StatistiqueFactory(idStatistique=1)
        dict=model_to_dict(reg)

        url = reverse('stat_regions-list')
        self.client.force_authenticate(user=self.user2)
        before_list_amount = statistiqueRegion.objects.count()
        response = self.client.post(url,dict,format='json')
        after_list_amount = statistiqueRegion.objects.count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(after_list_amount - before_list_amount, 1)

    def test_region_create_unauthorized(self):
        reg = StatistiqueFactory(idStatistique=3)
        dict=model_to_dict(reg)

        url = reverse('stat_regions-list')
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(url,dict,format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class StatistiqueValideList(APITestCase):

    def setUp(self):
        for i in range(2):
            StatistiqueFactory(validerSt=True)
        StatistiqueFactory(validerSt=False)

    def test_statistique_list_authorized(self):
        response = self.client.get(
            reverse('stat_valid_regions-list')
        )
        expected = 2

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)


class StatistiqueValideGet(APITestCase):

    def setUp(self):
        self.statistique = StatistiqueFactory(validerSt=True)

    def test_region_found(self):
        response = self.client.get(reverse('stat_valid_regions-detail',  kwargs={'pk':self.statistique.idStatistique}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_region_not_found(self):
        response = self.client.get(reverse('stat_valid_regions-detail',  kwargs={'pk':10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class RegionStatistiqueList(APITestCase):

    def setUp(self):
        self.region=RegionFactory()
        for i in range(4):
            StatistiqueFactory(idRegionSt=self.region,validerSt=True)

    def test_region_statistique_list(self):
        response = self.client.get(
            reverse('regionStats-list', kwargs={'id': self.region.idRegion})
        )
        expected = 4

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(json.loads(response.content.decode('utf-8'))),
            expected)

class RegionStatistiqueGet(APITestCase):

    def setUp(self):
        self.region = RegionFactory()
        self.statistique = StatistiqueFactory(idRegionSt=self.region,validerSt=True)

    def test_commentaire_found(self):
        response = self.client.get(reverse('regionStats-detail', kwargs={'id': self.region.idRegion,'pk': self.statistique.idStatistique}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_commentaire_not_found(self):
        response = self.client.get(reverse('regionStats-detail', kwargs={'id': self.region.idRegion,'pk': 10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)