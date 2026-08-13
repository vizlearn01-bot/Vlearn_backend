"""
SVG Validator, Sanitizer, and LessonAsset File Storage Helper.

Provides security validation and sanitization for programmatically generated
SVG diagrams, and standard file persistence into Django's LessonAsset.file storage.
"""

import re
import uuid
from typing import Tuple, Optional, Dict, Any
from django.core.files.base import ContentFile
from curriculum.models import Lesson, LessonAsset


# Dangerous SVG patterns for security sanitization
_SCRIPT_TAG_REGEX = re.compile(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', re.IGNORECASE | re.DOTALL)
_EVENT_HANDLER_REGEX = re.compile(r'\s+on[a-z]+\s*=\s*(?:"[^"]*"|\'[^\']*\'|[^\s>]+)', re.IGNORECASE)
_FOREIGNOBJECT_REGEX = re.compile(r'<foreignObject\b[^<]*(?:(?!<\/foreignObject>)<[^<]*)*<\/foreignObject>', re.IGNORECASE | re.DOTALL)
_DANGEROUS_PROTOCOLS_REGEX = re.compile(r'(?:href|xlink:href)\s*=\s*["\']\s*(?:javascript:|data:text\/html)[^"\']*["\']', re.IGNORECASE)
_STYLE_EXPRESSION_REGEX = re.compile(r'(?:expression\s*\(|javascript:|@import)', re.IGNORECASE)


def validate_svg_structure(svg_code: str) -> Tuple[bool, str]:
    """
    Validates that the input string is a structurally complete SVG document.
    Returns (is_valid, error_message).
    """
    if not svg_code or not isinstance(svg_code, str):
        return False, "SVG content must be a non-empty string."

    stripped = svg_code.strip()

    # Strip XML declaration if present
    if stripped.startswith("<?xml"):
        xml_end = stripped.find("?>")
        if xml_end != -1:
            stripped = stripped[xml_end + 2:].strip()

    # Strip leading comments/DOCTYPE if present
    while stripped.startswith("<!--") or stripped.startswith("<!DOCTYPE"):
        if stripped.startswith("<!--"):
            comment_end = stripped.find("-->")
            if comment_end != -1:
                stripped = stripped[comment_end + 3:].strip()
            else:
                break
        elif stripped.startswith("<!DOCTYPE"):
            doctype_end = stripped.find(">")
            if doctype_end != -1:
                stripped = stripped[doctype_end + 1:].strip()
            else:
                break

    if not stripped.startswith("<svg"):
        return False, "SVG must start with an '<svg' root element."

    if not stripped.endswith("</svg>"):
        return False, "SVG must terminate with a '</svg>' closing tag."

    if len(stripped) < 30:
        return False, "SVG content is too short to be a valid visual."

    return True, ""


def sanitize_svg(svg_code: str) -> str:
    """
    Sanitizes SVG content by removing executable scripts, event handlers,
    foreignObjects, and dangerous URL protocols.
    """
    if not svg_code:
        return ""

    sanitized = svg_code
    sanitized = _SCRIPT_TAG_REGEX.sub('', sanitized)
    sanitized = _EVENT_HANDLER_REGEX.sub('', sanitized)
    sanitized = _FOREIGNOBJECT_REGEX.sub('', sanitized)
    sanitized = _DANGEROUS_PROTOCOLS_REGEX.sub('', sanitized)
    sanitized = _STYLE_EXPRESSION_REGEX.sub('', sanitized)

    return sanitized.strip()


def validate_and_sanitize_svg(svg_code: str) -> Tuple[bool, str, Optional[str]]:
    """
    Validates structure and sanitizes SVG.
    Returns (is_valid, sanitized_svg, error_message).
    """
    is_valid, err = validate_svg_structure(svg_code)
    if not is_valid:
        return False, svg_code, err

    sanitized = sanitize_svg(svg_code)

    # Re-verify structure after sanitization
    is_valid_post, err_post = validate_svg_structure(sanitized)
    if not is_valid_post:
        return False, sanitized, f"Sanitization produced invalid SVG structure: {err_post}"

    return True, sanitized, None


def save_svg_as_lesson_asset(
    lesson: Lesson,
    svg_code: str,
    title: str = "",
    description: str = "",
    metadata: Optional[Dict[str, Any]] = None,
    alt_text: str = ""
) -> Tuple[Optional[LessonAsset], Optional[str]]:
    """
    Validates, sanitizes, and persists an SVG as a LessonAsset file.
    Uses LessonAsset.file (FileField -> upload_to='lesson_assets/').
    
    Returns (lesson_asset, error_message).
    """
    is_valid, sanitized_svg, error = validate_and_sanitize_svg(svg_code)
    if not is_valid:
        return None, error

    asset_meta = {
        'enrichment_agent': True,
        'render_format': 'svg',
        'provenance': 'VisualReasoner',
        'alt_text': alt_text or title or 'Generated diagram',
    }
    if metadata:
        asset_meta.update(metadata)

    asset = LessonAsset(
        lesson=lesson,
        asset_type='diagram',
        source_type='ai_generated',
        storage_type='file',
        status='attached',
        title=title or alt_text or 'Generated Diagram',
        description=description,
        metadata=asset_meta,
    )

    filename = f"diagram_{lesson.id}_{uuid.uuid4().hex[:8]}.svg"
    asset.file.save(filename, ContentFile(sanitized_svg.encode('utf-8')), save=True)

    return asset, None
