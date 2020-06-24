# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


from scrapy_djangoitem import DjangoItem

from Robots.models import Article, pubYoutube,pubGoogleNews


class ArticleItem(DjangoItem):
    django_model = Article


class YoutubeItem(DjangoItem):
    django_model = pubYoutube

class GNItem(DjangoItem):
    django_model = pubGoogleNews