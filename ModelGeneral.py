#se crea con python manage.py inspectdb >ModelGeneral.py
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class Consultas(models.Model):
    id_consulta = models.BigAutoField(primary_key=True)
    fecha = models.DateTimeField()
    notas_consulta = models.TextField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    id_paciente = models.ForeignKey('Pacientes', models.DO_NOTHING, db_column='id_paciente', blank=True, null=True)
    envio_plan = models.BooleanField(blank=True, null=True)
    id_sede = models.ForeignKey('Sedes', models.DO_NOTHING, db_column='id_sede', blank=True, null=True)
    id_forma_pago = models.ForeignKey('FormasPago', models.DO_NOTHING, db_column='id_forma_pago', blank=True, null=True)
    tipo_consulta = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consultas'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FormasPago(models.Model):
    id_forma_pago = models.BigAutoField(primary_key=True)
    nombre = models.TextField()
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formas_pago'


class Medidas(models.Model):
    id_medida = models.BigAutoField(primary_key=True)
    id_consulta = models.ForeignKey(Consultas, models.DO_NOTHING, db_column='id_consulta', blank=True, null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    talla = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sub_escapular = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tricep = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    supra_espinal = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    abdo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    muslo_anterior = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pierna_medial = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    brazo_relajado = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cintura = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cadera = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    muslo_medial = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pierna = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medidas'


class Pacientes(models.Model):
    id_paciente = models.BigAutoField(primary_key=True)
    nombre = models.TextField()
    apellidos = models.TextField()
    telefono = models.TextField(blank=True, null=True)
    correo = models.TextField(blank=True, null=True)
    sexo = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    localizacion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pacientes'


class Sedes(models.Model):
    id_sede = models.BigAutoField(primary_key=True)
    nombre = models.TextField()
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sedes'


class UsersUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users_user'


class UsersUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_groups'
        unique_together = (('user', 'group'),)


class UsersUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_user_permissions'
        unique_together = (('user', 'permission'),)
