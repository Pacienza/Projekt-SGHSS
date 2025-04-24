from rest_framework import serializers
from .models import AgendaProfissional

class AgendaProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendaProfissional
        fields = '__all__'