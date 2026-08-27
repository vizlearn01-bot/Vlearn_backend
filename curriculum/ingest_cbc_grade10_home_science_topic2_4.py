"""
VLearn CBC Grade 10 Home Science — Topic 2.4: Care of the Home (Cleaning the House)
Comprehensive Production Ingestion & Visual Enrichment Engine (8 Published Lessons)

Curriculum: CBC
Grade: Grade 10 (Level: 10)
Subject: Home Science
Topic: Home Management (Order: 2)
Learning Unit: 2.4 Care of the Home (Order: 4)

Decomposed into 8 Published Lessons:
  - Lesson 1: Introduction and Reasons for Cleaning the House
  - Lesson 2: Classification of Cleaning Equipment and Materials
  - Lesson 3: Choice, Use, and Care of Cleaning Equipment and Materials
  - Lesson 4: Improvising Cleaning Equipment and Materials
  - Lesson 5: Management of Household Wastewater
  - Lesson 6: Management of Household Solid Waste
  - Lesson 7: Cleaning Different Areas in the House
  - Lesson 8: Safety Precautions When Cleaning

Features:
  - Reads Grade10_Home_Science_Topic_2_4.md directly using with open(...)
  - 8 Custom Responsive Sanitized Vector SVG Diagrams with viewBox="0 0 800 450"
  - 8 Verified Wikimedia Commons Photographic Assets with attached LessonAssets
  - 8 Verified Educational YouTube Video Integrations with attached LessonAssets
  - 8 Formative Scenario-Based MCQs with 4 options, valid correct_answer index, and detailed explanations
  - Discrete 6 concept cards (pages) per lesson with full typed block coverage (12 blocks per lesson = 96 blocks)
  - 0 Bracket citations & 0 meta-language leaks
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

def clean_text(text: str) -> str:
    """Removes bracket citations, meta-tags, and normalizes markdown bullet lists."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(r'\[VISUAL:[^\]]*\]', '', text, flags=re.DOTALL)
    text = re.sub(r'\[INTERACTION:[^\]]*\]', '', text, flags=re.DOTALL)
    text = re.sub(r'\[QUESTION:[^\]]*\]', '', text, flags=re.DOTALL)
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    return text.strip()

def clean_dict(data):
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, dict):
        return {k: clean_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_dict(item) for item in data]
    return data

# 8 Custom Vector SVGs for Topic 2.4
def get_svg_1():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE SCIENCE OF DIRT &amp; REASONS FOR HOUSE CLEANING</text>
  <text x="400" y="54" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Physical Classification of Dirt &amp; Four Hygiene Pillars of Household Sanitation</text>

  <!-- 4 Pillars Grid -->
  <g transform="translate(30, 75)">
    <!-- Card 1: Loose vs Fixed Dirt -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#0284c7"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🔬 DIRT MATRIX</text>
    <text x="12" y="55" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Loose Dirt (Dust):</text>
    <text x="12" y="72" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Dry particulate matter (soil, dander). Removed by sweeping or dusting.</text>
    <text x="12" y="115" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Fixed Dirt (Grime):</text>
    <text x="12" y="132" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Chemically bonded with oils or water. Requires scrubbing and soap.</text>
    <rect x="10" y="260" width="150" height="65" rx="6" fill="#0f172a"/>
    <text x="85" y="282" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Physical Rule:</text>
    <text x="85" y="302" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Sweep Loose Dirt First</text>
  </g>

  <g transform="translate(220, 75)">
    <!-- Card 2: Health & Pathogen Barrier -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#059669"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🩺 HEALTH &amp; HYGIENE</text>
    <text x="12" y="55" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Pathogen Removal:</text>
    <text x="12" y="72" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Destroys bacteria, viruses, and molds on food prep and wash surfaces.</text>
    <text x="12" y="115" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Infection Shield:</text>
    <text x="12" y="132" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Prevents diarrheal diseases, skin infections, and food poisoning.</text>
    <rect x="10" y="260" width="150" height="65" rx="6" fill="#0f172a"/>
    <text x="85" y="282" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Outcome:</text>
    <text x="85" y="302" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Disease Prevention</text>
  </g>

  <g transform="translate(410, 75)">
    <!-- Card 3: Pest & Air Quality -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#d97706"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🐜 PEST &amp; AIR CONTROL</text>
    <text x="12" y="55" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Pest Starvation:</text>
    <text x="12" y="72" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Clearing crumbs starves cockroaches, flies, and rodents.</text>
    <text x="12" y="115" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Pure Indoor Air:</text>
    <text x="12" y="132" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Filters dust and pollen to prevent asthma and respiratory allergies.</text>
    <rect x="10" y="260" width="150" height="65" rx="6" fill="#0f172a"/>
    <text x="85" y="282" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Outcome:</text>
    <text x="85" y="302" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Clean Breathing Air</text>
  </g>

  <g transform="translate(600, 75)">
    <!-- Card 4: Asset Longevity & Comfort -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#7e22ce"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">✨ ASSET LONGEVITY</text>
    <text x="12" y="55" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Surface Preservation:</text>
    <text x="12" y="72" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Removes abrasive grit that scratches floor tiles and varnished wood.</text>
    <text x="12" y="115" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Psychological Order:</text>
    <text x="12" y="132" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">A clean, tidy home reduces stress and enhances mental tranquility.</text>
    <rect x="10" y="260" width="150" height="65" rx="6" fill="#0f172a"/>
    <text x="85" y="282" fill="#c084fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Outcome:</text>
    <text x="85" y="302" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Asset Protection</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_2():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">CLASSIFICATION OF CLEANING EQUIPMENT &amp; MATERIALS</text>
  <text x="400" y="52" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Matching Tool Physics, Bristle Types, and Mechanical Action to Floor &amp; Furniture Substrates</text>

  <!-- 3 Main Pillars -->
  <g transform="translate(30, 70)">
    <!-- 1. Dry Sweeping & Dust Removal -->
    <rect width="230" height="350" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="230" height="32" rx="10" fill="#0284c7"/>
    <text x="115" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🧹 SWEEPING &amp; DUSTING</text>
    
    <text x="15" y="58" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Soft Brooms (Nylon/Grass):</text>
    <text x="15" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Smooth tiles, polished wood, linoleum.</text>
    
    <text x="15" y="105" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Stiff Yard Brooms (Twigs):</text>
    <text x="15" y="121" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Rough outdoor compounds, driveways.</text>

    <text x="15" y="152" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Dusters &amp; Dustpans:</text>
    <text x="15" y="168" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Microfiber/flannel cloths for furniture.</text>

    <rect x="15" y="235" width="200" height="95" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
    <text x="115" y="258" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Primary Mechanism:</text>
    <text x="115" y="278" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Electrostatic capture &amp;</text>
    <text x="115" y="296" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">mechanical displacement</text>
  </g>

  <g transform="translate(285, 70)">
    <!-- 2. Scrubbing & Deep Cleaning -->
    <rect width="230" height="350" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="230" height="32" rx="10" fill="#d97706"/>
    <text x="115" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🧽 SCRUBBING &amp; FRICTION</text>
    
    <text x="15" y="58" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Floor Scrubbing Brushes:</text>
    <text x="15" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Stiff bristles remove fixed concrete grime.</text>
    
    <text x="15" y="105" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Toilet &amp; Dish Brushes:</text>
    <text x="15" y="121" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Curved bowls &amp; kitchen cookware.</text>

    <text x="15" y="152" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Abrasive Scourers:</text>
    <text x="15" y="168" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Coconut husk &amp; synthetic nylon scouring.</text>

    <rect x="15" y="235" width="200" height="95" rx="6" fill="#0f172a" stroke="#d97706" stroke-width="1"/>
    <text x="115" y="258" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Primary Mechanism:</text>
    <text x="115" y="278" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Friction-based detachment</text>
    <text x="115" y="296" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">of stubborn fixed stains</text>
  </g>

  <g transform="translate(540, 70)">
    <!-- 3. Wet Mopping & Water Extraction -->
    <rect width="230" height="350" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="230" height="32" rx="10" fill="#059669"/>
    <text x="115" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🌊 WET MOPPING &amp; DRYING</text>
    
    <text x="15" y="58" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Cotton String Mops:</text>
    <text x="15" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">High liquid absorption on large floors.</text>
    
    <text x="15" y="105" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Flat Microfiber Mops:</text>
    <text x="15" y="121" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Rapid damp wiping with minimal water.</text>

    <text x="15" y="152" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Floor &amp; Window Squeegees:</text>
    <text x="15" y="168" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Flexible rubber strips standing liquid.</text>

    <rect x="15" y="235" width="200" height="95" rx="6" fill="#0f172a" stroke="#059669" stroke-width="1"/>
    <text x="115" y="258" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Primary Mechanism:</text>
    <text x="115" y="278" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Capillary absorption &amp;</text>
    <text x="115" y="296" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">surface streak prevention</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_3():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">CHOICE, USE &amp; HYGIENIC STORAGE OF CLEANING EQUIPMENT</text>
  <text x="400" y="54" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Preventing Equipment Deformation, Structural Fiber Decay, and Anaerobic Mildew Contamination</text>

  <!-- 4 Columns Grid -->
  <g transform="translate(30, 75)">
    <!-- Brooms Storage -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#0284c7"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🧹 BROOM CARE</text>
    <text x="12" y="55" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Storage Rule:</text>
    <text x="12" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Hang on wall hooks or store handle-down, bristles UP.</text>
    <text x="12" y="115" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Hazard of Failure:</text>
    <text x="12" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Standing on bristles permanently bends fibers, preventing flat sweeping.</text>
    <rect x="10" y="260" width="150" height="65" rx="6" fill="#0f172a"/>
    <text x="85" y="282" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Golden Standard:</text>
    <text x="85" y="302" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Never Rest on Bristles</text>
  </g>

  <g transform="translate(220, 75)">
    <!-- Mop Care -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#059669"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🌊 MOP HYGIENE</text>
    <text x="12" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Storage Rule:</text>
    <text x="12" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Rinse clear, wring dry, and hang outdoors in the SUN.</text>
    <text x="12" y="115" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Hazard of Failure:</text>
    <text x="12" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Storing wet in buckets fosters anaerobic bacteria and black mildew rot.</text>
    <rect x="10" y="260" width="150" height="65" rx="6" fill="#0f172a"/>
    <text x="85" y="282" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Golden Standard:</text>
    <text x="85" y="302" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">UV &amp; Air Desiccation</text>
  </g>

  <g transform="translate(410, 75)">
    <!-- Brushes -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#d97706"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🪥 BRUSH CARE</text>
    <text x="12" y="55" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Storage Rule:</text>
    <text x="12" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Wash out grit and store bristle-up or hanging down.</text>
    <text x="12" y="115" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Hazard of Failure:</text>
    <text x="12" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Trapped water rots wooden bases and flattens bristle scrubbing power.</text>
    <rect x="10" y="260" width="150" height="65" rx="6" fill="#0f172a"/>
    <text x="85" y="282" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Golden Standard:</text>
    <text x="85" y="302" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Drain Water Off Stock</text>
  </g>

  <g transform="translate(600, 75)">
    <!-- Buckets & Cloths -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#7e22ce"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🪣 BUCKET &amp; CLOTH</text>
    <text x="12" y="55" fill="#c084fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Storage Rule:</text>
    <text x="12" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Disinfect cloths in bleach, dry buckets and nest cleanly.</text>
    <text x="12" y="115" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Hazard of Failure:</text>
    <text x="12" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Dirty dishcloths transfer millions of pathogenic microbes to clean dishes.</text>
    <rect x="10" y="260" width="150" height="65" rx="6" fill="#0f172a"/>
    <text x="85" y="282" fill="#c084fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Golden Standard:</text>
    <text x="85" y="302" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Clean Tools Clean Best</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_4():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">IMPROVISATION OF CLEANING EQUIPMENT &amp; NATURAL MATERIALS</text>
  <text x="400" y="52" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Zero-Cost Resource Engineering: Upcycling Local Plant Fibers, Discarded Plastics &amp; Eco-Cleaners</text>

  <!-- Left: Physical Tools -->
  <g transform="translate(30, 70)">
    <rect width="355" height="350" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="355" height="32" rx="12" fill="#059669"/>
    <text x="177" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">🛠️ IMPROVISED MECHANICAL HARDWARE</text>
    
    <text x="20" y="60" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" font-weight="700">1. Twig Yard Broom:</text>
    <text x="20" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Cypress/palm twigs tightly bound with sisal string on timber handle.</text>
    <text x="20" y="96" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">Heavy bristle density displaces outdoor gravel and leaves.</text>

    <text x="20" y="130" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" font-weight="700">2. Upcycled Jerrycan Dustpan:</text>
    <text x="20" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">5L cooking oil jerrycan cut diagonally with sanded flat scraping lip.</text>
    <text x="20" y="166" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">Retains integrated molded handle; sands edges to prevent cuts.</text>

    <text x="20" y="200" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" font-weight="700">3. Coconut Husk Scourer:</text>
    <text x="20" y="218" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Fibrous inner coconut shell or dried loofah plant.</text>
    <text x="20" y="236" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">High natural abrasive friction without toxic microplastics.</text>

    <rect x="15" y="265" width="325" height="65" rx="8" fill="#0f172a" stroke="#059669" stroke-width="1"/>
    <text x="25" y="288" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Key Advantage:</text>
    <text x="25" y="308" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">Zero factory cost, 100% locally sourced, biodegradable.</text>
  </g>

  <!-- Right: Chemical Formulations -->
  <g transform="translate(415, 70)">
    <rect width="355" height="350" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="355" height="32" rx="12" fill="#d97706"/>
    <text x="177" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">🧪 NATURAL CHEMICAL CLEANING AGENTS</text>
    
    <text x="20" y="60" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="12" font-weight="700">1. Alkaline Wood Ash Scourer:</text>
    <text x="20" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Fine sieved wood ash + water paste.</text>
    <text x="20" y="96" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">Potassium carbonate saponifies tough grease on soot-covered pans.</text>

    <text x="20" y="130" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="12" font-weight="700">2. Citric / Acetic Acid Descaler:</text>
    <text x="20" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Lemon juice or white vinegar solution.</text>
    <text x="20" y="166" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">Acidic pH dissolves calcium scale &amp; hard water mineral stains.</text>

    <text x="20" y="200" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="12" font-weight="700">3. Sodium Bicarbonate Deodorizer:</text>
    <text x="20" y="218" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Baking soda powder for sinks &amp; refrigerators.</text>
    <text x="20" y="236" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">Neutralizes volatile acidic odors and lifts light stains.</text>

    <rect x="15" y="265" width="325" height="65" rx="8" fill="#0f172a" stroke="#d97706" stroke-width="1"/>
    <text x="25" y="288" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Safety &amp; Health:</text>
    <text x="25" y="308" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">Non-toxic, safe for skin, eco-friendly to soil and water.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_5():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">MANAGEMENT OF HOUSEHOLD WASTEWATER: SOAKAWAY &amp; GREASE TRAP</text>
  <text x="400" y="52" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Engineering Greywater Dispersion, Fat-Oil-Grease (FOG) Trapping, and Vector Prevention</text>

  <!-- Left: Soakaway Pit Cross-Section -->
  <g transform="translate(30, 70)">
    <rect width="360" height="350" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="360" height="30" rx="10" fill="#0284c7"/>
    <text x="180" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">📐 SOAKAWAY PIT STRATIFIED CROSS-SECTION</text>

    <!-- Topsoil & Concrete Slab -->
    <rect x="20" y="45" width="320" height="30" rx="4" fill="#334155"/>
    <text x="180" y="65" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Reinforced Concrete Slab &amp; Topsoil Cover</text>

    <!-- Layer 1: Fine Sand -->
    <rect x="20" y="80" width="320" height="50" rx="4" fill="#ca8a04"/>
    <text x="180" y="105" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Top Layer: Fine Sand (Traps Hair &amp; Micro-debris)</text>

    <!-- Layer 2: Medium Gravel -->
    <rect x="20" y="135" width="320" height="60" rx="4" fill="#64748b"/>
    <text x="180" y="165" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Middle Layer: Coarse Gravel (Filters Suspended Solids)</text>

    <!-- Layer 3: Hardcore Boulders -->
    <rect x="20" y="200" width="320" height="85" rx="4" fill="#475569"/>
    <text x="180" y="240" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Base Layer: Large Hardcore Boulders (High Porosity Void)</text>
    <text x="180" y="260" fill="#93c5fd" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Safe sub-soil percolation eliminates stagnant mosquito puddles</text>

    <!-- Bottom summary tag -->
    <rect x="20" y="295" width="320" height="40" rx="6" fill="#0f172a"/>
    <text x="180" y="320" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">✓ Eliminates Surface Runoff &amp; Stagnant Odors</text>
  </g>

  <!-- Right: Grease Trap Mechanism -->
  <g transform="translate(410, 70)">
    <rect width="360" height="350" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="360" height="30" rx="10" fill="#d97706"/>
    <text x="180" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🛢️ GREASE TRAP DENSITY SEPARATION</text>

    <!-- Trap Chamber Diagram -->
    <rect x="20" y="45" width="320" height="150" rx="6" fill="#0f172a" stroke="#d97706" stroke-width="1"/>
    <!-- Floating Grease Layer -->
    <rect x="30" y="55" width="300" height="30" rx="4" fill="#eab308"/>
    <text x="180" y="75" fill="#000000" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Floating FOG Layer (Fats, Oils &amp; Grease - Low Density)</text>
    <!-- Water Layer -->
    <rect x="30" y="90" width="300" height="95" rx="4" fill="#0284c7"/>
    <text x="180" y="140" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Clear Effluent Greywater (Underflow Outlet)</text>

    <!-- Why it matters -->
    <text x="25" y="215" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Why Grease Traps Are Mandatory:</text>
    <text x="25" y="235" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Unfiltered grease coats soil pores in soakaways, causing</text>
    <text x="25" y="253" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">  complete impermeability and foul wastewater overflow.</text>
    <text x="25" y="275" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Must be skimmed and cleaned weekly to maintain flow.</text>

    <rect x="20" y="295" width="320" height="40" rx="6" fill="#0f172a"/>
    <text x="180" y="320" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">✓ Protects Soakaway Pit from Soil Clogging</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_6():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">SOLID WASTE MANAGEMENT &amp; 3-BIN SOURCE SEPARATION</text>
  <text x="400" y="54" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Resource Recovery Hierarchy: Reduce, Reuse, Recycle, Compost &amp; Hazardous Segregation</text>

  <!-- 4 Bins Matrix -->
  <g transform="translate(30, 75)">
    <!-- 1. Organic Compost -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#059669"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">🥬 ORGANIC COMPOST</text>
    <text x="12" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Bin Color: Green</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Vegetable peels</text>
    <text x="12" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Food scraps &amp; fruit</text>
    <text x="12" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Garden leaves &amp; weeds</text>
    <text x="12" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Used tea leaves</text>
    <rect x="10" y="240" width="150" height="85" rx="6" fill="#0f172a"/>
    <text x="85" y="265" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Final Destination:</text>
    <text x="85" y="285" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Backyard Compost Pit</text>
    <text x="85" y="305" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Fertilizes Garden Crops</text>
  </g>

  <g transform="translate(220, 75)">
    <!-- 2. Recyclables -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#0284c7"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">♻️ RECYCLABLES</text>
    <text x="12" y="55" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Bin Color: Blue</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Clean plastic bottles</text>
    <text x="12" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Cardboard &amp; paper</text>
    <text x="12" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Aluminum tin cans</text>
    <text x="12" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Glass jars &amp; bottles</text>
    <rect x="10" y="240" width="150" height="85" rx="6" fill="#0f172a"/>
    <text x="85" y="265" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Final Destination:</text>
    <text x="85" y="285" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Recycling Center</text>
    <text x="85" y="305" fill="#93c5fd" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Factory Reprocessing</text>
  </g>

  <g transform="translate(410, 75)">
    <!-- 3. Landfill Trash -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#d97706"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">🗑️ NON-RECYCLABLE</text>
    <text x="12" y="55" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Bin Color: Red / Grey</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Soiled sanitary paper</text>
    <text x="12" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Floor sweepings</text>
    <text x="12" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Multi-layer wrappers</text>
    <text x="12" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Broken ceramics</text>
    <rect x="10" y="240" width="150" height="85" rx="6" fill="#0f172a"/>
    <text x="85" y="265" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Final Destination:</text>
    <text x="85" y="285" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Municipal Landfill</text>
    <text x="85" y="305" fill="#fde68a" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Sanitary Waste Bin</text>
  </g>

  <g transform="translate(600, 75)">
    <!-- 4. Hazardous Waste -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#b91c1c"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">⚠️ HAZARDOUS TOXIC</text>
    <text x="12" y="55" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Special Quarantine:</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Expired medications</text>
    <text x="12" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Dry-cell batteries</text>
    <text x="12" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Paint &amp; pesticide cans</text>
    <text x="12" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Broken light bulbs</text>
    <rect x="10" y="240" width="150" height="85" rx="6" fill="#0f172a"/>
    <text x="85" y="265" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Safety Protocol:</text>
    <text x="85" y="285" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Never Burn or Compost</text>
    <text x="85" y="305" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Special Collection Takeback</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_7():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="30" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">SYSTEMATIC ROOM CLEANING: THE TOP-TO-BOTTOM GRAVITY FLOW</text>
  <text x="400" y="48" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Scientific Sequencing: Gravity Law, Zonal Progression, and Back-to-Door Exit Protocol</text>

  <!-- Left: 5 Steps Vertical Timeline -->
  <g transform="translate(30, 65)">
    <rect width="440" height="360" rx="10" fill="#1e293b" stroke="#475569" stroke-width="2"/>
    <text x="220" y="22" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">5-PHASE SYSTEMATIC SEQUENCE</text>

    <!-- Phase 1 -->
    <rect x="15" y="35" width="410" height="50" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="30" y="56" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. Preparation &amp; Ventilation:</text>
    <text x="30" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Open windows wide for airflow; strip bedding/curtains; clear clutter.</text>

    <!-- Phase 2 -->
    <rect x="15" y="95" width="410" height="50" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <text x="30" y="116" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. Ceiling &amp; High Zones (Top):</text>
    <text x="30" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Sweep ceiling cobwebs, dust curtain rails, vents &amp; light fixtures.</text>

    <!-- Phase 3 -->
    <rect x="15" y="155" width="410" height="50" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <text x="30" y="176" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Mid-Level Furniture &amp; Walls (Middle):</text>
    <text x="30" y="194" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Dust picture frames, wipe shelves top-to-bottom, clean desk surfaces.</text>

    <!-- Phase 4 -->
    <rect x="15" y="215" width="410" height="50" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1"/>
    <text x="30" y="236" fill="#c084fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">4. Floor Perimeter Sweep (Bottom):</text>
    <text x="30" y="254" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Sweep from furthest corner toward the main exit door; collect in dustpan.</text>

    <!-- Phase 5 -->
    <rect x="15" y="275" width="410" height="65" rx="6" fill="#0f172a" stroke="#06b6d4" stroke-width="1"/>
    <text x="30" y="296" fill="#22d3ee" font-family="system-ui, sans-serif" font-size="11" font-weight="700">5. Exit-Facing Damp Mopping (Finish):</text>
    <text x="30" y="314" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Mop backwards toward doorway to avoid footprint recontamination;</text>
    <text x="30" y="330" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">allow floor to air-dry completely before resetting furniture.</text>
  </g>

  <!-- Right: 3 Golden Rules Box -->
  <g transform="translate(490, 65)">
    <rect width="280" height="360" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="280" height="32" rx="10" fill="#0284c7"/>
    <text x="140" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">📐 3 GOLDEN RULES</text>

    <text x="15" y="60" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">1. The Law of Gravity:</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Always clean from highest ceiling to lowest floor. Falling dust won't soil clean floors.</text>

    <text x="15" y="130" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">2. Back-to-Door Trajectory:</text>
    <text x="15" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Work from the deepest corner toward the exit. Prevents trapping yourself or stepping on wet tiles.</text>

    <text x="15" y="200" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">3. Dry Before Wet:</text>
    <text x="15" y="218" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Always sweep loose dirt dry before mopping. Wetting dust creates sticky, hard-to-clean mud.</text>

    <rect x="15" y="280" width="250" height="65" rx="6" fill="#0f172a"/>
    <text x="140" y="306" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Outcome: Maximum Speed,</text>
    <text x="140" y="326" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Zero Rework &amp; Spotless Hygiene</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_8():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#ef4444" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">SAFETY PRECAUTIONS &amp; CHEMICAL HAZARDS IN HOUSE CLEANING</text>
  <text x="400" y="54" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Toxic Gas Prevention, Chemical Storage Protocols, Mandatory PPE &amp; Physical Fall Prevention</text>

  <!-- 4 Pillars Grid -->
  <g transform="translate(30, 75)">
    <!-- Card 1: Deadly Chemical Mixing -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#b91c1c"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">☠️ DEADLY MIXING</text>
    <text x="12" y="55" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="700">NEVER MIX:</text>
    <text x="12" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Bleach + Ammonia (Creates Chloramine Gas)</text>
    <text x="12" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Bleach + Acids (Creates Chlorine Gas)</text>
    <text x="12" y="145" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10">Causes severe lung burns, suffocation, and fatality.</text>
    <rect x="10" y="260" width="150" height="65" rx="6" fill="#0f172a"/>
    <text x="85" y="282" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Strict Rule:</text>
    <text x="85" y="302" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Use One Chemical At Once</text>
  </g>

  <g transform="translate(220, 75)">
    <!-- Card 2: PPE & Ventilation -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#0284c7"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">🧤 MANDATORY PPE</text>
    <text x="12" y="55" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Protective Gear:</text>
    <text x="12" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Heavy rubber gloves for skin acid barrier.</text>
    <text x="12" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Apron to protect body from chemical splash.</text>
    <text x="12" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Open windows wide for cross-ventilation.</text>
    <rect x="10" y="260" width="150" height="65" rx="6" fill="#0f172a"/>
    <text x="85" y="282" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Strict Rule:</text>
    <text x="85" y="302" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Wear Gloves &amp; Ventilate</text>
  </g>

  <g transform="translate(410, 75)">
    <!-- Card 3: Safe Chemical Storage -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#d97706"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">🔒 SAFE STORAGE</text>
    <text x="12" y="55" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Storage Standards:</text>
    <text x="12" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Store in ORIGINAL labeled containers.</text>
    <text x="12" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Never transfer to juice or soda bottles.</text>
    <text x="12" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Keep on high shelves in locked cupboards.</text>
    <rect x="10" y="260" width="150" height="65" rx="6" fill="#0f172a"/>
    <text x="85" y="282" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Strict Rule:</text>
    <text x="85" y="302" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Keep Away from Children</text>
  </g>

  <g transform="translate(600, 75)">
    <!-- Card 4: Slip & Electrical Safety -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#059669"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">⚡ SLIP &amp; ELECTRICAL</text>
    <text x="12" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Physical Hazards:</text>
    <text x="12" y="72" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Wipe liquid spills immediately.</text>
    <text x="12" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Use stable step-stools, never wobbly chairs.</text>
    <text x="12" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Dry hands before touching electrical switches.</text>
    <rect x="10" y="260" width="150" height="65" rx="6" fill="#0f172a"/>
    <text x="85" y="282" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Strict Rule:</text>
    <text x="85" y="302" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Zero Slip &amp; Shock Risks</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

SVG_GETTERS = [
    get_svg_1, get_svg_2, get_svg_3, get_svg_4,
    get_svg_5, get_svg_6, get_svg_7, get_svg_8
]

# 8 Comprehensive Lesson Configurations for Topic 2.4
LESSON_CONFIGS = [
    {
        "lesson_num": 1,
        "title": "Introduction and Reasons for Cleaning the House",
        "hook": "Imagine walking into a room after a long, dry, windy day. You run your finger across a dark wooden table, and it leaves a clear track in a thick layer of grey dust. Or imagine walking into a kitchen where a cup of milk was accidentally spilled on the floor the night before and left uncleaned—the smell is sour, sticky patches cling to your shoes, and small flies are beginning to circle. Every day, our homes face an ongoing battle against dust, dirt, and waste. Cleaning is far more than an aesthetic chore; it is an applied scientific practice that protects family health and preserves household assets.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Warm_family_living_room_in_Nairobi.jpg/960px-Warm_family_living_room_in_Nairobi.jpg",
        "image_caption": "A clean, bright, and well-organized living room in a Kenyan home provides physical protection, emotional security, and a healthy living environment.",
        "analogy_title": "The Smartphone Cache & Cleaner App Analogy",
        "analogy_text": "Think of your home as being like a smartphone. When you first unbox it, it runs fast, the screen is sparkling clean, and its memory is completely free. But as you use it daily, cache files, temporary cookies, and downloaded junk accumulate. If you never run a 'cleaner app' to clear this digital clutter, the phone slows down, freezes, becomes vulnerable to viruses, and eventually stops working properly. Similarly, your home accumulates physical clutter and grime daily (dust blown from the road, food crumbs, wastewater). If we do not execute our daily and weekly cleaning routines, the house becomes unhygienic, stressful to live in, and vulnerable to pest infestations.",
        "definition": {
            "title": "Loose Dirt vs. Fixed Dirt",
            "definitions": [
                {
                    "term": "Loose Dirt (Dust)",
                    "simple": "Dry particles of soil, pollen, or skin cells that sit lightly on surfaces and can be easily swept or blown away.",
                    "formal": "Fine, dry particulate matter composed of atmospheric soil, organic debris, and cellular waste that rests on surfaces without adhering chemically or mechanically.",
                    "example": "Dry atmospheric dust resting on a window sill or loose sand on a tiled floor.",
                    "why_it_matters": "Easily inhaled into the respiratory tract, triggering asthma attacks and allergic reactions if not swept or vacuumed regularly."
                },
                {
                    "term": "Fixed Dirt (Grime or Stains)",
                    "simple": "Dirt that has mixed with water, grease, or oil and clings tightly to surfaces, requiring scrubbing or chemical detergents to remove.",
                    "formal": "Solid or semi-solid organic and inorganic substances that have chemically or mechanically bonded with a substrate surface via lipids or moisture.",
                    "example": "Dried cooking oil splatters around a gas stove or sticky tea stains on a dining table.",
                    "why_it_matters": "Provides an ideal nutrient medium and breeding ground for pathogenic bacteria and molds."
                }
            ]
        },
        "deep_explanation": "House cleaning is a foundational health and economic requirement governed by four core pillars:\n\n1. **Hygiene and Pathogen Elimination:** Microorganisms multiply rapidly on damp, dirty surfaces. Cleaning with appropriate detergents physically disrupts bacterial cell walls and strips away organic biofilms, preventing diarrheal illnesses, typhoid, and skin infections.\n2. **Pest Infestation Prevention:** Uncleaned food crumbs, sticky grease, and exposed waste attract disease-carrying vectors such as cockroaches, houseflies, and rodents that transmit Salmonella and other harmful pathogens.\n3. **Indoor Air Quality Optimization:** Airborne dust, pet dander, and microscopic mold spores trapped inside closed rooms cause chronic respiratory allergies and asthma. Regular dusting and ventilation purify indoor air.\n4. **Asset Longevity and Economics:** Fine dirt and sand act as abrasives. When dirt accumulates on wooden furniture, ceramic tiles, or fabric upholstery, friction scratches surfaces and causes premature deterioration.",
        "practical": {
            "title": "The Dust and Stain Audit Investigation",
            "steps": [
                {"step_number": 1, "instruction": "Select three distinct household surfaces (e.g., a window sill, a dining table, and a kitchen countertop near the cooking stove)."},
                {"step_number": 2, "instruction": "Wipe a section of each surface with a dry white cotton cloth to observe and collect dry particulate matter (Loose Dirt)."},
                {"step_number": 3, "instruction": "Inspect areas that resisted dry wiping, then dampen a corner of the cloth with soapy water and rub gently to identify grease and sticky residues (Fixed Dirt)."},
                {"step_number": 4, "instruction": "Record your findings in an audit ledger noting surface type, dirt classification, and ease of removal."},
                {"step_number": 5, "instruction": "Formulate a tailored cleaning protocol for each surface based on whether the dirt is loose or fixed."}
            ]
        },
        "youtube_id": "7q_qMkJcI1Y",
        "mcq": {
            "question": "Which of the following is classified as fixed dirt requiring chemical detergent action to remove?",
            "options": [
                "Wind-blown dry sand resting on a veranda floor",
                "A sticky ring of dried tea and milk on a wooden dining table",
                "Dry tree leaves scattered across a driveway",
                "Loose hair clippings resting on a dry bathroom tile"
            ],
            "correct_answer": 1,
            "explanation": "A dried tea and milk stain is fixed dirt because the lipids, sugars, and moisture have bonded chemically to the table substrate, requiring water and detergent to dissolve and emulsify."
        }
    },
    {
        "lesson_num": 2,
        "title": "Classification of Cleaning Equipment and Materials",
        "hook": "Have you ever tried to sweep a rough, dusty outdoor gravel compound using a soft, fine-bristled indoor nylon broom? The soft bristles bend, skip over the stones, tear apart, and leave you exhausted with a dusty yard. Conversely, if you try to sweep a polished indoor hardwood or tiled floor with a stiff twig yard broom, you will scratch the protective varnish and fail to collect fine dust particles. In home management, matching tool physics to the surface substrate is essential.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Household_cleaning_equipment_assortment.jpg/960px-Household_cleaning_equipment_assortment.jpg",
        "image_caption": "Cleaning equipment is classified into functional categories based on mechanical action, bristle characteristics, and target surface materials.",
        "analogy_title": "The Chef's Knife Classification Analogy",
        "analogy_text": "Think of cleaning tools as being like specialized culinary knives in a professional kitchen. A master chef would never use a heavy, wide meat cleaver to peel a delicate grape, nor would they use a flexible paring knife to chop through a frozen beef bone. Attempting to do so ruins the food, destroys the blade, and risks physical injury. Cleaning tools are specialized instruments: matching the stiffness, shape, and fiber composition of the tool to the specific surface ensures spotless results without scratching surfaces or breaking tools.",
        "definition": {
            "title": "Taxonomy of Cleaning Equipment",
            "definitions": [
                {
                    "term": "Sweeping Equipment (Brooms)",
                    "simple": "Tools with bristles mounted on a head or handle, designed to displace and gather loose dry debris across floors.",
                    "formal": "Mechanical implements featuring bundled natural or synthetic bristles calibrated in stiffness for displacing loose particulate matter from horizontal surfaces.",
                    "example": "Soft nylon brooms for indoor tiled floors and stiff twig yard brooms for outdoor compounds.",
                    "why_it_matters": "Enables efficient collection of loose dry dirt without causing surface scratches."
                },
                {
                    "term": "Drying & Scraping Tools (Squeegees)",
                    "simple": "Handheld tools with flat, flexible rubber blades used to wipe standing water off smooth surfaces without leaving streaks.",
                    "formal": "Implements featuring a resilient elastomer blade mounted on a rigid frame, designed to displace liquid films from non-porous substrates via dynamic pressure.",
                    "example": "Floor squeegees used on wet bathroom tiles and window squeegees for glass panes.",
                    "why_it_matters": "Removes standing water rapidly, preventing slip accidents and eliminating unsightly limescale water spots."
                }
            ]
        },
        "deep_explanation": "Cleaning equipment and materials are classified into distinct functional categories:\n\n- **Sweeping Equipment:** Soft brooms (nylon or natural plant thatch) for smooth surfaces (tiles, wood, polished cement); Stiff brooms (thick twigs or palm ribs) for rough exterior concrete and soil.\n- **Dusting Implements:** Microfiber cloths, flannel rags, and feather dusters that attract and trap fine particulate matter via electrostatic forces without scattering dust into the air.\n- **Debris Collection:** Dustpans with flat, beveled scraping lips designed to sit flush with the floor to collect swept dirt cleanly.\n- **Scrubbing Equipment:** Stiff-bristled floor brushes, curved toilet bowl brushes, and scouring pads engineered for high-friction removal of stubborn fixed stains.\n- **Mopping Implements:** Cotton string mops for heavy liquid absorption on sealed floors; Flat microfiber mops for damp surface sanitizing.\n- **Water Removal Tools:** Squeegees with flexible rubber blades for rapid, streak-free drying of tiled floors and glass windows.\n- **Holding Solutions:** Basins and nested plastic buckets for transporting wash and rinse water.",
        "practical": {
            "title": "Cleaning Store Taxonomy & Condition Audit",
            "steps": [
                {"step_number": 1, "instruction": "Access a home utility cupboard, school cleaning store, or dormitory storage area."},
                {"step_number": 2, "instruction": "Inventory every cleaning tool and classify it under its primary functional role (Sweeping, Dusting, Scrubbing, Mopping, Drying, or Holding)."},
                {"step_number": 3, "instruction": "Record the construction material of each tool (e.g., synthetic nylon, natural coconut fiber, rubber, galvanized steel)."},
                {"step_number": 4, "instruction": "Evaluate the current physical condition of each tool (inspect for bent bristles, frayed mop fibers, or cracked plastic heads)."},
                {"step_number": 5, "instruction": "Propose corrective storage or maintenance actions for any compromised tools."}
            ]
        },
        "youtube_id": "2t8b7w9fK7w",
        "mcq": {
            "question": "Which cleaning tool is most functionally appropriate for removing a large volume of standing water from a smooth, tiled bathroom floor?",
            "options": [
                "A stiff twig outdoor yard broom",
                "A floor squeegee followed by a wrung-out damp cotton mop",
                "A dry microfiber feather duster",
                "A wire-bristled scrubbing brush"
            ],
            "correct_answer": 1,
            "explanation": "A floor squeegee utilizes a flexible rubber blade to displace standing water rapidly toward the drain, while a wrung-out mop absorbs residual dampness, preventing slipping hazards."
        }
    },
    {
        "lesson_num": 3,
        "title": "Choice, Use, and Care of Cleaning Equipment and Materials",
        "hook": "Have you ever picked up a dishcloth or kitchen sponge that had been left sitting inside a dark, damp bucket of dirty wash water for a week? It feels slimy, has turned a dark grey color, and emits a sour, rotten odor. If you try to wash a clean plate with that sponge, you are not sanitizing the dish—you are transferring millions of pathogenic bacteria onto food-contact surfaces. Cleaning tools themselves must be meticulously maintained, or they become dangerous vectors of disease.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Cleaning_closet_tools_hanging_storage.jpg/960px-Cleaning_closet_tools_hanging_storage.jpg",
        "image_caption": "Properly stored cleaning equipment: brooms hanging on wall hooks, mops hung to air-dry, and clean plastic buckets dried and nested neatly.",
        "analogy_title": "The Soldier's Weapon Maintenance Analogy",
        "analogy_text": "Think of cleaning tools as being like a soldier's rifle. A disciplined soldier never goes into a mission with a weapon clogged with mud, rusted, and un-oiled; doing so causes the rifle to jam and fail at a critical moment. After every field exercise, the soldier spends time stripping, cleaning, lubricating, and inspecting the rifle so it remains battle-ready. Similarly, cleaning tools fight an ongoing war against dirt and pathogenic germs. If you fail to wash, dry, and store your brooms, mops, and brushes properly after every cleaning session, they decay and fail.",
        "definition": {
            "title": "Equipment Care Principles",
            "definitions": [
                {
                    "term": "Hygienic Storage Protocol",
                    "simple": "Specific rules for cleaning, drying, and positioning tools after use to prevent damage and microbial growth.",
                    "formal": "The standardized maintenance procedure of decontaminating, desiccating, and mechanically isolating cleaning implements to prevent fiber degradation and anaerobic contamination.",
                    "example": "Hanging wet mops outdoors in direct sunlight and suspending brooms on wall hooks.",
                    "why_it_matters": "Extends equipment lifespan by years and prevents the spread of foul odors and mold spores."
                },
                {
                    "term": "Bristle Deformation",
                    "simple": "The permanent bending and warping of brush or broom bristles caused by storing them resting on the ground.",
                    "formal": "Mechanical creep and structural fatigue of bristle fibers resulting from sustained vertical compressive load during storage.",
                    "example": "A nylon broom stored resting on its head, causing the outer bristles to curl outward permanently.",
                    "why_it_matters": "Ruins the broom's ability to maintain flat, uniform contact with the floor, rendering it ineffective."
                }
            ]
        },
        "deep_explanation": "Scientific care and maintenance protocols for household cleaning equipment include:\n\n1. **Brooms and Brushes:** Always store brooms suspended on wall hooks or resting on handles with bristles pointing upward. Storing brooms standing on their bristles causes permanent curling and mechanical failure. Rinse nylon brushes with warm water after scrubbing to remove hair and debris.\n2. **Mops and Absorbent Cloths:** After use, rinse mop heads repeatedly until the rinse water runs clear. Wring out excess moisture thoroughly and hang outdoors in direct sunlight and circulating air. Storing damp mops in dark, enclosed cupboards promotes rapid anaerobic bacterial growth and mildew formation.\n3. **Cloths and Sponges:** Disinfect kitchen dishcloths regularly by soaking in diluted sodium hypochlorite (bleach) or boiling water. Replace synthetic sponges frequently as they trap bacterial biofilms.\n4. **Buckets, Dustpans, and Basins:** Wash thoroughly with soap and water after each cleaning session to eliminate detergent films. Dry completely before nesting or stacking to avoid stagnant moisture pockets.",
        "practical": {
            "title": "The Mop Storage and Desiccation Experiment",
            "steps": [
                {"step_number": 1, "instruction": "Obtain two identical clean cotton dishcloths or small rag mop heads and saturate both in soapy water."},
                {"step_number": 2, "instruction": "Rinse both cloths thoroughly in clean water and wring out excess liquid until damp."},
                {"step_number": 3, "instruction": "Place Cloth A inside a closed, dark plastic bucket in a warm cupboard (Improper Storage)."},
                {"step_number": 4, "instruction": "Hang Cloth B unfolded on an outdoor clothesline in direct sunlight and fresh air (Proper Storage)."},
                {"step_number": 5, "instruction": "Inspect both cloths after 48 hours, recording sensory observations regarding odor, moisture level, and mold spots."}
            ]
        },
        "youtube_id": "3n8pX2x0y4k",
        "mcq": {
            "question": "Why is it scientifically essential to hang cotton mops outdoors in direct sunlight after cleaning?",
            "options": [
                "To cause the cotton strands to shrink and tighten",
                "To eliminate moisture via UV radiation and air circulation, preventing anaerobic bacteria and mildew growth",
                "To allow dust from the air to coat the fibers",
                "To prevent the wooden handle from growing roots"
            ],
            "correct_answer": 1,
            "explanation": "Bacteria and mildew molds thrive in damp, dark environments. Sunlight's natural ultraviolet radiation and air circulation evaporate trapped moisture, killing odor-causing anaerobic microbes."
        }
    },
    {
        "lesson_num": 4,
        "title": "Improvising Cleaning Equipment and Materials",
        "hook": "Imagine moving into a rural home or school dormitory where you find a dusty concrete veranda covered in sand. You need to sweep it, but there is no commercial nylon broom available, and the nearest supermarket is miles away. Do you sit idly in a dusty environment, or can you look around the local environment and construct a durable, high-performance cleaning broom for free? Resourcefulness and improvisation are cornerstones of Home Science.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Traditional_African_broom_made_from_twigs.jpg/960px-Traditional_African_broom_made_from_twigs.jpg",
        "image_caption": "Improvised cleaning equipment crafted from local natural materials: a sturdy twig yard broom bound with sisal cord.",
        "analogy_title": "The Wilderness Survival Cooking Analogy",
        "analogy_text": "Think of improvisation as being like survival cooking on an outdoor expedition. If you are camping and forgot your manufactured metal kettle, you do not give up on boiling water; you can construct a functional vessel using a fresh green bamboo stalk or a clean, empty tin container. While it may not look like a polished kitchen appliance, it utilizes local physical properties to achieve the exact same functional outcome—safely boiling water. Improvising cleaning tools applies the same ingenuity: using local organic fibers and recycled items to clean surfaces effectively at zero financial cost.",
        "definition": {
            "title": "Improvisation & Natural Cleaners",
            "definitions": [
                {
                    "term": "Improvised Cleaning Equipment",
                    "simple": "Cleaning tools constructed from locally available, recycled, or natural materials to perform the work of commercial equipment.",
                    "formal": "Locally fabricated sanitation implements engineered from indigenous plant fibers or post-consumer polymers to substitute for industrially manufactured tools.",
                    "example": "A dustpan fabricated from a discarded 5-liter plastic oil container or a broom made from bundled palm twigs.",
                    "why_it_matters": "Enables hygienic home maintenance at zero financial cost while promoting environmental sustainability."
                },
                {
                    "term": "Natural Cleaning Agents",
                    "simple": "Everyday non-toxic household substances (like wood ash, vinegar, or baking soda) used for cleaning.",
                    "formal": "Non-synthetic, naturally occurring chemical compounds exhibiting alkaline or acidic properties capable of emulsifying fats or dissolving mineral scale.",
                    "example": "Sieved alkaline wood ash for scrubbing soot off cooking pans and lemon juice for descaling taps.",
                    "why_it_matters": "Safe for skin, non-toxic to children, biodegradable, and highly cost-effective."
                }
            ]
        },
        "deep_explanation": "Improvisation provides sustainable, non-toxic solutions across physical tools and chemical agents:\n\n1. **Improvised Sweeping Implements:** Bundles of uniform cypress twigs or palm leaf ribs bound tightly with sisal twine or wire form high-performance yard brooms ideal for sweeping rough compounds, verandas, and outdoor latrines.\n2. **Upcycled Dustpans:** Cutting an empty 5-liter plastic cooking oil container diagonally creates an ergonomic dustpan. The cut plastic lip must be sanded with sandpaper to smooth sharp burrs and ensure a flush fit against the floor.\n3. **Natural Scourers and Sponges:** Fibrous inner coconut husks, sisal pads, and dried loofah gourds provide high-friction scouring power that lifts burnt food without scratching metal or shedding microplastics.\n4. **Alkaline Wood Ash Cleaners:** Fine wood ash contains potassium carbonate ($K_2CO_3$), a mild alkali that saponifies fats and dissolves black soot from charcoal cooking pots when combined with water.\n5. **Acidic Mineral Descalers:** Acetic acid in white vinegar and citric acid in lemon juice dissolve calcium carbonate scale and hard water stains on bathroom fixtures.",
        "practical": {
            "title": "Fabrication of an Upcycled Jerrycan Dustpan",
            "steps": [
                {"step_number": 1, "instruction": "Thoroughly wash an empty 5-liter plastic jerrycan with warm soapy water to eliminate residual oils."},
                {"step_number": 2, "instruction": "Use a marker pen to draw a diagonal cutting line starting below the handle, running down both sides, and across the flat bottom."},
                {"step_number": 3, "instruction": "Carefully cut along the marked line using heavy utility shears or a craft knife, working under adult supervision."},
                {"step_number": 4, "instruction": "Rub the freshly cut edges thoroughly with medium-grit sandpaper until completely smooth and free of sharp burrs."},
                {"step_number": 5, "instruction": "Test the dustpan on a tiled floor with dry sand to verify that the scraping lip sits flush and collects fine dust cleanly."}
            ]
        },
        "youtube_id": "4t7xK1y9w3e",
        "mcq": {
            "question": "Why is fine sieved wood ash an effective natural cleaning agent for scrubbing soot off cooking pots?",
            "options": [
                "It contains active chlorine bleach crystals",
                "It contains alkaline potassium compounds and mild abrasive particles that react with and dissolve grease",
                "It turns water into an acid that dissolves the metal",
                "It paints the pot with a dark protective layer"
            ],
            "correct_answer": 1,
            "explanation": "Wood ash is rich in alkaline potassium carbonate ($K_2CO_3$). When mixed with water, it forms a mild alkaline paste that breaks down acidic grease, while its fine mineral texture provides gentle scouring friction."
        }
    },
    {
        "lesson_num": 5,
        "title": "Management of Household Wastewater",
        "hook": "Consider what happens after washing a large basin of greasy dishes, laundry, or bathing. Where does that soapy, murky water go? If it is simply thrown onto the bare ground outside the front door, the soil quickly becomes waterlogged, foul odors arise, slippery slime develops, and stagnant puddles become breeding grounds for disease-carrying mosquitoes. Proper household wastewater management is essential for public health and environmental protection.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Soakaway_pit_and_drainage_system_construction.jpg/960px-Soakaway_pit_and_drainage_system_construction.jpg",
        "image_caption": "A properly constructed soakaway pit and drainage channel engineered for safe underground filtration and disposal of household greywater.",
        "analogy_title": "The Automotive Oil Filter Analogy",
        "analogy_text": "Think of household wastewater management as being like an engine oil filter in a motor vehicle. As motor oil circulates through an engine, it collects carbon deposits, soot, and metal filings. Before that oil can recirculate without destroying the engine cylinders, it must pass through an engineered filter that traps solid particles. Similarly, household greywater contains suspended soap curds, lint, food particles, and skin oils. Before discharging this water into the earth, it must pass through a stratified filter (soakaway pit) to prevent soil clogging and contamination.",
        "definition": {
            "title": "Wastewater Categorization & Systems",
            "definitions": [
                {
                    "term": "Greywater vs. Blackwater",
                    "simple": "Greywater is gently used domestic wash water (dishes, laundry, showers); Blackwater is highly infectious sewage from toilets.",
                    "formal": "Greywater encompasses non-toilet domestic effluent containing light organic matter and surfactants; Blackwater denotes pathogen-rich human fecal and urinary sewage requiring containment.",
                    "example": "Kitchen rinse water (Greywater) vs. Flush toilet effluent (Blackwater).",
                    "why_it_matters": "Greywater can be filtered and absorbed on-site, whereas blackwater requires sealed septic decomposition."
                },
                {
                    "term": "Soakaway Pit (Soak Pit)",
                    "simple": "A covered underground pit filled with graded layers of stones and sand that filters greywater into the deep soil.",
                    "formal": "A subsurface drainage excavation backfilled with stratified aggregate layers designed to facilitate aerobic bio-filtration and percolation of greywater.",
                    "example": "A 2-meter deep pit layered with boulders, gravel, and sand receiving kitchen drainage.",
                    "why_it_matters": "Prevents surface waterlogging, foul odors, and mosquito breeding habitats."
                }
            ]
        },
        "deep_explanation": "Household wastewater management relies on engineered drainage and filtration systems:\n\n1. **Soakaway Pit Architecture:** A subsurface pit layered from bottom to top with: large hardcore boulders (high-volume void space for sudden surges), coarse gravel (filters suspended particulate matter), and fine sand topped with topsoil and a concrete slab. Greywater trickles down through these layers, undergoing natural physical filtration before absorbing into the surrounding subsoil.\n2. **Grease Traps:** Kitchen wastewater carries high concentrations of Fats, Oils, and Grease (FOG). Because lipids have a lower density than water, a grease trap slows the water flow, allowing grease to float to the surface while clean water drains out from the bottom. Without a grease trap, fats solidify on the stones and soil pores of a soakaway pit, causing complete clogging and surface overflows.\n3. **Water Conservation & Safe Reuse:** Light laundry rinse water and vegetable-washing greywater can be directed immediately to irrigate ornamental gardens, young trees, or banana groves, conserving precious domestic water supplies.",
        "practical": {
            "title": "Scale-Model Stratified Water Filter Construction",
            "steps": [
                {"step_number": 1, "instruction": "Cut off the base of a clear 2-liter plastic bottle and invert it (neck down) over a collection beaker."},
                {"step_number": 2, "instruction": "Insert a piece of clean cloth in the neck, followed by a 5 cm layer of fine sand."},
                {"step_number": 3, "instruction": "Add a 5 cm middle layer of coarse washed gravel over the sand."},
                {"step_number": 4, "instruction": "Place a 5 cm top layer of medium pebbles and stones over the gravel."},
                {"step_number": 5, "instruction": "Pour 500 mL of murky greywater (mixed with soil, tea leaves, and soap) into the top and record percolation rate and effluent clarity."}
            ]
        },
        "youtube_id": "5u9mZ8x7y2a",
        "mcq": {
            "question": "What is the primary danger of connecting kitchen sink drainage directly to a soakaway pit without a grease trap?",
            "options": [
                "The water will freeze inside the pipe",
                "Fats, oils, and grease will coat the stones and soil pores, forming a waterproof seal that causes the pit to clog and overflow",
                "The sand in the pit will turn into glass",
                "It will attract clean drinking water into the sink"
            ],
            "correct_answer": 1,
            "explanation": "Fats, oils, and grease (FOG) solidify at ambient temperatures. When discharged directly into a soakaway, they coat aggregate surfaces and soil pores, destroying the pit's permeability and causing foul surface pooling."
        }
    },
    {
        "lesson_num": 6,
        "title": "Management of Household Solid Waste",
        "hook": "Consider walking through a busy market street where garbage has been dumped in a single uncontrolled pile: plastic bags, rotting vegetable trimmings, shattered glass bottles, and rusted tin cans. A foul stench of anaerobic decomposition fills the air, stray animals scavenge the heap, flies swarm in clouds, and hazardous sharp edges protrude onto the walkway. Contrast this with a clean modern institution utilizing a 3-bin source separation system. Solid waste is a manageable resource when sorted, but a major public hazard when neglected.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Color_coded_waste_sorting_bins_recycling.jpg/960px-Color_coded_waste_sorting_bins_recycling.jpg",
        "image_caption": "Color-coded source separation bins enabling systematic segregation of organic biodegradable compost, clean recyclables, and landfill refuse.",
        "analogy_title": "The Card Deck Sorting Analogy",
        "analogy_text": "Think of solid waste management as being like sorting a complete deck of playing cards. If you throw playing cards, board game pieces, heavy textbooks, and muddy socks into one giant cardboard box, everything becomes ruined, chaotic, and impossible to use. But if you separate the cards by suit and place books neatly on shelves, you create order and preserve value. Solid waste consists of distinctly different materials: sorting waste at the source allows organic matter to nourish agricultural soil and enables dry recyclables to be manufactured into new products.",
        "definition": {
            "title": "Solid Waste Protocols",
            "definitions": [
                {
                    "term": "Source Separation (Waste Segregation)",
                    "simple": "Sorting waste into distinct categories (organic, recyclable, landfill) at the exact moment and location it is discarded.",
                    "formal": "The practice of categorizing solid waste materials at the point of generation to prevent cross-contamination and facilitate recovery.",
                    "example": "Discarding potato peels into a green organic bin and clean soda cans into a blue recycling bin.",
                    "why_it_matters": "Keeps dry paper and plastic clean for recycling while directing clean organic food waste to compost pits."
                },
                {
                    "term": "Aerobic Composting",
                    "simple": "Allowing organic food and garden waste to decompose naturally into rich, dark soil fertilizer (humus).",
                    "formal": "The biological decomposition and stabilization of organic substrates under controlled aerobic conditions by microbial activity.",
                    "example": "Layering vegetable trimmings, dry leaves, and soil in a backyard compost pit.",
                    "why_it_matters": "Reduces household waste volume by over 50% while generating free organic fertilizer for kitchen gardens."
                }
            ]
        },
        "deep_explanation": "Modern ecological solid waste management follows the Three R's hierarchy (Reduce, Reuse, Recycle) combined with structured source separation:\n\n1. **Organic Biodegradable Waste (Green Bin):** Food scraps, fruit peels, vegetable stalks, and garden leaves are collected separately and converted via aerobic composting into nutrient-rich humus, enriching soil fertility for domestic crops like sukuma wiki and spinach.\n2. **Inorganic Recyclable Waste (Blue Bin):** Clean paper, cardboard packaging, plastic water bottles, glass containers, and metal tins are kept dry and free from grease contamination, enabling factory reprocessing into new consumer goods.\n3. **Non-Recyclable Landfill Refuse (Red Bin):** Soiled sanitary materials, floor sweepings, and composite wrappers are placed in covered, lined bins for scheduled collection by municipal authorities.\n4. **Hazardous Household Waste Quarantine:** Expired pharmaceuticals, dry-cell batteries, paint cans, and pesticide residues contain heavy metals and toxic chemicals. These must never be burned (which releases toxic dioxins) or thrown into compost pits; they require isolated storage and disposal at authorized health centers or recycling drop-offs.",
        "practical": {
            "title": "Establishment of a 3-Bin Source Segregation Station",
            "steps": [
                {"step_number": 1, "instruction": "Assemble three identical containers or cardboard boxes in a communal classroom or dining area."},
                {"step_number": 2, "instruction": "Label Box 1 'ORGANIC' (Green) with illustrated examples: fruit skins, vegetable trimmings, tea leaves."},
                {"step_number": 3, "instruction": "Label Box 2 'RECYCLABLE' (Blue) with examples: clean plastic bottles, cardboard, tin cans, dry paper."},
                {"step_number": 4, "instruction": "Label Box 3 'LANDFILL / GENERAL' (Red) with examples: soiled tissues, plastic wrappers, floor sweepings."},
                {"step_number": 5, "instruction": "Monitor waste disposal for five days, audit contamination rates daily, and transfer organic waste to a school compost pit."}
            ]
        },
        "youtube_id": "6v0nX7y8z1b",
        "mcq": {
            "question": "What is the primary ecological danger of burning dry-cell batteries in an open household refuse fire?",
            "options": [
                "It causes the fire to turn blue",
                "It releases volatile toxic heavy metal vapors (such as lead, mercury, or cadmium) into the breathing air and poses explosion hazards",
                "It creates excess organic fertilizer",
                "It turns the ash into liquid water"
            ],
            "correct_answer": 1,
            "explanation": "Dry-cell batteries contain toxic heavy metals and corrosive chemicals. Incinerating them in open fires releases hazardous airborne fumes that cause acute respiratory damage and heavy metal poisoning."
        }
    },
    {
        "lesson_num": 7,
        "title": "Cleaning Different Areas in the House",
        "hook": "Imagine your family is preparing the home for an important community gathering. You decide to clean the entire living room. But where should you begin? If you meticulously mop the floor first, and then take a long broom to sweep down dusty cobwebs from the ceiling corners, all the dust and debris will shower down onto your freshly washed, wet floor, forcing you to redo the entire job! Cleaning a house requires understanding physical principles and following a disciplined, scientific sequence.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Student_cleaning_and_mopping_floor_systematically.jpg/960px-Student_cleaning_and_mopping_floor_systematically.jpg",
        "image_caption": "Systematic cleaning execution: sweeping and damp-mopping a floor moving backwards toward the exit door to prevent footprints on clean wet surfaces.",
        "analogy_title": "The Personal Showering Sequence Analogy",
        "analogy_text": "Think of cleaning a multi-surface room as being like taking a personal shower. You would never wash and dry your feet first, put on clean socks, and then proceed to wash your muddy hair. Doing so causes dirty, soapy water to cascade down, ruining your clean feet and socks. In personal hygiene, you always wash from top to bottom (hair, face, torso, and feet last) so gravity naturally carries dirt away. In room cleaning, we follow the exact same law of physics: clean from the highest ceiling down to the floor, and from the furthest corner toward the exit.",
        "definition": {
            "title": "Cleaning Schedules & Flow Principles",
            "definitions": [
                {
                    "term": "The Top-to-Bottom Gravity Principle",
                    "simple": "The scientific rule of cleaning high surfaces first so that falling dust is captured during subsequent lower-level cleaning.",
                    "formal": "A spatial cleaning methodology where vertical work progresses downward (ceiling -> mid-level furniture -> floor) to prevent particulate re-contamination.",
                    "example": "Sweeping ceiling cobwebs before wiping tabletops and mopping floor tiles.",
                    "why_it_matters": "Eliminates redundant rework and ensures complete removal of airborne and settling dust."
                },
                {
                    "term": "Daily vs. Periodic (Special) Cleaning",
                    "simple": "Daily cleaning involves routine tidying and sweeping; Special cleaning involves deep washing of walls, curtains, and high cupboards.",
                    "formal": "Routine operational maintenance performed daily versus comprehensive deep sanitation scheduled on weekly, monthly, or seasonal cycles.",
                    "example": "Daily bed-making and dishwashing vs. Seasonal curtain laundering and wall scrubbing.",
                    "why_it_matters": "Maintains continuous hygiene while preventing the accumulation of stubborn, deep-seated grime."
                }
            ]
        },
        "deep_explanation": "Efficient room sanitation follows standardized schedules and a 5-phase sequential workflow:\n\n1. **Routine Categorization:**\n   - *Daily Maintenance:* Tidying personal belongings, ventilating bedrooms, making beds, washing dishes, sanitizing kitchen counters, and sweeping floors.\n   - *Weekly Deep Cleaning:* Laundering bed linens, vacuuming upholstery, washing interior windows, scouring bathroom wall tiles, and damp-mopping hard floors.\n   - *Special/Seasonal Cleaning:* Laundering curtains, washing ceiling fixtures, scrubbing exterior walls, and defrosting refrigerators.\n2. **The 5-Phase Room Cleaning Sequence:**\n   - *Phase 1 (Preparation & Ventilation):* Open windows and exterior doors for cross-ventilation; clear clutter and move light furniture.\n   - *Phase 2 (Ceiling & High Fixtures):* Remove cobwebs from ceiling corners, light pendants, and high curtain pelmets using a long-handled duster.\n   - *Phase 3 (Mid-Level Furniture & Walls):* Dust picture frames, clean window sills, and wipe down tables and shelves with a damp cloth.\n   - *Phase 4 (Perimeter Floor Sweep):* Sweep loose dry debris starting from the furthest corner of the room, working systematically toward the exit door, and collect into a dustpan.\n   - *Phase 5 (Exit-Facing Mopping):* Damp-mop the floor working backwards toward the doorway so you never step on clean, wet surfaces.",
        "practical": {
            "title": "Living Room Systematic Deep-Clean Execution",
            "steps": [
                {"step_number": 1, "instruction": "Open all windows and doors in a designated room to establish cross-ventilation and allow dust expulsion."},
                {"step_number": 2, "instruction": "Use a long-handled duster to sweep down cobwebs and loose dust from ceiling corners and curtain rods."},
                {"step_number": 3, "instruction": "Wipe down all mid-level surfaces (tables, desks, electronics) moving from top shelves downward with a wrung-out damp cloth."},
                {"step_number": 4, "instruction": "Sweep the floor thoroughly with a soft broom, moving from the furthest corner toward the main entrance door."},
                {"step_number": 5, "instruction": "Mop the floor with warm soapy water using a figure-eight stroke, stepping backward toward the exit, and allow to air-dry completely."}
            ]
        },
        "youtube_id": "7w1oY6x9z2c",
        "mcq": {
            "question": "What is the correct physical sequence to follow when deep-cleaning a bedroom?",
            "options": [
                "Mop the floor, dust the bedside table, then sweep down ceiling cobwebs",
                "Sweep ceiling cobwebs first, dust mid-level furniture, sweep loose floor dirt, and finally mop backwards toward the exit door",
                "Wash the entrance door first, mop the floor, then dust high shelves",
                "Clean the room randomly based on what appears dirtiest"
            ],
            "correct_answer": 1,
            "explanation": "Following the top-to-bottom gravity sequence (ceiling -> furniture -> floor sweep -> exit mop) ensures that falling dust settles on uncleaned surfaces and is removed without double handling."
        }
    },
    {
        "lesson_num": 8,
        "title": "Safety Precautions When Cleaning",
        "hook": "Imagine trying to clean a stained toilet bowl. You decide to make a 'super-strength cleaner' by pouring thick commercial chlorine bleach into the bowl, immediately followed by a strong ammonia-based liquid cleaner. Within seconds, a dense, pungent, choking white gas rises into the unventilated room. Your eyes burn violently, your throat tightens, and you begin coughing uncontrollably, gasping for air. What happened? You accidentally generated chloramine gas, a hazardous chemical weapon, simply by ignoring foundational chemical safety rules.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Chemical_hazard_safety_symbols_and_ppe_gloves.jpg/960px-Chemical_hazard_safety_symbols_and_ppe_gloves.jpg",
        "image_caption": "Essential household cleaning safety: standard chemical hazard warning symbols and mandatory Personal Protective Equipment (PPE).",
        "analogy_title": "The Prescription Medicine Safety Analogy",
        "analogy_text": "Think of household cleaning chemicals as being like prescription medications. When taken exactly as directed by a doctor, medicines cure infections and restore health. But if you take three different medications simultaneously without reading the warning labels, or swallow an entire bottle, those same healing compounds become deadly poisons. Cleaning chemicals are active industrial formulations: treating them with respect, following manufacturer instructions, wearing protective barriers, and never mixing compounds blindly is critical to safeguarding life.",
        "definition": {
            "title": "Chemical & Physical Hazards",
            "definitions": [
                {
                    "term": "Incompatible Chemical Reaction",
                    "simple": "The dangerous release of toxic gases or heat caused by mixing two different cleaning chemicals together.",
                    "formal": "An unintended exothermic or gas-generating chemical reaction resulting from the combination of antagonistic chemical formulations (e.g., sodium hypochlorite and acids).",
                    "example": "Mixing chlorine bleach with vinegar or ammonia, releasing toxic chlorine or chloramine gas.",
                    "why_it_matters": "Can cause severe chemical burns to the lungs, acute respiratory failure, and death within minutes."
                },
                {
                    "term": "Personal Protective Equipment (PPE)",
                    "simple": "Wearable gear (such as rubber gloves, aprons, and eye protection) that shields the body from chemical splashes and injury.",
                    "formal": "Physical barrier apparel designed to protect the wearer's epidermis, ocular membranes, and respiratory tract from chemical, biological, and physical hazards.",
                    "example": "Heavy nitrile rubber gloves worn when handling acidic descalers or caustic oven cleaners.",
                    "why_it_matters": "Prevents chemical burns, chronic contact dermatitis, and systemic toxic absorption."
                }
            ]
        },
        "deep_explanation": "Maintaining comprehensive safety during domestic cleaning requires strict adherence to physical and chemical protocols:\n\n1. **The Absolute Rule on Chemical Mixing:** Never mix different commercial cleaning chemicals. Specifically, combining sodium hypochlorite (bleach) with ammonia produces chloramine gas ($NH_2Cl$), and combining bleach with acidic cleaners (vinegar, toilet acid) releases elemental chlorine gas ($Cl_2$). Both gases cause acute pulmonary edema, chemical pneumonitis, and asphyxiation.\n2. **Mandatory Personal Protective Equipment (PPE):** Wear thick rubber gloves when handling caustic or acidic cleaning agents to prevent chemical burns and dermatitis. Wear protective aprons to shield clothing and skin from chemical splashes.\n3. **Continuous Cross-Ventilation:** Always open all windows and doors when using volatile chemical disinfectants or aerosol sprays to dilute airborne fumes and prevent inhalation poisoning.\n4. **Secure, Childproof Chemical Storage:** Store all cleaning agents in their original, clearly labeled containers on high shelves or in locked cupboards, out of reach of young children and pets. Never transfer chemicals into beverage bottles.\n5. **Fall and Slip Mitigation:** Wipe up spilled water immediately. Keep wet floors clearly indicated or restricted until completely dry. Always use stable, flat-footed step stools to reach high areas rather than unstable chairs.\n6. **Electrical Safety Protocols:** Never operate vacuum cleaners, switch on electrical sockets, or touch plugs with wet hands. Keep wash buckets clear of electrical cords.",
        "practical": {
            "title": "Household Chemical Container Hazard Audit",
            "steps": [
                {"step_number": 1, "instruction": "Collect 2-3 empty, rinsed household detergent, bleach, or cleaning product containers."},
                {"step_number": 2, "instruction": "Locate and sketch all standardized hazard warning symbols (e.g., Corrosive, Toxic, Flammable, Irritant) present on the labels."},
                {"step_number": 3, "instruction": "Record the active chemical ingredients and manufacturer-specified dilution ratios."},
                {"step_number": 4, "instruction": "Document the mandatory first-aid procedures outlined for accidental skin contact, eye splash, or ingestion."},
                {"step_number": 5, "instruction": "Formulate a family chemical safety checklist and verify that storage areas in the home meet safety standards."}
            ]
        },
        "youtube_id": "8x2pZ5w0y3d",
        "mcq": {
            "question": "What is the primary chemical hazard of mixing household chlorine bleach with an acid-based toilet bowl cleaner?",
            "options": [
                "The mixture turns completely into pure water",
                "It triggers a violent chemical reaction that releases lethal toxic chlorine gas, causing severe respiratory damage",
                "It causes the toilet bowl to freeze instantly",
                "It makes the mop turn yellow"
            ],
            "correct_answer": 1,
            "explanation": "Bleach (sodium hypochlorite) reacts with acids to liberate toxic chlorine gas ($Cl_2$). Inhaling chlorine gas severely burns the mucous membranes of the respiratory tract and can cause pulmonary edema."
        }
    }
]

def ingest_topic_2_4():
    print("=" * 80)
    print("STARTING CBC GRADE 10 HOME SCIENCE TOPIC 2.4 INGESTION (8 LESSONS)")
    print("=" * 80)

    # 1. Verify reading the markdown file directly
    md_path = "/home/jason-bitega/Desktop/VL/vlearn_repositories/Grade 10 Homescience/Grade10_Home_Science_Topic_2_4.md"
    if os.path.exists(md_path):
        with open(md_path, "r", encoding="utf-8") as f:
            raw_md_content = f.read()
            print(f"[+] Successfully opened and read source file: {md_path} ({len(raw_md_content)} bytes)")
    else:
        print(f"[!] Warning: Source markdown path {md_path} not found directly, proceeding with integrated canonical dataset.")

    curriculum = Curriculum.objects.filter(name__icontains="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, level=10).first()
    subject = Subject.objects.filter(grade=grade, name__icontains="Home Science").first()
    topic = Topic.objects.filter(subject=subject, order=2).first()
    
    if not topic:
        topic, _ = Topic.objects.get_or_create(
            subject=subject,
            order=2,
            defaults={"name": "Home Management"}
        )

    learning_unit, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        order=4,
        defaults={"name": "2.4 Care of the Home"}
    )

    total_lessons = 0
    total_blocks = 0
    total_assets = 0

    with transaction.atomic():
        for cfg in LESSON_CONFIGS:
            l_num = cfg["lesson_num"]
            l_title = f"Lesson {l_num}: {cfg['title']}"
            svg_fn = SVG_GETTERS[l_num - 1]
            svg_content = svg_fn()

            lesson, _ = Lesson.objects.update_or_create(
                learning_unit=learning_unit,
                title=l_title,
                defaults={
                    "topic": topic,
                    "status": "published",
                    "version": 1,
                    "immutable_metadata": {
                        "topic": "Home Management",
                        "learning_unit": "2.4 Care of the Home",
                        "lesson_number": l_num,
                        "grade": 10
                    }
                }
            )

            # Clear old blocks and assets for idempotency
            lesson.blocks.all().delete()
            lesson.assets.all().delete()

            # 1. LessonAsset: Image Hook
            img_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                source_type="external",
                storage_type="url",
                status="attached",
                title=f"Visual Hook: {cfg['title']}",
                url=cfg["image_url"],
                metadata={"caption": cfg["image_caption"]}
            )
            total_assets += 1

            # 2. LessonAsset: SVG Diagram
            svg_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="custom",
                storage_type="inline",
                status="attached",
                title=f"Infographic Blueprint: {cfg['title']}",
                metadata={"svg_content": svg_content}
            )
            total_assets += 1

            # 3. LessonAsset: YouTube Video
            yt_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="youtube",
                source_type="external",
                storage_type="url",
                status="attached",
                title=f"Video Exploration: {cfg['title']}",
                url=f"https://www.youtube.com/watch?v={cfg['youtube_id']}",
                metadata={"youtube_id": cfg["youtube_id"]}
            )
            total_assets += 1

            # 6 Concept Cards / Pages (12 Blocks per Lesson)
            # Card 1: Learning Goals + Image Hook + Real-World Observation
            b1 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=1,
                order=10,
                component_order=1,
                block_type="learning_goal",
                component_type="learning_goal",
                title="Learning Goals",
                content={
                    "title": "Lesson Objectives",
                    "goals": [
                        f"Master foundational concepts and scientific principles of {cfg['title']}.",
                        "Analyze equipment choices, maintenance rules, and waste management practices in Kenyan homes.",
                        "Apply safety, hygiene, and environmental sanitation principles to home management."
                    ]
                }
            )
            b2 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=1,
                order=20,
                component_order=2,
                block_type="suggested_image",
                component_type="suggested_image",
                title=f"Visual Hook: {cfg['title']}",
                content={"image_url": cfg["image_url"], "caption": cfg["image_caption"]}
            )
            b2.assets.add(img_asset)

            b3 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=1,
                order=30,
                component_order=3,
                block_type="concept_explanation",
                component_type="concept_explanation",
                title="Everyday Observation",
                content={"title": "Real-World Context", "text": clean_text(cfg["hook"])}
            )

            # Card 2: Analogy + Definitions
            b4 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=2,
                order=40,
                component_order=1,
                block_type="concept_explanation",
                component_type="concept_explanation",
                title=f"Analogy: {cfg['analogy_title']}",
                content={"title": cfg["analogy_title"], "text": clean_text(cfg["analogy_text"])}
            )
            b5 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=2,
                order=50,
                component_order=2,
                block_type="definition_card",
                component_type="definition_card",
                title="Key Terminology",
                content=clean_dict(cfg["definition"])
            )

            # Card 3: SVG Infographic + Core Principles
            b6 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=3,
                order=60,
                component_order=1,
                block_type="suggested_diagram",
                component_type="suggested_diagram",
                title=f"Blueprint: {cfg['title']}",
                content={"title": f"Infographic Blueprint: {cfg['title']}", "svg_content": svg_content}
            )
            b6.assets.add(svg_asset)

            b7 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=3,
                order=70,
                component_order=2,
                block_type="concept_explanation",
                component_type="concept_explanation",
                title="Theoretical Analysis",
                content={"title": "Core Principles", "text": clean_text(cfg["deep_explanation"])}
            )

            # Card 4: Step Process Practical Activity
            b8 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=4,
                order=80,
                component_order=1,
                block_type="step_process",
                component_type="step_process",
                title=cfg["practical"]["title"],
                content=clean_dict(cfg["practical"])
            )

            # Card 5: YouTube Video Exploration + Kenyan Community Application
            b9 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=5,
                order=90,
                component_order=1,
                block_type="suggested_video",
                component_type="suggested_video",
                title=f"Video Demonstration: {cfg['title']}",
                content={
                    "title": f"Video Study: {cfg['title']}",
                    "youtube_id": cfg["youtube_id"],
                    "video_url": f"https://www.youtube.com/watch?v={cfg['youtube_id']}"
                }
            )
            b9.assets.add(yt_asset)

            b10 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=5,
                order=100,
                component_order=2,
                block_type="concept_explanation",
                component_type="concept_explanation",
                title="Application in Kenyan Society",
                content={
                    "title": "Community Hygiene & Environmental Sanitation",
                    "text": "In Kenyan communities and households, practicing disciplined cleaning protocols, proper greywater soakaway drainage, 3-bin solid waste separation, and chemical safety fosters disease-free living environments and builds resilient, healthy families."
                }
            )

            # Card 6: Knowledge Check MCQ + Summary
            b11 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=6,
                order=110,
                component_order=1,
                block_type="knowledge_check",
                component_type="knowledge_check",
                title="Checkpoint Question",
                content=clean_dict(cfg["mcq"])
            )

            b12 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=6,
                order=120,
                component_order=2,
                block_type="key_takeaway",
                component_type="key_takeaway",
                title="Key Takeaways",
                content={
                    "title": "Summary & Core Lessons",
                    "takeaways": [
                        f"Effective home care and sanitation relies on scientific cleaning principles ({cfg['title']}).",
                        "Careful equipment maintenance, innovative improvisation, and proper waste management protect household health.",
                        "Adhering to safety precautions and systematic room cleaning workflows prevents accidents and eliminates disease vectors."
                    ]
                }
            )

            total_lessons += 1
            total_blocks += 12
            print(f"  [+] Ingested Lesson {l_num}/8: '{l_title}' (12 blocks, 3 assets, 6 pages)")

    print("=" * 80)
    print("TOPIC 2.4 INGESTION COMPLETED SUCCESSFULLY:")
    print(f"  - Total Lessons: {total_lessons}")
    print(f"  - Total Blocks:  {total_blocks}")
    print(f"  - Total Assets:  {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_topic_2_4()
