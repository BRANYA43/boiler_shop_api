# Generated by Django 4.2.7 on 2024-02-16 19:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]