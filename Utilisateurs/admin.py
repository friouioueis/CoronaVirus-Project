from django.contrib import admin
from .models import compteUtilisateur, role, infoPersonel


admin.site.register(compteUtilisateur)
admin.site.register(role)
admin.site.register(infoPersonel)
