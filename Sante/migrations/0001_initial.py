# Generated by Django 3.0.4 on 2020-03-31 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='infoSante',
            fields=[
                ('idInfoSante', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('poids', models.FloatField(default=0)),
                ('temperature', models.FloatField(default=0)),
                ('Rythme_cardiaque', models.FloatField(default=0, verbose_name='rythme cardiaque')),
                ('dateSaisie', models.DateTimeField(auto_now=True, verbose_name='date de saisie')),
                ('idUtilisateurIs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
            options={
                'verbose_name_plural': 'Infos Sante',
            },
        ),
    ]