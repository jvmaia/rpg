from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class PlayerManager(BaseUserManager):
    def create_user(self, username, master, password=None, is_active=True, is_staff=False, is_admin=False):
        if not username:
            raise ValueError('Users must have an username')
        if not password:
            raise ValueError('Users must have a password')
        if not master:
            raise ValueError('Master need be defined')
        user_obj = self.model(username=username)
        user_obj.set_password(password)
        user_obj.master = master
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, username, master=True, password=None):
        user = self.create_user(
            username=username,
            password=password,
            master=master,
            is_staff=True
        )
        return user

    def create_superuser(self, username, master=True, password=None):
        user = self.create_user(
            username=username,
            password=password,
            master=master,
            is_staff=True,
            is_admin=True
        )
        return user

class PlayerUser(AbstractBaseUser):
    username = models.CharField(max_length=25, unique=True)
    master = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = []

    objects = PlayerManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
