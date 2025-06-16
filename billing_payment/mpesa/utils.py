import requests
from datetime import timedelta
from base64 import b64encode

import requests.auth
from billing_payment.models import MpesaPaymentAccount, MpesaApiAccessToken
from django.conf import settings
from django.utils import timezone
from django.utils.timezone import datetime

import logging

logger = logging.getLogger(__name__)

# Constants for API URLs
AUTHENTICATION_API_URL = "/oauth/v1/generate"
STK_PUSH_API_URL = "/mpesa/stkpush/v1/processrequest"
STK_PUSH_QUERY_API_URL = "/mpesa/stkpushquery/v1/query"
CALLBACK_URL = (
    f"https://{settings.LIVE_URL}/api/billing-and-payments/mpesa/stk-push-callback/"
)


class MpesaApi:
    """
    Handles API calls to the Daraja API.

    Attributes:
        mpesa_payment_account (MpesaPaymentAccount): Instance of MpesaPaymentAccount model.
        is_live (bool): Indicates whether the API calls should use the live environment.
    """

    def __init__(
        self, mpesa_payment_account: MpesaPaymentAccount, is_live: bool = False
    ):
        """
        Initializes an instance of MpesaApi.

        Args:
            mpesa_payment_account (MpesaPaymentAccount): Instance of MpesaPaymentAccount model.
            is_live (bool): Boolean indicating whether the API calls should use the live environment.
        """
        self.mpesa_payment_account = mpesa_payment_account
        self.is_live = is_live

        # Base URLs for the API
        self.base_url = (
            "https://api.safaricom.co.ke"
            if is_live
            else "https://sandbox.safaricom.co.ke"
        )

    def get_access_token(self) -> str:
        """
        Returns a valid access token to be used in API calls.
        Checks the MpesaPaymentAccount for an existing valid token or makes an API call to generate one.

        Returns:
            str: The access token string.
        """
        # Check for a valid access token in the MpesaPaymentAccount model
        access_token = self.mpesa_payment_account.get_access_token()
        if access_token:
            return access_token

        # If no valid token exists, make an API call to generate one
        url = f"{self.base_url}{AUTHENTICATION_API_URL}?grant_type=client_credentials"
        credentials = self.mpesa_payment_account.authentication_credentials

        print("credentials", credentials)

        if (
            not credentials
            or "customer_key" not in credentials
            or "customer_secret" not in credentials
        ):
            raise ValueError(
                "Missing authentication credentials for the Mpesa payment account."
            )

        response = requests.get(
            url,
            auth=requests.auth.HTTPBasicAuth(
                credentials["customer_key"], credentials["customer_secret"]
            ),
        )
        print(response)

        try:
            response_json = response.json()
        except ValueError:
            raise ValueError("Invalid JSON response from M-Pesa API.")

        # Parse response using AccessTokenRequestParser
        parser = AccessTokenRequestParser(response_json)
        if parser.is_successful():
            access_token = parser.get_access_token()
            expiry_date = parser.get_expiry_time()

            if access_token and expiry_date:
                new_access_token = MpesaApiAccessToken.objects.create(
                    mpesa_payment_account=self.mpesa_payment_account,
                    access_token=access_token,
                    expiry_date=expiry_date,
                )
                return new_access_token.access_token
            else:
                raise ValueError(
                    "Access token or expiry date not found in the API response."
                )
        else:
            error_message = parser.get_error_message()
            raise ValueError(f"Failed to generate access token. Error: {error_message}")

    def initiate_stk_push(
        self,
        phone_number: str,
        account_reference: str,
        amount: int,
        transaction_description: str,
        callback_url: str = CALLBACK_URL,
    ) -> dict:
        """
        Initiates an STK push request for the given phone number.

        Args:
            phone_number (str): The phone number of the paying user in the format 2547XXXXXXXX.
            callback_url (str): The callback URL for receiving notifications from M-Pesa API.
            account_reference (str): An identifier of the transaction for the CustomerPayBillOnline transaction type.
            amount (int): The amount to be transacted.
            transaction_description (str): Additional information/comment for the transaction.

        Returns:
            dict: The parsed response from the STK push API.
        """
        # Generate an access token
        access_token = self.get_access_token()

        # Prepare STK Push API URL
        url = f"{self.base_url}{STK_PUSH_API_URL}"

        # Prepare request data
        business_shortcode = (
            self.mpesa_payment_account.paybill_number
            or self.mpesa_payment_account.till_number
        )
        timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
        pass_key = self.mpesa_payment_account.authentication_credentials.get("pass_key")

        if not business_shortcode or not pass_key:
            raise ValueError(
                "Missing business shortcode or passkey for the Mpesa payment account."
            )

        password = b64encode(
            f"{business_shortcode}{pass_key}{timestamp}".encode()
        ).decode()

        request_data = {
            "BusinessShortCode": business_shortcode,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": (
                "CustomerPayBillOnline"
                if self.mpesa_payment_account.type == "PAYBILL"
                else "CustomerBuyGoodsOnline"
            ),
            "Amount": int(amount),  # Amount passed as a parameter
            "PartyA": phone_number,
            "PartyB": business_shortcode,
            "PhoneNumber": phone_number,
            "CallBackURL": callback_url,  # Callback URL passed as a parameter
            "AccountReference": account_reference,  # Account Reference passed as a parameter
            "TransactionDesc": transaction_description,  # Transaction Description passed as a parameter
        }

        print("STK Push Request Data:", request_data)

        # Prepare headers
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        # Make the API request
        response = requests.post(url, json=request_data, headers=headers)

        # Parse response using StkPushResponseParser
        parser = StkPushResponseParser(response.json())
        return parser.get_response_data()

    def query_stk_push_status(self, checkout_request_id: str) -> dict:
        """
        Queries the status of a Lipa Na M-PESA Online Payment.

        Args:
            checkout_request_id (str): The globally unique identifier of the processed checkout transaction request.

        Returns:
            dict: The parsed response with details about the STK Push request.
        """
        # Generate an access token
        access_token = self.get_access_token()

        # Prepare STK Push Query API URL
        url = f"{self.base_url}{STK_PUSH_QUERY_API_URL}"

        # Prepare request data
        business_shortcode = (
            self.mpesa_payment_account.paybill_number
            or self.mpesa_payment_account.till_number
        )
        timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
        passkey = self.mpesa_payment_account.authentication_credentials.get("passkey")

        if not business_shortcode or not passkey:
            raise ValueError(
                "Missing business shortcode or passkey for the Mpesa payment account."
            )

        password = b64encode(
            f"{business_shortcode}{passkey}{timestamp}".encode()
        ).decode()

        request_data = {
            "BusinessShortCode": business_shortcode,
            "Password": password,
            "Timestamp": timestamp,
            "CheckoutRequestID": checkout_request_id,
        }

        # Prepare headers
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        # Make the API request
        response = requests.post(url, json=request_data, headers=headers)

        # Parse response using StkPushResponseParser
        parser = StkPushResponseParser(response.json())
        return {
            "merchant_request_id": parser.get_merchant_request_id(),
            "checkout_request_id": parser.get_checkout_request_id(),
            "response_code": parser.get_response_code(),
            "response_description": parser.get_response_description(),
            "result_code": parser.get_result_code(),
            "result_description": parser.get_result_desc(),
            "is_successful": parser.is_successful(),  # Added is_successful flag
        }


class AccessTokenRequestParser:
    """
    Parses the response from the M-PESA Daraja Access Token API.
    Handles both successful and failed responses.
    """

    def __init__(self, response: dict):
        self.response = response

    def is_successful(self) -> bool:
        return "access_token" in self.response

    def get_access_token(self) -> str | None:
        return self.response.get("access_token")

    def get_expires_in(self) -> int | None:
        expires = self.response.get("expires_in")
        if expires is not None:
            try:
                return int(expires)
            except ValueError:
                return None
        return None

    def get_expiry_time(self) -> datetime | None:
        """
        Returns expiry time as a datetime object, or None if not available.
        Calculated from the time of this method call and the expires_in value.
        """
        expires_in = self.get_expires_in()
        if expires_in:
            expiry_time = timezone.now() + timedelta(seconds=expires_in)
            return expiry_time
        return None

    def get_error_code(self) -> str | None:
        return self.response.get("errorCode") or self.response.get("error") or None

    def get_error_message(self) -> str | None:
        return (
            self.response.get("errorMessage")
            or self.response.get("error_description")
            or self.response.get("message")
            or "Unknown error"
        )


class StkPushResponseParser:
    """
    Parses the response from the M-PESA Daraja STK Push API.
    Handles both successful and failed responses.
    """

    REQUEST_TYPES = ["stk_push", "stk_query"]

    def __init__(self, response: dict, is_status_query_request: bool = False):
        """
        Initializes an instance of StkPushResponseParser.
        Args:
            response (dict): The response dictionary from the M-PESA API.
            is_query_request (bool): Indicates if this is a status query request. Defaults to False (STK Push request).
        """
        self.is_status_query_request = is_status_query_request
        self.response = response

    def is_successful(self) -> bool:
        # Success if ResponseCode or ResultCode is "0"
        return (self.get_response_code() == "0") or (self.get_result_code() == "0")

    def get_response_code(self) -> str | None:
        return self.response.get("ResponseCode")

    def get_response_description(self) -> str | None:
        return self.response.get("ResponseDescription")

    def get_customer_message(self) -> str | None:
        return self.response.get("CustomerMessage")

    def get_merchant_request_id(self) -> str | None:
        return self.response.get("MerchantRequestID")

    def get_checkout_request_id(self) -> str | None:
        return self.response.get("CheckoutRequestID")

    def get_result_code(self) -> str | None:
        return self.response.get("ResultCode")

    def get_result_desc(self) -> str | None:
        return self.response.get("ResultDesc")

    def get_request_id(self) -> str | None:
        return self.response.get("requestId")

    def get_error_code(self) -> str | None:
        return self.response.get("errorCode")

    def get_error_message(self) -> str | None:
        return self.response.get("errorMessage")

    def get_response_data(self) -> dict:
        if self.is_successful():
            if self.is_status_query_request:
                return {
                    "merchant_request_id": self.get_merchant_request_id(),
                    "checkout_request_id": self.get_checkout_request_id(),
                    "response_code": self.get_response_code(),
                    "response_description": self.get_response_description(),
                    "result_code": self.get_result_code(),
                    "result_description": self.get_result_desc(),
                    "is_successful": True,
                }
            else:
                return {
                    "merchant_request_id": self.get_merchant_request_id(),
                    "checkout_request_id": self.get_checkout_request_id(),
                    "response_code": self.get_response_code(),
                    "response_description": self.get_response_description(),
                    "customer_message": self.get_customer_message(),
                    "is_successful": True,
                }

        else:
            return {
                "request_id": self.get_request_id(),
                "error_code": self.get_error_code(),
                "error_message": self.get_error_message(),
                "is_successful": False,
            }


class StkPushCallbackResponseParser:
    """
    Parses the callback response sent to your callback URL after the user acts on the STK Push
    (or after timeout, failure, or cancellation).
    """

    def __init__(self, response: dict):
        self.response = response
        self.stk_callback = (
            response.get("Body", {}).get("stkCallback", {})
            if "Body" in response and "stkCallback" in response["Body"]
            else {}
        )

    def get_merchant_request_id(self) -> str | None:
        return self.stk_callback.get("MerchantRequestID")

    def get_checkout_request_id(self) -> str | None:
        return self.stk_callback.get("CheckoutRequestID")

    def get_result_code(self) -> int | None:
        return self.stk_callback.get("ResultCode")

    def get_result_description(self) -> str | None:
        return self.stk_callback.get("ResultDesc")

    def get_callback_metadata(self) -> dict | None:
        return self.stk_callback.get("CallbackMetadata")

    def get_metadata_value(self, name: str):
        meta = self.get_callback_metadata()
        if meta and "Item" in meta:
            for item in meta["Item"]:
                if item.get("Name") == name:
                    return item.get("Value")
        return None

    def get_amount(self) -> float | None:
        return self.get_metadata_value("Amount")

    def get_mpesa_receipt_number(self) -> str | None:
        return self.get_metadata_value("MpesaReceiptNumber")

    def get_balance(self) -> float | None:
        return self.get_metadata_value("Balance")

    def get_transaction_date(self) -> datetime | None:
        timestamp_str = self.get_metadata_value("TransactionDate")
        if timestamp_str:
            try:
                # Convert timestamp to a readable format
                return timezone.datetime.strptime(
                    str(timestamp_str).strip(), "%Y%m%d%H%M%S"
                )
            except (ValueError, TypeError):
                logger.error(
                    f"Unable to parse transaction date from timestamp: {timestamp_str}"
                )

        return None

    def get_phone_number(self) -> str | None:
        return str(self.get_metadata_value("PhoneNumber"))

    def is_successful(self) -> bool:
        """
        Returns True if the callback indicates a successful transaction (ResultCode == 0),
        otherwise False.
        """
        code = self.get_result_code()
        return code == 0

    def get_result_data(self) -> dict:
        """
        Returns the parsed response data in a dictionary format.
        """
        return {
            "merchant_request_id": self.get_merchant_request_id(),
            "checkout_request_id": self.get_checkout_request_id(),
            "result_code": self.get_result_code(),
            "result_description": self.get_result_description(),
            "amount": self.get_amount(),
            "mpesa_receipt_number": self.get_mpesa_receipt_number(),
            "transaction_date": self.get_transaction_date().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "phone_number": self.get_phone_number(),
            "is_successful": self.is_successful(),
        }
