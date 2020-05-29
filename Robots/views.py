from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor

from .scrapy.news.news.spiders.article_spider import ArticleSpider
from .serializers import *
from .models import *


class pubFacebookView(viewsets.ModelViewSet):
    serializer_class                = pubFacebookSerializer
    queryset                        = pubFacebook.objects.all()


class pubYoutubeView(viewsets.ModelViewSet):
    serializer_class                = pubYoutubeSerializer
    queryset                        = pubYoutube.objects.all()


class pubSiteWebView(viewsets.ModelViewSet):
    serializer_class                = pubSiteWebSerializer
    queryset                        = pubSiteWeb.objects.all()


class SortedpubFacebookView(viewsets.ModelViewSet):
    serializer_class                = pubFacebookSerializer
    queryset                        = pubFacebook.objects.all().order_by('DateFb')


class SortedpubYoutubeView(viewsets.ModelViewSet):
    serializer_class                = pubYoutubeSerializer
    queryset                        = pubYoutube.objects.all().order_by('DateYt')


class SortedpubSiteWebView(viewsets.ModelViewSet):
    serializer_class                = pubSiteWebSerializer
    queryset                        = pubSiteWeb.objects.all().order_by('DateSw')


class RunSpiderView(viewsets.ViewSet):

    @action(detail=False, methods=['GET'], name='beer-run')
    def run(self, request, pk=None):
        configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
        runner = CrawlerRunner()
        d = runner.crawl(ArticleSpider)
        d.addBoth(lambda _: reactor.stop())
        reactor.run()  # the script will block here until the crawling is finished
        return HttpResponse('')
