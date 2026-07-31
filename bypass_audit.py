import os
import django
from rest_framework.test import APIClient

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from Resources.models import User

def audit():
    client = APIClient()
    
    # Create test user without subscriptions
    user, created = User.objects.get_or_create(username='audit_user_api', email='auditapi@example.com')
    if created:
        user.set_password('password')
        user.save()
    
    # Authenticate properly for DRF
    client.force_authenticate(user=user)

    print(f"Testing API access for authenticated user {user.username} (No Subscription)")

    endpoints_to_test = [
        ('/api/curriculum/lessons/', "Lessons API"),
        ('/api/curriculum/simulations/', "Simulations API"),
        ('/api/curriculum/lesson-blocks/', "Lesson Blocks API"),
        ('/questions/quizzes/', "Quizzes API"),
    ]

    failed = False
    for url, name in endpoints_to_test:
        response = client.get(url)
        print(f"{name} ({url}) -> Status: {response.status_code}")
        
        # We expect 403 Forbidden since HasActiveSubscription should block them.
        if response.status_code == 200:
            print(f"  [!] VULNERABILITY FOUND: {name} is accessible without subscription.")
            failed = True
        elif response.status_code == 403:
            print(f"  [+] SECURE: {name} correctly blocked with 403.")
        else:
            print(f"  [?] Unexpected status: {response.status_code}. Content: {response.content}")

    if failed:
        print("\nAudit Failed: Commercial bypass vulnerabilities exist.")
    else:
        print("\nAudit Passed: All tested premium endpoints are secure against direct API bypass.")

if __name__ == '__main__':
    audit()
