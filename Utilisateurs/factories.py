from random import choice

import factory
from factory import DjangoModelFactory, Faker
from .models import *


class compteUtilisateurFactory(DjangoModelFactory):
    username = Faker('name')
    email = Faker('email')
    class Meta:
        model = compteUtilisateur

class roleFactory(DjangoModelFactory):
    class Meta:
        model = role

    idRole = factory.Sequence(lambda n: 1 + n)
    idUtilisateurR = factory.SubFactory(compteUtilisateurFactory)
    Type = factory.LazyAttribute(lambda x: choice(ROLE_CHOICES)[0])

class infoFactory(DjangoModelFactory):
    class Meta:
        model = infoPersonel

    idInfoPer = factory.Sequence(lambda n: 1 + n)
    idUtilisateurIp = factory.SubFactory(compteUtilisateurFactory)
    nom = Faker('name')
    prenom = Faker('name')