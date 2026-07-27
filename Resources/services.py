import secrets, hashlib, logging
from datetime import timedelta
from django.utils import timezone
from .models import User, PasswordResetToken
from rest_framework_simplejwt.tokens import RefreshToken

def generate_token():
    """Returns (raw_token, hashed_token). Store only the hash."""
    raw = secrets.token_urlsafe(32)
    hashed = hashlib.sha256(raw.encode()).hexdigest()
    return raw, hashed

class AuthService:
    @staticmethod
    def register_user(validated_data, role=''):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            role=role,
            account_state=User.ACCOUNT_ACTIVE
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    @staticmethod
    def authenticate_user(username, password):
        from django.contrib.auth import authenticate
        user = authenticate(username=username, password=password)
        if user:
            if not user.is_active:
                return None
            return AuthService.get_tokens_for_user(user)
        return None

    @staticmethod
    def logout(refresh_token_str):
        try:
            token = RefreshToken(refresh_token_str)
            token.blacklist()
            return True
        except Exception:
            return False

    @staticmethod
    def request_password_reset(email):
        user = User.objects.filter(email=email).first()
        if not user:
            logging.info(f"Password reset requested for unknown email: {email}")
            return None, None
        
        raw, hashed = generate_token()
        expires_at = timezone.now() + timedelta(hours=24)
        reset_token_obj = PasswordResetToken.objects.create(
            user=user, token_hash=hashed, expires_at=expires_at
        )
        logging.info(f"Password reset token for {email}: {raw}")
        return raw, reset_token_obj

    @staticmethod
    def blacklist_user_tokens(user):
        try:
            from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
            tokens = OutstandingToken.objects.filter(user=user)
            for token in tokens:
                BlacklistedToken.objects.get_or_create(token=token)
        except Exception as e:
            logging.error(f"Failed to blacklist tokens for user {user.id}: {str(e)}")

    @staticmethod
    def reset_password(raw_token, new_password):
        hashed = hashlib.sha256(raw_token.encode()).hexdigest()
        reset_token_obj = PasswordResetToken.objects.filter(token_hash=hashed).first()
        if not reset_token_obj or reset_token_obj.is_used or reset_token_obj.expires_at < timezone.now():
            return False
        
        user = reset_token_obj.user
        user.set_password(new_password)
        user.save()
        
        AuthService.blacklist_user_tokens(user)
        
        reset_token_obj.is_used = True
        reset_token_obj.save()
        return True

    @staticmethod
    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)
        refresh['role'] = getattr(user, 'role', '')
        refresh['organization_id'] = getattr(user, 'organization_id', None)
        refresh['user_id'] = user.id

        access = refresh.access_token
        access['role'] = getattr(user, 'role', '')
        access['organization_id'] = getattr(user, 'organization_id', None)
        access['user_id'] = user.id

        return {
            "refresh": str(refresh),
            "access": str(access),
            "role": getattr(user, 'role', ''),
            "organization_id": getattr(user, 'organization_id', None),
            "user_id": user.id,
        }

    @staticmethod
    def create_invitation(email, role, organization_id, created_by):
        from .models import Invitation
        raw, hashed = generate_token()
        expires_at = timezone.now() + timedelta(days=7)
        invitation = Invitation.objects.create(
            email=email,
            role=role,
            organization_id=organization_id,
            token_hash=hashed,
            created_by=created_by,
            expires_at=expires_at
        )
        return raw, invitation

    @staticmethod
    def validate_invitation(raw_token):
        from .models import Invitation
        hashed = hashlib.sha256(raw_token.encode()).hexdigest()
        invitation = Invitation.objects.filter(token_hash=hashed, state='pending').first()
        if not invitation or invitation.expires_at < timezone.now():
            return None
        return invitation

    @staticmethod
    def accept_invitation(raw_token, user_data):
        from .models import Invitation
        from django.db import transaction

        hashed = hashlib.sha256(raw_token.encode()).hexdigest()
        
        with transaction.atomic():
            invitation = Invitation.objects.select_for_update().filter(
                token_hash=hashed, state='pending'
            ).first()
            
            if not invitation or invitation.expires_at < timezone.now():
                return None
                
            user = User(
                username=user_data['username'],
                email=invitation.email,
                first_name=user_data.get('first_name', ''),
                last_name=user_data.get('last_name', ''),
                role=invitation.role,
                organization_id=invitation.organization_id,
                account_state=User.ACCOUNT_PENDING
            )
            user.set_password(user_data['password'])
            user.save()
            
            invitation.state = 'accepted'
            invitation.accepted_by = user
            invitation.save()
            
            return AuthService.get_tokens_for_user(user)
