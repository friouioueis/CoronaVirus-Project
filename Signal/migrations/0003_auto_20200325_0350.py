# Generated by Django 3.0.4 on 2020-03-25 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Signal', '0002_auto_20200325_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selfphoto',
            name='lienSph',
            field=models.CharField(max_length=255, verbose_name='lien'),
        ),
        migrations.AlterField(
            model_name='selfphoto',
            name='validerSph',
            field=models.BooleanField(default=False, verbose_name='validée'),
        ),
        migrations.AlterField(
            model_name='signalement',
            name='dateSg',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de signalement'),
        ),
        migrations.AlterField(
            model_name='signalement',
            name='descriptionSg',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='signalement',
            name='lienSg',
            field=models.CharField(max_length=255, verbose_name='lien'),
        ),
        migrations.AlterField(
            model_name='signalement',
            name='typeSg',
            field=models.CharField(choices=[('ph', 'photo'), ('vi', 'video')], max_length=2, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='signalement',
            name='validerSg',
            field=models.BooleanField(default=False, verbose_name='validée'),
        ),
        migrations.AlterField(
            model_name='videothematique',
            name='descriptionVthema',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='videothematique',
            name='lienVthema',
            field=models.CharField(max_length=255, verbose_name='lien'),
        ),
        migrations.AlterField(
            model_name='videothematique',
            name='titreVthema',
            field=models.CharField(max_length=255, verbose_name='titre'),
        ),
        migrations.AlterField(
            model_name='videothematique',
            name='validerVthema',
            field=models.BooleanField(default=False, verbose_name='validée'),
        ),
    ]