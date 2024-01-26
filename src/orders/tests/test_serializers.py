from unittest.mock import patch

from rest_framework.serializers import HyperlinkedModelSerializer

from orders.serializers import OrderSerializer, OrderProductSerializer, CustomerSerializer
from utils.tests import CustomTestCase


class CustomerSerializerTest(CustomTestCase):
    def setUp(self) -> None:
        self.serializer = CustomerSerializer

    def test_serializer_inherit_necessary_classes(self):
        necessary_classes = [HyperlinkedModelSerializer]
        for class_ in necessary_classes:
            self.assertTrue(issubclass(self.serializer, class_))

    def test_serializer_has_only_expected_fields(self):
        expected_fields = ['url', 'uuid', 'order', 'full_name', 'email', 'phone']
        self.assertSerializerHasOnlyExpectedFields(self.serializer, expected_fields)

    def test_uuid_field(self):
        """
        Tests:
        field is read only;
        """
        field = self.get_serializer_field(self.serializer, 'uuid')
        self.assertTrue(field.read_only)

    @patch('rest_framework.serializers.HyperlinkedRelatedField.validate_empty_values', return_value=(True, None))
    def test_serializer_validates_and_formats_phone(self, mock):
        valid_phones = [
            '+380501234567',
            '+38 (050) 123-45-67',
            '+38(050)123-45-67',
            '380501234567',
            '0501234567',
            '050-123-45-67',
            '050 123 45 67',
            '050-1234567',
            '+380501234567',
            '+38 (050) 123-45-67',
            '+38(050)123-45-67',
            '0501234567',
            '050-123-45-67',
            '050 123 45 67',
            '050-1234567',
            '+380501234567',
            '+38 (050) 123-45-67',
            '+38(050)123-45-67',
            '0501234567',
            '050-123-45-67',
            '050 123 45 67',
            '050-1234567',
        ]
        expected_phone = '+38 (050) 123 45-67'

        for phone in valid_phones:
            serializer = self.serializer(data={'phone': phone})
            serializer.is_valid()
            self.assertEqual(serializer.validated_data['phone'], expected_phone)


class OrderProductSerializerTest(CustomTestCase):
    def setUp(self) -> None:
        self.serializer = OrderProductSerializer

    def test_serializer_inherit_necessary_classes(self):
        necessary_classes = [HyperlinkedModelSerializer]
        for class_ in necessary_classes:
            self.assertTrue(issubclass(self.serializer, class_))

    def test_serializer_has_only_expected_fields(self):
        expected_fields = ['url', 'uuid', 'order', 'product', 'quantity', 'price', 'total_cost']
        self.assertSerializerHasOnlyExpectedFields(self.serializer, expected_fields)

    def test_uuid_field(self):
        """
        Tests:
        field is read only;
        """
        field = self.get_serializer_field(self.serializer, 'uuid')
        self.assertTrue(field.read_only)

    def test_total_cost_field(self):
        """
        Test:
        field is read only;
        """
        field = self.get_serializer_field(self.serializer, 'total_cost')
        self.assertTrue(field.read_only)


class OrderSerializerTest(CustomTestCase):
    def setUp(self) -> None:
        self.serializer = OrderSerializer

    def test_serializer_inherit_necessary_classes(self):
        necessary_classes = [HyperlinkedModelSerializer]
        for class_ in necessary_classes:
            self.assertTrue(issubclass(self.serializer, class_))

    def test_serializer_has_only_expected_fields(self):
        expected_fields = [
            'url',
            'uuid',
            'status',
            'payment',
            'is_paid',
            'delivery',
            'delivery_address',
            'total_cost',
            'updated',
            'created',
        ]
        self.assertSerializerHasOnlyExpectedFields(self.serializer, expected_fields)

    def test_uuid_field(self):
        """
        Tests:
        field is read only;
        """
        field = self.get_serializer_field(self.serializer, 'uuid')
        self.assertTrue(field.read_only)

    def test_total_cost_field(self):
        """
        Test:
        field is read only;
        """
        field = self.get_serializer_field(self.serializer, 'total_cost')
        self.assertTrue(field.read_only)