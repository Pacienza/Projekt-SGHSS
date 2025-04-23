from django.db import models
from pacientes.models import Paciente
from profissionais.models import ProfissionalSaude
from unidade.models import UnidadeHospitalar

class Prontuario(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='prontuarios')
    profissional = models.ForeignKey(ProfissionalSaude, on_delete=models.SET_NULL, null=True, related_name='prontuarios')
    unidade = models.ForeignKey(UnidadeHospitalar, on_delete=models.SET_NULL, null=True, related_name='prontuarios')
    data_registro = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Prontuário de {self.paciente.usuario.username} em {self.data_registro.strftime("%d/%m/%Y %H:%M")}'

