from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .serializers import SignupSerializer
from signup.models import Signup


class SignupViewSet(ModelViewSet):
    queryset = Signup.objects.all()
    serializer_class = SignupSerializer
