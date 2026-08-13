"""
VLearn Form 4 Physics — Topic 1: Thin Lenses
Ingestion Script

Source: lessons.md / Lessons.md
Grade: Form 4
Subject: Physics
Curriculum: 844 (Kenyan 8-4-4 Secondary Curriculum)

Pedagogical Architecture:
  3 Learning Units / Modules × 14–16 pages each
  - Module 1.1: Lens Types, Geometric Properties, and Image Formation (14 pages)
  - Module 1.2: Lens Formula, Magnification, and Focal Length Experiments (16 pages)
  - Module 1.3: Optical Instruments, the Eye, and Corrective Spectacles (15 pages)

Features:
  - Adaptive calculation framework (concise 5-step for foundation, full 8-step for complex/multi-step)
  - Dedicated Physics Graph Strategy (1/v vs 1/u, gradient, intercepts, physical deductions)
  - Multi-tier worked examples (Level 1 to Level 5)
  - Laboratory experimental method (Aim, apparatus, variables, step-by-step procedure, errors)
  - Semantic visual opportunity blocks without creating empty placeholder LessonAssets
  - Clean student-facing titles & captions with zero developer terminology leaks
  - Idempotent and safe updates (preserves existing enriched assets unless --replace flag is used)

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/ingest_form4_physics.py
  Optional flag: --replace (clears and rebuilds all blocks for these lessons fresh)
"""

import os
import sys
import uuid
import re
import argparse
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.db import transaction
from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    LearningUnit, Lesson, LessonBlock, LessonAsset
)

def clean_text(raw_str):
    """Remove source citation brackets like [184], [32], [image_0] and clean whitespace."""
    if not isinstance(raw_str, str):
        return raw_str
    # Remove bracket citations like [184], [32, 33], [image_0]
    cleaned = re.sub(r'\[(?:\d+|image_\d+|[\d,\s]+)\]', '', raw_str)
    # Clean double spaces
    cleaned = re.sub(r'[ \t]+', ' ', cleaned)
    return cleaned.strip()

def clean_content_dict(data):
    """Recursively clean text within content dicts or lists."""
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, list):
        return [clean_content_dict(item) for item in data]
    elif isinstance(data, dict):
        return {k: clean_content_dict(v) for k, v in data.items()}
    return data


# =============================================================================
# MODULE 1.1 DATA — Lens Types, Geometric Properties, and Image Formation
# =============================================================================
MODULE_1_1 = {
    "unit_name": "Module 1.1: Lens Types, Geometric Properties, and Image Formation",
    "unit_order": 1,
    "lesson_title": "Lens Types, Geometric Properties, and Image Formation",
    "cards": [
        # Page 1: Hook & Learning Goals
        {
            "page_number": 1,
            "page_title": "Lenses in Daily Life: Bending Light to Create Images",
            "block_type": "learning_goal",
            "component_type": "learning_goal",
            "content": {
                "text": (
                    "Have you ever noticed how a clear water droplet on a leaf makes the leaf's fine veins appear "
                    "vastly magnified, or how a drinking straw in a glass of water appears bent or broken at the surface? "
                    "These phenomena occur because of refraction—the bending of light as it passes between transparent media.\n\n"
                    "A lens is a carefully crafted piece of transparent glass or plastic designed to refract light rays systematically, "
                    "converging or diverging them to form clear images. From smartphone cameras and spectacles to cinema projectors and "
                    "research telescopes, lenses are foundational to modern visual technology.\n\n"
                    "By the end of this lesson, you will be able to:\n"
                    "- Distinguish between converging (convex) and diverging (concave) lens geometries\n"
                    "- Identify key geometric landmarks: optical centre, principal axis, principal focus, and focal length\n"
                    "- Construct ray diagrams using the three principal rays\n"
                    "- Predict the nature, size, and position of images formed by convex and concave lenses\n"
                    "- Differentiate with precision between real and virtual images"
                )
            }
        },
        # Page 2: Lens Geometries & Classification
        {
            "page_number": 2,
            "page_title": "Classifying Thin Lenses: Converging vs. Diverging",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "Thin lenses are broadly categorized into two families based on how their physical thickness varies "
                    "from the centre to the outer edges:\n\n"
                    "### 1. Convex (Converging) Lenses\n"
                    "A convex lens is **thicker at its centre than at its edges**. When a parallel beam of light passes through a convex lens, "
                    "the refracted rays bend inwards and meet (converge) at a single real focal point.\n\n"
                    "- **Biconvex**: Both surfaces curve outwards.\n"
                    "- **Plano-convex**: One surface is flat (planar) and the other curves outwards.\n"
                    "- **Converging Meniscus**: One surface curves inwards and the other outwards, but the centre remains thicker than the rim.\n\n"
                    "### 2. Concave (Diverging) Lenses\n"
                    "A concave lens is **thicker at its edges than at its centre**. When parallel light enters a concave lens, "
                    "the refracted rays spread outwards (diverge) as though originating from a virtual focus behind the lens.\n\n"
                    "- **Biconcave**: Both surfaces curve inwards.\n"
                    "- **Plano-concave**: One surface is flat and the other curves inwards.\n"
                    "- **Diverging Meniscus**: One surface curves outwards and the other inwards, but the edges remain thicker than the centre."
                )
            }
        },
        {
            "page_number": 2,
            "page_title": "Converging and Diverging Lens Geometries",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Cross-sectional geometries comparing converging (biconvex, plano-convex, converging meniscus) and diverging (biconcave, plano-concave, diverging meniscus) lenses.",
                "instruction": (
                    "Draw 6 cross-sectional lens profiles grouped into two rows: "
                    "Top row (Converging, thicker centre): Biconvex, Plano-convex, Converging Meniscus. "
                    "Bottom row (Diverging, thicker edges): Biconcave, Plano-concave, Diverging Meniscus. "
                    "Use clear labels, light blue glass shading, and central thickness indicators."
                )
            }
        },
        # Page 3: Geometric Landmarks
        {
            "page_number": 3,
            "page_title": "Geometric Landmarks of a Thin Lens",
            "block_type": "comparison_table",
            "component_type": "comparison_table",
            "content": {
                "headers": ["Landmark / Property", "Symbol", "Physical Definition", "Key Optical Rule"],
                "rows": [
                    ["Optical Centre", "$O$", "The exact geometric centre of the lens.", "Any ray passing through $O$ continues straight without deflection."],
                    ["Centre of Curvature", "$C, C_1$", "The geometric centre of the spherical glass surface of which the lens forms a part.", "Each lens has two centres of curvature corresponding to its two curved faces."],
                    ["Principal Axis", "—", "The imaginary line passing perpendicularly through the optical centre $O$.", "Serves as the reference baseline for all distances and heights."],
                    ["Principal Focus", "$F$", "Convex: The point where incident parallel rays converge. Concave: The point from which parallel rays appear to diverge.", "Convex focus is Real (rays physically cross). Concave focus is Virtual (rays only appear to meet)."],
                    ["Focal Length", "$f$", "The distance along the principal axis between the optical centre $O$ and principal focus $F$.", "Dependent on the lens material's refractive index and curvature radii."]
                ]
            }
        },
        {
            "page_number": 3,
            "page_title": "Curvature Geometry and Landmarks of a Biconvex Lens",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Geometric construction showing two intersecting spheres defining a biconvex lens with optical centre O, principal axis, centres of curvature C, and focal points F.",
                "instruction": (
                    "Construct two overlapping transparent spheres illustrating how their shared intersection forms a biconvex lens. "
                    "Label centres of curvature C1 and C2, the horizontal principal axis, optical centre O, and the focal lengths f on both sides."
                )
            }
        },
        # Page 4: The Three Principal Rays
        {
            "page_number": 4,
            "page_title": "The Three Principal Rays of Geometric Ray Tracing",
            "block_type": "step_process",
            "component_type": "step_process",
            "content": {
                "title": "Standard Rules for Ray Construction",
                "steps": [
                    "**Ray 1 (The Parallel Ray):** A ray travelling parallel to the principal axis refracts through the principal focus $F$ on the opposite side (convex lens) or diverges outwards as if originating from the focus on the incoming side (concave lens).",
                    "**Ray 2 (The Optical Centre Ray):** A ray passing directly through the optical centre $O$ travels straight through completely undeflected and un-deviated.",
                    "**Ray 3 (The Focal Ray):** A ray passing through (or directed towards) the principal focus $F$ refracts through the lens and emerges travelling completely parallel to the principal axis.",
                    "**Image Location Rule:** To locate an image, construct any two of these three principal rays from the top of the object. The intersection of the refracted rays (or their backward dashed projections) defines the image position."
                ]
            }
        },
        {
            "page_number": 4,
            "page_title": "Principal Focus and Ray Refraction in Converging and Diverging Lenses",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Side-by-side comparison of parallel rays converging at a real focus F in a convex lens versus diverging from a virtual focus F in a concave lens.",
                "instruction": (
                    "Two side-by-side ray diagrams: "
                    "(Left) Convex lens with incoming parallel rays converging to real focal point F on the right. "
                    "(Right) Concave lens with incoming parallel rays diverging outwards, with dashed projection lines meeting at virtual focus F on the left."
                )
            }
        },
        # Page 5: Convex Lens: Object within Focus and at Focus
        {
            "page_number": 5,
            "page_title": "Convex Lens: Object at $u < f$ and $u = f$",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### Case 1: Object Placed Inside the Focal Point ($u < f$)\n"
                    "- **Ray Construction**: The parallel ray refracts through $F$ on the right, while the central ray passes undeflected through $O$. On the right, these rays diverge. Projecting them backward with dashed lines to the left reveals where they meet behind the object.\n"
                    "- **Image Nature**: **Virtual** (formed by extrapolated rays; cannot be projected on a screen).\n"
                    "- **Orientation**: **Erect (upright)**.\n"
                    "- **Size**: **Magnified** ($m > 1$).\n"
                    "- **Real-World Application**: **Simple magnifying glass / reading lens**.\n\n"
                    "### Case 2: Object Placed Exactly at the Focal Point ($u = f$)\n"
                    "- **Ray Construction**: The refracted rays emerge completely parallel to each other. Because parallel rays never intersect, the image is formed at infinity.\n"
                    "- **Image Nature**: **Real (at infinity)**, **Inverted**, **Highly Magnified**.\n"
                    "- **Real-World Application**: **Searchlight collimators and spotlight projectors** (producing non-diverging parallel light beams)."
                )
            }
        },
        {
            "page_number": 5,
            "page_title": "Ray Diagram: Object Placed Inside the Focal Length ($u < f$)",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Ray diagram showing a convex lens forming a virtual, upright, and magnified image behind the object when u < f.",
                "instruction": (
                    "Draw convex lens on principal axis with object arrow between O and F (u < f). "
                    "Trace parallel ray refracting through F, and centre ray through O. "
                    "Draw dashed backward projections intersecting on the left side to form a large upright dashed image arrow. Label: Virtual, Erect, Magnified."
                )
            }
        },
        # Page 6: Convex Lens: Object between F & 2F and at 2F
        {
            "page_number": 6,
            "page_title": "Convex Lens: Object at $f < u < 2f$ and $u = 2f$",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### Case 3: Object Placed Between $F$ and $2F$ ($f < u < 2f$)\n"
                    "- **Ray Construction**: The parallel ray passes through $F$ on the right, and the central ray passes through $O$. The rays physically meet and cross below the principal axis **beyond $2F$**.\n"
                    "- **Image Position**: Beyond $2F$ on the opposite side ($v > 2f$).\n"
                    "- **Image Nature**: **Real** (can be captured on a screen), **Inverted**, **Magnified** ($m > 1$).\n"
                    "- **Real-World Application**: **Slide projectors, cinema movie projectors, and photographic enlargers**.\n\n"
                    "### Case 4: Object Placed Exactly at $2F$ ($u = 2f$)\n"
                    "- **Ray Construction**: The refracted rays intersect symmetrically at the $2F$ mark on the opposite side ($v = 2f$).\n"
                    "- **Image Position**: Exactly at $2F$ on the opposite side.\n"
                    "- **Image Nature**: **Real**, **Inverted**, **Same Size as Object** ($m = 1$).\n"
                    "- **Real-World Application**: **Inverting prisms and terrestrial telescope relay systems** (inverting an image without altering its scale)."
                )
            }
        },
        {
            "page_number": 6,
            "page_title": "Ray Diagram: Object Placed Between F and 2F ($f < u < 2f$)",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Ray diagram showing a convex lens forming a real, inverted, and magnified image beyond 2F on the opposite side when f < u < 2f.",
                "instruction": (
                    "Draw convex lens on principal axis with object arrow between F and 2F. "
                    "Trace parallel ray through right F and central ray through O, intersecting beyond 2F on the right. "
                    "Draw inverted solid arrow image. Label: Real, Inverted, Magnified."
                )
            }
        },
        # Page 7: Convex Lens: Object beyond 2F and at Infinity
        {
            "page_number": 7,
            "page_title": "Convex Lens: Object at $u > 2f$ and $u \\approx \\infty$",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### Case 5: Object Placed Beyond $2F$ ($u > 2f$)\n"
                    "- **Ray Construction**: The refracted rays cross between the focal point $F$ and $2F$ on the opposite side.\n"
                    "- **Image Position**: Between $F$ and $2F$ ($f < v < 2f$).\n"
                    "- **Image Nature**: **Real**, **Inverted**, **Diminished** ($m < 1$).\n"
                    "- **Real-World Application**: **Standard photographic camera and the human eye** (capturing large distant scenes onto a compact sensor/retina).\n\n"
                    "### Case 6: Object Placed at Infinity ($u \\approx \\infty$)\n"
                    "- **Ray Construction**: Incoming rays arrive as parallel lines (which may be tilted relative to the principal axis). After refraction, they meet in the **focal plane** (the vertical plane at distance $f$).\n"
                    "- **Image Position**: In the focal plane at $F$.\n"
                    "- **Image Nature**: **Real**, **Inverted**, **Highly Diminished (Point Image)**.\n"
                    "- **Real-World Application**: **Astronomical telescope objective lens** (focusing light from distant stars)."
                )
            }
        },
        {
            "page_number": 7,
            "page_title": "Ray Diagram: Object Placed Beyond 2F ($u > 2f$)",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Ray diagram showing a convex lens forming a real, inverted, and diminished image between F and 2F on the opposite side when u > 2f.",
                "instruction": (
                    "Draw convex lens on principal axis with object arrow placed to the left of 2F. "
                    "Trace parallel ray through F and centre ray through O, meeting between F and 2F on the right side. "
                    "Draw a smaller, solid inverted arrow image. Label: Real, Inverted, Diminished."
                )
            }
        },
        # Page 8: Diverging (Concave) Lens Image Formation
        {
            "page_number": 8,
            "page_title": "Image Formation by a Diverging (Concave) Lens",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "Unlike a convex lens, which produces six distinct image configurations depending on object distance, "
                    "a **diverging (concave) lens behaves identically for all object positions** in front of it:\n\n"
                    "### Ray Construction for a Concave Lens:\n"
                    "1. Draw a ray from the top of the object parallel to the principal axis. At the lens, refract it bending outwards (diverging) such that its backward extension aligns with the virtual focus $F$ on the object side.\n"
                    "2. Draw a second ray straight through the optical centre $O$ without deviation.\n"
                    "3. The refracted parallel ray spreads away into space on the right, so it cannot physically meet the central ray. Projecting the refracted parallel ray backward (dashed line) intersects the optical centre ray on the left.\n\n"
                    "### Universal Image Characteristics (For ALL Object Positions):\n"
                    "- **Position**: Between the principal focus $F$ and the lens ($v < f$), on the **same side as the object**.\n"
                    "- **Nature**: **Virtual** (cannot be formed on a screen).\n"
                    "- **Orientation**: **Erect (upright)**.\n"
                    "- **Size**: **Diminished** (always smaller than the object, $m < 1$).\n\n"
                    "**Primary Real-World Applications**: Spectacles for correcting short-sightedness (myopia), peep-holes in security doors, and wide-angle viewfinders."
                )
            }
        },
        {
            "page_number": 8,
            "page_title": "Ray Diagram: Image Formation by a Concave (Diverging) Lens",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Ray diagram illustrating how a concave lens forms an upright, virtual, and diminished image on the object side for any object position.",
                "instruction": (
                    "Draw a concave lens on the principal axis. Place an object arrow on the left. "
                    "Trace parallel ray diverging upwards with dashed backward projection to left F. "
                    "Trace central ray straight through O. "
                    "Draw small dashed upright image where the dashed projection crosses the central ray between O and F. Label: Virtual, Erect, Diminished."
                )
            }
        },
        # Page 9: Comparative Analysis: Real vs Virtual Images
        {
            "page_number": 9,
            "page_title": "Comparative Analysis: Real vs. Virtual Images",
            "block_type": "comparison_table",
            "component_type": "comparison_table",
            "content": {
                "headers": ["Property / Dimension", "Real Image", "Virtual Image"],
                "rows": [
                    ["Physical Ray Behavior", "Formed by light rays that physically intersect and cross at a point.", "Formed by diverging rays that only appear to intersect when extrapolated backward."],
                    ["Screen Projection", "Can be projected onto a physical screen or piece of paper.", "Cannot be projected onto a screen."],
                    ["Diagrammatic Representation", "Drawn with solid, continuous lines.", "Drawn with dashed / dotted projection lines."],
                    ["Orientation to Object", "Always inverted (upside down).", "Always erect (upright)."],
                    ["Direct Human Viewing", "Viewable on a screen or by placing eye beyond the image location.", "Viewable only by looking directly through the lens toward the object."],
                    ["Lens Formations", "Formed only by convex lenses when $u > f$.", "Formed by concave lenses (always) and convex lenses (when $u < f$)."]
                ]
            }
        },
        # Page 10: Interactive Simulation / Sandbox Spec
        {
            "page_number": 10,
            "page_title": "Interactive Exploration: The Thin Lens Sandbox",
            "block_type": "prediction",
            "component_type": "prediction",
            "content": {
                "text": (
                    "**Think & Predict Before Exploring:**\n\n"
                    "Imagine you have a convex lens with a focal length of $f = 10\\text{ cm}$. "
                    "An illuminated object arrow is placed at $u = 35\\text{ cm}$ (beyond $2F$). "
                    "If you slowly drag the object closer to the lens until it sits at $u = 15\\text{ cm}$ (between $F$ and $2F$):\n\n"
                    "1. What will happen to the image distance $v$?\n"
                    "2. What will happen to the image size (magnification $m$)?\n"
                    "3. Will the image remain real or become virtual?"
                )
            }
        },
        {
            "page_number": 10,
            "page_title": "Interactive Lens Ray Tracing Simulator",
            "block_type": "suggested_simulation",
            "component_type": "suggested_simulation",
            "content": {
                "text": "Interactive dynamic ray-tracing simulation allowing students to toggle lens type (convex/concave), adjust focal length f, drag object position u and height, and observe real-time ray refraction and image metrics.",
                "instruction": "Simulation Key: optics. Allows continuous manipulation of focal length slider (5cm - 30cm) and object distance slider (2cm - 100cm) with active readouts of image distance v, magnification m, and real/virtual status."
            }
        },
        {
            "page_number": 10,
            "page_title": "Reflecting on Lens Behavior",
            "block_type": "reflection",
            "component_type": "reflection",
            "content": {
                "text": (
                    "As you bring an object from infinity closer and closer to a convex lens, the real image moves further and further away "
                    "and grows larger and larger. The exact moment the object crosses inside the focal point ($u < f$), the rays on the right diverge, "
                    "and the image abruptly switches from a far-away inverted real image to a close-up upright magnified virtual image!"
                )
            }
        },
        # Page 11: Common Misconceptions & Traps
        {
            "page_number": 11,
            "page_title": "Common Misconceptions in Lens Optics",
            "block_type": "common_misconception",
            "component_type": "common_misconception",
            "content": {
                "text": (
                    "### Misconception 1: \"A virtual image cannot be seen by the human eye because it cannot be projected on a screen.\"\n"
                    "**Scientific Correction**: While a virtual image cannot be captured on a flat paper screen, your eye can see it perfectly! "
                    "Your eye contains its own converging crystalline lens. When diverging rays from a virtual image enter your eye, your eye's lens "
                    "refracts them to converge on your retina, allowing you to clearly observe the virtual image (such as when looking into a magnifying glass).\n\n"
                    "### Misconception 2: \"If you cover the top half of a convex lens with black paper, only the bottom half of the image will form.\"\n"
                    "**Scientific Correction**: This is a major exam trap! Every single portion of a lens refracts light rays coming from every part of the object. "
                    "If you cover the top half of the lens, the **complete image is still formed in the exact same location and orientation**. However, because only "
                    "half as many light rays pass through the lens, the image will appear **dimmer (half the original brightness)**."
                )
            }
        },
        # Page 12: Knowledge Check (MCQ)
        {
            "page_number": 12,
            "page_title": "Check Your Understanding: Object Between F and 2F",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "A slide projector uses a convex lens of focal length $f = 10\\text{ cm}$. To project a sharp, magnified image of a slide onto a screen across the room, at which position should the slide be placed relative to the lens?",
                "options": [
                    "Inside the focal length ($u < 10\\text{ cm}$)",
                    "Between the focus and twice the focal length ($10\\text{ cm} < u < 20\\text{ cm}$)",
                    "Exactly at twice the focal length ($u = 20\\text{ cm}$)",
                    "Beyond twice the focal length ($u > 20\\text{ cm}$)"
                ],
                "answer": "B",
                "explanation": (
                    "To form a real, inverted, and magnified image on a distant screen ($v > 2f$), the object must be positioned between $F$ and $2F$ ($10\\text{ cm} < u < 20\\text{ cm}$). "
                    "Placing it inside $F$ would create a virtual image that cannot be captured on a screen, while placing it beyond $2F$ would create a diminished image."
                )
            }
        },
        # Page 13: Knowledge Check (True/False & Concept Diagnosis)
        {
            "page_number": 13,
            "page_title": "Check Your Understanding: Concave Lens Properties",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "true_false",
                "question": "A single diverging (concave) lens can produce a real, magnified image if the object is placed sufficiently close to the lens surface.",
                "options": ["True", "False"],
                "answer": "False",
                "explanation": (
                    "False. A diverging (concave) lens always diverges incident light rays outward. For all real object positions anywhere along the principal axis, "
                    "a concave lens exclusively produces a virtual, erect, and diminished image located between the focus and the lens."
                )
            }
        },
        # Page 14: Summary & Key Takeaways
        {
            "page_number": 14,
            "page_title": "Module 1.1 Summary: Geometric Optics of Thin Lenses",
            "block_type": "summary",
            "component_type": "summary",
            "content": {
                "text": (
                    "### Summary of Core Principles:\n"
                    "- **Lens Families**: Convex lenses are thicker at the centre and converge parallel light to a real focus ($+f$). Concave lenses are thicker at the edges and diverge light from a virtual focus ($-f$).\n"
                    "- **Three Principal Rays**: (1) Parallel ray refracts through focus; (2) Centre ray passes straight through $O$; (3) Focal ray refracts parallel to principal axis.\n"
                    "- **Convex Lens Cases**: Position determines nature—$u < f$ (Virtual, Erect, Magnified); $u = f$ (At infinity); $f < u < 2f$ (Real, Inverted, Magnified); $u = 2f$ (Real, Inverted, Same size); $u > 2f$ (Real, Inverted, Diminished); $u = \\infty$ (Real, Inverted, Point image at $F$).\n"
                    "- **Concave Universality**: Always forms a virtual, erect, diminished image between $F$ and the lens.\n"
                    "- **Real vs. Virtual**: Real images are formed by intersecting rays and can be projected on a screen; virtual images are formed by diverging rays and can only be seen by looking through the optical system."
                )
            }
        },
        {
            "page_number": 14,
            "page_title": "Core Takeaways on Lens Geometry",
            "block_type": "key_takeaway",
            "component_type": "key_takeaway",
            "content": {
                "text": "Convex lenses transform light dynamically across 6 distinct positions, while concave lenses consistently produce upright, diminished virtual images for all positions."
            }
        }
    ]
}


# =============================================================================
# MODULE 1.2 DATA — Lens Formula, Magnification, and Focal Length Experiments
# =============================================================================
MODULE_1_2 = {
    "unit_name": "Module 1.2: Lens Formula, Magnification, and Focal Length Experiments",
    "unit_order": 2,
    "lesson_title": "Lens Formula, Magnification, and Focal Length Experiments",
    "cards": [
        # Page 1: Hook & Learning Goals
        {
            "page_number": 1,
            "page_title": "From Geometric Diagrams to Mathematical Precision",
            "block_type": "learning_goal",
            "component_type": "learning_goal",
            "content": {
                "text": (
                    "While geometric ray diagrams provide visual intuition, optical engineers designing smartphone cameras, "
                    "laser microscopes, and prescription glasses require exact mathematical models to predict image positions down to fractions of a millimetre.\n\n"
                    "In this module, you will master the fundamental quantitative laws of thin lenses, understand how sign conventions prevent algebraic errors, "
                    "and discover how experimental physics allows us to determine focal lengths in the laboratory using linear graphs.\n\n"
                    "By the end of this lesson, you will be able to:\n"
                    "- Calculate linear magnification ($m$) using height and distance ratios\n"
                    "- Apply the lens formula $\\frac{1}{f} = \\frac{1}{u} + \\frac{1}{v}$ under the 'Real-is-Positive' sign convention\n"
                    "- Calculate the optical power of a lens in diopters ($D$)\n"
                    "- Structure multi-step calculation problems using the VLearn 8-step reasoning framework\n"
                    "- Describe the laboratory method for determining focal length and interpret linear reciprocal graphs"
                )
            }
        },
        # Page 2: Linear Magnification
        {
            "page_number": 2,
            "page_title": "Linear Magnification: Quantifying Image Scaling",
            "block_type": "formula_breakdown",
            "component_type": "formula_breakdown",
            "content": {
                "formula": "$$\\text{Magnification } (m) = \\frac{\\text{Height of Image } (h_i)}{\\text{Height of Object } (h_o)} = \\frac{\\text{Image Distance } (v)}{\\text{Object Distance } (u)}$$",
                "content": (
                    "Linear magnification ($m$) is a dimensionless ratio comparing the scale of an image to its source object.\n\n"
                    "| Symbol | Meaning | Standard Units |\n"
                    "|---|---|---|\n"
                    "| $m$ | Linear magnification | Dimensionless (pure ratio) |\n"
                    "| $h_i$ | Height of the image | $\\text{cm}$ or $\\text{m}$ |\n"
                    "| $h_o$ | Height of the object | $\\text{cm}$ or $\\text{m}$ |\n"
                    "| $v$ | Distance from lens optical centre to image | $\\text{cm}$ or $\\text{m}$ |\n"
                    "| $u$ | Distance from lens optical centre to object | $\\text{cm}$ or $\\text{m}$ |\n\n"
                    "### Physical Meaning of the Magnification Value:\n"
                    "- **If $m > 1$**: The image is **magnified** (larger than object).\n"
                    "- **If $m = 1$**: The image is the **same size** as the object (occurs at $u = 2f$).\n"
                    "- **If $0 < m < 1$**: The image is **diminished** (smaller than object)."
                )
            }
        },
        # Page 3: The Lens Formula & Sign Conventions
        {
            "page_number": 3,
            "page_title": "The Lens Formula & The 'Real-is-Positive' Sign Convention",
            "block_type": "formula_breakdown",
            "component_type": "formula_breakdown",
            "content": {
                "formula": "$$\\frac{1}{f} = \\frac{1}{u} + \\frac{1}{v}$$",
                "content": (
                    "The lens formula relates the focal length ($f$), object distance ($u$), and image distance ($v$) for any thin spherical lens.\n\n"
                    "### The 'Real-is-Positive' Sign Convention Rules:\n\n"
                    "1. **Focal Length ($f$):**\n"
                    "   - Converging (Convex) lens has a real focus $\\rightarrow \\mathbf{+f}$ (Positive).\n"
                    "   - Diverging (Concave) lens has a virtual focus $\\rightarrow \\mathbf{-f}$ (Negative).\n\n"
                    "2. **Object Distance ($u$):**\n"
                    "   - Real object placed in front of the lens $\\rightarrow \\mathbf{+u}$ (Positive).\n\n"
                    "3. **Image Distance ($v$):**\n"
                    "   - Real image (formed by converging rays on the opposite side) $\\rightarrow \\mathbf{+v}$ (Positive).\n"
                    "   - Virtual image (formed by diverging rays on the same side) $\\rightarrow \\mathbf{-v}$ (Negative)."
                )
            }
        },
        # Page 4: Power of a Lens
        {
            "page_number": 4,
            "page_title": "Optical Power of a Lens",
            "block_type": "formula_breakdown",
            "component_type": "formula_breakdown",
            "content": {
                "formula": "$$\\text{Power } (P) = \\frac{1}{f \\text{ (in metres)}}$$",
                "content": (
                    "The optical power of a lens measures its refractive strength—its ability to bend light rays.\n"
                    "A lens with a short focal length bends light sharply and has high power, while a lens with a long focal length bends light gently and has low power.\n\n"
                    "| Quantity | Symbol | SI Unit | Note |\n"
                    "|---|---|---|---|\n"
                    "| Power | $P$ | Diopter ($\\text{D}$ or $\\text{m}^{-1}$) | $1\\text{ D} = 1\\text{ m}^{-1}$ |\n"
                    "| Focal Length | $f$ | Metres ($\\text{m}$) | **Must be converted from cm to m!** |\n\n"
                    "### Sign Rules for Power:\n"
                    "- Converging (Convex) lenses have positive power: $\\mathbf{+P}$ (e.g., $+5.0\\text{ D}$).\n"
                    "- Diverging (Concave) lenses have negative power: $\\mathbf{-P}$ (e.g., $-2.5\\text{ D}$)."
                )
            }
        },
        {
            "page_number": 4,
            "page_title": "Mandatory Unit Conversion Warning",
            "block_type": "callout",
            "component_type": "callout",
            "content": {
                "text": (
                    "**Crucial Exam Pitfall:** If a lens has a focal length of $f = 20\\text{ cm}$, calculating $P = \\frac{1}{20} = 0.05\\text{ D}$ is **completely wrong**! "
                    "You must first convert the focal length to metres: $f = 20\\text{ cm} = 0.20\\text{ m}$. "
                    "Then: $P = \\frac{1}{0.20\\text{ m}} = \\mathbf{+5.0\\text{ D}}$."
                )
            }
        },
        # Page 5: 8-Step Reasoning Methodology
        {
            "page_number": 5,
            "page_title": "The VLearn 8-Step Analytical Problem-Solving Method",
            "block_type": "step_process",
            "component_type": "step_process",
            "content": {
                "title": "Systematic Analytical Reasoning Pipeline",
                "steps": [
                    "**Step 1 — Identify Goal:** State clearly what physical quantity is required (e.g., image position $v$, object distance $u$, focal length $f$, or magnification $m$).",
                    "**Step 2 — List Given Quantities with Units:** Extract all stated variables, convert units to consistency (cm or m), and assign the correct algebraic sign using 'Real-is-Positive'.",
                    "**Step 3 — State Governing Equation:** Write the lens equation $\\frac{1}{f} = \\frac{1}{u} + \\frac{1}{v}$ or magnification ratio $m = \\frac{v}{u}$.",
                    "**Step 4 — Rearrange Equation:** Isolate the target unknown variable symbolically before inserting numbers.",
                    "**Step 5 — Substitute Values:** Plug in numerical values with their positive/negative signs cleanly.",
                    "**Step 6 — Calculate Arithmetic:** Perform step-by-step arithmetic using common denominators or decimals.",
                    "**Step 7 — State Final Answer with SI Units:** Express the result clearly with appropriate physical units (cm, m, or D).",
                    "**Step 8 — Physical Reasonableness Check:** Validate whether the calculated result agrees with qualitative ray-tracing rules (e.g., if object is between $F$ and $2F$, is $v > 2f$ and positive?)."
                ]
            }
        },
        # Page 6: Worked Example Level 1
        {
            "page_number": 6,
            "page_title": "Example 1: Direct Substitution (Image Position)",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A real object is placed $12\\text{ cm}$ in front of a converging lens of focal length $10\\text{ cm}$. "
                    "Find the position and nature of the image formed."
                ),
                "steps": [
                    "**Given & Required:** Converging lens focal length $f = +10\\text{ cm}$ (positive for convex); Object distance $u = +12\\text{ cm}$ (real object). Required: Image distance $v$.",
                    "**Governing Formula:** $$\\frac{1}{f} = \\frac{1}{u} + \\frac{1}{v}$$",
                    "**Rearranging for Unknown:** $$\\frac{1}{v} = \\frac{1}{f} - \\frac{1}{u}$$",
                    "**Substitution & Calculation:** $$\\frac{1}{v} = \\frac{1}{10} - \\frac{1}{12} = \\frac{6 - 5}{60} = \\frac{1}{60}$$ $$v = +60\\text{ cm}$$",
                    "**Answer & Physical Check:** The image distance is $\\mathbf{+60\\text{ cm}}$ (formed $60\\text{ cm}$ on the opposite side of the lens). Because $v$ is positive, the image is **real and inverted**. Since the object was between $F$ ($10\\text{ cm}$) and $2F$ ($20\\text{ cm}$), forming a real image beyond $2F$ ($60\\text{ cm} > 20\\text{ cm}$) is physically consistent!"
                ]
            }
        },
        # Page 7: Worked Example Level 2
        {
            "page_number": 7,
            "page_title": "Example 2: Equation Rearrangement (Virtual Image)",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "An object is placed in front of a converging lens of focal length $18\\text{ cm}$. "
                    "A virtual image is formed at a distance of $36\\text{ cm}$ from the lens. "
                    "Calculate the distance at which the object was placed."
                ),
                "steps": [
                    "**Given & Required:** Focal length $f = +18\\text{ cm}$; Virtual image distance $v = -36\\text{ cm}$ (negative for virtual image). Required: Object distance $u$.",
                    "**Governing Formula:** $$\\frac{1}{f} = \\frac{1}{u} + \\frac{1}{v} \\implies \\frac{1}{u} = \\frac{1}{f} - \\frac{1}{v}$$",
                    "**Substitution (Watch the Double Negative):** $$\\frac{1}{u} = \\frac{1}{18} - \\left(\\frac{1}{-36}\\right) = \\frac{1}{18} + \\frac{1}{36}$$",
                    "**Calculation:** $$\\frac{1}{u} = \\frac{2 + 1}{36} = \\frac{3}{36} = \\frac{1}{12} \\implies u = +12\\text{ cm}$$",
                    "**Answer & Physical Check:** The object distance is $\\mathbf{u = 12\\text{ cm}}$. A convex lens only forms a virtual image when the object is placed inside the focal length ($u < f$). Since $12\\text{ cm} < 18\\text{ cm}$, the result is physically verified!"
                ]
            }
        },
        # Page 8: Worked Example Level 3
        {
            "page_number": 8,
            "page_title": "Example 3: Multi-Step (Combining Magnification & Lens Equation)",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "The focal length of a converging lens is $10\\text{ cm}$. "
                    "How far should the lens be placed from an illuminated object to obtain an image that is magnified 5 times on a screen?"
                ),
                "steps": [
                    "**Goal:** Find object distance $u$.\n**Given:** $f = +10\\text{ cm}$, magnification $m = 5$. Since the image is formed on a screen, it must be a **real image**, meaning $v > 0$.",
                    "**Linking Equations:** $$m = \\frac{v}{u} \\implies v = 5u$$ $$\\frac{1}{f} = \\frac{1}{u} + \\frac{1}{v}$$",
                    "**Substitution & Simplification:** $$\\frac{1}{10} = \\frac{1}{u} + \\frac{1}{5u} = \\frac{5}{5u} + \\frac{1}{5u} = \\frac{6}{5u}$$",
                    "**Cross-Multiplication & Solution:** $$5u = 60 \\implies u = \\frac{60}{5} = \\mathbf{12\\text{ cm}}$$",
                    "**Physical Interpretation:** The lens must be placed $12\\text{ cm}$ from the object. To achieve a real, magnified image ($m = 5$), the object must lie between $F$ ($10\\text{ cm}$) and $2F$ ($20\\text{ cm}$), which matches our $12\\text{ cm}$ result."
                ]
            }
        },
        # Page 9: Worked Example Level 4
        {
            "page_number": 9,
            "page_title": "Example 4: Real-World Engineering (Projector Lens Design)",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "The lens of a slide projector focuses an image of height $1.5\\text{ m}$ on a screen placed $9.0\\text{ m}$ away. "
                    "If the picture on the slide has a height of $6.5\\text{ cm}$, determine:\n"
                    "(a) The distance from the slide to the projector lens ($u$).\n"
                    "(b) The focal length of the projector lens ($f$)."
                ),
                "steps": [
                    "**Given & Unit Normalization:** Object height $h_o = 6.5\\text{ cm}$; Image height $h_i = 1.5\\text{ m} = 150\\text{ cm}$; Image distance $v = 9.0\\text{ m} = 900\\text{ cm}$ (real image, $+v$).",
                    "**(a) Finding Object Distance $u$:** $$m = \\frac{h_i}{h_o} = \\frac{v}{u} \\implies \\frac{150}{6.5} = \\frac{900}{u}$$ $$u = \\frac{900 \\times 6.5}{150} = 6 \\times 6.5 = \\mathbf{39\\text{ cm}}$$",
                    "**(b) Finding Focal Length $f$:** $$\\frac{1}{f} = \\frac{1}{u} + \\frac{1}{v} = \\frac{1}{39} + \\frac{1}{900}$$ $$\\frac{1}{f} \\approx 0.02564 + 0.00111 = 0.02675\\text{ cm}^{-1}$$ $$f = \\frac{1}{0.02675} \\approx \\mathbf{37.4\\text{ cm}}$$",
                    "**Physical Reality Check:** In slide projectors, the slide is positioned just outside the focal point ($u = 39\\text{ cm} > f = 37.4\\text{ cm}$) so that a highly magnified, real image is thrown far across the room onto the projection screen."
                ]
            }
        },
        # Page 10: Worked Example Level 5
        {
            "page_number": 10,
            "page_title": "Example 5: Prescription Power & Diverging Lenses",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A patient's prescription spectacles have an optical power of $-4.0\\text{ D}$. "
                    "Determine the type of lens and its focal length in centimetres."
                ),
                "steps": [
                    "**Given & Goal:** Power $P = -4.0\\text{ D}$. Find focal length $f$ in cm and identify lens type.",
                    "**Governing Formula:** $$P = \\frac{1}{f\\text{ (m)}} \\implies f = \\frac{1}{P}$$",
                    "**Calculation in Metres:** $$f = \\frac{1}{-4.0\\text{ D}} = -0.25\\text{ m}$$",
                    "**Unit Conversion to Centimetres:** $$f = -0.25 \\times 100 = \\mathbf{-25\\text{ cm}}$$",
                    "**Physical Conclusion:** The negative power and focal length signify a **diverging (concave) lens** of focal length **$25\\text{ cm}$**, prescribed to correct short-sightedness (myopia)."
                ]
            }
        },
        # Page 11: Experimental Physics Setup
        {
            "page_number": 11,
            "page_title": "Experimental Physics: Determining Focal Length of a Convex Lens",
            "block_type": "step_process",
            "component_type": "step_process",
            "content": {
                "title": "Laboratory Investigation Protocol",
                "steps": [
                    "**Aim:** To determine the focal length ($f$) of a converging lens using the lens formula and graphical analysis.",
                    "**Apparatus Required:** Mounted convex lens, ray box with illuminated cross-wire screen, white receiving screen, metre rule ($1.0\\text{ m}$), power supply.",
                    "**Variable Identification:** Independent Variable: Object distance ($u$). Dependent Variable: Image distance ($v$). Controlled Variables: Lens focal length ($f$), source illumination, alignment along principal axis.",
                    "**Procedure:** Place the ray box at one end of the bench. Set the lens at a series of measured object distances ($u = 15, 20, 25, 30, 35, 40\\text{ cm}$). For each position, adjust the screen until a sharply focused image of the cross-wire is formed, then record $v$."
                ]
            }
        },
        {
            "page_number": 11,
            "page_title": "Laboratory Apparatus Setup for Focal Length Determination",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Laboratory bench setup showing illuminated ray box with cross-wire, convex lens on holder, white receiving screen, and metre rule measuring object distance u and image distance v.",
                "instruction": (
                    "Draw an optical bench setup: Ray box on left with illuminated cross-wire target, convex lens on central mount, and white cardboard screen on right. "
                    "Show metre rule aligned beneath with arrows showing measurement of object distance u (source to lens) and image distance v (lens to screen)."
                )
            }
        },
        # Page 12: Experimental Data & Graph Analysis
        {
            "page_number": 12,
            "page_title": "Graphical Analysis: The Reciprocal Graph ($1/v$ vs. $1/u$)",
            "block_type": "comparison_table",
            "component_type": "comparison_table",
            "content": {
                "headers": ["Trial", "Object Dist $u$ (cm)", "Image Dist $v$ (cm)", "$1/u$ ($\\text{cm}^{-1}$)", "$1/v$ ($\\text{cm}^{-1}$)", "Calculated $f = \\frac{uv}{u+v}$ (cm)"],
                "rows": [
                    ["1", "15.0", "30.0", "0.0667", "0.0333", "10.0"],
                    ["2", "20.0", "20.0", "0.0500", "0.0500", "10.0"],
                    ["3", "30.0", "15.0", "0.0333", "0.0667", "10.0"],
                    ["4", "40.0", "13.3", "0.0250", "0.0750", "10.0"],
                    ["5", "60.0", "12.0", "0.0167", "0.0833", "10.0"]
                ]
            }
        },
        {
            "page_number": 12,
            "page_title": "Graph Interpretation: Linear Reciprocal Relationship",
            "block_type": "suggested_graph",
            "component_type": "suggested_graph",
            "content": {
                "text": "Linear graph of 1/v on the vertical axis against 1/u on the horizontal axis. Straight line with gradient = -1, y-intercept = 1/f, and x-intercept = 1/f.",
                "instruction": (
                    "Plot a Cartesian graph with y-axis: 1/v (cm^-1) and x-axis: 1/u (cm^-1). "
                    "Draw a downward-sloping linear line crossing the y-axis at (0, 1/f) and x-axis at (1/f, 0). "
                    "Annotate: Gradient = -1; Vertical intercept A = 1/f; Horizontal intercept B = 1/f; Focal length f = 1 / intercept."
                )
            }
        },
        {
            "page_number": 12,
            "page_title": "Derivation of the Graph Equation",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### Derivation of the Linear Relationship:\n"
                    "Starting from the lens formula: $$\\frac{1}{f} = \\frac{1}{u} + \\frac{1}{v}$$\n"
                    "Rearranging into standard linear form ($y = mx + c$) where $y = \\frac{1}{v}$ and $x = \\frac{1}{u}$:\n"
                    "$$\\frac{1}{v} = -\\left(\\frac{1}{u}\\right) + \\frac{1}{f}$$\n\n"
                    "- **Gradient ($m$):** The gradient of this plot is always $\\mathbf{-1}$.\n"
                    "- **Vertical Intercept (y-intercept):** When $\\frac{1}{u} = 0$, $\\frac{1}{v} = \\frac{1}{f}$. Therefore: $$\\mathbf{f = \\frac{1}{y\\text{-intercept}}}$$\n"
                    "- **Horizontal Intercept (x-intercept):** When $\\frac{1}{v} = 0$, $\\frac{1}{u} = \\frac{1}{f}$. Therefore: $$\\mathbf{f = \\frac{1}{x\\text{-intercept}}}$$"
                )
            }
        },
        # Page 13: Laboratory Errors & Precautions
        {
            "page_number": 13,
            "page_title": "Laboratory Error Management & Practical Precautions",
            "block_type": "common_misconception",
            "component_type": "common_misconception",
            "content": {
                "text": (
                    "### 1. Focusing Uncertainty (Subjective Sharpness Error)\n"
                    "**Challenge**: It can be difficult to identify the exact position where the cross-wire image is sharpest on the screen.\n"
                    "**Precaution**: Move the screen past the focus until the image begins to blur, then move it back, taking the midpoint of the range over which the image remains distinct. Always conduct the experiment in a semi-darkened room to enhance contrast.\n\n"
                    "### 2. Parallax Error in Distance Measurements\n"
                    "**Challenge**: Reading the metre rule scale from an angled viewpoint produces systematic errors in $u$ and $v$.\n"
                    "**Precaution**: Position your line of sight perpendicular ($90^\\circ$) to the metre rule scale when recording object and image positions.\n\n"
                    "### 3. Lens-Screen Alignment Error\n"
                    "**Precaution**: Ensure the illuminated object, lens centre, and screen centre all lie along the exact same horizontal optical axis."
                )
            }
        },
        # Page 14: Calculation Practice (Image Position & Height)
        {
            "page_number": 14,
            "page_title": "Check Your Understanding: Lens Formula Calculation",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "An object of height $5.0\\text{ cm}$ is placed $15\\text{ cm}$ in front of a converging lens of focal length $10\\text{ cm}$. What is the position ($v$) and height ($h_i$) of the image formed?",
                "options": [
                    "$v = +30\\text{ cm}$, $h_i = 10.0\\text{ cm}$ (Inverted)",
                    "$v = +30\\text{ cm}$, $h_i = 5.0\\text{ cm}$ (Upright)",
                    "$v = -6.0\\text{ cm}$, $h_i = 2.0\\text{ cm}$ (Virtual)",
                    "$v = +25\\text{ cm}$, $h_i = 7.5\\text{ cm}$ (Inverted)"
                ],
                "answer": "A",
                "explanation": (
                    "1. Find image distance: 1/v = 1/f - 1/u = 1/10 - 1/15 = (3 - 2)/30 = 1/30 ==> v = +30 cm (Real, inverted image on opposite side).\n"
                    "2. Find magnification: m = v/u = 30/15 = 2.\n"
                    "3. Find image height: h_i = m * h_o = 2 * 5.0 cm = 10.0 cm."
                )
            }
        },
        # Page 15: Graph Interpretation Check
        {
            "page_number": 15,
            "page_title": "Check Your Understanding: Reciprocal Graph Interpretation",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "A student plots a graph of $1/v$ against $1/u$ from laboratory measurements. The straight line crosses the vertical axis at $0.08\\text{ cm}^{-1}$. What is the focal length ($f$) and optical power ($P$) of this lens?",
                "options": [
                    "$f = 12.5\\text{ cm}$, $P = +8.0\\text{ D}$",
                    "$f = 8.0\\text{ cm}$, $P = +12.5\\text{ D}$",
                    "$f = 0.08\\text{ cm}$, $P = +1.25\\text{ D}$",
                    "$f = 12.5\\text{ cm}$, $P = +0.08\\text{ D}$"
                ],
                "answer": "A",
                "explanation": (
                    "1. Focal length from vertical intercept: f = 1 / y-intercept = 1 / 0.08 cm^-1 = 12.5 cm.\n"
                    "2. Convert focal length to metres: f = 12.5 cm = 0.125 m.\n"
                    "3. Calculate power: P = 1 / f(m) = 1 / 0.125 m = +8.0 D."
                )
            }
        },
        # Page 16: Summary & Key Takeaways
        {
            "page_number": 16,
            "page_title": "Module 1.2 Summary: Quantitative Lens Optics",
            "block_type": "summary",
            "component_type": "summary",
            "content": {
                "text": (
                    "### Key Formulas & Relationships:\n"
                    "- **Magnification**: $m = \\frac{h_i}{h_o} = \\frac{v}{u}$\n"
                    "- **Lens Formula**: $\\frac{1}{f} = \\frac{1}{u} + \\frac{1}{v}$ (Convex $+f$, Concave $-f$; Real $+v$, Virtual $-v$)\n"
                    "- **Power of a Lens**: $P = \\frac{1}{f\\text{ (m)}}$ in Diopters ($D$)\n"
                    "- **8-Step Method**: Goal $\\rightarrow$ Given $\\rightarrow$ Formula $\\rightarrow$ Rearrange $\\rightarrow$ Substitute $\\rightarrow$ Calculate $\\rightarrow$ Units $\\rightarrow$ Reasonableness Check\n"
                    "- **Reciprocal Graph**: Plotting $\\frac{1}{v}$ against $\\frac{1}{u}$ yields gradient $=-1$, with intercepts at $\\frac{1}{f}$."
                )
            }
        },
        {
            "page_number": 16,
            "page_title": "Core Takeaways on Mathematical Optics",
            "block_type": "key_takeaway",
            "component_type": "key_takeaway",
            "content": {
                "text": "The lens formula and linear reciprocal graphs provide exact mathematical and experimental tools to determine focal lengths and design optical systems with precision."
            }
        }
    ]
}


# =============================================================================
# MODULE 1.3 DATA — Optical Instruments, the Eye, and Corrective Spectacles
# =============================================================================
MODULE_1_3 = {
    "unit_name": "Module 1.3: Optical Instruments, the Eye, and Corrective Spectacles",
    "unit_order": 3,
    "lesson_title": "Optical Instruments, the Eye, and Corrective Spectacles",
    "cards": [
        # Page 1: Hook & Goals
        {
            "page_number": 1,
            "page_title": "Engineering Vision: Optical Instruments and Human Sight",
            "block_type": "learning_goal",
            "component_type": "learning_goal",
            "content": {
                "text": (
                    "By combining multiple lenses, optical engineers can construct powerful instruments that reveal the microscopic realm of living cells "
                    "or capture light from galaxies billions of kilometres away. Furthermore, the human eye itself is a biological optical instrument "
                    "operating on these exact physical principles.\n\n"
                    "In this module, you will explore the ray optics and mechanics of microscopes, telescopes, cameras, and human vision defects.\n\n"
                    "By the end of this lesson, you will be able to:\n"
                    "- Explain the optical principles of the simple microscope, compound microscope, astronomical telescope, and camera\n"
                    "- Trace rays through multi-lens optical systems\n"
                    "- Compare the optical mechanics of the camera and the human eye\n"
                    "- Explain the biological mechanism of accommodation\n"
                    "- Diagnose vision defects (myopia, hypermetropia, presbyopia, astigmatism) and explain their lens corrections"
                )
            }
        },
        # Page 2: The Simple Microscope
        {
            "page_number": 2,
            "page_title": "The Simple Microscope (Magnifying Glass)",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### How It Works:\n"
                    "A simple microscope consists of a **single converging (convex) lens of short focal length**.\n"
                    "The object to be viewed is placed inside the focal point ($u < f$). As light refracts through the lens, diverging rays emerge on the eye side. "
                    "When the eye looks through the lens, it sees a **virtual, erect, and magnified image**.\n\n"
                    "### The Near Point and Distinct Vision ($D$):\n"
                    "To view the image with maximum clarity and minimum eye strain, the lens position is adjusted so that the virtual image forms at the "
                    "**least distance of distinct vision ($D = 25\\text{ cm}$)**, known as the near point of a normal human eye.\n\n"
                    "### Angular Magnification (Magnifying Power $M$):\n"
                    "$$M = \\frac{\\text{Angle subtended by image at eye (}\\beta\\text{)}}{\\text{Angle subtended by object at eye without lens at distance } D\\text{ (}\\alpha\\text{)}} = \\frac{\\beta}{\\alpha}$$\n"
                    "A lens with a shorter focal length bends light more sharply, producing a larger visual angle $\\beta$ and higher magnifying power."
                )
            }
        },
        {
            "page_number": 2,
            "page_title": "Ray Diagram: Simple Microscope at Near Point D = 25 cm",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Ray diagram of a simple magnifying glass showing an object placed within focal length u < f forming a virtual, upright, magnified image at near point D = 25 cm from the eye.",
                "instruction": (
                    "Draw a convex lens with an eye on the right side. Place an object on the left inside focal point F (u < f). "
                    "Trace two rays refracting into the eye. Draw dashed backward projections intersecting at distance D = 25 cm to form a large virtual upright image."
                )
            }
        },
        # Page 3: The Compound Microscope
        {
            "page_number": 3,
            "page_title": "The Compound Microscope: Two-Stage Magnification",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "To achieve magnifications far beyond the capability of a single lens, a **compound microscope** uses two converging lenses in series:\n\n"
                    "### 1. The Objective Lens (Short Focal Length $f_o$):\n"
                    "- Positioned close to the microscopic specimen.\n"
                    "- The specimen is placed just outside its focal point ($f_o < u < 2f_o$).\n"
                    "- Produces a **real, inverted, and magnified intermediate image ($I_1$)** inside the microscope barrel.\n\n"
                    "### 2. The Eyepiece Lens (Focal Length $f_e$, where $f_e > f_o$):\n"
                    "- Positioned near the observer's eye.\n"
                    "- The barrel length is adjusted so that the intermediate image $I_1$ falls inside the focal length of the eyepiece ($u_e < f_e$).\n"
                    "- The eyepiece acts as a magnifying glass, magnifying $I_1$ into a **massive virtual, inverted final image ($I_2$)** at near point $D = 25\\text{ cm}$.\n\n"
                    "### Total Magnification Formula:\n"
                    "$$M_{\\text{total}} = m_{\\text{objective}} \\times m_{\\text{eyepiece}} = \\left(\\frac{v_o}{u_o}\\right) \\times \\left(\\frac{v_e}{u_e}\\right)$$"
                )
            }
        },
        {
            "page_number": 3,
            "page_title": "Ray Diagram: Optical Train of a Compound Microscope",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Two-lens ray diagram of a compound microscope showing objective lens forming real magnified intermediate image I1 and eyepiece lens forming massive virtual final image I2 at distance D.",
                "instruction": (
                    "Draw two coaxial lenses: Objective lens (small diameter, short fo) and Eyepiece lens (larger diameter, fe). "
                    "Trace rays from specimen outside Fo forming inverted real image I1 inside Fe. "
                    "Trace rays from I1 through eyepiece diverging into eye, with dashed projections forming huge virtual inverted final image I2 at D."
                )
            }
        },
        # Page 4: The Astronomical Telescope
        {
            "page_number": 4,
            "page_title": "The Astronomical Telescope: Capturing Distant Starlight",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "The astronomical telescope is designed to view celestial objects at optical infinity (planets, stars, distant galaxies):\n\n"
                    "### 1. Objective Lens (Very Large Focal Length $f_o$, Wide Aperture):\n"
                    "- Gathers maximum starlight and focuses incoming parallel rays to form a **real, inverted, highly diminished intermediate image ($I_1$)** in its focal plane ($F_o$).\n\n"
                    "### 2. Eyepiece Lens (Short Focal Length $f_e$):\n"
                    "- Magnifies the intermediate image $I_1$.\n\n"
                    "### Normal Adjustment (Viewing at Infinity for a Relaxed Eye):\n"
                    "- In normal adjustment, the telescope is set so the focal points of both lenses coincide at the same physical point ($F_o = F_e$).\n"
                    "- The intermediate image $I_1$ forms exactly at $F_e$, causing the eyepiece to refract the rays completely parallel to infinity, allowing the observer to view the final image with a completely relaxed, unstrained eye.\n\n"
                    "### Key Formulas in Normal Adjustment:\n"
                    "- **Telescope Barrel Length ($L$):** $$L = f_o + f_e$$\n"
                    "- **Angular Magnification ($M$):** $$M = \\frac{f_o}{f_e}$$"
                )
            }
        },
        {
            "page_number": 4,
            "page_title": "Ray Diagram: Astronomical Telescope in Normal Adjustment",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Ray diagram of an astronomical telescope in normal adjustment showing incoming parallel rays from infinity focusing at shared focal plane Fo = Fe and emerging parallel from eyepiece.",
                "instruction": (
                    "Draw objective lens (left) and eyepiece (right) sharing focal plane Fo = Fe. "
                    "Trace tilted parallel rays from distant star focusing to inverted intermediate image I1 at Fo. "
                    "Trace rays from I1 through eyepiece emerging as parallel beam into eye. Label: Barrel Length L = fo + fe, Final Image at Infinity."
                )
            }
        },
        # Page 5: The Photographic Camera
        {
            "page_number": 5,
            "page_title": "The Photographic / Digital Camera",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "A camera is a light-proof enclosure with a converging lens system at one end and a light-sensitive surface (digital sensor or film) at the other:\n\n"
                    "### Key Functional Components:\n"
                    "- **Converging Lens System**: Focuses light from an object ($u > 2f$) to form a **real, inverted, diminished image** on the sensor.\n"
                    "- **Focusing Mechanism**: The focusing ring physically moves the lens closer to or further from the sensor to ensure sharp focus for objects at different distances ($v$).\n"
                    "- **Aperture & Diaphragm**: An adjustable circular iris that regulates the light intensity entering the camera.\n"
                    "- **Shutter**: A precision mechanical or electronic gate that opens for a fraction of a second (exposure time, e.g., $1/1000\\text{ s}$) to expose the sensor to light.\n"
                    "- **Sensor / Film**: The recording surface coated with photosensitive pixels or chemical emulsion."
                )
            }
        },
        {
            "page_number": 5,
            "page_title": "Cross-Section Diagram of a Camera Mechanism",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Cross-sectional engineering diagram of a camera showing converging lens, focusing ring, adjustable aperture diaphragm, shutter, and digital sensor.",
                "instruction": (
                    "Draw cross-section of a camera: light-proof box, front converging lens assembly, focusing screw mechanism, iris diaphragm aperture, shutter curtain, and rear digital sensor/film plane with ray cone focusing on sensor."
                )
            }
        },
        # Page 6: The Human Eye: Biological Optics
        {
            "page_number": 6,
            "page_title": "The Human Eye: Anatomy and Optical Mechanics",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "The human eye is a biological optical instrument functioning analogously to a camera:\n\n"
                    "### Key Anatomical Landmarks:\n"
                    "- **Cornea**: Tough transparent outer membrane providing the initial and greatest refraction of incoming light.\n"
                    "- **Crystalline Lens**: Flexible, double-convex organic lens that provides fine-focusing adjustments.\n"
                    "- **Iris & Pupil**: The iris is a coloured muscle that expands or contracts the central aperture (pupil) to regulate light entry.\n"
                    "- **Retina**: Light-sensitive screen at the back of the eye coated with photoreceptors (rods and cones) where **real, inverted images** form.\n"
                    "- **Optic Nerve**: Transmits electrical signals from the retina to the brain's visual cortex, which inverts the perception upright.\n\n"
                    "### The Mechanism of Accommodation:\n"
                    "Accommodation is the ability of the eye to alter its focal length to focus clearly on both near and distant objects:\n"
                    "- **Viewing Distant Objects ($u = \\infty$):** Ciliary muscles relax $\\rightarrow$ suspensory ligaments pull taut $\\rightarrow$ crystalline lens is flattened $\\rightarrow$ **focal length increases** to focus parallel rays onto retina.\n"
                    "- **Viewing Near Objects ($u = 25\\text{ cm}$):** Ciliary muscles contract $\\rightarrow$ suspensory ligaments loosen $\\rightarrow$ lens bulges into a thicker, more spherical shape $\\rightarrow$ **focal length decreases** to bend divergent rays onto retina."
                )
            }
        },
        {
            "page_number": 6,
            "page_title": "Anatomical Cross-Section of the Human Eye",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Anatomical diagram of the human eye showing cornea, aqueous humour, iris, pupil, crystalline lens, ciliary muscles, suspensory ligaments, vitreous humour, retina, and optic nerve.",
                "instruction": (
                    "Draw horizontal cross-section of the human eye: Cornea, anterior chamber, iris, pupil aperture, crystalline lens suspended by ciliary muscles and ligaments, vitreous body, retina screen at back, fovea, and optic nerve exiting to brain."
                )
            }
        },
        # Page 7: Camera vs. Human Eye Comparison
        {
            "page_number": 7,
            "page_title": "Comparison: Photographic Camera vs. Human Eye",
            "block_type": "comparison_table",
            "component_type": "comparison_table",
            "content": {
                "headers": ["Camera Component", "Human Eye Equivalent", "Shared Optical Function", "Operational Difference"],
                "rows": [
                    ["Converging Lens", "Cornea & Crystalline Lens", "Refracts and focuses light rays.", "Camera focuses by physically moving the lens; Eye focuses by changing lens curvature (accommodation)."],
                    ["Aperture & Diaphragm", "Pupil & Iris", "Regulates intensity of entering light.", "Camera aperture is manually or electronically set; Eye iris reacts involuntarily to ambient brightness."],
                    ["Shutter Gate", "Eyelids", "Controls light entry and exposure.", "Camera shutter opens for precise fractions of a second; Eyelids protect the eye and blink periodically."],
                    ["Light-Sensitive Film / Sensor", "Retina", "Serves as the screen where real inverted image forms.", "Camera records static digital/chemical frames; Retina continuously transmits dynamic neural impulses."],
                    ["Light-Proof Casing", "Sclera & Choroid", "Prevents internal light reflection.", "Camera uses black-painted metal/plastic box; Eye uses opaque sclera and pigmented choroid layer."]
                ]
            }
        },
        # Page 8: Vision Defects: Short-Sightedness (Myopia)
        {
            "page_number": 8,
            "page_title": "Vision Defect 1: Short-Sightedness (Myopia) & Correction",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### What is Myopia?\n"
                    "A short-sighted person can see near objects clearly, but **distant objects appear blurred**.\n\n"
                    "### Physical Causes:\n"
                    "1. The eyeball is **too long** from front to back.\n"
                    "2. The eye lens is **too curved / too strong** (relaxed focal length is too short), causing parallel rays from distant objects to converge and focus **in front of the retina**.\n\n"
                    "### Optical Correction: Diverging (Concave) Lens\n"
                    "Placing a **diverging (concave) lens** in front of the eye diverges the incoming parallel rays slightly before they enter the cornea. "
                    "This pre-divergence pushes the focal point further back, forming a sharp image directly **on the retina**."
                )
            }
        },
        {
            "page_number": 8,
            "page_title": "Ray Diagram: Myopic Eye and Concave Lens Optical Correction",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Two-panel ray diagram showing (top) myopic eye focusing distant parallel rays in front of the retina, and (bottom) concave spectacle lens diverging rays so they focus sharply on the retina.",
                "instruction": (
                    "Draw 2 vertically stacked eye diagrams: "
                    "(Top) Elongated eye with parallel incoming rays converging and crossing in front of the retina, producing a blurred spot on retina. "
                    "(Bottom) Concave lens placed in front of eye, slightly diverging parallel rays before entering eye, bringing sharp focus directly onto retina screen."
                )
            }
        },
        # Page 9: Vision Defects: Long-Sightedness (Hypermetropia)
        {
            "page_number": 9,
            "page_title": "Vision Defect 2: Long-Sightedness (Hypermetropia) & Correction",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### What is Hypermetropia?\n"
                    "A long-sighted person can see distant objects clearly, but **near objects (at $25\\text{ cm}$) appear blurred**.\n\n"
                    "### Physical Causes:\n"
                    "1. The eyeball is **too short** from front to back.\n"
                    "2. The eye lens is **too flat / too weak** (ciliary muscles cannot contract enough to achieve a short focal length), causing divergent rays from near objects to focus **behind the retina**.\n\n"
                    "### Optical Correction: Converging (Convex) Lens\n"
                    "Placing a **converging (convex) lens** in front of the eye pre-converges the divergent rays from near objects before they enter the eye. "
                    "The weakened crystalline lens can then easily complete the convergence to form a sharp image directly **on the retina**."
                )
            }
        },
        {
            "page_number": 9,
            "page_title": "Ray Diagram: Hypermetropic Eye and Convex Lens Optical Correction",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "text": "Two-panel ray diagram showing (top) hypermetropic eye focusing near divergent rays behind the retina, and (bottom) convex spectacle lens pre-converging rays to focus sharply on the retina.",
                "instruction": (
                    "Draw 2 vertically stacked eye diagrams: "
                    "(Top) Shortened eye with divergent rays from near object (25 cm) focusing behind the retina plane. "
                    "(Bottom) Convex lens placed in front of eye pre-converging rays, allowing eye lens to bring focus directly onto retina surface."
                )
            }
        },
        # Page 10: Presbyopia and Astigmatism
        {
            "page_number": 10,
            "page_title": "Presbyopia and Astigmatism: Aging & Curvature Defects",
            "block_type": "definition_card",
            "component_type": "definition_card",
            "content": {
                "term": "Presbyopia (Old-Age Sight Defect)",
                "definition": (
                    "**Presbyopia** is the loss of the eye's accommodation power due to aging. "
                    "As people age, ciliary muscles weaken and the crystalline lens loses elasticity, preventing it from bulging for near vision.\n\n"
                    "**Correction:** **Bifocal spectacles** containing a converging lower segment for reading and a plain or diverging upper segment for distance viewing."
                )
            }
        },
        {
            "page_number": 10,
            "page_title": "Astigmatism: Non-Spherical Cornea Defect",
            "block_type": "concept_explanation",
            "component_type": "concept_explanation",
            "content": {
                "text": (
                    "### Astigmatism\n"
                    "**Astigmatism** is a vision defect where light rays in different planes (horizontal vs. vertical) focus at different distances, "
                    "causing horizontal lines to appear sharp while vertical lines appear blurred (or vice versa).\n\n"
                    "- **Cause**: The cornea or crystalline lens is **non-spherical** (curved more sharply in one meridian than another, like a rugby ball).\n"
                    "- **Correction**: **Cylindrical lenses** designed with different radii of curvature in perpendicular planes to equalize focal power across all axes."
                )
            }
        },
        # Page 11: Multi-Step Worked Example: Compound Microscope Challenge
        {
            "page_number": 11,
            "page_title": "Challenge Problem: Compound Microscope Optics",
            "block_type": "worked_example",
            "component_type": "worked_example",
            "content": {
                "problem": (
                    "A research compound microscope consists of an objective lens of focal length $f_o = 1.0\\text{ cm}$ "
                    "and an eyepiece lens of focal length $f_e = 5.0\\text{ cm}$. An illuminated specimen is placed $1.2\\text{ cm}$ from the objective lens.\n\n"
                    "(a) Calculate the position of the intermediate image ($v_o$) formed by the objective lens.\n"
                    "(b) If the final virtual image is formed at the near point $D = 25\\text{ cm}$ from the eyepiece, calculate the required barrel length ($L$) between the two lenses.\n"
                    "(c) Determine the total magnification ($M_{\\text{total}}$) produced by the microscope system."
                ),
                "steps": [
                    "**(a) Objective Lens Image Position ($v_o$):** $$\\frac{1}{f_o} = \\frac{1}{u_o} + \\frac{1}{v_o} \\implies \\frac{1}{v_o} = \\frac{1}{1.0} - \\frac{1}{1.2} = 1.0 - 0.833 = 0.167\\text{ cm}^{-1}$$ $$v_o = \\frac{1}{0.167} = \\mathbf{+6.0\\text{ cm}} \\text{ (inside the barrel)}$$",
                    "**(b) Eyepiece Object Distance ($u_e$) & Barrel Length ($L$):** Eyepiece forms virtual image at $v_e = -25\\text{ cm}$ with $f_e = +5.0\\text{ cm}$: $$\\frac{1}{u_e} = \\frac{1}{f_e} - \\frac{1}{v_e} = \\frac{1}{5.0} - \\left(\\frac{1}{-25}\\right) = \\frac{5}{25} + \\frac{1}{25} = \\frac{6}{25}$$ $$u_e = \\frac{25}{6} \\approx 4.17\\text{ cm}$$ Total barrel separation: $$L = v_o + u_e = 6.0\\text{ cm} + 4.17\\text{ cm} = \\mathbf{10.17\\text{ cm}}$$",
                    "**(c) Total System Magnification ($M_{\\text{total}}$):** Objective magnification: $$m_o = \\frac{v_o}{u_o} = \\frac{6.0}{1.2} = 5.0$$ Eyepiece magnification: $$m_e = \\frac{v_e}{u_e} = \\frac{25}{4.17} = 6.0$$ Total magnification: $$M_{\\text{total}} = m_o \\times m_e = 5.0 \\times 6.0 = \\mathbf{30\\text{ times}}$$",
                    "**Physical Conclusion:** The specimen is magnified 5 times into a real intermediate image, which the eyepiece magnifies a further 6 times, producing a sharp, 30-times enlarged virtual image for the researcher."
                ]
            }
        },
        # Page 12: Common Misconceptions
        {
            "page_number": 12,
            "page_title": "Common Traps in Biological & Instrument Optics",
            "block_type": "common_misconception",
            "component_type": "common_misconception",
            "content": {
                "text": (
                    "### Trap 1: \"We see upright because the image formed on the retina is upright.\"\n"
                    "**Scientific Correction**: The cornea and crystalline lens form a converging system that projects a **real, inverted (upside-down) image** on the retina. "
                    "The brain's visual cortex processes the neural electrical signals from the optic nerve and flips the visual perception right-side-up.\n\n"
                    "### Trap 2: \"Myopia is long-sightedness and Hypermetropia is short-sightedness.\"\n"
                    "**Scientific Correction**: **Myopia = Short-sightedness** (corrected by concave diverging lenses). **Hypermetropia = Long-sightedness** (corrected by convex converging lenses).\n\n"
                    "### Trap 3: \"Astigmatism is the same as Cataracts.\"\n"
                    "**Scientific Correction**: Astigmatism is an optical curvature defect (non-spherical cornea corrected by cylindrical spectacles). Cataracts occur when the organic eye lens becomes cloudy/opaque with protein deposits, requiring surgical replacement with an artificial intraocular lens."
                )
            }
        },
        # Page 13: Knowledge Check: Diagnosing Vision Defects
        {
            "page_number": 13,
            "page_title": "Check Your Understanding: Diagnosing Vision Defects",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "A patient cannot read a book held at $25\\text{ cm}$ because divergent light rays from the text converge behind the retina. Diagnose the defect and state the corrective spectacle lens required:",
                "options": [
                    "Hypermetropia (Long-sightedness), corrected by a Converging (Convex) lens",
                    "Myopia (Short-sightedness), corrected by a Diverging (Concave) lens",
                    "Presbyopia, corrected by a Cylindrical lens",
                    "Astigmatism, corrected by a Diverging (Concave) lens"
                ],
                "answer": "A",
                "explanation": (
                    "When rays from near objects focus behind the retina, the eyeball is either too short or the lens is too weak to accommodate, which is Hypermetropia (Long-sightedness). "
                    "It is corrected by a converging (convex) lens, which pre-converges the rays so the eye lens focuses them sharply on the retina."
                )
            }
        },
        # Page 14: Knowledge Check: Telescope Optics
        {
            "page_number": 14,
            "page_title": "Check Your Understanding: Astronomical Telescope Optics",
            "block_type": "knowledge_check",
            "component_type": "knowledge_check",
            "content": {
                "check_type": "multiple_choice",
                "question": "An astronomical telescope in normal adjustment has an objective lens of focal length $f_o = 100\\text{ cm}$ and an eyepiece of focal length $f_e = 5\\text{ cm}$. What is the barrel length ($L$) and angular magnification ($M$) of the telescope?",
                "options": [
                    "$L = 105\\text{ cm}$, $M = 20$",
                    "$L = 95\\text{ cm}$, $M = 20$",
                    "$L = 105\\text{ cm}$, $M = 500$",
                    "$L = 500\\text{ cm}$, $M = 20$"
                ],
                "answer": "A",
                "explanation": (
                    "In normal adjustment: \n"
                    "1. Barrel Length: L = f_o + f_e = 100 cm + 5 cm = 105 cm.\n"
                    "2. Angular Magnification: M = f_o / f_e = 100 / 5 = 20 times."
                )
            }
        },
        # Page 15: Summary & Key Takeaways
        {
            "page_number": 15,
            "page_title": "Module 1.3 Summary: Optical Instruments and Vision",
            "block_type": "summary",
            "component_type": "summary",
            "content": {
                "text": (
                    "### Summary of Optical Instruments:\n"
                    "- **Simple Microscope**: Single convex lens ($u < f$), forms virtual, upright, magnified image at near point $D = 25\\text{ cm}$.\n"
                    "- **Compound Microscope**: Objective ($f_o$) forms real magnified intermediate image; Eyepiece ($f_e$) magnifies it to massive virtual image ($M = m_o \\times m_e$).\n"
                    "- **Astronomical Telescope**: Long $f_o$ objective gathers starlight to focal plane; short $f_e$ eyepiece refracts parallel to infinity ($L = f_o + f_e$, $M = f_o / f_e$).\n"
                    "- **Camera vs. Eye**: Camera focuses by moving lens ($v$), eye focuses by ciliary muscle accommodation (changing curvature $f$).\n"
                    "- **Corrective Optometry**: Myopia (short-sighted, rays focus in front $\\rightarrow$ concave lens); Hypermetropia (long-sighted, rays focus behind $\\rightarrow$ convex lens); Presbyopia (bifocals); Astigmatism (cylindrical lens)."
                )
            }
        },
        {
            "page_number": 15,
            "page_title": "Core Takeaways on Optical Systems",
            "block_type": "key_takeaway",
            "component_type": "key_takeaway",
            "content": {
                "text": "Optical instruments combine multiple lenses to manipulate light geometry, enabling humans to observe the microscopic realm, explore deep space, and correct biological vision defects."
            }
        }
    ]
}

ALL_MODULES = [MODULE_1_1, MODULE_1_2, MODULE_1_3]


# =============================================================================
# INGESTION EXECUTOR
# =============================================================================

def run_ingestion(replace_mode=False):
    print("=" * 80)
    print("VLEARN FORM 4 PHYSICS — TOPIC 1: THIN LENSES INGESTION")
    print(f"Mode: {'REPLACE (Destructive Fresh Ingestion)' if replace_mode else 'IDEMPOTENT SAFE UPDATE'}")
    print("=" * 80)

    # 1. Resolve Curriculum Hierarchy
    curriculum = Curriculum.objects.filter(name="844").first()
    if not curriculum:
        curriculum = Curriculum.objects.create(name="844", description="Kenyan 8-4-4 Secondary Curriculum")
        print(f"Created Curriculum: {curriculum.name}")
    else:
        print(f"Found Curriculum: {curriculum.name} (ID: {curriculum.id})")

    grade, _ = Grade.objects.get_or_create(
        curriculum=curriculum,
        name="Form 4",
        defaults={"level": 4, "description": "Form 4 Secondary Level"}
    )
    print(f"Grade verified: {grade.name} (Curriculum: {curriculum.name}, Level: {grade.level})")

    subject, _ = Subject.objects.get_or_create(
        grade=grade,
        name="Physics",
        defaults={"description": "Form 4 Physics (844 Syllabus)"}
    )
    print(f"Subject verified: {subject.name} (ID: {subject.id}) under {grade.name}")

    topic, _ = Topic.objects.get_or_create(
        subject=subject,
        name="Topic 1: Thin Lenses",
        defaults={
            "description": (
                "Comprehensive study of converging and diverging thin lenses, ray tracing principles, "
                "the lens formula and magnification, focal length determination experiments, optical instruments "
                "(microscopes, telescopes, cameras), and human vision defects and corrective optometry."
            ),
            "order": 1
        }
    )
    print(f"Topic verified: {topic.name} (ID: {topic.id}) under {subject.name}\n")

    # 2. Module Ingestion Loop
    total_blocks_created = 0
    total_blocks_updated = 0

    for m_idx, m_data in enumerate(ALL_MODULES, start=1):
        unit, created = LearningUnit.objects.get_or_create(
            topic=topic,
            name=m_data["unit_name"],
            defaults={"order": m_data["unit_order"]}
        )
        print(f"[{m_idx}/3] Learning Unit: '{unit.name}' ({'Created' if created else 'Found'})")

        lesson, created = Lesson.objects.get_or_create(
            learning_unit=unit,
            defaults={
                "title": m_data["lesson_title"],
                "topic": topic,
                "status": "published",
                "version": 1
            }
        )
        if not created:
            lesson.title = m_data["lesson_title"]
            lesson.status = "published"
            lesson.save()
        print(f"     Lesson: '{lesson.title}' (ID: {lesson.id}, status={lesson.status})")

        with transaction.atomic():
            if replace_mode:
                del_blocks, _ = LessonBlock.objects.filter(lesson=lesson).delete()
                del_assets, _ = LessonAsset.objects.filter(lesson=lesson).delete()
                if del_blocks or del_assets:
                    print(f"     [Replace Mode] Purged {del_blocks} existing blocks, {del_assets} existing assets")

            for order, card in enumerate(m_data["cards"], start=1):
                clean_card = clean_content_dict(card)
                block_id = f"block_{lesson.id}_p{clean_card['page_number']}_{order}_{uuid.uuid4().hex[:6]}"

                if replace_mode:
                    LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=block_id,
                        order=order,
                        page_number=clean_card["page_number"],
                        page_title=clean_card["page_title"],
                        block_type=clean_card["block_type"],
                        component_type=clean_card["component_type"],
                        component_order=order,
                        title=clean_card["page_title"],
                        content=clean_card["content"]
                    )
                    total_blocks_created += 1
                else:
                    # Safe Idempotent Mode: Match by page_number, block_type, and order
                    existing_block = LessonBlock.objects.filter(
                        lesson=lesson,
                        page_number=clean_card["page_number"],
                        block_type=clean_card["block_type"]
                    ).first()

                    if existing_block:
                        existing_block.order = order
                        existing_block.page_title = clean_card["page_title"]
                        existing_block.component_type = clean_card["component_type"]
                        existing_block.component_order = order
                        existing_block.title = clean_card["page_title"]
                        
                        # Preserve existing enriched assets and svg_content if present
                        if isinstance(existing_block.content, dict) and 'svg_content' in existing_block.content:
                            clean_card["content"]["svg_content"] = existing_block.content["svg_content"]
                            clean_card["content"]["svg"] = existing_block.content.get("svg")
                        
                        existing_block.content = clean_card["content"]
                        existing_block.save()
                        total_blocks_updated += 1
                    else:
                        LessonBlock.objects.create(
                            lesson=lesson,
                            block_id=block_id,
                            order=order,
                            page_number=clean_card["page_number"],
                            page_title=clean_card["page_title"],
                            block_type=clean_card["block_type"],
                            component_type=clean_card["component_type"],
                            component_order=order,
                            title=clean_card["page_title"],
                            content=clean_card["content"]
                        )
                        total_blocks_created += 1

        num_pages = max(c["page_number"] for c in m_data["cards"])
        print(f"     Processed {len(m_data['cards'])} cards across {num_pages} pages.\n")

    print("=" * 80)
    print("INGESTION COMPLETED SUCCESSFULLY!")
    print(f"Total Blocks Created: {total_blocks_created} | Total Blocks Updated: {total_blocks_updated}")
    print(f"Curriculum: {curriculum.name} | Grade: {grade.name} | Subject: {subject.name} | Topic: {topic.name}")
    print("=" * 80)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Form 4 Physics Ingestion")
    parser.add_argument("--replace", action="store_true", help="Purge and replace blocks fresh")
    args = parser.parse_args()
    run_ingestion(replace_mode=args.replace)
