from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("hari", "vharikumar.art@gmail.com.com", "Hari@1234")
    print("Superuser created.")
else:
    print("Superuser already exists.")
