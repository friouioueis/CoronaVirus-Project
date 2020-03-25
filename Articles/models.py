from django.db import models
from Utilisateurs.models import compteUtilisateur



class article(models.Model):
    idArticle                   = models.AutoField(primary_key=True, editable=False)
    idRedacteurAr               = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE,
                                            related_name='art_redacteur', verbose_name='redacteur')
    idModerateurAr              = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE,
                                            related_name='art_moderateur', verbose_name='moderateur')
    dateAr                      = models.DateTimeField(auto_now=True, verbose_name='date de redaction')
    contenuAr                   = models.TextField(verbose_name='Contenu')
    validerAR                   = models.BooleanField(default=False, verbose_name='Validée')

    def __str__(self):
        return 'Article redigé par: ' + self.idRedacteurAr.nomUtilisateur


class videoArticle(models.Model):
    idVideo                     = models.AutoField(primary_key=True, editable=False)
    idArticleVd                 = models.ForeignKey(article, on_delete=models.CASCADE, verbose_name='article')
    lienViAc                    = models.CharField(max_length=255, verbose_name='lien')

    def __str__(self):
        return 'video pour article n°: ' + str(self.idArticleVd)

class photoArticle(models.Model):
    idPhoto                     = models.AutoField(primary_key=True, editable=False)
    idArticlePh                 = models.ForeignKey(article, on_delete=models.CASCADE, verbose_name='article')
    lienPhAc                    = models.CharField(max_length=255, verbose_name='lien')

    def __str__(self):
        return 'photo pour article n°: ' + str(self.idArticlePh)


class commentaire(models.Model):
    idCommentaire               = models.AutoField(primary_key=True, editable=False)
    idUtilisateurCom            = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE,
                                                           related_name='com_utilisateur', verbose_name='utilisateur')
    idModerateurCom             = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE,
                                                           related_name='com_moderateur', verbose_name='moderateur')
    idArticleCom                = models.ForeignKey(article, on_delete=models.CASCADE, verbose_name='article')
    contenuCom                  = models.TextField(verbose_name='contenu')
    signalerCom                 = models.BooleanField(default=False, verbose_name='signalé')

    def __str__(self):
        return 'commentaire pour article n°: ' + str(self.idArticleCom) + \
               ' par: ' + self.idUtilisateurCom.nomUtilisateur
