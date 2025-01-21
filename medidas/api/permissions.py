from rest_framework.permissions import BasePermission

class IsAdminReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST' or request.method == 'PUT':
            return request.user.is_authenticated 
        if request.method == 'DELETE':
            return request.user.is_staff 
        return request.user.is_authenticated 