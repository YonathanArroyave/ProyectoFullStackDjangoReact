from django.db import models

# Create your models here.
class Sede(models.Model):
    id_sede = models.BigAutoField(primary_key=True)
    nombre = models.TextField()
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sedes'
    def __str__(self):
            return str(self.id_sede)+" - "+ self.nombre