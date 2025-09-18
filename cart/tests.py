from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Cart, CartItem
from catalog.models import Category, Product


class CartModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.cart = Cart.objects.create(user=self.user)
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        self.product = Product.objects.create(
            name='Test Product',
            slug='test-product',
            description='Test Description',
            price=99.99,
            category=self.category,
            stock=5
        )

    def test_cart_str(self):
        expected = f"Cart for {self.user.username}"
        self.assertEqual(str(self.cart), expected)

    def test_cart_get_total_cost(self):
        CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)
        expected_cost = 99.99 * 2
        self.assertEqual(float(self.cart.get_total_cost()), expected_cost)

    def test_cart_get_total_items(self):
        CartItem.objects.create(cart=self.cart, product=self.product, quantity=3)
        self.assertEqual(self.cart.get_total_items(), 3)


class CartItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.cart = Cart.objects.create(user=self.user)
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        self.product = Product.objects.create(
            name='Test Product',
            slug='test-product',
            description='Test Description',
            price=99.99,
            category=self.category,
            stock=5
        )
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)

    def test_cart_item_str(self):
        expected = f"2 x {self.product.name}"
        self.assertEqual(str(self.cart_item), expected)

    def test_cart_item_get_cost(self):
        expected_cost = 99.99 * 2
        self.assertEqual(float(self.cart_item.get_cost()), expected_cost)
