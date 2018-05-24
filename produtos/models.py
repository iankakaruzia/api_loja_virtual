from django.db import models

CATEGORIAS = (
    (1, 'Processadores'),
    (2, 'Memória RAM'),
    (3, 'Disco Rígido/SSD'),
    (4, 'Placa de Vídeo'),
    (5, 'Gabinete'),
    (6, 'Placa Mãe'),
    (7, 'Fonte'),
)


class Produtos(models.Model):

    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=1000000, decimal_places=2)
    quantidade = models.IntegerField(default=1)
    categoria = models.IntegerField(choices=CATEGORIAS, default=1)

    def __str__(self):
        return self.nome
