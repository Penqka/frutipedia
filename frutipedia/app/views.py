from django.http import HttpResponse
from django.shortcuts import render, redirect

from frutipedia.app.forms import ProfileCreateForm, FruitCreateForm, FruitEditForm, FruitDeleteForm, ProfileEditForm
from frutipedia.app.models import Fruit
from frutipedia.helpers.retriev_data import get_profile, get_all_fruits, get_fruit_from_pk


def index(request):
    context = {
        'profile': get_profile()
    }

    return render(request, 'common/index.html', context)


def dashboard(request):
    context = {
        'profile': get_profile(),
        'fruits': get_all_fruits(),
    }
    return render(request, 'common/dashboard.html', context)


def fruit_create(request):
    if request.method == 'GET':
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'profile': get_profile(),
        'form': form,
    }
    return render(request, 'fruit/create-fruit.html', context)


def fruit_details(request, fruitId):
    fruit = get_fruit_from_pk(fruitId)

    context = {
        'profile': get_profile(),
        'fruit': fruit,

    }

    return render(request, 'fruit/details-fruit.html', context)


def fruit_edit(request, fruitId):
    fruit = get_fruit_from_pk(fruitId)

    if request.method == 'GET':
        form = FruitEditForm(instance=fruit)
    else:
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()

            return redirect('dashboard page')

    context = {
        'profile': get_profile(),
        'form': form,
        'fruit': fruit,
    }
    return render(request, 'fruit/edit-fruit.html', context)


def fruit_delete(request, fruitId):
    fruit = get_fruit_from_pk(fruitId)
    if request.method == 'GET':
        form = FruitDeleteForm(instance=fruit)
    else:
        form = FruitDeleteForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            fruit.delete()

            return redirect('dashboard page')

    context = {
        'profile': get_profile(),
        'form': form,
        'fruit': fruit,
    }

    return render(request, 'fruit/delete-fruit.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('dashboard page')

    context = {
        'profile': get_profile(),
        'form': form
    }

    return render(request, 'profile/create-profile.html', context)


def profile_details(request):


    context = {
        'profile': get_profile(),
        'posts': Fruit.objects.all().count()
    }

    return render(request, 'profile/details-profile.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details page')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()
    fruits = get_all_fruits()
    if request.method == 'POST':
        profile.delete()
        if fruits:
            fruits.delete()

        return redirect('home page')

    context = {
        'profile': profile,
    }

    return render(request, 'profile/delete-profile.html', context)
