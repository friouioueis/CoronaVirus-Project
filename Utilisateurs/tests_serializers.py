from django.test import TestCase
from .serializers import *
from .factories import *


class utilisateurSerializer(TestCase):
    def test_model_fields(self):
        user = compteUtilisateurFactory()
        serializer = compteUtilisateurSerializer(user)
        for field_name in [
            'username', 'email'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(user, field_name))


class rolesSerializer(TestCase):
    def test_model_fields(self):
        role = roleFactory()
        serializer = roleSerializer(role)
        for field_name in [
            'idRole', 'Type'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(role, field_name))
        for field_name in [
            'idUtilisateurR'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(role, field_name).id
            )

class infoSerializer(TestCase):
    def test_model_fields(self):
        info = infoFactory()
        serializer = infoPersonelSerializer(info)
        for field_name in [
            'idInfoPer', 'nom', 'prenom'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(info, field_name))
        for field_name in [
            'idUtilisateurIp'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(info, field_name).id
            )
