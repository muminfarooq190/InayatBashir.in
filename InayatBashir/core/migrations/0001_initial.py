# Generated by Django 3.2.6 on 2021-08-20 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=2000)),
                ('image_one', models.ImageField(upload_to='')),
                ('image_two', models.ImageField(upload_to='')),
                ('published_on', models.DateTimeField(auto_now=True)),
                ('is_in_top_three', models.BooleanField(default=False)),
                ('is_top_one', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_one', models.ImageField(upload_to='')),
                ('image_two', models.ImageField(upload_to='')),
                ('description_one', models.CharField(max_length=1000)),
                ('description_two', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.city')),
            ],
        ),
    ]
