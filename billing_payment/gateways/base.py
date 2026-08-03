from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, Dict, Any
from decimal import Decimal


@dataclass
class PaymentInitiationRequest:
    amount: Decimal
    phone_number: str
    account_reference: str
    transaction_description: str
    callback_url: str
    metadata: Optional[Dict[str, Any]] = None


@dataclass 
class GatewayResponse:
    is_successful: bool
    provider_transaction_id: str  # CheckoutRequestID
    provider_reference: str       # MerchantRequestID
    response_code: str
    response_message: str
    raw_response: Dict[str, Any]


@dataclass
class NormalizedPaymentResult:
    is_successful: bool
    provider_transaction_id: str
    receipt_number: Optional[str]
    amount_paid: Optional[Decimal]
    phone_number: Optional[str]
    paid_at: Optional[str]
    result_code: str
    result_description: str
    raw_payload: Dict[str, Any]


class BasePaymentGateway(ABC):
    @abstractmethod
    def initiate_payment(self, request: PaymentInitiationRequest) -> GatewayResponse: ...

    @abstractmethod
    def query_payment_status(self, provider_transaction_id: str) -> NormalizedPaymentResult: ...

    @abstractmethod
    def validate_webhook(self, headers: Dict[str, str], body: bytes, params: Dict[str, Any]) -> bool: ...

    @abstractmethod
    def parse_webhook_payload(self, raw_payload: Dict[str, Any]) -> NormalizedPaymentResult: ...
