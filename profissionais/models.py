from django.db import models
from usuarios.models import Usuario

class ProfissionalSaude(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='profissional')
    cpf = models.CharField(max_length=11, unique=True)
    especialidade = models.CharField(max_length=100)
    crm = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.usuario.username

