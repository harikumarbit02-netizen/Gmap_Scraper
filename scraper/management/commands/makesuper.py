from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User = get_user_model()

        username = os.getenv("hari")
        password = os.getenv("Hari@1234")
        email = os.getenv("vharikumar.art@gmail.com")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write("Superuser created.")
        else:
            self.stdout.write("Superuser already exists.")
