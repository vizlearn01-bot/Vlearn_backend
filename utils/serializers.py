from rest_framework import serializers
from utils.validators import PhoneNumberValidator


class AddressSerializer(serializers.Serializer):
    street = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    building = serializers.CharField(max_length=100, required=False)
    description = serializers.CharField(
        max_length=200, required=False, allow_blank=True
    )


class ContactsSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        validators=[
            PhoneNumberValidator(min_length=10, max_length=12),
        ],
    )
    email = serializers.EmailField()
