from django.db import models
from Utilisateurs.models import compteUtilisateur

SIGNALEMENT_CHOICES = (
    ('ph', 'photo'),
    ('vi', 'video')
)

class signalement(models.Model):
    idSignal                        = models.AutoField(primary_key=True, editable=False)
    idUtilisateurSg                 = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE,
                                                        related_name='sign_utilisateur', verbose_name='utilisateur')
    idModerateurSg                  = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE,
                                                        related_name='sign_moderateur', verbose_name='moderateur',
                                                        null=True, blank=True)
    descriptionSg                   = models.TextField(verbose_name='Description')
    validerSg                       = models.BooleanField(default=False, verbose_name='validée',null=True, blank=True)
    refuserSg                       = models.BooleanField(default=False, verbose_name='refusée',null=True, blank=True)
    dateSg                          = models.DateTimeField(auto_now=True, verbose_name='Date de signalement')
    typeSg                          = models.CharField(max_length=2, choices=SIGNALEMENT_CHOICES, verbose_name='type')
    lienSg                          = models.CharField(max_length=255, verbose_name='lien')

    def __str__(self):
        return 'Signalement par: ' + self.idUtilisateurSg.nomUtilisateur


class selfPhoto(models.Model):
    idSelfPhoto                     = models.AutoField(primary_key=True, editable=True)
    idUtilisateurSph                = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE,
                                                           related_name='sphoto_utilisateur', verbose_name='utilisateur')
    idModerateurSph                 = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE,
                                                           related_name='sphoto_moderateur', verbose_name='moderateur')
    lienSph                         = models.CharField(max_length=255, verbose_name='lien')

    def __str__(self):
        return 'Photo par: ' + self.idUtilisateurSph.nomUtilisateur
