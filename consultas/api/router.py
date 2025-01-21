from rest_framework.routers import DefaultRouter
from consultas.api.views import ConsultasApiViewSet

router_Consultas= DefaultRouter()
router_Consultas.register(prefix='consultas', basename='consultas', viewset= ConsultasApiViewSet)
