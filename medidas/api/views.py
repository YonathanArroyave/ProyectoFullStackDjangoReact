from rest_framework.viewsets import ModelViewSet
from medidas.models import Medida
from medidas.api.serializers import MedidasSerializers


class MedidasApiViewSet(ModelViewSet):
    serializer_class= MedidasSerializers
    queryset = Medida.objects.all()