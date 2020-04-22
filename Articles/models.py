from django.db import models
from Utilisateurs.models import compteUtilisateur



class article(models.Model):
    idArticle                       = models.AutoField(primary_key=True, editable=False)
    idRedacteurAr                   = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE,
                                            related_name='art_redacteur', verbose_name='redacteur')
    idModerateurAr                  = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE,
                                            related_name='art_moderateur', verbose_name='moderateur',
                                            null=True,blank=True)
    dateAr                          = models.DateTimeField(verbose_name='date de redaction')
    contenuAr                       = models.TextField(verbose_name='Contenu')
    terminerAR                      = models.BooleanField(default=False, verbose_name='Terminé', null=True, blank=True)
    validerAR                       = models.BooleanField(default=False, verbose_name='Validé', null=True, blank=True)
    refuserAR                       = models.BooleanField(default=False, verbose_name='refusé', null=True, blank=True)

    @property
    def photos(self):
        return self.photoarticle_set.all()

    @property
    def videos(self):
        return self.videoarticle_set.all()

    def __str__(self):
        return 'Article redigé par: ' + self.idRedacteurAr.username



class videoArticle(models.Model):
    idVideo                         = models.AutoField(primary_key=True, editable=False)
    idArticleVd                     = models.ForeignKey(article, on_delete=models.CASCADE, verbose_name='article')
    lienViAc                        = models.CharField(max_length=255, verbose_name='lien')

    def __str__(self):
        return 'video pour article n°: ' + str(self.idArticleVd)

class photoArticle(models.Model):
    idPhoto                         = models.AutoField(primary_key=True, editable=False)
    idArticlePh                     = models.ForeignKey(article, on_delete=models.CASCADE, verbose_name='article')
    lienPhAc                        = models.CharField(max_length=255, verbose_name='lien')

    def __str__(self):
        return 'photo pour article n°: ' + str(self.idArticlePh)

class commentaire(models.Model):
    idCommentaire                   = models.AutoField(primary_key=True, editable=False)
    idUtilisateurCom                = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE,
                                                           related_name='com_utilisateur', verbose_name='utilisateur')
    idModerateurCom                 = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE,
                                                           related_name='com_moderateur', verbose_name='moderateur',
                                                           null=True,blank=True)
    idArticleCom                    = models.ForeignKey(article, on_delete=models.CASCADE, verbose_name='article')
    contenuCom                      = models.TextField(verbose_name='contenu')
    signalerCom                     = models.BooleanField(default=False, verbose_name='signalé', null=True,blank=True)

    def __str__(self):
        return 'commentaire pour article n°: ' + str(self.idArticleCom) + \
               ' par: ' + self.idUtilisateurCom.nomUtilisateur


class videoThematique(models.Model):
    idVideoThema                    = models.AutoField(primary_key=True, editable=True)
    idUtilisateurVThema             = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE,
                                            related_name='vid_utilisateur', verbose_name='utilisateur')
    idModerateurVthema              = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE,
                                           related_name='vid_moderateur', verbose_name='moderateur')
    lienVthema                      = models.CharField(max_length=255, verbose_name='lien')
    validerVthema                   = models.BooleanField(default=False, verbose_name='validée')
    refuserVthema                   = models.BooleanField(default=False, verbose_name='refusée')
    titreVthema                     = models.CharField(max_length=255, verbose_name='titre')
    descriptionVthema               = models.TextField(verbose_name='description')

    def __str__(self):
        return 'Video par: ' + self.idUtilisateurVThema.nomUtilisateur