from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from datetime import datetime
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
        profissional_id = request.query_params.get('profissional')
        inicio = request.query_params.get('inicio')
        fim = request.query_params.get('fim')

        filtros = {}
        if unidade_id:
            filtros['unidade_id'] = unidade_id
        if profissional_id:
            filtros['profissional_id'] = profissional_id

        filtros_data = {}
        if inicio and fim:
            try:
                dt_inicio = datetime.strptime(inicio, '%d/%m/%Y')
                dt_fim = datetime.strptime(fim, '%d/%m/%Y')
                filtros_data = {'data_entrada__range': (dt_inicio, dt_fim)}
            except ValueError:
                return Response(
                    {'erro': 'Formato de data inválido. Use dd/mm/aaaa.'},
                    status=400
                )

        return Response({
            "unidade": UnidadeHospitalar.objects.get(id=unidade_id).nome if unidade_id else "Todas",
            "total_consultas": Consulta.objects.filter(**filtros, **filtros_data).count(),
            "total_prescricoes": Prescricao.objects.filter(**filtros, **filtros_data).count(),
            "total_internacoes": Internacao.objects.filter(**filtros, **filtros_data).count(),
            "total_pacientes": Paciente.objects.count()
        })
