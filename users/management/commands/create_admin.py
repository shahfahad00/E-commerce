from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create a default admin user for production deployment'

    def handle(self, *args, **options):
        User = get_user_model()

        # Check if admin user already exists
        if User.objects.filter(username='admin').exists():
            self.stdout.write(
                self.style.WARNING('Admin user already exists!')
            )
            return

        # Create admin user
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created admin user: {admin_user.username}'
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                'Login credentials - Username: admin, Password: admin123'
            )
        )