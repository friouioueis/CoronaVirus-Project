# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

from google.oauth2.credentials import Credentials
import googleapiclient.discovery
import googleapiclient.errors

from Robots.scrapy.news.news.items import YoutubeItem


scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def youtube_spider(q,dateDebut,dateFin):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "CLIENT_SECRET_FILE.json"

    # Get credentials and create an API client

    credentials = Credentials(
        None,
        refresh_token="1//03PrUBw6basXGCgYIARAAGAMSNwF-L9IreBEtJvsMmrdlCkXWkwB3pHoWBZmqEYBSiFVHORbxAEbL_M6RTfhmMVD_wb2WvxPO9sk",
        token_uri="https://accounts.google.com/o/oauth2/token",
        client_id="505408046383-26b9r64ehc9do94dll6s4r3oijqi86pq.apps.googleusercontent.com",
        client_secret="RK6t2oDNjo-CM0HsB-ka8h-s"
    )

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.search().list(
        q=q,
        part="id,snippet",
        maxResults=50
    )
    response = request.execute()

    for search_result in response.get("items", []):
        date =search_result["snippet"]["publishedAt"]
        if search_result["id"]["kind"] == "youtube#video" and date > dateDebut and date<dateFin:
            item = YoutubeItem()
            item['videoId'] = search_result["id"]["videoId"]
            item['dateYt'] =date
            item['titreYt']=search_result["snippet"]["title"]
            item['chaineYt']=search_result["snippet"]["channelTitle"]
            item.save()

if __name__ == "__main__":
    youtube_spider()
