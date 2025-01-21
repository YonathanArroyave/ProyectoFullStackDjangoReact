from rest_framework import serializers
from pacientes.models import Paciente

class PacientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields=['id_paciente','nombre','apellidos', 'telefono', 'correo', 'sexo', 'fecha_nacimiento', 'localizacion']
        