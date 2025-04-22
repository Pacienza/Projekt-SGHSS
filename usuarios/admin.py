from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ['username', 'email', 'perfil', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('perfil',)}),
    )
