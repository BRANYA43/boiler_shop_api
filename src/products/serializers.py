from rest_framework import serializers

from products.models import Category, Product, ProductImageSet, Specification


class ProductImageSetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductImageSet
        fields = ['url', 'uuid', 'product', 'images']
        read_only_fields = ['uuid']


class SpecificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Specification
        fields = ['url', 'uuid', 'product', 'attributes']
        read_only_fields = ['uuid']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    price = serializers.SerializerMethodField(method_name='get_decimal_price')

    class Meta:
        model = Product
        fields = [
            'url',
            'uuid',
            'category',
            'name',
            'slug',
            'price',
            'stock',
            'description',
            'is_displayed',
            'specification',
            'image_set',
            'updated',
            'created',
        ]
        read_only_fields = ['uuid', 'updated', 'created']

    @staticmethod
    def get_decimal_price(obj):
        return obj.price.price


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'uuid', 'name', 'parent', 'subs']
        read_only_fields = ['uuid']
