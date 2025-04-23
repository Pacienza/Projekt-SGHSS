from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from consultas.models import Consulta
from pacientes.models import Paciente
from profissionais.models import ProfissionalSaude
from prescricoes.models import Prescricao
from internacoes.models import Internacao
from unidade.models import UnidadeHospitalar

class ResumoGeralView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        unidade_id = request.query_params.get('unidade')

        filtros = {}
        if unidade_id:
            filtros['unidade_id'] = unidade_id

        return Response({
            "unidade": UnidadeHospitalar.objects.get(id=unidade_id).nome if unidade_id else "Todas",
            "total_consultas": Consulta.objects.filter(**filtros).count(),
            "total_prontuarios": Prontuario.objects.filter(**filtros).count(),
            "total_prescricoes": Prescricao.objects.filter(**filtros).count(),
            "total_internacoes": Internacao.objects.filter(**filtros).count(),
            "total_pacientes": Paciente.objects.count(),  # pode ou não depender da unidade
        })
