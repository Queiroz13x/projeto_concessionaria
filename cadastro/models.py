from django.db import models

# Create your models here.
class Marca (models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
      ordering = ['nome']

class Cliente (models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.nome} - {self.telefone} - {self.email}'

class Modelo(models.Model):  
    marca = models.ForeignKey(Marca, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome} - {self.marca.nome}'
    
    