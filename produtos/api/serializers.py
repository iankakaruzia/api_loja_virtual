from rest_framework.serializers import ModelSerializer
from produtos.models import Produtos


class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produtos
        fields = ['nome', 'preco', 'quantidade', 'categoria']
        write_only = ['quantidade']
