# Generated by Django 3.1 on 2022-04-11 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0017_auto_20220411_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default=None, upload_to='', verbose_name='Изображение места'),
        ),
        migrations.AlterField(
            model_name='image',
            name='place',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='imgs', to='places.place', verbose_name='К какому месту относится'),
        ),
    ]
