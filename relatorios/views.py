from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from consultas.models import Consulta
from pacientes.models import Paciente
from profissionais.models import ProfissionalSaude
from prescricoes.models import Prescricao
from internacoes.models import Internacao

class ResumoGeralView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        return Response({
            "total_pacientes": Paciente.objects.count(),
            "total_profissionais": ProfissionalSaude.objects.count(),
            "total_consultas": Consulta.objects.count(),
            "total_prescricoes": Prescricao.objects.count(),
            "total_internacoes": Internacao.objects.count()
        })

