from django.contrib.auth import authenticate, login
from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import AccountModel


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountModel
        fields = ('id', 'username', 'email', 'password', 'phone', 'name')

    def logar(self, request):
        usuario_aux = User.objects.get(email=request.POST['email'])
        usuario = authenticate(username=usuario_aux.username,
                               password=request.POST["senha"])
        if usuario is not None:
            login(request, usuario)

    def create(self, request, *args, **kwargs):
        User.objects.create_user(request['username'], request['email'], request['password'])

        self.logar(request)

        return super(UserSerializer, self).create(request, *args, **kwargs)
