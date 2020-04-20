from django.urls import reverse
from faker import factory
from rest_framework import status
from rest_framework.test import APITestCase
from Articles.models import *
from Articles.serializers import *


class ArticleFactory(factory.Factory):
    class Meta:
        model = article

class ArticleTest(APITestCase):
    def can_get_all(self):
        response = self.client.get('/articles/articles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def can_get_article(self):
        article=ArticleFactory()
