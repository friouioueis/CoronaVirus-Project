from rest_access_policy import AccessPolicy


class SignalAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["create"],
            "principal": ["*"],
            "effect": "allow"
        },
        {
            "action": ["destroy","update"],
            "principal": ["*"],
            "effect": "allow",
            "condition": "is_author"
        },
        {
            "action": ["list","retrieve","destroy","partial_update"],
            "principal": ["group:md"],
            "effect": "allow",
        },
    ]
    def is_author(self, request, view, action) -> bool:
        s = view.get_object()
        return request.user == s.idUtilisateurSg