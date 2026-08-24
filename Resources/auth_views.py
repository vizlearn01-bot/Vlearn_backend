import logging
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.conf import settings
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from .otp.service import OTPService
from .otp.models import OTPVerification
from .models import UserProfile

logger = logging.getLogger(__name__)
User = get_user_model()


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {'refresh': str(refresh), 'access': str(refresh.access_token)}


class RequestOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        phone_number = request.data.get('phone_number')
        purpose = request.data.get('purpose')

        if not phone_number or not purpose:
            return Response({'error': 'phone_number and purpose are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if purpose not in dict(OTPVerification.PURPOSE_CHOICES):
            return Response({'error': 'Invalid purpose'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            code = OTPService.generate_otp(phone_number, purpose)
            OTPService.send_otp(phone_number, code)
            
            masked_phone = phone_number[:-4].replace(phone_number[:-4], '*' * len(phone_number[:-4])) + phone_number[-4:] if len(phone_number) > 4 else phone_number
            response_data = {'message': 'OTP sent', 'phone_number': masked_phone}
            
            if getattr(settings, 'DEBUG', False):
                response_data['code'] = code  # Only for testing
                
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        phone_number = request.data.get('phone_number')
        otp_code = request.data.get('otp_code')
        purpose = request.data.get('purpose')

        if not all([phone_number, otp_code, purpose]):
            return Response({'error': 'phone_number, otp_code, and purpose are required'}, status=status.HTTP_400_BAD_REQUEST)

        success, verification_token = OTPService.verify_otp(phone_number, otp_code, purpose)

        if success:
            return Response({
                'verified': True,
                'verification_token': verification_token
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'error': 'Invalid or expired OTP'
            }, status=status.HTTP_400_BAD_REQUEST)


from django.db import transaction
from rest_framework.exceptions import ValidationError
import re
import uuid
from organizations.models import School, OrganizationMembership

SCHOOL_TYPE_MAP = {
    'national school': 'NATIONAL',
    'national': 'NATIONAL',
    'extra county': 'EXTRA_COUNTY',
    'extra county school': 'EXTRA_COUNTY',
    'county school': 'COUNTY',
    'county': 'COUNTY',
    'sub-county school': 'SUB_COUNTY',
    'sub county school': 'SUB_COUNTY',
    'sub-county': 'SUB_COUNTY',
    'sub county': 'SUB_COUNTY',
    'private school': 'PRIVATE',
    'private': 'PRIVATE',
    'international school': 'INTERNATIONAL',
    'international': 'INTERNATIONAL',
    'public': 'COUNTY',
}

CURRICULUM_MAP = {
    'knec (8-4-4)': '8-4-4',
    '8-4-4': '8-4-4',
    'cbc (competency based)': 'CBC',
    'cbc': 'CBC',
    'both': 'BOTH',
    'both cbc and 8-4-4': 'BOTH',
    'igcse / cambridge': '8-4-4',
    'ib (international baccalaureate)': '8-4-4',
}

def generate_school_code(school_name):
    clean_name = re.sub(r'[^A-Za-z]', '', school_name)[:3].upper()
    if len(clean_name) < 3:
        clean_name = "SCH"
    unique_suffix = uuid.uuid4().hex[:4].upper()
    code = f"{clean_name}-{unique_suffix}"
    while School.objects.filter(code=code).exists():
        unique_suffix = uuid.uuid4().hex[:4].upper()
        code = f"{clean_name}-{unique_suffix}"
    return code


class PhoneRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        phone_number = request.data.get('phone_number') or request.data.get('phone')
        verification_token = request.data.get('verification_token')
        password = request.data.get('password')
        admin_name = request.data.get('admin_name') or request.data.get('name') or request.data.get('adminName') or ''
        admin_email = request.data.get('admin_email') or request.data.get('email') or ''
        role = request.data.get('role', User.ROLE_SCHOOL_ADMIN)

        # School metadata
        school_name = request.data.get('school_name') or request.data.get('schoolName') or ''
        school_type = request.data.get('school_type') or request.data.get('schoolType') or 'County School'
        curriculum = request.data.get('curriculum') or 'KNEC (8-4-4)'
        county = request.data.get('county') or ''
        sub_county = request.data.get('sub_county') or request.data.get('subCounty') or ''
        school_phone = request.data.get('school_phone') or request.data.get('phone') or phone_number

        if not all([phone_number, verification_token, password]):
            return Response({'error': 'phone_number, verification_token, and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate verification token
        try:
            otp = OTPVerification.objects.get(
                phone_number=phone_number,
                verification_token=verification_token,
                is_verified=True,
                purpose=OTPVerification.PURPOSE_REGISTRATION
            )
        except OTPVerification.DoesNotExist:
            return Response({'error': 'Invalid or missing verification token. Please verify your phone number.'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(phone_number=phone_number).exists():
            return Response({'error': 'An account with this phone number already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                # 1. Create User
                user = User.objects.create_user(
                    username=phone_number,
                    phone_number=phone_number,
                    password=password,
                    role=role,
                    first_name=admin_name.strip(),
                    email=admin_email.strip()
                )
                
                # 2. Update UserProfile (created by post_save signal)
                UserProfile.objects.filter(user=user).update(
                    phone_number=phone_number,
                    location_county=county,
                    location_subcounty=sub_county
                )

                # 3. If school registration, create School + OrganizationMembership
                school_obj = None
                if school_name or role == User.ROLE_SCHOOL_ADMIN:
                    if not school_name or not school_name.strip():
                        raise ValidationError({'school_name': ['School name is required.']})
                    
                    clean_school_name = school_name.strip()
                    if School.objects.filter(name__iexact=clean_school_name).exists():
                        raise ValidationError({'school_name': [f"A school with the name '{clean_school_name}' is already registered."]})

                    school_code = generate_school_code(clean_school_name)
                    mapped_type = SCHOOL_TYPE_MAP.get(str(school_type).lower().strip(), 'COUNTY')
                    mapped_curr = CURRICULUM_MAP.get(str(curriculum).lower().strip(), 'BOTH')

                    school_obj = School.objects.create(
                        name=clean_school_name,
                        code=school_code,
                        owner=user,
                        completed_by=user,
                        contact_email=admin_email.strip(),
                        phone_number=school_phone or phone_number,
                        school_type=mapped_type,
                        curricula_offered=mapped_curr,
                        location_county=county,
                        location_subcounty=sub_county,
                        setup_status='PROFILE_COMPLETE',
                        onboarding_version=1,
                        is_active=True
                    )

                    # 4. Create OrganizationMembership
                    OrganizationMembership.objects.create(
                        user=user,
                        school=school_obj,
                        role='school_admin',
                        state='ACTIVE',
                        assigned_by=user
                    )

            # Response formatting
            tokens = get_tokens_for_user(user)
            tokens['role'] = user.role
            tokens['user'] = {
                'id': user.id,
                'username': user.username,
                'phone_number': user.phone_number,
                'first_name': user.first_name,
                'email': user.email,
                'role': user.role
            }
            if school_obj:
                tokens['school'] = {
                    'id': school_obj.id,
                    'name': school_obj.name,
                    'code': school_obj.code,
                    'setup_status': school_obj.setup_status
                }

            return Response(tokens, status=status.HTTP_201_CREATED)

        except ValidationError as ve:
            return Response({'error': getattr(ve, 'detail', str(ve))}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error during school registration: {str(e)}", exc_info=True)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



def normalize_phone_variants(phone_str):
    if not phone_str:
        return []
    clean = str(phone_str).strip().replace(' ', '').replace('-', '')
    variants = [clean]
    if clean.startswith('+254'):
        variants.append('0' + clean[4:])
        variants.append(clean[1:])
        variants.append(clean[4:])
    elif clean.startswith('0'):
        variants.append('+254' + clean[1:])
        variants.append('254' + clean[1:])
        variants.append(clean[1:])
    elif clean.startswith('254'):
        variants.append('+' + clean)
        variants.append('0' + clean[3:])
        variants.append(clean[3:])
    return list(set(variants))


class PhoneLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        phone_input = request.data.get('phone_number') or request.data.get('phone')
        password = request.data.get('password')

        if not all([phone_input, password]):
            return Response({'error': 'Phone number and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        variants = normalize_phone_variants(phone_input)
        from django.db.models import Q
        user = User.objects.filter(
            Q(phone_number__in=variants) | Q(username__in=variants) | Q(username=phone_input)
        ).first()

        if not user:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.is_active:
            return Response({'error': 'Account is disabled.'}, status=status.HTTP_403_FORBIDDEN)

        # Authenticate
        user_auth = authenticate(request, username=user.username, password=password)
        if user_auth is None:
            if user.check_password(password):
                user_auth = user
            else:
                return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

        tokens = get_tokens_for_user(user_auth)
        tokens['role'] = user_auth.role
        tokens['user'] = {
            'id': user_auth.id,
            'username': user_auth.username,
            'phone_number': user_auth.phone_number,
            'first_name': user_auth.first_name,
            'last_name': user_auth.last_name,
            'email': user_auth.email,
            'role': user_auth.role,
            'tsc_number': user_auth.tsc_number,
        }
        return Response(tokens, status=status.HTTP_200_OK)


class PhonePasswordResetView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        phone_input = request.data.get('phone_number') or request.data.get('phone')
        otp_code = request.data.get('otp_code')
        new_password = request.data.get('new_password')

        if not all([phone_input, otp_code, new_password]):
            return Response({'error': 'Phone number, OTP code, and new password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        variants = normalize_phone_variants(phone_input)
        
        # Verify against any variant
        verified = False
        for p in variants:
            success, _ = OTPService.verify_otp(p, otp_code, OTPVerification.PURPOSE_PASSWORD_RESET)
            if success:
                verified = True
                break
            # Also check if verified under registration or login purpose
            success_reg, _ = OTPService.verify_otp(p, otp_code, OTPVerification.PURPOSE_REGISTRATION)
            if success_reg:
                verified = True
                break

        if not verified:
            return Response({'error': 'Invalid or expired OTP code.'}, status=status.HTTP_400_BAD_REQUEST)

        from django.db.models import Q
        user = User.objects.filter(
            Q(phone_number__in=variants) | Q(username__in=variants)
        ).first()

        if not user:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        user.set_password(new_password)
        user.account_state = User.ACCOUNT_ACTIVE
        user.is_active = True
        user.save()

        tokens = get_tokens_for_user(user)
        tokens['role'] = user.role
        tokens['message'] = 'Password reset successful.'
        return Response(tokens, status=status.HTTP_200_OK)
