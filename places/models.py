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
    title = models.CharField('Название места', max_length=70, blank=False)
    short_description = models.TextField('Краткое описание места', blank=True)
    long_description = HTMLField('Полное описание места', blank=True)
    lat = models.FloatField('Широта', null=True, blank=False)
    lng = models.FloatField('Долгота', null=True, blank=False)
    place_id = models.CharField('ID места', max_length=25, blank=False, unique=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    """
        Модель картинки для Place
    """
    image = models.ImageField('Изображение места', null=True, blank=False)
    place = models.ForeignKey(Place,
                              on_delete=models.CASCADE,
                              verbose_name='К какому месту относится',
                              related_name='imgs',
                              default=None,
                              null=True,
                              blank=False)

    number = models.IntegerField('Номер картинки', blank=False, default=0)

    class Meta(object):
        ordering = ['number']

    def preview(self):
        full_url = str(self.image.url)
        return format_html('<img src="{}", width=200, height=200>', full_url)

    def __str__(self):
        return f'{self.number}  img of  {self.place.title}'