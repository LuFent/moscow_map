from django.core.management.base import BaseCommand, CommandError
from places.models import Place, Image
import os
import requests
from django.core.files.base import ContentFile


class Command(BaseCommand):

    help = 'Adding place to DB'

    def add_arguments(self, parser):
        parser.add_argument('place_json', type=str)

    def add_place(self, link_to_json):
        response = requests.get(link_to_json.strip())

        try:
            response.raise_for_status()
        except requests.exceptions.ConnectionError:
            self.stdout.write(self.style.ERROR('Cannot register this place'))

        new_place_fields = response.json()

        new_place, creation_status = Place.objects.update_or_create(
            title=new_place_fields['title'],
            lng=new_place_fields['coordinates']["lng"],
            lat=new_place_fields['coordinates']["lat"],
            defaults={'short_description': new_place_fields['description_short'],
                      'long_description': new_place_fields['description_long'],
                      }
        )
        new_place.place_id = str(new_place.id)
        new_place.save()

        if not creation_status:
            self.stdout.write(self.style.ERROR('This place already exists'))
            return

        for num, img_link in enumerate(new_place_fields['imgs']):
            image_name = img_link.split('/')[-1]
            image_file = ContentFile(requests.get(img_link).content)

            image_obj, creation_status = Image.objects.get_or_create(
                place=new_place,
                number=num
            )
            image_obj.image.save(image_name, image_file, save=True)

        self.stdout.write(self.style.SUCCESS('Place added'))

    def handle(self, *args, **kwargs):
        self.add_place(kwargs['place_json'])

