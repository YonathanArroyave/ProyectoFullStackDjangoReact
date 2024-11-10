from django.contrib import admin
from medidas.models import Medida

# Register your models here.
@admin.register(Medida)

class MedidasAdmin(admin.ModelAdmin):
    list_display = ['id_consulta', 'peso', 'talla', 'sub_escapular', 'tricep', 'supra_espinal', 'abdo', 'muslo_anterior', 'pierna_medial', 'brazo_relajado', 'cintura', 'cadera', 'muslo_medial', 'pierna']