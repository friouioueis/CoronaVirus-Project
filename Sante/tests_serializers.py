from django.test import TestCase

from .serializers import *
from .factories import *


class InfoSanteSerializer(TestCase):
    def test_model_fields(self):
        """Serializer data matches the article object for each field."""
        ar = InfoSanteFactory()
        serializer=infoSanteSerializer(ar)
        for field_name in [
            'idInfoSante', 'poids', 'temperature','Rythme_cardiaque'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(ar, field_name)
            )
        for field_name in [
            'idUtilisateurIs'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(ar, field_name).id
            )

