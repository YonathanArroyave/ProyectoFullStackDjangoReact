from django.db import models

# Create your models here.
class FormasPago(models.Model):
    id_forma_pago = models.BigAutoField(primary_key=True)
    nombre = models.TextField(max_length=100)
    descripcion = models.TextField(max_length=100)

    class Meta:
        managed = False
        db_table = 'formas_pago'
    
    def __str__(self):
        return str(self.id_forma_pago)+" - "+ self.nombre