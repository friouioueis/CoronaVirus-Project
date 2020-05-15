from django.forms import model_to_dict
from rest_access_policy import AccessPolicy


class InfoSanteAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["retrieve","destroy","update","partial_update"],
            "principal": ["*"],
            "effect": "allow",
            "condition": "is_author"
        },
        {
            "action": ["list"],
            "principal": ["*"],
            "effect": "deny"
        },
        {
            "action": ["create"],
            "principal": ["*"],
            "effect": "allow"
        },
    ]
    def is_author(self, request, view, action) -> bool:
        info = view.get_object()
        return request.user == info.idUtilisateurIs

class UtilisateurInfoSanteAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["retrieve"],
            "principal": ["*"],
            "effect": "allow",
            "condition": "is_author"
        },
        {
            "action": ["list"],
            "principal": ["*"],
            "effect": "allow",
            "condition": "is_author2"
        },
    ]
    def is_author(self, request, view, action) -> bool:
        info = view.get_object()
        return request.user == info.idUtilisateurIs

    def is_author2(self, request, view, action) -> bool:
        info = view.get_queryset().first()
        return request.user == info.idUtilisateurIs