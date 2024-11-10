from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User
from django.utils.translation import gettext_lazy as _

@admin.register(User)
# Register your models here.
class UserAdmin(BaseUserAdmin):
    pass

admin.site.site_header = _("Mi Panel de Administración")
admin.site.site_title = _("Mi Sitio de Administración")
admin.site.index_title = _("Bienvenido al Panel de Administración")