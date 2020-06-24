from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor

from .scrapy.news.news.spiders.article_spider import ArticleSpider
from .scrapy.news.news.spiders.news import news
from .scrapy.news.news.spiders.youtube import youtube_spider


def SpidersManager (langue,source,dateDebut,dateFin):
    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    runner = CrawlerRunner()
    sources=[]
    if 'youtube' in source:
        if langue=='ar':
            q="كورونا"
        else:
            q="corona"
        youtube_spider(q,dateDebut,dateFin)
    if 'google news' in source:
        news(langue,dateDebut,dateFin)
    if langue=='ar':
        if 'bbc' in source:
            sources.append('https://www.bbc.com/arabic/worldnews/index.xml')
        if 'france24' in source:
            sources.append('https://www.france24.com/ar/rss')
        if 'cnn' in source:
            sources.append('https://arabic.cnn.com/api/v1/rss/rss.xml')
        if 'un' in source:
            sources.append('https://news.un.org/feed/subscribe/ar/news/topic/health/feed/rss.xml')
        if 'arabia' in source:
            sources.append('https://www.alarabiya.net/.mrss/ar/medicine-and-health.xml')
    else:
        if 'who' in source:
            sources.append('https://www.who.int/rss-feeds/news-french.xml')
        if 'france24' in source:
            sources.append('https://www.france24.com/fr/rss')
        if 'un' in source:
            sources.append('https://news.un.org/feed/subscribe/fr/news/topic/health/feed/rss.xml')
    d = runner.crawl(ArticleSpider,start_urls=sources, langue=langue,dateDebut=dateDebut,dateFin=dateFin)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
    return None