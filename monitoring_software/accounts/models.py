from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Location(models.Model):
    name = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=2, blank=False)
    zip = models.IntegerField(blank=False)
    capacity = models.IntegerField(blank=False)
    description = models.TextField(max_length=500)


class User(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    phone = models.IntegerField(blank=False)
    notes = models.TextField(max_length=500)