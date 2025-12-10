from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')

        # Create categories
        electronics = Category.objects.get_or_create(
            name='Electronics',
            slug='electronics',
            defaults={'description': 'Electronic devices and gadgets'}
        )[0]

        clothing = Category.objects.get_or_create(
            name='Clothing',
            slug='clothing',
            defaults={'description': 'Fashion and apparel'}
        )[0]

        books = Category.objects.get_or_create(
            name='Books',
            slug='books',
            defaults={'description': 'Books and literature'}
        )[0]

        # Create products
        products_data = [
            {
                'name': 'Smartphone Pro',
                'slug': 'smartphone-pro',
                'description': 'Latest smartphone with advanced features, high-resolution camera, and long battery life.',
                'price': 699.99,
                'category': electronics,
                'stock': 25
            },
            {
                'name': 'Wireless Headphones',
                'slug': 'wireless-headphones',
                'description': 'Premium wireless headphones with noise cancellation and superior sound quality.',
                'price': 199.99,
                'category': electronics,
                'stock': 15
            },
            {
                'name': 'Laptop Computer',
                'slug': 'laptop-computer',
                'description': 'High-performance laptop perfect for work and gaming with fast processor and graphics.',
                'price': 1299.99,
                'category': electronics,
                'stock': 8
            },
            {
                'name': 'Cotton T-Shirt',
                'slug': 'cotton-t-shirt',
                'description': 'Comfortable 100% cotton t-shirt available in various colors and sizes.',
                'price': 29.99,
                'category': clothing,
                'stock': 50
            },
            {
                'name': 'Denim Jeans',
                'slug': 'denim-jeans',
                'description': 'Classic denim jeans with perfect fit and premium quality fabric.',
                'price': 79.99,
                'category': clothing,
                'stock': 30
            },
            {
                'name': 'Programming Guide',
                'slug': 'programming-guide',
                'description': 'Comprehensive guide to modern programming languages and best practices.',
                'price': 49.99,
                'category': books,
                'stock': 20
            },
            {
                'name': 'Science Fiction Novel',
                'slug': 'science-fiction-novel',
                'description': 'Bestselling science fiction novel that will transport you to another world.',
                'price': 24.99,
                'category': books,
                'stock': 35
            }
        ]

        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                slug=product_data['slug'],
                defaults=product_data
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')
            else:
                self.stdout.write(f'Product already exists: {product.name}')

        # Create admin user if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            self.stdout.write('Created admin user (username: admin, password: admin123)')

        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))