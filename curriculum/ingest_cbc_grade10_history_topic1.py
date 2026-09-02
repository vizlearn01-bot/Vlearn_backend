"""
VLearn CBC Grade 10 History — Topic 1: Linguistic Groups in Kenya
Production Ingestion Script for Lessons 1 through 5
Topic 1.1: Linguistic Groups in Kenya
"""

import os
import sys
import re
from pathlib import Path
from dotenv import load_dotenv

# Set up paths and Django environment
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
load_dotenv(BASE_DIR / ".env")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
import django
django.setup()

from django.db import transaction
from curriculum.models import (
    Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

def clean_text(text: str) -> str:
    """Removes bracket citations and normalizes markdown formatting."""
    if not text:
        return ""
    # Remove bracket citations like [108], [109], [110, 112]
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Remove internal prompt tags if present
    text = re.sub(r'\[(VISUAL|HISTORICAL_CONTEXT|SOURCE ANALYSIS|MISCONCEPTION|MCQ|CRITICAL THINKING|REAL WORLD APPLICATION|SOURCE QUESTION):?[^\]]*\]', '', text)
    # Normalize unicode bullets into standard markdown list items
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    text = re.sub(r'^([^\n\-\*\d\>#][^\n]*)\n(- |\* )', r'\1\n\n\2', text, flags=re.MULTILINE)
    return text.strip()

def clean_dict(data):
    """Recursively cleans all strings in dictionary/list data structures."""
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, dict):
        return {k: clean_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_dict(item) for item in data]
    return data

def sanitize_svg(svg: str) -> str:
    """Cleans up XML headers from SVGs."""
    svg = re.sub(r'<\?xml.*?\?>', '', svg)
    svg = re.sub(r'<!DOCTYPE.*?>', '', svg)
    return svg.strip()

# =====================================================================
# VECTOR SVGS FOR GRADE 10 HISTORY TOPIC 1 (DARK THEME 960x520/640)
# =====================================================================

SVG_LINGUISTIC_CLASSIFICATION = sanitize_svg(r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 560" width="100%" height="auto" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="530" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Kenya's Linguistic Classification: The Three Major Language Families</text>
  <text x="480" y="68" font-size="12.5" fill="#94a3b8" text-anchor="middle">Comparative Taxonomy of Origins, Economic Specializations, Technologies, and Constituent Communities</text>

  <!-- Column 1: Bantu -->
  <g transform="translate(45, 95)">
    <rect width="270" height="375" rx="12" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="270" height="34" rx="8" fill="#059669"/>
    <text x="135" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">BANTU FAMILY</text>
    <text x="135" y="52" font-size="10.5" font-weight="bold" fill="#34d399" text-anchor="middle">Niger-Congo Phylum (~65% of Pop.)</text>
    
    <rect x="15" y="65" width="240" height="1" fill="#10b981" opacity="0.4"/>
    <text x="15" y="82" font-size="10.5" font-weight="bold" fill="#6ee7b7">Origin &amp; Homeland:</text>
    <text x="15" y="98" font-size="9.5" fill="#e2e8f0">&#8226; West Africa / Cameroon-Nigeria</text>
    <text x="15" y="112" font-size="9.5" fill="#e2e8f0">&#8226; Migrated east &amp; south in waves</text>
    
    <text x="15" y="138" font-size="10.5" font-weight="bold" fill="#6ee7b7">Economic Specialization:</text>
    <text x="15" y="154" font-size="9.5" fill="#e2e8f0">&#8226; Settled Agriculture &amp; Farming</text>
    <text x="15" y="168" font-size="9.5" fill="#e2e8f0">&#8226; Iron smelting &amp; Tool forging</text>
    <text x="15" y="182" font-size="9.5" fill="#e2e8f0">&#8226; Pottery (Urewe ware / Kwale ware)</text>
    
    <text x="15" y="208" font-size="10.5" font-weight="bold" fill="#6ee7b7">Primary Settlement Zones:</text>
    <text x="15" y="224" font-size="9.5" fill="#e2e8f0">&#8226; Central Highlands (Mt. Kenya)</text>
    <text x="15" y="238" font-size="9.5" fill="#e2e8f0">&#8226; Coastal Lowlands &amp; Tana River</text>
    <text x="15" y="252" font-size="9.5" fill="#e2e8f0">&#8226; Western Highlands &amp; Lake Basin</text>

    <text x="15" y="278" font-size="10.5" font-weight="bold" fill="#6ee7b7">Example Communities:</text>
    <text x="15" y="294" font-size="9.5" fill="#e2e8f0">&#8226; Agikuyu, Abaluhya, Ameru</text>
    <text x="15" y="308" font-size="9.5" fill="#e2e8f0">&#8226; Abagusii, Akamba, Mijikenda</text>
    <text x="15" y="322" font-size="9.5" fill="#e2e8f0">&#8226; Embu, Taita, Kuria, Pokomo</text>
    
    <rect x="15" y="338" width="240" height="24" rx="4" fill="#047857"/>
    <text x="135" y="354" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Agrarian &amp; Iron Age Pioneers</text>
  </g>

  <!-- Column 2: Nilotic -->
  <g transform="translate(345, 95)">
    <rect width="270" height="375" rx="12" fill="#0c4a6e" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="270" height="34" rx="8" fill="#0284c7"/>
    <text x="135" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">NILOTIC FAMILY</text>
    <text x="135" y="52" font-size="10.5" font-weight="bold" fill="#7dd3fc" text-anchor="middle">Nilo-Saharan Phylum (~30% of Pop.)</text>
    
    <rect x="15" y="65" width="240" height="1" fill="#0ea5e9" opacity="0.4"/>
    <text x="15" y="82" font-size="10.5" font-weight="bold" fill="#38bdf8">Origin &amp; Homeland:</text>
    <text x="15" y="98" font-size="9.5" fill="#e2e8f0">&#8226; Nile Valley / South Sudan Region</text>
    <text x="15" y="112" font-size="9.5" fill="#e2e8f0">&#8226; Moved south along Nile &amp; Rift</text>
    
    <text x="15" y="138" font-size="10.5" font-weight="bold" fill="#38bdf8">Economic Specialization:</text>
    <text x="15" y="154" font-size="9.5" fill="#e2e8f0">&#8226; Pastoralism (Cattle herding)</text>
    <text x="15" y="168" font-size="9.5" fill="#e2e8f0">&#8226; Mixed farming &amp; Riverine fishing</text>
    <text x="15" y="182" font-size="9.5" fill="#e2e8f0">&#8226; Highly mobile livestock husbandry</text>
    
    <text x="15" y="208" font-size="10.5" font-weight="bold" fill="#38bdf8">Three Distinct Sub-Branches:</text>
    <text x="15" y="224" font-size="9.5" fill="#e2e8f0">&#8226; Plains: Maasai, Samburu, Turkana</text>
    <text x="15" y="238" font-size="9.5" fill="#e2e8f0">&#8226; River-Lake: Luo (Lake Victoria basin)</text>
    <text x="15" y="252" font-size="9.5" fill="#e2e8f0">&#8226; Highland: Kalenjin (Nandi, Kipsigis)</text>

    <text x="15" y="278" font-size="10.5" font-weight="bold" fill="#38bdf8">Example Communities:</text>
    <text x="15" y="294" font-size="9.5" fill="#e2e8f0">&#8226; Luo, Maasai, Samburu</text>
    <text x="15" y="308" font-size="9.5" fill="#e2e8f0">&#8226; Kalenjin (Pokot, Tugen, Marakwet)</text>
    <text x="15" y="322" font-size="9.5" fill="#e2e8f0">&#8226; Turkana, Iteso</text>
    
    <rect x="15" y="338" width="240" height="24" rx="4" fill="#0369a1"/>
    <text x="135" y="354" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Pastoralist &amp; Mixed Herders</text>
  </g>

  <!-- Column 3: Cushitic -->
  <g transform="translate(645, 95)">
    <rect width="270" height="375" rx="12" fill="#451a03" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="270" height="34" rx="8" fill="#d97706"/>
    <text x="135" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">CUSHITIC FAMILY</text>
    <text x="135" y="52" font-size="10.5" font-weight="bold" fill="#fcd34d" text-anchor="middle">Afroasiatic Phylum (~4% of Pop.)</text>
    
    <rect x="15" y="65" width="240" height="1" fill="#f59e0b" opacity="0.4"/>
    <text x="15" y="82" font-size="10.5" font-weight="bold" fill="#fbbf24">Origin &amp; Homeland:</text>
    <text x="15" y="98" font-size="9.5" fill="#e2e8f0">&#8226; Horn of Africa (Ethiopia / Somalia)</text>
    <text x="15" y="112" font-size="9.5" fill="#e2e8f0">&#8226; Earliest food producers in Kenya</text>
    
    <text x="15" y="138" font-size="10.5" font-weight="bold" fill="#fbbf24">Economic Specialization:</text>
    <text x="15" y="154" font-size="9.5" fill="#e2e8f0">&#8226; Nomadic Pastoralism (Arid lands)</text>
    <text x="15" y="168" font-size="9.5" fill="#e2e8f0">&#8226; Deep-well water engineering</text>
    <text x="15" y="182" font-size="9.5" fill="#e2e8f0">&#8226; Camels, goats, sheep, hardy cattle</text>
    
    <text x="15" y="208" font-size="10.5" font-weight="bold" fill="#fbbf24">Primary Settlement Zones:</text>
    <text x="15" y="224" font-size="9.5" fill="#e2e8f0">&#8226; Northern Kenya Arid Plains</text>
    <text x="15" y="238" font-size="9.5" fill="#e2e8f0">&#8226; North-Eastern Semi-Arid Scrubland</text>
    <text x="15" y="252" font-size="9.5" fill="#e2e8f0">&#8226; Upper Tana &amp; Chalbi Desert fringe</text>

    <text x="15" y="278" font-size="10.5" font-weight="bold" fill="#fbbf24">Example Communities:</text>
    <text x="15" y="294" font-size="9.5" fill="#e2e8f0">&#8226; Somali, Borana, Rendille</text>
    <text x="15" y="308" font-size="9.5" fill="#e2e8f0">&#8226; Gabbra, Orma, Burji</text>
    <text x="15" y="322" font-size="9.5" fill="#e2e8f0">&#8226; Dahalo (Southern Cushites)</text>
    
    <rect x="15" y="338" width="240" height="24" rx="4" fill="#b45309"/>
    <text x="135" y="354" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Arid Land Pastoral Specialists</text>
  </g>

  <!-- Bottom Clarification Banner -->
  <g transform="translate(45, 485)">
    <rect width="870" height="48" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="435" y="20" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">&#9888; CRITICAL HISTORICAL PRINCIPLE: Linguistic Families &#8800; Biological Races</text>
    <text x="435" y="38" font-size="9" fill="#cbd5e1" text-anchor="middle">These categories classify languages, not biological purity. Kenyan communities have intermarried, assimilated, and traded for centuries.</text>
  </g>
</svg>""")

SVG_PUSHPULL_MIGRATION = sanitize_svg(r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="100%" height="auto" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="510" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Pre-Colonial Migration Dynamics: Push and Pull Model</text>
  <text x="480" y="68" font-size="12.5" fill="#94a3b8" text-anchor="middle">Environmental, Demographic, and Economic Forces Shaping Population Dispersal into Kenya</text>

  <!-- Left: Push Factors -->
  <g transform="translate(45, 95)">
    <rect width="380" height="340" rx="12" fill="#450a0a" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="380" height="34" rx="8" fill="#dc2626"/>
    <text x="190" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">&#8679; PUSH FACTORS (At Original Homelands)</text>

    <g transform="translate(20, 50)">
      <!-- Item 1 -->
      <rect width="340" height="54" rx="6" fill="#1f1315" stroke="#ef4444" stroke-width="1"/>
      <text x="12" y="20" font-size="11" font-weight="bold" fill="#fca5a5">1. Severe Climate Shocks &amp; Droughts</text>
      <text x="12" y="38" font-size="9" fill="#e2e8f0">Drying of rivers, pasture failure, and crop desiccation forced groups outward.</text>

      <!-- Item 2 -->
      <g transform="translate(0, 64)">
        <rect width="340" height="54" rx="6" fill="#1f1315" stroke="#ef4444" stroke-width="1"/>
        <text x="12" y="20" font-size="11" font-weight="bold" fill="#fca5a5">2. Acute Population Pressure</text>
        <text x="12" y="38" font-size="9" fill="#e2e8f0">Rapid demographic growth led to severe land shortages and soil depletion.</text>
      </g>

      <!-- Item 3 -->
      <g transform="translate(0, 128)">
        <rect width="340" height="54" rx="6" fill="#1f1315" stroke="#ef4444" stroke-width="1"/>
        <text x="12" y="20" font-size="11" font-weight="bold" fill="#fca5a5">3. Inter-Clan Warfare &amp; Succession Disputes</text>
        <text x="12" y="38" font-size="9" fill="#e2e8f0">Leadership rivalries and defeats in regional conflicts forced weaker factions to flee.</text>
      </g>

      <!-- Item 4 -->
      <g transform="translate(0, 192)">
        <rect width="340" height="54" rx="6" fill="#1f1315" stroke="#ef4444" stroke-width="1"/>
        <text x="12" y="20" font-size="11" font-weight="bold" fill="#fca5a5">4. Diseases, Epidemics &amp; Epizootics</text>
        <text x="12" y="38" font-size="9" fill="#e2e8f0">Outbreaks of human plagues and livestock diseases (rinderpest) forced evacuation.</text>
      </g>
    </g>
  </g>

  <!-- Center: Flow Connectors -->
  <g transform="translate(435, 190)">
    <path d="M 10 30 L 75 30" fill="none" stroke="#38bdf8" stroke-width="6" stroke-linecap="round"/>
    <polygon points="75,20 90,30 75,40" fill="#38bdf8"/>

    <rect x="5" y="60" width="80" height="50" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="45" y="78" font-size="8.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">CENTURIES-</text>
    <text x="45" y="90" font-size="8.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">LONG</text>
    <text x="45" y="102" font-size="8" fill="#94a3b8" text-anchor="middle">Waves</text>

    <path d="M 10 130 L 75 130" fill="none" stroke="#38bdf8" stroke-width="6" stroke-linecap="round"/>
    <polygon points="75,120 90,130 75,140" fill="#38bdf8"/>
  </g>

  <!-- Right: Pull Factors -->
  <g transform="translate(535, 95)">
    <rect width="380" height="340" rx="12" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="380" height="34" rx="8" fill="#059669"/>
    <text x="190" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">&#8681; PULL FACTORS (Attracting to Kenya)</text>

    <g transform="translate(20, 50)">
      <!-- Item 1 -->
      <rect width="340" height="54" rx="6" fill="#0f291e" stroke="#10b981" stroke-width="1"/>
      <text x="12" y="20" font-size="11" font-weight="bold" fill="#6ee7b7">1. Fertile Arable Soils &amp; Reliable Rainfall</text>
      <text x="12" y="38" font-size="9" fill="#e2e8f0">Volcanic highlands around Mt. Kenya, Aberdares, and Lake Victoria basin.</text>

      <!-- Item 2 -->
      <g transform="translate(0, 64)">
        <rect width="340" height="54" rx="6" fill="#0f291e" stroke="#10b981" stroke-width="1"/>
        <text x="12" y="20" font-size="11" font-weight="bold" fill="#6ee7b7">2. Expansive Pastureland &amp; Water Wells</text>
        <text x="12" y="38" font-size="9" fill="#e2e8f0">Rift Valley grasslands and perennial water sources attracted pastoralists.</text>
      </g>

      <!-- Item 3 -->
      <g transform="translate(0, 128)">
        <rect width="340" height="54" rx="6" fill="#0f291e" stroke="#10b981" stroke-width="1"/>
        <text x="12" y="20" font-size="11" font-weight="bold" fill="#6ee7b7">3. Natural Defensive Terrain</text>
        <text x="12" y="38" font-size="9" fill="#e2e8f0">Forested ridges, caves, and mountain slopes offered security from raiders.</text>
      </g>

      <!-- Item 4 -->
      <g transform="translate(0, 192)">
        <rect width="340" height="54" rx="6" fill="#0f291e" stroke="#10b981" stroke-width="1"/>
        <text x="12" y="20" font-size="11" font-weight="bold" fill="#6ee7b7">4. Regional Barter &amp; Trade Networks</text>
        <text x="12" y="38" font-size="9" fill="#e2e8f0">Flourishing barter networks for iron tools, salt, grain, and cattle products.</text>
      </g>
    </g>
  </g>

  <!-- Bottom Insight -->
  <g transform="translate(45, 450)">
    <rect width="870" height="54" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="435" y="22" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">&#10003; HISTORICAL SYNTHESIS</text>
    <text x="435" y="40" font-size="9.5" fill="#cbd5e1" text-anchor="middle">Migration was a gradual, multi-generational adaptation where families moved, cultivated or grazed, rested, and expanded over centuries.</text>
  </g>
</svg>""")

SVG_MIGRATION_MAP = sanitize_svg(r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 620" width="100%" height="auto" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="590" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Historical Migration Routes into Kenya (Pre-Colonial Era)</text>
  <text x="480" y="68" font-size="12.5" fill="#94a3b8" text-anchor="middle">Spatial Trajectories of Bantu, Nilotic, and Cushitic Communities across East Africa</text>

  <!-- Map Background Panel -->
  <g transform="translate(45, 90)">
    <rect width="570" height="495" rx="12" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>

    <!-- Geographic Outlines (Kenya Region) -->
    <!-- Lake Turkana -->
    <ellipse cx="230" cy="110" rx="20" ry="60" fill="#0284c7" opacity="0.6"/>
    <text x="230" y="115" font-size="8" fill="#ffffff" text-anchor="middle">L. Turkana</text>

    <!-- Lake Victoria -->
    <ellipse cx="90" cy="340" rx="55" ry="70" fill="#0284c7" opacity="0.6"/>
    <text x="90" y="345" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Lake Victoria</text>

    <!-- Indian Ocean Coast -->
    <path d="M 400 480 Q 480 430 520 320 Q 550 200 560 100" fill="none" stroke="#0ea5e9" stroke-width="8" opacity="0.5"/>
    <text x="490" y="450" font-size="10" font-weight="bold" fill="#38bdf8" transform="rotate(-40, 490, 450)">INDIAN OCEAN</text>

    <!-- Mt Kenya Landmark -->
    <polygon points="280,310 290,290 300,310" fill="#f59e0b"/>
    <text x="290" y="325" font-size="8.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">&#9650; Mt. Kenya</text>

    <!-- Mt Elgon Landmark -->
    <polygon points="125,270 135,250 145,270" fill="#f59e0b"/>
    <text x="135" y="285" font-size="8" font-weight="bold" fill="#fbbf24" text-anchor="middle">&#9650; Mt. Elgon</text>

    <!-- Great Rift Valley Corridor -->
    <path d="M 230 180 Q 250 280 270 420" fill="none" stroke="#64748b" stroke-width="16" stroke-dasharray="6,6" opacity="0.3"/>
    <text x="265" y="440" font-size="8.5" fill="#94a3b8" text-anchor="middle">Rift Valley Basin</text>

    <!-- ROUTE 1: BANTU (GREEN) -->
    <!-- From West Africa / Congo basin into Western & Central Kenya -->
    <path d="M 30 260 Q 100 270 150 300" fill="none" stroke="#10b981" stroke-width="4"/>
    <!-- Branch to Central Highlands -->
    <path d="M 150 300 Q 220 310 270 305" fill="none" stroke="#10b981" stroke-width="3.5"/>
    <!-- Branch to Coast / Shungwaya -->
    <path d="M 270 305 Q 360 360 430 430" fill="none" stroke="#10b981" stroke-width="3"/>
    <!-- Coastal Shungwaya southward dispersal -->
    <path d="M 520 220 Q 480 320 440 420" fill="none" stroke="#10b981" stroke-width="3" stroke-dasharray="4,4"/>
    <circle cx="520" cy="220" r="4" fill="#10b981"/>
    <text x="520" y="210" font-size="8.5" font-weight="bold" fill="#34d399" text-anchor="middle">Shungwaya</text>

    <text x="70" y="245" font-size="9.5" font-weight="bold" fill="#34d399">Bantu Route (Western)</text>
    <text x="290" y="280" font-size="8.5" fill="#6ee7b7">Central Highlands (Kikuyu, Meru)</text>
    <text x="420" y="465" font-size="8.5" fill="#6ee7b7">Coastal Bantu (Mijikenda, Pokomo)</text>

    <!-- ROUTE 2: NILOTIC (RED) -->
    <!-- From South Sudan down Nile basin -->
    <path d="M 160 30 Q 180 120 180 200" fill="none" stroke="#ef4444" stroke-width="4"/>
    <!-- River-Lake Nilotes (Luo to Lake Victoria) -->
    <path d="M 180 200 Q 140 260 110 320" fill="none" stroke="#ef4444" stroke-width="3.5"/>
    <!-- Plains Nilotes (Maasai / Samburu down Rift Valley) -->
    <path d="M 180 200 Q 230 290 260 410" fill="none" stroke="#ef4444" stroke-width="3.5"/>
    <!-- Highland Nilotes (Kalenjin to Western Highlands) -->
    <path d="M 180 200 Q 170 260 180 290" fill="none" stroke="#ef4444" stroke-width="3"/>

    <text x="160" y="20" font-size="9.5" font-weight="bold" fill="#f87171">Nilotic Entry (Nile Valley)</text>
    <text x="40" y="380" font-size="8.5" fill="#fca5a5">River-Lake (Luo)</text>
    <text x="270" y="390" font-size="8.5" fill="#fca5a5">Plains (Maasai/Samburu)</text>
    <text x="175" y="315" font-size="8" fill="#fca5a5">Highland (Kalenjin)</text>

    <!-- ROUTE 3: CUSHITIC (BLUE/AMBER) -->
    <!-- From Horn of Africa (Ethiopia/Somalia) into Northern & Eastern Kenya -->
    <path d="M 460 40 Q 380 90 320 160" fill="none" stroke="#f59e0b" stroke-width="4"/>
    <path d="M 320 160 Q 280 210 260 250" fill="none" stroke="#f59e0b" stroke-width="3"/>
    <!-- Eastern Cushites (Somali into NE Kenya) -->
    <path d="M 460 40 Q 480 140 450 250" fill="none" stroke="#f59e0b" stroke-width="3.5"/>

    <text x="470" y="30" font-size="9.5" font-weight="bold" fill="#fbbf24">Cushitic Entry (Horn of Africa)</text>
    <text x="340" y="150" font-size="8.5" fill="#fde68a">Southern &amp; Eastern Cushites</text>
    <text x="465" y="220" font-size="8.5" fill="#fde68a">Somali / Borana / Rendille</text>
  </g>

  <!-- Right Panel: Legend & Analysis -->
  <g transform="translate(635, 90)">
    <rect width="280" height="495" rx="12" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <rect width="280" height="32" rx="8" fill="#1e293b"/>
    <text x="140" y="22" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">MAP LEGEND &amp; ANALYSIS</text>

    <g transform="translate(15, 45)">
      <!-- Bantu Legend -->
      <rect width="250" height="70" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
      <line x1="12" y1="20" x2="45" y2="20" stroke="#10b981" stroke-width="4"/>
      <text x="55" y="24" font-size="10.5" font-weight="bold" fill="#34d399">Bantu Migration (Green)</text>
      <text x="12" y="44" font-size="8.5" fill="#e2e8f0">&#8226; Origin: West Africa / Congo Basin</text>
      <text x="12" y="58" font-size="8.5" fill="#e2e8f0">&#8226; Trajectory: Western, Central, Coast</text>

      <!-- Nilotic Legend -->
      <g transform="translate(0, 80)">
        <rect width="250" height="70" rx="6" fill="#450a0a" stroke="#ef4444" stroke-width="1"/>
        <line x1="12" y1="20" x2="45" y2="20" stroke="#ef4444" stroke-width="4"/>
        <text x="55" y="24" font-size="10.5" font-weight="bold" fill="#f87171">Nilotic Migration (Red)</text>
        <text x="12" y="44" font-size="8.5" fill="#e2e8f0">&#8226; Origin: Nile Valley (South Sudan)</text>
        <text x="12" y="58" font-size="8.5" fill="#e2e8f0">&#8226; Trajectory: Rift Valley &amp; Lake Victoria</text>
      </g>

      <!-- Cushitic Legend -->
      <g transform="translate(0, 160)">
        <rect width="250" height="70" rx="6" fill="#451a03" stroke="#f59e0b" stroke-width="1"/>
        <line x1="12" y1="20" x2="45" y2="20" stroke="#f59e0b" stroke-width="4"/>
        <text x="55" y="24" font-size="10.5" font-weight="bold" fill="#fbbf24">Cushitic Migration (Amber)</text>
        <text x="12" y="44" font-size="8.5" fill="#e2e8f0">&#8226; Origin: Horn of Africa</text>
        <text x="12" y="58" font-size="8.5" fill="#e2e8f0">&#8226; Trajectory: Northern &amp; Eastern Arid Plains</text>
      </g>

      <!-- Pedagogical Note -->
      <g transform="translate(0, 240)">
        <rect width="250" height="195" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="1"/>
        <text x="12" y="20" font-size="10" font-weight="bold" fill="#38bdf8">&#128221; Critical Map Interpretation:</text>
        <text x="12" y="40" font-size="8.5" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#ffffff">Not Straight Highways</tspan>: Arrows show broad generational trends, not single journeys.</text>
        <text x="12" y="80" font-size="8.5" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#ffffff">Modern Counties Transcended</tspan>: Historical migration occurred long before 47 modern county boundaries were established.</text>
        <text x="12" y="130" font-size="8.5" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#ffffff">Meeting Points</tspan>: Areas like Western Kenya and Rift Valley became vibrant melting pots.</text>
        <text x="12" y="175" font-size="8" font-style="italic" fill="#94a3b8">Source: Kenya National Archives &amp; Archaeological Atlas.</text>
      </g>
    </g>
  </g>
</svg>""")

SVG_INTERACTION_NETWORK = sanitize_svg(r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 560" width="100%" height="auto" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="530" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Pre-Colonial Inter-Community Economic &amp; Cultural Exchange Network</text>
  <text x="480" y="68" font-size="12.5" fill="#94a3b8" text-anchor="middle">Symbiotic Highland-Lowland Trade, Cultural Borrowing, Intermarriage, and Peace Covenants</text>

  <!-- Node 1: Bantu Agrarians (Top Left) -->
  <g transform="translate(50, 95)">
    <rect width="250" height="155" rx="10" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
    <rect width="250" height="28" rx="8" fill="#059669"/>
    <text x="125" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">BANTU FARMERS (Highlands)</text>
    
    <text x="12" y="48" font-size="9.5" font-weight="bold" fill="#6ee7b7">&#127806; Goods Offered to Neighbors:</text>
    <text x="12" y="64" font-size="8.5" fill="#e2e8f0">&#8226; Sorghum, millet, sweet potatoes</text>
    <text x="12" y="78" font-size="8.5" fill="#e2e8f0">&#8226; Iron hoes, knives, spears, axes</text>
    <text x="12" y="92" font-size="8.5" fill="#e2e8f0">&#8226; Clay cooking pots &amp; gourds</text>
    <text x="12" y="112" font-size="9.5" font-weight="bold" fill="#6ee7b7">&#129309; Cultural Contributions:</text>
    <text x="12" y="128" font-size="8.5" fill="#e2e8f0">&#8226; Agricultural methods &amp; Iron metallurgy</text>
    <text x="12" y="142" font-size="8.5" fill="#e2e8f0">&#8226; Centralized council structures (Kiama)</text>
  </g>

  <!-- Node 2: Nilotic Pastoralists (Top Right) -->
  <g transform="translate(660, 95)">
    <rect width="250" height="155" rx="10" fill="#0c4a6e" stroke="#0ea5e9" stroke-width="2"/>
    <rect width="250" height="28" rx="8" fill="#0284c7"/>
    <text x="125" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">NILOTIC PASTORALISTS (Plains)</text>
    
    <text x="12" y="48" font-size="9.5" font-weight="bold" fill="#7dd3fc">&#128004; Goods Offered to Neighbors:</text>
    <text x="12" y="64" font-size="8.5" fill="#e2e8f0">&#8226; Cattle, sheep, goats, hides</text>
    <text x="12" y="78" font-size="8.5" fill="#e2e8f0">&#8226; Milk, butter/ghee, meat, leather</text>
    <text x="12" y="92" font-size="8.5" fill="#e2e8f0">&#8226; River/lake fish (Luo in Nyanza)</text>
    <text x="12" y="112" font-size="9.5" font-weight="bold" fill="#7dd3fc">&#129309; Cultural Contributions:</text>
    <text x="12" y="128" font-size="8.5" fill="#e2e8f0">&#8226; Age-set social organizations</text>
    <text x="12" y="142" font-size="8.5" fill="#e2e8f0">&#8226; Pastoralist loanwords &amp; Military tactics</text>
  </g>

  <!-- Central Exchange Hub (Center) -->
  <g transform="translate(330, 110)">
    <rect width="300" height="220" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect width="300" height="30" rx="8" fill="#d97706"/>
    <text x="150" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">&#9878; THE BORDERLAND EXCHANGE HUB</text>

    <!-- Connecting Arrows -->
    <text x="150" y="55" font-size="10.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">1. BARTER COMMERCE</text>
    <text x="150" y="72" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Highland grains traded for lowland milk &amp; meat.</text>
    <text x="150" y="86" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Vital survival safety net during droughts.</text>

    <text x="150" y="112" font-size="10.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">2. INTERMARRIAGE ALLIANCES</text>
    <text x="150" y="128" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Kikuyu-Maasai &amp; Luo-Luhya marriages</text>
    <text x="150" y="142" font-size="8.5" fill="#cbd5e1" text-anchor="middle">fostered peace covenants and bilingual families.</text>

    <text x="150" y="168" font-size="10.5" font-weight="bold" fill="#34d399" text-anchor="middle">3. ELDERS' DIPLOMACY</text>
    <text x="150" y="184" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Traditional treaties enforced strictly: women &amp; children</text>
    <text x="150" y="198" font-size="8.5" fill="#cbd5e1" text-anchor="middle">could trade safely even during warrior border skirmishes.</text>
  </g>

  <!-- Node 3: Cushitic Pastoralists (Bottom Left) -->
  <g transform="translate(50, 275)">
    <rect width="250" height="155" rx="10" fill="#451a03" stroke="#f59e0b" stroke-width="2"/>
    <rect width="250" height="28" rx="8" fill="#b45309"/>
    <text x="125" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">CUSHITIC TRADERS (Drylands)</text>
    
    <text x="12" y="48" font-size="9.5" font-weight="bold" fill="#fde68a">&#128042; Goods Offered to Neighbors:</text>
    <text x="12" y="64" font-size="8.5" fill="#e2e8f0">&#8226; Camels, goats, rock salt, hides</text>
    <text x="12" y="78" font-size="8.5" fill="#e2e8f0">&#8226; Incense, herbal resins, leather goods</text>
    <text x="12" y="92" font-size="8.5" fill="#e2e8f0">&#8226; Desert navigation &amp; deep-well tech</text>
    <text x="12" y="112" font-size="9.5" font-weight="bold" fill="#fde68a">&#129309; Cultural Contributions:</text>
    <text x="12" y="128" font-size="8.5" fill="#e2e8f0">&#8226; Lunar calendar calculations</text>
    <text x="12" y="142" font-size="8.5" fill="#e2e8f0">&#8226; Age-set systems shared with Bantu</text>
  </g>

  <!-- Node 4: Coastal & Riverine Networks (Bottom Right) -->
  <g transform="translate(660, 275)">
    <rect width="250" height="155" rx="10" fill="#3b0764" stroke="#a855f7" stroke-width="2"/>
    <rect width="250" height="28" rx="8" fill="#7e22ce"/>
    <text x="125" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">COASTAL &amp; INTERIOR CARAVANS</text>
    
    <text x="12" y="48" font-size="9.5" font-weight="bold" fill="#d8b4fe">&#128736; Long-Distance Exchange:</text>
    <text x="12" y="64" font-size="8.5" fill="#e2e8f0">&#8226; Marine salt, cowrie shells, cloth</text>
    <text x="12" y="78" font-size="8.5" fill="#e2e8f0">&#8226; Glass beads, copper wire, pottery</text>
    <text x="12" y="92" font-size="8.5" fill="#e2e8f0">&#8226; Ivory, honey, beeswax, grain</text>
    <text x="12" y="112" font-size="9.5" font-weight="bold" fill="#d8b4fe">&#129309; Cultural Contributions:</text>
    <text x="12" y="128" font-size="8.5" fill="#e2e8f0">&#8226; Emergence of Kiswahili trade lingua</text>
    <text x="12" y="142" font-size="8.5" fill="#e2e8f0">&#8226; Regional market days (*Gikuyu / Kamba*)</text>
  </g>

  <!-- Connecting Lines with Labels -->
  <!-- Top Left to Center -->
  <path d="M 300 170 L 330 170" fill="none" stroke="#10b981" stroke-width="3"/>
  <!-- Top Right to Center -->
  <path d="M 660 170 L 630 170" fill="none" stroke="#0ea5e9" stroke-width="3"/>
  <!-- Bottom Left to Center -->
  <path d="M 300 350 L 330 310" fill="none" stroke="#f59e0b" stroke-width="3"/>
  <!-- Bottom Right to Center -->
  <path d="M 660 350 L 630 310" fill="none" stroke="#a855f7" stroke-width="3"/>

  <!-- Bottom Insight Panel -->
  <g transform="translate(50, 460)">
    <rect width="860" height="60" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="430" y="24" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">&#10024; ECOLOGICAL COMPLEMENTARITY</text>
    <text x="430" y="44" font-size="9.5" fill="#cbd5e1" text-anchor="middle">Highland farmers and lowland pastoralists were not enemies in permanent isolation, but symbiotic partners whose survival depended on mutual trade and peace covenants.</text>
  </g>
</svg>""")

SVG_COHESION_WHEEL = sanitize_svg(r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 560" width="100%" height="auto" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="530" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Cohesion Wheel: Pillars of National Unity in Diversity</text>
  <text x="480" y="68" font-size="12.5" fill="#94a3b8" text-anchor="middle">Constitutional and Civic Framework for Promoting Social Cohesion and Valuing Kenya's Diversity</text>

  <!-- Central Hub -->
  <g transform="translate(480, 275)">
    <!-- Outer Glow Circle -->
    <circle cx="0" cy="0" r="105" fill="#1e1b4b" stroke="#6366f1" stroke-width="3"/>
    <circle cx="0" cy="0" r="90" fill="#312e81" stroke="#818cf8" stroke-width="2"/>
    <text x="0" y="-35" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">&#127472;&#127466; SHARED</text>
    <text x="0" y="-18" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">NATIONAL IDENTITY</text>
    <text x="0" y="2" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">&amp; CITIZENSHIP</text>
    <line x1="-60" y1="12" x2="60" y2="12" stroke="#818cf8" stroke-width="1"/>
    <text x="0" y="28" font-size="8.5" fill="#e2e8f0" text-anchor="middle">Article 10 Values:</text>
    <text x="0" y="42" font-size="8" fill="#cbd5e1" text-anchor="middle">Democracy, Equity,</text>
    <text x="0" y="56" font-size="8" fill="#cbd5e1" text-anchor="middle">Human Dignity &amp; Unity</text>
  </g>

  <!-- Pillar 1: Intercultural Dialogue (Top) -->
  <g transform="translate(380, 95)">
    <rect width="200" height="75" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
    <text x="100" y="20" font-size="10.5" font-weight="bold" fill="#34d399" text-anchor="middle">1. Intercultural Dialogue</text>
    <text x="10" y="38" font-size="8.5" fill="#e2e8f0">&#8226; Open multi-ethnic forums</text>
    <text x="10" y="52" font-size="8.5" fill="#e2e8f0">&#8226; Dismantling negative stereotypes</text>
    <text x="10" y="66" font-size="8.5" fill="#e2e8f0">&#8226; Fostering mutual respect</text>
  </g>
  <!-- Connector 1 -->
  <line x1="480" y1="170" x2="480" y2="185" stroke="#10b981" stroke-width="3" stroke-dasharray="3,3"/>

  <!-- Pillar 2: Equitable Resource Distribution (Top Right) -->
  <g transform="translate(680, 160)">
    <rect width="220" height="75" rx="8" fill="#0c4a6e" stroke="#0ea5e9" stroke-width="1.5"/>
    <text x="110" y="20" font-size="10.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">2. Equitable Distribution</text>
    <text x="10" y="38" font-size="8.5" fill="#e2e8f0">&#8226; Fair devolution of public funds</text>
    <text x="10" y="52" font-size="8.5" fill="#e2e8f0">&#8226; Ending regional marginalization</text>
    <text x="10" y="66" font-size="8.5" fill="#e2e8f0">&#8226; Equal infrastructure access</text>
  </g>
  <!-- Connector 2 -->
  <line x1="680" y1="220" x2="570" y2="250" stroke="#0ea5e9" stroke-width="3" stroke-dasharray="3,3"/>

  <!-- Pillar 3: Celebrating Cultural Diversity (Bottom Right) -->
  <g transform="translate(680, 330)">
    <rect width="220" height="75" rx="8" fill="#451a03" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="110" y="20" font-size="10.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">3. Valuing Cultural Diversity</text>
    <text x="10" y="38" font-size="8.5" fill="#e2e8f0">&#8226; Preserving indigenous languages</text>
    <text x="10" y="52" font-size="8.5" fill="#e2e8f0">&#8226; Music, drama &amp; heritage festivals</text>
    <text x="10" y="66" font-size="8.5" fill="#e2e8f0">&#8226; Diversity as national strength</text>
  </g>
  <!-- Connector 3 -->
  <line x1="680" y1="350" x2="570" y2="300" stroke="#f59e0b" stroke-width="3" stroke-dasharray="3,3"/>

  <!-- Pillar 4: Civic Education & History (Bottom Left) -->
  <g transform="translate(60, 330)">
    <rect width="220" height="75" rx="8" fill="#3b0764" stroke="#a855f7" stroke-width="1.5"/>
    <text x="110" y="20" font-size="10.5" font-weight="bold" fill="#c084fc" text-anchor="middle">4. Multi-Ethnic Civic Education</text>
    <text x="10" y="38" font-size="8.5" fill="#e2e8f0">&#8226; Teaching interconnected history</text>
    <text x="10" y="52" font-size="8.5" fill="#e2e8f0">&#8226; Cultivating shared patriotism</text>
    <text x="10" y="66" font-size="8.5" fill="#e2e8f0">&#8226; Critical thinking against tribalism</text>
  </g>
  <!-- Connector 4 -->
  <line x1="280" y1="350" x2="390" y2="300" stroke="#a855f7" stroke-width="3" stroke-dasharray="3,3"/>

  <!-- Pillar 5: Human Rights & Rule of Law (Top Left) -->
  <g transform="translate(60, 160)">
    <rect width="220" height="75" rx="8" fill="#1f2937" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="110" y="20" font-size="10.5" font-weight="bold" fill="#f1f5f9" text-anchor="middle">5. Rule of Law &amp; Inclusivity</text>
    <text x="10" y="38" font-size="8.5" fill="#e2e8f0">&#8226; National Cohesion 1/3 Ethnic Rule</text>
    <text x="10" y="52" font-size="8.5" fill="#e2e8f0">&#8226; Non-discrimination in hiring</text>
    <text x="10" y="66" font-size="8.5" fill="#e2e8f0">&#8226; Equal constitutional protection</text>
  </g>
  <!-- Connector 5 -->
  <line x1="280" y1="220" x2="390" y2="250" stroke="#94a3b8" stroke-width="3" stroke-dasharray="3,3"/>

  <!-- Bottom Clarification Banner -->
  <g transform="translate(45, 465)">
    <rect width="870" height="55" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="435" y="22" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">&#10004; CORE CIVIC PRINCIPLE: Unity in Diversity vs Forced Assimilation</text>
    <text x="435" y="42" font-size="9" fill="#cbd5e1" text-anchor="middle">True social cohesion does NOT mean erasing mother tongues or cultural identities. It means celebrating distinct cultures under a shared constitutional allegiance.</text>
  </g>
</svg>""")

SVG_HISTORICAL_TRIANGULATION = sanitize_svg(r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="100%" height="auto" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="510" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Historical Triangulation: Reconstructing Pre-Colonial History</text>
  <text x="480" y="68" font-size="12.5" fill="#94a3b8" text-anchor="middle">Synthesizing Oral Traditions, Historical Linguistics, and Archaeological Science</text>

  <!-- Triangle Nodes -->
  <!-- Top Node: Oral Traditions -->
  <g transform="translate(345, 95)">
    <rect width="270" height="110" rx="10" fill="#451a03" stroke="#f59e0b" stroke-width="2"/>
    <rect width="270" height="26" rx="6" fill="#d97706"/>
    <text x="135" y="18" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">&#128483; 1. ORAL TRADITIONS</text>
    <text x="10" y="44" font-size="8.5" fill="#fde68a">&#8226; <tspan font-weight="bold">Evidence</tspan>: Spoken stories, clan genealogies, elders' memories</text>
    <text x="10" y="60" font-size="8.5" fill="#fde68a">&#8226; <tspan font-weight="bold">Strength</tspan>: Explains motives, alliances, feelings &amp; values</text>
    <text x="10" y="76" font-size="8.5" fill="#fde68a">&#8226; <tspan font-weight="bold">Limitation</tspan>: Memory decay, omission, chronological telescoping</text>
  </g>

  <!-- Bottom Left Node: Historical Linguistics -->
  <g transform="translate(45, 305)">
    <rect width="270" height="115" rx="10" fill="#0c4a6e" stroke="#0ea5e9" stroke-width="2"/>
    <rect width="270" height="26" rx="6" fill="#0284c7"/>
    <text x="135" y="18" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">&#128218; 2. HISTORICAL LINGUISTICS</text>
    <text x="10" y="44" font-size="8.5" fill="#7dd3fc">&#8226; <tspan font-weight="bold">Evidence</tspan>: Shared vocabulary, loanwords, dialect evolution</text>
    <text x="10" y="60" font-size="8.5" fill="#7dd3fc">&#8226; <tspan font-weight="bold">Strength</tspan>: Traces ancient contact zones &amp; cultural borrowing</text>
    <text x="10" y="76" font-size="8.5" fill="#7dd3fc">&#8226; <tspan font-weight="bold">Limitation</tspan>: Cannot provide precise calendar dates</text>
  </g>

  <!-- Bottom Right Node: Archaeology -->
  <g transform="translate(645, 305)">
    <rect width="270" height="115" rx="10" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
    <rect width="270" height="26" rx="6" fill="#059669"/>
    <text x="135" y="18" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">&#9874; 3. ARCHAEOLOGY</text>
    <text x="10" y="44" font-size="8.5" fill="#6ee7b7">&#8226; <tspan font-weight="bold">Evidence</tspan>: Urewe potsherds, iron slag, animal bones, burial sites</text>
    <text x="10" y="60" font-size="8.5" fill="#6ee7b7">&#8226; <tspan font-weight="bold">Strength</tspan>: Provides physical artifacts &amp; scientific carbon dating</text>
    <text x="10" y="76" font-size="8.5" fill="#6ee7b7">&#8226; <tspan font-weight="bold">Limitation</tspan>: Cannot reveal spoken language or social identity directly</text>
  </g>

  <!-- Central Corroboration Hub -->
  <g transform="translate(365, 235)">
    <circle cx="115" cy="65" r="75" fill="#1e1b4b" stroke="#818cf8" stroke-width="2.5"/>
    <text x="115" y="45" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">&#127919; CORROBORATED</text>
    <text x="115" y="62" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">HISTORICAL</text>
    <text x="115" y="78" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">TRUTH</text>
    <text x="115" y="96" font-size="8" fill="#38bdf8" text-anchor="middle">Synthesized Evidence</text>
  </g>

  <!-- Triangulation Arrows -->
  <path d="M 430 205 L 450 240" fill="none" stroke="#f59e0b" stroke-width="3" stroke-dasharray="3,3"/>
  <path d="M 315 340 L 375 315" fill="none" stroke="#0ea5e9" stroke-width="3" stroke-dasharray="3,3"/>
  <path d="M 645 340 L 585 315" fill="none" stroke="#10b981" stroke-width="3" stroke-dasharray="3,3"/>

  <!-- Bottom Takeaway -->
  <g transform="translate(45, 445)">
    <rect width="870" height="55" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="435" y="22" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">&#128269; THE HISTORICAL INQUIRY METHOD</text>
    <text x="435" y="42" font-size="9" fill="#cbd5e1" text-anchor="middle">No single source is complete on its own. Reliable history is constructed when oral narratives, linguistic loanwords, and archaeological excavations corroborate one another.</text>
  </g>
</svg>""")


# =====================================================================
# LESSON DATA SPECIFICATION (5 LESSONS x 6 PAGES ATOMIC CARDS)
# =====================================================================

def build_grade10_history_topic1_curriculum():
    return [
        # =====================================================================
        # LESSON 1: Kenya’s Major Linguistic Families
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Kenya’s Major Linguistic Families",
            "unit_description": "Classification of Kenya’s population into Bantu, Nilotic, and Cushitic language families; points of origin, economic specializations, technology, and oral tradition analysis.",
            "lesson_title": "Kenya’s Major Linguistic Families",
            "pages": [
                # Page 1: Orientation & Continental Roots
                [
                    {
                        "type": "suggested_image",
                        "title": "Continental Distribution of African Language Families",
                        "content": {
                            "title": "Continental Distribution of African Language Families",
                            "caption": "Map showing the broad continental distribution of major African language families: Niger-Congo (Bantu), Nilo-Saharan (Nilotic), and Afroasiatic (Cushitic).",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Language_families_of_Africa.svg/1024px-Language_families_of_Africa.svg.png",
                            "author": "Wikimedia Commons / Mark Dingemanse",
                            "licensing": "CC BY-SA 2.5"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Linguistic Families of Kenya",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify Kenya’s **three major linguistic families**: Bantu, Nilotic, and Cushitic.",
                                "Trace the **historical regions of origin** for each linguistic group across the African continent.",
                                "Analyze the relationship between **material culture/technology** (agriculture, ironworking, pastoralism) and linguistic groups.",
                                "Distinguish clearly between **linguistic categorization** and biological or racial concepts."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Kenya as a Historical Crossroads",
                        "content": {
                            "title": "A Confluence of African Civilizations",
                            "text": "Kenya occupies a unique geographic position at the intersection of Eastern, Central, and Northern Africa. Over several millennia, communities from diverse ecological regions migrated into the Kenyan territory, creating one of the most culturally vibrant and linguistically diverse nations on earth.\n\n- **Linguistic Evidence**: In the absence of early written records, language classification provides historians with powerful scientific clues to trace migration routes, trade alliances, and shared cultural ancestry.\n- **Three Language Phyla**: Virtually all indigenous Kenyan languages belong to three distinct African language phyla: **Niger-Congo (Bantu)**, **Nilo-Saharan (Nilotic)**, and **Afroasiatic (Cushitic)**."
                        }
                    }
                ],

                # Page 2: Core Knowledge — The Three Linguistic Families
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Three Major Linguistic Families in Detail",
                        "content": {
                            "title": "Bantu, Nilotic, and Cushitic Characteristics",
                            "text": "1. **The Bantu Group (Niger-Congo Phylum)**:\n   - **Origins**: Originated in the West African borderland between modern Cameroon and Nigeria.\n   - **Economic Mode**: Practiced sedentary agriculture (sorghum, millet, yams) and developed advanced iron smelting technologies.\n   - **Representative Communities**: Agikuyu, Abaluhya, Abagusii, Ameru, Mijikenda, Akamba, Embu, and Taita.\n\n2. **The Nilotic Group (Nilo-Saharan Phylum)**:\n   - **Origins**: Originated in the Nile Valley / Bahr el Ghazal region of South Sudan.\n   - **Economic Mode**: Strong pastoralist traditions (cattle herding), alongside mixed agriculture and lake/river fishing.\n   - **Three Branches**: *Plains Nilotes* (Maasai, Samburu, Turkana, Iteso), *River-Lake Nilotes* (Luo), and *Highland Nilotes* (Kalenjin groups: Kipsigis, Nandi, Pokot, Tugen).\n\n3. **The Cushitic Group (Afroasiatic Phylum)**:\n   - **Origins**: Originated in the Horn of Africa (modern-day Ethiopia and Somalia).\n   - **Economic Mode**: Specialized nomadic pastoralism (camels, goats, sheep, hardy cattle) and advanced deep-well water conservation.\n   - **Representative Communities**: Somali, Borana, Rendille, Gabbra, Orma, Burji, and Dahalo."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comparative Matrix of Kenya’s Three Linguistic Families",
                        "content": {
                            "title": "Linguistic Families Summary Matrix",
                            "headers": ["Linguistic Family", "African Phylum", "Region of Origin", "Primary Economic Practice", "Example Communities in Kenya"],
                            "rows": [
                                ["Bantu", "Niger-Congo", "West Africa (Cameroon/Nigeria)", "Agriculture, Ironworking, Pottery", "Agikuyu, Abaluhya, Abagusii, Ameru, Mijikenda, Akamba"],
                                ["Nilotic", "Nilo-Saharan", "Nile Valley (South Sudan)", "Pastoralism, Mixed Farming, Fishing", "Luo, Maasai, Samburu, Kalenjin (Nandi, Kipsigis), Turkana"],
                                ["Cushitic", "Afroasiatic", "Horn of Africa (Ethiopia/Somalia)", "Nomadic Pastoralism (Camels/Goats), Deep Wells", "Somali, Borana, Rendille, Gabbra, Orma, Burji"]
                            ]
                        }
                    }
                ],

                # Page 3: Visual Classification Matrix
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Kenya’s Linguistic Classification Matrix",
                        "content": {
                            "title": "Kenya’s Linguistic Classification Matrix",
                            "caption": "Three-column structural matrix classifying Bantu, Nilotic, and Cushitic groups by origins, economic modes, technologies, and constituent communities.",
                            "svg_content": SVG_LINGUISTIC_CLASSIFICATION
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Language Classification vs Biological Fluidity",
                        "content": {
                            "title": "Why Language Is Not Race",
                            "text": "It is essential to understand that terms such as 'Bantu', 'Nilotic', and 'Cushitic' are strictly **linguistic classifications**, not biological races or closed genetic categories.\n\n- **Linguistic Borrowing**: Communities living adjacent to each other regularly adopted words, social customs, and circumcision rituals from their neighbors.\n- **Intermarriage & Fluidity**: Centuries of inter-ethnic marriage meant that biological backgrounds constantly intermingled, while languages evolved dynamically through contact."
                        }
                    }
                ],

                # Page 4: Source Analysis & Material Culture
                [
                    {
                        "type": "suggested_image",
                        "title": "Early Iron Age Forged Tools and Agricultural Implements",
                        "content": {
                            "title": "Early Iron Age Forged Tools and Agricultural Implements",
                            "caption": "Early Iron Age agricultural tools forged by early farming communities, showcasing the technological basis of settled agriculture and forest clearing.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Bantu_expansion_iron_tools.jpg/1024px-Bantu_expansion_iron_tools.jpg",
                            "author": "Wikimedia Commons / World History Archive",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Source Analysis: Oral Tradition Extract of Bantu Migration",
                        "content": {
                            "title": "Analyzing an Oral Tradition of Migration",
                            "task": "Read the oral testimony preserved by community elders:\n\n*\"Our elders tell us that a long time ago, our people lived in a land far to the west where the big rivers flow. When the land became crowded and the rains failed, our ancestors began a slow journey toward the rising sun. They carried their seeds and their iron tools, settling down to clear the forests and plant crops whenever they found fertile soil.\"*\n\n**Investigative Questions**:\n1. What specific economic activities and technologies are identified in this oral tradition?\n2. What push factors forced the ancestors to leave their western homeland?\n3. What are the strengths and limitations of relying on oral tradition to reconstruct history?",
                            "materials": ["Notebook", "Pen", "Source Text"],
                            "safety": "Synthesize historical facts objectively using evidence."
                        }
                    }
                ],

                # Page 5: Video Exploration & Common Misconceptions
                [
                    {
                        "type": "suggested_video",
                        "title": "African Language Families and East African Linguistic Origins",
                        "content": {
                            "title": "African Language Families and East African Linguistic Origins",
                            "description": "Comprehensive educational documentary breaking down the Niger-Congo, Nilo-Saharan, and Afroasiatic language phyla in East Africa and their historical migrations.",
                            "youtube_id": "3JtT3qGf1Ew",
                            "url": "https://www.youtube.com/watch?v=3JtT3qGf1Ew"
                        }
                    },
                    {
                        "type": "common_misconception",
                        "title": "Misconception: Linguistic Groups as Homogeneous Races",
                        "content": {
                            "misconception": "The terms 'Bantu', 'Nilote', or 'Cushite' refer to distinct biological races or completely uniform tribes.",
                            "correction": "These terms refer to linguistic language families. Within each family, distinct communities possess unique political systems, traditions, and dialects. Furthermore, extensive historical intermarriage, trade, and cultural assimilation created fluid, multi-layered identities rather than rigid genetic boxes."
                        }
                    }
                ],

                # Page 6: Assessment & Review
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Kenya's Linguistic Groups",
                        "content": {
                            "question": "Which of the following represents the largest linguistic family in Kenya?",
                            "options": [
                                "Cushitic",
                                "Nilotic",
                                "Bantu",
                                "Semitic"
                            ],
                            "correct": "C",
                            "explanation": "The Bantu language family constitutes the largest linguistic group in Kenya (accounting for approximately 65% of the total population), followed by the Nilotes and Cushites."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Nilotic Classification",
                        "content": {
                            "question": "A student incorrectly categorizes the Maasai and Kalenjin into the Cushitic family. Why is this categorization historically and linguistically flawed?",
                            "options": [
                                "The Maasai and Kalenjin originated in West Africa and belong to the Bantu family",
                                "They originated in the Nile Valley (South Sudan region) and belong to the Nilotic family",
                                "They migrated from the Arabian peninsula and speak Semitic dialects",
                                "They are purely hunter-gatherer communities without any linguistic classification"
                            ],
                            "correct": "B",
                            "explanation": "The Maasai (Plains Nilotes) and Kalenjin (Highland Nilotes) originated in the Nile Valley and belong to the Nilotic language family, whereas Cushitic groups originated in the Horn of Africa."
                        }
                    },
                    {
                        "type": "summary_card",
                        "title": "Key Takeaways: Lesson 1 Recap",
                        "content": {
                            "title": "Summary of Core Concepts",
                            "text": "- **Three Major Language Families**: Kenya’s population is classified into **Bantu** (Niger-Congo), **Nilotic** (Nilo-Saharan), and **Cushitic** (Afroasiatic).\n- **Distinct Origins**: Bantu migrated from West Africa; Nilotes from the Nile Valley; Cushites from the Horn of Africa.\n- **Economic Adaptations**: Bantu introduced settled agriculture and iron smelting; Nilotes specialized in cattle pastoralism and fishing; Cushites mastered arid-land livestock husbandry.\n- **Linguistic, Not Biological**: Language families reflect shared linguistic roots, not genetic isolation."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Migration, Settlement, and Expansion
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Migration, Settlement, and Expansion",
            "unit_description": "Push and pull factors driving pre-colonial migrations into Kenya; spatial routes, regional settlement patterns, environmental adaptation, and archaeological corroboration.",
            "lesson_title": "Migration, Settlement, and Expansion",
            "pages": [
                # Page 1: Orientation & Objectives
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Migration Dynamics",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain the **push and pull factors** that triggered pre-colonial migrations into Kenya.",
                                "Trace the **geographical routes and settlement zones** of Bantu, Nilotic, and Cushitic groups on a historical map.",
                                "Analyze how migrant communities **adapted economically to different environmental zones**.",
                                "Interpret **archaeological and material evidence** (such as Urewe pottery and cattle bones) to corroborate migration timelines."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Nature of Multi-Generational Migration",
                        "content": {
                            "title": "Migration as a Gradual Historical Process",
                            "text": "Human migration in pre-colonial Africa was rarely a single, rapid military invasion. Instead, it was a **slow, multi-generational process** of gradual movement, seasonal scouting, settlement, and subsequent expansion over hundreds of years.\n\n- **Stepping-Stone Dispersal**: Groups would settle in an area, cultivate crops or graze herds for several decades, and as their population expanded or climatic conditions altered, splinter groups would move further into new frontiers.\n- **Ecological Niches**: Migrants actively sought ecological zones that matched their primary production systems—farmers sought fertile, well-watered soils, while pastoralists sought savanna grasslands."
                        }
                    }
                ],

                # Page 2: Push and Pull Dynamics
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Push-Pull Migration Dynamics Flowchart",
                        "content": {
                            "title": "Push-Pull Migration Dynamics Flowchart",
                            "caption": "Flowchart illustrating environmental, demographic, and political push factors alongside agricultural, pastoral, and commercial pull factors.",
                            "svg_content": SVG_PUSHPULL_MIGRATION
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Detailed Analysis of Push and Pull Factors",
                        "content": {
                            "title": "The Drivers of Population Movement",
                            "text": "Pre-colonial migrations into Kenya were shaped by a dynamic interplay of push and pull factors:\n\n1. **Push Factors (Factors driving groups away from original homelands)**:\n   - **Population Pressure**: Demographic expansion caused acute land scarcity and resource competition.\n   - **Drought and Climate Change**: Periodic desertification and drying of river basins forced groups to search for water.\n   - **Internal and External Conflicts**: Rivalries over chieftaincy, succession disputes, and attacks by stronger neighbors.\n   - **Diseases and Epizootics**: Outbreaks of human epidemics and livestock plagues like rinderpest.\n\n2. **Pull Factors (Factors attracting groups toward Kenya)**:\n   - **Fertile Arable Soils**: Rich volcanic soils and reliable rainfall in the central highlands and Lake Victoria basin.\n   - **Abundant Savanna Pastures**: Lush grazing lands in the Great Rift Valley.\n   - **Natural Security & Defensibility**: Mountain ranges and forested highlands offering refuge from raiders.\n   - **Regional Trade Opportunities**: Access to thriving barter networks for iron tools, salt, and grain."
                        }
                    }
                ],

                # Page 3: Migration Routes & Settlement Patterns
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Historical Migration Routes Map into Kenya",
                        "content": {
                            "title": "Historical Migration Routes Map into Kenya",
                            "caption": "High-precision vector map showing the migration corridors of the Bantu (Green), Nilotes (Red), and Cushites (Amber) into Kenya's ecological zones.",
                            "svg_content": SVG_MIGRATION_MAP
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Spatial Routes and Settlement Patterns",
                        "content": {
                            "title": "Where the Communities Settled",
                            "text": "1. **Bantu Migration Routes**:\n   - **Western Route**: Moved through the Interlacustrine region into Western Kenya, giving rise to the Abaluhya, Abagusii, and Kuria.\n   - **Eastern & Coastal Route**: Dispersed around Mt. Kenya (Agikuyu, Ameru, Embu, Akamba) and along the coast via Shungwaya (Mijikenda, Pokomo, Taita).\n\n2. **Nilotic Migration Routes**:\n   - **River-Lake Nilotes (Luo)**: Followed the Nile basin south into Uganda before entering the Lake Victoria basin in Nyanza.\n   - **Plains Nilotes (Maasai, Samburu, Turkana)**: Moved straight down the Great Rift Valley corridor and northwestern plains.\n   - **Highland Nilotes (Kalenjin)**: Settled in the western highlands and Mau escarpment.\n\n3. **Cushitic Migration Routes**:\n   - Moved south from the Ethiopian highlands and Somali peninsula into the arid and semi-arid plains of northern and northeastern Kenya."
                        }
                    }
                ],

                # Page 4: Archaeological Evidence & Source Analysis
                [
                    {
                        "type": "suggested_image",
                        "title": "Excavated Urewe Ware Pottery Vessel from Lake Victoria Basin",
                        "content": {
                            "title": "Excavated Urewe Ware Pottery Vessel from Lake Victoria Basin",
                            "caption": "Excavated Urewe Ware pottery vessel from Western Kenya, demonstrating Early Iron Age settled farming and metallurgy.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Urewe_pottery_vessel_East_Africa.jpg/1024px-Urewe_pottery_vessel_East_Africa.jpg",
                            "author": "Wikimedia Commons / East African Archaeological Survey",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Archaeological Source Analysis: Pottery and Cattle Bones",
                        "content": {
                            "title": "Corroborating Material Remains with Oral History",
                            "task": "Examine the archaeological findings from a Western Kenya excavation site:\n\n*Archaeologists discovered distinct layers containing Bantu 'Urewe ware' pottery fragments, iron smelting slag, and carbonized sorghum grains, immediately adjacent to cattle bone middens associated with early Nilotic pastoral encampments dating between 500 CE and 1200 CE.*\n\n**Analysis Task**:\n1. What does the co-presence of pottery, iron slag, and cattle bones indicate about the interaction between early farmers and pastoralists?\n2. Why is archaeological dating essential to confirm the multi-generational timeline of oral migration traditions?",
                            "materials": ["Archaeological Site Report", "Notebook"],
                            "safety": "Handle historical artifacts and data with objective rigor."
                        }
                    }
                ],

                # Page 5: Environmental Adaptation & Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Pre-Colonial Migration Routes and Settlement Patterns in Kenya",
                        "content": {
                            "title": "Pre-Colonial Migration Routes and Settlement Patterns in Kenya",
                            "description": "Visual geographic journey detailing the multi-generational migration waves of the Bantu, Nilotes, and Cushites into Kenya and their environmental adaptations.",
                            "youtube_id": "B_kE4Tq7e4Y",
                            "url": "https://www.youtube.com/watch?v=B_kE4Tq7e4Y"
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Worked Analysis: Cushitic Environmental Adaptation",
                        "content": {
                            "title": "Adapting to Arid Landscapes",
                            "problem": "Read the excerpt: 'As Cushitic pastoralists moved south from the Horn of Africa, they encountered arid scrublands. They adapted by building deep wells, mastering water-conservation engineering, and developing highly mobile rotational grazing patterns.' Explain how environmental conditions shaped Cushitic socioeconomic lifestyle.",
                            "solution": "The dry, semi-arid environment of northern Kenya precluded crop cultivation. Consequently, Cushitic groups developed a specialized mobile pastoralist economy. They adapted by:\n1. Domesticating drought-resilient livestock (camels, desert goats, sheep).\n2. Engineering deep-well water systems (such as the *Tula* deep wells of the Borana) to access subterranean water.\n3. Establishing nomadic transhumance cycles to preserve fragile pasture vegetation from overgrazing."
                        }
                    },
                    {
                        "type": "common_misconception",
                        "title": "Misconception: Sudden Mass Invasions",
                        "content": {
                            "misconception": "Pre-colonial migrations were sudden, organized invasions where entire tribes marched along straight highway paths.",
                            "correction": "Migrations were decentralized, gradual family and clan movements that unfolded over dozens of generations. Groups settled, farmed, established cultural roots, split, and moved onward as ecological and demographic conditions demanded."
                        }
                    }
                ],

                # Page 6: Assessment & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Ecological Push Factors",
                        "content": {
                            "question": "What was an immediate ecological 'push' factor that triggered pastoralist Nilotic groups to migrate from the Nile Valley southward into Kenya?",
                            "options": [
                                "The invention of industrial steam-powered transport",
                                "Severe climate shocks, prolonged droughts, and pasture desiccation",
                                "The drawing of international colonial borders",
                                "The complete depletion of iron ore in the Nile delta"
                            ],
                            "correct": "B",
                            "explanation": "Severe droughts, drying river valleys, and pasture failures acted as primary ecological push factors, forcing Nilotic pastoralists to search for greener savannas southward."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Bantu Settlement Geography",
                        "content": {
                            "question": "Which physical environment did early Bantu migrants primarily seek when settling in Kenya, and why?",
                            "options": [
                                "Arid sand dunes to rear desert camels",
                                "High-rainfall highland zones with fertile soils suitable for crop cultivation and ironworking",
                                "Deep underground caves to isolate themselves from all trade",
                                "Dense mangrove swamps exclusively along the deep sea"
                            ],
                            "correct": "B",
                            "explanation": "As agriculturalists and ironworkers, Bantu migrants sought fertile volcanic soils and reliable rainfall in the central highlands, western hills, and coastal river valleys to cultivate crops."
                        }
                    },
                    {
                        "type": "summary_card",
                        "title": "Key Takeaways: Lesson 2 Recap",
                        "content": {
                            "title": "Summary of Core Concepts",
                            "text": "- **Push and Pull Dynamics**: Migrations were driven by push factors (drought, population pressure, warfare, disease) and pull factors (fertile soils, rich pastures, trade, security).\n- **Settlement Patterns**: Bantu settled in well-watered highlands and coastal zones; Nilotes settled in the Rift Valley and Lake basin; Cushites mastered northern arid ecosystems.\n- **Archaeological Corroboration**: Urewe pottery, iron slag, and animal bones scientifically confirm the settlement timelines described in oral histories."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Interaction, Cultural Exchange, and Conflict
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Interaction, Cultural Exchange, and Conflict",
            "unit_description": "Forms of pre-colonial inter-community interaction; economic barter networks, cultural and linguistic borrowing, age-set adoptions, and traditional dispute resolution.",
            "lesson_title": "Interaction, Cultural Exchange, and Conflict",
            "pages": [
                # Page 1: Orientation & Shared Frontiers
                [
                    {
                        "type": "suggested_image",
                        "title": "Traditional Pre-Colonial Barter Market Scene in East Africa",
                        "content": {
                            "title": "Traditional Pre-Colonial Barter Market Scene in East Africa",
                            "caption": "Traditional pre-colonial inter-community barter market scene in East Africa, where agricultural produce from highland farmers was traded for livestock goods from pastoralists.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/East_African_traditional_market.jpg/1024px-East_African_traditional_market.jpg",
                            "author": "Wikimedia Commons / Historical East Africa Archives",
                            "licensing": "Public Domain / CC BY-SA"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Inter-Community Relations",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Analyze the **economic interdependence** between agrarian and pastoralist communities.",
                                "Identify historical examples of **cultural and linguistic borrowing** (e.g., age-set systems, vocabulary).",
                                "Evaluate how **intermarriage and trade alliances** maintained long-term peace across ethnic boundaries.",
                                "Analyze the role of **councils of elders and traditional covenants** in regulating conflict and resource disputes."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Shared Ecological Frontiers",
                        "content": {
                            "title": "Living on the Contact Zones",
                            "text": "Pre-colonial communities did not live in isolated, hermetically sealed ethnic bubbles. Instead, they shared dynamic **ecological frontiers** where highland forests met open savanna plains.\n\n- **Ecological Complementarity**: Farmers produced carbohydrates (grains, tubers) and manufactured iron implements, while pastoralists produced proteins (meat, milk, butter) and leather goods. Neither group could flourish in total isolation.\n- **Dominant Pattern of Peace**: While localized skirmishes occurred during severe droughts, the overarching historical pattern was one of **sustained trade, diplomatic intermarriage, and cultural synthesis**."
                        }
                    }
                ],

                # Page 2: Forms of Pre-Colonial Interaction
                [
                    {
                        "type": "concept_explanation",
                        "title": "Three Facets of Pre-Colonial Interaction",
                        "content": {
                            "title": "Economic, Cultural, and Diplomatic Ties",
                            "text": "1. **Economic Interdependence & Barter Trade**:\n   - Highland Bantu (e.g., Agikuyu, Abaluhya) exchanged grains, sweet potatoes, bananas, and iron tools with Nilotic pastoralists (e.g., Maasai, Luo) for cattle, milk, ghee, and leather cloaks.\n   - During droughts, pastoralists relied on grain from farming neighbors to survive, while farmers acquired cattle to rebuild depleted herds.\n\n2. **Cultural and Linguistic Borrowing**:\n   - **Age-Set Systems**: Several Bantu groups adopted the age-set (*mariika*) and circumcision rituals from Southern Nilotes and Cushites to organize youth into civic and defense cadres.\n   - **Loanwords**: Extensive borrowing occurred in pastoral and agricultural vocabulary across Bantu and Nilotic languages.\n   - **Intermarriage**: Marriages between neighboring communities (such as Luo and Luhya, or Kikuyu and Maasai) established kinship ties that prevented large-scale hostilities.\n\n3. **Resource Competition & Managed Conflicts**:\n   - Conflicts arose primarily during severe ecological crises over water wells and pasture.\n   - Cattle raids were governed by customary rules of engagement and mediated promptly by elders."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Pre-Colonial Inter-Community Barter Matrix",
                        "content": {
                            "title": "Highland-Lowland Barter Matrix",
                            "headers": ["Producing Group", "Ecological Zone", "Commodities Supplied", "Commodities Received in Return"],
                            "rows": [
                                ["Highland Bantu Farmers (e.g. Agikuyu, Embu)", "Moist volcanic highlands", "Sorghum, millet, sweet potatoes, yams, iron hoes, axes, clay pots", "Livestock, hides, milk, butter/ghee, leather cloaks, beadwork"],
                                ["Plains Nilotic Pastoralists (e.g. Maasai, Samburu)", "Savanna grasslands & Rift Valley", "Cattle, goats, sheep, milk, butter, meat, hides, defensive alliances", "Grains, flour, iron weapons, agricultural tools, calabashes"],
                                ["River-Lake Nilotes (e.g. Luo of Nyanza)", "Lake Victoria Basin", "Dried fish, lake shells, pottery, specialized cattle", "Grains, bananas, timber, iron hoes from neighboring Abaluhya/Abagusii"],
                                ["Cushitic Pastoralists (e.g. Borana, Somali)", "Arid & semi-arid northern plains", "Camels, rock salt, incense, aromatic resins, leather shields", "Grains, cloth, metalware, agricultural food from riverine neighbors"]
                            ]
                        }
                    }
                ],

                # Page 3: Visual Interaction Network
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Pre-Colonial Inter-Community Exchange Network",
                        "content": {
                            "title": "Pre-Colonial Inter-Community Exchange Network",
                            "caption": "Network diagram illustrating reciprocal barter trade, cultural borrowing, intermarriage alliances, and elder dispute mediation between Bantu, Nilotes, and Cushites.",
                            "svg_content": SVG_INTERACTION_NETWORK
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Adoption of Age-Set Social Systems",
                        "content": {
                            "title": "Institutional Borrowing Across Phyla",
                            "text": "One of the most striking examples of cultural borrowing in Kenyan history is the adoption of the **age-set system** (*riika* / *olporror*).\n\n- **Origins**: Originated among Southern Cushitic and Southern Nilotic (Kalenjin/Maasai) pastoralists.\n- **Spread to Bantu**: Adopted by the Agikuyu, Ameru, Embu, and Akamba as an effective mechanism for social cohesion, civic governance, and community defense.\n- **Significance**: Proves that pre-colonial communities admired and incorporated superior institutional innovations from their neighbors across linguistic boundaries."
                        }
                    }
                ],

                # Page 4: Peacebuilding, Mediation & Elders
                [
                    {
                        "type": "suggested_image",
                        "title": "Council of Community Elders Assembled for Dispute Resolution",
                        "content": {
                            "title": "Council of Community Elders Assembled for Dispute Resolution",
                            "caption": "Council of elders (*Kiama / Njuri Ncheke / Piny Owacho*) gathered under a sacred tree to mediate territorial borders, resolve cattle disputes, and ratify peace covenants.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Traditional_African_elders_council_meeting.jpg/1024px-Traditional_African_elders_council_meeting.jpg",
                            "author": "Wikimedia Commons / National Museums of Kenya Collection",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Traditional Governance and Conflict Resolution",
                        "content": {
                            "title": "Customary Rules of Engagement",
                            "text": "Pre-colonial warfare was not anarchic or total. Strict ethical codes governed conflicts:\n\n- **Protection of Civilians**: Traditional laws across communities strictly prohibited harming women, children, the elderly, or food crops during skirmishes.\n- **Elder Councils (*Kiama*, *Njuri Ncheke*, *Piny Owacho*)**: Respected elders from opposing communities met at designated border trees to conduct peace ceremonies, slaughter sacrificial animals, and establish binding treaties.\n- **Compensation (*Blood Wealth*)**: Murders or livestock theft were settled through compensatory payments of cattle and grain rather than cycles of endless revenge."
                        }
                    }
                ],

                # Page 5: Source Analysis: Maasai-Kikuyu Peace Covenant & Video
                [
                    {
                        "type": "mini_activity",
                        "title": "Source Analysis: The Maasai-Kikuyu Peace Covenant",
                        "content": {
                            "title": "Analyzing an Oral History of Peace Diplomacy",
                            "task": "Read the oral history account recorded from elders on the borderlands:\n\n*\"In times of hunger, Maasai women would travel freely up into the Kikuyu hills. They brought leather cloaks and beads, and in return, Kikuyu families gave them sweet potatoes and millet. To guarantee their safety, the elders performed a peace ritual at the border, declaring that women and children must never be harmed, even if the warriors of the two sides were at war over pastures.\"*\n\n**Investigative Questions**:\n1. What role did women play in sustaining inter-community trade during ecological crises?\n2. How did the traditional peace covenant challenge the colonial stereotype of endless tribal hostility?\n3. What modern lessons on conflict resolution can contemporary Kenyan society draw from this pre-colonial practice?",
                            "materials": ["Source Excerpt", "Notebook"],
                            "safety": "Reflect critically on indigenous peacebuilding traditions."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Pre-Colonial Trade, Cultural Exchange, and Dispute Resolution in Kenya",
                        "content": {
                            "title": "Pre-Colonial Trade, Cultural Exchange, and Dispute Resolution in Kenya",
                            "description": "Historical investigation into highland-lowland barter trade, linguistic loanwords, age-set adoptions, and traditional peace covenants between Kenyan communities.",
                            "youtube_id": "D6_VqL_8rLw",
                            "url": "https://www.youtube.com/watch?v=D6_VqL_8rLw"
                        }
                    }
                ],

                # Page 6: Assessment & Review
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Cultural Borrowing",
                        "content": {
                            "question": "Which of the following is a clear historical example of cultural borrowing between linguistic groups in pre-colonial Kenya?",
                            "options": [
                                "The complete physical isolation of farming communities from pastoralists",
                                "The adoption of age-set social organizations and initiation systems across linguistic boundaries",
                                "The abandonment of all indigenous languages in favor of foreign European dialects",
                                "The destruction of all iron tools by pastoralist Nilotes"
                            ],
                            "correct": "B",
                            "explanation": "The adoption of age-set systems and initiation rituals (borrowed by Bantu groups from Southern Nilotes and Cushites) is a classic example of cross-cultural institutional borrowing."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Pre-Colonial Conflicts",
                        "content": {
                            "question": "Pre-colonial resource skirmishes, such as cattle raiding between pastoralists and farmers, were most frequently triggered by:",
                            "options": [
                                "Disputes over international maritime sea routes",
                                "Severe ecological stress, such as prolonged droughts and drying pasturelands",
                                "Disagreements over the spelling of indigenous words",
                                "Colonial legislation passed in European parliaments"
                            ],
                            "correct": "B",
                            "explanation": "Resource competition was primarily triggered by environmental stress and severe droughts, which created acute shortages of grazing pasture and water wells."
                        }
                    },
                    {
                        "type": "summary_card",
                        "title": "Key Takeaways: Lesson 3 Recap",
                        "content": {
                            "title": "Summary of Core Concepts",
                            "text": "- **Economic Interdependence**: Highland farmers and lowland pastoralists were mutually dependent trade partners.\n- **Cultural & Linguistic Borrowing**: Communities exchanged vocabulary, intermarried extensively, and adopted age-set governance systems.\n- **Customary Peacebuilding**: Councils of elders mediated border disputes, enforced strict civilian protections, and used peace covenants to resolve conflicts."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Social Cohesion and Appreciation of Diversity
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Social Cohesion and Appreciation of Diversity",
            "unit_description": "Promoting social cohesion, valuing cultural diversity, constitutional principles of unity in diversity, the Cohesion Wheel, and civic action.",
            "lesson_title": "Social Cohesion and Appreciation of Diversity",
            "pages": [
                # Page 1: Orientation & Civic Identity
                [
                    {
                        "type": "suggested_image",
                        "title": "Students Celebrating National Cultural Diversity at Kenya Music Festival",
                        "content": {
                            "title": "Students Celebrating National Cultural Diversity at Kenya Music Festival",
                            "caption": "Kenyan secondary school students celebrating cultural diversity through traditional music, poetry, and dance at the Kenya National Music and Cultural Festival.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Kenya_National_Music_Festival_performers.jpg/1024px-Kenya_National_Music_Festival_performers.jpg",
                            "author": "Wikimedia Commons / Ministry of Education Kenya",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Social Cohesion & Diversity",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **social cohesion** and explain why diversity is a foundational national strength.",
                                "Analyze the **five core pillars of the Cohesion Wheel** under the Constitution of Kenya (2010).",
                                "Distinguish between **forced assimilation** and **unity in diversity**.",
                                "Design practical **civic action plans** to promote intercultural dialogue and eliminate ethnic stereotyping."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Diversity as Kenya’s National Strength",
                        "content": {
                            "title": "From Historical Crossroads to Modern Nation",
                            "text": "Kenya is home to over 40 distinct indigenous ethnic communities, representing a vast repository of languages, arts, ecological knowledge, and philosophical traditions.\n\n- **The Danger of Stereotypes**: Ignorance of other communities' histories breeds negative ethnic prejudices, ethnic nepotism (*tribalism*), and social division.\n- **Constitutional Foundation**: The **Constitution of Kenya (2010)** explicitly recognizes cultural diversity as the bedrock of our national identity. Article 10 establishes national unity, inclusiveness, non-discrimination, and protection of the marginalized as non-negotiable national values."
                        }
                    }
                ],

                # Page 2: Strategies for Social Cohesion
                [
                    {
                        "type": "concept_explanation",
                        "title": "Five Core Strategies for Social Cohesion",
                        "content": {
                            "title": "Building a Cohesive Republic",
                            "text": "1. **Intercultural Dialogue & Engagement**:\n   - Fostering open communication across cultural boundaries to demystify stereotypes and build empathy.\n\n2. **Equitable Resource Distribution & Devolution**:\n   - Ensuring fair allocation of national resources, infrastructure, and development funds to eradicate historical marginalization.\n\n3. **Civic Education & Multi-Ethnic History**:\n   - Teaching our shared migration histories and mutual contributions in schools so every citizen recognizes their stake in the republic.\n\n4. **Celebrating Cultural Diversity & Language Preservation**:\n   - Promoting indigenous music, literature, sports, and language preservation as shared national heritage.\n\n5. **Constitutional Inclusivity & Anti-Discrimination**:\n   - Implementing affirmative action and anti-bias laws to ensure equitable representation in public employment and leadership."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Cultural Assimilation vs Unity in Diversity",
                        "content": {
                            "title": "Assimilation vs Unity in Diversity",
                            "headers": ["Dimension", "Forced Cultural Assimilation", "Constitutional Unity in Diversity"],
                            "rows": [
                                ["Core Philosophy", "Erasing differences to make everyone identical", "Celebrating unique cultural identities under shared citizenship"],
                                ["Language Policy", "Suppressing indigenous mother tongues", "Promoting mother tongues alongside national languages (Kiswahili & English)"],
                                ["Cultural Heritage", "Views ethnic diversity as a threat or weakness", "Views cultural diversity as a source of resilience and national pride"],
                                ["Constitutional Alignment", "Contrary to democratic rights and human dignity", "Directly mandated by the Constitution of Kenya (2010) Article 10 & 27"]
                            ]
                        }
                    }
                ],

                # Page 3: The Cohesion Wheel
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Cohesion Wheel Diagram",
                        "content": {
                            "title": "The Cohesion Wheel Diagram",
                            "caption": "The Cohesion Wheel: A structural model showing Shared National Identity supported by the 5 pillars of Intercultural Dialogue, Equity, Diversity, Civic Education, and Human Rights.",
                            "svg_content": SVG_COHESION_WHEEL
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Analyzing the Five Pillars of the Cohesion Wheel",
                        "content": {
                            "title": "How the Pillars Support the National Hub",
                            "text": "The **Cohesion Wheel** illustrates that a peaceful, prosperous nation depends on five interdependent spokes radiating from a central hub of **Shared National Identity**:\n\n- When economic inequality grows, the wheel wobbles due to ethnic grievances.\n- When cultural stereotyping goes unchecked, intercultural trust breaks down.\n- Therefore, social cohesion requires deliberate, ongoing commitment from every citizen, educator, and political leader."
                        }
                    }
                ],

                # Page 4: Legal & Policy Framework
                [
                    {
                        "type": "suggested_image",
                        "title": "Diverse Citizens Participating in National Peace Assembly",
                        "content": {
                            "title": "Diverse Citizens Participating in National Peace Assembly",
                            "caption": "Kenyan citizens and community leaders participating in an inter-ethnic peace assembly, embodying the constitutional principle of national unity in diversity.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Inter-community_peace_assembly_Kenya.jpg/1024px-Inter-community_peace_assembly_Kenya.jpg",
                            "author": "Wikimedia Commons / National Cohesion and Integration Commission",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Source Analysis: National Cohesion and Integration Act",
                        "content": {
                            "title": "Analyzing the 1/3 Ethnic Employment Rule",
                            "task": "Read the policy extract from the **National Cohesion and Integration Act**:\n\n*\"The State shall take active measures to promote equal opportunities, public participation, and non-discrimination. No public institution shall employ more than one-third of its staff from a single ethnic community, ensuring that the diversity of the Kenyan people is reflected across all public bodies.\"*\n\n**Policy Analysis Questions**:\n1. Why did the Kenyan parliament introduce the 'one-third ethnic ceiling' for public sector employment?\n2. How does this legal provision help address historical grievances regarding ethnic favoritism (*tribalism*)?\n3. What challenges might public institutions face in implementing this rule, and how can they overcome them?",
                            "materials": ["Statutory Excerpt", "Notebook"],
                            "safety": "Engage in objective civic analysis."
                        }
                    }
                ],

                # Page 5: Civic Action & Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Building Social Cohesion and Valuing Diversity under the Constitution of Kenya 2010",
                        "content": {
                            "title": "Building Social Cohesion and Valuing Diversity under the Constitution of Kenya 2010",
                            "description": "Civic education guide on national integration, the Cohesion Wheel, Article 10 constitutional values, and celebrating ethnic diversity without division.",
                            "youtube_id": "QcW9J_1lW8c",
                            "url": "https://www.youtube.com/watch?v=QcW9J_1lW8c"
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Civic Action Plan: School Cultural Day",
                        "content": {
                            "title": "Designing a Cultural Day for Intercultural Cohesion",
                            "task": "Imagine your school is hosting an annual Cultural Day. In your group:\n1. **Design a 3-step action plan** to ensure that the event celebrates Bantu, Nilotic, and Cushitic cultures equally and actively dismantles ethnic stereotypes.\n2. **Draft a Student Peace Pledge** declaring your commitment to intercultural dialogue, mutual respect, and zero tolerance for ethnic discrimination in your school.",
                            "materials": ["Flipchart", "Markers", "Notebook"],
                            "safety": "Ensure full inclusivity and respectful representation of all cultures."
                        }
                    },
                    {
                        "type": "common_misconception",
                        "title": "Misconception: National Unity Requires Erasing Culture",
                        "content": {
                            "misconception": "To achieve national unity, Kenyans must stop speaking indigenous mother tongues and erase their ethnic heritage.",
                            "correction": "National unity does not require cultural erasure. The Constitution celebrates 'unity in diversity'—pride in one's ethnic identity harmoniously complements a shared allegiance to the Kenyan nation and its democratic laws."
                        }
                    }
                ],

                # Page 6: Assessment & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Constitutional Cohesion Strategies",
                        "content": {
                            "question": "Which of the following constitutional measures directly promotes social cohesion by eliminating regional economic marginalization in Kenya?",
                            "options": [
                                "The prohibition of teaching local history in public schools",
                                "The equitable distribution of national revenue and development resources to all 47 counties through devolution",
                                "Restricting citizens from moving or working outside their home counties",
                                "Imposing a single mandatory state religion across the country"
                            ],
                            "correct": "B",
                            "explanation": "Devolution and equitable resource allocation ensure that all counties and communities receive fair development funding, eliminating historical economic disparities that cause ethnic tension."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Principle of Unity in Diversity",
                        "content": {
                            "question": "What is the primary philosophical difference between 'forced assimilation' and 'constitutional unity in diversity'?",
                            "options": [
                                "Forced assimilation promotes multilingualism while unity in diversity bans local dialects",
                                "Unity in diversity celebrates distinct cultural heritages under shared citizenship, whereas forced assimilation attempts to erase cultural differences",
                                "There is no difference; both concepts require everyone to dress and speak identically",
                                "Forced assimilation is mandated by Article 10 of the Kenya Constitution"
                            ],
                            "correct": "B",
                            "explanation": "Constitutional unity in diversity protects and celebrates diverse cultural identities while uniting all citizens under common national values and laws."
                        }
                    },
                    {
                        "type": "summary_card",
                        "title": "Key Takeaways: Lesson 4 Recap",
                        "content": {
                            "title": "Summary of Core Concepts",
                            "text": "- **Social Cohesion Defined**: The strength of social bonds, trust, and solidarity across a multi-ethnic nation.\n- **The Cohesion Wheel**: Supported by 5 pillars—Intercultural Dialogue, Equitable Distribution, Valuing Diversity, Multi-Ethnic Education, and Rule of Law.\n- **Unity in Diversity**: We can celebrate our unique ethnic languages and cultures while upholding shared loyalty to the Republic of Kenya."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Integrated Inquiry: Who Belongs and How Do We Know?
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Integrated Inquiry: Who Belongs and How Do We Know?",
            "unit_description": "Historical methodology, multi-source dossier analysis (oral traditions, linguistics, archaeology), evidence corroboration, and synthesis argument on migration and identity.",
            "lesson_title": "Integrated Inquiry: Who Belongs and How Do We Know?",
            "pages": [
                # Page 1: Orientation & The Historian's Craft
                [
                    {
                        "type": "suggested_image",
                        "title": "Archaeological Excavation Site Uncovering Pre-Colonial Artifacts",
                        "content": {
                            "title": "Archaeological Excavation Site Uncovering Pre-Colonial Artifacts",
                            "caption": "Archaeologists excavating stratigraphic layers of pottery sherds, iron slag, and bone remains in East Africa to reconstruct pre-colonial migration timelines.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Archaeological_excavation_in_East_Africa.jpg/1024px-Archaeological_excavation_in_East_Africa.jpg",
                            "author": "Wikimedia Commons / British Institute in Eastern Africa",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Historical Inquiry & Corroboration",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Evaluate the **strengths and limitations** of oral traditions, historical linguistics, and archaeology.",
                                "Analyze a **multi-source investigative dossier** containing linguistic vocabulary, archaeological artifacts, and oral legends.",
                                "Perform **evidence corroboration** to cross-check historical claims.",
                                "Construct an **evidence-based synthesis argument** demonstrating how migration formed an interconnected Kenyan society."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "How Historians Reconstruct the Past",
                        "content": {
                            "title": "The Multi-Disciplinary Toolkit",
                            "text": "How can historians reconstruct events that occurred hundreds or thousands of years ago when no written diaries or books exist?\n\n- **The Multi-Disciplinary Approach**: Historians of pre-colonial Africa combine three major streams of evidence: **Oral Traditions** (spoken memories passed down across generations), **Historical Linguistics** (comparative analysis of vocabularies and loanwords), and **Archaeology** (scientific excavation of physical remains).\n- **The Power of Corroboration**: No single source is infallible. Reliable history is established when independent clues from all three sources agree with and reinforce one another."
                        }
                    }
                ],

                # Page 2: Triangular Historical Corroboration
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Triangular Historical Corroboration Model",
                        "content": {
                            "title": "Triangular Historical Corroboration Model",
                            "caption": "Triangulation model showing how Oral Traditions, Historical Linguistics, and Archaeology converge to produce validated historical truth.",
                            "svg_content": SVG_HISTORICAL_TRIANGULATION
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comparative Evaluation of Historical Source Types",
                        "content": {
                            "title": "Historical Source Evaluation Matrix",
                            "headers": ["Source Type", "Nature of Evidence", "Primary Strengths", "Limitations & Risks", "How It Is Corroborated"],
                            "rows": [
                                ["Oral Traditions", "Spoken memories, poems, clan genealogies, songs", "Preserves human emotions, social motives, values, and alliance names", "Memory fading, chronological compression, political bias", "Cross-checked against physical archaeology and carbon dates"],
                                ["Historical Linguistics", "Comparative word lists, cognates, loanwords, glottochronology", "Maps contact zones, intermarriage, and technological borrowing", "Cannot yield precise calendar years; depends on surviving languages", "Corroborated with pottery styles and settlement locations"],
                                ["Archaeology", "Excavated potsherds, iron slag, animal bones, burial sites", "Provides tangible physical proof and precise radiocarbon dates", "Cannot reveal spoken language, names, or ideological motives directly", "Interpreted using oral traditions and linguistic geographic maps"]
                            ]
                        }
                    }
                ],

                # Page 3: The Multi-Source Dossier
                [
                    {
                        "type": "comparison_table",
                        "title": "Source A: Comparative Linguistic Vocabulary Dossier",
                        "content": {
                            "title": "Source A: Comparative Vocabulary Across Kenyan Language Families",
                            "headers": ["English Concept", "Bantu (Luyia)", "Nilotic (Luo)", "Cushitic (Somali)", "Historical Linguistic Interpretation"],
                            "rows": [
                                ["Cattle / Cow", "Ingoombe", "Dhiang'", "Sacc", "Distinct root words prove ancient, independent cattle-herding traditions."],
                                ["Grain Porridge", "Obusera", "Nyuka", "Boorash", "Demonstrates culinary sharing and grain adoption across neighboring farming groups."],
                                ["Fish", "Esikhonye", "Rech", "Kalluun", "Highly distinct vocabularies reflecting differing historical proximity to lakes and rivers."]
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Source B & Source C: Archaeology and Oral Legends",
                        "content": {
                            "title": "Material & Spoken Evidence from Western Kenya",
                            "text": "**Source B: Archaeological Evidence (Urewe Pottery Excavations)**:\n- *Excavation*: Elaborately decorated clay vessels (Urewe Ware) dating between 100 BCE and 1000 CE excavated around Lake Victoria.\n- *Context*: Found alongside ancient iron slag and carbonized finger millet seeds, confirming settled agriculture and metallurgy.\n\n**Source C: Oral History (The Legend of Intermarriage & Cuisine)**:\n- *Elder Testimony*: *\"When the ancestors of the Luyia arrived in Western Kenya, they encountered the Luo living near the lake. The Luyia were farmers and the Luo were fishermen. At first they clashed over territory, but soon their children intermarried. The Luo learned to cook grain porridge from Luyia wives, and the Luyia learned to eat fish from Luo mothers. Today, our blood and our vocabularies are intertwined.\"*"
                        }
                    }
                ],

                # Page 4: Inquiry Tasks & Critical Thinking
                [
                    {
                        "type": "mini_activity",
                        "title": "Integrated Historical Inquiry: Three Investigative Tasks",
                        "content": {
                            "title": "Student Historian Investigation",
                            "task": "Using **Sources A, B, and C**, complete the three inquiry tasks in your notebook:\n\n1. **Corroboration Task**: How does the oral legend in **Source C** explain the cultural borrowing observed in the linguistic data of **Source A** (specifically regarding porridge and fish)?\n2. **Evidence Comparison**: What can **Source B** (archaeological pottery & slag) prove with certainty that oral traditions might distort? Conversely, what human dynamics does **Source C** reveal that physical pottery can never show?\n3. **Synthesis Argument**: Write a well-supported 5-sentence paragraph answering: *'How did historical migration and inter-community interaction forge an interconnected Kenyan society?'* Cite evidence from all three sources.",
                            "materials": ["Dossier Sources A, B, C", "Inquiry Worksheet", "Pen"],
                            "safety": "Construct reasoned arguments grounded strictly in historical evidence."
                        }
                    }
                ],

                # Page 5: Primary Source Evaluation & Video
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Analysis: Mijikenda Shungwaya Oral Tradition",
                        "content": {
                            "title": "Evaluating the Shungwaya Migration Narrative",
                            "problem": "Read the elder's testimony: 'We are the Mijikenda, the Nine Towns. Our tradition recounts that we migrated south from Shungwaya to escape conflict. Along our trek, we met Cushitic traders who taught us how to traverse the arid plains. Though we are Bantu and they are Cushitic, we became brothers of trade.' Identify one Bantu group in this source and explain how their migration fostered cross-cultural cooperation.",
                            "solution": "The Mijikenda are a Bantu group. According to this oral history, their southward migration to escape conflict brought them into contact with Cushitic traders. This physical encounter produced cooperation rather than hostility: the Mijikenda learned arid-land navigation techniques from their Cushitic neighbors, establishing peaceful trade partnerships and mutual respect across linguistic families."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Historical Inquiry: Corroborating Oral Traditions, Linguistics, and Archaeology",
                        "content": {
                            "title": "Historical Inquiry: Corroborating Oral Traditions, Linguistics, and Archaeology",
                            "description": "Step-by-step masterclass on how historians synthesize oral histories, comparative vocabulary, and archaeological artifacts to construct evidence-based African history.",
                            "youtube_id": "M2_J6r9P7wM",
                            "url": "https://www.youtube.com/watch?v=M2_J6r9P7wM"
                        }
                    }
                ],

                # Page 6: Assessment & Topic 1.1 Mastery
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Corroboration in Historical Inquiry",
                        "content": {
                            "question": "Why must historians triangulate oral traditions with archaeological and linguistic evidence when reconstructing pre-colonial African history?",
                            "options": [
                                "Because oral traditions are completely fabricated and must always be dismissed",
                                "Because corroborating multiple independent sources overcomes the limitations of individual source types and establishes verifiable historical truth",
                                "Because archaeological pottery alone can reveal the exact language and political speeches of ancient rulers",
                                "Because the Constitution of Kenya prohibits using oral tradition in schools"
                            ],
                            "correct": "B",
                            "explanation": "Triangulating oral traditions, linguistics, and archaeology allows historians to cross-examine evidence: archaeology provides physical and chronological grounding, linguistics tracks contact and borrowing, and oral tradition provides human motivations and cultural context."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Topic 1.1 Synthesis",
                        "content": {
                            "question": "Which statement best synthesizes the core historical lesson of Topic 1.1 regarding Kenyan linguistic groups and citizenship?",
                            "options": [
                                "Kenya's linguistic groups lived in permanent isolation and never influenced each other",
                                "Historical migrations and interactions created a deeply interconnected society where diversity is a foundational strength protected by constitutional values",
                                "All Kenyans originally spoke a single language until European colonialists arrived in 1895",
                                "Linguistic groups represent rigid biological races that must remain strictly separated"
                            ],
                            "correct": "B",
                            "explanation": "Topic 1.1 demonstrates that centuries of migration, trade, intermarriage, and cultural borrowing forged an interconnected, diverse nation whose unity is anchored in shared constitutional citizenship."
                        }
                    },
                    {
                        "type": "summary_card",
                        "title": "Topic 1.1 Mastery: Comprehensive Synthesis",
                        "content": {
                            "title": "Topic 1.1 Final Milestone Recap",
                            "text": "- **Kenya’s Population**: Classified into **Bantu**, **Nilotic**, and **Cushitic** language families with rich, distinct continental origins.\n- **Dynamic Migration**: Push-pull forces guided multi-generational movements that established our modern geographical landscape.\n- **Interdependence & Exchange**: Pre-colonial trade, cultural borrowing (e.g. age-sets), intermarriage, and elder diplomacy created deep inter-ethnic bonds.\n- **Social Cohesion**: Constitutional values (Article 10) mandate **unity in diversity**, equitable resource distribution, and the active appreciation of all cultures.\n- **Inquiry Methodology**: Historical truth is uncovered by triangulating **oral traditions**, **linguistics**, and **archaeology**."
                        }
                    }
                ]
            ]
        }
    ]


# =====================================================================
# INGESTION RUNNER FUNCTION
# =====================================================================

def ingest_grade10_history_topic1(replace=True):
    print("=" * 80)
    print("INGESTING CBC GRADE 10 HISTORY — TOPIC 1: LINGUISTIC GROUPS IN KENYA")
    print("=" * 80)

    # 1. Resolve Grade 10 CBC
    grade = Grade.objects.filter(name="Grade 10", curriculum__name="CBC").first()
    if not grade:
        grade = Grade.objects.filter(id=5).first()
    if not grade:
        raise ValueError("Could not resolve Grade 10 in CBC curriculum.")
    print(f"[*] Resolved Grade: {grade.name} (ID: {grade.id}, Curriculum: {grade.curriculum.name if grade.curriculum else 'None'})")

    # 2. Resolve or Create Subject 'History'
    subject, s_created = Subject.objects.get_or_create(
        grade=grade,
        name="History",
        defaults={
            "description": "Senior School History and Citizenship Curriculum (Grade 10 CBC)"
        }
    )
    if s_created:
        print(f"[+] Created Subject: {subject.name} (ID: {subject.id}) in Grade: {grade.name}")
    else:
        print(f"[*] Resolved Subject: {subject.name} (ID: {subject.id}) in Grade: {grade.name}")

    # 3. Resolve or Create Topic 1: Linguistic Groups in Kenya
    topic_name = "Topic 1.1: Linguistic Groups in Kenya"
    topic_desc = (
        "This topic introduces the rich population diversity of Kenya by exploring the major linguistic families, "
        "their migration histories, settlement patterns, and interactions. Students will learn how environmental, political, "
        "and social forces shaped the diverse cultural landscape of modern Kenya and understand the constitutional and civic "
        "values necessary for promoting social cohesion and national integration in a multi-ethnic society."
    )
    
    topic = Topic.objects.filter(subject=subject, order=1).first()
    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            order=1,
            name=topic_name,
            description=topic_desc
        )
        print(f"[+] Created Topic 1: {topic.name} (ID: {topic.id})")
    else:
        topic.name = topic_name
        topic.description = topic_desc
        topic.save()
        print(f"[*] Updated Topic 1: {topic.name} (ID: {topic.id})")

    # 4. Ingest Lessons & Blocks inside atomic transaction
    curriculum_data = build_grade10_history_topic1_curriculum()
    total_units = 0
    total_lessons = 0
    total_pages = 0
    total_blocks = 0
    total_assets = 0

    with transaction.atomic():
        if replace:
            print("[*] Clearing existing LearningUnits, Lessons, Blocks, and Assets for Topic 1...")
            existing_units = LearningUnit.objects.filter(topic=topic)
            for eu in existing_units:
                existing_lessons = Lesson.objects.filter(learning_unit=eu)
                for el in existing_lessons:
                    LessonAsset.objects.filter(lesson=el).delete()
                    el.blocks.all().delete()
                existing_lessons.delete()
            existing_units.delete()

        for item in curriculum_data:
            u_order = item["unit_order"]
            u_name = item["unit_name"]
            u_desc = item["unit_description"]
            l_title = item["lesson_title"]
            pages = item["pages"]

            unit = LearningUnit.objects.create(
                topic=topic,
                order=u_order,
                name=u_name,
                description=u_desc
            )
            total_units += 1

            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=l_title,
                status="published",
                version=1,
                immutable_metadata={
                    "author": "VLearn Senior History Curriculum Specialist",
                    "grade": "Grade 10",
                    "subject": "History",
                    "topic_order": 1,
                    "unit_order": u_order,
                    "lesson_number": u_order
                }
            )
            total_lessons += 1

            block_counter = 1
            for page_idx, page_blocks in enumerate(pages, start=1):
                total_pages += 1
                for comp_idx, block_def in enumerate(page_blocks, start=1):
                    b_type = block_def["type"]
                    b_title = clean_text(block_def.get("title", ""))
                    b_content = clean_dict(block_def.get("content", {}))

                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=f"g10_hist_t1_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={
                            "grade": "Grade 10",
                            "subject": "History",
                            "topic_order": 1,
                            "unit_order": u_order,
                            "page": page_idx
                        }
                    )
                    block_counter += 1
                    total_blocks += 1

                    # Attach LessonAssets based on component type
                    if b_type == "suggested_diagram" and "svg_content" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="diagram",
                            source_type="ai_generated",
                            storage_type="embed",
                            status="attached",
                            title=b_title,
                            description=b_content.get("caption", b_title),
                            metadata={"svg_content": b_content["svg_content"]}
                        )
                        block.assets.add(asset)
                        total_assets += 1

                    elif b_type == "suggested_image" and "url" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="image",
                            source_type="external",
                            storage_type="url",
                            status="attached",
                            title=b_title,
                            description=b_content.get("caption", b_title),
                            url=b_content["url"],
                            metadata={
                                "author": b_content.get("author", "Wikimedia Commons"),
                                "licensing": b_content.get("licensing", "CC BY-SA 4.0"),
                                "caption": b_content.get("caption", "")
                            }
                        )
                        block.assets.add(asset)
                        total_assets += 1

                    elif b_type == "suggested_video" and "youtube_id" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="youtube",
                            source_type="external",
                            storage_type="url",
                            status="attached",
                            title=b_title,
                            description=b_content.get("description", b_title),
                            url=b_content.get("url", f"https://www.youtube.com/watch?v={b_content['youtube_id']}"),
                            metadata={"youtube_id": b_content["youtube_id"]}
                        )
                        block.assets.add(asset)
                        total_assets += 1

            print(f"  [+] Ingested Unit {u_order}: '{u_name}' -> Lesson '{l_title}' ({len(pages)} Pages, {block_counter - 1} Blocks)")

    print("=" * 80)
    print("INGESTION COMPLETE SUMMARY:")
    print(f"  Grade:            {grade.name} (Curriculum: {grade.curriculum.name if grade.curriculum else 'None'})")
    print(f"  Subject:          {subject.name} (ID: {subject.id})")
    print(f"  Topic:            {topic.name} (Order: {topic.order}, ID: {topic.id})")
    print(f"  Units Ingested:   {total_units}")
    print(f"  Lessons Ingested: {total_lessons} (All published)")
    print(f"  Pages Ingested:   {total_pages}")
    print(f"  Blocks Ingested:  {total_blocks}")
    print(f"  Assets Attached:  {total_assets}")
    print("=" * 80)

    return {
        "grade_id": grade.id,
        "subject_id": subject.id,
        "topic_id": topic.id,
        "total_units": total_units,
        "total_lessons": total_lessons,
        "total_pages": total_pages,
        "total_blocks": total_blocks,
        "total_assets": total_assets
    }


if __name__ == "__main__":
    replace_flag = "--no-replace" not in sys.argv
    ingest_grade10_history_topic1(replace=replace_flag)
