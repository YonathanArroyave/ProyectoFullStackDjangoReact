from rest_framework import serializers
from consultas.models import Consulta


class ConsultasSerializers(serializers.ModelSerializer):
    class Meta:
        model= Consulta
        fields=['id_consulta', 'fecha', 'notas_consulta', 'valor', 'id_paciente', 'envio_plan', 'id_sede', 'id_forma_pago', 'tipo_consulta']
        
   