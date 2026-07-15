import json

class ValidationEngine:
    @staticmethod
    def validate_block(content: str, schema: dict) -> bool:
        if not content or len(content.strip()) < 10:
            return False
            
        # If schema is provided, we might check for JSON structure
        if schema and schema.get("type") == "object":
            try:
                # Naive check if content can be parsed as JSON
                parsed = json.loads(content)
                # Ensure all required keys are present
                for key in schema.get("required", []):
                    if key not in parsed:
                        return False
            except json.JSONDecodeError:
                return False
                
        return True
