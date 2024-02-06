from rest_framework import status
from rest_framework.reverse import reverse

from orders import serializers
from orders.models import OrderProduct
from utils.tests import CustomTestCase
from utils.tests.creators import create_test_order_product, create_test_product, create_test_order

list_url = 'orderproduct-list'
detail_url = 'orderproduct-detail'


class OrderProductCreateViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.url = reverse(list_url)
        self.data = {'order': self._get_order_url(), 'product': self._get_product_url()}

    def _get_order_url(self):
        order = create_test_order()
        return reverse('order-detail', args=[order.uuid])

    def _get_product_url(self):
        product = create_test_product()
        return reverse('product-detail', args=[product.uuid])

    def test_view_is_allowed(self):
        response = self.client.post(self.url, data=self.data)

        self.assertStatusCodeEqual(response, status.HTTP_201_CREATED)

    def test_view_returns_correct_data(self):
        response = self.client.post(self.url, data=self.data)

        self.assertEqual(OrderProduct.objects.count(), 1)

        expected_data = serializers.OrderProductSerializer(
            OrderProduct.objects.first(), context=self.get_fake_context()
        ).data

        self.assertEqual(response.data, expected_data)


class OrderProductRetrieveViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.order_product = create_test_order_product()
        self.url = reverse(detail_url, args=[self.order_product.uuid])

    def test_view_is_allowed(self):
        response = self.client.get(self.url)

        self.assertStatusCodeEqual(response, status.HTTP_200_OK)

    def test_view_returns_correct_data(self):
        expected_data = serializers.OrderProductSerializer(self.order_product, context=self.get_fake_context()).data
        response = self.client.get(self.url)

        self.assertEqual(response.data, expected_data)