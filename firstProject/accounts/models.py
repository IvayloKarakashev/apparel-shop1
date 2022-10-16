from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User
from django.db import models

from firstProject.accounts.managers import FirstProjectUserManager


class FirstProjectUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 25

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = FirstProjectUserManager()


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
    )

    image = models.URLField()

    user = models.OneToOneField(
        FirstProjectUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
