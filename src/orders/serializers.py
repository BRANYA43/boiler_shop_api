import re

from rest_framework import serializers

from orders.models import Order, OrderProduct, Customer
from orders.validators import PHONE_PATTERN


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['uuid', 'order', 'full_name', 'email', 'phone']
        read_only_fields = ['uuid']

    def validate_phone(self, phone):
        if phone and (match := re.match(PHONE_PATTERN, phone)) is not None:
            phone = '+38 ({}) {} {}-{}'.format(*match.groups()[1:])
        return phone


class OrderProductSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField(method_name='get_price_value')

    class Meta:
        model = OrderProduct
        fields = ['uuid', 'order', 'product', 'quantity', 'price', 'total_cost']
        read_only_fields = ['uuid', 'price', 'price_value']

    @staticmethod
    def get_price_value(obj):
        return 0 if obj.price is None else obj.price.value


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'uuid',
            'status',
            'payment',
            'is_paid',
            'delivery',
            'delivery_address',
            'total_cost',
            'customer',
            'products',
            'updated',
            'created',
        ]
        read_only_fields = ['uuid', 'products', 'customer', 'updated', 'created']
