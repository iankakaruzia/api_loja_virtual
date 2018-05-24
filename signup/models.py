from django.db import models


class Signup(models.Model):
    nome = models.CharField(max_length=600, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    senha = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nome
