from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from pedidos.models import Pedidos
from produtos.api.serializers import ProdutoSerializer
from produtos.models import Produtos


class PedidoSerializer(ModelSerializer):
    produtos = ProdutoSerializer(many=True)
    valor_pedido = SerializerMethodField()

    class Meta:
        model = Pedidos
        fields = ['id', 'usuario', 'produtos', 'valor_pedido', 'status']
        read_only = ['status']

    def cria_pedidos(self, produtos, p):
        for produto in produtos:
            pr = Produtos.object.create(**produto)
            p.produtos.add(pr)

    def create(self, validated_data):
        produtos = validated_data('produtos')
        del validated_data['produtos']

        p = Pedidos.object.create(**validated_data)
        self.cria_pedidos(produtos, p)

        p.save()

        return p

    def get_valor_pedido(self, obj):
        valor = 0
        prod = obj.produtos.all()
        for p in prod:
            valor = valor + p.preco
        return '%f' % valor
