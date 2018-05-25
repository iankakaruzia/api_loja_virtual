from rest_framework.serializers import ModelSerializer
from pedidos.models import Pedidos
from produtos.api.serializers import ProdutoSerializer
from produtos.models import Produtos


class PedidoSerializer(ModelSerializer):
    produtos = ProdutoSerializer(many=True)

    class Meta:
        model = Pedidos
        fields = ['id', 'produtos', 'calcular_valor_pedido']

    def cria_pedidos(self, produtos, p):
        for produto in produtos:
            pr = Produtos.object.create(**produto)
            p.produtos.add(pr)

    def create(self, validated_data):
        produtos = validated_data('produtos')
        del validated_data['produtos']

        p = Pedidos.object.create(**validated_data)
        self.cria_atracoes(produtos, p)

        p.save()

        return p
