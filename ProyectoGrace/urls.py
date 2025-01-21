"""
URL configuration for ProyectoGrace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view #documentacion API
from drf_yasg import openapi #documentacion API
#importaciones de api propias
from formadepagos.api.router import router_FormaDePago
from        sedes.api.router import router_Sedes

schema_view = get_schema_view(#propio de la documentacion de la api
   openapi.Info(
      title="Proyecto Control Grace API",
      default_version='v1',
      description="Test description proyecto Nutricionista Grace",
      terms_of_service="",
      contact=openapi.Contact(email=""),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   #permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
    path('api/', include('users.api.router')),
    path('api/', include(router_FormaDePago.urls)),
    path('api/', include(router_Sedes.urls)),
]
