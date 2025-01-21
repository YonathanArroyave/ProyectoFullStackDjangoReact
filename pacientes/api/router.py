from rest_framework.routers import    DefaultRouter
from pacientes.api.views import PacientessApiViewSet

router_Pacientes= DefaultRouter()
router_Pacientes.register(prefix='pacientes', basename='pacientes', viewset= PacientessApiViewSet)

