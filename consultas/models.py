from django.db import models
from pacientes.models import Paciente
from profissionais.models import ProfissionalSaude
from unidades.models import UnidadeHospitalar

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    profissional = models.ForeignKey(ProfissionalSaude, on_delete=models.CASCADE, related_name='consultas')
    data = models.DateTimeField()
    observacoes = models.TextField(blank=True, null=True)
    unidade = models.ForeignKey(UnidadeHospitalar, on_delete=models.SET_NULL, null=True, related_name='consultas')
    status = models.CharField(max_length=20, choices=[
        ('agendada', 'Agendada'),
        ('realizada', 'Realizada'),
        ('cancelada', 'Cancelada'),
    ], default='agendada')

    def __str__(self):
        return f"{self.paciente.nome} com {self.profissional.nome} em {self.data.strftime('%d/%m/%Y %H:%M')}"

