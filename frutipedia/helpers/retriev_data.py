from frutipedia.app.models import Profile, Fruit

import json


def get_profile():
    profile = Profile.objects.all().first()
    if profile:
        return profile

    return False


def get_all_fruits():
    fruits = Fruit.objects.all()
    if fruits:
        return fruits
    return None


def get_fruit_from_pk(pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    return fruit


# get user and pass for postgres db

