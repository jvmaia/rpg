from django.shortcuts import render
from .models import Room

def index(request):
    if not request.user.is_authenticated:
        return render(request, "chat/login_e.html")

    rooms = Room.objects.order_by("title")

    return render(request, "chat/rooms.html", {
        "rooms": rooms,
    })
