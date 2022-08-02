from django.db import models

# Create your models here.

class Roles(models.Model):
    id_roles = models.IntegerField(primary_key=True)
    nombre_rol = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre_rol

"""class Rolecitos(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    nombre_roles = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre_roles"""

class Permisos(models.Model):
    id_permiso = models.IntegerField(primary_key=True)
    nombre_permiso = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre_permiso
        
"""class RolesPermisos(models.Model):
    id_roles_permisos = models.IntegerField(primary_key=True)"""
    
