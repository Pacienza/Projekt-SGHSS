from rest_framework import serializers
from .models import Internacao

class InternacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internacao
        fields = '__all__'
