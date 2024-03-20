# Generated by Django 4.2.7 on 2024-03-20 14:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='state',
            field=models.CharField(
                choices=[('none', '---'), ('new', 'New'), ('bestseller', 'Bestseller')],
                default='none',
                max_length=20,
                verbose_name='State',
            ),
        ),
    ]
