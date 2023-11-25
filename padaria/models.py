from django.db import models

class padaria(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    endereco = models.CharField(max_length=200, null=False, blank=False)
    telefone = models.IntegerField(null=False, blank=False)
    dia = models.DateField(null=False)
