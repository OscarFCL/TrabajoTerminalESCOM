# Generated by Django 2.2.10 on 2020-03-12 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0021_auto_20200312_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nacionalidad',
            field=models.CharField(choices=[('AL', 'Alemania'), ('BR', 'Brasil'), ('CA', 'Canada'), ('DI', 'Dinamarca'), ('EC', 'Ecuador'), ('MX', 'Mexico')], default='MX', max_length=2),
        ),
    ]
