from rest_framework import serializers
from sedes.models import Sede

class SedeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields=['id_sede','nombre','descripcion']
        