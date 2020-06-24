from django.forms import model_to_dict
from rest_access_policy import AccessPolicy

from Articles.models import article


class ArticleAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list","retrieve","create"],
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

class ArticleTermineAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list","retrieve"],
            "principal": ["group:rd","group:md"],
            "effect": "allow"
        },
    ]


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
        return request.user == ar.idRedacteurAr


class ModerateurAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["retrieve"],
            "principal": ["group:md"],
            "effect": "allow",
            "condition": "is_moderateur"
        },
        {
            "action": ["list"],
            "principal": ["group:md"],
            "effect": "allow"
        },
    ]

    def is_moderateur(self, request, view, action) -> bool:
        ar = view.get_object()
        return request.user == ar.idModerateurAr


class CommentaireAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list","retrieve"],
            "principal": ["*"],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ["*"],
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "principal": ["*"],
            "effect": "allow",
            "condition": "is_author"
        },
        {
            "action": ["signaler"],
            "principal": ["*"],
            "effect": "allow",
        },
        {
            "action": ["modifier"],
            "principal": ["*"],
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
