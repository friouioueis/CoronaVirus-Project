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
                                                           related_name='sign_moderateur', verbose_name='moderateur')
    descriptionSg                   = models.TextField(verbose_name='Description')
    validerSg                       = models.BooleanField(default=False, verbose_name='validée')
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
    validerSph                      = models.BooleanField(default=False, verbose_name='validée')

    def __str__(self):
        return 'Photo par: ' + self.idUtilisateurSph.nomUtilisateur


class videoThematique(models.Model):
    idVideoThema                    = models.AutoField(primary_key=True, editable=True)
    idUtilisateurVThema             = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE,
                                            related_name='vid_utilisateur', verbose_name='utilisateur')
    idModerateurVthema              = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE,
                                           related_name='vid_moderateur', verbose_name='moderateur')
    lienVthema                      = models.CharField(max_length=255, verbose_name='lien')
    validerVthema                   = models.BooleanField(default=False, verbose_name='validée')
    titreVthema                     = models.CharField(max_length=255, verbose_name='titre')
    descriptionVthema               = models.TextField(verbose_name='description')

    def __str__(self):
        return 'Video par: ' + self.idUtilisateurVThema.nomUtilisateur