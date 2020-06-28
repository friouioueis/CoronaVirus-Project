from rest_access_policy import AccessPolicy



class UserAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["create"],
            "principal": ["group:ad"],
            "effect": "allow"
        },
        {
            "action": ["list", "retrieve"],
            "principal": ["*"],
            "effect": "allow"
        }


    ]