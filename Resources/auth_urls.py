from django.urls import path
from .auth_views import (
    RequestOTPView,
    VerifyOTPView,
    PhoneRegisterView,
    PhoneLoginView,
    PhonePasswordResetView
)

urlpatterns = [
    path('request-otp/', RequestOTPView.as_view(), name='request-otp'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
    path('phone-register/', PhoneRegisterView.as_view(), name='phone-register'),
    path('phone-login/', PhoneLoginView.as_view(), name='phone-login'),
    path('phone-reset-password/', PhonePasswordResetView.as_view(), name='phone-reset-password'),
]
