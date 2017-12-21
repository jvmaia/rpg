from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# TODO create custom authentication_form for our custom user model

@login_required(login_url='login/')
def dashboard(request):
	return HttpResponse('<a href="/dash/logout">Logout</a>')
