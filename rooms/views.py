from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from . import models


class HomeView(ListView):

    """ HomeView Class Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 3
    context_object_name = "rooms"

    # context를 custom 할 수 있다
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        now = timezone.now()

        context["now"] = now

        return context


def room_detail(request, pk):

    try:

        room = models.Room.objects.get(pk=pk)

        return render(request, "rooms/detail.html", {"room": room})

    except models.Room.DoesNotExist:

        return redirect(reverse("core:home"))

