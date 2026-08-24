import hashlib
import json
import uuid

VLEARN_NAMESPACE = uuid.UUID('a1b2c3d4-e5f6-7890-abcd-ef1234567890')

def generate_deterministic_uuid(model_name: str, pk: int) -> uuid.UUID:
    """Generate a deterministic UUID based on model name and primary key."""
    return uuid.uuid5(VLEARN_NAMESPACE, f"{model_name}:{pk}")

OPERATIONAL_FIELDS = {
    'Lesson': ['immutable_metadata'],  # Contains generation_job_id
}

NATURAL_KEY_MODELS = {
    'Curriculum': ['name'],
    'Grade': ['curriculum__name', 'name'],
    'Subject': ['grade__curriculum__name', 'grade__name', 'name'],
    'Simulation': ['key'],
}

def compute_content_hash(instance, exclude_fields=None) -> str:
    """
    Compute a SHA-256 hash of the content fields of a model instance.
    """
    base_exclude = {'id', 'pk', 'created_at', 'updated_at', 'content_uuid', 'content_hash'}
    if exclude_fields:
        base_exclude.update(exclude_fields)
        
    model_name = instance.__class__.__name__
    if model_name in OPERATIONAL_FIELDS:
        base_exclude.update(OPERATIONAL_FIELDS[model_name])
        
    # Get all fields for the model
    fields = instance._meta.get_fields()
    
    # We only care about concrete fields (not reverse relations)
    concrete_fields = [f for f in fields if f.concrete and not f.many_to_many]
    
    # Sort by field name to ensure deterministic order
    concrete_fields.sort(key=lambda f: f.name)
    
    hash_input = []
    
    for field in concrete_fields:
        if field.name in base_exclude:
            continue
            
        value = getattr(instance, field.attname)
        
        if value is None:
            hash_input.append(f"{field.name}:null")
        elif isinstance(value, (dict, list)):
            # For JSON fields, serialize with sorted keys
            try:
                json_str = json.dumps(value, sort_keys=True)
                hash_input.append(f"{field.name}:{json_str}")
            except (TypeError, ValueError):
                hash_input.append(f"{field.name}:{str(value)}")
        else:
            hash_input.append(f"{field.name}:{str(value)}")
            
    hash_str = "|".join(hash_input)
    return hashlib.sha256(hash_str.encode('utf-8')).hexdigest()

def build_natural_key_lookup(source_obj, model_name: str) -> dict:
    """Build a dictionary of filter kwargs for natural key lookup."""
    if model_name not in NATURAL_KEY_MODELS:
        return {}
        
    lookup = {}
    for key_path in NATURAL_KEY_MODELS[model_name]:
        parts = key_path.split('__')
        
        # Traverse relationships on the source object
        current_obj = source_obj
        for part in parts[:-1]:
            current_obj = getattr(current_obj, part)
            if current_obj is None:
                break
                
        if current_obj is not None:
            lookup[key_path] = getattr(current_obj, parts[-1])
            
    return lookup

def find_target_match(source_obj, target_queryset, model_name: str):
    """
    Find the matching object in the target database.
    Uses natural keys for Curriculum/Grade/Subject/Simulation.
    Uses content_uuid for all other models.
    Returns the target object or None.
    """
    if model_name in NATURAL_KEY_MODELS:
        lookup = build_natural_key_lookup(source_obj, model_name)
        if not lookup:
            return None
        return target_queryset.filter(**lookup).first()
    else:
        # For non-natural key models, we must use content_uuid
        if not hasattr(source_obj, 'content_uuid') or not source_obj.content_uuid:
            return None
        return target_queryset.filter(content_uuid=source_obj.content_uuid).first()
