from rest_framework.routers import DefaultRouter
from medidas.api.views import MedidasApiViewSet

router_Medidas= DefaultRouter()
router_Medidas.register(prefix='medidas', basename='medidas', viewset= MedidasApiViewSet)
