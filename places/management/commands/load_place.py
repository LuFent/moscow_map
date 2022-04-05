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
        if response.ok:
            place_data = response.json()
            place, creation_status = Place.objects.get_or_create(
                title=place_data['title'],
                short_description=place_data['description_short'],
                long_description=place_data['description_long'],
                lat=place_data['coordinates']["lng"],
                lng=place_data['coordinates']["lat"]
            )
            place.place_id = str(place.id)
            place.save()

            if creation_status:
                for num, img_link in enumerate(place_data['imgs']):
                    image_name = img_link.split('/')[-1]
                    image_file = ContentFile(requests.get(img_link).content)

                    image_obj, creation_status = Image.objects.get_or_create(
                        place=place,
                        number=num
                    )
                    image_obj.image.save(image_name, image_file, save=True)

                self.stdout.write(self.style.SUCCESS('Place added'))

            else:
                self.stdout.write(self.style.ERROR('Cannot add this images'))
        else:
            self.stdout.write(self.style.ERROR('Cannot register this place'))




    def handle(self, *args, **kwargs):
        self.add_place(kwargs['place_json'])

