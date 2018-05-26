from rest_framework.viewsets import ModelViewSet
from pedidos.models import Pedidos
from .serializers import PedidoSerializer


class PedidoViewSet(ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidoSerializer
