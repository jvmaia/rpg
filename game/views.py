from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Char, Map, Object, Weapon
from django.contrib.auth.decorators import login_required


@login_required(login_url='login/')
def dashboard_master(request):
    maps = Map.objects.all()
    chars = Char.objects.all().order_by('-level')
    objects = Object.objects.all()
    weapons = Weapon.objects.all().order_by('-damage')
    return render(request, 'game/dashboard_master.html', {
        'maps': maps,
        'chars': chars,
        'objects': objects,
        'weapons': weapons
    })


@login_required(login_url='login/')
def dashboard_player(request):
    try:
        maps = Map.objects.all()
        char = Char.objects.get(name=request.COOKIES['char'])
        items = list(char.bag.values())
        skills = char.getAvailableSkills()
        characters = Char.objects.all()
        return render(request, 'game/dashboard_player.html', {
            'char': char,
            'skills': skills,
            'characters': characters,
            'items': items,
            'maps': maps
        })
    except (Char.DoesNotExist, KeyError):
        chars = Char.objects.all()
        return render(request, 'game/select_char.html', {'chars': chars})


def main_page(request):
    return render(request, 'game/main_page.html')


def char_backpack(request, char_name):
    try:
        char = Char.objects.get(slug=char_name)
    except:
        return HttpResponse('Char not found')

    weapons = list(char.weapons.values())
    for weapon in weapons:
        family_name = Weapon.objects.get(id=weapon['family_id']).name
        weapon['family_name'] = family_name
    items = list(char.bag.values())

    return render(request, 'game/char_backpack.html', {'char': char, 'items': items, 'weapons': weapons})


def char_levelup(request, char_id):
    char = get_object_or_404(Char, pk=char_id)
    char.level += 1
    char.save()
    return HttpResponse("Char %s arrived to a new level" % (char.name), content_type="text/plain")


def char_applyDamage(request, char_name, damage):
    try:
        char = Char.objects.get(slug=char_name)
    except:
        return HttpResponse('Char not found')

    if char.actual_life < damage:
        char.actual_life = 0
    else:
        char.actual_life -= damage
    char.save()
    return HttpResponse("Char %s new life: %i" % (char.name, char.actual_life), content_type="text/plain")


def char_giveItem(request, char_name, item_name):
    try:
        char = Char.objects.get(slug=char_name)
    except:
        return HttpResponse('Char not found')

    try:
        item = Object.objects.get(slug=item_name)
    except:
        try:
            item = Weapon.objects.get(slug=item_name)
        except:
            return HttpResponse('Item not found')

    if isinstance(item, Object):
        char.bag.add(item)
    else:
        char.weapons.add(item)

    return HttpResponse('Char received a new item')
