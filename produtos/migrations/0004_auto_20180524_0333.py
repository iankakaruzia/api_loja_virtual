# Generated by Django 2.0.5 on 2018-05-24 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_produtos_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='quantidade',
            field=models.IntegerField(choices=[(1, 'Processadores'), (2, 'Memória RAM'), (3, 'Disco Rígido/SSD'), (4, 'Placa de Vídeo'), (5, 'Gabinete'), (6, 'Placa Mãe'), (7, 'Fonte')]),
        ),
    ]
