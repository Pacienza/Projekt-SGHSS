from rest_framework import serializers
from .models import Telemedicina

class TelemedicinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telemedicina
        fields = '__all__'