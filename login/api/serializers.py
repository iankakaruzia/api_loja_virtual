from rest_framework.serializers import ModelSerializer
from login.models import Login


class LoginSerializer(ModelSerializer):
    class Meta:
        model = Login
        fields = ['email', 'senha']
