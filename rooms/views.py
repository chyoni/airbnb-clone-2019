from django.shortcuts import render
from math import ceil
from rooms import models as room_models

# Create your views here.


def all_rooms(request):

    page = request.GET.get("page", 1)

    page = int(page or 1)

    if page == 0:
        page = 1

    room_size = 10

    limit = room_size * page

    offset = limit - room_size

    all_rooms = room_models.Room.objects.all()[offset:limit]

    page_count = ceil(room_models.Room.objects.count() / room_size)

    return render(
        request,
        "rooms/home.html",
        context={
            "rooms": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count + 1),
        },
    )
