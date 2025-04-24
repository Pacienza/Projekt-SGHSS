from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Consulta
from .serializers import ConsultaSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.perfil == 'admin':
            return Consulta.objects.all()
        elif user.perfil == 'profissional':
            return Consulta.objects.filter(profissional__usuario=user)
        elif user.perfil == 'paciente':
            return Consulta.objects.filter(paciente__usuario=user)
        return Consulta.objects.none()


