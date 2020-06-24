# Generated by Django 2.2.13 on 2020-06-20 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Robots', '0002_auto_20200620_0133'),
    ]

    operations = [
        migrations.CreateModel(
            name='pubGoogleNews',
            fields=[
                ('idPubGN', models.AutoField(primary_key=True, serialize=False)),
                ('lienPubGN', models.CharField(max_length=255, verbose_name='lien')),
                ('source', models.CharField(max_length=512, verbose_name='source')),
                ('auteur', models.CharField(max_length=512, verbose_name='auteur')),
                ('titre', models.CharField(max_length=512, verbose_name='titre')),
                ('langue', models.CharField(blank=True, choices=[('ar', 'arabe'), ('fr', 'français')], max_length=2, null=True, verbose_name='langue')),
                ('dateGN', models.DateTimeField(verbose_name='date de publication')),
                ('validerGN', models.BooleanField(blank=True, default=False, null=True, verbose_name='validée')),
                ('refuserGN', models.BooleanField(blank=True, default=False, null=True, verbose_name='refusée')),
                ('idModerateurGN', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gn_moderateur', to=settings.AUTH_USER_MODEL, verbose_name='moderateur')),
            ],
        ),
        migrations.DeleteModel(
            name='pubFacebook',
        ),
    ]
