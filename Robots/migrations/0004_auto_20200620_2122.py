# Generated by Django 2.2.13 on 2020-06-20 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Robots', '0003_auto_20200620_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='pubgooglenews',
            name='dateExt',
            field=models.DateTimeField(auto_now=True, verbose_name='date de scrapping'),
        ),
        migrations.AddField(
            model_name='pubyoutube',
            name='dateExt',
            field=models.DateTimeField(auto_now=True, verbose_name='date de scrapping'),
        ),
    ]
