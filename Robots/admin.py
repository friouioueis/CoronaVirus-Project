from django.contrib import admin
from .models import pubYoutube, pubSiteWeb, pubFacebook, Article

admin.site.register(pubFacebook)
admin.site.register(pubSiteWeb)
admin.site.register(pubYoutube)
admin.site.register(Article)