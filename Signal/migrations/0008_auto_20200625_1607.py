# Generated by Django 2.2.13 on 2020-06-25 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Signal', '0007_emailccc_attach'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signalement',
            name='lienSg',
            field=models.ImageField(upload_to='signalement/', verbose_name='lien'),
        ),
    ]