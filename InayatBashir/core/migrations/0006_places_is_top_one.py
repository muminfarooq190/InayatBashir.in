# Generated by Django 3.2.6 on 2021-08-23 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_places_is_in_top_four'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='is_top_one',
            field=models.BooleanField(default=False),
        ),
    ]