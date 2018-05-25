from rest_framework.viewsets import ModelViewSet
from .serializers import LoginSerializer
from login.models import Login


class LoginViewSet(ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
