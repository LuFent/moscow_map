# Generated by Django 2.2 on 2022-04-02 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20220402_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='number',
            field=models.IntegerField(null=True, verbose_name='Номер картинки'),
        ),
    ]
