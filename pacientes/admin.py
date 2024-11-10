from django.contrib import admin
from pacientes.models import Paciente
# Register your models here.
@admin.register(Paciente)

class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellidos', 'telefono', 'correo', 'sexo', 'fecha_nacimiento', 'localizacion']