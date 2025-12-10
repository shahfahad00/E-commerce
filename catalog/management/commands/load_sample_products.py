from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Load sample products with images'

    def handle(self, *args, **options):
        self.stdout.write('Loading sample products...')
        
        # Create categories
        electronics, _ = Category.objects.get_or_create(
            name='Electronics',
            defaults={
                'slug': 'electronics',
                'description': 'Electronic gadgets and devices'
            }
        )
        
        clothing, _ = Category.objects.get_or_create(
            name='Clothing',
            defaults={
                'slug': 'clothing',
                'description': 'Fashion and apparel'
            }
        )
        
        books, _ = Category.objects.get_or_create(
            name='Books',
            defaults={
                'slug': 'books',
                'description': 'Books and literature'
            }
        )
        
        # Sample products with image URLs (using placeholder images)
        products = [
            {
                'name': 'Wireless Headphones',
                'slug': 'wireless-headphones',
                'description': 'High-quality wireless headphones with noise cancellation',
                'price': 99.99,
                'category': electronics,
                'stock': 50,
                'image_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500'
            },
            {
                'name': 'Smartphone',
                'slug': 'smartphone',
                'description': 'Latest model smartphone with advanced features',
                'price': 699.99,
                'category': electronics,
                'stock': 30,
                'image_url': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500'
            },
            {
                'name': 'Laptop',
                'slug': 'laptop',
                'description': 'Powerful laptop for work and gaming',
                'price': 1299.99,
                'category': electronics,
                'stock': 20,
                'image_url': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500'
            },
            {
                'name': 'T-Shirt',
                'slug': 't-shirt',
                'description': 'Comfortable cotton t-shirt',
                'price': 19.99,
                'category': clothing,
                'stock': 100,
                'image_url': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=500'
            },
            {
                'name': 'Jeans',
                'slug': 'jeans',
                'description': 'Classic blue jeans',
                'price': 49.99,
                'category': clothing,
                'stock': 75,
                'image_url': 'https://images.unsplash.com/photo-1542272604-787c3835535d?w=500'
            },
            {
                'name': 'Python Programming Book',
                'slug': 'python-programming-book',
                'description': 'Learn Python programming from scratch',
                'price': 29.99,
                'category': books,
                'stock': 40,
                'image_url': 'https://images.unsplash.com/photo-1589998059171-988d887df646?w=500'
            },
        ]
        
        created_count = 0
        for product_data in products:
            product, created = Product.objects.get_or_create(
                slug=product_data['slug'],
                defaults=product_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created product: {product.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Product already exists: {product.name}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'\nSuccessfully loaded {created_count} new products!')
        )
