from django.db import models
from pacientes.models import Paciente
from profissionais.models import ProfissionalSaude
from unidades.models import UnidadeHospitalar

class Internacao(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='internacoes')
    profissional = models.ForeignKey(ProfissionalSaude, on_delete=models.SET_NULL, null=True, related_name='internacoes')
    data_entrada = models.DateTimeField()
    data_alta = models.DateTimeField(blank=True, null=True)
    motivo = models.CharField(max_length=255)
    observacoes = models.TextField(blank=True, null=True)
    leito = models.CharField(max_length=20, blank=True, null=True)
    unidade = models.ForeignKey(UnidadeHospitalar, on_delete=models.SET_NULL, null=True, related_name='internacoes')

    def __str__(self):
        return f"{self.paciente.usuario.username} - Internado em {self.data_entrada.strftime('%d/%m/%Y')}"
