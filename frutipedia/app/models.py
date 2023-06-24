from django.core.validators import MinLengthValidator
from django.db import models

from frutipedia.helpers.validators import name_validator, only_letters_validator


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 25
    FIRST_NAME_MIN_LEN = 2

    LAST_NAME_MAX_LEN = 35
    LAST_NAME_MIN_LEN = 1

    PASS_MAX_LEN = 20
    PASS_MIN_LEN = 8

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            name_validator,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            name_validator,
        )
    )

    email = models.EmailField(
        max_length=40,
    )

    password = models.CharField(
        max_length=PASS_MAX_LEN,
        validators=(
            MinLengthValidator(PASS_MIN_LEN),
        )
    )

    image = models.URLField(
        blank=True,
        null=True,
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=18,
    )


class Fruit(models.Model):
    MAX_NAME_LEN = 30
    MIN_NAME_LEN = 2

    name = models.CharField(
        max_length=MAX_NAME_LEN,
        validators=(
            MinLengthValidator(MIN_NAME_LEN),
            only_letters_validator,
        )
    )

    image = models.URLField()

    description = models.TextField()

    nutrition = models.TextField(
        blank=True,
        null=True,
    )
