import factory
from factory import DjangoModelFactory, Faker

from .models import *


class compteUtilisateurFactory(DjangoModelFactory):
    username=Faker('name')
    email = Faker('email')
    class Meta:
        model = compteUtilisateur