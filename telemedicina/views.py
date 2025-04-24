from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from usuarios.permissions import IsAdmin, IsProfissional
from .models import Telemedicina
from .serializers import TelemedicinaSerializer

class TelemedicinaViewSet(viewsets.ModelViewSet):
    queryset = Telemedicina.objects.all()
    serializer_class = TelemedicinaSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsProfissional)]
