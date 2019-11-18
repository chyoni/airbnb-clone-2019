from django.shortcuts import render
from datetime import datetime

# Create your views here.


def all_rooms(request):

    now = datetime.now()
    hungry = True

    return render(request, "all_rooms.html", context={"now": now, "hungry": hungry})
