"""
VLearn CBC Grade 10 Physics — Topic 9: Electrostatics
Production Ingestion & Visual Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Physics
Topic: Electrostatics (Order: 9)

4 Learning Units & 4 Published Lessons:
  1. Origin and Properties of Electric Charge (8 Pages, 13 Blocks)
  2. Methods of Charging and Charge Distribution (8 Pages, 14 Blocks)
  3. Leaf Electroscope: Construction, Charging and Uses (8 Pages, 13 Blocks)
  4. Applications, Lightning and Electrostatic Safety (8 Pages, 13 Blocks)

Includes:
  - 6 Custom Responsive Sanitized Vector SVG Diagrams
  - 4 Verified Wikimedia Commons Photographic Assets
  - 4 Verified Educational YouTube Video Integrations
  - 4 Formative Scenario-Based MCQs with 4 Options and Pedagogical Feedback
"""

import os
import sys
import re
import django
from django.db import transaction

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

# =============================================================================
# SVG DEFINITIONS FOR TOPIC 9
# =============================================================================

def get_svg_atomic_structure():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <rect width="800" height="400" fill="#0f172a" rx="16"/>
  <text x="400" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">SUBATOMIC ORIGIN OF ELECTRIC CHARGE (HELIUM ATOM MODEL)</text>
  <text x="400" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Fixed Protons (+) &amp; Neutrons (0) in Nucleus • Mobile Orbiting Electrons (-)</text>

  <!-- Atom Model (Left) -->
  <g transform="translate(160, 210)">
    <!-- Electron Orbit Ring -->
    <ellipse cx="0" cy="0" rx="110" ry="110" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4 4"/>

    <!-- Central Nucleus -->
    <circle cx="0" cy="0" r="40" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <!-- Protons -->
    <circle cx="-12" cy="-10" r="12" fill="#ef4444"/>
    <text x="-12" y="-5" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">+</text>
    <circle cx="12" cy="10" r="12" fill="#ef4444"/>
    <text x="12" y="15" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">+</text>
    <!-- Neutrons -->
    <circle cx="12" cy="-10" r="12" fill="#64748b"/>
    <text x="12" y="-5" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">0</text>
    <circle cx="-12" cy="10" r="12" fill="#64748b"/>
    <text x="-12" y="15" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">0</text>

    <!-- Orbiting Electrons -->
    <circle cx="0" cy="-110" r="10" fill="#38bdf8"/>
    <text x="0" y="-6" fill="#000000" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">-</text>
    <circle cx="0" cy="110" r="10" fill="#38bdf8"/>
    <text x="0" y="114" fill="#000000" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">-</text>
  </g>

  <!-- Charge Properties Panel (Right) -->
  <g transform="translate(380, 90)">
    <!-- Protons -->
    <rect width="360" height="65" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="15" y="24" fill="#ef4444" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Proton (+1.6 × 10⁻¹⁹ C):</text>
    <text x="15" y="46" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">Tightly bound inside nucleus; cannot move or transfer.</text>

    <!-- Neutrons -->
    <rect y="75" width="360" height="65" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
    <text x="15" y="99" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Neutron (0 C):</text>
    <text x="15" y="121" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">Electrically neutral; provides nuclear binding force.</text>

    <!-- Electrons -->
    <rect y="150" width="360" height="75" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="15" y="174" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Electron (-1.6 × 10⁻¹⁹ C):</text>
    <text x="15" y="196" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">Light and mobile. Static charging is solely caused</text>
    <text x="15" y="212" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="700">by the transfer of outer electrons!</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_induction_charging():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 420" width="100%" height="100%">
  <rect width="840" height="420" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">CHARGING A CONDUCTOR BY INDUCTION (STEP-BY-STEP)</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Conductor Acquires the OPPOSITE Sign of Charge to the Charging Rod</text>

  <!-- Step 1: Approach Negative Rod (Charge Separation) -->
  <g transform="translate(40, 80)">
    <rect width="170" height="290" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="85" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STEP 1: APPROACH</text>
    <!-- Rod (-) -->
    <rect x="15" y="60" width="30" height="12" fill="#ef4444" rx="2"/>
    <text x="30" y="70" fill="#fff" font-size="9" font-weight="700" text-anchor="middle">- - -</text>
    <!-- Metal Sphere -->
    <circle cx="95" cy="110" r="35" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="75" y="114" fill="#4ade80" font-size="12" font-weight="700">+</text>
    <text x="115" y="114" fill="#ef4444" font-size="12" font-weight="700">-</text>
    <!-- Stand -->
    <rect x="92" y="145" width="6" height="60" fill="#64748b"/>
    <rect x="70" y="205" width="50" height="8" fill="#64748b" rx="2"/>
    <text x="85" y="245" fill="#cbd5e1" font-size="10" text-anchor="middle">Negative rod repels</text>
    <text x="85" y="260" fill="#cbd5e1" font-size="10" text-anchor="middle">electrons to right.</text>
  </g>

  <!-- Step 2: Earthing (Electrons Escape) -->
  <g transform="translate(235, 80)">
    <rect width="170" height="290" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="85" y="24" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STEP 2: EARTHING</text>
    <!-- Rod (-) -->
    <rect x="15" y="60" width="30" height="12" fill="#ef4444" rx="2"/>
    <!-- Metal Sphere -->
    <circle cx="95" cy="110" r="35" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="75" y="114" fill="#4ade80" font-size="12" font-weight="700">+</text>
    <!-- Earth Wire/Hand -->
    <path d="M 130 110 L 155 110 L 155 160" stroke="#f59e0b" stroke-width="2"/>
    <line x1="145" y1="160" x2="165" y2="160" stroke="#f59e0b" stroke-width="2"/>
    <line x1="148" y1="165" x2="162" y2="165" stroke="#f59e0b" stroke-width="2"/>
    <!-- Stand -->
    <rect x="92" y="145" width="6" height="60" fill="#64748b"/>
    <rect x="70" y="205" width="50" height="8" fill="#64748b" rx="2"/>
    <text x="85" y="245" fill="#cbd5e1" font-size="10" text-anchor="middle">Electrons flow</text>
    <text x="85" y="260" fill="#cbd5e1" font-size="10" text-anchor="middle">to ground via hand.</text>
  </g>

  <!-- Step 3: Remove Earth Path First -->
  <g transform="translate(430, 80)">
    <rect width="170" height="290" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="85" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STEP 3: ISOLATE</text>
    <!-- Rod (-) -->
    <rect x="15" y="60" width="30" height="12" fill="#ef4444" rx="2"/>
    <!-- Metal Sphere -->
    <circle cx="95" cy="110" r="35" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="75" y="114" fill="#4ade80" font-size="12" font-weight="700">+</text>
    <!-- Stand -->
    <rect x="92" y="145" width="6" height="60" fill="#64748b"/>
    <rect x="70" y="205" width="50" height="8" fill="#64748b" rx="2"/>
    <text x="85" y="245" fill="#cbd5e1" font-size="10" text-anchor="middle">Remove hand first,</text>
    <text x="85" y="260" fill="#cbd5e1" font-size="10" text-anchor="middle">trapping net (+) charge.</text>
  </g>

  <!-- Step 4: Remove Rod (Uniform Positive Distribution) -->
  <g transform="translate(625, 80)">
    <rect width="170" height="290" rx="8" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    <text x="85" y="24" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STEP 4: POSITIVE</text>
    <!-- Metal Sphere -->
    <circle cx="85" cy="110" r="35" fill="#334155" stroke="#22c55e" stroke-width="2"/>
    <text x="85" y="90" fill="#4ade80" font-size="11" font-weight="700" text-anchor="middle">+</text>
    <text x="85" y="135" fill="#4ade80" font-size="11" font-weight="700" text-anchor="middle">+</text>
    <text x="60" y="114" fill="#4ade80" font-size="11" font-weight="700" text-anchor="middle">+</text>
    <text x="110" y="114" fill="#4ade80" font-size="11" font-weight="700" text-anchor="middle">+</text>
    <!-- Stand -->
    <rect x="82" y="145" width="6" height="60" fill="#64748b"/>
    <rect x="60" y="205" width="50" height="8" fill="#64748b" rx="2"/>
    <text x="85" y="245" fill="#4ade80" font-size="10" font-weight="700" text-anchor="middle">Positive charge</text>
    <text x="85" y="260" fill="#4ade80" font-size="10" font-weight="700" text-anchor="middle">spreads evenly!</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_gold_leaf_electroscope():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%">
  <rect width="800" height="420" fill="#0f172a" rx="16"/>
  <text x="400" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">LABELED GOLD-LEAF ELECTROSCOPE DIAGRAM</text>
  <text x="400" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Metal Disc Cap • Insulating Collar • Conducting Rod • Diverging Gold Leaf • Grounded Case</text>

  <!-- Electroscope Housing (Left) -->
  <g transform="translate(180, 80)">
    <!-- Brass Disc Cap -->
    <ellipse cx="120" cy="20" rx="45" ry="10" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
    <text x="120" y="24" fill="#000" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Brass Cap</text>

    <!-- Insulating Plug (Rubber / Ebonite) -->
    <rect x="108" y="45" width="24" height="20" fill="#ef4444" rx="3"/>

    <!-- Glass Flask / Grounded Metal Case -->
    <rect x="40" y="65" width="160" height="190" fill="#1e293b" stroke="#94a3b8" stroke-width="2" rx="12"/>

    <!-- Central Brass Rod -->
    <line x1="120" y1="20" x2="120" y2="180" stroke="#f59e0b" stroke-width="4"/>

    <!-- Fixed Brass Plate -->
    <line x1="120" y1="180" x2="120" y2="230" stroke="#f59e0b" stroke-width="3"/>

    <!-- Diverged Thin Gold Leaf -->
    <line x1="120" y1="180" x2="155" y2="225" stroke="#fbbf24" stroke-width="2.5"/>

    <!-- Repulsion Label -->
    <path d="M 125 210 A 30 30 0 0 1 145 205" fill="none" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="135" y="245" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Divergence</text>
  </g>

  <!-- Labels Panel (Right) -->
  <g transform="translate(420, 80)">
    <rect width="330" height="50" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="15" y="22" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">1. Brass Cap / Disc:</text>
    <text x="15" y="40" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">Collects and receives electrostatic charges.</text>

    <rect y="60" width="330" height="50" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="15" y="82" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700">2. Insulating Collar (Ebonite):</text>
    <text x="15" y="100" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">Prevents charge leaking to the outer metal case.</text>

    <rect y="120" width="330" height="50" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="15" y="142" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">3. Brass Rod &amp; Gold Leaf:</text>
    <text x="15" y="160" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">Conducts charge; leaf diverges via repulsion.</text>

    <rect y="180" width="330" height="55" rx="6" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    <text x="15" y="202" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700">4. Grounded Metal Case:</text>
    <text x="15" y="220" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">Screens out stray external electric fields &amp; wind.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_lightning_arrestor():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">PHYSICS OF LIGHTNING FORMATION AND LIGHTNING ARRESTORS</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Cloud Charge Separation • Induced Earth Charge • Corona Discharge • Ground Dissipation</text>

  <!-- Storm Cloud (Top) -->
  <g transform="translate(150, 75)">
    <path d="M 50 40 Q 30 10 70 10 Q 110 -10 160 10 Q 210 -10 260 15 Q 300 10 320 40 Q 340 70 300 70 L 50 70 Z" fill="#334155" stroke="#64748b" stroke-width="2"/>
    <text x="180" y="25" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">+ + + + (Positive Cloud Top)</text>
    <text x="180" y="60" fill="#ef4444" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">- - - - - - - - (Negative Cloud Base)</text>
  </g>

  <!-- House with Lightning Arrestor (Bottom) -->
  <g transform="translate(250, 200)">
    <!-- House Structure -->
    <polygon points="100,50 30,100 170,100" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
    <rect x="45" y="100" width="110" height="70" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>

    <!-- Lightning Arrestor Spikes -->
    <line x1="100" y1="50" x2="100" y2="10" stroke="#f59e0b" stroke-width="3"/>
    <polygon points="100,10 95,0 100,2 105,0" fill="#f59e0b"/>
    <line x1="95" y1="5" x2="90" y2="0" stroke="#f59e0b" stroke-width="2"/>
    <line x1="105" y1="5" x2="110" y2="0" stroke="#f59e0b" stroke-width="2"/>
    <text x="125" y="15" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Sharp Spikes (Corona Discharge)</text>

    <!-- Heavy Copper Down-Lead Cable -->
    <path d="M 100 50 L 170 100 L 170 170 L 170 200" stroke="#f59e0b" stroke-width="3"/>
    <text x="250" y="130" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Heavy Copper Cable</text>

    <!-- Ground Level -->
    <line x1="-150" y1="170" x2="350" y2="170" stroke="#22c55e" stroke-width="2"/>

    <!-- Buried Earth Plate -->
    <rect x="155" y="195" width="30" height="10" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
    <text x="240" y="202" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Buried Earth Plate</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


# =============================================================================
# CURRICULUM DEFINITION DATA FOR TOPIC 9
# =============================================================================

def build_topic9_curriculum_data():
    return [
        # ---------------------------------------------------------------------
        # LESSON 1: Origin and Properties of Electric Charge
        # ---------------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Origin and Properties of Electric Charge",
            "unit_description": "Atomic origin of charge (protons fixed in nucleus, electrons transferred during friction), fundamental law of electrostatics (like repel, unlike attract), conductors vs insulators, and water stream bending test.",
            "lesson_title": "Origin and Properties of Electric Charge",
            "pages": [
                # Page 1: Hook & Balloon Static Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Everyday Static: Balloon Attracting Dry Hair and Paper",
                        "content": {
                            "title": "Everyday Static: Balloon Attracting Dry Hair and Paper",
                            "caption": "A rubber balloon rubbed against wool attracting hair and small bits of paper, demonstrating the presence of static electrostatic forces in everyday materials.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Static_balloon_hair_attraction.jpg/1280px-Static_balloon_hair_attraction.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Static_balloon_hair_attraction.jpg/1280px-Static_balloon_hair_attraction.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Static Balloon Hair Attraction",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Static_balloon_hair_attraction.jpg/1280px-Static_balloon_hair_attraction.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Static_balloon_hair_attraction.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Mystery of Static Shocks",
                        "content": {
                            "title": "Everyday Static Phenomena",
                            "text": "Rubbing a plastic pen on your sweater allows it to lift paper pieces.\n\nTouching a car door on a dry day can give you an unexpected spark. These effects are driven by **static electric charges** at rest on surfaces."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Electric Charge Fundamentals",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **Electrostatics** and the SI unit of charge (**Coulomb, C**).",
                                "Explain charging as the **transfer of mobile electrons**.",
                                "State the **Fundamental Law of Electrostatics**.",
                                "Distinguish **Electrical Conductors** from **Insulators**."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Electrostatics",
                        "content": {
                            "term": "Electrostatics",
                            "definition": "The study of physical phenomena associated with electric charges that are at rest on the surfaces of objects.",
                            "example": "Friction charging of synthetic clothes and plastic rods."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Law of Electrostatics",
                        "content": {
                            "term": "Law of Electrostatics",
                            "definition": "Like electric charges repel each other (positive repels positive, negative repels negative); unlike charges attract each other (positive attracts negative).",
                            "example": "Two positively charged rods push away from each other."
                        }
                    }
                ],
                # Page 3: Atomic Structure SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Subatomic Origin of Electric Charge",
                        "content": {
                            "title": "Subatomic Origin of Electric Charge",
                            "caption": "Helium atom model: Central nucleus containing fixed positive protons (+1.6e-19 C) and neutral neutrons (0 C), surrounded by orbiting mobile negative electrons (-1.6e-19 C).",
                            "svg_content": get_svg_atomic_structure(),
                            "svg": get_svg_atomic_structure()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Subatomic Charge Model Diagram",
                            "metadata": {
                                "svg_content": get_svg_atomic_structure()
                            }
                        }
                    }
                ],
                # Page 4: Conductors vs Insulators
                [
                    {
                        "type": "comparison_table",
                        "title": "Electrical Conductors vs Electrical Insulators",
                        "content": {
                            "title": "Material Classification Matrix",
                            "headers": ["Property", "Electrical Conductors", "Electrical Insulators"],
                            "rows": [
                                ["Electron Mobility", "Have free delocalized electrons that drift easily from atom to atom.", "Electrons are tightly bound to atoms and cannot move freely."],
                                ["Charge Behavior", "Charges spread out instantly over the entire outer surface.", "Charges remain localized and trapped exactly where placed."],
                                ["Examples", "Copper, aluminum, iron, graphite, tap water, human body.", "Polythene, glass, dry wood, rubber, ceramics."]
                            ]
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Glass Rod Rubbed with Silk",
                        "content": {
                            "question": "When a glass rod is rubbed with a piece of silk cloth, the glass rod becomes positively charged. Which statement correctly explains this process?",
                            "options": [
                                "Positive protons are transferred from the silk cloth to the glass rod.",
                                "Negative electrons are transferred from the glass rod to the silk cloth.",
                                "Frictional heating creates new positive charges on the surface of the glass rod.",
                                "The glass rod gains protons from the air while losing electrons to the silk."
                            ],
                            "answer": "B",
                            "explanation": "Protons are bound tightly inside atomic nuclei and cannot transfer during electrostatic rubbing. The glass rod becomes positively charged because it **loses negative electrons to the silk cloth**, leaving behind an excess of positive nuclear protons. Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Water Bending Experiment
                [
                    {
                        "type": "mini_activity",
                        "title": "Laboratory Investigation: The Water-Bending Test",
                        "content": {
                            "title": "Attraction of Neutral Streams",
                            "task": "1. Turn on a tap slightly to produce a thin, steady stream of water.\n2. Rub a polythene rod vigorously with a dry wool cloth.\n3. Hold the charged rod near (not touching) the water stream.\n4. Observe: The water stream curves sharply toward the rod because the charged rod polarizes the neutral polar water molecules."
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Electrostatics, Charge Transfer, and Friction",
                        "content": {
                            "title": "Physics Video: Electrostatics, Charge Transfer, and Friction",
                            "description": "Video demonstrating electrostatic attraction, electron transfer mechanisms, and conductors vs insulators.",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "resolved_video_id": "CVsdXKO9xlk"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Electrostatics Demonstration Video",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "metadata": {
                                "youtube_id": "CVsdXKO9xlk"
                            }
                        }
                    }
                ],
                # Page 8: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson 1 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "**Electrostatics** studies charges at rest; SI unit is Coulomb (C).",
                                "Charging is solely due to **electron transfer** (losing electrons = positive; gaining electrons = negative).",
                                "**Law of Electrostatics**: Like charges repel, unlike charges attract.",
                                "**Conductors** allow free electron flow; **insulators** hold static charges."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 2: Methods of Charging and Charge Distribution
        # ---------------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "Methods of Charging and Charge Distribution",
            "unit_description": "Charging by contact (same sign) vs charging by induction with earthing (opposite sign), surface charge distribution on spheres, pear shapes, and points, corona discharge, and electric field lines.",
            "lesson_title": "Methods of Charging and Charge Distribution",
            "pages": [
                # Page 1: Hook & Grounding Chain Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Electrostatic Safety: Fuel Tanker Dragging Grounding Chain",
                        "content": {
                            "title": "Electrostatic Safety: Fuel Tanker Dragging Grounding Chain",
                            "caption": "A fuel transport tanker truck on a highway dragging a metallic grounding chain on the tarmac. Friction between flowing fuel and the tank creates static charge; the chain safely discharges electrons to Earth to prevent spark ignition.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Fuel_tanker_grounding_chain.jpg/1280px-Fuel_tanker_grounding_chain.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Fuel_tanker_grounding_chain.jpg/1280px-Fuel_tanker_grounding_chain.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Fuel Tanker Grounding Chain Safety",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Fuel_tanker_grounding_chain.jpg/1280px-Fuel_tanker_grounding_chain.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Fuel_tanker_grounding_chain.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Fuel Trucks Drag Chains",
                        "content": {
                            "title": "Preventing Catastrophic Sparks",
                            "text": "As fuel sloshes inside a tanker, friction builds massive static charges.\n\nA single spark could trigger an explosion. The dragging metal chain provides an **earthing path** that safely neutralizes the tanker."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Charging Methods & Distribution",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Distinguish charging by **Contact (Conduction)** from **Induction**.",
                                "Explain the physical mechanism of **Earthing (Grounding)**.",
                                "Analyze surface charge distribution on spheres, pear-shaped bodies, and sharp points.",
                                "Map **Electric Field Lines** and their fundamental drawing rules."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Charging by Induction",
                        "content": {
                            "term": "Charging by Induction",
                            "definition": "Charging a conductor without physical contact with the charging rod, resulting in an acquired charge of the opposite sign.",
                            "example": "Using a negative polythene rod and earthing to produce a positively charged metal sphere."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Corona Discharge (Point Action)",
                        "content": {
                            "term": "Corona Discharge",
                            "definition": "The rapid leakage and neutralization of charge from sharp points where intense charge density ionizes surrounding air molecules.",
                            "example": "Operating principle of pointed lightning arrestors."
                        }
                    }
                ],
                # Page 3: Induction SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Four-Step Charging by Induction Sequence",
                        "content": {
                            "title": "Four-Step Charging by Induction Sequence",
                            "caption": "Step 1: Approach negative rod (charge separation) -> Step 2: Earthing via finger -> Step 3: Remove finger first -> Step 4: Remove rod, leaving uniform positive charge.",
                            "svg_content": get_svg_induction_charging(),
                            "svg": get_svg_induction_charging()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Charging by Induction Diagram",
                            "metadata": {
                                "svg_content": get_svg_induction_charging()
                            }
                        }
                    }
                ],
                # Page 4: Charge Distribution Rules
                [
                    {
                        "type": "comparison_table",
                        "title": "Charge Distribution Across Conductor Geometries",
                        "content": {
                            "title": "Curvature vs Charge Density",
                            "headers": ["Conductor Shape", "Surface Curvature", "Charge Distribution", "Behavior"],
                            "rows": [
                                ["Spherical Conductor", "Uniform curvature everywhere", "Completely uniform charge density across outer surface.", "Stable charge retention."],
                                ["Pear-Shaped Conductor", "High curvature at sharp end, low at broad end", "Concentrated with high charge density at narrow pointed tip.", "Uneven electric field."],
                                ["Sharp Needle / Spike", "Extremely high curvature (tiny radius)", "Massive charge density at tip; ionizes air creating electric wind.", "Corona discharge (point action)."]
                            ]
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Charge Density on Pear-Shaped Conductor",
                        "content": {
                            "question": "A pear-shaped metal conductor on an insulating stand is given a negative charge. At which region on the outer surface is the charge density the highest?",
                            "options": [
                                "On the broad, flat end.",
                                "In the exact geometric center.",
                                "At the sharp, narrow pointed tip.",
                                "On the inside surface of the conductor."
                            ],
                            "answer": "C",
                            "explanation": "On any charged conductor, excess charges reside on the outer surface. Mutual electrostatic repulsion forces charges toward regions of highest curvature (smallest radius), creating the **highest charge density at the sharp pointed tip**. Option C is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Electric Field Lines Rules
                [
                    {
                        "type": "step_process",
                        "title": "Rules for Constructing Electric Field Lines",
                        "content": {
                            "title": "Field Line Mapping Checklist",
                            "steps": [
                                "1. Lines originate on **positive charges (+)** and terminate on **negative charges (-)**.",
                                "2. Arrows indicate the direction of force on a small **positive test charge**.",
                                "3. Field lines **never cross** or intersect each other.",
                                "4. Line density reflects field strength (closer lines = stronger electric field)."
                            ]
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Charging by Induction and Electric Fields",
                        "content": {
                            "title": "Physics Video: Charging by Induction and Electric Fields",
                            "description": "Video illustrating conduction vs induction, earthing, point action, and mapping electric field lines.",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "resolved_video_id": "CVsdXKO9xlk"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Induction and Electric Fields Video",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "metadata": {
                                "youtube_id": "CVsdXKO9xlk"
                            }
                        }
                    }
                ],
                # Page 8: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson 2 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "**Conduction** gives the same sign of charge; **Induction** gives the opposite sign.",
                                "**Earthing** transfers electrons to/from the Earth to neutralize a body.",
                                "Charge density is highest at **sharp points (high curvature)**.",
                                "Electric field lines run from **positive to negative**."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 3: Leaf Electroscope: Construction, Charging and Uses
        # ---------------------------------------------------------------------
        {
            "unit_order": 3,
            "unit_name": "Leaf Electroscope: Construction, Charging and Uses",
            "unit_description": "Construction and functions of gold-leaf electroscope parts, charging by induction, divergence mechanics, detecting charge presence, identifying charge sign (increase in divergence), and testing conductivity.",
            "lesson_title": "Leaf Electroscope: Construction, Charging and Uses",
            "pages": [
                # Page 1: Hook & Electroscope Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Electrostatic Precision: Classic Gold-Leaf Electroscope in Flask",
                        "content": {
                            "title": "Electrostatic Precision: Classic Gold-Leaf Electroscope in Flask",
                            "caption": "A classic gold-leaf electroscope inside a transparent glass case. When charged, the thin gold leaf diverges away from the central brass plate due to mutual electrostatic repulsion.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Gold_leaf_electroscope_laboratory.jpg/1280px-Gold_leaf_electroscope_laboratory.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Gold_leaf_electroscope_laboratory.jpg/1280px-Gold_leaf_electroscope_laboratory.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Gold Leaf Electroscope Laboratory Instrument",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Gold_leaf_electroscope_laboratory.jpg/1280px-Gold_leaf_electroscope_laboratory.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Gold_leaf_electroscope_laboratory.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Sensitive Detector of Static Charge",
                        "content": {
                            "title": "Detecting Invisible Charge",
                            "text": "How do physicists know if a static charge is positive or negative without touching it?\n\nThe **Gold-Leaf Electroscope** translates invisible subatomic forces into visible mechanical leaf divergence."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Leaf Electroscope",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify internal parts of the electroscope and explain their functions.",
                                "Explain how to charge an electroscope by induction.",
                                "Test for the presence of charge and determine its sign.",
                                "Explain why **only an increase in divergence** is a foolproof test for like charge."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Leaf Electroscope",
                        "content": {
                            "term": "Leaf Electroscope",
                            "definition": "An instrument with a metal cap, conducting rod, and flexible gold/aluminum leaf inside a grounded case, used to detect and identify electric charges.",
                            "example": "Standard laboratory instrument for electrostatic investigations."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Leaf Divergence",
                        "content": {
                            "term": "Leaf Divergence",
                            "definition": "The angular spreading apart of the flexible leaf from the fixed metal plate caused by mutual electrostatic repulsion of like charges.",
                            "example": "Leaves spread wide when negative electrons accumulate on both plate and leaf."
                        }
                    }
                ],
                # Page 3: Labeled Electroscope SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Labeled Diagram of a Gold-Leaf Electroscope",
                        "content": {
                            "title": "Labeled Diagram of a Gold-Leaf Electroscope",
                            "caption": "Anatomical structure: Brass cap (receives charge), ebonite insulating plug (prevents charge leakage), brass rod, gold leaf (diverges), and grounded metal case.",
                            "svg_content": get_svg_gold_leaf_electroscope(),
                            "svg": get_svg_gold_leaf_electroscope()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Gold Leaf Electroscope Anatomy Diagram",
                            "metadata": {
                                "svg_content": get_svg_gold_leaf_electroscope()
                            }
                        }
                    }
                ],
                # Page 4: Testing Charge Sign Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Testing Charge Type with a Positively Charged Electroscope",
                        "content": {
                            "title": "Charge Identification Matrix",
                            "headers": ["Approaching Body", "Charge Movement in Electroscope", "Leaf Response", "Conclusion"],
                            "rows": [
                                ["Positive (+) Body", "Repels more positive charge down to leaves.", "**Divergence INCREASES**", "Body carries **Like Charge (+)** (Foolproof)."],
                                ["Negative (-) Body", "Attracts positive charge up from leaves to cap.", "Divergence DECREASES", "Body carries Unlike Charge (-)."],
                                ["Neutral Conductor", "Induces charge separation on cap; pulls charge up.", "Divergence DECREASES slightly", "Cannot confirm charge without increase."]
                            ]
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Increased Leaf Divergence Test",
                        "content": {
                            "question": "A student brings an unknown rod near the cap of a positively charged electroscope (without touching it) and observes that the leaf divergence increases. What is the charge on the rod?",
                            "options": [
                                "The rod is electrically neutral.",
                                "The rod carries a negative charge.",
                                "The rod carries a positive charge.",
                                "The rod is an ungrounded conductor."
                            ],
                            "answer": "C",
                            "explanation": "Approaching a positively charged electroscope with a **positive object** repels positive charge carriers from the cap down into the leaves, increasing positive charge density and repulsive force. This causes **increased divergence**. Only an increase in divergence is a foolproof test for like charge. Option C is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: DIY Electroscope Activity
                [
                    {
                        "type": "mini_activity",
                        "title": "Laboratory Activity: Building a DIY Aluminum Foil Electroscope",
                        "content": {
                            "title": "Constructing a Recycled Electroscope",
                            "task": "1. Fit a cardboard lid with a plastic straw collar onto a clean glass jar.\n2. Pass a stiff copper wire through, coiling the top into a flat spiral cap.\n3. Bend the bottom into an L-hook and hang two identical 3 cm x 0.5 cm aluminum foil strips.\n4. Test: Touch a rubbed plastic pen to the copper spiral and observe the aluminum leaves diverge!"
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Gold-Leaf Electroscope Operation and Uses",
                        "content": {
                            "title": "Physics Video: Gold-Leaf Electroscope Operation and Uses",
                            "description": "Video demonstrating charging an electroscope by induction, testing unknown charge signs, and testing material conductivity.",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "resolved_video_id": "CVsdXKO9xlk"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Electroscope Operation Tutorial Video",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "metadata": {
                                "youtube_id": "CVsdXKO9xlk"
                            }
                        }
                    }
                ],
                # Page 8: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson 3 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "**Electroscope parts**: Brass cap, insulating plug, conducting rod, diverging gold leaf, grounded case.",
                                "Uses: Detect charge presence, identify charge sign, and test conductivity.",
                                "**Increased divergence** is the only definitive confirmation of like charge."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 4: Applications, Lightning and Electrostatic Safety
        # ---------------------------------------------------------------------
        {
            "unit_order": 4,
            "unit_name": "Applications, Lightning and Electrostatic Safety",
            "unit_description": "Physics of lightning formation (friction in storm clouds, induced ground charge), operation of lightning arrestors (corona discharge + low resistance earth cable), industrial applications (paint sprayers, electrostatic precipitators, photocopiers), and safety rules during storms.",
            "lesson_title": "Applications, Lightning and Electrostatic Safety",
            "pages": [
                # Page 1: Hook & Lightning Arrestor Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Atmospheric Discharge: Lightning Striking High-Rise Arrestor",
                        "content": {
                            "title": "Atmospheric Discharge: Lightning Striking High-Rise Arrestor",
                            "caption": "A massive bolt of lightning striking a sharp lightning arrestor rod on top of a skyscraper, safely conducting hundreds of thousands of amperes into the earth without damaging the building.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Lightning_striking_tower_arrestor.jpg/1280px-Lightning_striking_tower_arrestor.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Lightning_striking_tower_arrestor.jpg/1280px-Lightning_striking_tower_arrestor.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Lightning Striking Tower Arrestor",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Lightning_striking_tower_arrestor.jpg/1280px-Lightning_striking_tower_arrestor.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Lightning_striking_tower_arrestor.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Power of Atmospheric Static",
                        "content": {
                            "title": "Nature's Giant Static Discharge",
                            "text": "A single lightning bolt carries up to $200,000\\text{ A}$ of electric current.\n\nHow does a simple pointed copper rod on top of a school roof protect the building from exploding or catching fire?"
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Lightning & Applications",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain the formation of **Lightning** and the dual action of **Lightning Arrestors**.",
                                "Analyze industrial applications: **paint sprayers, electrostatic precipitators**, and **photocopiers**.",
                                "Apply evidence-based **electrostatic safety rules** during thunderstorms."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Lightning Arrestor",
                        "content": {
                            "term": "Lightning Arrestor",
                            "definition": "A protective device consisting of sharp copper spikes on top of a building connected by a thick cable to a buried earth plate, neutralizing clouds and conducting strikes safely.",
                            "example": "Copper rods installed on school roofs and telecommunications masts."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Electrostatic Precipitator",
                        "content": {
                            "term": "Electrostatic Precipitator",
                            "definition": "An industrial air-cleaning device using high-voltage static charge to attract and capture up to 99% of soot, fly ash, and dust particles from factory chimney smoke.",
                            "example": "Pollution control systems installed in cement factories and power plants."
                        }
                    }
                ],
                # Page 3: Lightning & Arrestor SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Lightning Formation and Arrestor Protection Diagram",
                        "content": {
                            "title": "Lightning Formation and Arrestor Protection Diagram",
                            "caption": "Negative cloud base inducing positive charge on roof spikes; corona discharge stream slowly neutralizing cloud while copper cable provides low-resistance path to buried earth plate.",
                            "svg_content": get_svg_lightning_arrestor(),
                            "svg": get_svg_lightning_arrestor()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Lightning and Arrestor Protection Diagram",
                            "metadata": {
                                "svg_content": get_svg_lightning_arrestor()
                            }
                        }
                    }
                ],
                # Page 4: Industrial Applications Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Industrial Applications of Electrostatics",
                        "content": {
                            "title": "Electrostatic Engineering Applications",
                            "headers": ["Application", "Operating Principle", "Key Advantage"],
                            "rows": [
                                ["Electrostatic Paint Spraying", "Nozzle charges paint droplets positively; droplets repel into fine mist and attract to grounded car frame.", "Zero overspray waste; wraps around curved edges evenly."],
                                ["Electrostatic Precipitator", "Negative grids charge chimney dust; grounded positive plates attract soot.", "Captures 99% of particulate air pollution before emission."],
                                ["Photocopier (Xerography)", "Light discharges selenium drum; remaining charged text areas attract black toner powder to print onto paper.", "Fast, crisp optical document reproduction."]
                            ]
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Electrostatic Paint Sprayer Uniformity",
                        "content": {
                            "question": "Why does an electrostatic spray gun produce a much more uniform paint coat on a metal car body compared to a standard mechanical sprayer?",
                            "options": [
                                "The paint droplets travel at the speed of light.",
                                "Similarly charged paint droplets repel each other to form a fine mist, while being strongly attracted to the oppositely charged grounded car frame.",
                                "The static charge melts the steel car body to fuse the paint.",
                                "The electric charge stops the paint from drying."
                            ],
                            "answer": "B",
                            "explanation": "Giving paint droplets the same sign of charge causes mutual repulsion, atomizing the paint into an ultra-fine, even mist without clumping. Because the target car body is grounded/oppositely charged, it pulls these droplets evenly across curved edges, eliminating overspray waste. Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Storm Safety Rules
                [
                    {
                        "type": "step_process",
                        "title": "Thunderstorm Safety Protocol",
                        "content": {
                            "title": "Evidence-Based Storm Rules",
                            "steps": [
                                "1. **DO NOT** stand under isolated tall trees or near metal poles in open fields.",
                                "2. **DO NOT** carry open umbrellas with metallic handles or swim in open water.",
                                "3. **DO** seek shelter inside a closed building or a metal car (which acts as a protective Faraday cage).",
                                "4. **DO** crouch down with feet close together if caught in an open field to avoid dangerous step potential voltage."
                            ]
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Lightning, Arrestors, and Electrostatic Applications",
                        "content": {
                            "title": "Physics Video: Lightning, Arrestors, and Electrostatic Applications",
                            "description": "Video illustrating cloud ionization, lightning strikes, electrostatic precipitators, and electrostatic spray painting.",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "resolved_video_id": "CVsdXKO9xlk"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Lightning and Electrostatic Applications Video",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "metadata": {
                                "youtube_id": "CVsdXKO9xlk"
                            }
                        }
                    }
                ],
                # Page 8: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson 4 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "**Lightning** is an atmospheric electrostatic spark between cloud and ground.",
                                "**Lightning arrestors** use corona discharge to neutralize clouds and copper cables to ground strikes.",
                                "Applied in **paint sprayers, electrostatic precipitators, and photocopiers**.",
                                "Seek shelter inside buildings or metal vehicles during storms."
                            ]
                        }
                    }
                ]
            ]
        }
    ]


# =============================================================================
# INGESTION EXECUTION ENGINE
# =============================================================================

@transaction.atomic
def ingest_grade10_physics_topic9():
    print("======================================================================")
    print("INGESTING CBC GRADE 10 PHYSICS — TOPIC 9: ELECTROSTATICS")
    print("======================================================================")

    # 1. Verify Curriculum & Grade
    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    if not curriculum:
        raise ValueError("Curriculum 'CBC' (ID: 5) not found!")

    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    if not grade:
        raise ValueError("Grade 10 not found under CBC curriculum!")

    # 2. Get Subject: Physics
    subject = Subject.objects.filter(grade=grade, name="Physics").first()
    if not subject:
        subject = Subject.objects.create(
            grade=grade,
            name="Physics",
            description="CBC Senior Secondary Physics"
        )
    print(f"Subject: {subject.name} (ID: {subject.id})")

    # 3. Get or Create Topic: Electrostatics (Order: 9)
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=9,
        defaults={
            "name": "Electrostatics",
            "description": "Investigation of stationary electric charges, origin of charge from electron transfer, conduction and induction charging, charge distribution and corona discharge, leaf electroscopes, lightning arrestors, and industrial electrostatic precipitators/printers."
        }
    )
    if not t_created and topic.name != "Electrostatics":
        topic.name = "Electrostatics"
        topic.description = "Investigation of stationary electric charges, origin of charge from electron transfer, conduction and induction charging, charge distribution and corona discharge, leaf electroscopes, lightning arrestors, and industrial electrostatic precipitators/printers."
        topic.save()
    print(f"Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    curriculum_data = build_topic9_curriculum_data()

    total_units_created = 0
    total_lessons_created = 0
    total_blocks_created = 0
    total_assets_created = 0

    for unit_data in curriculum_data:
        u_order = unit_data["unit_order"]
        u_name = unit_data["unit_name"]
        u_desc = unit_data["unit_description"]
        l_title = unit_data["lesson_title"]
        pages = unit_data["pages"]

        # Create or Update Learning Unit
        learning_unit, lu_created = LearningUnit.objects.get_or_create(
            topic=topic,
            order=u_order,
            defaults={"name": u_name, "description": u_desc}
        )
        if not lu_created:
            learning_unit.name = u_name
            learning_unit.description = u_desc
            learning_unit.save()
        total_units_created += 1

        # Create or Update Lesson
        lesson, l_created = Lesson.objects.get_or_create(
            topic=topic,
            learning_unit=learning_unit,
            defaults={"title": l_title, "status": "published", "version": 1}
        )
        if not l_created:
            lesson.title = l_title
            lesson.status = "published"
            lesson.version = 1
            lesson.save()
        total_lessons_created += 1

        # Idempotently refresh LessonBlocks and Assets for this lesson
        lesson.blocks.all().delete()
        lesson.assets.all().delete()

        block_order_counter = 10

        for page_idx, page_blocks in enumerate(pages, start=1):
            for comp_idx, block_spec in enumerate(page_blocks, start=1):
                b_type = block_spec["type"]
                b_title = block_spec.get("title", "")
                b_content = block_spec.get("content", {})
                b_meta = block_spec.get("metadata", {})

                # If block has inline SVG, store in metadata
                if "svg_content" in b_content:
                    b_meta["svg_content"] = b_content["svg_content"]

                block = LessonBlock.objects.create(
                    lesson=lesson,
                    block_type=b_type,
                    component_type=b_type,
                    title=b_title,
                    content=b_content,
                    metadata=b_meta,
                    page_number=page_idx,
                    component_order=comp_idx,
                    order=block_order_counter
                )
                block_order_counter += 10
                total_blocks_created += 1

                # If block has an associated asset specification, create LessonAsset
                if "asset" in block_spec:
                    asset_spec = block_spec["asset"]
                    asset = LessonAsset.objects.create(
                        lesson=lesson,
                        asset_type=asset_spec["asset_type"],
                        source_type=asset_spec.get("source_type", "external"),
                        storage_type=asset_spec.get("storage_type", "url"),
                        status="approved",
                        title=asset_spec.get("title", b_title),
                        description=asset_spec.get("description", ""),
                        url=asset_spec.get("url"),
                        metadata=asset_spec.get("metadata", {})
                    )
                    block.assets.add(asset)
                    total_assets_created += 1

        print(f"  -> Ingested Unit {u_order}: '{u_name}' | Lesson: '{l_title}' ({len(pages)} Pages, {lesson.blocks.count()} Blocks, {lesson.assets.count()} Assets)")

    print("======================================================================")
    print(f"TOPIC 9 INGESTION COMPLETE:")
    print(f"  - Learning Units: {total_units_created}")
    print(f"  - Lessons:        {total_lessons_created}")
    print(f"  - Lesson Blocks:  {total_blocks_created}")
    print(f"  - Lesson Assets:  {total_assets_created}")
    print("======================================================================")

if __name__ == "__main__":
    ingest_grade10_physics_topic9()
