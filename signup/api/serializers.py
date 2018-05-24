from rest_framework.serializers import ModelSerializer
from signup.models import Signup


class SignupSerializer(ModelSerializer):
    class Meta:
        model = Signup
        fields = ['nome', 'email', 'telefone', 'senha']
