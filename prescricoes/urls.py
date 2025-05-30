from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PrescricaoViewSet

router = DefaultRouter()
router.register(r'prescricoes', PrescricaoViewSet, basename='prescricoes')

urlpatterns = [
    path('', include(router.urls)),
]
