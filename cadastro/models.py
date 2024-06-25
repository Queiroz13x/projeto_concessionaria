from django.db import models

# Create your models here.
class Marca (models.Model):
    nome = models.CharField(max_length=100)

    def _str_(self):
        return self.nome

class Cliente (models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


    def _str_(self):
        return f'{self.nome} - {self.telefone} - {self.email}'
    