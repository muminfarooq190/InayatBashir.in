# Generated by Django 3.2.6 on 2021-08-20 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210820_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
