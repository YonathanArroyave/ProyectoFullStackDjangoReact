from rest_framework.viewsets import ModelViewSet
from consultas.models import Consulta
from consultas.api.serializers import ConsultasSerializers
from permisosAPI.permissions import IsAdminReadOnly


class ConsultasApiViewSet(ModelViewSet):
    permission_classes=[IsAdminReadOnly]
    serializer_class= ConsultasSerializers
    queryset = Consulta.objects.all()