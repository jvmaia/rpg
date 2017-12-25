from django.shortcuts import render
from django.http import HttpResponse
from .models import Char
from django.contrib.auth.decorators import login_required

# TODO create custom authentication_form for our custom user model

@login_required(login_url='login/')
def dashboard_master(request):
	return render(request, 'game/dashboard_master.html')

@login_required(login_url='login/')
def dashboard_player(request):
	try:
		char = Char.objects.get(name=request.COOKIES['char'])
		return render(request, 'game/dashboard_player.html', {'char': char})
	except (Char.DoesNotExist, KeyError):
		all_chars = Char.objects.all()
		return render(request, 'game/select_char.html', {'chars': all_chars})

def main_page(request):
    return render(request, 'game/main_page.html')
