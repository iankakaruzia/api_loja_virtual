from django.contrib.auth import authenticate, login
from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import SignupModel, LoginModel


class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = SignupModel
        fields = ('id', 'username', 'email', 'password', 'phone', 'name')

    def create(self, request, *args, **kwargs):
        User.objects.create_user(request['username'], request['email'], request['password'])

        return super(SignupSerializer, self).create(request, *args, **kwargs)


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoginModel
        fields = ('id', 'email')

    def logar(self, request):
        usuario_aux = User.objects.get(email=request.POST['email'])
        usuario = authenticate(username=usuario_aux.username,
                               password=request.POST["senha"])
        if usuario is not None:
            login(request, usuario)
