from django.db import models
from consultas.models import Consulta
# Create your models here.
class Medida(models.Model):
    id_medida = models.BigAutoField(primary_key=True)
    id_consulta = models.ForeignKey(Consulta, on_delete=models.SET_NULL, null=True, db_column='id_consulta')
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    talla = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sub_escapular = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tricep = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    supra_espinal = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    abdo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    muslo_anterior = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pierna_medial = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    brazo_relajado = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cintura = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cadera = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    muslo_medial = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pierna = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medidas'
    
    