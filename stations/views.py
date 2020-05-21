from django.shortcuts import render, get_object_or_404

from .models import Station
from core.cities.models import City

def index(request):
    stations = Station.objects.all()

    return render(request, 'radiomamba/index.html', {'stations': stations})

def detail(request, station_id):
    station = get_object_or_404(Station, pk=station_id)
    
    return render(request, 'radiomamba/detail.html', {'station': station})

def create(request):
    city = City.objects.get(name=request.POST['city'])

    station = Station.objects.create(
        name=request.POST['name'],
        stream_url=request.POST['url'],
        city_id=city.id
    )
    
    return index(request)

def form(request):
    cities = City.objects.all()
    
    return render(request, 'radiomamba/form.html', {'cities': cities})
    
def delete(request, station_id):
    station = Station.objects.get(pk=station_id)
    station.delete()
    
    return index(request)