from django.contrib import admin
from consultas.models import Consulta

# Register your models here.
@admin.register(Consulta)

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'notas_consulta', 'valor', 'id_paciente', 'envio_plan', 'id_sede', 'id_forma_pago', 'tipo_consulta']