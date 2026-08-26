ROLE_HIERARCHY = ['student', 'teacher', 'school_admin', 'platform_admin']

ROLE_PERMISSIONS = {
    'read_curriculum':    ['student', 'teacher', 'school_admin', 'platform_admin'],
    'write_curriculum':   ['platform_admin'],
    'attempt_quiz':       ['student', 'teacher', 'platform_admin'],
    'read_own_profile':   ['student', 'teacher', 'school_admin', 'platform_admin'],
    'read_all_users':     ['platform_admin'],
    'update_user_role':   ['platform_admin'],
    'update_user_status': ['platform_admin'],
    'create_invitation':  ['school_admin', 'platform_admin'],
    'view_analytics':     ['platform_admin'],
    'write_content':      ['platform_admin'],
    'manage_school':      ['school_admin', 'platform_admin'],
    'invite_teacher':     ['school_admin', 'platform_admin'],
    'invite_student':     ['school_admin', 'platform_admin'],
    'assign_teacher':     ['school_admin', 'platform_admin'],
    'enroll_student':     ['school_admin', 'platform_admin'],
}

def role_can(role: str, action: str) -> bool:
    return role in ROLE_PERMISSIONS.get(action, [])

def user_can(user, action: str) -> bool:
    if not user or not user.is_authenticated or not user.is_active:
        return False
    role = getattr(user, 'role', 'student')
    if role == 'platform_admin' or user.is_superuser:
        return True
    return role_can(role, action)


def get_user_content_restrictions(user):
    """
    Returns content and operational restrictions for a user.
    For the marketing demo account ('vizlearn_test'), limits student view
    strictly to Chemistry Form 3 Gas Laws topic (Subject ID 27, Topic ID 22),
    with no simulations, no experiment videos, and no ability to purchase subscriptions.
    """
    if not user or not user.is_authenticated:
        return {
            'is_restricted': False,
            'allowed_subject_ids': [],
            'allowed_topic_ids': [],
            'allow_simulations': True,
            'allow_experiments': True,
            'allow_purchases': True,
            'allow_extra_lessons': True,
            'restriction_message': '',
        }

    username = getattr(user, 'username', '')
    is_student_demo = (
        username in ['vizlearn-student-demo', 'vizlearn_student_demo', 'vizlearn_test'] or
        getattr(user, 'is_content_restricted', False)
    )

    if is_student_demo:
        return {
            'is_restricted': True,
            'allowed_subject_ids': [27],        # Chemistry Form 3
            'allowed_topic_ids': [22],          # Topic 1: Gas Laws
            'allowed_learning_unit_ids': [166], # Module 1.5: Graham's Law of Diffusion and Kinetic Theory
            'allowed_lesson_ids': [163],        # Lesson 163: Graham's Law of Diffusion and Kinetic Theory
            'allow_simulations': False,
            'allow_experiments': False,
            'allow_purchases': False,
            'allow_extra_lessons': False,
            'restriction_message': "This account has limited demo privileges and is restricted to the Graham's Law lesson in Chemistry Form 3.",
        }

    is_teacher_demo = username in ['vizlearn-teacher-demo', 'vizlearn_teacher_demo']
    if is_teacher_demo:
        return {
            'is_restricted': False,
            'allowed_subject_ids': [27],
            'allowed_topic_ids': [],
            'allowed_learning_unit_ids': [],
            'allowed_lesson_ids': [],
            'allow_simulations': True,
            'allow_experiments': True,
            'allow_purchases': False,
            'allow_extra_lessons': True,
            'restriction_message': "This is a demo teacher account and cannot purchase subscriptions.",
        }

    return {
        'is_restricted': False,
        'allowed_subject_ids': [],
        'allowed_topic_ids': [],
        'allowed_learning_unit_ids': [],
        'allowed_lesson_ids': [],
        'allow_simulations': True,
        'allow_experiments': True,
        'allow_purchases': True,
        'allow_extra_lessons': True,
        'restriction_message': '',
    }



