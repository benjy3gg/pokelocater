from django.db import models

class Pokemon(models.Model):
    id = models.CharField(max_length=255, default='')
    spawn = models.CharField(max_length=255, default='')
    lat = models.CharField(max_length=255, default='')
    long = models.CharField(max_length=255, default='')
    expires = models.DateTimeField(null=True)