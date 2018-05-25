from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Signup(models.Model):
    first_name = models.CharField(max_length=600, default='')
    last_name = models.CharField(max_length=600, default='')
    email = models.EmailField(max_length=254, default='')
    phone = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.first_name

    @receiver(post_save, sender=User)
    def create_user(sender, instance, created, **kwargs):
        if created:
            Signup.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
