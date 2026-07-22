from typing import Any, Dict, Type, Callable
from ai_infrastructure.providers.base import AbstractAIProvider
from ai_infrastructure.providers.gemini import GeminiProvider

_registry: Dict[str, Any] = {}
_factories: Dict[str, Callable[[], Any]] = {}

def register_provider(interface_cls: Type, provider_instance: Any) -> None:
    """Register a concrete provider instance for an interface class."""
    _registry[interface_cls.__name__] = provider_instance

def register_factory(interface_cls: Type, factory_func: Callable[[], Any]) -> None:
    """Register a callable factory to generate a provider instance when needed."""
    _factories[interface_cls.__name__] = factory_func

def get_provider(interface_cls: Type) -> Any:
    """Retrieve the registered instance or invoke factory to resolve interface dependency."""
    key = interface_cls.__name__
    if key in _registry:
        return _registry[key]
    if key in _factories:
        instance = _factories[key]()
        _registry[key] = instance
        return instance
    
    # Standard fallback resolutions
    if interface_cls == AbstractAIProvider:
        instance = GeminiProvider()
        _registry[key] = instance
        return instance
        
    raise ValueError(f"No provider or factory registered for interface: {key}")

def get_ai_provider() -> AbstractAIProvider:
    """Convenience getter for the AbstractAIProvider."""
    return get_provider(AbstractAIProvider)

def reset_registry() -> None:
    """Reset all registered bindings (useful for testing cleanups)."""
    _registry.clear()
    _factories.clear()
