from django.test import TestCase

from .serializers import *
from .factories import *


class ArticleSerializer(TestCase):
    def test_model_fields(self):
        """Serializer data matches the article object for each field."""
        ar = ArticleFactory()
        serializer=articleSerializer(ar)
        for field_name in [
            'idArticle', 'contenuAr', 'dateAr', 'terminerAR','validerAR', 'refuserAR'
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