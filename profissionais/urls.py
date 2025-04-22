from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfissionalSaudeViewSet

router = DefaultRouter()
router.register(r'profissionais', ProfissionalSaudeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
