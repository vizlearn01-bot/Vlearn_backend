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


class OnboardingService:
    @staticmethod
    def get_student_onboarding_state(user):
        from .models import UserProfile, StudentSubjectSelection, StudentAcademicBaseline
        profile, _ = UserProfile.objects.get_or_create(user=user)
        
        selections = StudentSubjectSelection.objects.filter(user=user).select_related('subject')
        selected_subject_ids = list(selections.values_list('subject_id', flat=True))
        priority_subject_ids = list(selections.filter(is_priority=True).values_list('subject_id', flat=True))
        
        baselines = StudentAcademicBaseline.objects.filter(user=user).select_related('subject', 'academic_year', 'examination')
        baseline_data = [
            {
                "subject_id": b.subject_id,
                "subject_name": b.subject.name,
                "grading_scheme": b.grading_scheme,
                "raw_previous_grade": b.raw_previous_grade,
                "normalized_score": str(b.normalized_score) if b.normalized_score else None,
                "target_grade": b.target_grade,
                "academic_year_id": b.academic_year_id,
                "examination_id": b.examination_id,
            }
            for b in baselines
        ]

        return {
            "onboarding_status": profile.onboarding_status,
            "onboarding_version": profile.onboarding_version,
            "completed_at": profile.completed_at,
            "profile": {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "curriculum_id": profile.curriculum_id,
                "curriculum_name": profile.curriculum.name if profile.curriculum else None,
                "grade_id": profile.curriculum_grade_id,
                "grade_name": profile.curriculum_grade.name if profile.curriculum_grade else None,
                "school_association_type": profile.school_association_type,
                "verified_school_id": profile.verified_school_id,
                "verified_school_name": profile.verified_school.name if profile.verified_school else None,
                "unverified_school_name": profile.unverified_school_name,
                "school_type": profile.school_type,
                "location_county": profile.location_county,
                "location_subcounty": profile.location_subcounty,
                "location_town_village": profile.location_town_village,
                "confidence_level": profile.confidence_level,
                "primary_device": profile.primary_device,
                "career_aspiration": profile.career_aspiration,
            },
            "selected_subject_ids": selected_subject_ids,
            "priority_subject_ids": priority_subject_ids,
            "baselines": baseline_data
        }

    @staticmethod
    def save_student_onboarding_step(user, step, payload):
        from .models import UserProfile
        from curriculum.models import Curriculum, Grade
        from django.core.exceptions import ValidationError

        profile, _ = UserProfile.objects.get_or_create(user=user)

        if step == 1:
            if 'first_name' in payload:
                user.first_name = payload['first_name']
            if 'last_name' in payload:
                user.last_name = payload['last_name']
            user.save()
        elif step == 2:
            curriculum_id = payload.get('curriculum_id')
            grade_id = payload.get('grade_id')
            if curriculum_id:
                curriculum = Curriculum.objects.filter(id=curriculum_id).first()
                if not curriculum:
                    raise ValidationError("Invalid curriculum ID.")
                profile.curriculum = curriculum
            if grade_id:
                grade = Grade.objects.filter(id=grade_id).first()
                if not grade:
                    raise ValidationError("Invalid grade ID.")
                if profile.curriculum and grade.curriculum_id != profile.curriculum.id:
                    raise ValidationError("Grade does not belong to the selected curriculum.")
                profile.curriculum_grade = grade

        if profile.onboarding_status == 'NOT_STARTED':
            profile.onboarding_status = 'IN_PROGRESS'
        profile.save()
        return profile

    @staticmethod
    def complete_minimum_student_onboarding(user, payload):
        from .models import UserProfile, StudentSubjectSelection
        from curriculum.models import Curriculum, Grade, Subject
        from organizations.models import School, UnverifiedSchoolSuggestion
        from django.core.exceptions import ValidationError
        from django.db import transaction

        curriculum_id = payload.get('curriculum_id')
        grade_id = payload.get('grade_id')
        selected_subject_ids = payload.get('selected_subject_ids', [])
        priority_subject_ids = payload.get('priority_subject_ids', [])
        school_id = payload.get('school_id')
        unverified_school_name = payload.get('unverified_school_name')

        curriculum = Curriculum.objects.filter(id=curriculum_id).first()
        if not curriculum:
            raise ValidationError({"curriculum_id": "Invalid curriculum ID."})

        grade = Grade.objects.filter(id=grade_id, curriculum=curriculum).first()
        if not grade:
            raise ValidationError({"grade_id": "Invalid grade ID for selected curriculum."})

        # Dynamic configurable subject limit checks
        max_subjects = grade.max_selectable_subjects_override or curriculum.max_selectable_subjects
        max_priorities = grade.max_priority_subjects_override or curriculum.max_priority_subjects

        if len(selected_subject_ids) > max_subjects:
            raise ValidationError({"selected_subject_ids": f"Maximum {max_subjects} subjects allowed for {grade.name}."})

        if len(priority_subject_ids) > max_priorities:
            raise ValidationError({"priority_subject_ids": f"Maximum {max_priorities} priority subjects allowed."})

        # Validate priority subjects are a subset of selected subjects
        if not set(priority_subject_ids).issubset(set(selected_subject_ids)):
            raise ValidationError({"priority_subject_ids": "Priority subjects must be a subset of selected subjects."})

        # Validate all subjects belong to the grade
        valid_grade_subject_ids = set(Subject.objects.filter(grade=grade).values_list('id', flat=True))
        if not set(selected_subject_ids).issubset(valid_grade_subject_ids):
            raise ValidationError({"selected_subject_ids": "Selected subjects must belong to the chosen grade."})

        with transaction.atomic():
            profile, _ = UserProfile.objects.get_or_create(user=user)
            profile.curriculum = curriculum
            profile.curriculum_grade = grade
            profile.grade = grade.name
            profile.onboarding_version = 1
            profile.onboarding_status = 'MINIMUM_COMPLETE'
            profile.onboarding_complete = True
            profile.completed_at = timezone.now()

            # Handle school selection
            if school_id:
                verified_school = School.objects.filter(id=school_id, is_active=True).first()
                if verified_school:
                    profile.verified_school = verified_school
                    profile.school_association_type = 'VERIFIED_ORGANIZATION'
                    profile.school = verified_school.name
            elif unverified_school_name and unverified_school_name.strip():
                profile.unverified_school_name = unverified_school_name.strip()
                profile.school_association_type = 'UNVERIFIED_SUGGESTION'
                profile.school = unverified_school_name.strip()
                UnverifiedSchoolSuggestion.objects.create(
                    name=unverified_school_name.strip(),
                    proposed_by=user,
                    status='UNVERIFIED'
                )
            else:
                profile.school_association_type = 'INDEPENDENT'

            profile.save()

            # Persist selected & priority subjects
            StudentSubjectSelection.objects.filter(user=user).delete()
            subject_objects = Subject.objects.filter(id__in=selected_subject_ids)
            profile.selected_subjects.set(subject_objects)

            selections = []
            for rank, sub_id in enumerate(selected_subject_ids, 1):
                is_priority = sub_id in priority_subject_ids
                p_rank = (priority_subject_ids.index(sub_id) + 1) if is_priority else None
                selections.append(StudentSubjectSelection(
                    user=user,
                    subject_id=sub_id,
                    is_priority=is_priority,
                    priority_rank=p_rank
                ))
            StudentSubjectSelection.objects.bulk_create(selections)

            user.account_state = User.ACCOUNT_ACTIVE
            user.save()

        return profile

    @staticmethod
    def complete_progressive_student_onboarding(user, payload):
        from .models import UserProfile, StudentAcademicBaseline
        from organizations.models import AcademicYear, AcademicExamination
        from curriculum.models import Subject
        from django.core.exceptions import ValidationError
        from django.db import transaction

        profile, _ = UserProfile.objects.get_or_create(user=user)

        with transaction.atomic():
            if 'location_county' in payload:
                profile.location_county = payload['location_county']
            if 'location_subcounty' in payload:
                profile.location_subcounty = payload['location_subcounty']
            if 'location_town_village' in payload:
                profile.location_town_village = payload['location_town_village']
            if 'school_type' in payload:
                profile.school_type = payload['school_type']
            if 'confidence_level' in payload:
                profile.confidence_level = payload['confidence_level']
            if 'primary_device' in payload:
                profile.primary_device = payload['primary_device']
            if 'career_aspiration' in payload:
                profile.career_aspiration = payload['career_aspiration']

            baselines = payload.get('baselines', [])
            for b in baselines:
                sub_id = b.get('subject_id')
                raw_grade = b.get('raw_previous_grade')
                if sub_id and raw_grade:
                    subject = Subject.objects.filter(id=sub_id).first()
                    if subject:
                        ay_id = b.get('academic_year_id')
                        exam_id = b.get('examination_id')
                        ay = AcademicYear.objects.filter(id=ay_id).first() if ay_id else None
                        exam = AcademicExamination.objects.filter(id=exam_id).first() if exam_id else None
                        
                        StudentAcademicBaseline.objects.update_or_create(
                            user=user,
                            subject=subject,
                            academic_year=ay,
                            examination=exam,
                            defaults={
                                "grading_scheme": b.get('grading_scheme', 'LETTER_GRADE'),
                                "raw_previous_grade": raw_grade,
                                "normalized_score": b.get('normalized_score'),
                                "target_grade": b.get('target_grade', ''),
                            }
                        )

            profile.onboarding_status = 'FULLY_COMPLETE'
            profile.save()

        return profile

