from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    cpf = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.nome


class Computador(models.Model):
    computador = models.CharField(max_length=1000)
    tipo = models.CharField(max_length=1000)
    modelo = models.CharField(max_length=1000)
    descricao = models.CharField(max_length=1000)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.computador