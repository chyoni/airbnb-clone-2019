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

    country = request.GET.get("country")

    if country:

        form = forms.SearchForm(request.GET)

        if form.is_valid():

            city = form.cleaned_data.get("city")
            country = form.cleaned_data.get("country")
            room_type = form.cleaned_data.get("room_type")
            price = form.cleaned_data.get("price")
            guests = form.cleaned_data.get("guests")
            bedrooms = form.cleaned_data.get("bedrooms")
            beds = form.cleaned_data.get("beds")
            baths = form.cleaned_data.get("baths")
            instant_book = form.cleaned_data.get("instant_book")
            superhost = form.cleaned_data.get("superhost")
            amenities = form.cleaned_data.get("amenities")
            facilities = form.cleaned_data.get("facilities")

            filter_args = {}

            if city != "Anywhere":
                filter_args["city__startswith"] = city

            filter_args["country"] = country

            if room_type is not None:
                filter_args["room_type"] = room_type

            if price is not None:
                filter_args["price__lte"] = price

            if guests is not None:
                filter_args["guests__gte"] = guests

            if bedrooms is not None:
                filter_args["bedrooms__gte"] = bedrooms

            if beds is not None:
                filter_args["ged__gte"] = beds

            if baths is not None:
                filter_args["baths__gte"] = baths

            if instant_book is True:
                filter_args["instant_book"] = True

            if superhost is True:
                filter_args["host__superhost"] = True

            if len(amenities) > 0:
                filter_args["amenities__in"] = list(amenities)

            if len(facilities) > 0:
                filter_args["facilities__in"] = list(facilities)

            rooms = models.Room.objects.filter(**filter_args).distinct()

            return render(request, "rooms/search.html", {"form": form, "rooms": rooms})
    else:

        form = forms.SearchForm()

        return render(request, "rooms/search.html", {"form": form})

