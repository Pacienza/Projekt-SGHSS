from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from usuarios.permissions import IsAdmin, IsProfissional
from .models import Internacao
from .serializers import InternacaoSerializer

class InternacaoViewSet(viewsets.ModelViewSet):
    queryset = Internacao.objects.all()
    serializer_class = InternacaoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.perfil == 'admin':
            return Internacao.objects.all()
        elif user.perfil == 'profissional':
            return Internacao.objects.filter(profissional__usuario=user)
        elif user.perfil == 'paciente':
            return Internacao.objects.filter(paciente__usuario=user)
        return Internacao.objects.none()

