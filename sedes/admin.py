from django.contrib import admin
from sedes.models import Sede

# Register your models here.
@admin.register(Sede)

class SedeAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']