from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from accounts.validators import telephone_number_validator, validate_name_is_alpha, validate_name_starts_with_upper


class HiveUser(AbstractUser):

    MIN_NAMES_LENGTH = MinLengthValidator(2)
    DEFAULT_MAX_LENGTH = 30

    email = models.EmailField(
        blank=False,
        null=False,
        unique=True
    )

    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=DEFAULT_MAX_LENGTH,
        validators=[
            MIN_NAMES_LENGTH,
            validate_name_is_alpha,
            validate_name_starts_with_upper
        ]
    )

    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=DEFAULT_MAX_LENGTH,
        validators=[
            MIN_NAMES_LENGTH,
            validate_name_is_alpha,
            validate_name_starts_with_upper
        ]
    )

    profile_picture = models.ImageField(
        blank=True,
        null=True,
        upload_to='profile_pics',

    )

    telephone_number = models.CharField(
        blank=True,
        null=True,
        validators=[
            telephone_number_validator
        ]
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