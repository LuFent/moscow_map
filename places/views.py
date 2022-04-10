from django.http import HttpResponse, JsonResponse
from django.template import loader
import os
from .models import Place
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.shortcuts import render


def serialize_place(place):
    """
        Функция, для создания словаря для шаблона
        :param place: Объект модели Place
        :return: Словарь
    """
    serialized_place = \
     {
        'type': 'Feature',
        "geometry": {
                    'type': 'Point',
                    'coordinates': [place.lng, place.lat,]
                    },

        'properties': {
                    'title': place.title,
                    'placeId': place.place_id,
                    'detailsUrl': reverse('place_json', kwargs={'place_id': place.place_id})
                     }
     }

    return serialized_place


def main_page(request):
    """
        Вьюха для главной страницы
    """
    places = Place.objects.all()

    places_geojson = {
        'type': 'FeatureCollection',
        'features': [serialize_place(place) for place in places]
    }

    context = {
        'all_places': places_geojson,
    }

    return render(request, 'index.html', context)


def place_json(request, place_id):
    """
            API для получения словаря для detailsUrl
            :param place_id: ID места
            :return: Словарь detailsUrl
    """
    required_place = get_object_or_404(Place, place_id=place_id)
    place_data = {
                    'title': required_place.title,
                    'imgs': [str(image.image.url) for image in required_place.imgs.all()],
                    'description_short': required_place.short_description,
                    'description_long': required_place.long_description,
                    'coordinates': {
                    'lng': required_place.lng,
                    'lat': required_place.lat
                    }
                }

    return JsonResponse(place_data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})

