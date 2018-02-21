from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Char, Map
from django.contrib.auth.decorators import login_required

@login_required(login_url='login/')
def dashboard_master(request):
    maps = Map.objects.all()
    chars = Char.objects.all()
    return render(request, 'game/dashboard_master.html', {'maps': maps, 'chars': chars})

@login_required(login_url='login/')
def dashboard_player(request):
    try:
        char = Char.objects.get(name=request.COOKIES['char'])
        items = list(char.bag.values())
        skills = char.getAvailableSkills()
        partners = Char.objects.all().exclude(name=request.COOKIES['char'])
        return render(request, 'game/dashboard_player.html', {'char': char, 'skills': skills, 'partners': partners, 'items':items})
    except (Char.DoesNotExist, KeyError):
        chars = Char.objects.all()
        return render(request, 'game/select_char.html', {'chars': chars})

def main_page(request):
    return render(request, 'game/main_page.html')

def char_levelup(request, char_id):
    char = get_object_or_404(Char, pk=char_id)
    char.level += 1
    char.save()
    return HttpResponse("Char %s arrived to a new level" % (char_id))
