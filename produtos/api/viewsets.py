from rest_framework.viewsets import ModelViewSet
from produtos.models import Produtos
from .serializers import ProdutoSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutoSerializer
