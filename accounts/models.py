from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from django.templatetags.static import static
from accounts.validators import names_validator, telephone_number_validator


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
        upload_to='profile_pics',

    )

    telephone_number = models.CharField(
        blank=True,
        null=True,
        validators=[telephone_number_validator]
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    def get_full_name(self):

        names = [self.first_name, self.last_name]
        names = [name for name in names if name is not None]

        return ' '.join(names)

    class Meta:
        verbose_name = 'Hive User'
        verbose_name_plural = 'Hive Users'