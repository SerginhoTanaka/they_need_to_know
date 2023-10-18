from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True )
    password = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(default=timezone.now)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/')

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
