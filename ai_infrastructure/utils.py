import re
import json
from typing import Any, Optional

_FENCE_RE = re.compile(r'^```(?:json)?\s*|\s*```$', re.MULTILINE)

def strip_markdown_fences(text: str) -> str:
    """
    Remove leading/trailing markdown code fences that LLMs sometimes add around JSON outputs.
    """
    if not text:
        return ""
    return _FENCE_RE.sub('', text).strip()

def parse_json_safely(text: str) -> Optional[Any]:
    """
    Clean and parse JSON from LLM text output, handling markdown fences.
    """
    if not text:
        return None
    cleaned = strip_markdown_fences(text)
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return None
