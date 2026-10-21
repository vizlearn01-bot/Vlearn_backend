"""
billing_payment/utils/config.py

Runtime configuration utilities for the billing and payment system.
"""
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


import os

def get_mpesa_callback_url() -> str:
    """
    Returns the configured M-Pesa STK Push callback URL.

    Resolution order:
        1. MPESA_CALLBACK_URL if explicitly configured and NOT pointing to dead domains (e.g. api.vizlearn.co).
        2. RENDER_EXTERNAL_HOSTNAME if running on Render.
        3. LIVE_URL if configured and NOT pointing to dead domains.
        4. Production fallback: https://vlearn-backend-4y9z.onrender.com/api/billing-and-payments/mpesa/stk-push-callback/

    Returns:
        str: The full callback URL for the M-Pesa STK Push API.
    """
    explicit_url = str(getattr(settings, "MPESA_CALLBACK_URL", "") or "").strip()
    if explicit_url and "api.vizlearn.co" not in explicit_url:
        logger.debug("get_mpesa_callback_url: Using MPESA_CALLBACK_URL=%s", explicit_url)
        return explicit_url

    render_host = os.getenv("RENDER_EXTERNAL_HOSTNAME", "").strip()
    if render_host:
        constructed_url = f"https://{render_host}/api/billing-and-payments/mpesa/stk-push-callback/"
        logger.debug("get_mpesa_callback_url: Using RENDER_EXTERNAL_HOSTNAME: %s", constructed_url)
        return constructed_url

    live_url = str(getattr(settings, "LIVE_URL", "") or "").strip().rstrip("/")
    if live_url and "api.vizlearn.co" not in live_url:
        if live_url.startswith("http://") or live_url.startswith("https://"):
            return f"{live_url}/api/billing-and-payments/mpesa/stk-push-callback/"
        constructed_url = f"https://{live_url}/api/billing-and-payments/mpesa/stk-push-callback/"
        logger.debug("get_mpesa_callback_url: Constructed from LIVE_URL: %s", constructed_url)
        return constructed_url

    return "https://vlearn-backend-4y9z.onrender.com/api/billing-and-payments/mpesa/stk-push-callback/"

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
