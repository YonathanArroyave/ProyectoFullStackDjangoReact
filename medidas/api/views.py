from rest_framework.viewsets import ModelViewSet
from medidas.models import Medida
from medidas.api.serializers import MedidasSerializers
from permisosAPI.permissions import IsAdminReadOnly


class MedidasApiViewSet(ModelViewSet):
    permission_classes=[IsAdminReadOnly]
    serializer_class= MedidasSerializers
    queryset = Medida.objects.all()