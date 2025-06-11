from django.core.management.base import BaseCommand
from authentication.models import User

class Command(BaseCommand):
    help = 'Create a superuser with custom User model'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(email='admin@healthcare.com').exists():
            User.objects.create_superuser(
                email='admin@healthcare.com',
                name='Admin User',
                password='admin123'
            )
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))