from django.test import TestCase
from .models import CategoryGroup, SubCategory, Product


class TestCategoryModel(TestCase):
    """
    Testing Category Model
    """

    def setUp(self):
        """
        Sets the Category Object with required attributes
        """
        self.category = CategoryGroup.objects.create(
            name="Cases", friendly_name="cases"
        )
        self.subcategory1 = SubCategory.objects.create(name="Full Tower")
        self.subcategory2 = SubCategory.objects.create(name="Midi Tower")
        self.category.sub_categories.add(self.subcategory1)
        self.category.sub_categories.add(self.subcategory2)
        self.expected_str = str(self.category)
        self.friendly_str = str(self.category.friendly_name)

    def test_category_model(self):
        """
        Tests the Category model's attributes
        """
        self.assertEqual(self.category.name, "Cases")
        self.assertEqual(str(self.category), self.expected_str)
        self.assertEqual(
            str(self.category.get_friendly_name()), self.friendly_str
        )
        self.assertEqual(self.category.sub_categories.count(), 2)
        self.assertIn(self.subcategory1, self.category.sub_categories.all())
        self.assertIn(self.subcategory2, self.category.sub_categories.all())


class TestSubCategoryModel(TestCase):
    """
    Testing SubCategory Model
    """

    def setUp(self):
        """
        Sets the SubCategory Object with required attributes
        """
        self.subcategory = SubCategory.objects.create(
            name="Full Tower", friendly_name="full_tower"
        )
        self.expected_str = str(self.subcategory)
        self.friendly_str = str(self.subcategory.friendly_name)

    def test_subcategory_model(self):
        """
        Tests the SubCategory model's attributes
        """
        self.assertEqual(self.subcategory.name, "Full Tower")
        self.assertEqual(str(self.subcategory), self.expected_str)
        self.assertEqual(
            str(self.subcategory.get_friendly_name()), self.friendly_str
        )


class TestProductModel(TestCase):
    """
    Testing Product Model
    """

    def setUp(self):
        """
        Sets the Product Object with required attributes
        """
        self.category = CategoryGroup.objects.create(
            name="Cases", friendly_name="cases"
        )
        self.subcategory = SubCategory.objects.create(
            name="Full Tower", friendly_name="full_tower"
        )
        self.product = Product.objects.create(
            category=self.category,
            sub_category=self.subcategory,
            name="NZXT",
            slug="nzxt",
            features="A new case",
            description="A big case",
            price=100,
            stock_level=1,
            discount=10,
        )
        self.product.sku = self.product.generate_sku()
        self.product.save()
        self.expected_str = str(self.product)

    def test_product_model(self):
        """
        Tests the Product model's attributes
        """
        self.assertEqual(self.product.name, "NZXT")
        self.assertTrue(self.product.sku.startswith("pp-"))
        self.assertEqual(self.product.slug, "nzxt")
        self.assertEqual(self.product.features, "A new case")
        self.assertEqual(self.product.description, "A big case")
        self.assertEqual(self.product.price, 100)
        self.assertEqual(self.product.stock_level, 1)
        self.assertEqual(self.product.discount, 10)
        self.assertEqual(str(self.product), self.expected_str)

    def test_product_save_method(self):
        """
        Tests the save method of the Product model
        """
        self.product.stock_level = 0
        self.product.in_stock = True
        self.product.save()
        self.assertFalse(self.product.in_stock)

        self.product.stock_level = 1
        self.product.has_sale = True
        self.product.save()
        self.assertEqual(self.product.sale_price, 90)
