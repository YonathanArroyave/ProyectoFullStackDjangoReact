from django.db import models
from pacientes.models import Paciente
from sedes.models import Sede
from formadepagos.models import FormasPago

# Create your models here.
class Consulta(models.Model):
    PRESENCIAL = 'Presencial'
    VIRTUAL = 'Virtual'
    TIPOCONSULTA_CHOICES = [
        (PRESENCIAL, 'Presencial'),
        (VIRTUAL, 'Virtual')
    ]
    id_consulta = models.BigAutoField(primary_key=True)
    fecha = models.DateTimeField()
    notas_consulta = models.TextField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True, db_column='id_paciente')
    envio_plan = models.BooleanField(blank=True, null=True, default=False)
    id_sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, null=True, db_column='id_sede')
    id_forma_pago = models.ForeignKey(FormasPago, on_delete=models.SET_NULL, null=True, db_column='id_forma_pago')
    nombrePaciente = Paciente.nombre
    tipo_consulta = models.TextField(max_length=10,
        choices=TIPOCONSULTA_CHOICES,
        default=PRESENCIAL)

    class Meta:
        managed = False
        db_table = 'consultas'
    
    def __str__(self):
        # Formatear la fecha a un formato legible
        fecha_formateada = self.fecha.strftime("%d-%m-%Y %H:%M")
        return f"{self.id_paciente.nombre} {self.id_paciente.apellidos} - {fecha_formateada}"
