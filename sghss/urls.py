from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)

# Rotas do sistema
urlpatterns = [
    path('admin/', admin.site.urls),
    # ENDPOINTS ATORES DO SISTEMA
    path('api/', include('usuarios.urls')),
    path('api/', include('pacientes.urls')),
    path('api/', include('profissionais.urls')),
    path('api/', include('prontuarios.urls')),

    
    # ENDPOINTS FUNÇÔES DO SISTEMA
    path('api/', include('consultas.urls')),

    
    # Swagger
    path('api/', include('docs.urls')),
    
    # Autenticação JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
