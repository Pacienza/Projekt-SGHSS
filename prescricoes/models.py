from django.db import models
from pacientes.models import Paciente
from profissionais.models import ProfissionalSaude
from unidade.models import UnidadeHospitalar

class Prescricao(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='prescricoes')
    profissional = models.ForeignKey(ProfissionalSaude, on_delete=models.SET_NULL, null=True, related_name='prescricoes')
    unidade = models.ForeignKey(UnidadeHospitalar, on_delete=models.SET_NULL, null=True, related_name='prescricoes')
    data_emissao = models.DateTimeField(auto_now_add=True)
    medicamento = models.CharField(max_length=255)
    dosagem = models.CharField(max_length=100)
    posologia = models.TextField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.medicamento} para {self.paciente.usuario.username}"

