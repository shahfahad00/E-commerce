import pytest
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Category, Product


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Electronics',
            slug='electronics',
            description='Electronic devices and gadgets'
        )

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Electronics')

    def test_category_get_absolute_url(self):
        expected_url = reverse('catalog:category_detail', kwargs={'slug': 'electronics'})
        self.assertEqual(self.category.get_absolute_url(), expected_url)


class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Electronics',
            slug='electronics'
        )
        self.product = Product.objects.create(
            name='Smartphone',
            slug='smartphone',
            description='A high-quality smartphone',
            price=699.99,
            category=self.category,
            stock=10,
            available=True
        )

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Smartphone')

    def test_product_get_absolute_url(self):
        expected_url = reverse('catalog:product_detail', kwargs={'slug': 'smartphone'})
        self.assertEqual(self.product.get_absolute_url(), expected_url)

    def test_product_available_default(self):
        self.assertTrue(self.product.available)


class ProductViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            name='Electronics',
            slug='electronics'
        )
        self.product = Product.objects.create(
            name='Smartphone',
            slug='smartphone',
            description='A high-quality smartphone',
            price=699.99,
            category=self.category,
            stock=10,
            available=True
        )

    def test_product_list_view(self):
        response = self.client.get(reverse('catalog:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Smartphone')

    def test_product_detail_view(self):
        response = self.client.get(reverse('catalog:product_detail', kwargs={'slug': 'smartphone'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Smartphone')
        self.assertContains(response, '$699.99')

    def test_api_product_list(self):
        response = self.client.get(reverse('catalog:api_product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('application/json', response['Content-Type'])


@pytest.mark.django_db
class TestProductAPI:
    def test_api_product_detail(self):
        client = Client()
        category = Category.objects.create(name='Test Category', slug='test-category')
        product = Product.objects.create(
            name='Test Product',
            slug='test-product',
            description='Test Description',
            price=99.99,
            category=category,
            stock=5,
            available=True
        )

        response = client.get(reverse('catalog:api_product_detail', kwargs={'slug': 'test-product'}))
        assert response.status_code == 200
        assert 'Test Product' in str(response.content)
