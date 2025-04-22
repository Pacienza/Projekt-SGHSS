from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Consulta
from .serializers import ConsultaSerializer
from usuarios.permissions import IsProfissional, IsAdmin

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [IsProfissional | IsAdmin]

