from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    PERFIS = [
        ('admin', 'Administrador'),
        ('profissional', 'Profissional de Saúde'),
        ('paciente', 'Paciente'),
    ]
    perfil = models.CharField(max_length=20, choices=PERFIS, default='paciente')

    def __str__(self):
        return f"{self.username} ({self.perfil})"

