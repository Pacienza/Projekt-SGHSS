from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TelemedicinaViewSet

router = DefaultRouter()
router.register(r'telemedicina', TelemedicinaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
