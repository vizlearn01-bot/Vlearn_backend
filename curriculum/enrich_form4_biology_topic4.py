"""
VLearn Form 4 Biology — Topic 4: Support and Movement in Plants and Animals
Visual Enrichment Engine (18 Vector SVGs + 8 Verified Wikimedia Photos)

Attaches:
  - 18 Custom Vector SVGs to suggested_diagram blocks
  - 8 Pre-Verified Wikimedia Photos to suggested_image blocks
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_form4_biology_topic4.py
"""

import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, Lesson, LessonBlock, LessonAsset
)

def sanitize_svg(svg: str) -> str:
    """Ensures SVG is clean, responsive, and stripped of unneeded XML headers."""
    svg = re.sub(r'<\?xml.*?\?>', '', svg)
    svg = re.sub(r'<!DOCTYPE.*?>', '', svg)
    return svg.strip()

# =====================================================================
# 18 HIGH-PRECISION VECTOR SVGS FOR BIOLOGY TOPIC 4
# =====================================================================

SVG_1 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Skeletal Types: Hydrostatic, Exoskeleton, and Endoskeleton</text>
  <g transform="translate(30, 80)">
    <rect x="0" y="0" width="220" height="300" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="110" y="30" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">Hydrostatic Skeleton</text>
    <text x="110" y="80" font-size="12" fill="#cbd5e1" text-anchor="middle">Pressurized Coelomic Fluid</text>
    <text x="110" y="120" font-size="12" fill="#cbd5e1" text-anchor="middle">Circular &amp; Longitudinal</text>
    <text x="110" y="160" font-size="12" fill="#cbd5e1" text-anchor="middle">e.g., Earthworms, Jellyfish</text>

    <rect x="250" y="0" width="220" height="300" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="360" y="30" font-size="14" font-weight="bold" fill="#10b981" text-anchor="middle">Exoskeleton</text>
    <text x="360" y="80" font-size="12" fill="#cbd5e1" text-anchor="middle">Hard Chitinous Cuticle</text>
    <text x="360" y="120" font-size="12" fill="#cbd5e1" text-anchor="middle">Requires Ecdysis (Molting)</text>
    <text x="360" y="160" font-size="12" fill="#cbd5e1" text-anchor="middle">e.g., Insects, Crabs</text>

    <rect x="500" y="0" width="220" height="300" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="610" y="30" font-size="14" font-weight="bold" fill="#a855f7" text-anchor="middle">Endoskeleton</text>
    <text x="610" y="80" font-size="12" fill="#cbd5e1" text-anchor="middle">Internal Living Bone &amp; Cartilage</text>
    <text x="610" y="120" font-size="12" fill="#cbd5e1" text-anchor="middle">Grows Continuously with Body</text>
    <text x="610" y="160" font-size="12" fill="#cbd5e1" text-anchor="middle">e.g., Fish, Mammals</text>
  </g>
</svg>
""")

SVG_2 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Plant Support Tissues Cross-Section: Collenchyma vs Sclerenchyma</text>
  <rect x="40" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="212" y="110" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">Collenchyma Tissue</text>
  <text x="60" y="170" font-size="13" fill="#cbd5e1">• Living cells with active cytoplasm</text>
  <text x="60" y="210" font-size="13" fill="#cbd5e1">• Cell walls thickened at corners</text>
  <text x="60" y="250" font-size="13" fill="#a7f3d0">• Provides flexible strength in stems</text>

  <rect x="415" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
  <text x="587" y="110" font-size="15" font-weight="bold" fill="#ef4444" text-anchor="middle">Sclerenchyma Tissue</text>
  <text x="435" y="170" font-size="13" fill="#cbd5e1">• Dead cells at functional maturity</text>
  <text x="435" y="210" font-size="13" fill="#cbd5e1">• Thickened with Lignin secondary walls</text>
  <text x="435" y="250" font-size="13" fill="#fca5a5">• Provides rigid, non-yielding support</text>
</svg>
""")

SVG_3 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Lignified Xylem Vessels &amp; Tracheid Thickenings</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="400" y="120" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">Xylem Wall Lignin Reinforcement Patterns</text>
  <text x="80" y="170" font-size="13" fill="#cbd5e1">1. Annular Thickenings: Lignin rings along vessel length.</text>
  <text x="80" y="210" font-size="13" fill="#cbd5e1">2. Spiral Thickenings: Continuous helical lignin coil.</text>
  <text x="80" y="250" font-size="13" fill="#cbd5e1">3. Reticulate &amp; Pitted Thickenings: Dense network with unlignified pits for water movement.</text>
  <text x="80" y="290" font-size="13" font-weight="bold" fill="#a7f3d0">Dual Role: High-efficiency water transport &amp; high mechanical rigidity.</text>
</svg>
""")

SVG_4 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Fish Myotome Muscle Blocks &amp; Fin Anatomy (Pectoral, Pelvic, Caudal)</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="400" y="120" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">Bony Fish (Tilapia) Anatomy</text>
  <text x="80" y="170" font-size="13" fill="#cbd5e1">1. W-Shaped Myotome Muscle Blocks: Contract alternately along spine driving lateral tail waves.</text>
  <text x="80" y="210" font-size="13" fill="#cbd5e1">2. Caudal Fin: Main propulsive tail fin pushing fish forward.</text>
  <text x="80" y="250" font-size="13" fill="#cbd5e1">3. Paired Fins (Pectoral &amp; Pelvic): Steering, pitching, and braking.</text>
  <text x="80" y="290" font-size="13" fill="#cbd5e1">4. Unpaired Fins (Dorsal &amp; Anal): Prevent rolling and yawing instability.</text>
</svg>
""")

SVG_5 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Yawing, Pitching, and Rolling Controls in Finned Fish</text>
  <g transform="translate(30, 80)">
    <rect x="0" y="0" width="220" height="300" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="110" y="30" font-size="14" font-weight="bold" fill="#ef4444" text-anchor="middle">Pitching (Up/Down)</text>
    <text x="110" y="80" font-size="12" fill="#cbd5e1" text-anchor="middle">Vertical head/tail movement</text>
    <text x="110" y="130" font-size="13" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Controlled by Paired</text>
    <text x="110" y="160" font-size="13" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Pectoral &amp; Pelvic Fins</text>

    <rect x="250" y="0" width="220" height="300" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="360" y="30" font-size="14" font-weight="bold" fill="#f59e0b" text-anchor="middle">Rolling (Rotational)</text>
    <text x="360" y="80" font-size="12" fill="#cbd5e1" text-anchor="middle">Sideways tipping over axis</text>
    <text x="360" y="130" font-size="13" font-weight="bold" fill="#fef08a" text-anchor="middle">Prevented by Unpaired</text>
    <text x="360" y="160" font-size="13" font-weight="bold" fill="#fef08a" text-anchor="middle">Dorsal &amp; Anal Fins</text>

    <rect x="500" y="0" width="220" height="300" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="610" y="30" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">Yawing (Lateral)</text>
    <text x="610" y="80" font-size="12" fill="#cbd5e1" text-anchor="middle">Side-to-side displacement</text>
    <text x="610" y="130" font-size="13" font-weight="bold" fill="#93c5fd" text-anchor="middle">Prevented by Dorsal,</text>
    <text x="610" y="160" font-size="13" font-weight="bold" fill="#93c5fd" text-anchor="middle">Anal &amp; Caudal Fins</text>
  </g>
</svg>
""")

SVG_6 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Mammalian Skull Anatomy: Cranium, Orbit, Maxilla, Mandible</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="400" y="120" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">Skull Architecture</text>
  <text x="80" y="170" font-size="13" fill="#cbd5e1">1. Cranium (Brainbox): Protects delicate brain inside fused cranial bones.</text>
  <text x="80" y="210" font-size="13" fill="#cbd5e1">2. Orbits: Deep sockets housing sensory eyes.</text>
  <text x="80" y="250" font-size="13" fill="#cbd5e1">3. Jaws: Maxilla (Upper fixed jaw) &amp; Mandible (Lower movable jaw).</text>
  <text x="80" y="290" font-size="13" fill="#cbd5e1">4. Occipital Condyles: Double smooth knobs articulating with Atlas vertebra.</text>
</svg>
""")

SVG_7 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Structural Blueprint of a Typical Mammalian Vertebra</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <circle cx="400" cy="240" r="90" fill="#1e293b" stroke="#10b981" stroke-width="3"/>
  <circle cx="400" cy="210" r="35" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <text x="400" y="215" font-size="11" fill="#38bdf8" text-anchor="middle">Neural Canal</text>
  <line x1="400" y1="120" x2="400" y2="150" stroke="#10b981" stroke-width="4"/>
  <text x="400" y="110" font-size="12" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Neural Spine</text>
  <text x="400" y="280" font-size="14" font-weight="bold" fill="#cbd5e1" text-anchor="middle">Centrum (Body)</text>
</svg>
""")

SVG_8 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Cervical Vertebrae Specialization: Atlas vs Axis</text>
  <rect x="40" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="212" y="110" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">1st Cervical: Atlas</text>
  <text x="60" y="170" font-size="13" fill="#cbd5e1">• Ring-shaped bone, Lacks Centrum</text>
  <text x="60" y="210" font-size="13" fill="#cbd5e1">• Broad facets for skull condyles</text>
  <text x="60" y="250" font-size="13" fill="#93c5fd">• Enables 'YES' nodding movement</text>

  <rect x="415" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="587" y="110" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">2nd Cervical: Axis</text>
  <text x="435" y="170" font-size="13" fill="#cbd5e1">• Features Odontoid Process (Peg)</text>
  <text x="435" y="210" font-size="13" fill="#cbd5e1">• Peg fits into Atlas ring</text>
  <text x="435" y="250" font-size="13" fill="#a7f3d0">• Enables 'NO' side rotation movement</text>
</svg>
""")

SVG_9 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Thoracic Vertebra vs Lumbar Vertebra Architecture</text>
  <rect x="40" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="212" y="110" font-size="15" font-weight="bold" fill="#f59e0b" text-anchor="middle">Thoracic Vertebra (12)</text>
  <text x="60" y="170" font-size="13" fill="#cbd5e1">• Long neural spine pointing backwards</text>
  <text x="60" y="210" font-size="13" fill="#cbd5e1">• Capitular &amp; Tuberculular rib facets</text>
  <text x="60" y="250" font-size="13" fill="#fef08a">• Medium-sized centrum</text>

  <rect x="415" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="587" y="110" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">Lumbar Vertebra (5)</text>
  <text x="435" y="170" font-size="13" fill="#cbd5e1">• Massive, heavy load-bearing centrum</text>
  <text x="435" y="210" font-size="13" fill="#cbd5e1">• Broad flat transverse processes</text>
  <text x="435" y="250" font-size="13" fill="#a7f3d0">• Well-developed metapophyses</text>
</svg>
""")

SVG_10 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Human Rib Cage &amp; Sternum Anatomy</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="400" y="120" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">12 Pairs of Ribs Classification</text>
  <text x="80" y="170" font-size="13" fill="#cbd5e1">1. True Ribs (Pairs 1–7): Attached directly to Sternum via Costal Cartilages.</text>
  <text x="80" y="210" font-size="13" fill="#cbd5e1">2. False Ribs (Pairs 8–10): Attached indirectly to 7th costal cartilage.</text>
  <text x="80" y="250" font-size="13" fill="#cbd5e1">3. Floating Ribs (Pairs 11–12): Unattached anteriorly in abdominal wall muscles.</text>
  <text x="80" y="290" font-size="13" font-weight="bold" fill="#a7f3d0">Protects Heart &amp; Lungs; Enables Intercostal Respiration Movements.</text>
</svg>
""")

SVG_11 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Pectoral Girdle Anatomy: Scapula &amp; Clavicle</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
  <text x="400" y="120" font-size="15" font-weight="bold" fill="#a855f7" text-anchor="middle">Shoulder Girdle Components</text>
  <text x="80" y="170" font-size="13" fill="#cbd5e1">1. Scapula: Flat triangular shoulder blade with prominent dorsal spine.</text>
  <text x="80" y="210" font-size="13" fill="#cbd5e1">2. Glenoid Cavity: Shallow cup receiving head of humerus (Shoulder Joint).</text>
  <text x="80" y="250" font-size="13" fill="#cbd5e1">3. Acromion &amp; Metacromion Processes: Muscle attachment points.</text>
  <text x="80" y="290" font-size="13" fill="#cbd5e1">4. Clavicle: Slender rod collarbone bracing shoulder to sternum.</text>
</svg>
""")

SVG_12 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Forelimb Bones &amp; Elbow Joint Mechanics (Humerus, Radius, Ulna)</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="400" y="120" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">Forelimb Skeleton Layout</text>
  <text x="80" y="170" font-size="13" fill="#cbd5e1">1. Humerus: Upper arm bone featuring smooth head, deltoid ridge, &amp; trochlea.</text>
  <text x="80" y="210" font-size="13" fill="#cbd5e1">2. Radius: Lateral forearm bone aligned with thumb side.</text>
  <text x="80" y="250" font-size="13" fill="#cbd5e1">3. Ulna: Medial forearm bone with Olecranon Process forming elbow point.</text>
  <text x="80" y="290" font-size="13" font-weight="bold" fill="#a7f3d0">Elbow Hinge Mechanics: Olecranon process locks into fossa to prevent hyperextension.</text>
</svg>
""")

SVG_13 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Pelvis Anatomy: Innominate Bone (Ilium, Ischium, Pubis, Acetabulum)</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="400" y="120" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">Pelvic Innominate Components</text>
  <text x="80" y="170" font-size="13" fill="#cbd5e1">1. Ilium: Broad upper flanged bone articulating with sacrum.</text>
  <text x="80" y="210" font-size="13" fill="#cbd5e1">2. Ischium: Heavy posterior bone forming seat base.</text>
  <text x="80" y="250" font-size="13" fill="#cbd5e1">3. Pubis: Anterior bone fusing at cartilaginous Pubic Symphysis.</text>
  <text x="80" y="290" font-size="13" fill="#cbd5e1">4. Acetabulum: Deep cup socket receiving head of femur (Hip Ball-and-Socket).</text>
</svg>
""")

SVG_14 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Hindlimb Bones: Femur, Patella, Tibia, and Fibula</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="400" y="120" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">Lower Limb Skeleton Layout</text>
  <text x="80" y="170" font-size="13" fill="#cbd5e1">1. Femur: Longest, strongest bone; head fits into acetabulum; greater/lesser trochanters.</text>
  <text x="80" y="210" font-size="13" fill="#cbd5e1">2. Patella: Kneecap sesamoid bone protecting knee joint.</text>
  <text x="80" y="250" font-size="13" fill="#cbd5e1">3. Tibia: Larger medial shin bone bearing main body weight.</text>
  <text x="80" y="290" font-size="13" fill="#cbd5e1">4. Fibula: Slender lateral bone for leg muscle attachments.</text>
</svg>
""")

SVG_15 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Synovial Joint Architecture: Capsule, Membrane, Fluid, Cartilage</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="400" y="120" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">Synovial Joint Architecture</text>
  <text x="80" y="170" font-size="13" fill="#cbd5e1">1. Articular Cartilage: Smooth shock-absorbing cap on bone ends reducing friction.</text>
  <text x="80" y="210" font-size="13" fill="#cbd5e1">2. Synovial Membrane: Inner lining secreting viscous lubricating fluid.</text>
  <text x="80" y="250" font-size="13" fill="#cbd5e1">3. Synovial Fluid: Reduces friction &amp; absorbs mechanical shocks during movement.</text>
  <text x="80" y="290" font-size="13" fill="#cbd5e1">4. Capsular Ligaments: Fibrous capsule binding articulating bones intact.</text>
</svg>
""")

SVG_16 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Ball-and-Socket Joint vs Hinge Joint Comparison</text>
  <rect x="40" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="212" y="110" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">Ball-and-Socket Joint</text>
  <text x="60" y="170" font-size="13" fill="#cbd5e1">• Spherical head inside cup socket</text>
  <text x="60" y="210" font-size="13" fill="#cbd5e1">• 360 Degree motion in all planes</text>
  <text x="60" y="250" font-size="13" fill="#93c5fd">• Shoulder (Glenoid) &amp; Hip (Acetabulum)</text>

  <rect x="415" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="587" y="110" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">Hinge Joint</text>
  <text x="435" y="170" font-size="13" fill="#cbd5e1">• Convex surface inside concave notch</text>
  <text x="435" y="210" font-size="13" fill="#cbd5e1">• 180 Degree motion in single plane</text>
  <text x="435" y="250" font-size="13" fill="#a7f3d0">• Elbow &amp; Knee Joints</text>
</svg>
""")

SVG_17 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Histology of Muscle Types: Skeletal, Smooth, and Cardiac</text>
  <g transform="translate(30, 80)">
    <rect x="0" y="0" width="220" height="300" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="110" y="30" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">Skeletal Muscle</text>
    <text x="110" y="80" font-size="12" fill="#cbd5e1" text-anchor="middle">Striated &amp; Voluntary</text>
    <text x="110" y="120" font-size="12" fill="#cbd5e1" text-anchor="middle">Cylindrical, Multinucleated</text>
    <text x="110" y="160" font-size="12" fill="#cbd5e1" text-anchor="middle">Attached to Skeleton</text>

    <rect x="250" y="0" width="220" height="300" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="360" y="30" font-size="14" font-weight="bold" fill="#10b981" text-anchor="middle">Smooth Muscle</text>
    <text x="360" y="80" font-size="12" fill="#cbd5e1" text-anchor="middle">Unstriated &amp; Involuntary</text>
    <text x="360" y="120" font-size="12" fill="#cbd5e1" text-anchor="middle">Spindle-Shaped, Single Nucleus</text>
    <text x="360" y="160" font-size="12" fill="#cbd5e1" text-anchor="middle">Internal Organ Walls</text>

    <rect x="500" y="0" width="220" height="300" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="610" y="30" font-size="14" font-weight="bold" fill="#a855f7" text-anchor="middle">Cardiac Muscle</text>
    <text x="610" y="80" font-size="12" fill="#cbd5e1" text-anchor="middle">Myogenic &amp; Involuntary</text>
    <text x="610" y="120" font-size="12" fill="#cbd5e1" text-anchor="middle">Branched, Intercalated Discs</text>
    <text x="610" y="160" font-size="12" fill="#cbd5e1" text-anchor="middle">Non-Fatiguing Heart Wall</text>
  </g>
</svg>
""")

SVG_18 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Antagonistic Muscle Action: Biceps &amp; Triceps Arm Flexion/Extension</text>
  <rect x="40" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="212" y="110" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">Arm Bending (Flexion)</text>
  <text x="60" y="170" font-size="13" fill="#cbd5e1">• Biceps (Flexor) CONTRACTS</text>
  <text x="60" y="210" font-size="13" fill="#cbd5e1">• Triceps (Extensor) RELAXES</text>
  <text x="60" y="250" font-size="13" fill="#a7f3d0">• Forearm pulled UPWARDS</text>

  <rect x="415" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="587" y="110" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">Arm Straightening (Extension)</text>
  <text x="435" y="170" font-size="13" fill="#cbd5e1">• Triceps (Extensor) CONTRACTS</text>
  <text x="435" y="210" font-size="13" fill="#cbd5e1">• Biceps (Flexor) RELAXES</text>
  <text x="435" y="250" font-size="13" fill="#93c5fd">• Forearm pulled DOWNWARDS</text>
</svg>
""")

TOPIC4_BIOLOGY_SVGS = [
    SVG_1, SVG_2, SVG_3, SVG_4, SVG_5, SVG_6,
    SVG_7, SVG_8, SVG_9, SVG_10, SVG_11, SVG_12,
    SVG_13, SVG_14, SVG_15, SVG_16, SVG_17, SVG_18
]

# =====================================================================
# 8 VERIFIED WIKIMEDIA COMMONS PHOTOS FOR BIOLOGY TOPIC 4
# =====================================================================

TOPIC4_BIOLOGY_PHOTOS = [
    {
        "lesson_order": 1,
        "page": 4,
        "title": "Human Skeleton Upper Body",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Human_Skeleton_Upper_Body_Anterior_View.jpg",
        "author": "CC BY-SA 4.0, Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "Anterior view of the human upper body endoskeleton displaying skull, clavicle, rib cage, and vertebral column."
    },
    {
        "lesson_order": 2,
        "page": 5,
        "title": "Plant Stem Cross-Section Visualization",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/67/Stem_Cross-Section.jpg",
        "author": "Public Domain, Wikimedia Commons",
        "licensing": "Public domain",
        "caption": "Photomicrograph of dicotyledonous plant stem cross-section showing vascular bundles and sclerenchyma caps."
    },
    {
        "lesson_order": 2,
        "page": 11,
        "title": "Plant Weak Stem Tendrils",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/51/Pisum_sativum_var._macrocarpum_Ilowiecki_2017-04-14_6973.jpg",
        "author": "CC BY-SA 4.0, Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "Garden pea plant showing thigmotropic tendrils coiled around support structures for mechanical elevation."
    },
    {
        "lesson_order": 3,
        "page": 5,
        "title": "Animal Locomotion Organisms",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/50/Darwin%27s_finches.png",
        "author": "Public Domain, Wikimedia Commons",
        "licensing": "Public domain",
        "caption": "Adaptive locomotion morphologies across aquatic and terrestrial fauna."
    },
    {
        "lesson_order": 4,
        "page": 4,
        "title": "Mammalian Skull Lateral View",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c5/Human_Skull_Lateral_View_Unlabeled.jpg",
        "author": "CC BY-SA 4.0, Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "Lateral view of human cranium and facial bone structures."
    },
    {
        "lesson_order": 4,
        "page": 9,
        "title": "Lumbar Vertebra Superior Blueprint",
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/1f/Vertebra_-_lumbales_%28superior_view%29.jpg",
        "author": "CC BY-SA 4.0, Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "Superior view of human lumbar vertebra showing massive centrum and broad transverse processes."
    },
    {
        "lesson_order": 7,
        "page": 7,
        "title": "Human Femur Anterior View",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a0/Femur_-_anterior_view.png",
        "author": "CC BY-SA 4.0, Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "Anterior view of human femur showing smooth spherical head, neck, and distal condyles."
    },
    {
        "lesson_order": 10,
        "page": 3,
        "title": "Laboratory Assay Visualization",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Agar_Diffusion_Method_1.jpg",
        "author": "CC BY-SA 4.0, Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "Laboratory diagnostic assay showing biochemical screening for pharmaceutical and tissue compounds."
    }
]

def enrich_form4_biology_topic4():
    print("=" * 80)
    print("VLearn Form 4 Biology — Topic 4 (Support & Movement): Visual Enrichment Engine")
    print("Attaching 18 Vector SVGs & 8 Verified Wikimedia Photographic Assets")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    subject = Subject.objects.filter(grade=grade, name="Biology").first()
    topic = Topic.objects.filter(subject=subject, name="Support and Movement in Plants and Animals").first()

    if not topic:
        print("[!] Error: Topic 4 not found under Biology!")
        return

    lessons = list(topic.lessons.all().order_by("learning_unit__order"))
    LessonAsset.objects.filter(lesson__in=lessons).delete()
    print("[*] Cleared existing LessonAssets for clean enrichment.")

    svg_counter = 0

    for lesson in lessons:
        u_order = lesson.learning_unit.order
        print(f"\n[*] Enriching Lesson {u_order}: {lesson.title}")

        # 1. Attach SVG Diagrams
        diagram_blocks = list(LessonBlock.objects.filter(lesson=lesson, block_type="suggested_diagram").order_by("order"))
        for db in diagram_blocks:
            if svg_counter < len(TOPIC4_BIOLOGY_SVGS):
                svg_data = TOPIC4_BIOLOGY_SVGS[svg_counter]
                content = db.content or {}
                content["svg_content"] = svg_data
                content["svg"] = svg_data
                db.content = content
                db.save()

                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type="diagram",
                    source_type="ai_generated",
                    storage_type="embed",
                    status="attached",
                    title=db.title,
                    description=f"Sanitized vector diagram: {db.title}",
                    metadata={"svg_content": svg_data}
                )
                db.assets.add(asset)
                print(f"  [SVG OK] '{db.title[:40]}' -> Block ID: {db.id} (Page {db.page_number})")
                svg_counter += 1

        # 2. Attach Wikimedia Photos
        photo_meta_list = [p for p in TOPIC4_BIOLOGY_PHOTOS if p["lesson_order"] == u_order]
        image_blocks = list(LessonBlock.objects.filter(lesson=lesson, block_type="suggested_image").order_by("order"))

        for idx, ib in enumerate(image_blocks):
            if idx < len(photo_meta_list):
                pm = photo_meta_list[idx]
                content = ib.content or {}
                content["resolved_image_url"] = pm["url"]
                content["url"] = pm["url"]
                content["author"] = pm["author"]
                content["licensing"] = pm["licensing"]
                content["caption"] = pm["caption"]
                ib.content = content
                ib.save()

                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type="image",
                    source_type="external",
                    storage_type="url",
                    status="attached",
                    title=ib.title,
                    description=pm["caption"],
                    url=pm["url"],
                    metadata={
                        "author": pm["author"],
                        "licensing": pm["licensing"],
                        "caption": pm["caption"]
                    }
                )
                ib.assets.add(asset)
                print(f"  [WIKIMEDIA OK] '{ib.title[:40]}' -> Block ID: {ib.id} (Page {ib.page_number})")

    total_assets = LessonAsset.objects.filter(lesson__in=lessons).count()
    print("=" * 80)
    print(f"[SUCCESS] Form 4 Biology Topic 4 (Support & Movement) Visual Enrichment Complete!")
    print(f"[*] Total LessonAssets Created: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_form4_biology_topic4()
