# Generated by Django 3.2.6 on 2021-09-22 09:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_places_is_top_one'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='description',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image_two',
        ),
        migrations.AddField(
            model_name='blog',
            name='body',
            field=ckeditor.fields.RichTextField(default='hello'),
        ),
    ]
