from django.test import TestCase
from .serializers import *
from .factories import *


class ArticleSerializer(TestCase):
    def test_model_fields(self):
        """Serializer data matches the article object for each field."""
        ar = ArticleFactory()
        serializer=articleSerializer(ar)
        for field_name in [
            'idArticle', 'contenuAr', 'dateAr', 'terminerAR','validerAR'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(ar, field_name)
            )
        for field_name in [
            'idRedacteurAr', 'idModerateurAr'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(ar, field_name).id
            )

class CommentaireSerializer(TestCase):
    def test_model_fields(self):
        """Serializer data matches the article object for each field."""
        ar = CommentaireFactory()
        serializer=commentaireSerializer(ar)
        for field_name in [
            'idCommentaire', 'contenuCom', 'signalerCom'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(ar, field_name)
            )
        for field_name in [
            'idUtilisateurCom', 'idModerateurCom'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(ar, field_name).id
            )
        for field_name in [
            'idArticleCom'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(ar, field_name).idArticle
            )