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

    def test_add_role(self):
        user                        = compteUtilisateur.objects.create(email='user@esi.dz', username='user', password='user')
        role1                       = role.objects.create(idUtilisateurR=user, Type='si')
        role2                       = role.objects.get(idUtilisateurR=user)
        self.assertEqual(role2.get_Type_display(), role1.get_Type_display())

    def test_delete_user(self):
        user3                        = compteUtilisateur.objects.create(email='user3@esi.dz', username='user3', password='user3')
        user3.delete()
        self.assertFalse(compteUtilisateur.objects.filter(email='user3@esi.dz').exists())
