# Generated by Django 2.0.5 on 2018-05-27 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0008_auto_20180526_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='status',
            field=models.CharField(default='Pedido Realizado', max_length=30),
        ),
    ]
