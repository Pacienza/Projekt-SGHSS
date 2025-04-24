from django.db import models
from profissionais.models import ProfissionalSaude

class AgendaProfissional(models.Model):
    profissional = models.ForeignKey(ProfissionalSaude, on_delete=models.CASCADE, related_name='agendas')
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    class Meta:
        unique_together = ('profissional', 'data', 'hora_inicio')
        ordering = ['data', 'hora_inicio']

    def __str__(self):
        return f"{self.profissional} - {self.data} de {self.hora_inicio} até {self.hora_fim}"
