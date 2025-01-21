from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminReadOnly(BasePermission):
    """
    Permite acceso según los permisos y autenticación del usuario:
    - GET (y otros métodos seguros): cualquier usuario autenticado.
    - POST, PUT, PATCH: cualquier usuario autenticado.
    - DELETE: Solo usuarios con permisos de staff.
    """
    def has_permission(self, request, view):
        # Permitir métodos seguros (GET, HEAD, OPTIONS) a cualquier usuario autenticado
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        # Permitir POST, PUT, PATCH solo a usuarios autenticados
        if request.method in ['POST', 'PUT', 'PATCH']:
            return request.user.is_authenticated

        # Permitir DELETE solo a usuarios administradores
        if request.method == 'DELETE':
            return request.user.is_staff

        # Negar cualquier otro método
        return False
