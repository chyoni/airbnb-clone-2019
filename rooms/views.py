from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from rooms import models as room_models

# Create your views here.


def all_rooms(request):

    page = request.GET.get("page", 1)

    # 이건 데이터베이스에서 데이터를 가져오는 것이 아니라 쿼리문을 생성한 것 뿐
    all_rooms = room_models.Room.objects.all()

    # 이렇게 all_rooms를 호출하여야만 데이터베이스에서 데이터를 뽑아옴
    # Django QuerySet is Lazy ! OK?
    paginator = Paginator(all_rooms, 10, orphans=3)

    try:

        contacts = paginator.page(int(page))

        return render(request, "rooms/home.html", context={"contacts": contacts},)

    except EmptyPage:

        return redirect("/")
