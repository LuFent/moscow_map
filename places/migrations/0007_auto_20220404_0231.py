# Generated by Django 2.2 on 2022-04-03 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_place_placeid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='img',
            new_name='url',
        ),
        migrations.RemoveField(
            model_name='place',
            name='placeId',
        ),
        migrations.AddField(
            model_name='place',
            name='place_id',
            field=models.CharField(blank=True, max_length=25, verbose_name='ID места'),
        ),
    ]
