# Generated by Django 3.2.6 on 2021-09-23 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_blog_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='image_four',
            field=models.ImageField(blank=True, upload_to='places'),
        ),
        migrations.AddField(
            model_name='places',
            name='image_three',
            field=models.ImageField(blank=True, upload_to='places'),
        ),
        migrations.AlterField(
            model_name='places',
            name='image_two',
            field=models.ImageField(blank=True, upload_to='places'),
        ),
    ]