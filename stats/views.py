from re import A
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings

from .models import Battle, Vehicle
from .forms import MatchForm, VehicleForm


def index(request):
    matches = Battle.objects.all().select_related('vehicles')
    paginator = Paginator(matches, settings.PAGINATION_PAGE_SIZE)
    page = paginator.get_page(request.GET.get('page'))

    return render (
        request,
        'index.html',
        {
            'page': page,
            'paginator': paginator
        }
    )


def add_match(request):
    form = MatchForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        match = form.save()
        return redirect(reverse('match_view', match_id=match.id))

    return render(request, 'matches/add_match.html', {'form': form})


def match_view(request, match_id):
    match = get_object_or_404(Battle, match_id=match_id)
    return render(request, 'matches/match_view.html', {'match': match})


def add_vehicle(request):
    form = VehicleForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        vehicle = form.save()
        return redirect(reverse('vehicle_view', slug=vehicle.slug))

    return render(request, 'vehicles/add_vehicle.html', {'form': form})


def vehicle_view(request, vehicle):
    vehicle = get_object_or_404(Vehicle, slug=vehicle)
    return render(request, 'vehicle/vehicle_view.html', {'match': vehicle})


def vehicles(request):
    vehicles = Vehicle.objects.all()
    paginator = Paginator(vehicles, settings.PAGINATION_PAGE_SIZE)
    page = paginator.get_page(request.GET.get('page'))

    return render (
        request,
        'index.html',
        {
            'page': page,
            'paginator': paginator
        }
    )
