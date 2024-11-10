from django.contrib import admin
from formadepagos.models import FormasPago 
# Register your models here.
@admin.register(FormasPago)

class FormasPagoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']