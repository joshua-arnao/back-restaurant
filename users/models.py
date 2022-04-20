from django.db import models
# AbstractBaseUser => modifica todo el modelo auth_user desde cero
# AbstractUser => Permite agregar nuevas columnas de las que ya estaban creadas incialmente
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from users.authManager import UserManager
from django.utils import timezone

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45, null=False)
    first_name = models.CharField(max_length=45, null=False)
    last_name = models.CharField(max_length=45, null=False)
    date_joined = models.DateTimeField(default=timezone.now)

    email = models.EmailField(unique=True, null=False)
    password = models.TextField(null=False)
    name = models.CharField(max_length=45, null=False)
    rol = models.CharField(choices=(
        # con la cual se usara en la bd y se mostrara | la que se usara para los formularios
        ['ADMINISTRADOR', 'ADMINISTRADOR'],
        ['MOZO', 'MOZO']), max_length=40)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_actived = models.BooleanField(default=True)

    createAt = models.DateTimeField(auto_now_add=True, db_column='created_at')

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name', 'username', 'rol']

    class Meta:
        db_table = 'users'
