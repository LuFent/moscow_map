from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField

"""
:Place: Модель места на карте
:Image: Модель картинки места 
"""


class Place(models.Model):
    """
        Модель места на карте
    """
    title = models.CharField('Название места', max_length=70, blank=True)
    short_description = models.CharField('Краткое описание места', max_length=350, blank=True)
    long_description = HTMLField('Полное описание места', blank=True)
    lat = models.FloatField('Широта', null=True)
    lng = models.FloatField('Долгота', null=True)
    place_id = models.CharField('ID места', max_length=25, blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    """
        Модель картинки для Place
    """
    image = models.ImageField('Изображение места', null=True, blank=True)
    place = models.ForeignKey(Place,
                              on_delete=models.CASCADE,
                              verbose_name='К какому месту относится',
                              related_name='imgs',
                              default=None)

    number = models.IntegerField('Номер картинки', null=True, blank=False, default=0)

    class Meta(object):
        ordering = ['number']

    def preview(self):
        full_url = str(self.image.url)
        return format_html(f'<img src="{full_url}", width=200, height=200>')

    def __str__(self):
        return f'{self.number}  img of  {self.place.title}'