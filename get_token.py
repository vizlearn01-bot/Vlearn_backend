import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()
user = User.objects.get(email='jasonbitega@gmail.com')
refresh = RefreshToken.for_user(user)
print(f"ACCESS_TOKEN={str(refresh.access_token)}")
