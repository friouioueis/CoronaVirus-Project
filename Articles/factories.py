import random

import factory
from factory import DjangoModelFactory, Faker

from .models import *
from Utilisateurs.factories import compteUtilisateurFactory


class ArticleFactory(DjangoModelFactory):

    class Meta:
        model = article
    idArticle = factory.Sequence(lambda n: 1+n)
    idRedacteurAr=factory.SubFactory(compteUtilisateurFactory)
    idModerateurAr=factory.SubFactory(compteUtilisateurFactory)
    contenuAr=Faker('text')
    dateAr = Faker('date')
    terminerAR=None
    validerAR=None
    refuserAR=None

class VideoArticleFactory(DjangoModelFactory):

    class Meta:
        model = videoArticle


class PhotoArticleFactory(DjangoModelFactory):

    class Meta:
        model = photoArticle


class CommentaireFactory(DjangoModelFactory):

    class Meta:
        model = commentaire