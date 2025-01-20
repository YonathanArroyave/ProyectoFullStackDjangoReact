from rest_framework import serializers
from formadepagos.models import FormasPago

class FormaDePagoSerializers(serializers.ModelSerializer):
    class Meta:
        model = FormasPago
        fields=['id_forma_pago','nombre','descripcion']
        