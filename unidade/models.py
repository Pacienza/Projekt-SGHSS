from django.db import models

class UnidadeHospitalar(models.Model):
    nome = models.CharField(max_length=120)
    endereco = models.TextField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome
