from rest_framework import status
from rest_framework.reverse import reverse

from products.serializers import ProductSerializer
from utils.tests import CustomTestCase
from utils.tests.creators import create_test_product

list_url = 'product-list'
detail_url = 'product-detail'


class ProductListViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.url = reverse(list_url)

    def test_view_is_allowed(self):
        response = self.client.get(self.url)

        self.assertStatusCodeEqual(response, status.HTTP_200_OK)

    def test_view_returns_correct_data(self):
        products = [create_test_product() for i in range(3)]
        expected_data = ProductSerializer(products, many=True, context=self.get_fake_context()).data

        response = self.client.get(self.url)

        self.assertEqual(response.data, expected_data)

    def test_view_returns_data_of_only_displayed_products(self):
        displayed_products = create_test_product()
        not_displayed_products = create_test_product(is_displayed=False)  # noqa

        expected_data = ProductSerializer([displayed_products], many=True, context=self.get_fake_context()).data

        response = self.client.get(self.url)

        self.assertEqual(response.data, expected_data)


class ProductRetrieveViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.product = create_test_product()
        self.url = reverse(detail_url, args=[self.product.uuid])

    def test_view_is_allowed(self):
        response = self.client.get(self.url)

        self.assertStatusCodeEqual(response, status.HTTP_200_OK)

    def test_view_returns_correct_data(self):
        expected_data = ProductSerializer(self.product, context=self.get_fake_context()).data

        response = self.client.get(self.url)

        self.assertEqual(response.data, expected_data)

    def test_view_view_returns_data_only_displayed_product(self):
        self.product.is_displayed = False
        self.product.save()

        response = self.client.get(self.url)

        self.assertStatusCodeEqual(response, status.HTTP_404_NOT_FOUND)
