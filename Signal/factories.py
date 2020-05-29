from datetime import datetime

import factory
from factory import DjangoModelFactory, Faker

from .models import *
from Utilisateurs.factories import compteUtilisateurFactory


SIGNALEMENT_CHOICES = (
    ('ph', 'photo'),
    ('vi', 'video')
)

class SignalementFactory(DjangoModelFactory):

    class Meta:
        model = signalement

    idSignal = factory.Sequence(lambda n: 1+n)
    idUtilisateurSg=factory.SubFactory(compteUtilisateurFactory)
    idModerateurSg=factory.SubFactory(compteUtilisateurFactory)
    descriptionSg=Faker('text')
    validerSg = Faker('boolean')
    dateSg = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
    typeSg='ph'
    lienSg=factory.django.FileField()

