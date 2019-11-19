from django.shortcuts import render
from rooms import models as room_models

# Create your views here.


def all_rooms(request):

    print(request.GET.get("page"))
    page = int(request.GET.get("page", 1))

    if page == 0:
        page = 1
    room_size = 10
    limit = room_size * page
    offset = limit - room_size

    all_rooms = room_models.Room.objects.all()[offset:limit]

    return render(request, "rooms/home.html", context={"rooms": all_rooms})
