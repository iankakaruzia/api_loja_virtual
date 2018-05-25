from rest_framework.serializers import ModelSerializer
from pedidos.models import Pedidos


class PedidoSerializer(ModelSerializer):
    class Meta:
        model = Pedidos
        fields = ['id', 'usuario', 'produtos']
