from rest_framework.routers import    DefaultRouter
from sedes.api.views import SedesApiViewSet

router_Sedes= DefaultRouter()
router_Sedes.register(prefix='sedes', basename='sedes', viewset= SedesApiViewSet)

