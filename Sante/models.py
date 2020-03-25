from django.db import models
from Utilisateurs.models import compteUtilisateur




class infoSante(models.Model):
    idInfoSante                         = models.AutoField(primary_key=True, editable=False)
    idUtilisateurIs                     = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE, verbose_name='utilisateur')
    poids                               = models.FloatField(default=0)
    temperature                         = models.FloatField(default=0)
    Rythme_cardiaque                    = models.FloatField(default=0, verbose_name='rythme cardiaque')
    dateSaisie                          = models.DateTimeField(auto_now=True, verbose_name='date de saisie')

    class Meta:
        verbose_name_plural = 'Infos Sante'

    def __str__(self):
        return 'Infos de santé de: ' + self.idUtilisateurIs.nomUtilisateur