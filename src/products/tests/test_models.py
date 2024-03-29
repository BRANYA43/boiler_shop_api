from django.core.exceptions import ValidationError
from django.db.models import ProtectedError

from products.models import Category, Product, ProductImageSet, Specification, Price
from utils.mixins import CreatedAndUpdatedDateTimeMixin, ImageSetMixin, UUIDMixin
from utils.models import Attribute, Image
from utils.tests import CustomTestCase
from utils.tests import creators


class PriceModelTest(CustomTestCase):
    def setUp(self) -> None:
        self.model = Price

    def test_model_inherit_necessary_mixins(self):
        mixins = [UUIDMixin]
        for mixin in mixins:
            self.assertTrue(issubclass(self.model, mixin))

    def test_product_field(self):
        """
        Tests:
        field has relation many ot one;
        field has related_model as Product;
        """
        field = self.get_model_field(self.model, 'product')
        self.assertTrue(field.many_to_one)
        self.assertIs(field.related_model, Product)

    def test_value_field(self):
        """
        Tests:
        field has max digits as 10;
        field has decimal places as 2;
        """
        field = self.get_model_field(self.model, 'value')
        self.assertEqual(field.max_digits, 10)
        self.assertEqual(field.decimal_places, 2)

    def test_created_field(self):
        """
        Tests:
        field sets date only when model is created;
        """
        field = self.get_model_field(self.model, 'created')
        self.assertTrue(field.auto_now_add)

    def test_instance_model_is_deleted_after_deleting_product(self):
        price = creators.create_test_price()
        product = price.product

        self.assertEqual(Price.objects.count(), 1)

        product.delete()

        self.assertEqual(Price.objects.count(), 0)

    def test_model_instance_sets_product_price_after_saving_it(self):
        price = creators.create_test_price(value=1000)
        self.assertEqual(price.product.price, price.value)


class ProductImageSetModelTest(CustomTestCase):
    def setUp(self) -> None:
        self.model = ProductImageSet

    def test_model_inherit_necessary_mixins(self):
        mixins = [ImageSetMixin]
        for mixin in mixins:
            self.assertTrue(issubclass(self.model, mixin))

    def test_product_field(self):
        """
        Tests:
        field has relation one ot one;
        field has related_model as Product;
        """
        field = self.get_model_field(self.model, 'product')
        self.assertTrue(field.one_to_one)
        self.assertIs(field.related_model, Product)

    def test_cover_image_field(self):
        """
        Test:
        field has relation many to one;
        field has related_model as Image;
        field can be null;
        """
        field = self.get_model_field(self.model, 'cover_image')
        self.assertTrue(field.many_to_one)
        self.assertIs(field.related_model, Image)
        self.assertTrue(field.null)

    def test_model_is_protected_from_deleting_cover_image(self):
        image = creators.create_test_image()
        image_set = creators.create_test_product().image_set
        image_set.cover_image = image
        image_set.save()

        with self.assertRaises(ProtectedError):
            image.delete()

    def test_model_is_created_after_creating_product(self):
        self.assertEqual(self.model.objects.count(), 0)

        creators.create_test_product()

        self.assertEqual(self.model.objects.count(), 1)

    def test_model_is_deleted_after_deleting_product(self):
        self.assertEqual(self.model.objects.count(), 0)

        product = creators.create_test_product()

        self.assertEqual(self.model.objects.count(), 1)

        product.delete()

        self.assertEqual(self.model.objects.count(), 0)


class SpecificationModelTest(CustomTestCase):
    def setUp(self) -> None:
        self.model = Specification
        self.attributes = [creators.create_test_attribute() for i in range(10)]

    def test_model_inherit_necessary_mixins(self):
        mixins = [UUIDMixin]
        for mixin in mixins:
            self.assertTrue(issubclass(self.model, mixin))

    def test_model_has_necessary_fields(self):
        necessary_field = ['uuid', 'product', 'all_attributes', 'card_attributes', 'detail_attributes']
        self.assertModelHasNecessaryFields(self.model, necessary_field)

    def test_product_field(self):
        """
        Tests:
        field has relation one ot one;
        field has related model as Product;
        """
        field = self.get_model_field(self.model, 'product')
        self.assertTrue(field.one_to_one)
        self.assertIs(field.related_model, Product)

    def test_all_attributes_field(self):
        """
        Tests:
        field has relation many to many;
        field has related model as Attribute;
        field can be blank;
        """
        field = self.get_model_field(self.model, 'all_attributes')
        self.assertTrue(field.many_to_many)
        self.assertIs(field.related_model, Attribute)
        self.assertTrue(field.blank)

    def test_card_attributes_field(self):
        """
        Tests:
        field has relation many to many;
        field has related model as Attribute;
        field can be blank;
        """
        field = self.get_model_field(self.model, 'card_attributes')
        self.assertTrue(field.many_to_many)
        self.assertIs(field.related_model, Attribute)
        self.assertTrue(field.blank)

    def test_detail_attributes_field(self):
        """
        Tests:
        field has relation many to many;
        field has related model as Attribute;
        field can be blank;
        """
        field = self.get_model_field(self.model, 'detail_attributes')
        self.assertTrue(field.many_to_many)
        self.assertIs(field.related_model, Attribute)
        self.assertTrue(field.blank)

    def test_model_is_created_after_creating_product(self):
        self.assertEqual(Specification.objects.count(), 0)

        creators.create_test_product()

        self.assertEqual(Specification.objects.count(), 1)

    def test_model_is_deleted_after_deleting_product(self):
        self.assertEqual(Specification.objects.count(), 0)

        product = creators.create_test_product()

        self.assertEqual(Specification.objects.count(), 1)

        product.delete()

        self.assertEqual(Specification.objects.count(), 0)

    def test_card_attributes_field_cannot_have_different_attributes_from_attributes_of_all_attributes_field(self):
        specification = creators.create_test_product().specification
        specification.all_attributes.set(self.attributes[:3])
        specification.card_attributes.set(self.attributes[1:4])

        with self.assertRaises(ValidationError):
            specification.full_clean()

    def test_card_attributes_field_cannot_have_more_3_attributes(self):
        specification = creators.create_test_product().specification
        specification.all_attributes.set(self.attributes)
        specification.card_attributes.set(self.attributes[:4])

        with self.assertRaises(ValidationError):
            specification.full_clean()

    def test_detail_attributes_field_cannot_have_different_attributes_from_attributes_of_all_attributes_field(self):
        specification = creators.create_test_product().specification
        specification.all_attributes.set(self.attributes[:5])
        specification.card_attributes.set(self.attributes[1:5])

        with self.assertRaises(ValidationError):
            specification.full_clean()

    def test_detail_attributes_field_cannot_have_more_5_attributes(self):
        specification = creators.create_test_product().specification
        specification.all_attributes.set(self.attributes)
        specification.card_attributes.set(self.attributes[:6])

        with self.assertRaises(ValidationError):
            specification.full_clean()


class ProductModelTest(CustomTestCase):
    def setUp(self) -> None:
        self.model = Product

    def test_model_inherit_necessary_mixins(self):
        mixins = [UUIDMixin, CreatedAndUpdatedDateTimeMixin]
        for mixin in mixins:
            self.assertTrue(issubclass(self.model, mixin))

    def test_model_has_necessary_fields(self):
        necessary_fields = [
            'uuid',
            'name',
            'category',
            'stock',
            'price',
            'description',
            'is_displayed',
            'updated',
            'created',
        ]
        self.assertModelHasNecessaryFields(self.model, necessary_fields)

    def test_name_field(self):
        """
        Tests:
        field has max length as 50;
        """
        field = self.get_model_field(self.model, 'name')
        self.assertEqual(field.max_length, 55)

    def test_category_field(self):
        """
        Tests:
        field has relation many to one;
        field has Category as related model;
        """
        field = self.get_model_field(self.model, 'category')
        self.assertTrue(field.many_to_one)
        self.assertIs(field.related_model, Category)

    def test_stock_field(self):
        """
        Tests:
        field is Stock.IN_STOCK by default;
        field has Stock.choices;
        """
        field = self.get_model_field(self.model, 'stock')
        self.assertEqual(field.default, self.model.Stock.IN_STOCK)
        self.assertEqual(field.choices, self.model.Stock.choices)

    def test_is_displayed_field(self):
        """
        Tests:
        field is true by default;
        """
        field = self.get_model_field(self.model, 'is_displayed')
        self.assertTrue(field.default)

    def test_description_field(self):
        """
        Tests:
        field can be null;
        field can be blank;
        """
        field = self.get_model_field(self.model, 'description')
        self.assertTrue(field.null)
        self.assertTrue(field.blank)

    def test_price_field(self):
        """
        Tests:
        field has max_digits as 10;
        field has decimal_places as 2;
        field is 0 by default;
        """
        field = self.get_model_field(self.model, 'price')
        self.assertEqual(field.max_digits, 10)
        self.assertEqual(field.decimal_places, 2)
        self.assertEqual(field.default, 0)

    def test_state_field(self):
        """
        Tests:
        field has max_length as 20;
        field is State.NONE by default;
        field has State.choices;
        """
        field = self.get_model_field(self.model, 'state')
        self.assertEqual(field.default, self.model.State.NONE)
        self.assertEqual(field.choices, self.model.State.choices)

    def test_model_allows_category_to_be_deleted(self):
        product = creators.create_test_product()
        category = product.category

        with self.assertRaises(ProtectedError):
            category.delete()


class CategoryModelTest(CustomTestCase):
    def setUp(self) -> None:
        self.model = Category

    def test_model_inherit_necessary_mixins(self):
        mixins = [UUIDMixin]
        for mixin in mixins:
            self.assertTrue(issubclass(self.model, mixin))

    def test_model_has_necessary_fields(self):
        necessary_fields = ['uuid', 'name', 'parent']
        self.assertModelHasNecessaryFields(self.model, necessary_fields)

    def test_image_field(self):
        """
        Tests:
        field has relation many to one;
        field has related model as Image;
        field can be null;
        field can be blank;
        """
        field = self.get_model_field(self.model, 'image')
        self.assertTrue(field.many_to_one)
        self.assertIs(field.related_model, Image)
        self.assertTrue(field.null)
        self.assertTrue(field.blank)

    def test_name_field(self):
        """
        Tests:
        field is unique;
        field has max length as 50;
        """
        field = self.get_model_field(self.model, 'name')
        self.assertTrue(field.unique)
        self.assertEqual(field.max_length, 50)

    def test_parent_field(self):
        """
        Tests:
        field has relation many to one;
        field has related model as Category;
        field can be null;
        field can be blank;
        field is None by default;
        """
        field = self.get_model_field(self.model, 'parent')
        self.assertTrue(field.many_to_one)
        self.assertIs(field.related_model, self.model)
        self.assertTrue(field.null)
        self.assertTrue(field.blank)
        self.assertIsNone(field.default)

    def test_parent_field_is_set_as_null_if_parent_category_is_deleted(self):
        parent = Category.objects.create(name='parent')
        child = Category.objects.create(name='child', parent=parent)

        self.assertIsNotNone(child.parent)

        parent.delete()
        child.refresh_from_db()

        self.assertIsNone(child.parent)

    def test_is_child_category_property_is_true_if_parent_is_not_none(self):
        parent = Category.objects.create(name='parent')
        child = Category.objects.create(name='child', parent=parent)

        self.assertIsNotNone(child.parent)
        self.assertTrue(child.is_child_category)

    def test_is_child_category_property_is_false_if_parent_is_none(self):
        child = Category.objects.create(name='child')

        self.assertIsNone(child.parent)
        self.assertFalse(child.is_child_category)

    def test_is_parent_category_property_is_true_if_sub_categories_are_not_none(self):
        parent = Category.objects.create(name='parent')
        child = Category.objects.create(name='child', parent=parent)  # noqa

        self.assertIsNotNone(parent.children.first())
        self.assertTrue(parent.is_parent_category)

    def test_is_parent_category_property_is_false_if_sub_categories_are_none(self):
        parent = Category.objects.create(name='parent')

        self.assertIsNone(parent.children.first())
        self.assertFalse(parent.is_parent_category)

    def test_model_is_protected_from_deleting_image(self):
        image = creators.create_test_image()
        creators.create_test_category(image=image)

        with self.assertRaises(ProtectedError):
            image.delete()
