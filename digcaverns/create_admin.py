import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digcaverns.settings')
django.setup()

def create_user():
    """Create user if doesn't exists using env variables"""
    User = get_user_model()
    username = os.getenv('DJANGO_SUPERUSER_USERNAME')
    email = os.getenv('DJANGO_SUPERUSER_EMAIL')
    password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

    if User.objects.filter(username=username).exists():
        print("Super user already exists.")
    else:
        User.objects.create_superuser(username, email, password)
        print("Super user was created.")


if __name__ == "__main__":
    create_user()

