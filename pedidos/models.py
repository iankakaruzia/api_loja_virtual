from django.contrib.auth.models import User
from django.db import models

from produtos.models import Produtos


class Pedidos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    produtos = models.ManyToManyField(Produtos)
    status = models.CharField(max_length=30, default='Pedido Realizado')


