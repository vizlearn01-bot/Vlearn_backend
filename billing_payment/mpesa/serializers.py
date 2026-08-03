from rest_framework import serializers
from utils.validators import PhoneNumberValidator


class MpesaPaymentDetailsSerializer(serializers.Serializer):
    mpesa_phone_number = serializers.CharField(max_length=20)
