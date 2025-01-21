from rest_framework import serializers
from medidas.models import Medida


class MedidasSerializers(serializers.ModelSerializer):
    class Meta:
        model= Medida
        fields=['id_medida', 'id_consulta', 'peso', 'talla', 'sub_escapular', 'tricep', 'supra_espinal', 'abdo', 'muslo_anterior', 'pierna_medial', 'brazo_relajado', 'cintura', 'cadera', 'muslo_medial', 'pierna']
        
   