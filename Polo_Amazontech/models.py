from django.db import models

class UserManager(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    cpf = models.PositiveBigIntegerField()
    