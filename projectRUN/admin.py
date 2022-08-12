from django.contrib import admin
from .models import Roles, Marcas, Permisos, RolesPermisos
# Register your models here.

@admin.register(Roles)
class RolesAdmin(admin.ModelAdmin):
    list_display = ('id_roles', 'nombre_rol')
    search_fields = ['id_roles', 'nombre_rol']
    
@admin.register(Permisos)
class PermisosAdmin(admin.ModelAdmin):
    list_display = ('nombre_permiso', 'description')
    search_fields = ['nombre_permiso', 'description']
        
    
@admin.register(Marcas)
class MarcasADmin(admin.ModelAdmin):
    list_display = ('id_marca','nombre_marca',)
    search_fields = ['id_marca', 'nombre_marca',]

@admin.register(RolesPermisos)
class RolesPermisosAdmin(admin.ModelAdmin):
    list_display = ('id_roles_permisos','roles','permisos',)
    search_fields = ['id_roles_permisos',]


"""@admin.register(Rolecitos)
class RolecitosAdmin(admin.ModelAdmin):
    list_display = ('id_rol', 'nombre_roles')"""
   