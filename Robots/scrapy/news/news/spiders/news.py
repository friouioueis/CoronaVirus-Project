from datetime import datetime

from newsapi import NewsApiClient

# Init
from Robots.scrapy.news.news.items import GNItem

newsapi = NewsApiClient(api_key='d70492be2a8b45ebbe1b8128b313c20e')

def news(langue, dateDebut,dateFin):
    response = newsapi.get_everything(q='  كورونا OR corona ',
                                          language=langue,
                                          from_param=datetime.strptime(dateDebut, '%Y-%m-%dT%H:%M'),
                                          to=datetime.strptime(dateFin,'%Y-%m-%dT%H:%M'),
                                          sort_by='relevancy')
    print(response)

    for search_result in response.get("articles", []):
        item = GNItem()
        item['titre'] = search_result["title"]
        item['lienPubGN'] =search_result["url"]
        item['auteur']=search_result["author"]
        item['source'] = search_result["source"]["name"]
        item['dateGN'] = search_result["publishedAt"]
        item['langue']=langue
        item.save()


if __name__ == "__main__":
    news()