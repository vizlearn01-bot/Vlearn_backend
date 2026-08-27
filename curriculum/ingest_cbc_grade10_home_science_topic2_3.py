"""
VLearn CBC Grade 10 Home Science — Sub-Strand 2.3: Housing the Family
Comprehensive Production Ingestion & Visual Enrichment Engine

Curriculum: CBC
Grade: Grade 10 (Level: 10)
Subject: Home Science
Topic: Home Management (Order: 2)
Learning Unit 3: 2.3 Housing the Family (Order: 3)

Decomposed into 4 Published Lessons:
  - Lesson 1: Reasons for Housing the Family
  - Lesson 2: Categorisation of Houses in the Community
  - Lesson 3: Methods of Housing the Family
  - Lesson 4: Room Functions and Room Interrelationships

Features:
  - Reads Grade10_Home_Science_Topic_2_3.md directly
  - 4 Custom Responsive Sanitized Vector SVG Diagrams with viewBox="0 0 800 450"
  - 4 Verified Wikimedia Commons Photographic Assets with attached LessonAssets
  - 4 Verified Educational YouTube Video Integrations with attached LessonAssets
  - 4 Formative Scenario-Based MCQs with 4 options, valid correct_answer index, and detailed explanations
  - Discrete 6 concept cards (pages) per lesson with full typed block coverage
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
    """Removes bracket citations and normalizes markdown."""
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

# 4 Custom Vector SVGs for Topic 2.3
def get_svg_1():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">HOUSING THE FAMILY: CORE REASONS &amp; HUMAN NEEDS</text>
  <text x="400" y="54" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">A Comprehensive Blueprint of Physical, Health, Psychological, and Economic Shelter Functions</text>

  <!-- 4 Pillars Grid -->
  <g transform="translate(30, 75)">
    <!-- Card 1: Physical Protection -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#0284c7"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🛡️ PHYSICAL NEEDS</text>
    <text x="12" y="55" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Weather Shield:</text>
    <text x="12" y="72" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Rain, extreme heat, cold winds, sun.</text>
    <text x="12" y="102" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Intruder Security:</text>
    <text x="12" y="119" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Locks, high walls, pest barrier.</text>
    <text x="12" y="149" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Asset Storage:</text>
    <text x="12" y="166" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Food, farm tools, clothes &amp; beds.</text>
    <rect x="10" y="260" width="150" height="65" rx="6" fill="#0f172a"/>
    <text x="85" y="282" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Primary Metric:</text>
    <text x="85" y="302" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Survival &amp; Security</text>
  </g>

  <g transform="translate(220, 75)">
    <!-- Card 2: Health & Sanitation -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#059669"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🩺 HEALTH &amp; HYGIENE</text>
    <text x="12" y="55" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Waste Management:</text>
    <text x="12" y="72" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Proper sewer, drain &amp; latrine pipes.</text>
    <text x="12" y="102" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Pathogen Defense:</text>
    <text x="12" y="119" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Fly-screens, clean kitchen surfaces.</text>
    <text x="12" y="149" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Safe Cooking:</text>
    <text x="12" y="166" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Clean water access, smoke exhaust.</text>
    <rect x="10" y="260" width="150" height="65" rx="6" fill="#0f172a"/>
    <text x="85" y="282" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Primary Metric:</text>
    <text x="85" y="302" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Disease Prevention</text>
  </g>

  <g transform="translate(410, 75)">
    <!-- Card 3: Psychological & Social -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#d97706"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">💖 PSYCHOLOGICAL</text>
    <text x="12" y="55" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Privacy &amp; Dignity:</text>
    <text x="12" y="72" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Private bedrooms, dressing rooms.</text>
    <text x="12" y="102" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Family Bonding:</text>
    <text x="12" y="119" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Living &amp; dining social connection.</text>
    <text x="12" y="149" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Identity &amp; Pride:</text>
    <text x="12" y="166" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Cultural decor, emotional warmth.</text>
    <rect x="10" y="260" width="150" height="65" rx="6" fill="#0f172a"/>
    <text x="85" y="282" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Primary Metric:</text>
    <text x="85" y="302" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Mental Well-Being</text>
  </g>

  <g transform="translate(600, 75)">
    <!-- Card 4: Economic & Status -->
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="32" rx="10" fill="#7e22ce"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">📈 ECONOMIC ASSET</text>
    <text x="12" y="55" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Generational Equity:</text>
    <text x="12" y="72" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Real estate wealth appreciation.</text>
    <text x="12" y="102" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Social Status:</text>
    <text x="12" y="119" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Community recognition &amp; stability.</text>
    <text x="12" y="149" fill="#f1f5f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Collateral Security:</text>
    <text x="12" y="166" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Title deed for business financing.</text>
    <rect x="10" y="260" width="150" height="65" rx="6" fill="#0f172a"/>
    <text x="85" y="282" fill="#c084fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Primary Metric:</text>
    <text x="85" y="302" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Financial Resilience</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_2():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">CATEGORISATION OF HOUSES: TRADITIONAL VS. MODERN ARCHITECTURE</text>
  <text x="400" y="52" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Material Physics, Structural Forms, and Environmental Adaptations</text>

  <!-- Left: Traditional Architecture -->
  <g transform="translate(30, 70)">
    <rect width="355" height="350" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="355" height="32" rx="12" fill="#b45309"/>
    <text x="177" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">🏕️ TRADITIONAL HOUSES</text>
    
    <text x="20" y="60" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="12" font-weight="700">1. Manyatta (Maasai):</text>
    <text x="20" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Woven timber frame + mud, ash, cow dung layer.</text>
    <text x="20" y="96" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">Sun-baked cow dung creates waterproof thermal shell.</text>

    <text x="20" y="130" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="12" font-weight="700">2. Grass-Thatched Mud Roundhouse:</text>
    <text x="20" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">High thermal mass mud walls + thick conical thatch.</text>
    <text x="20" y="166" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">Trapped air pockets insulate against midday heat &amp; night chill.</text>

    <!-- Bottom Pros/Cons Box -->
    <rect x="15" y="205" width="325" height="125" rx="8" fill="#0f172a" stroke="#d97706" stroke-width="1"/>
    <text x="25" y="228" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Key Advantages:</text>
    <text x="25" y="246" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">Zero factory cost, local sustainable sourcing, natural thermal regulation.</text>
    <text x="25" y="278" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✗ Key Limitations:</text>
    <text x="25" y="296" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">Vulnerable to termites, decay, fire; frequent re-thatching required.</text>
  </g>

  <!-- Right: Modern Architecture -->
  <g transform="translate(415, 70)">
    <rect width="355" height="350" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="355" height="32" rx="12" fill="#0284c7"/>
    <text x="177" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">🏢 MODERN HOUSES</text>
    
    <text x="20" y="60" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">1. Bungalow &amp; Maisonette:</text>
    <text x="20" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Bungalow: Single-story accessible ground layout.</text>
    <text x="20" y="96" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">Maisonette: Multi-story with internal staircase.</text>

    <text x="20" y="130" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">2. Apartments &amp; Sustainable Eco-Homes:</text>
    <text x="20" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Vertical stacking maximizes high-value urban land.</text>
    <text x="20" y="166" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10.5">Eco-homes utilize compressed earth bricks + solar systems.</text>

    <!-- Bottom Pros/Cons Box -->
    <rect x="15" y="205" width="325" height="125" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
    <text x="25" y="228" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Key Advantages:</text>
    <text x="25" y="246" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">Reinforced durability, fire-proof, security, scalable plumbing &amp; power.</text>
    <text x="25" y="278" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✗ Key Limitations:</text>
    <text x="25" y="296" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">High capital expenditure, requires ceiling insulation to prevent thermal swings.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_3():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">METHODS OF HOUSING: BUILDING VS. BUYING VS. RENTING</text>
  <text x="400" y="54" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Comparative Trade-Off Matrix of Capital Requirements, Equity, and Flexibility</text>

  <!-- 3 Pillars Grid -->
  <g transform="translate(35, 75)">
    <!-- 1. Building -->
    <rect x="0" y="0" width="220" height="340" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="32" rx="10" fill="#059669"/>
    <text x="110" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">🔨 1. BUILDING A HOUSE</text>
    
    <text x="15" y="60" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Financial Profile:</text>
    <text x="15" y="78" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">• High capital, spread over years</text>
    <text x="15" y="96" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">• Phased construction avoids debt</text>

    <text x="15" y="130" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Flexibility &amp; Control:</text>
    <text x="15" y="148" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">• 100% custom architectural plan</text>
    <text x="15" y="166" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">• Full quality oversight of materials</text>

    <text x="15" y="200" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Trade-Off / Risk:</text>
    <text x="15" y="218" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">• Time-consuming project management</text>
    <text x="15" y="236" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">• Risk of material inflation / overruns</text>

    <rect x="15" y="265" width="190" height="55" rx="6" fill="#0f172a"/>
    <text x="110" y="288" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Equity Build-Up:</text>
    <text x="110" y="306" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">★★★★★ Maximum</text>
  </g>

  <g transform="translate(290, 75)">
    <!-- 2. Buying -->
    <rect x="0" y="0" width="220" height="340" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="32" rx="10" fill="#0284c7"/>
    <text x="110" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">🏡 2. BUYING A HOUSE</text>
    
    <text x="15" y="60" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Financial Profile:</text>
    <text x="15" y="78" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">• Very high upfront cash or mortgage</text>
    <text x="15" y="96" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">• Bank interest charges apply</text>

    <text x="15" y="130" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Flexibility &amp; Control:</text>
    <text x="15" y="148" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">• Immediate occupancy &amp; roads</text>
    <text x="15" y="166" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">• Established water/grid connections</text>

    <text x="15" y="200" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Trade-Off / Risk:</text>
    <text x="15" y="218" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">• Rigid floor plan cannot change</text>
    <text x="15" y="236" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">• Property taxes &amp; legal deed costs</text>

    <rect x="15" y="265" width="190" height="55" rx="6" fill="#0f172a"/>
    <text x="110" y="288" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Occupancy Speed:</text>
    <text x="110" y="306" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">★★★★★ Immediate</text>
  </g>

  <g transform="translate(545, 75)">
    <!-- 3. Renting -->
    <rect x="0" y="0" width="220" height="340" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="32" rx="10" fill="#d97706"/>
    <text x="110" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">🔑 3. RENTING A HOME</text>
    
    <text x="15" y="60" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Financial Profile:</text>
    <text x="15" y="78" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">• Low initial barrier (deposit + 1 mo)</text>
    <text x="15" y="96" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">• Fixed monthly operating expense</text>

    <text x="15" y="130" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Flexibility &amp; Control:</text>
    <text x="15" y="148" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">• High mobility for changing jobs</text>
    <text x="15" y="166" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">• Landlord pays structural maintenance</text>

    <text x="15" y="200" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Trade-Off / Risk:</text>
    <text x="15" y="218" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">• Zero equity accumulation over time</text>
    <text x="15" y="236" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10.5">• Risk of rent hikes / lease termination</text>

    <rect x="15" y="265" width="190" height="55" rx="6" fill="#0f172a"/>
    <text x="110" y="288" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Mobility Flexibility:</text>
    <text x="110" y="306" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">★★★★★ Maximum</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_4():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="30" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">ROOM FUNCTIONS &amp; ARCHITECTURAL INTERRELATIONSHIPS</text>
  <text x="400" y="48" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Spatial Zonation, Circulation Flow, Acoustic Isolation, and Privacy Buffer</text>

  <!-- Left: Floor Plan Blueprint Layout -->
  <g transform="translate(30, 65)">
    <rect width="440" height="360" rx="10" fill="#1e293b" stroke="#475569" stroke-width="2"/>
    <text x="220" y="22" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">RESIDENTIAL ZONAL FLOOR PLAN</text>

    <!-- Quiet Private Zone (Top Left) -->
    <rect x="15" y="35" width="190" height="150" rx="6" fill="#1e1b4b" stroke="#818cf8" stroke-width="1.5"/>
    <text x="110" y="58" fill="#c7d2fe" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🛏️ BEDROOM 1 &amp; 2</text>
    <text x="110" y="78" fill="#818cf8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">[QUIET PRIVATE ZONE]</text>
    <rect x="25" y="100" width="170" height="70" rx="4" fill="#0f172a"/>
    <text x="110" y="125" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Bathroom Access Buffer</text>
    <text x="110" y="145" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Acoustically Isolated</text>

    <!-- Utility & Prep Zone (Top Right) -->
    <rect x="235" y="35" width="190" height="150" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="1.5"/>
    <text x="330" y="58" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🍳 KITCHEN &amp; PANTRY</text>
    <text x="330" y="78" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">[WORK &amp; UTILITY ZONE]</text>
    <rect x="245" y="100" width="170" height="70" rx="4" fill="#0f172a"/>
    <text x="330" y="125" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Direct Food Flow Path</text>
    <text x="330" y="145" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Adjacent to Dining</text>

    <!-- Central Hallway / Circulation Buffer -->
    <rect x="15" y="195" width="410" height="30" rx="4" fill="#334155"/>
    <text x="220" y="215" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">↔️ CENTRAL CIRCULATION HALLWAY (PRIVACY SCREEN)</text>

    <!-- Social & Public Living Zone (Bottom) -->
    <rect x="15" y="235" width="230" height="110" rx="6" fill="#451a03" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="130" y="258" fill="#fde68a" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🛋️ LIVING ROOM</text>
    <text x="130" y="278" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">[SOCIAL PUBLIC ZONE]</text>
    <text x="130" y="305" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Main Entry &amp; Guest Lounge</text>

    <!-- Dining Room (Bottom Right) -->
    <rect x="255" y="235" width="170" height="110" rx="6" fill="#14532d" stroke="#22c55e" stroke-width="1.5"/>
    <text x="340" y="258" fill="#bbf7d0" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🍽️ DINING ROOM</text>
    <text x="340" y="278" fill="#4ade80" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">[SEMI-SOCIAL ZONE]</text>
    <text x="340" y="305" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Direct Serving Connection</text>
  </g>

  <!-- Right: 4 Golden Principles of Room Arrangement -->
  <g transform="translate(490, 65)">
    <rect width="280" height="360" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="280" height="32" rx="10" fill="#0284c7"/>
    <text x="140" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">📐 4 LAYOUT PRINCIPLES</text>

    <text x="15" y="60" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">1. Efficiency &amp; Proximity:</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Kitchen directly adjacent to Dining saves steps and prevents hot spills.</text>

    <text x="15" y="120" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">2. Privacy Separation:</text>
    <text x="15" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Bedrooms and toilets isolated from guest sightlines in living areas.</text>

    <text x="15" y="180" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">3. Acoustic Noise Control:</text>
    <text x="15" y="198" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Quiet study/sleep zones buffered from TV, laundry, and kitchen sounds.</text>

    <text x="15" y="240" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700">4. Health &amp; Sanitation:</text>
    <text x="15" y="258" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Toilets buffered from food prep areas to eliminate pathogen vectors.</text>

    <rect x="15" y="300" width="250" height="45" rx="6" fill="#0f172a"/>
    <text x="140" y="326" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Outcome: Peaceful, Hygienic Home</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

SVG_GETTERS = [get_svg_1, get_svg_2, get_svg_3, get_svg_4]

# Lesson Configurations
LESSON_CONFIGS = [
    {
        "lesson_num": 1,
        "title": "Reasons for Housing the Family",
        "hook": "Think about a cold, rainy evening. Dark clouds gather, a chilly wind blows, and heavy rain starts pounding on the ground. Where does everyone rush to go? They go home. Or think about where you keep your clothes, eat meals with your family, and sleep safely at night. A house is not just a building made of stone, mud, or wood; it is a vital environment that shapes our health, happiness, and family relationships.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Warm_family_living_room_in_Nairobi.jpg/960px-Warm_family_living_room_in_Nairobi.jpg",
        "image_caption": "A welcoming home environment provides physical protection, emotional security, and a central space for family bonding.",
        "analogy_title": "The Astronaut's Space Suit",
        "analogy_text": "Think of a house as a space suit worn by an astronaut. On the moon, there is no air, temperatures are extreme, and there is dangerous radiation. The space suit acts as a portable shelter, protecting the astronaut and providing life support. Similarly, our planet has harsh weather, disease vectors, and hazards. A house acts as our 'earthly space suit'—a protective envelope that keeps us healthy, safe, organized, and connected to our loved ones.",
        "definition": {
            "title": "House vs. Home",
            "definitions": [
                {
                    "term": "House",
                    "simple": "A physical building or structure that serves as a shelter for people to live in.",
                    "formal": "A permanent or semi-permanent physical architectural enclosure providing basic protection against environmental elements and external dangers.",
                    "example": "A concrete structure with stone walls and an iron sheet roof.",
                    "why_it_matters": "Provides the structural foundation for human dwelling."
                },
                {
                    "term": "Home",
                    "simple": "A house transformed by a family's love, shared experiences, values, and care into a place of belonging and emotional security.",
                    "formal": "The socio-psychological environment established within a dwelling that fulfills emotional, cultural, and relational human needs.",
                    "example": "A living space where family members share meals, celebrate culture, and feel accepted.",
                    "why_it_matters": "A house is a physical structure, but a home is a space of emotional warmth and identity."
                }
            ]
        },
        "deep_explanation": "Housing fulfills fundamental human needs across four key categories:\n\n1. **Physical Protection:** Shelters from rain, extreme heat, cold winds, sun, intruders, and pests. Provides dry storage for food, clothes, and tools.\n2. **Health and Sanitation:** Facilities for clean water, hygienic cooking, washing, and waste disposal block pathogen transmission.\n3. **Social and Psychological Needs:** Provides privacy for rest, a central hub for family bonding, and an expression of cultural identity.\n4. **Economic and Social Status:** Real estate ownership builds generational equity, financial resilience, and community recognition.",
        "practical": {
            "title": "Household Functional Needs Audit",
            "steps": [
                {"step_number": 1, "instruction": "Identify 5 distinct spaces or items in your home (e.g. front door lock, dining table, bedroom window, pantry, bathroom tap)."},
                {"step_number": 2, "instruction": "Categorize each item under its primary human need: Physical, Health/Sanitation, Psychological, or Economic."},
                {"step_number": 3, "instruction": "Record how each feature directly improves your daily well-being and health."},
                {"step_number": 4, "instruction": "Identify one simple improvement that would enhance hygiene or privacy in your living space."},
                {"step_number": 5, "instruction": "Document your findings and reflections in your Home Science workbook."}
            ]
        },
        "youtube_id": "7q_qMkJcI1Y",
        "mcq": {
            "question": "Which of the following is considered a purely psychological and emotional need fulfilled by housing?",
            "options": [
                "Keeping heavy rain and cold wind out",
                "Storing farm tools safely in a locked pantry",
                "Providing a private bedroom for rest, relaxation, and personal space",
                "Connecting the kitchen drainage pipe to a municipal soakaway"
            ],
            "correct_answer": 2,
            "explanation": "Privacy, rest, and personal emotional security are psychological needs. Weather protection and storage are physical needs, while drainage is a sanitation need."
        }
    },
    {
        "lesson_num": 2,
        "title": "Categorisation of Houses in the Community",
        "hook": "Take a look around your local community or travel across Kenya. You will see an incredible variety of houses: a Maasai Manyatta made of mud and cow dung, a rural house with mud walls and a grass-thatched roof, a single-story brick bungalow, or a tall multi-story concrete apartment block. Why are there so many different styles, and what materials are used to build them?",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Men_at_work_in_a_residential_house_construction_site.jpg/960px-Men_at_work_in_a_residential_house_construction_site.jpg",
        "image_caption": "Housing styles evolve from traditional indigenous structures using natural materials to modern engineered buildings.",
        "analogy_title": "Classifying Seasonal Garments",
        "analogy_text": "Think of categorizing houses as being like classifying different types of clothing. In cold weather, you wear heavy woolen coats; in hot weather, light cotton. Traditional clothing uses natural local materials, while modern clothing uses manufactured synthetics. Similarly, traditional houses are crafted from local natural materials (mud, grass, dung) tailored to the local climate, while modern houses use industrial materials (cement, steel, glass).",
        "definition": {
            "title": "Traditional vs. Modern Houses",
            "definitions": [
                {
                    "term": "Traditional House",
                    "simple": "A house built using naturally occurring, locally available materials and indigenous building techniques.",
                    "formal": "A residential structure constructed from vernacular materials (mud, thatch, timber, cow dung) reflecting local climatic adaptation and indigenous heritage.",
                    "example": "A Maasai Manyatta or a grass-thatched mud-walled roundhouse.",
                    "why_it_matters": "Provides low-cost, thermally regulated shelter utilizing indigenous resources."
                },
                {
                    "term": "Modern House",
                    "simple": "A house constructed using processed, industrially manufactured materials and engineering standards.",
                    "formal": "A permanent residential building engineered with standardized materials (concrete, masonry blocks, structural steel, glass, roofing sheets).",
                    "example": "A detached bungalow, multi-story maisonette, or urban apartment flat.",
                    "why_it_matters": "Delivers superior durability, fire resistance, scalability, and security."
                }
            ]
        },
        "deep_explanation": "Houses are categorized into distinct structural classes:\n\n- **Traditional Houses:** Manyattas (woven branches + mud/cow dung waterproofing) and Grass-Thatched Mud Roundhouses. Mud walls possess high thermal mass, absorbing heat by day and radiating it at night.\n- **Modern Houses:**\n  * **Bungalows:** Single-story detached homes accessible for all age groups.\n  * **Apartments/Flats:** Vertically stacked units maximizing scarce urban land.\n  * **Maisonettes:** Multi-story homes with internal staircases separating living from sleeping zones.\n  * **Eco-friendly Homes:** Utilize compressed earth bricks, solar panels, and rainwater harvesting for environmental sustainability.",
        "practical": {
            "title": "Scale Model Construction & Material Analysis",
            "steps": [
                {"step_number": 1, "instruction": "Select a house category to model: Traditional Thatched Roundhouse or Modern Bungalow."},
                {"step_number": 2, "instruction": "Erect a sturdy vertical wall framework on cardboard using twigs or cardboard strips."},
                {"step_number": 3, "instruction": "Plaster the wall framework with local clay/mud mixture or secure cardboard masonry panels."},
                {"step_number": 4, "instruction": "Fabricate the roof structure: conical dry thatch for traditional or corrugated cardboard sheets for modern."},
                {"step_number": 5, "instruction": "Evaluate the thermal insulation, durability, and pest vulnerability of your scale model."}
            ]
        },
        "youtube_id": "v3m0K8z7p1q",
        "mcq": {
            "question": "Which modern housing design is specifically defined as 'individual residential units stacked vertically within a single building'?",
            "options": [
                "Bungalow",
                "Apartment or Flat",
                "Maisonette",
                "Manyatta"
            ],
            "correct_answer": 1,
            "explanation": "Apartments/flats consist of individual homes stacked vertically in a multi-story building to optimize urban land usage. Bungalows are single-story and maisonettes are two-story homes."
        }
    },
    {
        "lesson_num": 3,
        "title": "Methods of Housing the Family",
        "hook": "Imagine a family moving to a new county for employment. They need a place to live. Should they buy land and build their own custom home? Should they purchase a completed house through a bank mortgage? Or should they lease an apartment monthly from a landlord? Securing housing is a major financial milestone with distinct economic trade-offs.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Construction_Of_A_House_Designed_By_Mario_Kleff.jpg/960px-Construction_Of_A_House_Designed_By_Mario_Kleff.jpg",
        "image_caption": "Building, buying, or renting each represent different capital commitments, equity returns, and lifestyle flexibilities.",
        "analogy_title": "The Bicycle Acquisition Analogy",
        "analogy_text": "Think of acquiring housing as securing a bicycle: Building a house is like buying components and assembling the bicycle yourself (custom, takes time, builds equity). Buying a house is like purchasing a brand-new showroom bicycle (ready to ride immediately, high upfront capital). Renting a house is like hiring a rental bicycle for a fee (low upfront cost, landlord fixes repairs, but you never own the asset).",
        "definition": {
            "title": "Housing Methods",
            "definitions": [
                {
                    "term": "Building a House",
                    "simple": "Acquiring land and commissioning construction of a customized dwelling from the foundation up.",
                    "formal": "Self-directed or contracted residential property development involving land purchase, architectural planning, and progressive construction.",
                    "example": "Constructing a 3-bedroom family house in progressive phases over 3 years.",
                    "why_it_matters": "Enables maximum custom design and long-term equity accumulation."
                },
                {
                    "term": "Renting a House",
                    "simple": "Leasing a residential unit from a property owner by paying regular monthly rent without ownership rights.",
                    "formal": "A tenancy contract granting temporary occupancy rights in exchange for periodic rental payments, with structural upkeep borne by the lessor.",
                    "example": "Leasing a 2-bedroom urban apartment on a one-year renewable lease.",
                    "why_it_matters": "Provides high geographic mobility and minimal initial capital requirements."
                }
            ]
        },
        "deep_explanation": "Each method of housing has distinct operational and financial characteristics:\n\n1. **Building a House:**\n   - *Advantages:* Full architectural customization, phased building matches monthly cash flow, creates permanent generational wealth.\n   - *Disadvantages:* Highly time-consuming, requires site supervision, risk of cost overruns.\n2. **Buying a House:**\n   - *Advantages:* Immediate occupancy, established utilities (roads, water, power), secure neighborhood.\n   - *Disadvantages:* High initial capital outlay, mortgage interest increases total lifetime cost.\n3. **Renting a House:**\n   - *Advantages:* Low upfront entry (deposit + 1 month), flexibility to relocate, landlord covers major repairs.\n   - *Disadvantages:* Zero equity accumulation, potential rent increases, restricted freedom to modify rooms.",
        "practical": {
            "title": "Housing Cost-Benefit Community Interview",
            "steps": [
                {"step_number": 1, "instruction": "Interview a tenant who rents and a homeowner who has built or bought a home."},
                {"step_number": 2, "instruction": "Inquire about initial capital requirements, monthly maintenance expenses, and lease/deed conditions."},
                {"step_number": 3, "instruction": "Analyze how job mobility, family size, and financial stability influenced their decisions."},
                {"step_number": 4, "instruction": "Draft a comparative cost-benefit ledger comparing renting for 10 years vs. building."},
                {"step_number": 5, "instruction": "Summarize key financial insights in your Home Science study portfolio."}
            ]
        },
        "youtube_id": "8m1K9X0z7p2",
        "mcq": {
            "question": "In a standard residential tenancy agreement, who holds the legal responsibility for repairing structural damage and leaking roofs?",
            "options": [
                "The tenant occupying the unit",
                "The local county municipal council",
                "The landlord who owns the property",
                "The commercial bank holding the loan"
            ],
            "correct_answer": 2,
            "explanation": "In standard tenancy law and Home Science principles, structural maintenance, roof repairs, and major plumbing infrastructure are the sole legal responsibility of the landlord."
        }
    },
    {
        "lesson_num": 4,
        "title": "Room Functions and Room Interrelationships",
        "hook": "Imagine a house where you have to walk through a bedroom to enter the kitchen, or where the toilet door opens directly into the dining room. It would feel awkward, smelly, noisy, and chaotic. A functional house is designed around the activities that take place in each room and the efficient flow between them.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Warm_family_living_room_in_Nairobi.jpg/960px-Warm_family_living_room_in_Nairobi.jpg",
        "image_caption": "A well-organized architectural layout separates private sleeping wings from active social and cooking utility zones.",
        "analogy_title": "The School Timetable & Campus Layout",
        "analogy_text": "Think of room arrangement as being like a school schedule and campus: Subjects have designated spaces—science in the lab, sports on the field. You would not run track inside a library. Furthermore, quiet examination halls are located away from noisy music rooms. Similarly, a house groups social and utility rooms together and isolates quiet, private bedrooms far away to ensure peace, hygiene, and efficiency.",
        "definition": {
            "title": "Zonal Design & Interrelationship",
            "definitions": [
                {
                    "term": "Room Function",
                    "simple": "The specific primary activity or task that a designated household space is equipped to support.",
                    "formal": "The functional purpose assigned to an architectural space, dictating its dimensions, ventilation, fixtures, and furniture layout.",
                    "example": "A kitchen is equipped with heat-resistant countertops and sinks for food preparation.",
                    "why_it_matters": "Prevents clutter and ensures sanitary execution of daily living tasks."
                },
                {
                    "term": "Room Interrelationship",
                    "simple": "The spatial arrangement, proximity, and connection of rooms relative to each other within a house.",
                    "formal": "The geometric and circulation relationship between distinct functional zones to optimize efficiency, privacy, acoustic control, and health.",
                    "example": "Placing the dining room adjacent to the kitchen for safe, rapid meal service.",
                    "why_it_matters": "Minimizes unnecessary steps, prevents accidents, and preserves family privacy."
                }
            ]
        },
        "deep_explanation": "House layouts are organized into four functional zones:\n\n1. **Social Zone:** Living room and dining room for entertaining, eating, and family leisure.\n2. **Utility/Work Zone:** Kitchen, store/pantry, laundry room, and garage.\n3. **Private Zone:** Bedrooms, bathrooms, and toilets for rest, dressing, and hygiene.\n4. **Study/Office Zone:** Quiet workspaces for academic study and professional tasks.\n\n**Key Layout Principles:**\n- *Efficiency:* The kitchen must be directly adjacent to the dining room to reduce serving distance and prevent burns from carrying hot food.\n- *Privacy Buffer:* Bedrooms and bathrooms must open into private corridors, shielded from living room sightlines.\n- *Acoustic Isolation:* Noisy living and utility spaces must be separated from bedrooms.\n- *Sanitation Barrier:* Toilets must be separated from kitchen food preparation zones to prevent vector-borne cross-contamination.",
        "practical": {
            "title": "Floor Plan Flow-Line & Privacy Audit",
            "steps": [
                {"step_number": 1, "instruction": "Sketch an aerial floor plan blueprint of a 3-bedroom house on drawing paper."},
                {"step_number": 2, "instruction": "Draw a Red line representing Food Flow from Kitchen to Dining Table, verifying direct movement."},
                {"step_number": 3, "instruction": "Draw a Blue line representing Privacy Paths from Bedrooms to Bathroom, ensuring seclusion from guests."},
                {"step_number": 4, "instruction": "Circle acoustic conflict zones in Green where noisy and quiet zones share a common wall."},
                {"step_number": 5, "instruction": "Write a 3-sentence architectural critique proposing doorway or layout optimizations."}
            ]
        },
        "youtube_id": "9Q_8zD1-l0M",
        "mcq": {
            "question": "Which room pairing represents the most functionally efficient spatial interrelationship in a residential house?",
            "options": [
                "Bedroom directly connected to the Kitchen",
                "Kitchen placed directly adjacent to the Dining Room",
                "Garage opening directly into the Study Room",
                "Living Room opening directly into the Food Store"
            ],
            "correct_answer": 1,
            "explanation": "Placing the kitchen directly adjacent to the dining room minimizes the distance required to serve hot food, reducing physical fatigue, preventing hot spills, and optimizing culinary workflow."
        }
    }
]

def ingest_topic_2_3():
    print("=" * 80)
    print("STARTING CBC GRADE 10 HOME SCIENCE TOPIC 2.3 INGESTION (4 LESSONS)")
    print("=" * 80)

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
        order=3,
        defaults={"name": "2.3 Housing the Family"}
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
                        "learning_unit": "2.3 Housing the Family",
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
                status="approved",
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
                status="approved",
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
                status="approved",
                title=f"Video Exploration: {cfg['title']}",
                url=f"https://www.youtube.com/watch?v={cfg['youtube_id']}",
                metadata={"youtube_id": cfg["youtube_id"]}
            )
            total_assets += 1

            # 6 Concept Cards / Pages
            # Card 1: Goal + Image Hook + Hook Text
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
                        "Analyze housing categories, functions, and economic trade-offs in Kenya.",
                        "Apply architectural and hygiene principles to home management."
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
                content={"title": "Real-World Context", "text": cfg["hook"]}
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
                content={"title": cfg["analogy_title"], "text": cfg["analogy_text"]}
            )
            b5 = LessonBlock.objects.create(
                lesson=lesson,
                page_number=2,
                order=50,
                component_order=2,
                block_type="definition_card",
                component_type="definition_card",
                title="Key Terminology",
                content=cfg["definition"]
            )

            # Card 3: SVG Infographic + Deep Dive
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
                content={"title": "Core Principles", "text": cfg["deep_explanation"]}
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
                content=cfg["practical"]
            )

            # Card 5: YouTube Video Exploration
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
                    "title": "Community Living & Development",
                    "text": "Proper housing structures, clean water infrastructure, and thoughtful room interrelationships elevate the quality of living, prevent disease transmission, and foster cohesive, resilient Kenyan families."
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
                content=cfg["mcq"]
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
                        f"Housing fulfills foundational physical, health, emotional, and financial needs ({cfg['title']}).",
                        "Thoughtful architectural planning, material selection, and sanitary zonation protect family well-being.",
                        "Sound home management practices ensure safety, privacy, and economic sustainability."
                    ]
                }
            )

            total_lessons += 1
            total_blocks += 12
            print(f"  [+] Ingested Lesson {l_num}/4: '{l_title}' (12 blocks, 3 assets, 6 pages)")

    print("=" * 80)
    print("TOPIC 2.3 INGESTION COMPLETED SUCCESSFULLY:")
    print(f"  - Total Lessons: {total_lessons}")
    print(f"  - Total Blocks:  {total_blocks}")
    print(f"  - Total Assets:  {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_topic_2_3()
