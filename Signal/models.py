from django.db import models
from django.db.models import EmailField
from django_mysql.models import ListTextField

from Utilisateurs.models import compteUtilisateur

SIGNALEMENT_CHOICES = (
    ('ph', 'photo'),
    ('vi', 'video')
)

class emailCCC (models.Model):
    idEmail=models.AutoField(primary_key=True, editable=False)
    subject = models.TextField(verbose_name='Titre')
    message = models.TextField(verbose_name='Message')
    email_from = models.EmailField(verbose_name='source')
    recipient_list = ListTextField(
        base_field=EmailField(),
        size=100,
    )
    attach=models.TextField(verbose_name='piece jointe')

    def __str__(self):
        return 'email titre: ' + self.subject

class signalement(models.Model):
    idSignal                        = models.AutoField(primary_key=True, editable=False)
    idUtilisateurSg                 = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE,
                                                        related_name='sign_utilisateur', verbose_name='utilisateur',null=True, blank=True)
    idModerateurSg                  = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE,
                                                        related_name='sign_moderateur', verbose_name='moderateur',
                                                        null=True, blank=True)
    descriptionSg                   = models.TextField(verbose_name='Description')
    validerSg                       = models.BooleanField(default=None, verbose_name='validé',null=True, blank=True)
    dateSg                          = models.DateTimeField(auto_now=True, verbose_name='Date de signalement')
    typeSg                          = models.CharField(max_length=2, choices=SIGNALEMENT_CHOICES, verbose_name='type')
    lienSg                          = models.ImageField(upload_to='signalement/', verbose_name='lien')

    def __str__(self):
        return 'Signalement par: ' + self.idUtilisateurSg.username



class selfPhoto(models.Model):
    idSelfPhoto                     = models.AutoField(primary_key=True, editable=True)
    idUtilisateurSph                = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE,
                                                           related_name='sphoto_utilisateur', verbose_name='utilisateur')
    idModerateurSph                 = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE,
                                                           related_name='sphoto_moderateur', verbose_name='moderateur')
    lienSph                         = models.CharField(max_length=255, verbose_name='lien')

    def __str__(self):
        return 'Photo par: ' + self.idUtilisateurSph.username
