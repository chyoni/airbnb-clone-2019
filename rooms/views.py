from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.shortcuts import render
from . import forms
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


class RoomDetail(DetailView):

    model = models.Room

    # 이거 안해도 DetailView 는 기본으로 argument를 pk로 받음
    pk_url_kwarg = "pk"


def search(request):

    form = forms.SearchForm()

    return render(request, "rooms/search.html", {"form": form})
