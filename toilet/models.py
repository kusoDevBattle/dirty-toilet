from django.db import models
from django.contrib.auth.models import User


class Toilet(models.Model):
    place = models.CharField(blank=False, max_length=255)
    comment = models.CharField(blank=False, max_length=1000)
    latitude = models.CharField(blank=True, max_length=20)
    longitude = models.CharField(blank=True, max_length=20)
    level = models.IntegerField()
    user = models.ForeignKey(User)
