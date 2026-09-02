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
    if role == 'platform_admin' or user.is_superuser or getattr(user, 'is_staff', False):
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
    is_teacher_demo = username in ['vizlearn-teacher-demo', 'vizlearn_teacher_demo']

    if is_student_demo or is_teacher_demo:
        # Dynamically resolve IDs so this works in both Local and Production/Supabase databases
        from curriculum.models import Subject, Topic, Lesson, LearningUnit
        from django.db.models import Q

        # 1. 8-4-4 Form 3 Chemistry (Topic 1: Gas Laws -> Graham's Law)
        chem_subj = Subject.objects.filter(name__iexact='Chemistry', grade__name__iexact='Form 3').first()
        chem_subj_id = chem_subj.id if chem_subj else 27

        chem_topic = Topic.objects.filter(subject_id=chem_subj_id, name__icontains='Gas Laws').first()
        chem_topic_id = chem_topic.id if chem_topic else 22

        chem_lesson = Lesson.objects.filter(topic_id=chem_topic_id, title__icontains='Graham').first()
        chem_lesson_id = chem_lesson.id if chem_lesson else 163
        chem_unit_id = chem_lesson.learning_unit_id if (chem_lesson and chem_lesson.learning_unit_id) else 166

        # 2. CBC Grade 10 Computer Science (Topic 1: Evolution of Computers -> Lesson 1: Early Computing Devices)
        cs_subj = Subject.objects.filter(name__iexact='Computer Science', grade__name__iexact='Grade 10').first()
        cs_subj_id = cs_subj.id if cs_subj else 38

        cs_topic = Topic.objects.filter(subject_id=cs_subj_id).order_by('order', 'id').first()
        cs_topic_id = cs_topic.id if cs_topic else 204

        cs_unit = LearningUnit.objects.filter(topic_id=cs_topic_id).order_by('order', 'id').first() if cs_topic_id else None
        cs_unit_id = cs_unit.id if cs_unit else 1600

        cs_lesson = Lesson.objects.filter(
            Q(learning_unit_id=cs_unit_id) | Q(topic_id=cs_topic_id, learning_unit__isnull=True),
            status='published'
        ).order_by('id').first() if (cs_unit_id or cs_topic_id) else None
        cs_lesson_id = cs_lesson.id if cs_lesson else 1590

        allowed_subject_ids = list(filter(None, [chem_subj_id, cs_subj_id]))
        allowed_topic_ids = list(filter(None, [chem_topic_id, cs_topic_id]))
        allowed_unit_ids = list(filter(None, [chem_unit_id, cs_unit_id]))
        allowed_lesson_ids = list(filter(None, [chem_lesson_id, cs_lesson_id]))

        if is_student_demo:
            return {
                'is_restricted': True,
                'allowed_subject_ids': allowed_subject_ids,
                'allowed_topic_ids': allowed_topic_ids,
                'allowed_learning_unit_ids': allowed_unit_ids,
                'allowed_lesson_ids': allowed_lesson_ids,
                'allow_simulations': False,
                'allow_experiments': False,
                'allow_purchases': False,
                'allow_extra_lessons': False,
                'restriction_message': "This account has limited demo privileges and is restricted to demo lessons in Chemistry Form 3 and CBC Grade 10 Computer Science.",
            }

        # is_teacher_demo
        return {
            'is_restricted': True,
            'allowed_subject_ids': allowed_subject_ids,
            'allowed_topic_ids': allowed_topic_ids,
            'allowed_learning_unit_ids': allowed_unit_ids,
            'allowed_lesson_ids': allowed_lesson_ids,
            'allow_simulations': True,          # Teachers can preview simulations
            'allow_experiments': True,          # Teachers can preview experiments
            'allow_purchases': False,
            'allow_extra_lessons': False,
            'restriction_message': "This demo teacher account is restricted to demo lessons in Chemistry Form 3 and CBC Grade 10 Computer Science.",
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




