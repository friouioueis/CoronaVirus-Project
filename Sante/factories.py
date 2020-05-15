import random
from datetime import datetime

import factory
from factory import DjangoModelFactory

from .models import *
from Utilisateurs.factories import compteUtilisateurFactory


class InfoSanteFactory(DjangoModelFactory):

    class Meta:
        model = infoSante

    idInfoSante = factory.Sequence(lambda n: 1+n)
    idUtilisateurIs=factory.SubFactory(compteUtilisateurFactory)
    poids=random.randint(45, 100)
    temperature=random.randint(37, 42)
    Rythme_cardiaque = random.randint(37, 42)
    dateSaisie=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")