from rest_framework.viewsets import ModelViewSet
from pedidos.models import Pedidos
from .serializers import PedidoSerializer


class PedidoViewSet(ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidoSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
