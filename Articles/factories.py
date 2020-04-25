from datetime import datetime

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
    dateAr = datetime.now()
    terminerAR=True
    validerAR=None

class VideoArticleFactory(DjangoModelFactory):

    class Meta:
        model = videoArticle

    idVideo=factory.Sequence(lambda n: 1+n)
    idArticleVd=factory.SubFactory(ArticleFactory)
    lienViAc=factory.django.FileField()

class PhotoArticleFactory(DjangoModelFactory):

    class Meta:
        model = photoArticle

    idPhoto = factory.Sequence(lambda n: 1 + n)
    idArticlePh = factory.SubFactory(ArticleFactory)
    lienPhAc = factory.django.ImageField()

class CommentaireFactory(DjangoModelFactory):

    class Meta:
        model = commentaire

    idCommentaire=factory.Sequence(lambda n: 1 + n)
    idUtilisateurCom=factory.SubFactory(compteUtilisateurFactory)
    idModerateurCom=factory.SubFactory(compteUtilisateurFactory)
    idArticleCom=factory.SubFactory(ArticleFactory)
    contenuCom=Faker('text')
    signalerCom=False