from django.db import models



class pubFacebook(models.Model):
    idPubFacebook                   = models.AutoField(primary_key=True, editable=True)
    lienPubFb                       = models.CharField(max_length=255, verbose_name='lien')
    DateFb                          = models.DateTimeField(verbose_name='date de publication')
    validerFb                       = models.BooleanField(default=False, verbose_name='validée')

    def __str__(self):
        return 'Pub Facebook n°: ' + str(self.idPubFacebook)


class pubYoutube(models.Model):
    idPubYoutube                    = models.AutoField(primary_key=True, editable=True)
    lienPubYt                       = models.CharField(max_length=255, verbose_name='lien')
    DateYt                          = models.DateTimeField(verbose_name='date de publication')
    validerYt                       = models.BooleanField(default=False, verbose_name='validée')

    def __str__(self):
        return 'Pub Youtube n°: ' + str(self.idPubYoutube)


class pubSiteWeb(models.Model):
    idPubWeb                        = models.AutoField(primary_key=True, editable=True)
    lienPubWeb                      = models.CharField(max_length=255, verbose_name='lien')
    DateSw                          = models.DateTimeField(verbose_name='date de publication')
    validerSw                       = models.BooleanField(default=False, verbose_name='validée')

    def __str__(self):
        return 'Pub Web n°: ' + str(self.idPubWeb)



