from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

from accounts.validators import names_validator, telephone_number_validator


#   not yet migrated

class HiveUser(AbstractUser):

    MIN_NAMES_LENGTH = MinLengthValidator(2)

    email = models.EmailField(
        blank=False,
        null=False,
        unique=True
    )

    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        validators=[MIN_NAMES_LENGTH, names_validator]
    )

    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        validators=[MIN_NAMES_LENGTH, names_validator]
    )

    profile_picture = models.ImageField(
        blank=True,
        null=True,
        upload_to='profile_pics'
    )

    telephone_number = models.CharField(
        blank=True,
        null=True,
        validators=[telephone_number_validator]
    )