from django.test import TestCase

from .serializers import *
from .factories import *


class RegionSerializer(TestCase):
    def test_model_fields(self):
        """Serializer data matches the article object for each field."""
        ar = RegionFactory()
        serializer=regionSerializer(ar)
        for field_name in [
            'idRegion', 'nomRegion', 'is_risque'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(ar, field_name)
            )


class StatistiqueSerializer(TestCase):
    def test_model_fields(self):
        """Serializer data matches the article object for each field."""
        ar = StatistiqueFactory()
        serializer=statistiqueRegionSerializer(ar)
        for field_name in [
            'idStatistique','nbrPorteurVirus','casConfirme','casRetablis','nbrDeces','nbrGuerisons', 'dateSt','validerSt'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(ar, field_name)
            )
        for field_name in [
            'idModerateurSt','idAgentSt'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(ar, field_name).id
            )
        for field_name in [
            'idRegionSt'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(ar, field_name).idRegion
            )
