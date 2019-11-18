from django.shortcuts import render
from rooms import models as room_models

# Create your views here.


def all_rooms(request):

    all_rooms = room_models.Room.objects.all()

    return render(request, "rooms/home.html", context={"rooms": all_rooms})
