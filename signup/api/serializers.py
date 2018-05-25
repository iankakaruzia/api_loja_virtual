from rest_framework.serializers import ModelSerializer
from signup.models import Signup


class SignupSerializer(ModelSerializer):
    class Meta:
        model = Signup
        fields = ['first_name', 'last_name', 'email', 'phone', 'password']
