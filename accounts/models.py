from django.db import models


class AccountModel(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=50, default='')
    name = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.username


class LoginModel(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email