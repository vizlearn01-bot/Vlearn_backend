from django.db import models
import hashlib
import secrets
from django.utils import timezone
from datetime import timedelta


class OTPVerification(models.Model):
    """Stores OTP verification codes for phone-based authentication."""
    PURPOSE_REGISTRATION = 'registration'
    PURPOSE_LOGIN = 'login'
    PURPOSE_PASSWORD_RESET = 'password_reset'
    PURPOSE_CHOICES = [
        (PURPOSE_REGISTRATION, 'Registration'),
        (PURPOSE_LOGIN, 'Login'),
        (PURPOSE_PASSWORD_RESET, 'Password Reset'),
    ]

    phone_number = models.CharField(max_length=20, db_index=True)
    otp_hash = models.CharField(max_length=64, help_text="SHA-256 hash of the OTP code")
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_verified = models.BooleanField(default=False)
    attempts_count = models.PositiveIntegerField(default=0)
    verification_token = models.CharField(max_length=64, null=True, blank=True, unique=True,
                                          help_text="Token returned after successful verification")

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['phone_number', 'purpose', 'is_verified']),
        ]

    def __str__(self):
        return f"OTP for {self.phone_number} ({self.purpose})"

    @staticmethod
    def hash_otp(code):
        return hashlib.sha256(code.encode()).hexdigest()

    def is_expired(self):
        return timezone.now() > self.expires_at

    def verify(self, code):
        """Verify the OTP code. Returns True if valid."""
        if self.is_expired():
            return False
        if self.is_verified:
            return False
        if self.attempts_count >= 5:
            return False
        self.attempts_count += 1
        if self.otp_hash == self.hash_otp(code):
            self.is_verified = True
            self.verification_token = secrets.token_hex(32)
            self.save()
            return True
        self.save()
        return False
