# Generated by Django 3.2.6 on 2021-08-21 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_places_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='is_in_top_four',
            field=models.BooleanField(default=False),
        ),
    ]