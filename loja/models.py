from django.db import models


class Loja(models.Model):
    #Atributos da Loja
    nome = models.CharField(max_length=200, null=True, blank=True)
