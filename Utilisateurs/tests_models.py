from django.contrib.auth.models import Group
from django.test import TestCase
from .models import compteUtilisateur, role


class userTests(TestCase):
    def test_add_user(self):
        user1                       = compteUtilisateur.objects.create(email='user1@esi.dz', username='user1', password='user1')
        user2                       = compteUtilisateur.objects.get(email='user1@esi.dz')
        self.assertEqual(user2, user1)

    def test_add_superuser(self):
        sup_user1                   = compteUtilisateur.objects.create_superuser(email='supuser@gmail', username='supuser', password='supuser')
        sup_user2                   = compteUtilisateur.objects.get(email='supuser@gmail')
        self.assertEqual(sup_user2, sup_user1)
        self.assertIs(sup_user1.is_admin, True)

class roleTests(TestCase):

    def test_add_role(self):
        user                        = compteUtilisateur.objects.create(email='user@esi.dz', username='user', password='user')
        Group.objects.get_or_create(name='new_group')
        role.addRole(user.id,'new_group')
        self.assertTrue(user.groups.filter(name='new_group').exists())

    def test_delete_role(self):
        user                        = compteUtilisateur.objects.create(email='user3@esi.dz', username='user3', password='user3')
        Group.objects.get_or_create(name='new_group')
        role.addRole(user.id, 'new_group')
        role.deleteRole(user.id, 'new_group')
        self.assertFalse(user.groups.filter(name='new_group').exists())
