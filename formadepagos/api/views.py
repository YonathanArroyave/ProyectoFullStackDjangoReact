from rest_framework.viewsets import ModelViewSet
from formadepagos.models import FormasPago
from formadepagos.api.serializers import FormaDePagoSerializers
from permisosAPI.permissions import IsAdminReadOnly
#from formadepagos.api.permissions import IsAdminReadOnly


class  FormaDePagoApiViewSet(ModelViewSet):
    permission_classes=[IsAdminReadOnly]
    serializer_class= FormaDePagoSerializers
    queryset = FormasPago.objects.all()
    