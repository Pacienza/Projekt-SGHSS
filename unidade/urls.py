from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UnidadeHospitalarViewSet

router = DefaultRouter()
router.register(r'unidades', UnidadeHospitalarViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
