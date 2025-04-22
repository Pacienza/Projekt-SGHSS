from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.perfil == 'admin'

class IsProfissional(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.perfil == 'profissional'

class IsPaciente(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.perfil == 'paciente'
