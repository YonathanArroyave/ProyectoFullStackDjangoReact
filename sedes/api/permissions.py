from rest_framework.permissions import BasePermission


class IsAdminReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Permitir registro (POST) a cualquier usuario autenticado
        if request.method == 'POST' or request.method == 'PUT':
            return request.user.is_authenticated 
    
        if request.method == 'DELETE':
            return request.user.is_staff 
        
        # Permitir otras acciones (GET, etc.) solo a usuarios autenticados
        return request.user.is_authenticated 



         # Permitir solo usuarios autenticados y miembros del staff para usar la API
        #if request.user.is_authenticated:
        #if request.method == 'DELETE':
                #return request.user.is_staff  # Solo staff puede borrar
            #return True  # Permitir otros métodos si está autenticado
        #return False

        