from random import randint

from factory import DjangoModelFactory, Faker

from .models import *


class ArticleFactory(DjangoModelFactory):
    idArticle=randint(1, 100)
    idRedacteurAr=Faker('idRedacteurAr')
    idModerateurAr
    dateAr
    contenuAr
    terminerAR
    validerAR
    refuserAR
    class Meta:
        model = article


class VideoArticleFactory(DjangoModelFactory):

    class Meta:
        model = videoArticle


class PhotoArticleFactory(DjangoModelFactory):

    class Meta:
        model = photoArticle


class CommentaireFactory(DjangoModelFactory):

    class Meta:
        model = commentaire