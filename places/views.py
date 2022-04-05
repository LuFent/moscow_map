from django.http import HttpResponse, JsonResponse
from django.template import loader
import os
from .models import Place, Image
import pprint
from django.shortcuts import get_object_or_404
from django.urls import reverse


def serialize_place(place):
    serialized_place = \
     {
        "type": "Feature",
        "geometry": {
                    "type": "Point",
                    "coordinates": [place.lat, place.lng]
                    },

        "properties": {
                    "title": place.title,
                    "placeId": place.place_id,
                    "detailsUrl": reverse("place_json", kwargs={'place_id': place.place_id})
                     }
     }

    return serialized_place


def main_page(request):
    template = loader.get_template('index.html')

    places = Place.objects.all()

    places_geojson = {
        "type": "FeatureCollection",

        "features": [serialize_place(place) for place in places]
    }

    context = {
        'all_places': places_geojson,
    }
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def place_json(request, place_id):
    place = get_object_or_404(Place, place_id=place_id)
    place_data = {
                    "title": place.title,
                    "imgs": [str(image.image.url) for image in place.imgs.all()],
                    "description_short": place.short_description,
                    "description_long": place.long_description,
                    "coordinates": {
                    "lng": place.lng,
                    "lat": place.lat
                    }
                }

    return JsonResponse(place_data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})

