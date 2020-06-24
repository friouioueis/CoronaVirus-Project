from django.db import models
from Utilisateurs.models import compteUtilisateur


LANGUE_CHOICES = (
    ('ar', 'arabe'),
    ('fr', 'français')
)

class pubGoogleNews(models.Model):
    idPubGN                   = models.AutoField(primary_key=True, editable=True)
    lienPubGN                       = models.CharField(max_length=255, verbose_name='lien')
    source = models.CharField(max_length=512, verbose_name='source', null=True, blank=True)
    auteur = models.CharField(max_length=512, verbose_name='auteur', null=True, blank=True)
    titre = models.CharField(max_length=512, verbose_name='titre')
    langue = models.CharField(max_length=2, choices=LANGUE_CHOICES, verbose_name='langue', null=True, blank=True)
    dateGN                          = models.DateTimeField(verbose_name='date de publication')
    dateExt = models.DateTimeField(auto_now=True, verbose_name='date de scrapping')
    validerGN                       = models.BooleanField(default=None, verbose_name='validée',null=True, blank=True)
    idModerateurGN                  = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE,
                                        related_name='gn_moderateur', verbose_name='moderateur',
                                        null=True, blank=True)


    def __str__(self):
        return 'Pub google news n°: ' + str(self.idPubGN)


class pubYoutube(models.Model):
    idPubYoutube                    = models.AutoField(primary_key=True, editable=True)
    videoId                         = models.CharField(max_length=255, verbose_name='video_id')
    dateYt                          = models.DateTimeField(verbose_name='date de publication')
    titreYt                         = models.CharField(max_length=512, verbose_name='titre')
    chaineYt                        = models.CharField(max_length=255,verbose_name='chaine')
    dateExt = models.DateTimeField(auto_now=True, verbose_name='date de scrapping')
    validerYt                       = models.BooleanField(default=None, verbose_name='validée',null=True, blank=True)
    idModerateurYt                  = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE,
                                        related_name='yt_moderateur', verbose_name='moderateur',
                                        null=True, blank=True)
    def __str__(self):
        return 'Pub Youtube n°: ' + str(self.idPubYoutube)


class Article(models.Model):
    id = models.AutoField(primary_key=True, editable=True)
    titre = models.CharField(max_length=512, verbose_name='titre')
    lien = models.CharField(max_length=512, verbose_name='lien')
    source = models.CharField(max_length=512, verbose_name='source')
    datePub = models.DateTimeField(verbose_name='date de publication')
    langue =models.CharField(max_length=2, choices=LANGUE_CHOICES, verbose_name='langue',null=True, blank=True)
    dateExt=models.DateTimeField(auto_now=True, verbose_name='date de scrapping')
    validerAr = models.BooleanField(default=None, verbose_name='validée', null=True, blank=True)
    idModerateurSw = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE,
                                       related_name='ar_moderateur', verbose_name='moderateur',
                                       null=True, blank=True)

    def __str__(self):
        return self.titre
