from django.forms import model_to_dict
from rest_access_policy import AccessPolicy

from Articles.models import article


class ArticleAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list","retrieve"],
            "principal": ["*"],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ["group:rd"],
            "effect": "allow"
        },
        {
            "action": ["destroy","update"],
            "principal": ["group:rd"],
            "effect": "allow",
            "condition": "is_author"
        },
        {
            "action": ["destroy","partial_update"],
            "principal": ["group:md"],
            "effect": "allow",
        },
    ]

    def is_author(self, request, view, action) -> bool:
        article = view.get_object()
        return request.user == article.idRedacteurAr


class VideoArticleAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list","retrieve"],
            "principal": ["*"],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ["group:rd"],
            "effect": "allow"
        },
        {
            "action": ["destroy","update"],
            "principal": ["group:rd"],
            "effect": "allow",
            "condition": "is_author"
        },
        {
            "action": ["destroy","partial_update"],
            "principal": ["group:md"],
            "effect": "allow",
        },
    ]

    def is_author(self, request, view, action) -> bool:
        id = model_to_dict(view.get_object())['idArticleVd']
        ar=article.objects.filter(idArticle=id).first()
        print(ar)
        return request.user == ar.idRedacteurAr



class PhotoArticleAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list","retrieve"],
            "principal": ["*"],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ["group:rd"],
            "effect": "allow"
        },
        {
            "action": ["destroy","update"],
            "principal": ["group:rd"],
            "effect": "allow",
            "condition": "is_author"
        },
        {
            "action": ["destroy","partial_update"],
            "principal": ["group:md"],
            "effect": "allow",
        },
    ]

    def is_author(self, request, view, action) -> bool:
        id = model_to_dict(view.get_object())['idArticlePh']
        ar=article.objects.filter(idArticle=id).first()
        print(ar)
        return request.user == ar.idRedacteurAr



class ModerateurAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list","retrieve","destroy","update","partial_update"],
            "principal": ["group:md"],
            "effect": "allow",
            "condition": "is_moderateur"
        },
        {
            "action": ["create"],
            "principal": ["*"],
            "effect": "deny"
        },
    ]

    def is_moderateur(self, request, view, action) -> bool:
        article = view.get_object()
        return request.user == article.idModerateurAr


class CommentaireAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list","retrieve"],
            "principal": ["*"],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ["group:si"],
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "principal": ["group:si"],
            "effect": "allow",
            "condition": "is_author"
        },
        {
            "action": ["signaler"],
            "principal": ["group:si"],
            "effect": "allow",
        },
        {
            "action": ["modifier"],
            "principal": ["group:si"],
            "effect": "allow",
            "condition": "is_author"
        },
        {
            "action": ["update","partial_update"],
            "principal": ["*"],
            "effect": "deny",
        },
    ]

    def is_author(self, request, view, action) -> bool:
        commentaire = view.get_object()
        return request.user == commentaire.idUtilisateurCom
