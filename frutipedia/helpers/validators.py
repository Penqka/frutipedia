from django.core.exceptions import ValidationError


def name_validator(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


def only_letters_validator(value):
    for i in value:
        if not i.isalpha():
            raise ValidationError("Fruit name should contain only letters!")
