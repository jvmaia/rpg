from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from .models import Char, Map, Object, Weapon, Weapons_family
from django.contrib.auth.decorators import login_required


@login_required(login_url='login/')
def dashboard_master(request):
    maps = Map.objects.all()
    chars = Char.objects.all().order_by('-level')
    objects = Object.objects.all()
    weapons = list(Weapon.objects.all().order_by('-damage').values())
    for weapon in weapons:
        weapon['family_name'] = Weapons_family.objects.get(
            id=weapon['family_id']
        )

    return render(request, 'game/dashboard_master.html', {
        'maps': maps,
        'chars': chars,
        'objects': objects,
        'weapons': weapons
    })


@login_required(login_url='login/')
def dashboard_player(request):
    try:
        char = Char.objects.get(name=request.COOKIES['char'])
    except (Char.DoesNotExist, KeyError):
        chars = Char.objects.all()
        return render(request, 'game/select_char.html', {'chars': chars})

    maps = Map.objects.all()
    items = list(char.bag.values())
    weapons = list(char.weapons.values())
    for weapon in weapons:
        weapon['family_name'] = Weapons_family.objects.get(
            id=weapon['family_id']
        )

    skills = char.getAvailableSkills()
    chars = Char.objects.all()
    return render(request, 'game/dashboard_player.html', {
        'char': char,
        'skills': skills,
        'chars': chars,
        'items': items,
        'weapons': weapons,
        'maps': maps
    })


def main_page(request):
    return render(request, 'game/main_page.html')


def char_profile(request, char_name):
    try:
        char = Char.objects.get(slug=char_name)
    except:
        return JsonResponse({
            'message': 'Char not found'
        })

    weapons = list(char.weapons.values())
    for weapon in weapons:
        weapon['family_name'] = Weapons_family.objects.get(
            id=weapon['family_id']
        )

    items = list(char.bag.values())
    skills = char.getAvailableSkills()

    return render(request, 'game/char_profile.html', {
        'char': char,
        'items': items,
        'weapons': weapons,
        'skills': skills
    })


def char_levelup(request, char_id):
    char = get_object_or_404(Char, pk=char_id)
    char.level += 1
    char.save()
    return JsonResponse({
        'message': 'Char %s arrived to a new level' % (char.name)
    })


def char_applyDamage(request, char_name, difference):
    try:
        char = Char.objects.get(slug=char_name)
    except:
        return JsonResponse({
            'message': 'Char not found'
        })

    try:
        difference = int(difference)
    except:
        return JsonResponse({
            'message': 'Invalid number'
        })

    if difference > 0 and char.actual_life + difference > char.life:
        char.actual_life = char.life
    elif char.actual_life + difference < 0:
        char.actual_life = 0
    else:
        char.actual_life += difference

    char.save()
    return JsonResponse({
        'message': "Char %s new life: %i" % (char.name, char.actual_life)
    })


def char_giveItem(request, char_name, item_name):
    try:
        char = Char.objects.get(slug=char_name)
    except:
        return JsonResponse({
            'message': 'Char not found'
        })

    try:
        item = Object.objects.get(slug=item_name)
    except:
        try:
            item = Weapon.objects.get(slug=item_name)
        except:
            return JsonResponse({
                'message': 'Item not found'
            })

    if isinstance(item, Object):
        char.bag.add(item)
    else:
        char.weapons.add(item)

    return JsonResponse({
        'message': 'Char %s received the item %s' % (char.name, item.name)
    })


def item_transfer(request, source_char, target_char, item_name):
    if source_char == target_char:
        return JsonResponse({
            'message': 'You cannot transfer an item to yourself'
        })

    try:
        source_char = Char.objects.get(slug=source_char)
        target_char = Char.objects.get(slug=target_char)
    except:
        return JsonResponse({
            'message': 'Char not found'
        })

    try:
        item = Object.objects.get(slug=item_name)
    except:
        try:
            item = Weapon.objects.get(slug=item_name)
        except:
            return JsonResponse({
                'message': 'Item not found'
            })

    if {'slug': item.slug} in source_char.bag.values('slug'):
        source_char.bag.remove(item)
        target_char.bag.add(item)
    elif {'slug': item.slug} in source_char.weapons.values('slug'):
        source_char.weapons.remove(item)
        target_char.weapons.add(item)
    else:
        return JsonResposne({
            'message': "Source char doesn't have this item"
        })

    return JsonResponse({
        'message': 'Char %s transferred the item %s to the char %s' %
        (source_char.name, item.name, target_char.name)
    })
