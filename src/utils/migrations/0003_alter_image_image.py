# Generated by Django 4.2.7 on 2024-01-16 17:36

from django.db import migrations, models

import utils.utils


class Migration(migrations.Migration):
    dependencies = [
        ('utils', '0002_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=utils.utils.get_upload_filename),
        ),
    ]