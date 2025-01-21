from rest_framework.viewsets import ModelViewSet
from sedes.models import Sede
from sedes.api.serializers import SedeSerializers
#from formadepagos.api.permissions import IsAdminReadOnly


class  SedesApiViewSet(ModelViewSet):
    #permission_classes=[IsAdminReadOnly]
    serializer_class= SedeSerializers
    queryset = Sede.objects.all()
    