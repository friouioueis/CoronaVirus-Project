import random
from datetime import datetime

import factory
from factory import DjangoModelFactory, Faker

from .models import *
from Utilisateurs.factories import compteUtilisateurFactory

class RegionFactory(DjangoModelFactory):

    class Meta:
        model = region

    idRegion = factory.Sequence(lambda n: 1+n)
    nomRegion=Faker('name')
    is_risque=Faker('boolean')

class StatistiqueFactory(DjangoModelFactory):

    class Meta:
        model = statistiqueRegion

    idStatistique = factory.Sequence(lambda n: 1+n)
    idRegionSt = factory.SubFactory(RegionFactory)
    nbrPorteurVirus=random.randint(0, 500)
    casConfirme=random.randint(0, 500)
    casRetablis=random.randint(0, 500)
    nbrDeces=random.randint(0, 500)
    nbrGuerisons=random.randint(0, 500)
    dateSt = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
    idModerateurSt = factory.SubFactory(compteUtilisateurFactory)
    validerSt=Faker('boolean')