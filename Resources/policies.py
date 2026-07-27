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
