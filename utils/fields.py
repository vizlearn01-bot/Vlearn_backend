import json
import base64
import hashlib
from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
from cryptography.fernet import Fernet
from django.conf import settings
from django.core.exceptions import ValidationError
from django import forms
import os
from rest_framework import serializers


# Method 1: Generate a properly encoded key from your SECRET_KEY
def generate_fernet_key(secret_key):
    # Create a SHA256 hash of the secret key
    key_hash = hashlib.sha256(str(secret_key).encode()).digest()
    # Encode the hash to base64 and ensure it's URL-safe
    fernet_key = base64.urlsafe_b64encode(key_hash)

    return fernet_key


class EncryptedCharField(models.TextField):
    def __init__(self, *args, **kwargs):
        # Initialize the encryption key
        self.cipher = Fernet(generate_fernet_key(settings.SECRET_KEY))
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        """
        Decrypt the value when retrieving it from the database.
        """
        if value is None:
            return value
        try:
            return self.cipher.decrypt(base64.b64decode(value.encode())).decode()
        except Exception:
            raise ValueError("Failed to decrypt the value")

    def to_python(self, value):
        """
        Ensure the field is decrypted when accessed in Python.
        """
        if value is None:
            return value
        if isinstance(value, str):  # If already decrypted
            return value
        return self.cipher.decrypt(base64.b64decode(value.encode())).decode()

    def get_prep_value(self, value):
        """
        Encrypt the value before saving it to the database.
        """
        if value is None:
            return value
        encrypted = self.cipher.encrypt(value.encode())
        return base64.b64encode(encrypted).decode()
    
class EncryptedTextField(models.TextField):
    def __init__(self, *args, **kwargs):
        # Initialize the encryption key
        self.cipher = Fernet(generate_fernet_key(settings.SECRET_KEY))
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        """
        Decrypt the value when retrieving it from the database.
        """
        if value is None:
            return value
        try:
            return self.cipher.decrypt(base64.b64decode(value.encode())).decode()
        except Exception:
            raise ValueError("Failed to decrypt the value")

    def to_python(self, value):
        """
        Ensure the field is decrypted when accessed in Python.
        """
        if value is None:
            return value
        if isinstance(value, str):  # If already decrypted
            return value
        return self.cipher.decrypt(base64.b64decode(value.encode())).decode()

    def get_prep_value(self, value):
        """
        Encrypt the value before saving it to the database.
        """
        if value is None:
            return value
        encrypted = self.cipher.encrypt(value.encode())
        return base64.b64encode(encrypted).decode()

class EncryptedJSONFormField(forms.JSONField):
    def __init__(self, *args, **kwargs):
        kwargs["widget"] = forms.Textarea(attrs={"rows": 10, "cols": 60})
        super().__init__(*args, **kwargs)

    def prepare_value(self, value):
        """
        Prepare the value for display in the admin form
        """
        if value is None:
            return None

        if isinstance(value, (dict, list)):
            return json.dumps(value, indent=2, cls=DjangoJSONEncoder)

        try:
            parsed = json.loads(value)
            return json.dumps(parsed, indent=2, cls=DjangoJSONEncoder)
        except (TypeError, json.JSONDecodeError):
            return value

    def to_python(self, value):
        """
        Convert the value from the form to Python format.
        """
        if value in self.empty_values:
            return None

        try:
            if isinstance(value, (dict, list)):
                return value
            return json.loads(value)
        except json.JSONDecodeError as e:
            raise ValidationError(
                f"Invalid JSON: {str(e)}",
                code="invalid",
                params={"value": value},
            )


class EncryptedJSONField(models.JSONField):
    def __init__(self, *args, **kwargs):
        self.cipher = Fernet(generate_fernet_key(settings.SECRET_KEY))
        kwargs.setdefault("encoder", DjangoJSONEncoder)
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            "form_class": EncryptedJSONFormField,
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        try:
            decrypted = self.cipher.decrypt(base64.b64decode(value.encode())).decode()
            return json.loads(decrypted)
        except Exception as e:
            raise ValueError(f"Failed to decrypt or deserialize: {str(e)}")

    def get_prep_value(self, value):
        if value is None:
            return value

        # First let JSONField validate and transform the value
        value = super().get_prep_value(value)

        # Convert the dict back to a JSON string
        json_string = json.dumps(value, cls=self.encoder)

        # Encrypt the JSON string
        encrypted = self.cipher.encrypt(json_string.encode())
        return base64.b64encode(encrypted).decode()

    def validate(self, value, model_instance):
        # Use JSONField's built-in validation
        super().validate(value, model_instance)


class FileFromJSONField(serializers.JSONField):
    """
    A custom field that takes JSON file metadata and returns the actual file.

    Extends JSONField to properly parse the JSON input, then extracts
    the corresponding file from request.FILES.

    Expected JSON format:
    {
        "name": "filename.ext",
        "type": "mime/type",
        "size": 12345,
        "isFile": true,
        "fileKey": "reference_to_actual_file_in_FILES"
    }
    """

    def __init__(self, **kwargs):
        self.allow_empty_file = kwargs.pop("allow_empty_file", False)
        self.required_fields = kwargs.pop("required_fields", ["fileKey"])
        super().__init__(**kwargs)

    def to_internal_value(self, data):
        """
        Process the JSON data and extract the actual file object.
        """
        # First use JSONField's parsing to handle the JSON input
        parsed_data = super().to_internal_value(data)

        if not parsed_data:
            if self.required:
                raise ValidationError("This field is required.")
            return None

        # Check required metadata fields
        for field in self.required_fields:
            if field not in parsed_data:
                raise ValidationError(
                    f"Missing required field '{field}' in file metadata."
                )

        file_key = parsed_data.get("fileKey")

        # Make sure we have access to the request
        request = self.context.get("request")
        if not request:
            raise ValidationError(
                "Cannot access request. Make sure 'request' is included in serializer context."
            )

        # Get the file from request.FILES
        if file_key not in request.FILES:
            raise ValidationError(f"File not found with key '{file_key}'.")

        file_obj = request.FILES[file_key]

        # Validate file size if specified in metadata
        if "size" in parsed_data and parsed_data["size"] > 0:
            if not file_obj.size:
                raise ValidationError("File is empty.")

            if file_obj.size != parsed_data["size"]:
                # Just log a warning instead of failing
                print(
                    f"Warning: File size mismatch. Expected {parsed_data['size']}, got {file_obj.size}"
                )
        elif not self.allow_empty_file and not file_obj.size:
            raise ValidationError("File is empty.")

        # Return the actual file object
        return file_obj

    def to_representation(self, value):
        """
        Convert a file object to a JSON representation.
        """
        if not value:
            return None

        if hasattr(value, "url"):
            # If the file has a URL (e.g., stored on S3)
            url = value.url
        else:
            # Default to name if URL is not available
            url = None

        return {
            "name": os.path.basename(value.name),
            "size": value.size if hasattr(value, "size") else None,
            "url": url,
        }
