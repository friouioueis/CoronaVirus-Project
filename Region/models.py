from django.db import models



class region(models.Model):
    idRegion                        = models.AutoField(primary_key=True, editable=True)
    nomRegion                       = models.CharField(max_length=30, verbose_name='nom de la région')
    is_risque                       = models.BooleanField(default=False)

    def __str__(self):
        return self.nomRegion


class statistiqueRegion(models.Model):
    idStatistique                   = models.AutoField(primary_key=True, editable=True)
    idRegionSt                      = models.ForeignKey(region, on_delete=models.CASCADE, verbose_name='region')
    nbrPorteurVirus                 = models.IntegerField(default=0, verbose_name='Nombre de proteurs')
    casConfirme                     = models.IntegerField(default=0, verbose_name='cas confirmés')
    casRetablis                     = models.IntegerField(default=0, verbose_name='cas retablis')
    nbrDeces                        = models.IntegerField(default=0, verbose_name='Nombre de deces')
    nbrGuerisons                    = models.IntegerField(default=0, verbose_name='Nombre de guerisons')
    validerSt                       = models.IntegerField(default=0, verbose_name='validée')

    def __str__(self):
        return 'Statistiques de: ' + self.idRegionSt.nomRegion

