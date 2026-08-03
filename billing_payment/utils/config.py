"""
billing_payment/utils/config.py

Runtime configuration utilities for the billing and payment system.
"""
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


def get_mpesa_callback_url() -> str:
    """
    Returns the configured M-Pesa STK Push callback URL.

    Resolution order:
        1. MPESA_CALLBACK_URL (explicit override — highest priority)
           Use this for any environment including ngrok, Cloudflare Tunnel,
           localhost.run, or the production domain.
        2. LIVE_URL (legacy fallback — constructs URL from base domain)

    Local development with a tunnel:
        Set MPESA_CALLBACK_URL=https://<your-tunnel>.ngrok-free.app/api/billing-and-payments/mpesa/stk-push-callback/
        in your .env file. The application will use it without modification.

    Production deployment:
        Set MPESA_CALLBACK_URL=https://api.vizlearn.co/api/billing-and-payments/mpesa/stk-push-callback/
        in your production environment variables.

    Returns:
        str: The full callback URL for the M-Pesa STK Push API.
    """
    explicit_url = getattr(settings, "MPESA_CALLBACK_URL", None)
    if explicit_url:
        logger.debug("get_mpesa_callback_url: Using MPESA_CALLBACK_URL=%s", explicit_url)
        return explicit_url

    live_url = getattr(settings, "LIVE_URL", "")
    if not live_url:
        logger.error(
            "get_mpesa_callback_url: Neither MPESA_CALLBACK_URL nor LIVE_URL is configured. "
            "Safaricom will not be able to deliver payment callbacks."
        )
    constructed_url = f"https://{live_url}/api/billing-and-payments/mpesa/stk-push-callback/"
    logger.debug("get_mpesa_callback_url: Constructed from LIVE_URL: %s", constructed_url)
    return constructed_url

import urllib.parse

def build_secure_callback_url(base_url: str) -> str:
    """
    Takes a base callback URL and securely appends the MPESA_CALLBACK_SECRET_TOKEN
    query parameter if it is configured. Preserves existing query parameters.
    Does not duplicate the token if it is already present.
    """
    token = getattr(settings, "MPESA_CALLBACK_SECRET_TOKEN", None)
    if not token:
        return base_url

    parsed = urllib.parse.urlparse(base_url)
    query_dict = urllib.parse.parse_qs(parsed.query)
    
    if 'token' not in query_dict:
        query_dict['token'] = [token]
        new_query = urllib.parse.urlencode(query_dict, doseq=True)
        return parsed._replace(query=new_query).geturl()
        
    return base_url
