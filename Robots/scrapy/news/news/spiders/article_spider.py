from datetime import datetime

import pytz
import scrapy
from dateutil.parser import parse
from urllib.parse import urlparse


from Robots.scrapy.news.news.items import ArticleItem


class ArticleSpider(scrapy.Spider):
    name = "articles"
    allowed_domains = ["*"]
    keywords = ['coronavirus','corona', 'covid', 'COVID-19', 'كوفيد', 'COVID19', 'covid19', 'Corona', 'كوفيد19', 'كورونا']

    def parse(self, response):
        parsed_uri = urlparse(response.url)
        for news in response.css('item'):
            title = news.css('title::text').get('').strip()
            description = news.css('description::text').get('').strip()
            date=parse(news.css('pubDate::text').get()).astimezone(pytz.utc)\
                .strftime('%Y-%m-%dT%H:%M')
            if (date is not None):
                if (self.is_corona_related(title) or self.is_corona_related(description)) and parse(date) > parse(
                        self.dateDebut) and parse(date) < parse(self.dateFin):
                    item = ArticleItem()
                    item['lien'] = response.urljoin(news.css('link::text').get().strip())
                    item['titre'] = title
                    item['source'] = '.'.join(parsed_uri.netloc.split('.')[-2:])
                    item['datePub'] = date
                    item['langue'] = self.langue
                    item.save()


    def is_corona_related(self, text):
        for keyword in self.keywords:
            if keyword in text.lower():
                return True
        return False
