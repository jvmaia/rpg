from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# TODO create custom authentication_form for our custom user model

@login_required(login_url='login/')
def dashboard_master(request):
	return render(request, "game/dashboard_master.html")

@login_required(login_url='login/')
def dashboard_player(request):
    return render(request, "game/dashboard_player.html")

def main_page(request):
    return render(request, "game/main_page.html")
