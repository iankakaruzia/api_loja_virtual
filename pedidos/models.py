from django.contrib.auth.models import User
from django.db import models

from produtos.models import Produtos


class Pedidos(models.Model):
    produtos = models.ManyToManyField(Produtos)
    status = models.IntegerField(default=1) #Pode mudar para CharField



    @property
    def calcular_valor_pedido(self):
        valor = 0
        for p in self.produtos:
            valor += valor + p.preco
        return valor
