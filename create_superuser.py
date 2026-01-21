import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import User

# Superuser details
USERNAME = 'admin'
EMAIL = 'admin@example.com'
PASSWORD = 'admin123'

try:
    user = User.objects.get(username=USERNAME)
    # Update password if needed
    user.set_password(PASSWORD)
    user.is_superuser = True
    user.is_staff = True
    user.is_active = True
    user.email = EMAIL
    user.save()
    print(f"Superuser '{USERNAME}' already existed, password and permissions updated.")
except User.DoesNotExist:
    # Create new superuser
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print(f"Superuser '{USERNAME}' created successfully!")
