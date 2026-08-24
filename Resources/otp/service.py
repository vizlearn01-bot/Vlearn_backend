import secrets
import string
import logging
from django.utils import timezone
from datetime import timedelta
from django.conf import settings
from rest_framework.exceptions import ValidationError
from .models import OTPVerification
from .africastalking_client import AfricasTalkingClient

logger = logging.getLogger(__name__)

class OTPService:
    @staticmethod
    def generate_otp(phone_number, purpose):
        """Generate a 6-digit OTP, store it, and enforce rate limits."""
        # Rate limit check: max 5 per hour
        one_hour_ago = timezone.now() - timedelta(hours=1)
        recent_count = OTPVerification.objects.filter(
            phone_number=phone_number,
            created_at__gte=one_hour_ago
        ).count()
        if recent_count >= 5:
            raise ValidationError("Rate limit exceeded. Please try again later.")

        code = ''.join(secrets.choice(string.digits) for _ in range(6))
        otp_hash = OTPVerification.hash_otp(code)
        
        OTPVerification.objects.create(
            phone_number=phone_number,
            otp_hash=otp_hash,
            purpose=purpose,
            expires_at=timezone.now() + timedelta(minutes=10)
        )
        
        return code

    @staticmethod
    def send_otp(phone_number, code):
        """Send OTP via SMS. In DEBUG mode, only log it."""
        message = f"Your VLearn verification code is: {code}. It expires in 10 minutes."
        
        if getattr(settings, 'DEBUG', False):
            logger.info(f"DEBUG: SMS to {phone_number} -> {message}")
            return True
            
        client = AfricasTalkingClient()
        return client.send_sms(phone_number, message)

    @staticmethod
    def verify_otp(phone_number, code, purpose):
        """Verify the given OTP code."""
        otp = OTPVerification.objects.filter(
            phone_number=phone_number,
            purpose=purpose,
            is_verified=False
        ).order_by('-created_at').first()
        
        if not otp:
            return False, None
            
        if otp.verify(code):
            return True, otp.verification_token
            
        return False, None
