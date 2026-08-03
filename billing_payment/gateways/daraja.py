import logging
from typing import Dict, Any
from decimal import Decimal
from django.conf import settings

from .base import (
    BasePaymentGateway,
    PaymentInitiationRequest,
    GatewayResponse,
    NormalizedPaymentResult,
)
from billing_payment.models import MpesaPaymentAccount
from billing_payment.mpesa.utils import MpesaApi, StkPushCallbackResponseParser, _mask

logger = logging.getLogger(__name__)


class DarajaGateway(BasePaymentGateway):
    def __init__(self, mpesa_payment_account: MpesaPaymentAccount):
        self.mpesa_payment_account = mpesa_payment_account
        # Set is_live from settings
        self.is_live = getattr(settings, "MPESA_ENVIRONMENT", "sandbox") == "production"
        self._mpesa_api = MpesaApi(mpesa_payment_account, is_live=self.is_live)
        logger.info(
            "DarajaGateway: Initialized. account='%s', env=%s, is_live=%s, shortcode=%s",
            mpesa_payment_account.name,
            getattr(settings, 'MPESA_ENVIRONMENT', 'sandbox'),
            self.is_live,
            mpesa_payment_account.paybill_number or mpesa_payment_account.till_number or "N/A",
        )

    def initiate_payment(self, request: PaymentInitiationRequest) -> GatewayResponse:
        logger.info(
            "DarajaGateway.initiate_payment: Initiating payment. amount=%s, phone=%s, ref=%s",
            request.amount,
            _mask(request.phone_number),
            request.account_reference,
        )
        # Mask the token if it exists in the callback url for logging
        from urllib.parse import urlparse, parse_qs, urlencode
        masked_callback_url = request.callback_url
        if "token=" in masked_callback_url:
            parsed = urlparse(masked_callback_url)
            query_dict = parse_qs(parsed.query)
            if 'token' in query_dict:
                query_dict['token'] = ['****']
                new_query = urlencode(query_dict, doseq=True)
                masked_callback_url = parsed._replace(query=new_query).geturl()

        logger.info(
            "DarajaGateway.initiate_payment: CallBackURL=%s",
            masked_callback_url,
        )
        
        # Wrap existing STK push initiation
        response_data = self._mpesa_api.initiate_stk_push(
            phone_number=request.phone_number,
            account_reference=request.account_reference,
            amount=int(request.amount),
            transaction_description=request.transaction_description,
            callback_url=request.callback_url,
        )
        gateway_response = GatewayResponse(
            is_successful=response_data.get("is_successful", False),
            provider_transaction_id=response_data.get("checkout_request_id", ""),
            provider_reference=response_data.get("merchant_request_id", ""),
            response_code=response_data.get("response_code", ""),
            response_message=response_data.get("response_description", "") or response_data.get("customer_message", ""),
            raw_response=response_data,
        )
        logger.info(
            "DarajaGateway.initiate_payment: Result. is_successful=%s, checkout_request_id=%s",
            gateway_response.is_successful,
            gateway_response.provider_transaction_id or response_data.get("error_code"),
        )
        return gateway_response

    def query_payment_status(self, provider_transaction_id: str) -> NormalizedPaymentResult:
        logger.info(
            "DarajaGateway.query_payment_status: Querying status for checkout_request_id=%s",
            provider_transaction_id,
        )
        # Wrap existing STK push status query
        response_data = self._mpesa_api.query_stk_push_status(provider_transaction_id)
        
        result = NormalizedPaymentResult(
            is_successful=response_data.get("is_successful", False),
            provider_transaction_id=response_data.get("checkout_request_id", ""),
            receipt_number=None,
            amount_paid=None,
            phone_number=None,
            paid_at=None,
            result_code=str(response_data.get("result_code", "")),
            result_description=response_data.get("result_description", ""),
            raw_payload=response_data,
        )
        logger.info(
            "DarajaGateway.query_payment_status: Result. is_successful=%s, result_code=%s",
            result.is_successful,
            result.result_code,
        )
        return result

    def validate_webhook(self, headers: Dict[str, str], body: bytes, params: Dict[str, Any]) -> bool:
        logger.debug("DarajaGateway.validate_webhook: Validating incoming callback.")
        
        # Parse body for detailed diagnostics if possible
        import json
        checkout_request_id = "Unknown"
        result_code = "Unknown"
        try:
            raw_payload = json.loads(body)
            if "Body" in raw_payload and "stkCallback" in raw_payload["Body"]:
                checkout_request_id = raw_payload["Body"]["stkCallback"].get("CheckoutRequestID", "Unknown")
                result_code = raw_payload["Body"]["stkCallback"].get("ResultCode", "Unknown")
        except Exception:
            pass

        client_ip = headers.get("X-Forwarded-For") or headers.get("REMOTE_ADDR") or "Unknown"
        if client_ip and "," in client_ip:
            client_ip = client_ip.split(",")[0].strip()
            
        configured_token = getattr(settings, "MPESA_CALLBACK_SECRET_TOKEN", None)
        supplied_token = params.get("token")
        
        # Validate callback token
        if configured_token:
            if supplied_token != configured_token:
                logger.warning(
                    "Webhook validation failed\n"
                    "Configured token: Yes\n"
                    "Supplied token: %s\n"
                    "Client IP: %s\n"
                    "CheckoutRequestID: %s\n"
                    "ResultCode: %s",
                    "Yes" if supplied_token else "No",
                    client_ip,
                    checkout_request_id,
                    result_code,
                )
                return False
        else:
            logger.warning(
                "DarajaGateway.validate_webhook: MPESA_CALLBACK_SECRET_TOKEN not configured. Skipping token validation."
            )

        # Validate source IP
        allowed_ips = getattr(settings, "MPESA_ALLOWED_SOURCE_IPS", [])
        if allowed_ips:
            # Check standard IP headers
            source_ip = headers.get("X-Forwarded-For") or headers.get("REMOTE_ADDR")
            if source_ip and "," in source_ip:
                source_ip = source_ip.split(",")[0].strip()
                
            if not source_ip or source_ip not in allowed_ips:
                logger.warning(
                    "DarajaGateway.validate_webhook: REJECTED. Source IP not in whitelist. ip=%s",
                    source_ip,
                )
                return False
        else:
            logger.warning(
                "DarajaGateway.validate_webhook: MPESA_ALLOWED_SOURCE_IPS not configured. Skipping IP validation."
            )

        logger.debug("DarajaGateway.validate_webhook: ACCEPTED.")
        return True

    def parse_webhook_payload(self, raw_payload: Dict[str, Any]) -> NormalizedPaymentResult:
        parser = StkPushCallbackResponseParser(raw_payload)
        parsed_data = parser.get_result_data()
        
        logger.info(
            "DarajaGateway.parse_webhook_payload: Parsed callback. "
            "checkout_request_id=%s, is_successful=%s, result_code=%s, receipt=%s",
            parsed_data.get("checkout_request_id"),
            parsed_data.get("is_successful"),
            parsed_data.get("result_code"),
            parsed_data.get("mpesa_receipt_number"),
        )
        
        amount_paid = None
        if parsed_data.get("amount") is not None:
            amount_paid = Decimal(str(parsed_data.get("amount")))
            
        return NormalizedPaymentResult(
            is_successful=parsed_data.get("is_successful", False),
            provider_transaction_id=parsed_data.get("checkout_request_id", ""),
            receipt_number=parsed_data.get("mpesa_receipt_number"),
            amount_paid=amount_paid,
            phone_number=parsed_data.get("phone_number"),
            paid_at=parsed_data.get("transaction_date"),
            result_code=str(parsed_data.get("result_code", "")),
            result_description=parsed_data.get("result_description", ""),
            raw_payload=raw_payload,
        )
