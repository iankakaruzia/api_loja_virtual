from rest_framework.viewsets import ModelViewSet
from produtos.models import Produtos
from .serializers import ProdutoSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produtos.objects.all().order_by('categoria')
    serializer_class = ProdutoSerializer