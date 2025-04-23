from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InternacaoViewSet

router = DefaultRouter()
router.register(r'internacoes', InternacaoViewSet, basename='internacoes')

urlpatterns = [
    path('', include(router.urls)),
]
