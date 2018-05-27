from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import SignupModel


class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = SignupModel
        fields = ('id', 'username', 'email', 'password', 'phone', 'name')
        write_only = ['password']

    def create(self, request, *args, **kwargs):
        User.objects.create_user(request['username'], request['email'], request['password'])

        return super(SignupSerializer, self).create(request, *args, **kwargs)

