from django.db import models

# Create your models here.
class Paciente(models.Model):
    MASCULINO = 'Masculino'
    FEMENINO = 'femenino'
    OTRO = 'Otro'
    SEXO_CHOICES = [
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'femenino'),
        (OTRO, 'Otro')
    ]
     
    id_paciente = models.BigAutoField(primary_key=True)
    nombre = models.TextField()
    apellidos = models.TextField()
    telefono = models.TextField( )
    correo = models.TextField()
    sexo = models.TextField(max_length=10,
        choices=SEXO_CHOICES,
        default=OTRO)
    
    fecha_nacimiento = models.DateField()
    localizacion = models.TextField()

    class Meta:
        managed = False
        db_table = 'pacientes'
    def __str__(self):
            return str(self.id_paciente)+" - "+ self.nombre +" "+ self.apellidos