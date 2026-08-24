import os
import logging

logger = logging.getLogger(__name__)


class AfricasTalkingClient:
    """SMS client using Africa's Talking API."""
    
    def __init__(self):
        self.username = os.getenv('AT_USERNAME', 'sandbox')
        self.api_key = os.getenv('AT_API_KEY', '')
        self.sender_id = os.getenv('AT_SENDER_ID', None)
        self._initialized = False
        self._sms = None
    
    def _initialize(self):
        if self._initialized:
            return
        try:
            import africastalking
            africastalking.initialize(self.username, self.api_key)
            self._sms = africastalking.SMS
            self._initialized = True
        except ImportError:
            logger.warning("africastalking package not installed. SMS will not be sent.")
        except Exception as e:
            logger.error(f"Failed to initialize Africa's Talking: {e}")
    
    def send_sms(self, phone_number, message):
        """Send an SMS message. Returns True on success."""
        self._initialize()
        if not self._sms:
            logger.warning(f"SMS not sent (client not initialized): {phone_number}")
            return False
        try:
            kwargs = {'message': message, 'recipients': [phone_number]}
            if self.sender_id:
                kwargs['sender_id'] = self.sender_id
            response = self._sms.send(**kwargs)
            logger.info(f"SMS sent to {phone_number}: {response}")
            return True
        except Exception as e:
            logger.error(f"Failed to send SMS to {phone_number}: {e}")
            return False
