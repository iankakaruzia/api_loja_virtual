from django.db import models


class SignupModel(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=30, default='')
    phone = models.CharField(max_length=50, default='')
    name = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.username
