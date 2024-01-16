from django.db import models

from utils.mixins import CreatedAndUpdatedDateTimeMixin, UUIDMixin


def _set_grade_dict():
    return {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}


class Specification(UUIDMixin):
    product = models.OneToOneField('Product', on_delete=models.CASCADE, related_name='specification')
    attributes = models.ManyToManyField('Attribute', related_name='specifications')

    def __str__(self):
        return str(self.product)


class Attribute(UUIDMixin):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}: {self.value}'


class Stock(models.TextChoices):
    IN_STOCK = 'in_stock', 'In stock'
    OUT_OF_STOCK = 'out_of_stock', 'Out of stock'
    TO_ORDER = 'to_order', 'To order'


class Product(UUIDMixin, CreatedAndUpdatedDateTimeMixin):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.CharField(max_length=20, choices=Stock.choices, default=Stock.IN_STOCK)
    description = models.TextField(blank=True, null=True)
    is_displayed = models.BooleanField(default=True)
    grade = models.JSONField(default=_set_grade_dict)

    class Meta:
        pass

    def __str__(self):
        return self.name

    @property
    def total_grade(self):
        grade = sum([int(g) * c for g, c in self.grade.items()])
        count = sum(self.grade.values())
        if count != 0:
            return round(grade / count, 2)
        return 0


class Category(UUIDMixin):
    name = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey(
        'self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='sub_categories'
    )

    def __str__(self):
        return self.name

    @property
    def is_sub_category(self):
        if self.parent:
            return True
        return False

    @property
    def is_parent_category(self):
        if self.sub_categories.first():
            return True
        return False
