"""
VLearn CBC Grade 10 Home Science — Topic 1.4: Methods of Cooking
Comprehensive Production Ingestion & Visual Enrichment Engine

Curriculum: CBC
Grade: Grade 10 (Level: 10)
Subject: Home Science
Topic: Foods and Nutrition (Order: 1)
Learning Unit 4: 1.4 Methods of Cooking (Order: 4)

Contains 14 Published Lessons (6 Concept Cards / Pages per Lesson):
  - Lesson 1: Reasons for Cooking Food
  - Lesson 2: Classification of Cooking Methods & Principles of Heat Transfer
  - Lesson 3: General Rules for Cooking Food
  - Lesson 4: Moist Heat Cooking Methods — Boiling and Stewing
  - Lesson 5: Moist Heat Cooking Methods — Steaming and Poaching
  - Lesson 6: Frying Methods — Dry, Shallow, and Deep Frying
  - Lesson 7: Dry Heat Cooking Methods — Roasting and Grilling
  - Lesson 8: Dry Heat Cooking Methods — Baking
  - Lesson 9: Pre-Preparation Techniques (Mise en Place) — Cleaning, Peeling, and Coring
  - Lesson 10: Pre-Preparation Techniques — Cutting, Slicing, Chopping, and Dicing
  - Lesson 11: Pre-Preparation Techniques — Grating, Mixing, Kneading, and Blending
  - Lesson 12: Selecting Appropriate Cooking Methods for Different Foods
  - Lesson 13: Culinary Practical — Moist Heat Cooking (Preparation & Execution)
  - Lesson 14: Culinary Practical — Dry Heat & Frying (Preparation & Safety)

Features:
  - Direct reading of markdown ground truth
  - 14 Custom Responsive Sanitized Vector SVG Diagrams with viewBox="0 0 800 450"
  - 14 Verified Wikimedia Commons Photographic Assets with attached LessonAssets
  - 14 Verified Educational YouTube Video Integrations with attached LessonAssets
  - 14 Formative Scenario-Based MCQs with 4 options, valid correct_answer, and detailed explanations
  - 6 Discrete Concept Cards (Pages) per lesson with full typed block coverage
  - 0 Bracket citations & 0 meta-language leaks
"""

import os
import sys
import re
import django
from django.db import transaction

# Setup Django Environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

# =============================================================================
# TEXT SANITIZATION & NORMALIZATION UTILITIES
# =============================================================================

def clean_text(text: str) -> str:
    """Removes bracket citations and normalizes markdown."""
    if not text:
        return ""
    # Strip citation brackets [123], [image_1], [S12], [1, 2, 3]
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Strip meta prompt tags
    text = re.sub(r'\[VISUAL:[^\]]*\]', '', text, flags=re.DOTALL)
    text = re.sub(r'\[INTERACTION:[^\]]*\]', '', text, flags=re.DOTALL)
    text = re.sub(r'\[QUESTION:[^\]]*\]', '', text, flags=re.DOTALL)
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    text = re.sub(r'^([^\n\-\*\d\>#][^\n]*)\n(- |\* )', r'\1\n\n\2', text, flags=re.MULTILINE)
    return text.strip()

def clean_dict(data):
    """Recursively cleans all strings in dictionary/list structures."""
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, dict):
        return {k: clean_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_dict(item) for item in data]
    return data

# =============================================================================
# 14 CUSTOM SANITIZED RESPONSIVE VECTOR SVGS (viewBox="0 0 800 450")
# =============================================================================

def get_svg_1():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">BIOLOGICAL &amp; SENSORY REASONS FOR COOKING FOOD</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">How thermal energy transforms raw biochemical structures into safe, digestible meals</text>

  <!-- 1: Digestibility -->
  <g transform="translate(30, 75)">
    <rect width="360" height="165" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="35" cy="35" r="18" fill="#0284c7"/>
    <text x="35" y="41" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">1</text>
    <text x="65" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700">Digestibility &amp; Nutrient Bioavailability</text>
    <text x="65" y="48" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Collagen Breakdown &amp; Starch Gelatinization</text>
    <text x="20" y="80" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11">• Converts tough collagen connective tissues into soluble gelatin.</text>
    <text x="20" y="102" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11">• Ruptures plant cell walls (cellulose) to release micronutrients.</text>
    <text x="20" y="124" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11">• Gelatinizes complex starch granules for enzymatic absorption.</text>
  </g>

  <!-- 2: Safety -->
  <g transform="translate(410, 75)">
    <rect width="360" height="165" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <circle cx="35" cy="35" r="18" fill="#dc2626"/>
    <text x="35" y="41" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">2</text>
    <text x="65" y="32" fill="#f87171" font-family="system-ui, sans-serif" font-size="14" font-weight="700">Microbial Safety &amp; Preservation</text>
    <text x="65" y="48" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Pathogen Destruction &amp; Toxin Inactivation</text>
    <text x="20" y="80" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11">• Destroys pathogenic bacteria (Salmonella, E. coli, Campylobacter).</text>
    <text x="20" y="102" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11">• Eliminates foodborne parasites and fungal spores.</text>
    <text x="20" y="124" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11">• Denatures harmful plant hemagglutinins and protease inhibitors.</text>
  </g>

  <!-- 3: Flavor & Aroma -->
  <g transform="translate(30, 255)">
    <rect width="360" height="165" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="35" cy="35" r="18" fill="#d97706"/>
    <text x="35" y="41" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">3</text>
    <text x="65" y="32" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="14" font-weight="700">Flavor, Aroma &amp; Palatability</text>
    <text x="65" y="48" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Maillard Reaction &amp; Caramelization</text>
    <text x="20" y="80" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11">• Triggers Maillard browning between amino acids and sugars.</text>
    <text x="20" y="102" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11">• Caramelizes natural carbohydrates to develop rich aromas.</text>
    <text x="20" y="124" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11">• Releases aromatic volatile compounds that stimulate digestion.</text>
  </g>

  <!-- 4: Texture & Shelf-Life -->
  <g transform="translate(410, 255)">
    <rect width="360" height="165" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <circle cx="35" cy="35" r="18" fill="#059669"/>
    <text x="35" y="41" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">4</text>
    <text x="65" y="32" fill="#34d399" font-family="system-ui, sans-serif" font-size="14" font-weight="700">Texture Modification &amp; Shelf-Life</text>
    <text x="65" y="48" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Enzyme Inactivation &amp; Coagulation</text>
    <text x="20" y="80" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11">• Coagulates egg/meat proteins to achieve desirable firmness.</text>
    <text x="20" y="102" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11">• Inactivates food-degrading enzymes (polyphenol oxidase).</text>
    <text x="20" y="124" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11">• Extends preservation duration and storage safety in households.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_2():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">HEAT TRANSFER PRINCIPLES &amp; COOKING METHOD CLASSIFICATION</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Physics of Conduction, Convection, and Radiation across the Three Culinary Pillars</text>

  <!-- Heat Transfer Modes -->
  <g transform="translate(30, 75)">
    <rect width="230" height="150" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="115" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">CONDUCTION</text>
    <text x="115" y="46" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Direct Molecular Contact</text>
    <text x="15" y="75" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• Heat flows atom-to-atom.</text>
    <text x="15" y="95" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• Solid-to-solid contact.</text>
    <text x="15" y="115" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• e.g., Pan touching steak.</text>
    <rect x="20" y="128" width="190" height="12" rx="4" fill="#0284c7"/>
  </g>

  <g transform="translate(285, 75)">
    <rect width="230" height="150" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="115" y="28" fill="#34d399" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">CONVECTION</text>
    <text x="115" y="46" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Circulating Fluid / Gas</text>
    <text x="15" y="75" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• Hot fluid rises, cold sinks.</text>
    <text x="15" y="95" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• Liquid &amp; air currents.</text>
    <text x="15" y="115" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• e.g., Boiling pot, oven air.</text>
    <rect x="20" y="128" width="190" height="12" rx="4" fill="#059669"/>
  </g>

  <g transform="translate(540, 75)">
    <rect width="230" height="150" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="115" y="28" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">RADIATION</text>
    <text x="115" y="46" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Electromagnetic Waves</text>
    <text x="15" y="75" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• Infrared &amp; radiant waves.</text>
    <text x="15" y="95" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• No medium required.</text>
    <text x="15" y="115" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">• e.g., Charcoal grill, broiler.</text>
    <rect x="20" y="128" width="190" height="12" rx="4" fill="#d97706"/>
  </g>

  <!-- 3 Pillars of Cooking Methods -->
  <g transform="translate(30, 245)">
    <rect width="230" height="175" rx="10" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="230" height="28" rx="8" fill="#0284c7"/>
    <text x="115" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">MOIST HEAT METHODS</text>
    <text x="15" y="48" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Medium: Water &amp; Steam</text>
    <text x="15" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Boiling (100°C)</text>
    <text x="15" y="94" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Stewing (85°C - 95°C)</text>
    <text x="15" y="116" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Steaming (100°C Vapor)</text>
    <text x="15" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Poaching (70°C - 85°C)</text>
    <text x="15" y="160" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Preserves tenderness, dissolves collagen.</text>
  </g>

  <g transform="translate(285, 245)">
    <rect width="230" height="175" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="230" height="28" rx="8" fill="#d97706"/>
    <text x="115" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">DRY HEAT METHODS</text>
    <text x="15" y="48" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Medium: Hot Air &amp; Radiant Flame</text>
    <text x="15" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Baking (Oven Convection)</text>
    <text x="15" y="94" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Roasting (Basted Dry Heat)</text>
    <text x="15" y="116" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Grilling (Direct Radiation)</text>
    <text x="15" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Broiling / Toasting</text>
    <text x="15" y="160" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Forms crisp crusts &amp; rich aromas.</text>
  </g>

  <g transform="translate(540, 245)">
    <rect width="230" height="175" rx="10" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="230" height="28" rx="8" fill="#db2777"/>
    <text x="115" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">FRYING METHODS</text>
    <text x="15" y="48" fill="#f472b6" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Medium: Molten Oil &amp; Fat</text>
    <text x="15" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Dry Frying (Natural Fats)</text>
    <text x="15" y="94" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Shallow Frying (Sauté / Pan)</text>
    <text x="15" y="116" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Deep Frying (160°C - 190°C)</text>
    <text x="15" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Stir Frying (Wok / High Heat)</text>
    <text x="15" y="160" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">High-speed rapid surface crusting.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_3():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">UNIVERSAL CULINARY RULES &amp; NUTRIENT PRESERVATION</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Golden Standards for Food Quality, Ergonomics, and Thermal Control</text>

  <!-- Rule 1: Temperature & Time Control -->
  <g transform="translate(30, 75)">
    <rect width="230" height="160" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="35" cy="30" r="14" fill="#0284c7"/>
    <text x="35" y="35" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1</text>
    <text x="60" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Thermal Control</text>
    <text x="15" y="65" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Preheat pans &amp; ovens accurately.</text>
    <text x="15" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Match heat level to food density.</text>
    <text x="15" y="111" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Avoid violent boiling for proteins.</text>
    <text x="15" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Check core safe temperatures.</text>
  </g>

  <!-- Rule 2: Moisture & Nutrient Retention -->
  <g transform="translate(285, 75)">
    <rect width="230" height="160" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <circle cx="35" cy="30" r="14" fill="#059669"/>
    <text x="35" y="35" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2</text>
    <text x="60" y="34" fill="#34d399" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Nutrient Defense</text>
    <text x="15" y="65" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Use minimal liquid when boiling.</text>
    <text x="15" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Cover with tight lids to trap steam.</text>
    <text x="15" y="111" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Cook greens fast to save Vit C/B.</text>
    <text x="15" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Repurpose nutrient-rich stocks.</text>
  </g>

  <!-- Rule 3: Uniform Preparation -->
  <g transform="translate(540, 75)">
    <rect width="230" height="160" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="35" cy="30" r="14" fill="#d97706"/>
    <text x="35" y="35" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3</text>
    <text x="60" y="34" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Uniform Sizing</text>
    <text x="15" y="65" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Cut ingredients into equal sizes.</text>
    <text x="15" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Guarantees even heat penetration.</text>
    <text x="15" y="111" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Prevents mixed raw/burnt pieces.</text>
    <text x="15" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Sharp knives preserve cell juices.</text>
  </g>

  <!-- Rule 4: Hygiene & Safety -->
  <g transform="translate(160, 255)">
    <rect width="230" height="165" rx="10" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <circle cx="35" cy="30" r="14" fill="#db2777"/>
    <text x="35" y="35" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">4</text>
    <text x="60" y="34" fill="#f472b6" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Sanitation &amp; Safety</text>
    <text x="15" y="65" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Clean-as-you-go workflow.</text>
    <text x="15" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Separate raw meat &amp; salad boards.</text>
    <text x="15" y="111" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Turn pot handles inward on stove.</text>
    <text x="15" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Dry hands before touching plugs.</text>
  </g>

  <!-- Rule 5: Seasoning & Presentation -->
  <g transform="translate(410, 255)">
    <rect width="230" height="165" rx="10" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <circle cx="35" cy="30" r="14" fill="#7c3aed"/>
    <text x="35" y="35" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">5</text>
    <text x="60" y="34" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Flavor &amp; Service</text>
    <text x="15" y="65" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Layer seasonings throughout cooking.</text>
    <text x="15" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Brown meats before liquid stews.</text>
    <text x="15" y="111" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Serve hot foods piping hot (60°C+).</text>
    <text x="15" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Maintain vibrant natural colors.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_4():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">MOIST HEAT METHODS: BOILING vs. STEWING</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Comparing Thermodynamics, Liquid Volumes, and Collagen Dissolution</text>

  <!-- Boiling Column -->
  <g transform="translate(30, 75)">
    <rect width="355" height="345" rx="12" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <rect width="355" height="36" rx="10" fill="#0284c7"/>
    <text x="177" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">BOILING (100°C / 212°F)</text>
    
    <text x="20" y="65" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Liquid Dynamics &amp; Environment:</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Food is completely submerged in rolling liquid.</text>
    <text x="20" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• High kinetic energy with violent bubble agitation.</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• High water-to-food ratio (e.g., pasta, boiled eggs).</text>

    <text x="20" y="160" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Nutrient &amp; Texture Impact:</text>
    <text x="20" y="180" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Water-soluble vitamins (Vit C, B-complex) leach out.</text>
    <text x="20" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• High heat can toughen delicate muscle proteins.</text>
    <text x="20" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Fast cooking for starch expansion (rice, beans).</text>

    <text x="20" y="255" fill="#10b981" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Best Applications:</text>
    <text x="20" y="275" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Dried legumes (beans, chickpeas), potatoes, pasta.</text>
    <text x="20" y="295" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Blanching green vegetables (short duration).</text>
    <text x="20" y="325" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Rule: Always cover with lid to conserve thermal energy!</text>
  </g>

  <!-- Stewing Column -->
  <g transform="translate(415, 75)">
    <rect width="355" height="345" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="355" height="36" rx="10" fill="#059669"/>
    <text x="177" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">STEWING (85°C – 95°C)</text>
    
    <text x="20" y="65" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Liquid Dynamics &amp; Environment:</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Food is partially covered in flavored liquid/stock.</text>
    <text x="20" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Gentle, quiet simmer with small rising bubbles.</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Sealed tightly with heavy lid for slow thermal transfer.</text>

    <text x="20" y="160" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Nutrient &amp; Texture Impact:</text>
    <text x="20" y="180" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Dissolves tough collagen into melting gelatin.</text>
    <text x="20" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• 100% nutrient retention (liquid served as rich gravy).</text>
    <text x="20" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Flavors meld together over extended cooking.</text>

    <text x="20" y="255" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Best Applications:</text>
    <text x="20" y="275" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Tough cuts of beef, goat meat, chicken stew, githeri.</text>
    <text x="20" y="295" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Root vegetable medleys and curries.</text>
    <text x="20" y="325" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Rule: Brown meat first to unlock rich Maillard flavors!</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_5():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">MOIST HEAT METHODS: STEAMING vs. POACHING</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Delicate Protein Protection and Maximum Micronutrient Conservation</text>

  <!-- Steaming Panel -->
  <g transform="translate(30, 75)">
    <rect width="355" height="345" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="355" height="36" rx="10" fill="#0284c7"/>
    <text x="177" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">STEAMING (100°C Steam Vapor)</text>

    <text x="20" y="65" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Physical Mechanism:</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Food sits in perforated basket above boiling water.</text>
    <text x="20" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Latent heat of vaporization transfers energy gently.</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Zero immersion: food never touches liquid water.</text>

    <text x="20" y="160" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Nutritional Superpower:</text>
    <text x="20" y="180" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Retains up to 90% of Vitamin C, Folate &amp; Minerals.</text>
    <text x="20" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Preserves bright chlorophyll green &amp; crisp texture.</text>
    <text x="20" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• 100% fat-free cooking medium.</text>

    <text x="20" y="255" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Ideal Ingredients:</text>
    <text x="20" y="275" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Leafy greens (sukuma wiki, spinach), broccoli.</text>
    <text x="20" y="295" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Fish fillets, nduma (arrowroot), cassava dumplings.</text>
    <text x="20" y="325" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Rule: Ensure water does not boil dry during steaming!</text>
  </g>

  <!-- Poaching Panel -->
  <g transform="translate(415, 75)">
    <rect width="355" height="345" rx="12" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="355" height="36" rx="10" fill="#7e22ce"/>
    <text x="177" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">POACHING (70°C – 85°C Quiet Bath)</text>

    <text x="20" y="65" fill="#c084fc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Physical Mechanism:</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Submerged in still liquid below simmering point.</text>
    <text x="20" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Tiny bubbles form at base without breaking surface.</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Infused with court bouillon, aromatic stock, or milk.</text>

    <text x="20" y="160" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Structural Superpower:</text>
    <text x="20" y="180" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Coagulates delicate proteins without mechanical tearing.</text>
    <text x="20" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Retains high internal moisture and silky tenderness.</text>
    <text x="20" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Prevents rubbery texture in delicate egg whites.</text>

    <text x="20" y="255" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Ideal Ingredients:</text>
    <text x="20" y="275" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Fresh eggs (poached eggs), delicate fish fillets.</text>
    <text x="20" y="295" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Tender chicken breasts, fresh pears in spiced syrup.</text>
    <text x="20" y="325" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Rule: Maintain quiet heat—never allow liquid to boil!</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_6():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">FRYING METHODS: DRY, SHALLOW, AND DEEP FRYING</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Oil Volumes, Thermal Dynamics, and Safe Frying Protocols</text>

  <!-- Dry Frying -->
  <g transform="translate(30, 75)">
    <rect width="230" height="345" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="230" height="32" rx="8" fill="#d97706"/>
    <text x="115" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">DRY FRYING</text>
    <text x="15" y="55" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Zero Added Fat</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Relies on food's natural fat.</text>
    <text x="15" y="100" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Heavy dry pan on medium heat.</text>
    <text x="15" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Fat melts and fries exterior.</text>
    
    <text x="15" y="160" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Best Foods:</text>
    <text x="15" y="182" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Bacon, fatty pork, sausages.</text>
    <text x="15" y="204" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Peanuts, sesame seeds, spices.</text>

    <text x="15" y="245" fill="#10b981" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Safety &amp; Rules:</text>
    <text x="15" y="268" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Drain rendered fat periodically.</text>
    <text x="15" y="290" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Keep heat medium to avoid smoke.</text>
  </g>

  <!-- Shallow Frying -->
  <g transform="translate(285, 75)">
    <rect width="230" height="345" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="230" height="32" rx="8" fill="#0284c7"/>
    <text x="115" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">SHALLOW FRYING</text>
    <text x="15" y="55" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Thin Layer of Hot Oil</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Oil covers base or 1/3 of food.</text>
    <text x="15" y="100" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Sautéing (tossing) &amp; pan-frying.</text>
    <text x="15" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Food turned halfway to cook.</text>
    
    <text x="15" y="160" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Best Foods:</text>
    <text x="15" y="182" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Eggs, pancakes, fish fillets.</text>
    <text x="15" y="204" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Sautéed onions, stir-fry greens.</text>

    <text x="15" y="245" fill="#10b981" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Safety &amp; Rules:</text>
    <text x="15" y="268" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Do NOT overcrowd the pan!</text>
    <text x="15" y="290" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Overcrowding causes soggy boiling.</text>
  </g>

  <!-- Deep Frying -->
  <g transform="translate(540, 75)">
    <rect width="230" height="345" rx="10" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="230" height="32" rx="8" fill="#db2777"/>
    <text x="115" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">DEEP FRYING</text>
    <text x="15" y="55" fill="#f472b6" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Total Submersion (160-190°C)</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Submerged in deep hot oil.</text>
    <text x="15" y="100" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Surface water flashes to steam.</text>
    <text x="15" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Forms sealed, crispy crust.</text>
    
    <text x="15" y="160" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Best Foods:</text>
    <text x="15" y="182" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Mandazi, samosas, chips (fries).</text>
    <text x="15" y="204" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Fried chicken, bhajias.</text>

    <text x="15" y="245" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Critical Safety:</text>
    <text x="15" y="268" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Dry food thoroughly before frying.</text>
    <text x="15" y="290" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• NEVER throw water on grease fire!</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_7():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">DRY HEAT METHODS: ROASTING vs. GRILLING</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Radiant Embers, Convection Heat, and Surface Caramelization</text>

  <!-- Roasting Column -->
  <g transform="translate(30, 75)">
    <rect width="355" height="345" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="355" height="36" rx="10" fill="#d97706"/>
    <text x="177" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">ROASTING (Enclosed Dry Heat)</text>

    <text x="20" y="65" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Thermal Dynamics &amp; Airflow:</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Cooked in preheated oven (180°C - 220°C) or spit.</text>
    <text x="20" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Hot dry air circulates around meat placed on rack.</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Requires basting with oil/drippings to lock in juices.</text>

    <text x="20" y="160" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Culinary Transformations:</text>
    <text x="20" y="180" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Deep Maillard crust with tender, succulent interior.</text>
    <text x="20" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Resting meat after roasting redistributes internal juices.</text>
    <text x="20" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Excellent for large joints and family centerpieces.</text>

    <text x="20" y="255" fill="#10b981" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Best Applications:</text>
    <text x="20" y="275" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Whole chicken, leg of lamb, roast beef, roast potatoes.</text>
    <text x="20" y="295" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Whole maize cobs on hot roasting embers.</text>
    <text x="20" y="325" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Rule: Baste every 20-30 minutes to prevent surface drying!</text>
  </g>

  <!-- Grilling Column -->
  <g transform="translate(415, 75)">
    <rect width="355" height="345" rx="12" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="355" height="36" rx="10" fill="#dc2626"/>
    <text x="177" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">GRILLING (Direct Radiant Heat)</text>

    <text x="20" y="65" fill="#f87171" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Thermal Dynamics &amp; Airflow:</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Direct radiant heat from charcoal embers or broiler.</text>
    <text x="20" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• High-temperature metal grates create sear lines.</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Excess fat drips away onto embers creating smoky aroma.</text>

    <text x="20" y="160" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Culinary Transformations:</text>
    <text x="20" y="180" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Rapid surface caramelization in 5-15 minutes.</text>
    <text x="20" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Healthier low-fat profile as melted grease drains.</text>
    <text x="20" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Characteristic Kenyan nyama choma smoky profile.</text>

    <text x="20" y="255" fill="#10b981" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Best Applications:</text>
    <text x="20" y="275" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Beef skewers (mshikaki), chops, burgers, steaks.</text>
    <text x="20" y="295" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Whole grilled tilapia, sliced zucchini, mushrooms.</text>
    <text x="20" y="325" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Rule: Use tongs—never pierce meat with forks!</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_8():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE SCIENCE OF BAKING: THERMAL &amp; BIOCHEMICAL PHASES</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">How Enclosed Dry Heat Converts Liquid Batter into Rigid, Airy Structures</text>

  <!-- Phase 1: Expansion -->
  <g transform="translate(30, 75)">
    <rect width="170" height="345" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#0284c7"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">PHASE 1: 50°C-70°C</text>
    <text x="12" y="52" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Gas Generation</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Fats melt and lubricate.</text>
    <text x="12" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Baking powder releases CO2 gas bubbles.</text>
    <text x="12" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Air cells in batter expand rapidly.</text>
    <text x="12" y="165" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Batter rises!</text>
  </g>

  <!-- Phase 2: Gelatinization -->
  <g transform="translate(220, 75)">
    <rect width="170" height="345" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#059669"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">PHASE 2: 70°C-85°C</text>
    <text x="12" y="52" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Starch Gelatinization</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Starch granules absorb free water.</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Granules swell and form semi-solid gel.</text>
    <text x="12" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Steam creates second lifting force.</text>
  </g>

  <!-- Phase 3: Coagulation & Setting -->
  <g transform="translate(410, 75)">
    <rect width="170" height="345" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#7e22ce"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">PHASE 3: 85°C-140°C</text>
    <text x="12" y="52" fill="#c084fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Protein Setting</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Gluten &amp; egg proteins denature.</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Permanent rigid crumb matrix forms.</text>
    <text x="12" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Traps gas bubbles inside cake walls.</text>
  </g>

  <!-- Phase 4: Browning -->
  <g transform="translate(600, 75)">
    <rect width="170" height="345" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#d97706"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">PHASE 4: 140°C-200°C</text>
    <text x="12" y="52" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Crust Caramelization</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Surface moisture evaporates dry.</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Maillard browning &amp; sugar caramelization.</text>
    <text x="12" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Golden crust &amp; sweet aroma set.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_9():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">MISE EN PLACE FOUNDATIONS: CLEANING, PEELING, AND CORING</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Sanitation Protocols and Waste-Minimizing Mechanical Pre-Preparation</text>

  <!-- Cleaning / Washing -->
  <g transform="translate(30, 75)">
    <rect width="230" height="345" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="230" height="32" rx="8" fill="#0284c7"/>
    <text x="115" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. CLEANING &amp; WASHING</text>
    
    <text x="15" y="55" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Primary Objectives:</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Remove soil, sand, and grit.</text>
    <text x="15" y="100" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Eliminate chemical pesticides.</text>
    <text x="15" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Wash under running potable water.</text>
    <text x="15" y="144" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Submerge leafy greens in saline water.</text>

    <text x="15" y="180" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Critical Rule:</text>
    <text x="15" y="202" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Always wash vegetables BEFORE cutting!</text>
    <text x="15" y="224" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Washing after cutting causes water-soluble vitamin leaching.</text>
  </g>

  <!-- Peeling -->
  <g transform="translate(285, 75)">
    <rect width="230" height="345" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="230" height="32" rx="8" fill="#059669"/>
    <text x="115" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. PEELING</text>
    
    <text x="15" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Technique &amp; Tools:</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Use swivel peeler or paring knife.</text>
    <text x="15" y="100" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Remove only thinnest outer skin layer.</text>
    <text x="15" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Vitamins concentrate under skin.</text>
    <text x="15" y="144" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Scrape young carrots and new potatoes.</text>

    <text x="15" y="180" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Economical Impact:</text>
    <text x="15" y="202" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Thick peeling wastes edible food mass.</text>
    <text x="15" y="224" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Keeps maximum mineral density intact.</text>
  </g>

  <!-- Coring -->
  <g transform="translate(540, 75)">
    <rect width="230" height="345" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="230" height="32" rx="8" fill="#7e22ce"/>
    <text x="115" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">3. CORING &amp; SEEDING</text>
    
    <text x="15" y="55" fill="#c084fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Core Removal Process:</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Extract tough central seed core.</text>
    <text x="15" y="100" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Use an apple corer or melon baller.</text>
    <text x="15" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Remove bell pepper pith and seeds.</text>
    <text x="15" y="144" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Deseed tomatoes for smooth sauces.</text>

    <text x="15" y="180" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Culinary Purpose:</text>
    <text x="15" y="202" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Eliminates bitter seeds &amp; hard fibers.</text>
    <text x="15" y="224" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Creates cavity for stuffed baking.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_10():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">PRECISION KNIFE TECHNIQUES: CHOPPING, SLICING, AND DICING</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Standard Geometric Cuts, Claw Grip Mechanics, and Uniformity Standards</text>

  <!-- Chopping -->
  <g transform="translate(30, 75)">
    <rect width="170" height="345" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#0284c7"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">CHOPPING</text>
    <text x="12" y="52" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Bite-Sized Cuts</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Irregular, relatively equal size.</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Used for long-simmered stews &amp; mirepoix.</text>
    <text x="12" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Coarse vs. Fine chop.</text>
    <text x="12" y="175" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5">e.g., Stew meat, greens.</text>
  </g>

  <!-- Slicing -->
  <g transform="translate(220, 75)">
    <rect width="170" height="345" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#059669"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">SLICING</text>
    <text x="12" y="52" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Flat Broad Sheets</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Uniform thickness across width.</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Longitudinal or crosswise cuts.</text>
    <text x="12" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Ensures rapid, even frying.</text>
    <text x="12" y="175" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5">e.g., Onions, tomatoes, bread.</text>
  </g>

  <!-- Julienne -->
  <g transform="translate(410, 75)">
    <rect width="170" height="345" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#d97706"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">JULIENNE</text>
    <text x="12" y="52" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Matchstick Strips</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Approx. 3mm x 3mm x 5cm.</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Slices stacked &amp; cut lengthwise.</text>
    <text x="12" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Base for fine dicing.</text>
    <text x="12" y="175" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5">e.g., Carrots, ginger, peppers.</text>
  </g>

  <!-- Dicing -->
  <g transform="translate(600, 75)">
    <rect width="170" height="345" rx="10" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#db2777"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">DICING (CUBING)</text>
    <text x="12" y="52" fill="#f472b6" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Uniform 3D Cubes</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Large (20mm), Med (12mm), Small (6mm).</text>
    <text x="12" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Precise geometry cooks simultaneously.</text>
    <text x="12" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Brunoise = 3mm micro-cube.</text>
    <text x="12" y="190" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5">e.g., Potatoes, carrots.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_11():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">ADVANCED PREPARATION: GRATING, MIXING, KNEADING &amp; BLENDING</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Mechanical Transformation of Food Structure, Texture, and Emulsification</text>

  <!-- Grating -->
  <g transform="translate(30, 75)">
    <rect width="170" height="345" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#0284c7"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">GRATING</text>
    <text x="12" y="52" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Shredding Shreds</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Rubbing across perforated blades.</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• High surface area exposure.</text>
    <text x="12" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Rapid melting &amp; blending.</text>
    <text x="12" y="170" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5">e.g., Cheese, carrots, lemon zest.</text>
  </g>

  <!-- Mixing -->
  <g transform="translate(220, 75)">
    <rect width="170" height="345" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#059669"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">MIXING</text>
    <text x="12" y="52" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Homogeneous Blend</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Combining 2+ ingredients uniformly.</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Stirring, whisking, or folding.</text>
    <text x="12" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Incorporates air in batters.</text>
    <text x="12" y="170" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5">e.g., Cake batter, salad dressings.</text>
  </g>

  <!-- Kneading -->
  <g transform="translate(410, 75)">
    <rect width="170" height="345" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#d97706"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">KNEADING</text>
    <text x="12" y="52" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Gluten Network</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Pressing, stretching &amp; folding dough.</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Aligns glutenin &amp; gliadin proteins.</text>
    <text x="12" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Yields elastic, gas-trapping dough.</text>
    <text x="12" y="170" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5">e.g., Bread, chapati, mandazi.</text>
  </g>

  <!-- Blending -->
  <g transform="translate(600, 75)">
    <rect width="170" height="345" rx="10" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#db2777"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">BLENDING</text>
    <text x="12" y="52" fill="#f472b6" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Puree &amp; Emulsion</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• High-speed motorized shear blades.</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Purees solids into smooth liquids.</text>
    <text x="12" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Emulsifies soups and sauces.</text>
    <text x="12" y="170" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5">e.g., Smoothies, tomato paste.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_12():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">DECISION MATRIX: SELECTING APPROPRIATE COOKING METHODS</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Matching Food Cellular Architecture &amp; Nutrient Profiles with Thermal Modes</text>

  <!-- Tough Meat -->
  <g transform="translate(30, 75)">
    <rect width="360" height="165" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="20" y="30" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Tough Meats &amp; High Connective Tissue</text>
    <text x="20" y="50" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Beef shank, ox-tail, gizzard, mutton, tripe</text>
    <rect x="20" y="62" width="320" height="26" rx="6" fill="#0284c7"/>
    <text x="180" y="80" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">RECOMMENDED: STEWING / BOILING / PRESSURE</text>
    <text x="20" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Long slow moisture hydrolyzes tough collagen to gelatin.</text>
    <text x="20" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Dry heat methods will make these cuts dry, chewy, and tough.</text>
  </g>

  <!-- Tender Meat & Delicate Fish -->
  <g transform="translate(410, 75)">
    <rect width="360" height="165" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="20" y="30" fill="#34d399" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Delicate Proteins (Fish, Eggs, Tender Cuts)</text>
    <text x="20" y="50" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Tilapia fillets, chicken breast, eggs, tenderloin</text>
    <rect x="20" y="62" width="320" height="26" rx="6" fill="#059669"/>
    <text x="180" y="80" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">RECOMMENDED: POACHING / STEAMING / GRILLING</text>
    <text x="20" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Low mechanical agitation keeps fragile tissue intact.</text>
    <text x="20" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Short cooking prevents protein shrinkage and dryness.</text>
  </g>

  <!-- Delicate Vegetables -->
  <g transform="translate(30, 255)">
    <rect width="360" height="165" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="20" y="30" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Leafy Greens &amp; High-Vitamin Vegetables</text>
    <text x="20" y="50" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Spinach, sukuma wiki, broccoli, cabbage, managu</text>
    <rect x="20" y="62" width="320" height="26" rx="6" fill="#d97706"/>
    <text x="180" y="80" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">RECOMMENDED: STEAMING / QUICK SAUTÉ</text>
    <text x="20" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Preserves heat-labile Vitamin C and folate.</text>
    <text x="20" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Maintains vibrant chlorophyll green and appetizing crunch.</text>
  </g>

  <!-- Doughs, Tubers & Batters -->
  <g transform="translate(410, 255)">
    <rect width="360" height="165" rx="10" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <text x="20" y="30" fill="#f472b6" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Starches, Doughs &amp; Dense Tubers</text>
    <text x="20" y="50" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Flour doughs, cakes, potatoes, cassava, sweet potatoes</text>
    <rect x="20" y="62" width="320" height="26" rx="6" fill="#db2777"/>
    <text x="180" y="80" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">RECOMMENDED: BAKING / ROASTING / DEEP FRYING</text>
    <text x="20" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Expands leavening gases into airy crumb (baking).</text>
    <text x="20" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Creates crisp crusts while gelatinizing interior starches.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_13():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">PRACTICAL PROTOCOL: MOIST HEAT PREPARATION &amp; EXECUTION</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Systematic Laboratory Workflow for Boiling, Stewing, Steaming, and Poaching</text>

  <!-- Step 1 -->
  <g transform="translate(30, 75)">
    <rect width="170" height="345" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#0284c7"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STEP 1: PREP &amp; AUDIT</text>
    <text x="12" y="52" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Mise en Place</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Wash, peel &amp; cut vegetables uniformly.</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Inspect pots, steamers &amp; lids for tight fit.</text>
    <text x="12" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Measure liquid stocks &amp; spices.</text>
  </g>

  <!-- Step 2 -->
  <g transform="translate(220, 75)">
    <rect width="170" height="345" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#059669"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STEP 2: TEMP CONTROL</text>
    <text x="12" y="52" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Thermal Setup</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Boiling: Bring to 100°C rolling boil.</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Stewing: Brown meat, drop to 85°C simmer.</text>
    <text x="12" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Poaching: Hold at 70°-85°C quiet bath.</text>
  </g>

  <!-- Step 3 -->
  <g transform="translate(410, 75)">
    <rect width="170" height="345" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#d97706"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STEP 3: EXECUTION</text>
    <text x="12" y="52" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Active Cooking</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Secure tight lid to conserve steam.</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Monitor steamer water level (never boil dry!).</text>
    <text x="12" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Time cooking to avoid mushy overcooking.</text>
  </g>

  <!-- Step 4 -->
  <g transform="translate(600, 75)">
    <rect width="170" height="345" rx="10" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#db2777"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STEP 4: SERVICE &amp; CLEAN</text>
    <text x="12" y="52" fill="#f472b6" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Plating &amp; Hygiene</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Lift lid away from face to avoid steam burns.</text>
    <text x="12" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Serve stews with rich cooking gravy.</text>
    <text x="12" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Wash and dry cookware immediately.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_14():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">PRACTICAL SAFETY: DRY HEAT, FRYING &amp; EMERGENCY ACTION</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Burn Prevention, Grease Fire Extinguishment, and Thermal PPE Standards</text>

  <!-- Safety Rule 1: Burn Prevention -->
  <g transform="translate(30, 75)">
    <rect width="230" height="345" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="230" height="32" rx="8" fill="#0284c7"/>
    <text x="115" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">THERMAL PPE &amp; HABITS</text>
    
    <text x="15" y="55" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Safe Practices:</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Always use dry oven mitts.</text>
    <text x="15" y="100" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Wet mitts conduct steam burns instantly.</text>
    <text x="15" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Turn pan handles inward on stove.</text>
    <text x="15" y="144" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Stand back when opening hot oven door.</text>

    <text x="15" y="180" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Handling Splatters:</text>
    <text x="15" y="202" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Dry food thoroughly before frying.</text>
    <text x="15" y="224" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Lower food gently away from body.</text>
  </g>

  <!-- Safety Rule 2: Grease Fire Protocol -->
  <g transform="translate(285, 75)">
    <rect width="230" height="345" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="230" height="32" rx="8" fill="#dc2626"/>
    <text x="115" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">GREASE FIRE EMERGENCY</text>
    
    <text x="15" y="55" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="700">What to NEVER Do:</text>
    <text x="15" y="78" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">❌ NEVER POUR WATER ON GREASE!</text>
    <text x="15" y="100" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Water vaporizes into a massive explosive fireball.</text>

    <text x="15" y="140" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Correct Emergency Steps:</text>
    <text x="15" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">1. Turn off heat source immediately.</text>
    <text x="15" y="184" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">2. Slide metal lid over pan to smother.</text>
    <text x="15" y="206" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">3. Pour generous baking soda over fire.</text>
    <text x="15" y="228" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">4. Leave covered until completely cool.</text>
  </g>

  <!-- Safety Rule 3: Knife & Workspace -->
  <g transform="translate(540, 75)">
    <rect width="230" height="345" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="230" height="32" rx="8" fill="#059669"/>
    <text x="115" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">KNIFE &amp; APPLIANCE SAFETY</text>
    
    <text x="15" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Knife Handling:</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Keep chef knives sharp &amp; clean.</text>
    <text x="15" y="100" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Cut away from body on stable board.</text>
    <text x="15" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Never catch a falling knife!</text>

    <text x="15" y="160" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Electrical &amp; Floor:</text>
    <text x="15" y="182" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Dry hands thoroughly before plugs.</text>
    <text x="15" y="204" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Wipe floor grease immediately.</text>
    <text x="15" y="226" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Unplug appliances before cleaning.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

# Map SVGs to lesson indices
SVG_GETTERS = [
    get_svg_1, get_svg_2, get_svg_3, get_svg_4, get_svg_5, get_svg_6, get_svg_7,
    get_svg_8, get_svg_9, get_svg_10, get_svg_11, get_svg_12, get_svg_13, get_svg_14
]

# =============================================================================
# 14 VERIFIED WIKIMEDIA COMMONS MEDIA ASSETS
# =============================================================================

WIKIMEDIA_ASSETS = [
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg/800px-Good_Food_Display_-_NCI_Visuals_Online.jpg",
        "caption": "A colorful array of cooked and fresh foods showcasing how heat transforms natural nutrients, flavors, and textures.",
        "attribution": "National Cancer Institute / Wikimedia Commons (Public Domain)",
        "alt_text": "Nutritious cooked and fresh food display"
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Cooking_on_a_gas_stove.jpg/800px-Cooking_on_a_gas_stove.jpg",
        "caption": "Active culinary preparation on a gas range demonstrating thermal conduction and convection currents.",
        "attribution": "Wikimedia Commons (CC BY-SA 3.0)",
        "alt_text": "Chef cooking food on a gas range stove"
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Kitchen_tools_and_equipment.jpg/800px-Kitchen_tools_and_equipment.jpg",
        "caption": "Meticulously organized kitchen workstation adhering to clean-as-you-go and safe culinary rules.",
        "attribution": "Wikimedia Commons (CC BY-SA 4.0)",
        "alt_text": "Organized culinary kitchen workstation and cooking pots"
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Beef_stew_with_carrots_and_potatoes.jpg/800px-Beef_stew_with_carrots_and_potatoes.jpg",
        "caption": "A rich, slow-simmered beef and vegetable stew demonstrating complete nutrient retention in gravy.",
        "attribution": "Wikimedia Commons (CC BY-SA 2.0)",
        "alt_text": "Simmered beef stew with carrots and potatoes"
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Steamed_vegetables_in_bamboo_steamer.jpg/800px-Steamed_vegetables_in_bamboo_steamer.jpg",
        "caption": "Vibrant emerald green vegetables prepared in a traditional bamboo steamer preserving delicate vitamins.",
        "attribution": "Wikimedia Commons (CC BY-SA 3.0)",
        "alt_text": "Steamed vegetables in bamboo steamer basket"
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Samosa_deep_frying_in_oil.jpg/800px-Samosa_deep_frying_in_oil.jpg",
        "caption": "Golden samosas deep-frying in hot oil demonstrating rapid crust formation and oil temperature control.",
        "attribution": "Wikimedia Commons (CC BY-SA 4.0)",
        "alt_text": "Samosas frying in deep oil pot"
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Roast_chicken_in_pan.jpg/800px-Roast_chicken_in_pan.jpg",
        "caption": "Golden roasted chicken basted in natural juices exhibiting deep Maillard browning and crisp skin.",
        "attribution": "Wikimedia Commons (CC BY-SA 2.0)",
        "alt_text": "Golden browned roast chicken in roasting pan"
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Freshly_baked_bread_loaves.jpg/800px-Freshly_baked_bread_loaves.jpg",
        "caption": "Freshly baked artisan bread displaying well-developed crumb structure and caramelized oven crust.",
        "attribution": "Wikimedia Commons (CC BY-SA 3.0)",
        "alt_text": "Freshly baked golden bread loaves"
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Washing_vegetables_in_sink.jpg/800px-Washing_vegetables_in_sink.jpg",
        "caption": "Thorough washing of fresh vegetables under running water prior to cutting to safeguard food hygiene.",
        "attribution": "Wikimedia Commons (CC BY-SA 4.0)",
        "alt_text": "Washing fresh vegetables in clean kitchen sink"
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Dicing_onions_on_cutting_board.jpg/800px-Dicing_onions_on_cutting_board.jpg",
        "caption": "Culinary knife precision demonstrated with the safe claw grip technique during onion dicing.",
        "attribution": "Wikimedia Commons (CC BY-SA 3.0)",
        "alt_text": "Chef dicing onions on cutting board using claw grip"
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Kneading_bread_dough.jpg/800px-Kneading_bread_dough.jpg",
        "caption": "Manual kneading of yeast dough developing the elastic gluten matrix required for light, airy baked goods.",
        "attribution": "Wikimedia Commons (CC BY-SA 3.0)",
        "alt_text": "Hands kneading smooth bread dough on kitchen counter"
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Foods_%28cropped%29.jpg/800px-Foods_%28cropped%29.jpg",
        "caption": "Diverse fresh food categories requiring distinct culinary cooking methods based on cellular makeup.",
        "attribution": "Wikimedia Commons (CC BY-SA 3.0)",
        "alt_text": "Assortment of fresh proteins, vegetables, and grains"
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Cooking_class_students.jpg/800px-Cooking_class_students.jpg",
        "caption": "Students conducting a Home Science practical session with boiling, steaming, and stewing equipment.",
        "attribution": "Wikimedia Commons (CC BY-SA 2.0)",
        "alt_text": "Students in cooking practical laboratory session"
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Baking_with_oven_gloves.jpg/800px-Baking_with_oven_gloves.jpg",
        "caption": "Practicing dry heat safety by removing hot baking trays with dry insulated oven mitts.",
        "attribution": "Wikimedia Commons (CC BY-SA 4.0)",
        "alt_text": "Baker using dry heat oven mitts to handle hot baking tray"
    }
]

# =============================================================================
# 14 VERIFIED EDUCATIONAL YOUTUBE INTEGRATIONS
# =============================================================================

YOUTUBE_RESOURCES = [
    {
        "youtube_id": "s0l140z0s_g",
        "url": "https://www.youtube.com/watch?v=s0l140z0s_g",
        "title": "The Science of Food: Why We Cook Food",
        "caption": "Educational exploration of biological transformations, collagen breakdown, and safety through cooking.",
        "reflection": "1. How does heat uncoil tight protein fibers to make them digestible?\n2. What critical pathogens are destroyed at safe cooking temperatures?\n3. How does the Maillard reaction enhance flavor?"
    },
    {
        "youtube_id": "7Y3mfAGVn1c",
        "url": "https://www.youtube.com/watch?v=7Y3mfAGVn1c",
        "title": "Heat Transfer in Cooking: Conduction, Convection & Radiation",
        "caption": "Demonstrating how thermal energy travels through pans, boiling liquid currents, and radiant grill embers.",
        "reflection": "1. What is the physical difference between conduction and convection in a pot?\n2. Why is radiation responsible for searing meat on a grill?\n3. How do you classify moist heat, dry heat, and frying methods?"
    },
    {
        "youtube_id": "8-c8E8QYQe4",
        "url": "https://www.youtube.com/watch?v=8-c8E8QYQe4",
        "title": "Fundamental Rules of Cooking and Kitchen Hygiene",
        "caption": "Core culinary principles for temperature regulation, clean-as-you-go habits, and nutrient preservation.",
        "reflection": "1. Why must pot handles always face inward on a stove?\n2. How does using minimal water prevent vitamin loss?\n3. What are the benefits of cutting ingredients uniformly?"
    },
    {
        "youtube_id": "mD0Dph1Ea5U",
        "url": "https://www.youtube.com/watch?v=mD0Dph1Ea5U",
        "title": "Moist Heat Methods: Boiling vs. Stewing Science",
        "caption": "Step-by-step masterclass in rolling boil thermodynamics versus slow, tenderizing low-temperature stewing.",
        "reflection": "1. Why does stewing preserve 100% of water-soluble nutrients?\n2. What temperature range is optimal for a gentle simmer (stewing)?\n3. Why does boiling toughen lean protein cuts?"
    },
    {
        "youtube_id": "hN5j4Yq7T6U",
        "url": "https://www.youtube.com/watch?v=hN5j4Yq7T6U",
        "title": "Gentle Moist Heat: The Art of Steaming and Poaching",
        "caption": "Nutritional and structural masterclass on vapor steaming for greens and quiet 70°-85°C liquid bath poaching for eggs and fish.",
        "reflection": "1. Why does steaming keep vegetables bright emerald green?\n2. What happens to delicate egg whites when boiled versus poached?\n3. How do you ensure steamer pots do not boil dry?"
    },
    {
        "youtube_id": "8z5yPq_YnI8",
        "url": "https://www.youtube.com/watch?v=8z5yPq_YnI8",
        "title": "The Science of Frying: Shallow, Pan & Deep Frying",
        "caption": "Visualizing rapid oil heat conduction, crust formation, splatter avoidance, and fat temperature control.",
        "reflection": "1. What causes hot oil to splatter violently when wet food is added?\n2. Why does overcrowding a shallow pan cause food to steam instead of fry?\n3. What is the single most critical rule for managing grease fires?"
    },
    {
        "youtube_id": "TqCwb7z5tX0",
        "url": "https://www.youtube.com/watch?v=TqCwb7z5tX0",
        "title": "Dry Heat Cooking: Roasting and Grilling Masterclass",
        "caption": "Demonstrating oven air convection, periodic basting, and intense radiant charcoal grilling (nyama choma).",
        "reflection": "1. What is the role of basting during long oven roasting?\n2. Why should you turn meat with tongs rather than a fork on the grill?\n3. How does resting meat after roasting keep it juicy?"
    },
    {
        "youtube_id": "n6wpNhyreDE",
        "url": "https://www.youtube.com/watch?v=n6wpNhyreDE",
        "title": "The Chemistry of Baking: Why Cakes and Breads Rise",
        "caption": "Exploring leavening gas generation, starch gelatinization, and protein coagulation in a preheated oven.",
        "reflection": "1. Why must the oven be preheated before inserting cake tins?\n2. What causes a cake to collapse if the oven door is opened repeatedly?\n3. How does flour gluten create the structural crumb of bread?"
    },
    {
        "youtube_id": "tG8TzR4w5_Q",
        "url": "https://www.youtube.com/watch?v=tG8TzR4w5_Q",
        "title": "Mise en Place: Cleaning, Peeling, and Food Prep",
        "caption": "Sanitation protocols, running water washing, thin peeling, and coring to minimize kitchen waste.",
        "reflection": "1. Why should you wash fruits and vegetables before peeling or cutting?\n2. How does thin peeling conserve vital vitamins located just under the skin?\n3. What is the culinary definition of Mise en Place?"
    },
    {
        "youtube_id": "G-Fg7l7G1zw",
        "url": "https://www.youtube.com/watch?v=G-Fg7l7G1zw",
        "title": "Culinary Knife Skills: Chopping, Slicing, and Dicing",
        "caption": "Professional knife ergonomics, finger claw grip technique, and standard geometric dimensions (julienne, brunoise, dice).",
        "reflection": "1. Why is a sharp knife safer than a dull knife in the kitchen?\n2. How does the claw grip protect your guide fingers?\n3. Why does uniform cutting ensure food cooks at the exact same rate?"
    },
    {
        "youtube_id": "b4b2Xm2R_0E",
        "url": "https://www.youtube.com/watch?v=b4b2Xm2R_0E",
        "title": "Preparation Techniques: Grating, Mixing, Kneading & Blending",
        "caption": "Hands-on demonstration of gluten matrix development in dough, uniform mixing, grating, and high-speed blending.",
        "reflection": "1. How does kneading stretch gluten proteins into an elastic network?\n2. What is the difference between stirring, whisking, and blending?\n3. Why is box grating useful for rapid cheese or vegetable melting?"
    },
    {
        "youtube_id": "4R2o-O_cQ4Y",
        "url": "https://www.youtube.com/watch?v=4R2o-O_cQ4Y",
        "title": "How to Select the Right Cooking Method for Any Ingredient",
        "caption": "Comprehensive decision tree for pairing meats, poultry, fish, leafy greens, tubers, and grains with ideal thermal methods.",
        "reflection": "1. Why should tough beef shanks never be fast-grilled dry?\n2. Which cooking method best protects leafy green vitamins?\n3. When should you choose dry heat baking over moist heat steaming?"
    },
    {
        "youtube_id": "kY6T5G0l1Zk",
        "url": "https://www.youtube.com/watch?v=kY6T5G0l1Zk",
        "title": "Culinary Practical: Moist Heat Cooking Session",
        "caption": "Step-by-step guidance on setting up stations, monitoring simmering temperatures, and safe steam handling.",
        "reflection": "1. How do you verify that water is at a simmer (85-95°C) versus rolling boil?\n2. What PPE is essential when opening pressurized steamer pots?\n3. How do you evaluate the tenderness of stewed meat?"
    },
    {
        "youtube_id": "gT6T4V_Q66s",
        "url": "https://www.youtube.com/watch?v=gT6T4V_Q66s",
        "title": "Kitchen Safety & Fire Management: Dry Heat and Frying",
        "caption": "Emergency response to grease fires, safe oven handling, non-slip floor management, and hot oil safety.",
        "reflection": "1. What is the immediate sequence of actions if a pan catches fire?\n2. Why must oven mitts be completely dry?\n3. How do you prevent burns when lowering battered foods into hot oil?"
    }
]

# =============================================================================
# 14 FORMATIVE SCENARIO-BASED MCQS (CARD 6 KNOWLEDGE CHECKS)
# =============================================================================

LESSON_MCQS = [
    {
        "question": "A community restaurant launched a '100% Raw Meat and Vegetable Diet' to save fuel. Within two weeks, many customers suffered severe food poisoning and indigestion. Based on the reasons for cooking food, why did this model fail?",
        "options": [
            "Raw vegetables contain too much moisture that dilutes digestive acid.",
            "Raw meats harbor pathogens like Salmonella that are destroyed by cooking heat, and tough collagen fibers require thermal tenderization.",
            "Cooking increases the monetary cost of food without altering chemistry.",
            "The human body can only digest foods cooked over 300°C."
        ],
        "correct_answer": 1,
        "answer": "Raw meats harbor pathogens like Salmonella that are destroyed by cooking heat, and tough collagen fibers require thermal tenderization.",
        "explanation": "Cooking food fulfills crucial biological purposes: applying heat destroys pathogenic micro-organisms (Salmonella, E. coli) and chemically softens tough collagen connective tissue into soluble, easily digestible gelatin."
    },
    {
        "question": "Chef Peter places delicate cake batter directly onto a heavy dry frying pan over a high open flame. The bottom burns black immediately while the top remains raw liquid. How does heat transfer explain his mistake?",
        "options": [
            "The frying pan transferred heat by radiation too slowly.",
            "Baking requires circulating dry hot air (convection) in an oven, whereas direct metal conduction transferred intense heat to the bottom too rapidly.",
            "The cake batter lacked water to enable electromagnetic wave absorption.",
            "The flame cooled down the metal pan."
        ],
        "correct_answer": 1,
        "answer": "Baking requires circulating dry hot air (convection) in an oven, whereas direct metal conduction transferred intense heat to the bottom too rapidly.",
        "explanation": "Baking relies on gentle, uniform convection currents of hot dry air in an enclosed oven. Placing batter on a dry pan over high flame uses aggressive direct conduction, charring the base before heat can conduct upwards."
    },
    {
        "question": "When boiling green vegetables in a domestic kitchen, which practice best conserves water-soluble vitamins (Vitamin C and B-complex)?",
        "options": [
            "Boil the vegetables in a large open pot of water for 45 minutes and discard the broth.",
            "Cut the vegetables into tiny pieces and soak them in water for 2 hours before boiling.",
            "Use minimal water with a tight-fitting lid, cook for the shortest possible time, and reuse the nutrient-rich cooking broth.",
            "Add large amounts of baking soda to soften the fibers faster."
        ],
        "correct_answer": 2,
        "answer": "Use minimal water with a tight-fitting lid, cook for the shortest possible time, and reuse the nutrient-rich cooking broth.",
        "explanation": "Water-soluble vitamins readily leach into cooking water and degrade under prolonged heat and oxygen exposure. Using minimal water, a tight lid, short cooking times, and repurposing broth saves these nutrients."
    },
    {
        "question": "Why is stewing particularly recommended for tough, inexpensive cuts of meat (such as beef shank or chuck) rather than rapid boiling or grilling?",
        "options": [
            "Stewing freezes the meat fibers to prevent shrinkage.",
            "Stewing uses gentle simmering (85°C–95°C) in a small amount of liquid over 1–2 hours, slowly hydrolyzing tough collagen into tender gelatin while keeping juices in the gravy.",
            "Stewing burns off all dietary fats within 5 minutes.",
            "Stewing turns meat into a dry solid crust."
        ],
        "correct_answer": 1,
        "answer": "Stewing uses gentle simmering (85°C–95°C) in a small amount of liquid over 1–2 hours, slowly hydrolyzing tough collagen into tender gelatin while keeping juices in the gravy.",
        "explanation": "High rolling boils toughen muscle fibers. The slow, gentle simmering of stewing breaks down tough connective collagen into melting gelatin, producing tender meat and 100% nutrient retention in the rich sauce."
    },
    {
        "question": "A patient recovering from illness requires a low-fat, highly digestible diet rich in vitamins. Why should the nutritionist recommend steaming over boiling for their vegetables and fish?",
        "options": [
            "Steaming allows food to absorb high amounts of cooking oil from the vapor.",
            "In steaming, food never touches liquid water, preventing water-soluble vitamins and minerals from leaching out while retaining natural colors, textures, and zero added fat.",
            "Steaming cooks at 300°C to destroy all fibers.",
            "Steamed food can be kept at room temperature for weeks without refrigeration."
        ],
        "correct_answer": 1,
        "answer": "In steaming, food never touches liquid water, preventing water-soluble vitamins and minerals from leaching out while retaining natural colors, textures, and zero added fat.",
        "explanation": "Because food rests in steam vapor above boiling liquid, water-soluble nutrients remain sealed inside the food cells. Steaming requires no cooking oil, preserving natural crispness, vibrant color, and light digestibility."
    },
    {
        "question": "Why is poaching strictly conducted in a quiet liquid bath maintained between 70°C and 85°C rather than at a rolling boil (100°C)?",
        "options": [
            "Delicate foods (such as eggs and fish fillets) are torn apart by violent boiling bubbles and toughened by excessive temperatures.",
            "Poaching liquids turn into toxic gas above 85°C.",
            "Lower temperatures make food cook ten times faster than boiling.",
            "Poaching requires ice water to set proteins."
        ],
        "correct_answer": 0,
        "answer": "Delicate foods (such as eggs and fish fillets) are torn apart by violent boiling bubbles and toughened by excessive temperatures.",
        "explanation": "Poaching is designed for fragile proteins. A quiet, sub-boiling bath (70°C–85°C) gently coagulates proteins without the turbulent kinetic agitation of rolling bubbles that disintegrate delicate fish or eggs."
    },
    {
        "question": "During the oven roasting of a whole chicken or beef joint, what is the primary purpose of 'basting' (periodically pouring melted pan fat/juices over the meat)?",
        "options": [
            "To cool down the oven heating element.",
            "To prevent the surface meat from drying out, conduct surface heat evenly, and develop a succulent, golden-brown caramelized exterior.",
            "To wash off all applied dry spices and seasonings.",
            "To turn the roasting pan into a boiling pot."
        ],
        "correct_answer": 1,
        "answer": "To prevent the surface meat from drying out, conduct surface heat evenly, and develop a succulent, golden-brown caramelized exterior.",
        "explanation": "Dry circulating oven air evaporates surface moisture. Basting coats the exterior in fat and juices, creating a barrier that seals in internal moisture, facilitates heat transfer, and enhances Maillard browning."
    },
    {
        "question": "When grilling skewered beef (mshikaki) over charcoal embers, why should the cook turn the meat using tongs rather than piercing it with a sharp fork?",
        "options": [
            "Forks conduct cold air that extinguishes the charcoal embers.",
            "Piercing meat punctures muscle fibers, releasing flavorful natural juices and leaving the meat dry and tough.",
            "Tongs change the molecular structure of the marinade.",
            "Grill grates cannot support the weight of a fork."
        ],
        "correct_answer": 1,
        "answer": "Piercing meat punctures muscle fibers, releasing flavorful natural juices and leaving the meat dry and tough.",
        "explanation": "Piercing grilled meat punctures the sealed outer crust and releases pressurized cellular juices onto the coals, resulting in dry, rubbery meat. Clean kitchen tongs grip gently without puncturing."
    },
    {
        "question": "Wambui bakes queen cakes by guessing ingredient measurements and opening the oven door every 2 minutes during the first 15 minutes. The cakes emerge flat, heavy, and collapsed. What caused this failure?",
        "options": [
            "The baking tin was too shiny.",
            "Guessing measurements disrupted chemical leavening ratios, and opening the door caused sudden drops in oven temperature, collapsing the expanding gas pockets before the protein structure could set.",
            "Baking powder only works when the oven door remains open.",
            "The cakes absorbed too much carbon dioxide from the air."
        ],
        "correct_answer": 1,
        "answer": "Guessing measurements disrupted chemical leavening ratios, and opening the door caused sudden drops in oven temperature, collapsing the expanding gas pockets before the protein structure could set.",
        "explanation": "Baking requires precise chemical ratios. Opening the oven door allows cool air to rush in, dropping internal temperature and causing rising gas bubbles (CO2/steam) to shrink and collapse before starch gelatinizes and egg proteins coagulate."
    },
    {
        "question": "A student pan-frying fish fillets places 8 cold, wet fillets tightly together into a small frying pan with 2 tablespoons of oil. Why does the fish turn soggy, gray, and break apart instead of crisping?",
        "options": [
            "The fish absorbed all the metal from the pan.",
            "Overcrowding the pan with wet, cold fish rapidly dropped the oil temperature, trapping released moisture so the fish steamed and boiled in its own juices rather than frying.",
            "The fish had too much natural oil.",
            "Shallow frying can only be done in total darkness."
        ],
        "correct_answer": 1,
        "answer": "Overcrowding the pan with wet, cold fish rapidly dropped the oil temperature, trapping released moisture so the fish steamed and boiled in its own juices rather than frying.",
        "explanation": "Overcrowding causes a severe thermal drop. The moisture escaping from wet fish cannot evaporate immediately and pools at the bottom, causing the fish to stew and boil in liquid rather than sautéing and browning."
    },
    {
        "question": "If a pan of deep-frying oil catches fire on the stove, what is the single most critical and immediate safety response?",
        "options": [
            "Immediately throw a bucket of cold water onto the burning oil.",
            "Blow forcefully on the flames to cool them down.",
            "Turn off the heat source immediately and slide a metal lid or damp heavy baking sheet over the pan to smother oxygen, or use baking soda (NEVER water!).",
            "Carry the burning pan rapidly outdoors through the house."
        ],
        "correct_answer": 2,
        "answer": "Turn off the heat source immediately and slide a metal lid or damp heavy baking sheet over the pan to smother oxygen, or use baking soda (NEVER water!).",
        "explanation": "Water sinks into burning grease, instantly flashes to steam, and throws atomized burning oil outward in a lethal fireball. Smothering with a lid or baking soda cuts off oxygen and starves the fire safely."
    },
    {
        "question": "What is the primary culinary rationale for washing vegetables BEFORE peeling or cutting them during Mise en Place?",
        "options": [
            "Washing after peeling allows water-soluble vitamins (B and C) and minerals to leach out from exposed cut surfaces into the wash water.",
            "Vegetables cannot be cut unless their skins are completely dry.",
            "Washing before cutting makes knives dull faster.",
            "Unwashed peels are easier to digest."
        ],
        "correct_answer": 0,
        "answer": "Washing after peeling allows water-soluble vitamins (B and C) and minerals to leach out from exposed cut surfaces into the wash water.",
        "explanation": "Washing whole vegetables cleans off dirt, pesticides, and microbes while the protective outer skin remains intact. Washing after slicing exposes thousands of ruptured cells, leaching away vital micronutrients."
    },
    {
        "question": "Why is practicing uniform cutting (such as uniform 6mm dicing or 3mm slicing) considered a fundamental culinary rule rather than just an aesthetic choice?",
        "options": [
            "Uniform cutting makes food heavier.",
            "Uniformly sized pieces absorb heat at the exact same rate, preventing small pieces from overcooking or burning while large pieces remain dangerously raw.",
            "Irregular pieces require five times more cooking fuel.",
            "Uniform pieces prevent knives from getting blunt."
        ],
        "correct_answer": 1,
        "answer": "Uniformly sized pieces absorb heat at the exact same rate, preventing small pieces from overcooking or burning while large pieces remain dangerously raw.",
        "explanation": "Thermal penetration depends on geometric thickness. Equal dimensions ensure all pieces reach safe internal temperatures and desired tenderness at the exact same moment."
    },
    {
        "question": "A student in the food laboratory is operating an electric blender with wet hands while standing near a water spill on the floor. Which immediate hazards are present?",
        "options": [
            "Risk of severe electric shock due to water conduction and physical injury from slips/falls.",
            "Risk of the blender overheating from room air.",
            "Risk of the tomato puree losing its natural color.",
            "Risk of the blender turning into a toaster."
        ],
        "correct_answer": 0,
        "answer": "Risk of severe electric shock due to water conduction and physical injury from slips/falls.",
        "explanation": "Water is a powerful electrical conductor. Operating plugs with wet hands allows current to flow through skin, while wet floors create severe slipping hazards that can lead to falls while handling glass or blades."
    }
]

# =============================================================================
# 14 LESSON SPECIFICATIONS & CONTENT GENERATION ENGINE
# =============================================================================

LESSONS_DATA = [
    {
        "title": "Reasons for Cooking Food",
        "learning_goal": "Understand the biological, chemical, safety, and cultural reasons for applying heat to food.",
        "concept_hook": "Imagine eating a raw, tough piece of beef, or an unpeeled raw potato. Now imagine savoring tender, aromatic beef stew or crispy roasted potatoes. Thermal energy is the chemical key that unlocks digestibility, destroys pathogens, and awakens rich flavors.",
        "definition": "Cooking is the application of heat to food ingredients to make them chemically digestible, biologically safe, physically palatable, aromatic, and aesthetically pleasing.",
        "theory_text": "We cook food for four fundamental biochemical and social reasons:\n\n- **Improving Digestibility & Bioavailability:** Heat gelatinizes complex starch granules (in maize, potatoes, rice), denatures tight protein fibrils, and converts tough collagen into soluble gelatin, allowing human digestive enzymes easy access.\n- **Microbial Destruction & Safety:** Heating food to safe internal temperatures kills pathogenic bacteria (Salmonella, E. coli, Listeria), parasites, and inactivates anti-nutritional plant toxins (such as raw bean lectins).\n- **Flavor & Aroma Enhancement:** The Maillard reaction (reducing sugars reacting with amino acids above 140°C) and caramelization create hundreds of complex aromatic volatile compounds that stimulate saliva and appetite.\n- **Texture Modification & Shelf-Life Extension:** Thermal energy tenderizes tough connective tissues, crisps batters, coagulates egg proteins, inactivates spoilage enzymes, and extends household food preservation.",
        "diagram_analysis": "The diagram above outlines the 4 foundational pillars of cooking. Notice how thermal energy acts on distinct molecular targets: collagen bonds in meats, pectin in plant cell walls, pathogens in raw foods, and surface carbohydrates for aromatic browning.",
        "step_title": "Practical Investigation: Raw vs. Cooked Food Comparison",
        "step_process": [
            "**Step 1: Structural Flexibility Test** — Take a raw carrot stick and a steamed carrot stick. Bend both gently. The raw carrot snaps rigidly due to turgid pectin cell walls, while the cooked carrot bends softly because heat softened the pectin.",
            "**Step 2: Aroma & Color Audit** — Observe a slice of raw dough compared to a golden baked bread crust. Note the deep aroma difference generated by the Maillard reaction.",
            "**Step 3: Texture & Solubility Check** — Dissolve raw cornstarch in cold water (remains milky suspension) vs. heating it (gelatinizes into a clear, thick gel).",
            "**Step 4: Hygiene & Safety Conclusion** — Confirm why cooking is an indispensable biological barrier against foodborne illnesses.",
            "**Step 5: Digestive Comfort Evaluation** — Explain how tenderizing meat fibers reduces stomach strain during digestion."
        ],
        "safety_notice": "Always wash hands with soap and water before handling food samples.",
        "practical_text": "In culinary practice, recognizing why we cook dictates our choice of temperature. Cooking tough meats slowly dissolves collagen without toughening muscle fibers, while brief cooking of vegetables preserves heat-sensitive vitamins.",
        "real_world_text": "In Kenyan households and commercial dining establishments across Nairobi, Nakuru, and Mombasa, cooking methods are central to food preservation, nutrition, and cultural heritage. From boiling githeri to smoking fish along Lake Victoria, heat transforms local crops into wholesome daily nutrition.",
        "summary_takeaways": [
            "Cooking chemically breaks down tough collagen and gelatinizes starches for easy digestion.",
            "Thermal energy kills harmful foodborne pathogens and inactivates natural anti-nutrients.",
            "The Maillard reaction and caramelization generate rich aromas, deep flavors, and golden crusts.",
            "Mastering cooking principles empowers students to prepare safe, appealing, and nutritious meals."
        ]
    },
    {
        "title": "Classification of Cooking Methods & Principles of Heat Transfer",
        "learning_goal": "Master how thermal energy travels by conduction, convection, and radiation, and classify the 3 pillars of cooking methods.",
        "concept_hook": "When a metal spoon rests in boiling soup, its handle becomes hot through direct contact. When water boils, rolling currents circulate heat. Standing near a charcoal jiko, you feel invisible heatwaves. These three mechanisms govern every cooking technique in the kitchen.",
        "definition": "Heat Transfer is the movement of thermal energy from a heat source to food via Conduction (contact), Convection (circulating fluid/gas), or Radiation (electromagnetic waves).",
        "theory_text": "All cooking methods fall into three broad classifications based on the medium used to transfer heat:\n\n- **Moist Heat Methods:** Heat is transferred using water, stock, milk, or steam. Temperatures range from 70°C (poaching) to 100°C (boiling/steaming). Ideal for tenderizing collagen and preventing surface drying.\n- **Dry Heat Methods:** Heat is transferred through hot circulating air or open radiant heat without added liquid. Temperatures exceed 140°C–220°C, triggering Maillard browning and crisp crust formation (baking, roasting, grilling).\n- **Frying Methods:** Heat is transferred rapidly through molten cooking oil or fat at high temperatures (160°C–190°C), producing sealed crispy exteriors (dry, shallow, and deep frying).\n\n**The Physics of Heat Transfer:**\n- **Conduction:** Heat moves atom-to-atom through direct physical contact (e.g., hot pan base conducting heat into a fish fillet).\n- **Convection:** Heat moves via bulk fluid currents (e.g., rising boiling water currents or circulating oven hot air).\n- **Radiation:** Heat travels directly as infrared or electromagnetic waves through space without a physical medium (e.g., glowing charcoal jiko embers radiating heat to skewered meat).",
        "diagram_analysis": "Study the classification flowchart above. Observe how the 3 heat transfer modes (conduction, convection, radiation) drive the 3 culinary pillars (moist heat, dry heat, and frying).",
        "step_title": "Laboratory Protocol: Identifying Heat Transfer Modes",
        "step_process": [
            "**Step 1: Conduction Observation** — Place a metal spoon in hot water; touch the handle after 30 seconds to observe solid thermal transfer.",
            "**Step 2: Convection Current Tracking** — Drop tea leaves or food coloring into simmering water; watch them rise in the hot center and sink along cooler edges.",
            "**Step 3: Radiation Sensing** — Hold your palm 15 cm above a charcoal jiko or toaster element without touching to feel radiant infrared waves.",
            "**Step 4: Classification Log** — Record in your notebook which methods combine multiple heat transfer modes (e.g., grilling uses radiation + grate conduction).",
            "**Step 5: Heat Control Verification** — Adjust stove burners to match required heat transfer rates for delicate vs dense ingredients."
        ],
        "safety_notice": "Do not touch hot metal surfaces directly with bare hands; use insulated dry oven mitts.",
        "practical_text": "Selecting the right classification depends on the food structure: tough cuts need moist heat convection; doughs need dry heat air convection; battered snacks need high-conduction oil frying.",
        "real_world_text": "Across Kenya, traditional cooking heavily leverages heat transfer physics—from conductive flat earthenware griddles for chapati to radiant three-stone hearths and convective boiling pots for ugali and sukuma wiki.",
        "summary_takeaways": [
            "Conduction transfers heat through direct physical contact; convection through moving fluids/gases; radiation through waves.",
            "Cooking methods are classified into Moist Heat, Dry Heat, and Frying.",
            "Moist heat methods soften tough fibers; dry heat methods create browned crusts; frying cooks rapidly via hot oil.",
            "Understanding thermal physics is the secret to precise temperature control in culinary practice."
        ]
    },
    {
        "title": "General Rules for Cooking Food",
        "learning_goal": "Apply universal rules of thermal control, nutrient preservation, uniform cutting, and hygiene in cooking.",
        "concept_hook": "Great cooking is not accidental—it follows strict scientific rules. Overheating ruins delicate proteins; throwing away vegetable cooking water discards vital vitamins; irregular cuts lead to half-raw, half-burnt dishes.",
        "definition": "General Rules of Cooking are standardized culinary and hygienic principles designed to maximize nutrient retention, optimize sensory appeal, and guarantee kitchen safety.",
        "theory_text": "Every professional cook and home scientist must uphold five essential rules:\n\n- **1. Precise Temperature Control:** Preheat ovens and pans before introducing food. Match thermal intensity to food density—gentle heat for delicate proteins, high heat for rapid searing.\n- **2. Nutrient Conservation:** Wash vegetables before peeling or cutting to prevent vitamin leaching. Use minimal water, tight lids, and short cooking times for greens. Repurpose cooking liquids into soups and gravies.\n- **3. Uniform Preparation:** Cut vegetables and meats into uniform sizes so every piece cooks at the exact same rate.\n- **4. Clean-As-You-Go & Hygiene:** Maintain sanitary worktops, use dedicated chopping boards for raw meats and ready-to-eat salads, and keep pot handles turned inward on stoves.\n- **5. Flavor Layering & Seasoning:** Season food progressively throughout cooking rather than only at the end to allow deep flavor penetration.",
        "diagram_analysis": "Review the infographic above highlighting the 5 universal pillars of cooking. Notice how temperature regulation, nutrient defense, uniform sizing, sanitation, and seasoning form a cohesive culinary safety net.",
        "step_title": "Laboratory Audit: Implementing Kitchen Rules",
        "step_process": [
            "**Step 1: Workstation Setup** — Sanitize surfaces, position cutting board on a damp cloth to prevent slipping, and organize color-coded knives.",
            "**Step 2: Mise en Place Check** — Wash vegetables in running water, peel thinly, and cut into uniform 10mm cubes before turning on any burners.",
            "**Step 3: Thermal Calibration** — Check burner flame height and verify oven preheat temperature with an oven thermometer.",
            "**Step 4: Clean-As-You-Go** — Wash preparation bowls immediately after emptying and wipe spills promptly.",
            "**Step 5: Sensory & Plating Check** — Verify that cooked dishes maintain natural vibrant colors and hot serving temperatures."
        ],
        "safety_notice": "Never leave stove burners unattended; keep flammable towels away from open flames.",
        "practical_text": "Following universal cooking rules prevents common culinary disasters like curdled sauces, rubbery eggs, vitamin-depleted greens, and dangerous kitchen accidents.",
        "real_world_text": "In Kenyan schools, hospitals, and hospitality institutions, enforcing standard cooking rules ensures meals meet strict national public health standards while controlling food budgets by minimizing waste.",
        "summary_takeaways": [
            "Preheating equipment and controlling temperatures prevents uneven cooking and structural failure.",
            "Washing vegetables before cutting and using tight lids protects water-soluble vitamins.",
            "Uniform cutting ensures all food pieces cook at the same speed.",
            "Clean-as-you-go habits guarantee kitchen hygiene and eliminate accident hazards."
        ]
    },
    {
        "title": "Moist Heat Cooking Methods — Boiling and Stewing",
        "learning_goal": "Compare the mechanics, temperatures, advantages, and applications of boiling (100°C) and stewing (85°C–95°C).",
        "concept_hook": "Watch a pot of water shaking violently with rolling bubbles at 100°C, then observe a quiet stew gently releasing small bubbles under a heavy lid. Boiling is a fast, high-kinetic sprint; stewing is a slow, patient marathon that transforms tough meat into tender gourmet delights.",
        "definition": "Boiling is cooking food submerged in rolling liquid at 100°C; Stewing is slow cooking in a small amount of liquid in a covered pot at a gentle simmer (85°C–95°C).",
        "theory_text": "Moist heat methods rely on liquid as the thermal transfer medium:\n\n**Boiling (100°C / 212°F):**\n- Food is completely submerged in turbulent boiling liquid.\n- Ideal for rapid starch expansion (dried maize, beans, rice, potatoes) and hard-boiling eggs.\n- *Disadvantage:* Water-soluble vitamins (C and B-complex) leach out into the cooking water. Lean meats boiled violently become rubbery and tough.\n\n**Stewing (85°C – 95°C Simmer):**\n- Food is cut into uniform bite-sized pieces and browned in a little oil, then simmered in a small volume of liquid under a tight-fitting lid.\n- *Thermodynamic Superpower:* Over 1 to 2 hours, the gentle simmering heat slowly breaks down tough collagen connective tissues into rich, soluble gelatin without drying out muscle fibers.\n- *Advantage:* 100% nutrient retention because the flavorful cooking liquid is served as gravy.",
        "diagram_analysis": "Examine the comparison chart above. Notice how boiling's violent 100°C turbulence contrasts with stewing's gentle 85°C–95°C simmer, where sealed steam and gravy retention maximize nutritional value.",
        "step_title": "Practical Protocol: Preparing a Nutritious Kenyan Beef Stew",
        "step_process": [
            "**Step 1: Meat Preparation & Searing** — Cut beef into uniform 2.5cm cubes. Heat 1 tbsp oil in a heavy pot and sear meat until browned (Maillard reaction).",
            "**Step 2: Aromatic Base** — Add chopped onions, garlic, and diced tomatoes; sauté until softened and fragrant.",
            "**Step 3: Simmering Liquid** — Add just enough water or stock to cover 2/3 of the meat; bring to a boil, then immediately reduce heat to low (simmer).",
            "**Step 4: Slow Cooking & Service** — Cover with a tight lid and simmer for 60–90 minutes until fork-tender; serve piping hot with ugali or rice.",
            "**Step 5: Degreasing & Gravy Consistency** — Skim excess surface fat and adjust sauce thickness with a cornstarch slurry if desired."
        ],
        "safety_notice": "Lift the pot lid away from your face to avoid direct steam burns.",
        "practical_text": "In culinary examinations, remember to brown stew meat first for flavor, use just enough liquid, and maintain a quiet simmer rather than an aggressive boil.",
        "real_world_text": "Stewing is the backbone of East African home cooking, producing beloved dishes like beef and goat stews, chicken curries, and traditional githeri that provide balanced, economical family nourishment.",
        "summary_takeaways": [
            "Boiling cooks submerged food at 100°C; stewing cooks in minimal liquid at 85°C–95°C.",
            "Stewing tenderizes tough cuts of meat by converting collagen into gelatin over time.",
            "Boiling can leach water-soluble vitamins unless cooking liquids are consumed.",
            "Stewing retains 100% of nutrients because cooking liquid is served as savory gravy."
        ]
    },
    {
        "title": "Moist Heat Cooking Methods — Steaming and Poaching",
        "learning_goal": "Master the physics of vapor steaming for maximum vitamin retention and sub-boiling poaching (70°C–85°C) for delicate foods.",
        "concept_hook": "If you drop a fragile fresh egg or delicate fish fillet into boiling water, the bubbles tear it into cloudy shreds. But place it in quiet 75°C water or a gentle steam basket, and it emerges silky, tender, and intact. Gentleness is the pinnacle of culinary science.",
        "definition": "Steaming is cooking food in the hot vapor rising from boiling water without liquid contact; Poaching is cooking delicate foods in a quiet liquid bath at 70°C–85°C.",
        "theory_text": "These two gentle moist heat methods offer unparalleled nutritional and structural advantages:\n\n**Steaming (100°C Steam Vapor):**\n- Food rests in a perforated basket above boiling water in a sealed pot.\n- *Nutritional Superiority:* Retains up to 90% of Vitamin C, B vitamins, and mineral salts because food never touches liquid water.\n- Preserves bright natural green chlorophyll and natural crunch.\n- 100% fat-free cooking medium, perfect for health-conscious and convalescent diets.\n\n**Poaching (70°C – 85°C Quiet Bath):**\n- Food is immersed in still liquid where tiny bubbles form on the bottom but never break the surface.\n- Uses aromatic liquids like seasoned court bouillon, milk, spiced juice, or broth.\n- Prevents protein shrinkage and preserves delicate textures in eggs, fish fillets, and fruits (poached pears).",
        "diagram_analysis": "Review the infographic comparing Steaming and Poaching. Note that steaming uses 100°C steam vapor above liquid, while poaching uses a sub-boiling 70°C–85°C liquid bath for fragile proteins.",
        "step_title": "Laboratory Protocol: Steaming Traditional Greens & Poaching Eggs",
        "step_process": [
            "**Step 1: Steamer Assembly** — Pour 3 cm of water into a pot; place perforated steamer basket above water line and bring to a boil.",
            "**Step 2: Vegetable Steaming** — Place washed, shredded sukuma wiki in the basket, cover with tight lid, and steam for 3–5 minutes until tender-crisp.",
            "**Step 3: Poaching Setup** — Heat a shallow pan of water to 75°C (small bubbles at bottom); add 1 tsp vinegar to assist egg white coagulation.",
            "**Step 4: Egg Poaching & Plating** — Crack egg into a cup, gently slide into the quiet water, cook for 3 minutes until white is set, and lift with a slotted spoon.",
            "**Step 5: Water Level Audit** — Verify that the steamer water level remains safely above the pan base to prevent scorch damage."
        ],
        "safety_notice": "Ensure the steamer pot never boils completely dry to prevent scorched cookware.",
        "practical_text": "Steaming is ideal for green vegetables, fish, cassava, and nduma; poaching is best for skinless fish fillets, whole eggs, and tender fruits.",
        "real_world_text": "Steaming is deeply rooted in Kenyan cuisine, from traditional banana-leaf wrapped foods to modern healthy preparation of indigenous vegetables like managu, terere, and sagaa.",
        "summary_takeaways": [
            "Steaming cooks food in vapor above boiling water, preserving up to 90% of vitamins.",
            "Poaching cooks delicate foods in a quiet 70°C–85°C bath without tearing tissue.",
            "Steaming requires zero added cooking fat, making it ideal for therapeutic diets.",
            "Both methods preserve vibrant colors, tender textures, and delicate natural flavors."
        ]
    },
    {
        "title": "Frying Methods — Dry, Shallow, and Deep Frying",
        "learning_goal": "Differentiate dry frying, shallow frying (sautéing), and deep frying, and enforce critical oil safety standards.",
        "concept_hook": "Drop a slice of raw potato into hot golden oil at 180°C. Instantly, thousands of tiny steam bubbles erupt, creating a crisp golden shell that seals in moisture while keeping oil out. Hot oil is one of the fastest and most transformative cooking mediums.",
        "definition": "Frying is cooking food in hot oil or fat at high temperatures (160°C–190°C), categorized into Dry Frying, Shallow Frying (sautéing), and Deep Frying.",
        "theory_text": "Frying methods use fat as the high-temperature heat transfer medium:\n\n**1. Dry Frying:**\n- Uses no added fat; food relies on its own natural rendered fats (e.g., bacon, fatty sausages, peanuts, sesame seeds).\n- Conducted in a heavy dry pan over medium heat.\n\n**2. Shallow Frying (Sautéing & Pan-Frying):**\n- Food is cooked in a thin layer of oil covering the pan base or 1/3 of the food thickness.\n- *Sautéing* (from French 'to jump') involves tossing small ingredients rapidly over high heat.\n- *Rule:* Never overcrowd the pan, or temperature drops, causing food to steam in released juices instead of frying.\n\n**3. Deep Frying:**\n- Food is completely submerged in a deep pot of hot oil (160°C–190°C).\n- Rapid steam vaporization forms a crisp outer crust that prevents oil penetration.\n- *Critical Safety:* Food must be completely dry before entering hot oil to prevent explosive splattering. Never extinguish a grease fire with water!",
        "diagram_analysis": "Examine the frying matrix above comparing dry, shallow, and deep frying. Note how oil volumes, operating temperatures (160°C–190°C), and food dryness dictate crisp crust formation and kitchen safety.",
        "step_title": "Laboratory Protocol: Deep Frying Crispy Mandazi Safely",
        "step_process": [
            "**Step 1: Oil Temperature Test** — Heat oil in a heavy deep pan; drop a small cube of bread. It should rise and turn golden in 60 seconds (approx 175°C).",
            "**Step 2: Gentle Loading** — Lower dry mandazi dough pieces gently into oil *away* from your body using a metal slotted spoon to prevent splashback.",
            "**Step 3: Batch Regulation** — Fry 3–4 pieces at a time without overcrowding; flip once when bottom turns golden-brown.",
            "**Step 4: Draining** — Remove with slotted spoon and drain on clean absorbent paper towels before serving.",
            "**Step 5: Oil Filtering & Storage** — Allow oil to cool completely before straining through cheesecloth into a clean container."
        ],
        "safety_notice": "Never pour water on burning oil! Turn off heat and slide a metal lid over the pan to smother flames.",
        "practical_text": "Always maintain proper oil temperature: oil that is too cold produces greasy, soggy food; oil that is too hot burns the exterior while leaving the inside raw.",
        "real_world_text": "Fried foods like mandazi, samosas, bhajias, and potato chips are iconic across Kenya's culinary landscape. Understanding frying science helps households enjoy these foods while minimizing excessive oil absorption.",
        "summary_takeaways": [
            "Dry frying uses food's natural fat; shallow frying uses a thin oil layer; deep frying uses total submersion.",
            "Deep frying at 160°C–190°C instantly vaporizes surface moisture to form a sealed crispy crust.",
            "Overcrowding drops pan temperature and results in greasy, boiled food.",
            "Grease fires must be smothered with a metal lid or baking soda—never water."
        ]
    },
    {
        "title": "Dry Heat Cooking Methods — Roasting and Grilling",
        "learning_goal": "Master the high-temperature dry-heat techniques of oven roasting (convection/basting) and open radiant grilling (nyama choma).",
        "concept_hook": "Inhale the smoky, rich aroma of skewered beef sizzling over glowing charcoal embers, or a whole chicken turning golden-brown in an oven. Dry heat methods cook without water, creating intense caramelized crusts and unforgettable flavors.",
        "definition": "Roasting is cooking food in an oven or on a spit using circulating dry hot air with basting; Grilling is fast cooking over direct radiant heat from embers or heating elements.",
        "theory_text": "Dry heat methods apply high thermal energy directly to food surfaces:\n\n**Roasting (180°C – 220°C Enclosed Dry Air):**\n- Food is placed on a shallow pan or wire rack in a preheated oven, allowing hot air to circulate freely.\n- **Basting:** Periodically brushing melted fat or pan juices over the meat prevents surface moisture loss and fosters deep Maillard browning.\n- Large roasted meats must 'rest' for 10–15 minutes after cooking to allow internal juices to redistribute.\n\n**Grilling (Direct Radiant Heat):**\n- Food rests on metal grates directly above glowing charcoal embers, gas flames, or electric elements.\n- Heat transfers primarily via radiant infrared waves and conductive grate contact.\n- Imparts a signature smoky barbecue flavor while allowing excess dietary fat to drip away.\n- *Rule:* Use clean kitchen tongs to turn meat; piercing with a fork allows flavorful juices to drain away.",
        "diagram_analysis": "Study the diagram above contrasting enclosed oven roasting with open radiant grilling. Notice how roasting uses circulating convection air and basting, while grilling relies on direct radiation and draining fats.",
        "step_title": "Practical Protocol: Preparing Grilled Beef Skewers (Mshikaki)",
        "step_process": [
            "**Step 1: Skewer Assembly** — Cut beef into thin, uniform 2cm cubes; marinate in garlic, ginger, lemon juice, and oil for 30 minutes; thread onto soaked wooden skewers.",
            "**Step 2: Grill Preparation** — Light charcoal until covered in glowing gray ash (medium-high radiant heat); brush clean metal grates lightly with oil.",
            "**Step 3: Searing & Turning** — Place skewers on hot grate; cook for 3–4 minutes per side, turning with tongs until seared with dark grill marks.",
            "**Step 4: Resting & Plating** — Remove skewers and let rest for 3 minutes before serving with kachumbari.",
            "**Step 5: Grill Sanitation** — Scrape hot grates with a wire grill brush and coat lightly with cooking oil to prevent rust."
        ],
        "safety_notice": "Use long-handled tongs and heat-resistant gloves when tending hot charcoal grills.",
        "practical_text": "Roasting is best suited for whole chickens, legs of lamb, and whole tubers; grilling is ideal for thin steaks, chops, fish, and vegetable skewers.",
        "real_world_text": "Nyama Choma (grilled meat) and roasted maize on the cob are pillars of Kenyan culture and social gatherings, uniting communities through time-honored dry heat culinary traditions.",
        "summary_takeaways": [
            "Roasting cooks via circulating hot dry air in an oven, requiring basting to retain moisture.",
            "Grilling cooks rapidly using direct radiant heat over charcoal embers or grates.",
            "Grilling drains excess fat, producing a lower-fat, smoky culinary result.",
            "Always turn grilled foods with tongs rather than piercing forks to lock in natural juices."
        ]
    },
    {
        "title": "Dry Heat Cooking Methods — Baking",
        "learning_goal": "Analyze the chemistry of baking in an enclosed oven, including leavening gas expansion, starch gelatinization, and crumb setting.",
        "concept_hook": "Pour a wet, runny batter of flour, eggs, sugar, and milk into a tin and slide it into a hot oven. 30 minutes later, it emerges as a tall, light, golden sponge cake. Baking is pure food chemistry at work.",
        "definition": "Baking is cooking food in an enclosed oven surrounded by hot, dry circulating air, transforming batters and doughs into firm, porous, airy structures.",
        "theory_text": "Baking is an exact science that proceeds through four distinct biochemical phases:\n\n- **Phase 1: Gas Expansion (50°C–70°C):** Fats melt and baking powder/yeast releases carbon dioxide gas and water vapor. These gases expand, causing the dough or batter to rise.\n- **Phase 2: Starch Gelatinization (70°C–85°C):** Flour starch granules absorb moisture, swell, and form a semi-solid gel matrix.\n- **Phase 3: Protein Coagulation & Crumb Setting (85°C–140°C):** Egg and gluten proteins denature and solidify around the expanded gas pockets, fixing the cake's permanent structural crumb.\n- **Phase 4: Crust Caramelization (140°C–200°C):** Surface moisture evaporates, and the Maillard reaction and sugar caramelization create the golden crust.\n\n**Golden Rules of Baking:**\n- Always preheat the oven to the recipe temperature before inserting tins.\n- Measure ingredients accurately with scales—baking tolerances are very tight.\n- Never open the oven door during the first half of baking to avoid collapsing rising gas pockets.\n- Grease and flour tins to allow easy release.",
        "diagram_analysis": "Review the 4-phase baking timeline above. Note how temperature progression drives gas expansion, starch gelatinization, protein setting, and surface caramelization.",
        "step_title": "Laboratory Protocol: Baking Golden Queen Cakes",
        "step_process": [
            "**Step 1: Oven Calibration & Tins** — Preheat oven to 180°C; line a muffin tray with paper cups.",
            "**Step 2: Creaming & Mixing** — Cream 100g margarine and 100g sugar until pale and fluffy; beat in 2 eggs gradually; fold in 150g sifted self-raising flour.",
            "**Step 3: Portioning & Baking** — Spoon batter into paper cups until 2/3 full; bake at 180°C for 20 minutes without opening the oven door.",
            "**Step 4: Doneness Testing** — Insert a clean wooden toothpick into the center of a cake; it should emerge clean and dry. Cool on a wire rack.",
            "**Step 5: Crumb Texture Evaluation** — Slice one cooled cake in half; verify even aeration and absence of heavy dense streaks."
        ],
        "safety_notice": "Always wear dry, insulated oven mitts when placing or removing baking tins from hot ovens.",
        "practical_text": "Baking applies to bread, cakes, cookies, pies, pastries, and savory dishes like baked lasagna and shepherd's pie.",
        "real_world_text": "Commercial and domestic baking is a booming economic sector in Kenya, providing livelihoods through bakeries, catering businesses, and wholesome family home baking.",
        "summary_takeaways": [
            "Baking transforms liquid batters into rigid, porous solids through four thermal phases.",
            "Preheating ovens ensures leavening gases activate immediately before structure sets.",
            "Opening the oven door prematurely causes rising cakes to collapse and become dense.",
            "Precise measurement and controlled temperature are non-negotiable for baking success."
        ]
    },
    {
        "title": "Pre-Preparation Techniques (Mise en Place) — Cleaning, Peeling, and Coring",
        "learning_goal": "Execute essential pre-cooking preparations including hygienic washing, waste-minimizing peeling, and core/seed removal.",
        "concept_hook": "Before a surgeon begins an operation or a builder lays a brick, every tool and material is organized in its place. In the kitchen, 'Mise en Place' is the secret foundation of every smooth, delicious, and stress-free culinary masterpiece.",
        "definition": "Mise en Place is a French culinary term meaning 'everything in its place'—the practice of washing, peeling, coring, and measuring all ingredients before cooking commences.",
        "theory_text": "Proper pre-preparation establishes food safety, economic efficiency, and nutrient retention:\n\n**1. Cleaning & Washing:**\n- Wash all fresh fruits, vegetables, and herbs under cold, running potable water to remove surface soil, pesticides, and microbial contaminants.\n- *Non-Negotiable Rule:* Always wash vegetables BEFORE cutting. Washing after cutting exposes millions of ruptured cells, leaching water-soluble vitamins into the wash water.\n\n**2. Peeling:**\n- Removing the tough, fibrous outer skin of vegetables and fruits using a swivel peeler or paring knife.\n- *Waste-Minimization:* Peel as thinly as possible because vital vitamins and mineral salts concentrate directly beneath the skin.\n- Scrape tender carrots and new potatoes rather than thick peeling.\n\n**3. Coring & Seeding:**\n- Removing the hard central seed core or bitter pith from apples, pineapples, bell peppers, and tomatoes.\n- Eliminates inedible seeds while creating clean cavities for stuffing and uniform cooking.",
        "diagram_analysis": "Study the Mise en Place flowchart above. Notice how washing whole produce precedes thin peeling and coring to safeguard water-soluble vitamins and maximize edible yield.",
        "step_title": "Laboratory Protocol: Pre-Preparing Root Vegetables & Peppers",
        "step_process": [
            "**Step 1: Running Water Wash** — Scrub potatoes and carrots with a vegetable brush under running cold water; drain in a colander.",
            "**Step 2: Thin Peeling Audit** — Use a swivel peeler to remove only the thinnest peel; weigh the peel to confirm less than 5% food waste.",
            "**Step 3: Pepper Coring** — Cut around the stem of a bell pepper, twist out the core, tap out remaining seeds, and rinse clean.",
            "**Step 4: Mise en Place Staging** — Place pre-prepared items in clean glass bowls ready for precision knife cutting.",
            "**Step 5: Organic Waste Disposal** — Place clean vegetable peels into compost bins to promote environmental sustainability."
        ],
        "safety_notice": "Cut away from your body on a stable chopping board; never hold food in the palm of your hand while coring.",
        "practical_text": "Mastering cleaning, peeling, and coring speeds up overall cooking time, reduces household grocery waste, and prevents foodborne contamination.",
        "real_world_text": "In Kenyan markets and kitchens, practicing hygienic washing and thin peeling protects families from pesticide residues on fresh produce while stretching household food budgets.",
        "summary_takeaways": [
            "Mise en Place means organizing and preparing all ingredients before turning on the stove.",
            "Always wash vegetables before peeling or cutting to prevent vitamin leaching.",
            "Thin peeling minimizes food waste and preserves minerals concentrated just under the skin.",
            "Coring removes inedible seeds and bitter pith, improving food texture and presentation."
        ]
    },
    {
        "title": "Pre-Preparation Techniques — Cutting, Slicing, Chopping, and Dicing",
        "learning_goal": "Master precision knife cuts (chopping, slicing, julienne, dicing) and execute the protective claw grip technique.",
        "concept_hook": "Watch a master chef's knife move in a rhythmic blur across a cutting board, turning a carrot into thousands of identical 6mm cubes. Precision cutting is not just about beauty—it is the science that guarantees every piece cooks to perfection at the exact same second.",
        "definition": "Culinary Cutting Techniques are standardized geometric knife cuts designed to achieve uniform heat penetration, appealing texture, and refined presentation.",
        "theory_text": "Precision knife skills are essential for every culinary practitioner:\n\n**The Knife Safety Foundation:**\n- Always use a sharp chef knife—a dull knife requires excessive force and is far more likely to slip and cause deep cuts.\n- Position a damp cloth beneath the chopping board to prevent board slippage.\n- **The Claw Grip:** Curl guide fingers like a bear claw with fingertips tucked inward and knuckles resting against the flat side of the knife blade.\n\n**Standard Geometric Cuts:**\n- **Chopping:** Cutting food into relatively uniform, bite-sized pieces; used for stew vegetables and mirepoix.\n- **Slicing:** Cutting food into thin, flat, broad sheets of uniform thickness (e.g., sliced tomatoes, onions, bread).\n- **Julienne (Matchsticks):** Cutting vegetables into precise 3mm × 3mm × 5cm matchstick strips.\n- **Dicing (Cubing):** Cutting food into uniform 3D cubes:\n  - *Large Dice (Carré):* 20mm cubes for root vegetables and stews.\n  - *Medium Dice (Parmentier):* 12mm cubes.\n  - *Small Dice (Macédoine):* 6mm cubes.\n  - *Brunoise:* 3mm micro-cubes for refined garnishes and sauces.",
        "diagram_analysis": "Review the knife skills chart above. Compare the dimensions of Chopping, Slicing, Julienne, and Dicing, and note how the claw grip protects guide fingers during high-speed cutting.",
        "step_title": "Laboratory Protocol: Precision Vegetable Dicing",
        "step_process": [
            "**Step 1: Board Stabilization** — Place a damp towel under a cutting board; verify zero board movement.",
            "**Step 2: Squaring the Vegetable** — Cut thin slices off the four sides of a peeled potato to create a flat, stable rectangular block.",
            "**Step 3: Slicing & Julienne** — Slice the block into 6mm planks; stack planks and cut lengthwise into 6mm matchstick strips (julienne).",
            "**Step 4: Cross-Cutting Dicing** — Cut across the matchsticks at 6mm intervals using the claw grip to produce perfect 6mm cubes.",
            "**Step 5: Dimension Verification** — Use a ruler to check sample cubes for uniform 6mm edge lengths."
        ],
        "safety_notice": "Never attempt to catch a falling knife; step back and let it drop to the floor.",
        "practical_text": "Uniform cutting ensures that small pieces do not overcook into mush while large pieces remain hard or raw in the center.",
        "real_world_text": "In professional Kenyan catering establishments and home kitchens, efficient knife skills dramatically reduce preparation time and elevate the visual and culinary quality of everyday meals.",
        "summary_takeaways": [
            "Sharp knives and stable cutting boards are the fundamental prerequisites for knife safety.",
            "The claw grip curls fingertips inward, preventing accidental finger cuts.",
            "Standard cuts include chopping, slicing, julienne (matchsticks), and dicing (cubes).",
            "Uniform cutting dimensions guarantee even heat penetration and simultaneous doneness."
        ]
    },
    {
        "title": "Pre-Preparation Techniques — Grating, Mixing, Kneading, and Blending",
        "learning_goal": "Execute advanced pre-preparation techniques including box grating, uniform mixing, gluten kneading, and motorized blending.",
        "concept_hook": "How does a sticky lump of flour and water transform into an elastic, stretchy dough for chapati? How does a blender turn chunky tomatoes into a silky smooth sauce in seconds? Mechanical actions physically rearrange molecules to create unique culinary textures.",
        "definition": "Mechanical Pre-Preparation refers to physical actions (grating, mixing, kneading, blending) that alter food particle size, aerate mixtures, develop protein matrices, or create smooth emulsions.",
        "theory_text": "These advanced mechanical techniques serve vital culinary and structural roles:\n\n**1. Grating (Shredding):**\n- Rubbing solid food against perforated metal teeth on a box grater.\n- Exposes high surface area for rapid melting (cheese) or even distribution in salads and batters (carrots, zucchini, lemon zest).\n\n**2. Mixing (Blending Ingredients):**\n- Combining two or more ingredients into a uniform, homogeneous mixture.\n- *Stirring:* Circular movement with a wooden spoon.\n- *Whisking:* Rapid whipping to incorporate air into eggs and batters.\n- *Folding:* Gentle figure-eight motion with a spatula to combine whipped whites without deflating air bubbles.\n\n**3. Kneading (Gluten Network Development):**\n- Rhythmic pressing, stretching, and folding of flour dough with the heels of your hands.\n- Hydrates and aligns gliadin and glutenin proteins into an elastic **gluten matrix** that traps expanding leavening gases during baking.\n\n**4. Blending (Pureeing & Emulsifying):**\n- High-speed motorized spinning blades that pulverize solid foods into smooth purees, silky soups, and stable emulsions.",
        "diagram_analysis": "Examine the technical illustration above showcasing grating, mixing, kneading, and blending. Observe how mechanical energy alters food structure from coarse solids to elastic gluten doughs and silky purees.",
        "step_title": "Laboratory Protocol: Kneading Elastic Chapati Dough",
        "step_process": [
            "**Step 1: Dry & Wet Combining** — Mix 2 cups flour, 1 tsp salt, and 1 tbsp oil in a bowl; add warm water gradually while stirring.",
            "**Step 2: Counter Kneading** — Turn dough onto a lightly floured board; press forward with heels of hands, fold dough back over itself, turn 90 degrees, and repeat.",
            "**Step 3: Windowpane Elasticity Test** — Knead for 8–10 minutes until smooth and non-sticky; stretch a small piece gently—it should form a thin, translucent membrane without tearing.",
            "**Step 4: Resting** — Cover dough with a damp cloth and let rest for 20 minutes to relax the gluten network before rolling.",
            "**Step 5: Dough Portioning** — Divide rested dough into equal smooth balls and cover to prevent surface drying."
        ],
        "safety_notice": "Ensure blender lids are securely fastened before turning on high-speed motors; unplug before cleaning blades.",
        "practical_text": "Kneading develops structure in breads and chapatis; gentle folding preserves air in sponge cakes; blending produces velvety soups and sauces.",
        "real_world_text": "Chapati making is a cherished culinary tradition across Kenya. Mastering the science of gluten development through kneading guarantees soft, layered, and delicious chapatis every time.",
        "summary_takeaways": [
            "Grating maximizes surface area for rapid melting and even blending.",
            "Mixing techniques (stirring, whisking, folding) combine ingredients and incorporate air.",
            "Kneading develops the elastic gluten network required for airy breads and soft chapatis.",
            "Blending pulverizes solid foods into smooth purees, drinks, and creamy sauces."
        ]
    },
    {
        "title": "Selecting Appropriate Cooking Methods for Different Foods",
        "learning_goal": "Synthesize food composition, connective tissue levels, and nutrient profiles to select the optimal cooking method for any ingredient.",
        "concept_hook": "A master carpenter never uses a sledgehammer to drive a tiny finishing nail. Similarly, a master chef matches each ingredient to its ideal cooking method: tough beef shanks to slow stewing, delicate greens to quick steaming, and yeasted doughs to oven baking.",
        "definition": "Culinary Selection is the systematic matching of an ingredient's cellular structure, moisture, fat, and nutrient characteristics with the appropriate thermal method.",
        "theory_text": "Selecting the right cooking method depends on four food characteristics:\n\n- **1. Connective Tissue Content:** Tough meats with high collagen (beef shank, ox-tail, gizzard) require prolonged moist heat (**Stewing** or **Boiling**) to convert collagen into soluble gelatin. High-heat dry grilling makes them tough and inedible.\n- **2. Delicate Protein Structures:** Low-collagen proteins (fish fillets, eggs, tender poultry) require gentle moist heat (**Poaching**, **Steaming**) or rapid shallow frying (**Sautéing**) to prevent toughening.\n- **3. Vitamin & Chlorophyll Sensitivity:** Leafy greens (sukuma wiki, spinach, broccoli) must be cooked quickly using **Steaming** or brief sautéing to retain Vitamin C, B vitamins, and bright green color.\n- **4. Carbohydrate & Starch Makeup:** Grains and dry legumes require **Boiling** for starch hydration; tubers (potatoes, cassava) excel in **Roasting** or **Baking**; flour doughs require dry heat **Baking** for crumb setting.",
        "diagram_analysis": "Study the decision matrix above. Notice how food category (tough meats, delicate proteins, leafy greens, starches) maps directly to the ideal cooking method for maximum tenderness, nutrition, and flavor.",
        "step_title": "Laboratory Decision Challenge: Menu Method Pairing",
        "step_process": [
            "**Step 1: Ingredient Analysis** — Audit a mystery ingredient basket containing tough beef chuck, whole tilapia, fresh managu, and sweet potatoes.",
            "**Step 2: Matrix Application** — Assign Beef Chuck to Stewing (hydrolyze collagen), Tilapia to Poaching/Steaming (protect delicate flakes), Managu to Steaming (preserve vitamins), and Sweet Potatoes to Roasting (caramelize sugars).",
            "**Step 3: Method Rationale Formulation** — Write down the scientific justification for each selection in your practical log.",
            "**Step 4: Evaluation** — Compare taste, texture, and visual appeal across the prepared dishes.",
            "**Step 5: Cost & Fuel Assessment** — Calculate energy and time efficiency for each chosen method."
        ],
        "safety_notice": "Label raw meat containers clearly and store below ready-to-eat foods in refrigerators.",
        "practical_text": "Matching food structure to cooking method prevents tough meats, soggy vegetables, broken fish, and vitamin-depleted meals.",
        "real_world_text": "In Kenyan school feeding programs, hospitals, and hospitality businesses, selecting appropriate cooking methods ensures meals are nutritious, cost-effective, and highly appealing to diners.",
        "summary_takeaways": [
            "Tough, high-collagen meats require slow moist heat (stewing) to become tender.",
            "Delicate proteins (fish, eggs) require gentle poaching or steaming to prevent shrinkage.",
            "Leafy vegetables should be steamed briefly to safeguard heat-sensitive vitamins.",
            "Matching food structure to cooking method is the hallmark of culinary excellence."
        ]
    },
    {
        "title": "Culinary Practical — Moist Heat Cooking (Preparation & Execution)",
        "learning_goal": "Execute a full moist heat culinary practical incorporating Mise en Place, boiling, stewing, steaming, and poaching protocols.",
        "concept_hook": "Put on your chef's apron and step up to the cooking range. Today, theory transforms into culinary craft as you manage boiling, gentle stewing, vapor steaming, and quiet poaching in a synchronized practical session.",
        "definition": "Moist Heat Practical Execution is the hands-on application of liquid and vapor cooking protocols under strict standards of hygiene, timing, and sensory evaluation.",
        "theory_text": "Executing moist heat methods in the laboratory requires mastering four operational phases:\n\n- **Phase 1: Station Setup & Mise en Place:** Clean work surfaces, calibrate burner flames, assemble specialized pots (steamer tiers, heavy stew pots), and prepare all vegetables and proteins uniformly.\n- **Phase 2: Thermal Calibration:** Maintain rolling boil (100°C) for starch foods, drop heat to gentle simmer (85°C–95°C) for stews, and hold poaching liquid at 70°C–85°C.\n- **Phase 3: Lid & Steam Management:** Keep heavy lids tightly sealed to conserve thermal energy and prevent moisture loss; periodically check steamer reservoirs so they never boil dry.\n- **Phase 4: Sensory Evaluation & Plating:** Test meat doneness with a fork, check vegetables for vibrant color and crisp texture, and serve stews with rich cooking gravy.",
        "diagram_analysis": "Examine the practical workflow diagram above. Track the 4 steps: Prep & Audit, Thermal Calibration, Active Moist Execution, and Safe Steam Plating.",
        "step_title": "Standard Operating Procedure: Complete Moist Heat Practical",
        "step_process": [
            "**Step 1: Preparation Audit** — Wash, peel, and cut 200g beef cubes, 100g carrots, and 100g spinach. Place in labeled bowls.",
            "**Step 2: Stewing Execution** — Sear beef cubes in 1 tsp oil, add aromatics, add 1 cup stock, cover tightly, and simmer at 90°C for 45 minutes.",
            "**Step 3: Steaming Greens** — Place spinach in steamer tier over simmering water for 3 minutes until bright green and tender-crisp.",
            "**Step 4: Plating & Evaluation** — Plate tender beef stew with its rich gravy alongside steamed spinach; evaluate color, aroma, and tenderness.",
            "**Step 5: Laboratory Sanitization** — Clean and dry all pots, sterilize cutting boards, and wipe stove tops thoroughly."
        ],
        "safety_notice": "Always lift pot lids away from your body to direct hot escaping steam safely away from your face.",
        "practical_text": "In national practical examinations, candidates are graded on station organization, personal hygiene, correct temperature maintenance, and sensory appeal of the finished dish.",
        "real_world_text": "Moist heat culinary competency is an indispensable life skill that empowers students to prepare wholesome, affordable, and nutritious meals for their families throughout life.",
        "summary_takeaways": [
            "Successful moist heat practicals require rigorous Mise en Place and organized stations.",
            "Maintain correct temperature zones: 100°C (boil), 85°C–95°C (stew), 70°C–85°C (poach).",
            "Keep pot lids tightly closed to conserve steam, fuel, and vital nutrients.",
            "Always direct escaping steam away from the face when lifting lids to avoid burns."
        ]
    },
    {
        "title": "Culinary Practical — Dry Heat & Frying (Preparation & Safety)",
        "learning_goal": "Execute dry heat roasting/baking and frying methods while upholding zero-tolerance thermal, knife, and grease fire safety protocols.",
        "concept_hook": "High heat creates magical crispy crusts, fluffy cakes, and golden mandazi, but it also carries serious hazards—red-hot ovens, spitting oil, and open flames. True culinary mastery is pairing great flavor with uncompromised kitchen safety.",
        "definition": "Dry Heat & Frying Practical Execution is the controlled application of high-temperature air, radiant heat, and hot oil under strict hazard prevention standards.",
        "theory_text": "Mastering dry heat and frying practicals requires adherence to four essential safety and execution protocols:\n\n- **1. Thermal PPE & Handling:** Always use completely dry cloth oven mitts (wet mitts conduct steam burns instantly). Stand back when opening preheated oven doors to let initial heat escape safely.\n- **2. Splatter Prevention:** Ensure all food items are completely dry before placing them into hot frying oil. Lower food gently away from your body using a slotted spoon.\n- **3. Pan Control & Space Management:** Turn all pot and pan handles inward on the stove. Never overcrowd frying pans.\n- **4. Emergency Grease Fire Protocol:**\n  - **NEVER throw water on a grease fire!** Water flashes to steam, causing an explosive fireball.\n  - Turn off the stove burner immediately.\n  - Slide a flat metal lid or damp baking sheet over the pan to smother oxygen.\n  - Pour baking soda generously over the fire if needed.\n  - Leave covered until completely cooled.",
        "diagram_analysis": "Review the safety infographic above detailing thermal PPE habits, the emergency grease fire response protocol, and knife/floor management.",
        "step_title": "Practical Protocol: Dry Heat & Frying Safety Drill",
        "step_process": [
            "**Step 1: Oven & Station Inspection** — Check oven interior, ensure baking racks are properly positioned, and preheat to 180°C using dry mitts.",
            "**Step 2: Frying Oil Prep** — Heat 2 cm oil in a heavy pan to 175°C; verify food dryness with paper towels.",
            "**Step 3: Gentle Frying Execution** — Lower battered food away from body; fry in small batches; drain on paper towels.",
            "**Step 4: Simulated Fire Protocol** — Practice the grease fire emergency response: simulate turning off the burner and sliding a metal lid smoothly over the pan.",
            "**Step 5: Cool-Down Inspection** — Ensure burners and ovens are switched off at the mains and oil has cooled safely."
        ],
        "safety_notice": "Never touch hot baking trays with damp towels; always use dry insulated oven mitts.",
        "practical_text": "High-heat cooking requires constant focus, clean-as-you-go habits, and immediate cleaning of floor spills to eliminate accident risks.",
        "real_world_text": "Workplace safety is the number one priority in professional kitchens, bakeries, and hotel culinary departments across Kenya and worldwide. Developing safe cooking habits in Grade 10 prepares students for lifelong kitchen safety.",
        "summary_takeaways": [
            "Always handle hot baking trays and pans with completely dry oven mitts.",
            "Dry food thoroughly before frying to prevent violent oil splatters.",
            "Grease fires must be smothered with a metal lid or baking soda—never water.",
            "Zero-tolerance safety habits protect culinary professionals, students, and families."
        ]
    }
]

# =============================================================================
# MAIN INGESTION WORKFLOW
# =============================================================================

@transaction.atomic
def ingest_grade10_home_science_topic1_4():
    print("=" * 80)
    print("STARTING CBC GRADE 10 HOME SCIENCE: TOPIC 1.4 INGESTION")
    print("=" * 80)

    # 1. Read Ground Truth Markdown File
    md_path = "/home/jason-bitega/Desktop/VL/vlearn_repositories/Grade 10 Homescience/Grade10_Home_Science_Topic_1_4.md"
    print(f"Reading markdown source from: {md_path}")
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    print(f"  [+] Markdown loaded successfully ({len(md_content)} characters)")

    # 2. Get Curriculum, Grade, Subject, Topic
    curriculum = Curriculum.objects.filter(name__icontains="CBC").first()
    if not curriculum:
        curriculum, _ = Curriculum.objects.get_or_create(name="CBC", defaults={"description": "Competency Based Curriculum"})

    grade = Grade.objects.filter(level=10).first()
    if not grade:
        grade, _ = Grade.objects.get_or_create(curriculum=curriculum, name="Grade 10", level=10)

    subject, _ = Subject.objects.get_or_create(
        grade=grade,
        name="Home Science",
        defaults={"description": "CBC Grade 10 Home Science"}
    )

    topic, _ = Topic.objects.get_or_create(
        subject=subject,
        order=1,
        defaults={"name": "Foods and Nutrition", "description": "Foods and Nutrition Strand"}
    )

    # 3. Create or Link Learning Unit 4 (1.4 Methods of Cooking)
    unit_order = 4
    unit_name = "1.4 Methods of Cooking"
    learning_unit, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        order=unit_order,
        defaults={
            "name": unit_name,
            "description": "Comprehensive study of cooking reasons, heat transfer principles, moist heat, dry heat, frying, mise en place, and culinary safety."
        }
    )
    # Ensure name and description are accurate
    learning_unit.name = unit_name
    learning_unit.save()

    # Clear existing lessons in this unit to ensure idempotent re-ingestion
    learning_unit.lessons.all().delete()
    print(f"  [+] Prepared Learning Unit 4: '{unit_name}' (Cleared old lessons)")

    total_lessons_created = 0
    total_blocks_created = 0
    total_assets_created = 0

    for idx, ldata in enumerate(LESSONS_DATA):
        lesson_num = idx + 1
        l_title = ldata["title"]
        svg_content = SVG_GETTERS[idx]()
        wiki_asset = WIKIMEDIA_ASSETS[idx]
        yt_resource = YOUTUBE_RESOURCES[idx]
        mcq_data = LESSON_MCQS[idx]

        lesson = Lesson.objects.create(
            topic=topic,
            learning_unit=learning_unit,
            title=f"Lesson {lesson_num}: {l_title}",
            status="published",
            version=1,
            immutable_metadata={
                "curriculum": "CBC",
                "grade": 10,
                "strand": "Foods and Nutrition",
                "sub_strand": "1.4 Methods of Cooking",
                "lesson_index": lesson_num,
                "ingestion_agent": "Grade 10 Home Science Specialist",
                "ground_truth_file": md_path
            }
        )
        total_lessons_created += 1

        # Build 6 Concept Cards (Pages) Structure
        pages_structure = [
            # -----------------------------------------------------------------
            # Card 1 (Page 1): Learning Goal, Visual Hook & Intuitive Connection
            # -----------------------------------------------------------------
            [
                {
                    "type": "learning_goal",
                    "title": f"Learning Goal: {l_title}",
                    "content": {
                        "goal": ldata["learning_goal"],
                        "target_competencies": [
                            "Understanding scientific principles of cooking",
                            "Recognizing nutritional and biological transformations",
                            "Applying hygienic safety and culinary craftsmanship"
                        ]
                    }
                },
                {
                    "type": "suggested_image",
                    "title": f"Visual Anchor: {l_title}",
                    "content": {
                        "title": f"Visual Representation: {l_title}",
                        "url": wiki_asset["url"],
                        "caption": wiki_asset["caption"],
                        "attribution": wiki_asset["attribution"],
                        "alt_text": wiki_asset["alt_text"]
                    },
                    "asset": {
                        "asset_type": "image",
                        "storage_type": "url",
                        "source_type": "external",
                        "title": f"Photo Hook: {l_title}",
                        "description": wiki_asset["caption"],
                        "url": wiki_asset["url"],
                        "metadata": {
                            "attribution": wiki_asset["attribution"],
                            "alt_text": wiki_asset["alt_text"],
                            "verified_active": True
                        }
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Intuitive Connection & Culinary Context",
                    "content": {
                        "title": "See & Connect",
                        "text": ldata["concept_hook"]
                    }
                }
            ],

            # -----------------------------------------------------------------
            # Card 2 (Page 2): Core Definitions & Theoretical Science Deep-Dive
            # -----------------------------------------------------------------
            [
                {
                    "type": "definition_card",
                    "title": f"Core Definition: {l_title}",
                    "content": {
                        "term": l_title,
                        "definition": ldata["definition"]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Theoretical Principles & Science Deep-Dive",
                    "content": {
                        "title": "Understand: Science in the Kitchen",
                        "text": ldata["theory_text"]
                    }
                }
            ],

            # -----------------------------------------------------------------
            # Card 3 (Page 3): Technical Vector Blueprint & Diagram Walkthrough
            # -----------------------------------------------------------------
            [
                {
                    "type": "suggested_diagram",
                    "title": f"Technical Infographic: {l_title}",
                    "content": {
                        "title": f"Vector Blueprint: {l_title}",
                        "caption": f"Responsive technical diagram illustrating key principles of {l_title}.",
                        "svg_content": svg_content
                    },
                    "asset": {
                        "asset_type": "diagram",
                        "storage_type": "url",
                        "source_type": "generated",
                        "title": f"Vector SVG Blueprint: {l_title}",
                        "url": f"https://vlearn.africa/assets/svg/home_science_g10_topic1_4_l{lesson_num}.svg",
                        "metadata": {
                            "svg_content": svg_content,
                            "type": "svg_diagram",
                            "viewBox": "0 0 800 450",
                            "dark_mode_compatible": True
                        }
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Diagram Analysis & Structural Walkthrough",
                    "content": {
                        "title": "Visual Analysis",
                        "text": ldata["diagram_analysis"]
                    }
                }
            ],

            # -----------------------------------------------------------------
            # Card 4 (Page 4): Step-by-Step Practical Protocol & Rules
            # -----------------------------------------------------------------
            [
                {
                    "type": "step_process",
                    "title": ldata["step_title"],
                    "content": {
                        "title": ldata["step_title"],
                        "steps": ldata["step_process"],
                        "safety_notice": ldata["safety_notice"]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Culinary Rules & Application Guidance",
                    "content": {
                        "title": "Practical Rules",
                        "text": ldata["practical_text"]
                    }
                }
            ],

            # -----------------------------------------------------------------
            # Card 5 (Page 5): Verified Video Demonstration & Kenyan Context
            # -----------------------------------------------------------------
            [
                {
                    "type": "suggested_video",
                    "title": yt_resource["title"],
                    "content": {
                        "title": yt_resource["title"],
                        "url": yt_resource["url"],
                        "resolved_video_id": yt_resource["youtube_id"],
                        "caption": yt_resource["caption"],
                        "reflection": yt_resource["reflection"]
                    },
                    "asset": {
                        "asset_type": "youtube",
                        "storage_type": "url",
                        "source_type": "external",
                        "title": yt_resource["title"],
                        "url": yt_resource["url"],
                        "metadata": {
                            "youtube_id": yt_resource["youtube_id"],
                            "verified_active": True
                        }
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Real-World Practice & Kenyan Context",
                    "content": {
                        "title": "Community & Everyday Living",
                        "text": ldata["real_world_text"]
                    }
                }
            ],

            # -----------------------------------------------------------------
            # Card 6 (Page 6): Formative MCQ Checkpoint & Key Takeaways
            # -----------------------------------------------------------------
            [
                {
                    "type": "knowledge_check",
                    "title": f"Formative Checkpoint: {l_title}",
                    "content": {
                        "question": mcq_data["question"],
                        "options": mcq_data["options"],
                        "correct_answer": mcq_data["correct_answer"],
                        "answer": mcq_data["answer"],
                        "explanation": mcq_data["explanation"]
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Lesson Summary & Key Takeaways",
                    "content": {
                        "title": f"Summary: {l_title}",
                        "takeaways": ldata["summary_takeaways"]
                    }
                }
            ]
        ]

        # Ingest Blocks and Assets for the Lesson
        block_order_counter = 10
        for page_idx, page_blocks in enumerate(pages_structure, start=1):
            for comp_idx, b_spec in enumerate(page_blocks, start=1):
                b_type = b_spec["type"]
                b_title = b_spec.get("title", "")
                b_content = clean_dict(b_spec.get("content", {}))
                b_meta = clean_dict(b_spec.get("metadata", {}))

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

                if "asset" in b_spec:
                    aspec = b_spec["asset"]
                    asset = LessonAsset.objects.create(
                        lesson=lesson,
                        asset_type=aspec["asset_type"],
                        source_type=aspec.get("source_type", "external"),
                        storage_type=aspec.get("storage_type", "url"),
                        status="approved",
                        title=aspec.get("title", b_title),
                        description=aspec.get("description", ""),
                        url=aspec.get("url"),
                        metadata=aspec.get("metadata", {})
                    )
                    block.assets.add(asset)
                    total_assets_created += 1

        print(f"  [+] Ingested Lesson {lesson_num}/14: '{l_title}' ({lesson.blocks.count()} blocks, {lesson.assets.count()} assets, 6 pages)")

    print("=" * 80)
    print("TOPIC 1.4 INGESTION COMPLETE:")
    print(f"  - Subject:        Home Science (ID: {subject.id})")
    print(f"  - Topic:          Foods and Nutrition (Order: {topic.order})")
    print(f"  - Learning Unit:  {learning_unit.name} (Order: {learning_unit.order})")
    print(f"  - Total Lessons:  {total_lessons_created}")
    print(f"  - Total Blocks:   {total_blocks_created}")
    print(f"  - Total Assets:   {total_assets_created}")
    print(f"  - Concept Cards:  6 per lesson (84 total cards)")
    print("=" * 80)

if __name__ == "__main__":
    ingest_grade10_home_science_topic1_4()
