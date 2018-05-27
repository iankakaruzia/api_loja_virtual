from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from accounts.api.serializers import SignupSerializer
from accounts.models import SignupModel


class SignupViewSet(ModelViewSet):

    queryset = SignupModel.objects.all()
    serializer_class = SignupSerializer

    def post(self, request, format='json'):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
