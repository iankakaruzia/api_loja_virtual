from django.contrib.auth.models import User
from django.db import models

from produtos.models import Produtos


class Pedidos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produtos)
    status = models.IntegerField(default=1)


