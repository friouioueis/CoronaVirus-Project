# Generated by Django 3.0.3 on 2020-05-22 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Robots', '0002_beer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='type',
            field=models.CharField(max_length=200),
        ),
    ]
