from django.db import models

class UserManager(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    cpf = models.PositiveBigIntegerField()

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    consumo = models.CharField(max_length=255)
    protocolo = models.CharField(max_length=1000)

    def __str__(self):
        return self.nome