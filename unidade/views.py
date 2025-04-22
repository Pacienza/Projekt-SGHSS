from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import UnidadeHospitalar
from .serializers import UnidadeHospitalarSerializer

class UnidadeHospitalarViewSet(viewsets.ModelViewSet):
    queryset = UnidadeHospitalar.objects.all()
    serializer_class = UnidadeHospitalarSerializer
    permission_classes = [IsAuthenticated]

