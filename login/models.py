from django.db import models


class Login(models.Model):
    email = models.EmailField(max_length=254, null=True, blank=True)
    senha = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.email
