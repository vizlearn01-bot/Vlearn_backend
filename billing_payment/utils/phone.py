def normalize_phone_number(raw_phone: str) -> str:
    """
    Normalizes a phone number to the 254XXXXXXXXX format.
    
    Args:
        raw_phone (str): The raw phone number string to normalize.
        
    Returns:
        str: The normalized phone number.
        
    Raises:
        ValueError: If the phone number is invalid (e.g. non-numeric, wrong length).
    """
    if not isinstance(raw_phone, str):
        raise ValueError("Phone number must be a string.")
        
    # Strip whitespace
    cleaned = "".join(raw_phone.split())
    
    # Handle prefixes
    if cleaned.startswith("+254"):
        cleaned = cleaned[1:]
    elif cleaned.startswith("07") or cleaned.startswith("01"):
        cleaned = "254" + cleaned[1:]
        
    # Check for non-numeric characters
    if not cleaned.isdigit():
        raise ValueError("Invalid phone number format: contains non-numeric characters.")
        
    # Valid Kenyan numbers formatted this way have 12 digits total and start with 254
    if len(cleaned) != 12 or not cleaned.startswith("254"):
        raise ValueError("Invalid phone number format: insufficient digits or invalid prefix.")
        
    return cleaned
