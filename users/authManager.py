from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, name, rol, password):
        if not email:
            raise ValueError(
                'El usaurio debe tener obligatoriamente un correo')
        newUser = self.model(email=email, name=name, rol=rol)
        newUser.set_password(password)

        newUser.save(using=self._db)
        return newUser

    def create_superuser(self, email, name, rol, password):
        user = self.create_user(email, name, rol, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
