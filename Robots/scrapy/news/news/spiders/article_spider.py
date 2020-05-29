import pytz
import scrapy
from dateutil.parser import parse
from urllib.parse import urlparse


from Robots.scrapy.news.news.items import ArticleItem


class ArticleSpider(scrapy.Spider):
    name = "articles"
    allowed_domains = ["*"]
    keywords = ['coronavirus','corona', 'covid', 'COVID-19', 'كوفيد', 'COVID19', 'covid19', 'Corona', 'كوفيد19', 'كورونا']
    start_urls = [
        'https://www.who.int/rss-feeds/news-french.xml',
        'https://www.bbc.com/arabic/worldnews/index.xml',
        'https://www.france24.com/ar/rss','https://www.france24.com/fr/rss',
        'https://arabic.cnn.com/api/v1/rss/rss.xml',
        'https://news.un.org/feed/subscribe/ar/news/topic/health/feed/rss.xml',
        'https://news.un.org/feed/subscribe/fr/news/topic/health/feed/rss.xml',
        'https://www.alarabiya.net/.mrss/ar/medicine-and-health.xml',
        'http://feeds.aps.dz/APS-Sante-Science-Technologie',

    ]

    def parse(self, response):
        parsed_uri = urlparse(response.url)
        for news in response.css('item'):
            title = news.css('title::text').get('').strip()
            description = news.css('description::text').get('').strip()
            # check if the keywords are present in the title and description
            if self.is_corona_related(title) or self.is_corona_related(description):
                item = ArticleItem()
                item['lien'] = response.urljoin(news.css('link::text').get().strip())
                item['titre'] = title
                item['source'] = '.'.join(parsed_uri.netloc.split('.')[-2:])
                item['date'] = parse(news.css('pubDate::text').get()).astimezone(pytz.utc).strftime(
                        '%Y-%m-%d %H:%M:%S')
                item.save()

    def is_corona_related(self, text):
        for keyword in self.keywords:
            if keyword in text.lower():
                return True
        return False
