from rest_access_policy import AccessPolicy


class RegionAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list","retrieve"],
            "principal": ["*"],
            "effect": "allow"
        },
        {
            "action": ["destroy","update","partial_update","create"],
            "principal": ["group:ad"],
            "effect": "allow"
        },
        {
            "action": ["isRisque"],
            "principal": ["group:as"],
            "effect": "allow"
        },

    ]

class StatistiquesAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ["group:as","group:md"],
            "effect": "allow"
        },
        {
            "action": ["create","destroy"],
            "principal": ["group:as"],
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update"],
            "principal": ["group:md"],
            "effect": "allow"
        },
    ]
