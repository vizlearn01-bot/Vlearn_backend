from rest_framework import serializers
from utils.validators import PhoneNumberValidator


class MpesaPaymentDetailsSerializer(serializers.Serializer):
    mpesa_phone_number = serializers.CharField(
        max_length=20, validators=[PhoneNumberValidator(min_length=12, max_length=12)]
    )
