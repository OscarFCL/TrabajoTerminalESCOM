# Generated by Django 2.2.10 on 2020-06-11 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ofertaEducativa', '0010_auto_20200610_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidadaprendizaje',
            name='nombreUA',
            field=models.CharField(max_length=200),
        ),
    ]
