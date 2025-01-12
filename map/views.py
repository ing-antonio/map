from django.shortcuts import render
from .models import Location
import folium
from folium.plugins import FastMarkerCluster

def home(request):
    # Recupero todas las sucursales
    locations = Location.objects.all()

    # Defino el mapa
    initialMap = folium.Map(location=[19.432657077087686,-99.13332201502041], zoom_start=5)

    # Creamos el Clustering de los marcadores
    latitudes = [location.lat for location in locations]
    longitudes = [location.lng for location in locations]
    popups = [location.name for location in locations]

    print(latitudes)
    print(longitudes)
    print(list(zip(latitudes, longitudes, popups)))

    FastMarkerCluster(data=list(zip(latitudes, longitudes, popups))).add_to(initialMap)

    # Creamos los marcadores
    # for location in locations:
    #     coordinates = (location.lat, location.lng)
    #     folium.Marker(coordinates, popup='Sucursal ' + location.name).add_to(initialMap)

    context = {'map':initialMap._repr_html_(), 'locations':locations}
    return render(request, 'map/home.html', context)
