from django.db import models
from usuarios.models import Usuario
from unidade.models import UnidadeHospitalar


class Paciente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='paciente')
    unidade = models.ForeignKey(UnidadeHospitalar, on_delete=models.SET_NULL, null=True, related_name='paciente')
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.usuario.username

