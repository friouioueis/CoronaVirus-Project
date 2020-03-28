# Generated by Django 3.0.4 on 2020-03-28 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='compteUtilisateur',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('idUtilisateur', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('nomUtilisateur', models.CharField(max_length=30, unique=True, verbose_name="Nom d'utilisateur")),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='role',
            fields=[
                ('idRole', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Type', models.CharField(choices=[('si', 'simple'), ('rd', 'redacteur'), ('md', 'moderateur'), ('ad', 'admin')], max_length=2)),
                ('idUtilisateurR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='infoPersonel',
            fields=[
                ('idInfoPer', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('dateNaissance', models.DateField(verbose_name='Date de naissance')),
                ('wilaya', models.CharField(max_length=30)),
                ('idUtilisateurIp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
            options={
                'verbose_name_plural': 'Infos Personnelles',
            },
        ),
    ]
