from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from usuarios.permissions import IsAdmin, IsProfissional
from .models import Prescricao
from .serializers import PrescricaoSerializer

class PrescricaoViewSet(viewsets.ModelViewSet):
    serializer_class = PrescricaoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.perfil == 'admin':
            return Prescricao.objects.all()
        elif user.perfil == 'profissional':
            return Prescricao.objects.filter(profissional__usuario=user)
        elif user.perfil == 'paciente':
            return Prescricao.objects.filter(paciente__usuario=user)
        return Prescricao.objects.none()


