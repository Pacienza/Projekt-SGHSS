from rest_framework.routers import DefaultRouter
from .views import AgendaProfissionalViewSet

router = DefaultRouter()
router.register(r'agenda', AgendaProfissionalViewSet)

urlpatterns = router.urls
