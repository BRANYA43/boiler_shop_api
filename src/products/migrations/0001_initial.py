# Generated by Django 4.2.7 on 2024-02-16 21:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Title')),
                (
                    'image',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='categories',
                        to='utils.image',
                        verbose_name='Image',
                    ),
                ),
                (
                    'parent',
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='children',
                        to='products.category',
                        verbose_name='Parent Category',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('name', models.CharField(max_length=55, verbose_name='Title')),
                (
                    'stock',
                    models.CharField(
                        choices=[('in_stock', 'In stock'), ('out_of_stock', 'Out of stock'), ('to_order', 'To order')],
                        default='in_stock',
                        max_length=20,
                        verbose_name='Stock',
                    ),
                ),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('is_displayed', models.BooleanField(default=True, verbose_name='Is Displayed')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Price')),
                (
                    'category',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='products',
                        to='products.category',
                        verbose_name='Category',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                (
                    'all_attributes',
                    models.ManyToManyField(
                        blank=True,
                        related_name='specifications',
                        to='utils.attribute',
                        verbose_name='All Characteristics',
                    ),
                ),
                (
                    'card_attributes',
                    models.ManyToManyField(
                        blank=True,
                        related_name='_card_specifications',
                        to='utils.attribute',
                        verbose_name='Characteristics of Card',
                    ),
                ),
                (
                    'detail_attributes',
                    models.ManyToManyField(
                        blank=True,
                        related_name='_detail_specifications',
                        to='utils.attribute',
                        verbose_name='Characteristic of Detail Page',
                    ),
                ),
                (
                    'product',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='specification',
                        to='products.product',
                        verbose_name='Product',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Specification',
                'verbose_name_plural': 'Specifications',
            },
        ),
        migrations.CreateModel(
            name='ProductImageSet',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                (
                    'cover_image',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='_image_set',
                        to='utils.image',
                        verbose_name='Cover Image',
                    ),
                ),
                ('images', models.ManyToManyField(blank=True, to='utils.image', verbose_name='Images')),
                (
                    'product',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='image_set',
                        to='products.product',
                        verbose_name='Image Set',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Product Image Set',
                'verbose_name_plural': 'Product Image Sets',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Value')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                (
                    'product',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='prices',
                        to='products.product',
                        verbose_name='Product',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Price',
                'verbose_name_plural': 'Prices',
            },
        ),
    ]
