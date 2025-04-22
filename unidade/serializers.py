from rest_framework import serializers
from .models import UnidadeHospitalar

class UnidadeHospitalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeHospitalar
        fields = '__all__'
