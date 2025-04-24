from django.db import models
from consultas.models import Consulta

class Telemedicina(Consulta):


    link_sala = models.URLField(blank=True, null=True)
    registro_video = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Consulta iniciada em {self.data.strftime('%d/%m/%Y %H:%M')}"

