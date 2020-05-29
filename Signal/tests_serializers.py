from django.test import TestCase

from .serializers import *
from .factories import *


class SignalementSerializer(TestCase):
    def test_model_fields(self):
        """Serializer data matches the article object for each field."""
        ar = SignalementFactory()
        serializer=signalementSerializer(ar)
        for field_name in [
            'idSignal', 'descriptionSg', 'validerSg', 'dateSg','typeSg','lienSg'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(ar, field_name)
            )
        for field_name in [
            'idUtilisateurSg', 'idModerateurSg'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(ar, field_name).id
            )
