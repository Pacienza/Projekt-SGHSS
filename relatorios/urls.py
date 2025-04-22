from django.urls import path
from .views import ResumoGeralView

urlpatterns = [
    path('resumo-geral/', ResumoGeralView.as_view(), name='resumo-geral'),
]
