from django.contrib.auth import models as auth_models

from django.db import models

from firstProject.accounts.managers import FirstProjectUserManager


class FirstProjectUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 25

    email = models.EmailField(
        unique=True
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'

    objects = FirstProjectUserManager()


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30
    CHOICES_MAX_LENGTH = 6

    MALE = 'MALE'
    FEMALE = 'FEMALE'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        # null=True,
        # blank=True
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        # null=True,
        # blank=True
    )

    gender = models.CharField(
        max_length=CHOICES_MAX_LENGTH,
        choices=GENDER_CHOICES
    )

    # image = models.URLField(
    #     # null=True,
    #     # blank=True
    # )

    user = models.OneToOneField(
        FirstProjectUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
