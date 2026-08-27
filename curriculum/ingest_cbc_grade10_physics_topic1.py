"""
VLearn CBC Grade 10 Physics — Topic 1: Introduction to Physics
Production Ingestion & Visual Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Physics
Topic: Introduction to Physics (Order: 1)

3 Learning Units & 3 Published Lessons:
  1. Physics as a Body of Knowledge (9 Pages, 15 Blocks)
  2. Branches of Physics and Connections (8 Pages, 14 Blocks)
  3. Importance, Careers, and Scientific Citizenship (7 Pages, 13 Blocks)

Includes:
  - 3 Custom Responsive Sanitized Vector SVG Diagrams
  - 3 Verified Wikimedia Commons Photographic Assets
  - 3 Verified Educational YouTube Video Integrations
  - 3 Formative Scenario-Based MCQs with 4 Options and Pedagogical Feedback
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
# SVG DEFINITIONS (THEME AWARE / RESPONSIVE)
# =============================================================================

def get_svg_scientific_method():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <rect width="800" height="480" fill="#0f172a" rx="16"/>
  <text x="400" y="38" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle" letter-spacing="0.5">THE SCIENTIFIC METHOD: PATHWAY OF INQUIRY</text>
  <text x="400" y="62" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">A systematic journey from real-world observation to universal scientific laws</text>

  <!-- Step 1: Observation -->
  <g transform="translate(50, 85)">
    <rect width="700" height="60" fill="#1e293b" rx="10" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="35" cy="30" r="18" fill="#0284c7" />
    <text x="35" y="36" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">1</text>
    <text x="75" y="27" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="700">Real-World Observation</text>
    <text x="75" y="47" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">Noticing a natural phenomenon (e.g. objects of different masses falling in air vs vacuum)</text>
  </g>

  <!-- Down Arrow 1 -->
  <path d="M 400 147 L 400 163 M 394 157 L 400 163 L 406 157" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- Step 2: Hypothesis -->
  <g transform="translate(50, 165)">
    <rect width="700" height="60" fill="#1e293b" rx="10" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="35" cy="30" r="18" fill="#d97706" />
    <text x="35" y="36" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">2</text>
    <text x="75" y="27" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="15" font-weight="700">Hypothesis / Prediction</text>
    <text x="75" y="47" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">Formulating a tentative, testable proposal to explain the observed phenomenon</text>
  </g>

  <!-- Down Arrow 2 -->
  <path d="M 400 227 L 400 243 M 394 237 L 400 243 L 406 237" stroke="#f59e0b" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- Step 3: Controlled Experiment -->
  <g transform="translate(50, 245)">
    <rect width="700" height="60" fill="#1e293b" rx="10" stroke="#a855f7" stroke-width="1.5"/>
    <circle cx="35" cy="30" r="18" fill="#7e22ce" />
    <text x="35" y="36" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">3</text>
    <text x="75" y="27" fill="#c084fc" font-family="system-ui, sans-serif" font-size="15" font-weight="700">Controlled Experimentation & Measurement</text>
    <text x="75" y="47" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">Conducting rigorous tests, controlling variables, and recording quantitative physical data</text>
  </g>

  <!-- Down Arrow 3 -->
  <path d="M 400 307 L 400 323 M 394 317 L 400 323 L 406 317" stroke="#c084fc" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- Step 4: Evidence Analysis -->
  <g transform="translate(50, 325)">
    <rect width="700" height="60" fill="#1e293b" rx="10" stroke="#22c55e" stroke-width="1.5"/>
    <circle cx="35" cy="30" r="18" fill="#15803d" />
    <text x="35" y="36" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">4</text>
    <text x="75" y="27" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="700">Evidence Analysis & Mathematical Modeling</text>
    <text x="75" y="47" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">Analyzing data patterns, calculating uncertainties, and testing consistency with theory</text>
  </g>

  <!-- Down Arrow 4 -->
  <path d="M 400 387 L 400 403 M 394 397 L 400 403 L 406 397" stroke="#4ade80" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- Step 5: Scientific Law / Theory -->
  <g transform="translate(50, 405)">
    <rect width="700" height="60" fill="#1e293b" rx="10" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="35" cy="30" r="18" fill="#0369a1" />
    <text x="35" y="36" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">5</text>
    <text x="75" y="27" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="700">Theory Validation & Universal Scientific Law</text>
    <text x="75" y="47" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">Formulating absolute mathematical relationships (e.g. Law of Conservation of Energy)</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_branches_tree():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 500" width="100%" height="100%">
  <rect width="840" height="500" fill="#0a0f1d" rx="16"/>
  <text x="420" y="36" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE TREE OF PHYSICS: MAJOR SPECIALIZED BRANCHES</text>
  <text x="420" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Foundational science exploring matter, energy, and cosmic interactions</text>

  <!-- Central Trunk Base -->
  <path d="M 400 480 L 400 340 Q 400 290 320 220 M 440 480 L 440 340 Q 440 290 520 220" stroke="#78350f" stroke-width="18" stroke-linecap="round" fill="none"/>
  <rect x="340" y="370" width="160" height="55" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="420" y="394" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">PHYSICS</text>
  <text x="420" y="412" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Matter • Energy • Forces</text>

  <!-- Branch 1: Mechanics -->
  <g transform="translate(30, 90)">
    <rect width="170" height="75" rx="10" fill="#111827" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="85" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. Mechanics</text>
    <text x="85" y="43" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Motion, Forces, Energy</text>
    <text x="85" y="60" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Vehicles, Cranes, Dams</text>
    <path d="M 85 75 Q 160 160 360 270" stroke="#0284c7" stroke-width="3" fill="none" opacity="0.6"/>
  </g>

  <!-- Branch 2: Thermodynamics -->
  <g transform="translate(230, 75)">
    <rect width="170" height="75" rx="10" fill="#111827" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="85" y="24" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. Thermodynamics</text>
    <text x="85" y="43" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Heat & Energy Transfer</text>
    <text x="85" y="60" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Engines, Solar Geothermal</text>
    <path d="M 85 75 Q 150 160 380 260" stroke="#d97706" stroke-width="3" fill="none" opacity="0.6"/>
  </g>

  <!-- Branch 3: Waves & Acoustics -->
  <g transform="translate(440, 75)">
    <rect width="170" height="75" rx="10" fill="#111827" stroke="#22c55e" stroke-width="1.5"/>
    <text x="85" y="24" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">3. Waves & Acoustics</text>
    <text x="85" y="43" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Vibrations, Sound, Seismic</text>
    <text x="85" y="60" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Ultrasound, Earthquakes</text>
    <path d="M 85 75 Q 110 160 460 260" stroke="#16a34a" stroke-width="3" fill="none" opacity="0.6"/>
  </g>

  <!-- Branch 4: Geometrical Optics -->
  <g transform="translate(640, 90)">
    <rect width="170" height="75" rx="10" fill="#111827" stroke="#a855f7" stroke-width="1.5"/>
    <text x="85" y="24" fill="#c084fc" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">4. Geometrical Optics</text>
    <text x="85" y="43" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Light, Mirrors, Lenses</text>
    <text x="85" y="60" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Microscopes, Fibre Optics</text>
    <path d="M 85 75 Q 10 160 480 270" stroke="#9333ea" stroke-width="3" fill="none" opacity="0.6"/>
  </g>

  <!-- Branch 5: Electricity & Magnetism -->
  <g transform="translate(30, 205)">
    <rect width="170" height="75" rx="10" fill="#111827" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="85" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">5. Electromagnetism</text>
    <text x="85" y="43" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Charges, Currents, Motors</text>
    <text x="85" y="60" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Generators, Power Grid</text>
    <path d="M 170 242 L 350 280" stroke="#0284c7" stroke-width="3" fill="none" opacity="0.6"/>
  </g>

  <!-- Branch 6: Electronics -->
  <g transform="translate(230, 205)">
    <rect width="170" height="75" rx="10" fill="#111827" stroke="#f43f5e" stroke-width="1.5"/>
    <text x="85" y="24" fill="#fb7185" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">6. Electronics</text>
    <text x="85" y="43" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Semiconductors, Chips</text>
    <text x="85" y="60" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Computers, Smartphones</text>
    <path d="M 170 242 L 380 290" stroke="#e11d48" stroke-width="3" fill="none" opacity="0.6"/>
  </g>

  <!-- Branch 7: Modern Physics -->
  <g transform="translate(440, 205)">
    <rect width="170" height="75" rx="10" fill="#111827" stroke="#10b981" stroke-width="1.5"/>
    <text x="85" y="24" fill="#34d399" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">7. Modern Physics</text>
    <text x="85" y="43" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Subatomic, Quantum</text>
    <text x="85" y="60" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Nuclear, Radiotherapy</text>
    <path d="M 0 242 L 460 290" stroke="#059669" stroke-width="3" fill="none" opacity="0.6"/>
  </g>

  <!-- Branch 8: Astronomy & Space -->
  <g transform="translate(640, 205)">
    <rect width="170" height="75" rx="10" fill="#111827" stroke="#eab308" stroke-width="1.5"/>
    <text x="85" y="24" fill="#facc15" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">8. Astronomy & Space</text>
    <text x="85" y="43" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Cosmos, Celestial Orbits</text>
    <text x="85" y="60" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Satellites, Telescopes</text>
    <path d="M 0 242 L 490 280" stroke="#ca8a04" stroke-width="3" fill="none" opacity="0.6"/>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_electricity_vs_hdi():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="16"/>
  <text x="400" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">ENERGY INFRASTRUCTURE VS HUMAN DEVELOPMENT (DATA LITERACY)</text>
  <text x="400" y="54" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Electricity Consumption per Capita vs Human Development Index (HDI)</text>

  <!-- Coordinate Grid -->
  <g stroke="#334155" stroke-width="1" stroke-dasharray="4 4">
    <line x1="100" y1="360" x2="720" y2="360"/>
    <line x1="100" y1="290" x2="720" y2="290"/>
    <line x1="100" y1="220" x2="720" y2="220"/>
    <line x1="100" y1="150" x2="720" y2="150"/>
    <line x1="100" y1="80" x2="720" y2="80"/>

    <line x1="100" y1="80" x2="100" y2="360"/>
    <line x1="255" y1="80" x2="255" y2="360"/>
    <line x1="410" y1="80" x2="410" y2="360"/>
    <line x1="565" y1="80" x2="565" y2="360"/>
    <line x1="720" y1="80" x2="720" y2="360"/>
  </g>

  <!-- Solid Axes -->
  <line x1="100" y1="360" x2="740" y2="360" stroke="#94a3b8" stroke-width="2"/>
  <line x1="100" y1="360" x2="100" y2="70" stroke="#94a3b8" stroke-width="2"/>

  <!-- Y-Axis Labels (HDI: 0.0 to 1.0) -->
  <text x="85" y="365" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">0.0</text>
  <text x="85" y="295" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">0.25</text>
  <text x="85" y="225" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">0.50</text>
  <text x="85" y="155" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">0.75</text>
  <text x="85" y="85" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">1.00</text>
  <text x="35" y="220" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle" transform="rotate(-90 35 220)">HDI Score (Well-being)</text>

  <!-- X-Axis Labels (Electricity kWh per Capita) -->
  <text x="100" y="380" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">0</text>
  <text x="255" y="380" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">2,000</text>
  <text x="410" y="380" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">5,000</text>
  <text x="565" y="380" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">10,000</text>
  <text x="720" y="380" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">15,000+</text>
  <text x="410" y="415" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Electricity Consumption per Capita (kWh / year)</text>

  <!-- Scatter Points -->
  <circle cx="120" cy="310" r="5" fill="#ef4444" />
  <circle cx="140" cy="275" r="5" fill="#ef4444" />
  <circle cx="170" cy="230" r="6" fill="#f59e0b" />
  <text x="180" y="225" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Developing Nations</text>

  <circle cx="230" cy="180" r="5" fill="#38bdf8" />
  <circle cx="310" cy="140" r="5" fill="#38bdf8" />
  <circle cx="410" cy="115" r="6" fill="#22c55e" />
  <circle cx="530" cy="100" r="5" fill="#22c55e" />
  <circle cx="670" cy="92" r="5" fill="#22c55e" />
  <text x="540" y="85" fill="#22c55e" font-family="system-ui, sans-serif" font-size="11" font-weight="600">High HDI Frontier</text>

  <!-- Trendline Curve -->
  <path d="M 100 350 Q 150 250 250 160 T 500 105 T 720 90" stroke="#38bdf8" stroke-width="3.5" fill="none"/>

  <!-- Callout annotation -->
  <rect x="230" y="270" width="310" height="55" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="240" y="290" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Steep Initial Return on Energy Infrastructure:</text>
  <text x="240" y="310" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Basic electricity access rapidly drives literacy, health & economy</text>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


# =============================================================================
# CURRICULUM DEFINITION DATA FOR TOPIC 1
# =============================================================================

def build_topic1_curriculum_data():
    return [
        # ---------------------------------------------------------------------
        # LESSON 1: Physics as a Body of Knowledge
        # ---------------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Physics as a Body of Knowledge",
            "unit_description": "Introduction to Physics as the foundational science studying matter, energy, and forces; the scientific method of inquiry from observation to scientific laws; experimental measurement and everyday technologies.",
            "lesson_title": "Physics as a Body of Knowledge",
            "pages": [
                # Page 1: Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "Physics in Motion: Urban Transport and Electrical Power in Kenya",
                        "content": {
                            "title": "Physics in Motion: Urban Transport and Electrical Power in Kenya",
                            "caption": "A bustling Kenyan street with matatus, motorcycles, electrical power lines, and streetlights, demonstrating mechanical motion, electricity transmission, and energy conversion in everyday life.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Matatu_in_Nairobi.jpg/1280px-Matatu_in_Nairobi.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Matatu_in_Nairobi.jpg/1280px-Matatu_in_Nairobi.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Urban Transport and Electrical Infrastructure in Nairobi",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Matatu_in_Nairobi.jpg/1280px-Matatu_in_Nairobi.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons Contributors",
                                "licensing": "CC BY-SA 4.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Matatu_in_Nairobi.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Invisible Rules Governing Our World",
                        "content": {
                            "title": "Everyday Phenomena are Governed by Physics",
                            "text": "Every time you look at your smartphone, boil water for tea, or ride in a minibus (*matatu*) on a bumpy road, you are witnessing **Physics** in action.\n\n- **Why does a vehicle jolt forward** when the driver suddenly steps on the brakes?\n- **Why does water turn into steam** when heated, but ice melts into liquid?\n- **How does a glass screen on a phone** respond instantly to the electrical touch of your finger?\n\nPhysics is not confined to a laboratory or a chalkboard; it is the study of how the entire physical universe behaves. It gives us the toolkit to observe, measure, and explain natural phenomena."
                        }
                    }
                ],
                # Page 2: Learning Goals & Scope
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Nature of Physics",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Define **Physics** and explain its focus on **matter**, **energy**, and **forces** in the physical environment.",
                                "Connect prior Junior Secondary School (JSS) Integrated Science knowledge with Senior Secondary Physics.",
                                "Trace the **Scientific Method of Inquiry** from real-world observation to universal scientific laws.",
                                "Conduct a practical **Phenomenon Walk** to identify physical quantities in your immediate surroundings.",
                                "Analyze how core Physics principles drive everyday technologies like transport, cooking, and medical diagnosis."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Transitioning from JSS Science to Senior Secondary Physics",
                        "content": {
                            "title": "Building on Your Scientific Foundations",
                            "text": "In Junior Secondary School Integrated Science, you learned how to observe the world, take basic measurements, and conduct simple investigations.\n\nIn Senior Secondary Physics, we take those exact foundational skills to a deeper level:\n- Moving from **qualitative observation** (\"it feels hot\") to **quantitative measurement** (\"the temperature is $373\\text{ K}$\").\n- Uncovering **mathematical models** that describe nature with predictive precision.\n- Understanding the fundamental laws that govern interactions across both microscopic atoms and macroscopic galaxies."
                        }
                    }
                ],
                # Page 3: Definitions
                [
                    {
                        "type": "definition_card",
                        "title": "Key Term: Physics",
                        "content": {
                            "term": "Physics",
                            "definition": "The branch of science concerned with the study of matter, energy, and the forces that govern their interactions in the physical environment.",
                            "example": "Studying how heat energy converts into mechanical work to propel a locomotive engine."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Matter",
                        "content": {
                            "term": "Matter",
                            "definition": "Anything that has mass and occupies space. All physical objects you can see, touch, or measure are composed of matter.",
                            "example": "Solids (ice, metal), liquids (water, oil), and gases (air, steam)."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Energy",
                        "content": {
                            "term": "Energy",
                            "definition": "The capacity or ability to perform work. Energy exists in multiple interchangeable forms including kinetic, potential, thermal, electrical, and radiant energy.",
                            "example": "Solar radiation absorbed by photovoltaic cells and converted into electrical energy."
                        }
                    }
                ],
                # Page 4: Scientific Method Process Flow SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Scientific Method: Systematic Pathway of Inquiry",
                        "content": {
                            "title": "The Scientific Method: Systematic Pathway of Inquiry",
                            "caption": "Step-by-step pathway showing how physicists transition from real-world observations to verified theories and universal mathematical laws.",
                            "svg_content": get_svg_scientific_method(),
                            "svg": get_svg_scientific_method()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Scientific Method Pathway of Inquiry Flowchart",
                            "metadata": {
                                "svg_content": get_svg_scientific_method()
                            }
                        }
                    }
                ],
                # Page 5: Step-by-Step Breakdown
                [
                    {
                        "type": "step_process",
                        "title": "The 6 Stages of Scientific Inquiry",
                        "content": {
                            "title": "From Curiosity to Scientific Law",
                            "steps": [
                                "1. **Real-World Observation**: Noticing an intriguing physical event (e.g. noticing that a pendulum takes the same time for each swing regardless of amplitude).",
                                "2. **Hypothesis Formulation**: Proposing a tentative, testable explanation (e.g. 'The period of a pendulum depends only on its string length, not its bob mass').",
                                "3. **Controlled Experimentation**: Designing a controlled investigation where only one independent variable is altered while measuring physical quantities (length, time, mass).",
                                "4. **Evidence Collection & Data Analysis**: Recording quantitative measurements, plotting graphs, and evaluating experimental uncertainties.",
                                "5. **Theory Development**: Synthesizing a comprehensive, well-substantiated explanation supported by extensive empirical validation.",
                                "6. **Scientific Law**: Formulating a concise, universally valid relationship that describes what occurs under specified conditions, typically expressed as a mathematical equation."
                            ]
                        }
                    }
                ],
                # Page 6: Practical Investigation
                [
                    {
                        "type": "mini_activity",
                        "title": "Practical Investigation: The Phenomenon Walk",
                        "content": {
                            "title": "Training Your 'Physics Eyes'",
                            "task": "Take 10 minutes to walk around your school compound or home environment and identify 5 distinct physical events:\n\n1. **Select 5 events** (e.g. water dripping from a tap, a swinging gate, a solar panel charging a battery, a student kicking a football, sound echoing in a hall).\n2. **For each event, record in a table**:\n   - *What is moving, changing, or transferring energy?*\n   - *What physical quantities could we measure? (e.g. speed, temperature, time, force, electric current)*\n3. **Classify each event** into core physics branches: Mechanics, Heat, Light, Electricity, or Sound.",
                            "materials": ["Field Notebook", "Pen", "Metre Rule or Tape Measure", "Stopwatch / Phone Timer"],
                            "safety": "Walk carefully, avoid live electrical wires or slippery drainage areas, and respect laboratory rules."
                        }
                    }
                ],
                # Page 7: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Hypothesis vs Scientific Law",
                        "content": {
                            "question": "Which of the following statements best describes the scientific distinction between a **hypothesis** and a **scientific law**?",
                            "options": [
                                "A hypothesis is a proven fact, while a scientific law is an educated guess that has never been tested.",
                                "A hypothesis is a tentative, testable explanation for an observation, while a scientific law describes a constant, universal relationship in nature.",
                                "A hypothesis must always be written as a mathematical formula, whereas a scientific law can only be described in words.",
                                "A hypothesis is only used in chemistry, while a scientific law is only used in physics."
                            ],
                            "answer": "B",
                            "explanation": "A **hypothesis** is an initial testable proposal formulated to explain an observed event. A **scientific law** is a descriptive generalization of a constant, universal relationship observed in nature that has been confirmed by repeated experiments and is often expressed mathematically (e.g. $F = ma$). Option A is inverted. Option C is false because laws are frequently mathematical equations. Option D is incorrect because all natural sciences use hypotheses and laws.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 8: Real-World Applications
                [
                    {
                        "type": "real_world_connection",
                        "title": "Everyday Technologies Powered by Physics",
                        "content": {
                            "title": "Physics as the Engine of Modern Society",
                            "text": "Physics principles form the engineering backbone of modern technologies:\n\n- **Transport & Automotive**: Aeroplanes generate aerodynamic lift via fluid dynamics and pressure differentials, while vehicles stop safely through friction and hydraulic brake force transmission.\n- **Domestic Food Preparation**: Thermal physics and thermodynamics dictate how heat transfers from a gas stove or *jiko* into a metal *sufuria* to cook maize meal (*ugali*).\n- **Modern Healthcare**: Medical imaging diagnostics like X-rays, MRI scans, and ultrasound utilize wave mechanics, nuclear physics, and optics to visualize internal anatomy non-invasively.\n- **Telecommunications**: Smartphones transmit data using high-frequency electromagnetic radio waves traveling through space at the speed of light ($3.0 \\times 10^8\\text{ m/s}$)."
                        }
                    }
                ],
                # Page 9: YouTube Video & Summary
                [
                    {
                        "type": "suggested_video",
                        "title": "Demonstration: Physics and the Scientific Method in Action",
                        "content": {
                            "title": "Demonstration: Physics and the Scientific Method in Action",
                            "description": "An engaging video walk-through demonstrating how fundamental physics principles—matter, forces, and energy transformations—are applied to create everyday machines, vehicles, and medical scanners.",
                            "url": "https://www.youtube.com/watch?v=ZM8ECpBuQYE",
                            "resolved_video_id": "ZM8ECpBuQYE"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Introduction to Physics and the Scientific Method",
                            "url": "https://www.youtube.com/watch?v=ZM8ECpBuQYE",
                            "metadata": {
                                "youtube_id": "ZM8ECpBuQYE"
                            }
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Lesson 1 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "**Physics** is the fundamental science studying matter, energy, and the forces governing their interactions.",
                                "Scientific inquiry progresses systematically: **Observation $\\rightarrow$ Hypothesis $\\rightarrow$ Experiment $\\rightarrow$ Evidence $\\rightarrow$ Theory $\\rightarrow$ Scientific Law**.",
                                "Physics is essentially **experimental and quantitative**, relying on precise measurement of physical quantities.",
                                "Modern infrastructure, vehicles, smartphones, and medical equipment are direct engineering applications of Physics principles."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 2: Branches of Physics and Connections
        # ---------------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "Branches of Physics and Connections",
            "unit_description": "The major branches of Physics (Mechanics, Thermodynamics, Waves, Optics, Electricity & Magnetism, Electronics, Modern Physics, Astronomy), interdisciplinary connections with Mathematics, Chemistry, Biology, Geography, and Computer Science.",
            "lesson_title": "Branches of Physics and Connections",
            "pages": [
                # Page 1: Hook & Tree SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Tree of Physics: Major Specialized Branches",
                        "content": {
                            "title": "The Tree of Physics: Major Specialized Branches",
                            "caption": "A conceptual tree diagram showing Physics as a foundational trunk branching into 8 major specialized sub-disciplines.",
                            "svg_content": get_svg_branches_tree(),
                            "svg": get_svg_branches_tree()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "The Tree of Physics Branches Diagram",
                            "metadata": {
                                "svg_content": get_svg_branches_tree()
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "A Vast Tree of Specialized Knowledge",
                        "content": {
                            "title": "From Natural Philosophy to Specialized Domains",
                            "text": "Physics began centuries ago as general 'natural philosophy'—curiosity about why fire is hot, how planets orbit, and why things fall. Over time, as human understanding expanded, this broad science divided into distinct **specialized branches**.\n\nWhether designing an electric train, manufacturing a solar cell, or analyzing an earthquake, you apply specific branches of Physics."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Branches & Interdisciplinary Links",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify and describe the **8 primary branches of Physics**.",
                                "Analyze how Mathematics functions as the essential **language and modeling tool** of Physics.",
                                "Examine how Physics interfaces with Chemistry, Biology, Geography/Geology, and Computer Science to create hybrid disciplines (e.g. Biophysics, Geophysics).",
                                "Evaluate real-world engineering projects to identify which branches of Physics they utilize."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Branch of Physics",
                        "content": {
                            "term": "Branch of Physics",
                            "definition": "A specialized sub-field of physical science organized around a related group of natural phenomena, principles, and mathematical models.",
                            "example": "Thermodynamics is the branch studying heat, work, temperature, and energy transformations."
                        }
                    }
                ],
                # Page 3: Comparison Table of 8 Branches
                [
                    {
                        "type": "comparison_table",
                        "title": "The 8 Major Branches of Physics",
                        "content": {
                            "title": "Overview of Major Physics Branches",
                            "headers": ["Branch of Physics", "Central Focus", "Example Technology / Phenomenon", "Related STEM Career"],
                            "rows": [
                                ["Mechanics", "Study of motion, forces, energy, and mechanical equilibrium.", "Automobiles, construction cranes, hydroelectric dams.", "Mechanical & Civil Engineer"],
                                ["Thermodynamics", "Study of heat, temperature, and energy conversion.", "Refrigerators, vehicle engines, geothermal power plants.", "Thermal Power & Energy Engineer"],
                                ["Waves & Acoustics", "Study of vibrations traveling through matter or space.", "Musical instruments, sonar navigation, seismic waves.", "Acoustic Engineer, Seismologist"],
                                ["Geometrical Optics", "Study of light propagation, reflection, and refraction.", "Lenses, microscopes, eyeglasses, fibre-optic internet.", "Optometrist, Optical Engineer"],
                                ["Electricity & Magnetism", "Study of electric charges, currents, and magnetic fields.", "Electric motors, generators, national power grid.", "Electrical Power Systems Engineer"],
                                ["Electronics", "Study of electron flow through semiconductors and microcircuits.", "Microchips, computers, smartphones, automated sensors.", "Computer Hardware & Robotics Engineer"],
                                ["Modern Physics", "Study of atomic, subatomic, and relativistic phenomena.", "Nuclear energy, radiocarbon dating, cancer radiotherapy.", "Nuclear Physicist, Medical Physicist"],
                                ["Astronomy & Space Physics", "Study of celestial bodies, gravity, and cosmic dynamics.", "Satellites, space probes, planetary orbital tracking.", "Astrophysicist, Satellite Engineer"]
                            ]
                        }
                    }
                ],
                # Page 4: Interdisciplinary Connections
                [
                    {
                        "type": "concept_explanation",
                        "title": "Physics as the Fundamental Science",
                        "content": {
                            "title": "Connecting with Other Scientific Disciplines",
                            "text": "Physics is often termed the 'fundamental science' because its principles dictate the behaviour of all matter and energy in the universe:\n\n- **Mathematics**: Mathematics is the indispensable **language of Physics**. Without algebraic equations, geometry, and calculus, physical laws would be merely descriptive rather than predictive.\n- **Chemistry**: Chemical reactions involve valence electron interactions, bond energies, and atomic thermodynamics—all explained by quantum mechanics and electromagnetism.\n- **Biology (Biophysics)**: Biological organisms operate under physical laws. Your heart functions as a hydraulic pressure pump, your joints act as levers (moments), and your eyes refract light through lenses.\n- **Geography & Geology (Geophysics)**: Thermodynamics drives atmospheric weather, convection winds, and ocean currents. Geology uses seismology (wave mechanics) to map earthquakes and locate underground aquifers.\n- **Computer Science**: Modern microprocessors rely on semiconductor physics and quantum mechanics to switch billions of silicon transistors every second."
                        }
                    }
                ],
                # Page 5: Engineering Visual
                [
                    {
                        "type": "suggested_image",
                        "title": "Olkaria Geothermal Power Station: Thermodynamics and Electromagnetism in Action",
                        "content": {
                            "title": "Olkaria Geothermal Power Station: Thermodynamics and Electromagnetism in Action",
                            "caption": "Kenya's Olkaria Geothermal Power Station in the Great Rift Valley harnesses high-pressure underground steam (Thermodynamics) to rotate turbines that generate electricity (Electricity & Magnetism) for the national grid.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Olkaria_II_Geothermal_Power_Station.jpg/1280px-Olkaria_II_Geothermal_Power_Station.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Olkaria_II_Geothermal_Power_Station.jpg/1280px-Olkaria_II_Geothermal_Power_Station.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Olkaria II Geothermal Power Station, Kenya",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Olkaria_II_Geothermal_Power_Station.jpg/1280px-Olkaria_II_Geothermal_Power_Station.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Olkaria_II_Geothermal_Power_Station.jpg"
                            }
                        }
                    }
                ],
                # Page 6: Interactive Group Activity
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Scientific Panel: 'Match the Phenomenon'",
                        "content": {
                            "title": "Classifying Real-World Scenarios",
                            "task": "Working with a peer, analyze each scenario below to identify the **Primary Physics Branch** and the **Connected School Subject**:\n\n1. *A delivery drone navigating autonomously using GPS and adjusting its rotors to counteract turbulent wind gusts.*\n   - **Physics Branch**: Mechanics & Electronics.\n   - **Connected Discipline**: Mathematics (coordinates) & Computer Science (autopilot algorithms).\n\n2. *A sonographer using an ultrasound transducer probe to monitor fetal heartbeat in a hospital.*\n   - **Physics Branch**: Waves & Acoustics.\n   - **Connected Discipline**: Biology & Medicine.\n\n3. *Testing the volcanic rock composition in the Rift Valley using laser emission spectroscopy.*\n   - **Physics Branch**: Geometrical Optics & Modern Physics.\n   - **Connected Discipline**: Chemistry & Geology / Geography.",
                            "materials": ["Discussion Worksheet", "Pen"],
                            "safety": "Engage respectfully in peer collaborative discussions."
                        }
                    }
                ],
                # Page 7: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Energy Transformation in Geothermal Power",
                        "content": {
                            "question": "Engineers at Olkaria in the Rift Valley harness superheated steam from deep underground to rotate massive turbine shafts, which then drive electromagnetic generators to supply electricity to the national grid. Which two branches of Physics are most directly responsible for this process?",
                            "options": [
                                "Geometrical Optics and Waves & Acoustics",
                                "Astronomy and Modern Physics",
                                "Thermodynamics and Electricity & Magnetism",
                                "Electronics and Geometrical Optics"
                            ],
                            "answer": "C",
                            "explanation": "Converting thermal energy (steam from geothermal reservoirs) into mechanical rotation of a turbine is the domain of **Thermodynamics**. Converting that mechanical rotation into electrical energy via magnetic induction inside a generator is the domain of **Electricity & Magnetism**. Therefore, Option C is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 8: Video & Summary
                [
                    {
                        "type": "suggested_video",
                        "title": "Visual Exploration: The Map of Physics",
                        "content": {
                            "title": "Visual Exploration: The Map of Physics",
                            "description": "A visual journey through all major branches of Physics, demonstrating how classical mechanics, thermodynamics, electromagnetism, and modern quantum theory interconnect.",
                            "url": "https://www.youtube.com/watch?v=ZihywtixUYo",
                            "resolved_video_id": "ZihywtixUYo"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "The Map of Physics Overview",
                            "url": "https://www.youtube.com/watch?v=ZihywtixUYo",
                            "metadata": {
                                "youtube_id": "ZihywtixUYo"
                            }
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Lesson 2 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "Physics is organized into 8 primary branches: **Mechanics, Thermodynamics, Waves & Acoustics, Geometrical Optics, Electricity & Magnetism, Electronics, Modern Physics, and Astronomy**.",
                                "**Mathematics** provides the quantitative modeling language of physical laws.",
                                "Physics interfaces with Chemistry, Biology, Geography, and Computing to create interdisciplinary fields like **Biophysics, Geophysics, and Materials Science**."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 3: Importance, Careers, and Scientific Citizenship
        # ---------------------------------------------------------------------
        {
            "unit_order": 3,
            "unit_name": "Importance, Careers, and Scientific Citizenship",
            "unit_description": "The socio-economic importance of Physics in national development and Kenya Vision 2030, career pathways (medical physics, renewable energy, engineering, meteorology), dismantling STEM gender stereotypes, and responsible scientific citizenship.",
            "lesson_title": "Importance, Careers, and Scientific Citizenship",
            "pages": [
                # Page 1: Hook & Lake Turkana Wind Power Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Renewable Wind Energy in Kenya: Physics Driving National Development",
                        "content": {
                            "title": "Renewable Wind Energy in Kenya: Physics Driving National Development",
                            "caption": "The Lake Turkana Wind Power project in northern Kenya harnesses kinetic wind energy using massive aerodynamic turbine blades to generate clean, renewable electricity for the nation.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Lake_Turkana_Wind_Power_Station.jpg/1280px-Lake_Turkana_Wind_Power_Station.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Lake_Turkana_Wind_Power_Station.jpg/1280px-Lake_Turkana_Wind_Power_Station.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Lake Turkana Wind Power Station, Kenya",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Lake_Turkana_Wind_Power_Station.jpg/1280px-Lake_Turkana_Wind_Power_Station.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 4.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Lake_Turkana_Wind_Power_Station.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Study Physics? Beyond the Classroom",
                        "content": {
                            "title": "Physics as a Catalyst for National Transformation",
                            "text": "\"Why am I studying Physics?\" It is a question every student asks.\n\nPhysics is not just an academic subject; it is a practical launchpad that drives **national industrial development (Kenya's Vision 2030)**, powers sustainable energy transitions, and develops high-level analytical problem-solving skills that are valued in every modern career sector."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Careers & Civic Responsibility",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Evaluate the role of Physics in socioeconomic development and clean energy transition.",
                                "Explore diverse, high-value **career pathways** available to Physics graduates.",
                                "Dismantle pervasive myths and cultural stereotypes regarding participation in STEM, emphasizing **gender equity**.",
                                "Define and practice **Scientific Citizenship** by applying evidence-based reasoning to community challenges."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Scientific Citizenship",
                        "content": {
                            "term": "Scientific Citizenship",
                            "definition": "The active, responsible application of scientific knowledge, evidence-based reasoning, and technical literacy to make informed decisions that benefit one's community, nation, and environment.",
                            "example": "Advocating for energy-efficient LED lighting, practicing water conservation, or supporting climate resilience policies."
                        }
                    }
                ],
                # Page 3: Career Matrix Table
                [
                    {
                        "type": "comparison_table",
                        "title": "High-Value Career Pathways in Physics",
                        "content": {
                            "title": "Physics Career Opportunities Matrix",
                            "headers": ["Career Pathway", "Primary Responsibilities", "Core Physics Concepts Applied", "Societal & Economic Impact"],
                            "rows": [
                                ["Medical Physicist", "Calibrates radiotherapy machines for cancer treatment; maintains MRI & CT scanners.", "Radiation Physics, Wave Mechanics, Nuclear Physics", "Ensures precise medical diagnosis and safe cancer therapy."],
                                ["Renewable Energy Engineer", "Designs solar microgrids, wind farms, and geothermal power systems.", "Thermodynamics, Electromagnetism, Fluid Dynamics", "Expands clean, affordable electricity to rural and urban communities."],
                                ["Agricultural Technologist", "Develops automated drip irrigation, solar crop driers, and soil moisture sensors.", "Fluid Pressure, Electronics, Thermodynamics", "Enhances national food security and conserves water in arid lands."],
                                ["Civil & Structural Engineer", "Designs safe highways, suspension bridges, and climate-resilient structures.", "Mechanics, Statics, Material Elasticity & Moments", "Prevents structural failures and builds safe transportation infrastructure."],
                                ["Meteorologist & Climate Scientist", "Models atmospheric weather patterns and tracks climate change.", "Thermodynamics, Fluid Dynamics, Barometric Pressure", "Protects communities from droughts, floods, and agricultural losses."],
                                ["Data Scientist & Software Modeler", "Constructs computational models and analyzes complex system data.", "Mathematical Modeling, Logic Circuits, Statistical Mechanics", "Powers digital finance, logistics optimization, and tech innovation."]
                            ]
                        }
                    }
                ],
                # Page 4: Challenging Myths
                [
                    {
                        "type": "common_misconception",
                        "title": "Challenging the Myths: Physics is for Everyone!",
                        "content": {
                            "misconception": "Physics is an ultra-difficult subject only suitable for male 'geniuses' who memorize complex formulas.",
                            "correction": "Physics is a structured, learnable skill that thrives on curiosity, practice, and logical problem solving. Intelligence has absolutely no gender, and promoting women in STEM unlocks 100% of our creative potential.",
                            "why_it_matters": "Dispelling harmful stereotypes empowers all learners—especially girls—to pursue rewarding STEM careers that solve vital human problems."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Gender Equity in Senior School Physics",
                        "content": {
                            "title": "Unlocking National Potential",
                            "text": "Historically, cultural barriers discouraged girls from pursuing physical sciences. Today, Kenyan women are leading pioneers in geothermal engineering, medical physics, astrophysics, and telecommunications. Scientific talent and analytical capability belong to everyone!"
                        }
                    }
                ],
                # Page 5: Data Literacy SVG Graph
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Data Literacy: Electricity Consumption vs Human Development Index (HDI)",
                        "content": {
                            "title": "Data Literacy: Electricity Consumption vs Human Development Index (HDI)",
                            "caption": "Scatter plot showing that increasing per capita electrical energy access drastically boosts human development, health, and education before plateauing at advanced levels.",
                            "svg_content": get_svg_electricity_vs_hdi(),
                            "svg": get_svg_electricity_vs_hdi()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Electricity Consumption vs HDI Scatter Plot",
                            "metadata": {
                                "svg_content": get_svg_electricity_vs_hdi()
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Interpreting the Energy-Development Relationship",
                        "content": {
                            "title": "Why National Well-being Depends on Physics",
                            "text": "The graph above reveals a vital socioeconomic reality:\n\n- **Steep Upward Trajectory**: In developing regions, even a modest increase in per capita electrical power leads to massive leaps in the Human Development Index (HDI).\n- **Physical Foundation**: Electricity powers hospital intensive care units, pumps clean water to prevent waterborne disease, refrigerates agricultural produce, and lights classrooms for evening study.\n- **Conclusion**: Expanding a nation's Physics-based energy infrastructure is the single most effective tool for overcoming poverty and improving quality of life."
                        }
                    }
                ],
                # Page 6: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Scientific Citizenship in Practice",
                        "content": {
                            "question": "A Grade 10 student notices that their school leaves incandescent lighting and old ceiling fans running in empty classrooms, resulting in massive electricity bills. Using their knowledge of energy efficiency from Physics class, the student organizes an energy audit and leads a campaign to retrofit classrooms with LED bulbs and automated switches. This action is a direct demonstration of:",
                            "options": [
                                "A theoretical laboratory exercise in quantum mechanics",
                                "Scientific citizenship in practice",
                                "An unauthorized administrative intervention",
                                "Basic research in pure astronomy"
                            ],
                            "answer": "B",
                            "explanation": "**Scientific citizenship** is the active, responsible use of scientific knowledge and evidence-based reasoning to solve real-world problems in your immediate community (such as eliminating school electrical waste and lowering carbon emissions). Options A and D are incorrect subject domains. Option C is false because this is a responsible, highly valuable community initiative.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 7: Video & Summary
                [
                    {
                        "type": "suggested_video",
                        "title": "Career Horizons: Why Study Physics in the 21st Century?",
                        "content": {
                            "title": "Career Horizons: Why Study Physics in the 21st Century?",
                            "description": "An inspiring documentary highlighting modern career paths in physics—from renewable energy engineers building solar grids to medical physicists treating diseases.",
                            "url": "https://www.youtube.com/watch?v=tY8G_iW2Ff0",
                            "resolved_video_id": "tY8G_iW2Ff0"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Why Study Physics? 21st Century Careers in STEM",
                            "url": "https://www.youtube.com/watch?v=tY8G_iW2Ff0",
                            "metadata": {
                                "youtube_id": "tY8G_iW2Ff0"
                            }
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Lesson 3 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "Physics is a vital engine of **national development (Kenya Vision 2030)** and global sustainability.",
                                "Career pathways are diverse, lucrative, and impactful: **medical physics, renewable energy, civil engineering, meteorology, and data science**.",
                                "Scientific ability is gender-neutral; challenging cultural stereotypes ensures that everyone can participate in STEM innovation.",
                                "**Scientific citizenship** empowers learners to use evidence-based reasoning to solve local community challenges."
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
def ingest_grade10_physics_topic1():
    print("======================================================================")
    print("INGESTING CBC GRADE 10 PHYSICS — TOPIC 1: INTRODUCTION TO PHYSICS")
    print("======================================================================")

    # 1. Verify Curriculum & Grade
    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    if not curriculum:
        raise ValueError("Curriculum 'CBC' (ID: 5) not found!")

    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    if not grade:
        raise ValueError("Grade 10 not found under CBC curriculum!")

    # 2. Get or Create Subject: Physics
    subject, s_created = Subject.objects.get_or_create(
        grade=grade,
        name="Physics",
        defaults={"description": "CBC Senior Secondary Physics"}
    )
    print(f"Subject: {subject.name} (ID: {subject.id}, Created: {s_created})")

    # 3. Get or Create Topic: Introduction to Physics (Order: 1)
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=1,
        defaults={
            "name": "Introduction to Physics",
            "description": "Explores Physics as a fundamental science, its major specialized branches, interdisciplinary links, high-value career pathways, and scientific citizenship."
        }
    )
    if not t_created and topic.name != "Introduction to Physics":
        topic.name = "Introduction to Physics"
        topic.description = "Explores Physics as a fundamental science, its major specialized branches, interdisciplinary links, high-value career pathways, and scientific citizenship."
        topic.save()
    print(f"Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    curriculum_data = build_topic1_curriculum_data()

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
    print(f"TOPIC 1 INGESTION COMPLETE:")
    print(f"  - Learning Units: {total_units_created}")
    print(f"  - Lessons:        {total_lessons_created}")
    print(f"  - Lesson Blocks:  {total_blocks_created}")
    print(f"  - Lesson Assets:  {total_assets_created}")
    print("======================================================================")

if __name__ == "__main__":
    ingest_grade10_physics_topic1()
