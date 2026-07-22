import json
from typing import Any, Dict

# Detect Pydantic availability and version for backward/forward compatibility
try:
    from pydantic import BaseModel as PydanticBaseModel, Field as PydanticField
    HAS_PYDANTIC = True
    
    # Check if Pydantic is v2
    if hasattr(PydanticBaseModel, "model_dump"):
        class BaseModel(PydanticBaseModel):
            pass
        Field = PydanticField
    else:
        # Pydantic v1 compatibility adapter
        class BaseModel(PydanticBaseModel):
            def model_dump(self, *args, **kwargs) -> Dict[str, Any]:
                return self.dict(*args, **kwargs)
            
            @classmethod
            def model_validate(cls, obj: Any, *args, **kwargs) -> "BaseModel":
                return cls.parse_obj(obj, *args, **kwargs)
        Field = PydanticField
except ImportError:
    HAS_PYDANTIC = False
    
    # Mock BaseModel fallback to prevent system crash
    class BaseModel:
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)
        
        def model_dump(self) -> Dict[str, Any]:
            res = {}
            for k, v in self.__dict__.items():
                if k.startswith('_'):
                    continue
                if isinstance(v, BaseModel):
                    res[k] = v.model_dump()
                elif isinstance(v, list):
                    res[k] = [item.model_dump() if isinstance(item, BaseModel) else item for item in v]
                elif isinstance(v, dict):
                    res[k] = {key: val.model_dump() if isinstance(val, BaseModel) else val for key, val in v.items()}
                else:
                    res[k] = v
            return res
            
        def dict(self) -> Dict[str, Any]:
            return self.model_dump()
            
        @classmethod
        def model_validate(cls, obj: Any) -> "BaseModel":
            if isinstance(obj, dict):
                return cls(**obj)
            return obj

    def Field(*args, **kwargs) -> Any:
        return kwargs.get("default", None)
