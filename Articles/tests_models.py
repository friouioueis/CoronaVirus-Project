from django.test import TestCase

from .factories import *


class ArticleTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        ar = ArticleFactory()
        return self.assertEqual(str(ar), 'Article redigé par: ' + ar.idRedacteurAr.username)


