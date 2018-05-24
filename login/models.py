from django.db import models


class Login(models.Model):
    #Atributos de Login
    test = models.CharField(max_length=150)