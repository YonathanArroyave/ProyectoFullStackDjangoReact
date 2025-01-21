from rest_framework.viewsets import ModelViewSet
from consultas.models import Consulta
from consultas.api.serializers import ConsultasSerializers


class ConsultasApiViewSet(ModelViewSet):
    serializer_class= ConsultasSerializers
    queryset = Consulta.objects.all()