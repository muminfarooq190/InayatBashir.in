# Generated by Django 3.2.6 on 2021-08-20 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210820_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='core.city'),
        ),
    ]
