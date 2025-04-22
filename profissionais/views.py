from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ProfissionalSaude
from .serializers import ProfissionalSaudeSerializer
from usuarios.permissions import IsAdmin, IsProfissional

class ProfissionalSaudeViewSet(viewsets.ModelViewSet):
    queryset = ProfissionalSaude.objects.all()
    serializer_class = ProfissionalSaudeSerializer
    permission_classes = [IsAdmin | IsProfissional]

