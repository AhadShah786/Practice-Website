from django.db import models


# Create your models here.
class aloochat(models.Model):
    name = models.CharField(max_length=15)
    reply = models.CharField(max_length=20)
    