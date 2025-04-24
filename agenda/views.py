from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import AgendaProfissional
from .serializers import AgendaProfissionalSerializer

class AgendaProfissionalViewSet(viewsets.ModelViewSet):
    serializer_class = AgendaProfissionalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'profissional'):
            return AgendaProfissional.objects.filter(profissional=user.profissional)
        return AgendaProfissional.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if hasattr(user, 'profissional'):
            serializer.save(profissional=user.profissional)
