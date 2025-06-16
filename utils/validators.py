from rest_framework.exceptions import ValidationError


class PhoneNumberValidator:
    def __init__(self, min_length=None, max_length=None):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, value):
        if self.min_length is not None and len(value) < self.min_length:
            raise ValidationError(
                f"Phone number must be at least {self.min_length} characters long."
            )
        if self.max_length is not None and len(value) > self.max_length:
            raise ValidationError(
                f"Phone number cannot exceed {self.max_length} characters."
            )
        if not value.isdigit():
            raise ValidationError(
                "Phone number must consist only of digits. Exclude the + symbol on in your phone number."
            )
