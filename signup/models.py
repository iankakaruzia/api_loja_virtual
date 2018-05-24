from django.db import models


class Signup(models.Model):
    #Atributos de SignUp
    test = models.CharField(max_length=150)