from rest_framework.viewsets import ModelViewSet
from pedidos.models import Pedidos
from .serializers import PedidoSerializer


class PedidoViewSet(ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidoSerializer

    def create(self, request, *args, **kwargs):
        return super(PedidoViewSet, self).create(request, *args, **kwargs)