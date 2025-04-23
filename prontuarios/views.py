from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from usuarios.permissions import IsAdmin, IsProfissional
from .models import Prontuario
from .serializers import ProntuarioSerializer

class ProntuarioViewSet(viewsets.ModelViewSet):
    queryset = Prontuario.objects.all()
    serializer_class = ProntuarioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.perfil == 'admin':
            return Prontuario.objects.all()
        elif user.perfil == 'profissional':
            return Prontuario.objects.filter(profissional__usuario=user)
        elif user.perfil == 'paciente':
            return Prontuario.objects.filter(paciente__usuario=user)
        return Prontuario.objects.none()


