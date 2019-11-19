from django.shortcuts import render
from django.core.paginator import Paginator
from rooms import models as room_models

# Create your views here.


def all_rooms(request):

    page = request.GET.get("page", 1)

    page = int(page or 1)

    if page == 0:
        page = 1

    # 이건 데이터베이스에서 데이터를 가져오는 것이 아니라 쿼리문을 생성한 것 뿐
    all_rooms = room_models.Room.objects.all()

    paginator = Paginator(all_rooms, 10)
    contacts = paginator.get_page(page)

    return render(request, "rooms/home.html", context={"contacts": contacts},)
