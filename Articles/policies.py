from rest_access_policy import AccessPolicy


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
