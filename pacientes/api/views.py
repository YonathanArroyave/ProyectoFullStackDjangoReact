from rest_framework.viewsets import ModelViewSet
from pacientes.models import Paciente
from pacientes.api.serializers import PacientesSerializers
#from formadepagos.api.permissions import IsAdminReadOnly


class  PacientessApiViewSet(ModelViewSet):
    #permission_classes=[IsAdminReadOnly]
    serializer_class= PacientesSerializers
    queryset = Paciente.objects.all()
    