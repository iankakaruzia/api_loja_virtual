from django.db import models
from django.contrib.auth.models import User
from produtos.models import Produtos


class Pedidos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    produtos = models.ManyToManyField(Produtos)
    status = models.IntegerField(default=1) #Pode mudar para CharField

    def __str__(self):
        return super.usuario.username

    @property
    def calcular_valor_pedido(self):
        valor = 0
        for p in self.produtos:
            valor += valor + p.preco
        return valor
