from django.contrib.auth.models import User
from django.db import models

class Item(models.Model):
    TIPO_CHOICES = [
        ('alimento', 'Alimento'),
        ('roupa', 'Roupa'),
    ]
    ESTADO_CHOICES = [
        ('novo', 'Novo'),
        ('usado', 'Usado'),
        ('bom', 'Bom Estado'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    descricao = models.CharField(max_length=255)
    quantidade = models.PositiveIntegerField()
    estado_conservacao = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    local_retirada = models.CharField(max_length=255)
    contato_doador = models.CharField(max_length=100)
    doador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='itens_doacao')
    disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.descricao}"

class Interesse(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='interesses')
    interessado = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interesses')
    data_interesse = models.DateTimeField(auto_now_add=True)
    atendido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.interessado.username} - {self.item.descricao}"