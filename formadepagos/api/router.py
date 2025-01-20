from rest_framework.routers import    DefaultRouter
from formadepagos.api.views import FormaDePagoApiViewSet

router_FormaDePago= DefaultRouter()
router_FormaDePago.register(prefix='formadepagos', basename='formas_pago', viewset= FormaDePagoApiViewSet)

