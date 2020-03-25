from django.db import models
from Utilisateurs.models import compteUtilisateur

NOTIFICATION_CHOICES = (
    ('zd', 'zone dangereuse'),
    ('vv', 'video validée'),
    ('md', 'malade'),
    ('sg', 'signalement'),
)


class notifUtilisateur(models.Model):
    idNotif                             = models.AutoField(primary_key=True, editable=False)
    idUtilisateurNf                     = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE, verbose_name='utilisateur')
    typeNotif                           = models.CharField(max_length=2, choices=NOTIFICATION_CHOICES, verbose_name='type')
    contenuNotif                        = models.TextField(verbose_name='contenu')

    def __str__(self):
        return 'Notification n° ' + str(self.idNotif) + ' Par: ' + self.idUtilisateurNf.nomUtilisateur



