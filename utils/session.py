from django.conf import settings

def set_auth_cookies(response, access_token, refresh_token):
    """
    Helper function to set authentication tokens as HttpOnly cookies.
    This prepares for migration from Bearer headers to cookies.
    """
    cookie_max_age = 3600 * 24 * 7  # 7 days for refresh token
    
    secure = getattr(settings, 'SESSION_COOKIE_SECURE', False)
    
    response.set_cookie(
        key='access_token',
        value=access_token,
        httponly=True,
        secure=secure,
        samesite='Lax'
    )
    
    response.set_cookie(
        key='refresh_token',
        value=refresh_token,
        httponly=True,
        secure=secure,
        samesite='Lax',
        max_age=cookie_max_age
    )
    return response

def delete_auth_cookies(response):
    """
    Helper function to clear authentication cookies on logout.
    """
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')
    return response
