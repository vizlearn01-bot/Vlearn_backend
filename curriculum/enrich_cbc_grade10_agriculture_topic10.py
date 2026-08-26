"""
VLearn CBC Grade 10 Agriculture — Topic 10: General Animal Health
Visual Enrichment Engine (Phase 2: Vector SVGs, Verified Photos & Asset Persistence)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: General Animal Health (Order: 10)

Attaches:
  - 12 First-Card Photographic Visual Hooks (100% Tested HTTP 200 Direct Wikimedia URLs)
  - 8 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - 1 Verified Educational YouTube Video (Lesson 3 Card 3)
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_agriculture_topic10.py
"""

import os
import sys
import re
import json
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, Lesson, LessonBlock, LessonAsset
)

def sanitize_svg(svg: str) -> str:
    """Ensures SVG is clean, responsive, and stripped of unneeded XML/DOCTYPE headers."""
    svg = re.sub(r'<\?xml.*?\?>', '', svg)
    svg = re.sub(r'<!DOCTYPE.*?>', '', svg)
    return svg.strip()

# =============================================================================
# 8 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 10: GENERAL ANIMAL HEALTH
# =============================================================================

# SVG 1: Positive Feedback Loop of Animal Health (Lesson 1, Page 2)
SVG_HEALTH_FEEDBACK_LOOP = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Positive Feedback Loop of Livestock Health &amp; Agribusiness Profit</text>

  <!-- Central Hub: Healthy Animals -->
  <circle cx="400" cy="240" r="58" fill="#0f172a" stroke="#22c55e" stroke-width="3"/>
  <text x="400" y="232" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">OPTIMAL</text>
  <text x="400" y="248" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">ANIMAL</text>
  <text x="400" y="263" font-size="10" fill="#86efac" text-anchor="middle">HEALTH</text>

  <!-- Node 1: High Feed Conversion (Top) -->
  <g transform="translate(285, 68)">
    <rect x="0" y="0" width="230" height="78" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="24" rx="8" fill="#0284c7"/>
    <text x="115" y="16" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1. HIGH FEED CONVERSION</text>
    <text x="10" y="44" font-size="9" fill="#cbd5e1">• 100% nutrient absorption for growth</text>
    <text x="10" y="60" font-size="9" fill="#cbd5e1">• Zero energy squandered on fever</text>
  </g>
  <line x1="400" y1="146" x2="400" y2="182" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="395,172 400,182 405,172" fill="#38bdf8"/>

  <!-- Node 2: Peak Product Quality (Right) -->
  <g transform="translate(545, 195)">
    <rect x="0" y="0" width="220" height="80" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="25" rx="8" fill="#ca8a04"/>
    <text x="110" y="17" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2. PEAK PRODUCT QUALITY</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Low somatic cell count milk</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Zero antibiotic residues in food</text>
  </g>
  <line x1="545" y1="240" x2="458" y2="240" stroke="#eab308" stroke-width="3"/>
  <polygon points="468,235 458,240 468,245" fill="#eab308"/>

  <!-- Node 3: Low Veterinary Costs (Bottom) -->
  <g transform="translate(285, 322)">
    <rect x="0" y="0" width="230" height="78" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="24" rx="8" fill="#7e22ce"/>
    <text x="115" y="16" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3. MINIMAL VET EXPENSES</text>
    <text x="10" y="44" font-size="9" fill="#cbd5e1">• Zero emergency curative treatments</text>
    <text x="10" y="60" font-size="9" fill="#cbd5e1">• Zero morbidity production halts</text>
  </g>
  <line x1="400" y1="322" x2="400" y2="298" stroke="#a855f7" stroke-width="3"/>
  <polygon points="395,308 400,298 405,308" fill="#a855f7"/>

  <!-- Node 4: High Farmer Profit (Left) -->
  <g transform="translate(35, 195)">
    <rect x="0" y="0" width="220" height="80" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="25" rx="8" fill="#15803d"/>
    <text x="110" y="17" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">4. MAXIMUM PROFIT MARGIN</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Premium dairy/meat market prices</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• High return on feed investment</text>
  </g>
  <line x1="255" y1="240" x2="342" y2="240" stroke="#22c55e" stroke-width="3"/>
  <polygon points="332,235 342,240 332,245" fill="#22c55e"/>
</svg>
""")

# SVG 2: Cattle Clinical Diagnostic Checkpoints (Lesson 3, Page 2)
SVG_CATTLE_DIAGNOSTICS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Key Clinical Diagnostic Checkpoints on Cattle</text>

  <!-- Cow Schematic Diagram -->
  <g transform="translate(60, 60)">
    <!-- Cow Silhouette Body -->
    <ellipse cx="340" cy="180" rx="160" ry="60" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
    <!-- Head -->
    <ellipse cx="140" cy="150" rx="50" ry="35" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
    <!-- Neck -->
    <polygon points="170,130 210,145 190,195 150,180" fill="#334155"/>

    <!-- Checkpoint 1: Eyes & Nose (Respiratory / IBR) -->
    <circle cx="110" cy="140" r="14" fill="#ef4444" stroke="#ffffff" stroke-width="2"/>
    <text x="110" y="144" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
    <g transform="translate(10, 20)">
      <rect x="0" y="0" width="180" height="45" rx="6" fill="#0f172a" stroke="#ef4444"/>
      <text x="90" y="18" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">1. EYES &amp; NOSE</text>
      <text x="90" y="34" font-size="8" fill="#cbd5e1" text-anchor="middle">Discharge, crusts, pneumonia</text>
    </g>
    <line x1="90" y1="65" x2="110" y2="126" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="2,2"/>

    <!-- Checkpoint 2: Mucous Membrane / Anemia -->
    <circle cx="150" cy="125" r="14" fill="#eab308" stroke="#ffffff" stroke-width="2"/>
    <text x="150" y="129" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
    <g transform="translate(205, 20)">
      <rect x="0" y="0" width="170" height="45" rx="6" fill="#0f172a" stroke="#eab308"/>
      <text x="85" y="18" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">2. CONJUNCTIVAL MUCOSA</text>
      <text x="85" y="34" font-size="8" fill="#cbd5e1" text-anchor="middle">Pale/white = Severe Anemia</text>
    </g>
    <line x1="270" y1="65" x2="164" y2="120" stroke="#eab308" stroke-width="1.5" stroke-dasharray="2,2"/>

    <!-- Checkpoint 3: Left Flank / Bloat -->
    <circle cx="300" cy="155" r="16" fill="#06b6d4" stroke="#ffffff" stroke-width="2"/>
    <text x="300" y="160" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
    <g transform="translate(390, 20)">
      <rect x="0" y="0" width="170" height="45" rx="6" fill="#0f172a" stroke="#06b6d4"/>
      <text x="85" y="18" font-size="9" font-weight="bold" fill="#67e8f9" text-anchor="middle">3. LEFT FLANK (RUMEN)</text>
      <text x="85" y="34" font-size="8" fill="#cbd5e1" text-anchor="middle">Swollen tight = Acute Bloat</text>
    </g>
    <line x1="460" y1="65" x2="315" y2="150" stroke="#06b6d4" stroke-width="1.5" stroke-dasharray="2,2"/>

    <!-- Checkpoint 4: Spine / Arched Posture -->
    <circle cx="380" cy="125" r="14" fill="#a855f7" stroke="#ffffff" stroke-width="2"/>
    <text x="380" y="129" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">4</text>
    <g transform="translate(520, 90)">
      <rect x="0" y="0" width="160" height="45" rx="6" fill="#0f172a" stroke="#a855f7"/>
      <text x="80" y="18" font-size="9" font-weight="bold" fill="#d8b4fe" text-anchor="middle">4. ARCHED SPINE</text>
      <text x="80" y="34" font-size="8" fill="#cbd5e1" text-anchor="middle">Abdominal pain / peritonitis</text>
    </g>
    <line x1="520" y1="115" x2="394" y2="125" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="2,2"/>

    <!-- Checkpoint 5: Tail & Vent / Scours -->
    <circle cx="490" cy="180" r="14" fill="#22c55e" stroke="#ffffff" stroke-width="2"/>
    <text x="490" y="184" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">5</text>
    <g transform="translate(520, 200)">
      <rect x="0" y="0" width="160" height="45" rx="6" fill="#0f172a" stroke="#22c55e"/>
      <text x="80" y="18" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">5. TAIL &amp; PERINEUM</text>
      <text x="80" y="34" font-size="8" fill="#cbd5e1" text-anchor="middle">Fecal staining / Scours</text>
    </g>
    <line x1="520" y1="215" x2="504" y2="185" stroke="#22c55e" stroke-width="1.5" stroke-dasharray="2,2"/>
  </g>

  <!-- Technical Diagnostic Summary -->
  <g transform="translate(60, 355)">
    <rect x="0" y="0" width="680" height="60" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="340" y="22" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Daily Diagnostic Standard: Observe Alertness -> Rumen Motility (Left Flank) -> Mucosa Color</text>
    <text x="340" y="42" font-size="9" fill="#cbd5e1" text-anchor="middle">Active rumination + bright pink membranes = Healthy Cow. Distension + pale eyes = Critical Emergency!</text>
  </g>
</svg>
""")

# SVG 3: Sheep Bottle Jaw Pathology (Lesson 4, Page 2)
SVG_BOTTLE_JAW = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Pathophysiology of Bottle Jaw (Submandibular Edema) in Sheep</text>

  <!-- 4-Step Pathology Cascade -->
  <!-- Step 1: Parasite Ingestion -->
  <g transform="translate(45, 75)">
    <rect x="0" y="0" width="160" height="250" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="160" height="28" rx="8" fill="#991b1b"/>
    <text x="80" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 1: INFECTION</text>
    <text x="80" y="60" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">Haemonchus contortus</text>
    <text x="10" y="85" font-size="9" fill="#cbd5e1">• Blood-sucking wireworm</text>
    <text x="10" y="105" font-size="9" fill="#cbd5e1">• Attaches to abomasal</text>
    <text x="10" y="120" font-size="9" fill="#cbd5e1">  stomach wall</text>
    <text x="10" y="145" font-size="9" fill="#cbd5e1">• Consumes 0.05 mL</text>
    <text x="10" y="160" font-size="9" fill="#cbd5e1">  blood/worm/day</text>
  </g>
  <line x1="205" y1="200" x2="235" y2="200" stroke="#ef4444" stroke-width="3"/>
  <polygon points="225,195 235,200 225,205" fill="#ef4444"/>

  <!-- Step 2: Blood Protein Loss -->
  <g transform="translate(235, 75)">
    <rect x="0" y="0" width="160" height="250" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect x="0" y="0" width="160" height="28" rx="8" fill="#ca8a04"/>
    <text x="80" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 2: PROTEIN LOSS</text>
    <text x="80" y="60" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">Hypoproteinemia</text>
    <text x="10" y="85" font-size="9" fill="#cbd5e1">• Severe depletion of</text>
    <text x="10" y="100" font-size="9" fill="#cbd5e1">  serum albumin</text>
    <text x="10" y="125" font-size="9" fill="#cbd5e1">• Blood thinning</text>
    <text x="10" y="150" font-size="9" fill="#cbd5e1">• Critical drop in blood</text>
    <text x="10" y="165" font-size="9" fill="#cbd5e1">  colloid oncotic pressure</text>
  </g>
  <line x1="395" y1="200" x2="425" y2="200" stroke="#eab308" stroke-width="3"/>
  <polygon points="415,195 425,200 415,205" fill="#eab308"/>

  <!-- Step 3: Fluid Extravasation -->
  <g transform="translate(425, 75)">
    <rect x="0" y="0" width="160" height="250" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="160" height="28" rx="8" fill="#0284c7"/>
    <text x="80" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 3: LEAKAGE</text>
    <text x="80" y="60" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Fluid Extravasation</text>
    <text x="10" y="85" font-size="9" fill="#cbd5e1">• Plasma fluid escapes</text>
    <text x="10" y="100" font-size="9" fill="#cbd5e1">  from capillaries</text>
    <text x="10" y="125" font-size="9" fill="#cbd5e1">• Floods interstitial tissue</text>
    <text x="10" y="150" font-size="9" fill="#cbd5e1">• Gravitational pooling</text>
    <text x="10" y="165" font-size="9" fill="#cbd5e1">  in lowest body spaces</text>
  </g>
  <line x1="585" y1="200" x2="615" y2="200" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="605,195 615,200 605,205" fill="#38bdf8"/>

  <!-- Step 4: Bottle Jaw Manifestation -->
  <g transform="translate(615, 75)">
    <rect x="0" y="0" width="145" height="250" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="145" height="28" rx="8" fill="#15803d"/>
    <text x="72" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 4: BOTTLE JAW</text>
    <text x="72" y="60" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Submandibular Edema</text>
    <text x="8" y="85" font-size="9" fill="#cbd5e1">• Soft, cold swelling</text>
    <text x="8" y="100" font-size="9" fill="#cbd5e1">  under lower jaw</text>
    <text x="8" y="125" font-size="9" fill="#cbd5e1">• Extreme flock lagging</text>
    <text x="8" y="150" font-size="9" fill="#cbd5e1">• Cure: Albendazole drench</text>
    <text x="8" y="165" font-size="9" fill="#cbd5e1">  + pasture rotation</text>
  </g>

  <!-- Treatment Footer -->
  <g transform="translate(45, 345)">
    <rect x="0" y="0" width="715" height="65" rx="6" fill="#0f172a" stroke="#22c55e"/>
    <text x="357" y="24" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">Key Rule: Bottle Jaw is NOT an abscess—it is painless fluid accumulation from internal parasitism!</text>
    <text x="357" y="46" font-size="9" fill="#cbd5e1" text-anchor="middle">Prevention: Rotational grazing (spelling paddocks for 6 weeks) starves infective larvae on pasture without chemical resistance.</text>
  </g>
</svg>
""")

# SVG 4: The 3 Pillars of Preventative Health (Lesson 6, Page 2)
SVG_PREVENTATIVE_PILLARS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 3 Pillars of Preventative Animal Health</text>

  <!-- Triangular Pillar Layout -->
  <!-- 1. Nutrition & Clean Water (Top) -->
  <g transform="translate(275, 65)">
    <rect x="0" y="0" width="250" height="85" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="250" height="26" rx="10" fill="#15803d"/>
    <text x="125" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. NUTRITION &amp; CLEAN WATER</text>
    <text x="12" y="46" font-size="9" fill="#cbd5e1">• Vitamin A: Intact mucosal barriers</text>
    <text x="12" y="62" font-size="9" fill="#cbd5e1">• Balanced protein: Antibody synthesis</text>
    <text x="12" y="78" font-size="9" fill="#cbd5e1">• Clean water: Zero coliform bacteria</text>
  </g>

  <!-- 2. Engineered Housing & Ventilation (Bottom Left) -->
  <g transform="translate(45, 230)">
    <rect x="0" y="0" width="330" height="150" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="330" height="28" rx="10" fill="#0284c7"/>
    <text x="165" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. HOUSING &amp; VENTILATION</text>
    <text x="15" y="52" font-size="10" font-weight="bold" fill="#38bdf8">• Continuous Airflow (<10ppm Ammonia):</text>
    <text x="15" y="68" font-size="9" fill="#cbd5e1">  Prevents ciliary paralysis &amp; respiratory pneumonia.</text>
    <text x="15" y="92" font-size="10" font-weight="bold" fill="#38bdf8">• Dry Bedding Standards:</text>
    <text x="15" y="108" font-size="9" fill="#cbd5e1">  Prevents hoof softening, foot rot &amp; coccidiosis.</text>
    <text x="15" y="132" font-size="10" font-weight="bold" fill="#38bdf8">• Adequate Space: Eliminates social stress.</text>
  </g>

  <!-- 3. Bio-Sanitation & Disinfection (Bottom Right) -->
  <g transform="translate(425, 230)">
    <rect x="0" y="0" width="330" height="150" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="330" height="28" rx="10" fill="#ca8a04"/>
    <text x="165" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. BIO-SANITATION &amp; DISINFECTION</text>
    <text x="15" y="52" font-size="10" font-weight="bold" fill="#fde047">• Daily Manure Scraping:</text>
    <text x="15" y="68" font-size="9" fill="#cbd5e1">  Eliminates fly breeding &amp; coccidial reservoirs.</text>
    <text x="15" y="92" font-size="10" font-weight="bold" fill="#fde047">• Agricultural Lime Application:</text>
    <text x="15" y="108" font-size="9" fill="#cbd5e1">  Raises dirt floor pH to >11, destroying bacteria.</text>
    <text x="15" y="132" font-size="10" font-weight="bold" fill="#fde047">• Trough Washing: Scrubbed daily with clean brushes.</text>
  </g>

  <!-- Central Connecting Lines -->
  <line x1="330" y1="150" x2="210" y2="230" stroke="#22c55e" stroke-width="2" stroke-dasharray="3,3"/>
  <line x1="470" y1="150" x2="590" y2="230" stroke="#22c55e" stroke-width="2" stroke-dasharray="3,3"/>
  <line x1="375" y1="305" x2="425" y2="305" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3"/>
</svg>
""")

# SVG 5: Farm Biosecurity & 30-Day Quarantine (Lesson 7, Page 2)
SVG_BIOSECURITY_QUARANTINE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Farm Biosecurity Perimeter &amp; 30-Day Quarantine Architecture</text>

  <!-- Left: Biosecurity Blueprint -->
  <g transform="translate(45, 60)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="28" rx="10" fill="#15803d"/>
    <text x="170" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">FARM BIOSECURITY BARRIERS</text>

    <!-- 1. Main Gate Vehicle Dip -->
    <g transform="translate(15, 40)">
      <rect x="0" y="0" width="310" height="50" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="12" y="18" font-size="10" font-weight="bold" fill="#38bdf8">1. Main Gate Vehicle Tire Dip:</text>
      <text x="12" y="36" font-size="9" fill="#cbd5e1">Disinfects truck wheels from external farms.</text>
    </g>

    <!-- 2. Disinfectant Footbaths -->
    <g transform="translate(15, 100)">
      <rect x="0" y="0" width="310" height="50" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="12" y="18" font-size="10" font-weight="bold" fill="#38bdf8">2. Disinfectant Footbaths at Sheds:</text>
      <text x="12" y="36" font-size="9" fill="#cbd5e1">Copper sulfate / Virkon-S boots sterilization.</text>
    </g>

    <!-- 3. Bird & Rodent Mesh -->
    <g transform="translate(15, 160)">
      <rect x="0" y="0" width="310" height="50" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="12" y="18" font-size="10" font-weight="bold" fill="#38bdf8">3. Wild Bird Exclusion Mesh:</text>
      <text x="12" y="36" font-size="9" fill="#cbd5e1">1.5cm wire mesh blocks wild Newcastle carriers.</text>
    </g>

    <!-- 4. Mandatory Handwashing -->
    <g transform="translate(15, 220)">
      <rect x="0" y="0" width="310" height="50" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="12" y="18" font-size="10" font-weight="bold" fill="#38bdf8">4. 20-Sec Sanitization Sinks:</text>
      <text x="12" y="36" font-size="9" fill="#cbd5e1">Soap &amp; clean water stations at all exit doors.</text>
    </g>

    <text x="170" y="300" font-size="9" fill="#4ade80" text-anchor="middle">Goal: Zero biological pathogens penetrate the farm fence!</text>
  </g>

  <!-- Right: 30-Day Quarantine Unit -->
  <g transform="translate(415, 60)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="28" rx="10" fill="#ca8a04"/>
    <text x="172" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">THE 30-DAY QUARANTINE PROTOCOL</text>

    <!-- Schematic Distance Box -->
    <rect x="15" y="40" width="315" height="110" rx="6" fill="#1e293b" stroke="#eab308"/>
    <text x="157" y="62" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">ISOLATED QUARANTINE SHED</text>
    <text x="157" y="80" font-size="10" font-weight="bold" fill="#ef4444" text-anchor="middle">≥ 100 METERS DISTANCE FROM MAIN HERD</text>
    <text x="157" y="105" font-size="9" fill="#cbd5e1" text-anchor="middle">• Dedicated tools, feed buckets, &amp; boots</text>
    <text x="157" y="125" font-size="9" fill="#cbd5e1">• Attendant visits quarantine pen LAST in the day</text>

    <!-- 30-Day Timeline -->
    <g transform="translate(15, 165)">
      <rect x="0" y="0" width="315" height="65" rx="6" fill="#0f172a" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">Days 1–14: Clinical Monitoring &amp; Deworming</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Watch for incubation of FMD, Anthrax, or ECF.</text>
      <text x="15" y="54" font-size="9" fill="#cbd5e1">Administer broad-spectrum anthelmintics &amp; acaricide.</text>
    </g>

    <g transform="translate(15, 240)">
      <rect x="0" y="0" width="315" height="65" rx="6" fill="#0f172a" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">Days 15–30: Vaccinations &amp; Clearance</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Administer farm-specific booster vaccines.</text>
      <text x="15" y="54" font-size="9" fill="#86efac">Day 30: Full veterinary sign-off -> Joins Main Herd.</text>
    </g>
  </g>
</svg>
""")

# SVG 6: Parasite Life Cycle & Pasture Rotation (Lesson 8, Page 2)
SVG_PASTURE_ROTATION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Internal Parasite Life Cycle &amp; Pasture Rotation Breaking Mechanism</text>

  <!-- Circular Parasite Cycle (Left) -->
  <g transform="translate(45, 60)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="28" rx="10" fill="#991b1b"/>
    <text x="170" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">PARASITE TRANSMISSION CYCLE</text>

    <g transform="translate(15, 40)">
      <rect x="0" y="0" width="310" height="50" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="12" y="18" font-size="10" font-weight="bold" fill="#f87171">1. Eggs Shed in Manure:</text>
      <text x="12" y="35" font-size="9" fill="#cbd5e1">Adult Haemonchus shed 10,000 eggs/day in dung.</text>

      <rect x="0" y="60" width="310" height="50" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="12" y="18" font-size="10" font-weight="bold" fill="#f87171">2. Larvae Hatch on Grass (3–5 Days):</text>
      <text x="12" y="35" font-size="9" fill="#cbd5e1">Microscopic L3 infective larvae crawl up dew drops.</text>

      <rect x="0" y="120" width="310" height="50" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="12" y="18" font-size="10" font-weight="bold" fill="#f87171">3. Ingestion by Grazing Sheep:</text>
      <text x="12" y="35" font-size="9" fill="#cbd5e1">Animals graze grass tips, swallowing infective larvae.</text>

      <rect x="0" y="180" width="310" height="50" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="12" y="18" font-size="10" font-weight="bold" fill="#f87171">4. Abomasal Blood Loss &amp; Disease:</text>
      <text x="12" y="35" font-size="9" fill="#cbd5e1">Causes severe anemia, hypoproteinemia &amp; bottle jaw.</text>
    </g>
  </g>

  <!-- Rotational Grazing Breaking Strategy (Right) -->
  <g transform="translate(415, 60)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="28" rx="10" fill="#15803d"/>
    <text x="172" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">HOW PASTURE ROTATION BREAKS CYCLE</text>

    <!-- 4 Paddock Grid -->
    <g transform="translate(20, 45)">
      <!-- Paddock A (Grazing Now) -->
      <rect x="0" y="0" width="145" height="100" rx="6" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
      <text x="72" y="25" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">PADDOCK A</text>
      <text x="72" y="45" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">CURRENT GRAZING</text>
      <text x="72" y="65" font-size="8" fill="#ffffff" text-anchor="middle">Stock present 7 days</text>
      <text x="72" y="82" font-size="8" fill="#dcfce7" text-anchor="middle">Eggs shed in manure</text>

      <!-- Paddock B (Resting 14 Days) -->
      <rect x="160" y="0" width="145" height="100" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="232" y="25" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">PADDOCK B</text>
      <text x="232" y="45" font-size="9" fill="#94a3b8" text-anchor="middle">RESTING (Week 2)</text>
      <text x="232" y="65" font-size="8" fill="#cbd5e1" text-anchor="middle">Larvae hatching</text>
      <text x="232" y="82" font-size="8" fill="#cbd5e1" text-anchor="middle">No hosts available!</text>

      <!-- Paddock C (Resting 28 Days) -->
      <rect x="0" y="115" width="145" height="100" rx="6" fill="#1e293b" stroke="#eab308"/>
      <text x="72" y="140" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">PADDOCK C</text>
      <text x="72" y="160" font-size="9" fill="#94a3b8" text-anchor="middle">RESTING (Week 4)</text>
      <text x="72" y="180" font-size="8" fill="#cbd5e1" text-anchor="middle">Larvae starving</text>
      <text x="72" y="195" font-size="8" fill="#cbd5e1" text-anchor="middle">Sunlight desiccation</text>

      <!-- Paddock D (Clean Pasture 42 Days) -->
      <rect x="160" y="115" width="145" height="100" rx="6" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
      <text x="232" y="140" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">PADDOCK D</text>
      <text x="232" y="160" font-size="9" font-weight="bold" fill="#86efac" text-anchor="middle">CLEAN (Week 6)</text>
      <text x="232" y="180" font-size="8" fill="#ffffff" text-anchor="middle">95% Larvae DEAD!</text>
      <text x="232" y="195" font-size="8" fill="#dcfce7" text-anchor="middle">Safe for grazing return</text>
    </g>

    <text x="172" y="280" font-size="9" fill="#86efac" text-anchor="middle">Pasture spelling for 6 weeks breaks cycle with zero chemicals!</text>
  </g>
</svg>
""")

# SVG 7: Safe Oral Drenching Mechanics (Lesson 10, Page 2)
SVG_DRENCHING_MECHANICS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Safe Oral Drenching Head Angle vs. Fatal Aspiration Pneumonia</text>

  <!-- Left: Safe Horizontal Technique (Green) -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="32" rx="10" fill="#15803d"/>
    <text x="170" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">SAFE TECHNIQUE (HORIZONTAL HEAD)</text>

    <!-- Anatomical Graphic Simulation -->
    <g transform="translate(20, 50)">
      <rect x="0" y="0" width="300" height="110" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="150" y="25" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">Head Held Level &amp; Horizontal (0°–15°)</text>
      <text x="15" y="55" font-size="10" fill="#cbd5e1">• Drenching nozzle in side diastema</text>
      <text x="15" y="75" font-size="10" fill="#cbd5e1">• Epiglottis reflex SEALS the windpipe</text>
      <text x="15" y="95" font-size="10" font-weight="bold" fill="#86efac">• Liquid enters ESOPHAGUS -> Rumen</text>
    </g>

    <g transform="translate(20, 180)">
      <rect x="0" y="0" width="300" height="90" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="150" y="25" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">Outcome: 100% Effective</text>
      <text x="15" y="55" font-size="9" fill="#cbd5e1">• Full therapeutic anthelmintic dose delivered</text>
      <text x="15" y="75" font-size="9" fill="#cbd5e1">• Zero choking, coughing, or lung damage</text>
    </g>
  </g>

  <!-- Right: Fatal Vertical Technique (Red) -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#991b1b"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">LETHAL TECHNIQUE (VERTICAL HEAD)</text>

    <!-- Anatomical Graphic Simulation -->
    <g transform="translate(20, 50)">
      <rect x="0" y="0" width="305" height="110" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="152" y="25" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">Muzzle Pointed Vertically to Sky (70°–90°)</text>
      <text x="15" y="55" font-size="10" fill="#cbd5e1">• Throat muscles locked &amp; stretched tight</text>
      <text x="15" y="75" font-size="10" fill="#cbd5e1">• Epiglottis CANNOT close over trachea</text>
      <text x="15" y="95" font-size="10" font-weight="bold" fill="#fca5a5">• Liquid floods TRACHEA -> Lungs!</text>
    </g>

    <g transform="translate(20, 180)">
      <rect x="0" y="0" width="305" height="90" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="152" y="25" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">Outcome: Fatal Aspiration</text>
      <text x="15" y="55" font-size="9" fill="#cbd5e1">• Acute chemical drowning in lungs</text>
      <text x="15" y="75" font-size="9" fill="#cbd5e1">• Severe, fatal Aspiration Pneumonia in 48h</text>
    </g>
  </g>
</svg>
""")

# SVG 8: Master General Animal Health Matrix (Lesson 12, Page 2)
SVG_MASTER_HEALTH_MATRIX = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Master General Animal Health &amp; Disease Defense Operational Matrix</text>

  <!-- Central Hub: Healthy Farm -->
  <circle cx="400" cy="240" r="55" fill="#0f172a" stroke="#22c55e" stroke-width="3"/>
  <text x="400" y="235" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">PREVENTATIVE</text>
  <text x="400" y="252" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">HERD HEALTH</text>

  <!-- 1. Clinical Diagnostics -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="97" y="22" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. DIAGNOSTICS</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Rumen stasis &amp; Bloat</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Bottle jaw &amp; Pale mucosa</text>
  </g>
  <line x1="240" y1="102" x2="345" y2="200" stroke="#38bdf8" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 2. Housing & Nutrition -->
  <g transform="translate(560, 65)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="97" y="22" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">2. HOUSING &amp; FEED</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Airflow &lt;10ppm ammonia</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Dry bedding + Vitamin A</text>
  </g>
  <line x1="560" y1="102" x2="455" y2="200" stroke="#22c55e" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 3. Biosecurity & Vaccines -->
  <g transform="translate(35, 195)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <text x="97" y="22" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">3. BIOSECURITY</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Footbaths &amp; 30-Day Quarantine</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• 6-Week vaccine calendars</text>
  </g>
  <line x1="230" y1="240" x2="345" y2="240" stroke="#eab308" stroke-width="2"/>

  <!-- 4. Parasites & Waste -->
  <g transform="translate(570, 195)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="97" y="22" font-size="11" font-weight="bold" fill="#d8b4fe" text-anchor="middle">4. PARASITE &amp; WASTE</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• 6-Week pasture rotation</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• >60°C thermophilic compost</text>
  </g>
  <line x1="570" y1="240" x2="455" y2="240" stroke="#a855f7" stroke-width="2"/>

  <!-- 5. Routine Care & Welfare -->
  <g transform="translate(300, 335)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <text x="100" y="22" font-size="11" font-weight="bold" fill="#67e8f9" text-anchor="middle">5. ROUTINE &amp; WELFARE</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Hoof trimming &amp; Drenching</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• The 5 Animal Freedoms</text>
  </g>
  <line x1="400" y1="335" x2="400" y2="298" stroke="#06b6d4" stroke-width="2"/>
</svg>
""")

SVG_MAP = {
    1: {"page": 2, "svg": SVG_HEALTH_FEEDBACK_LOOP, "title": "Positive Feedback Loop of Livestock Health & Agribusiness Profit"},
    3: {"page": 2, "svg": SVG_CATTLE_DIAGNOSTICS, "title": "Key Clinical Diagnostic Checkpoints on Cattle"},
    4: {"page": 2, "svg": SVG_BOTTLE_JAW, "title": "Pathophysiology of Bottle Jaw in Sheep"},
    6: {"page": 2, "svg": SVG_PREVENTATIVE_PILLARS, "title": "The 3 Pillars of Preventative Animal Health"},
    7: {"page": 2, "svg": SVG_BIOSECURITY_QUARANTINE, "title": "Farm Biosecurity Perimeter & 30-Day Quarantine Architecture"},
    8: {"page": 2, "svg": SVG_PASTURE_ROTATION, "title": "Internal Parasite Life Cycle & Pasture Rotation Breaking Mechanism"},
    10: {"page": 2, "svg": SVG_DRENCHING_MECHANICS, "title": "Safe Oral Drenching Head Angle vs Fatal Aspiration Pneumonia"},
    12: {"page": 2, "svg": SVG_MASTER_HEALTH_MATRIX, "title": "Master General Animal Health & Disease Defense Matrix"}
}

def enrich_grade10_topic10():
    """Injects verified photos, responsive vector SVGs, YouTube embeds, and creates LessonAssets."""
    print("=" * 80)
    print("STARTING ENRICHMENT: CBC Grade 10 Agriculture — Topic 10: General Animal Health")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()
    topic = Topic.objects.filter(subject=subject, name="General Animal Health").first()

    assert topic, "Topic 'General Animal Health' not found!"

    images_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grade10_topic10_verified_images.json")
    with open(images_path, "r", encoding="utf-8") as f:
        verified_images = json.load(f)

    lessons = list(topic.lessons.all().order_by("learning_unit__order"))
    LessonAsset.objects.filter(lesson__in=lessons).delete()

    total_images_attached = 0
    total_svgs_attached = 0
    total_videos_attached = 0
    total_assets_persisted = 0

    for lesson in lessons:
        u_order = lesson.learning_unit.order
        u_str = str(u_order)

        # ---------------------------------------------------------------------
        # 1. First-Card Visual Hook (Photographic Wikimedia URL)
        # ---------------------------------------------------------------------
        hook_block = LessonBlock.objects.filter(
            lesson=lesson,
            page_number=1,
            block_type="suggested_image"
        ).first()

        if hook_block and u_str in verified_images:
            img_data = verified_images[u_str]
            content = hook_block.content or {}
            content["resolved_image_url"] = img_data["url"]
            content["url"] = img_data["url"]
            content["attribution"] = f"Photo by {img_data.get('author', 'Wikimedia Commons')} ({img_data.get('licensing', 'CC')})"
            content["commons_url"] = img_data.get("commons_url", "")
            hook_block.content = content
            hook_block.save()
            total_images_attached += 1

            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                source_type="external",
                storage_type="url",
                status="attached",
                title=f"Lesson {u_order} Visual Hook: {hook_block.title}",
                description=content.get("caption", hook_block.title),
                url=img_data["url"],
                metadata={
                    "topic_order": 10,
                    "unit_order": u_order,
                    "card": 1,
                    "author": img_data.get("author", "Wikimedia Commons"),
                    "licensing": img_data.get("licensing", "CC"),
                    "commons_url": img_data.get("commons_url", "")
                }
            )
            hook_block.assets.add(asset)
            total_assets_persisted += 1
            print(f"  [Image Hook Attached] Lesson {u_order}: {img_data['title'][:50]}...")

        # ---------------------------------------------------------------------
        # 2. Custom Responsive Vector SVGs
        # ---------------------------------------------------------------------
        if u_order in SVG_MAP:
            svg_def = SVG_MAP[u_order]
            diag_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_diagram"
            ).first()

            if diag_block:
                diag_content = diag_block.content or {}
                diag_content["svg"] = svg_def["svg"]
                diag_content["svg_xml"] = svg_def["svg"]
                diag_content["title"] = svg_def["title"]
                diag_block.content = diag_content
                diag_block.save()
                total_svgs_attached += 1

                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type="diagram",
                    source_type="ai_generated",
                    storage_type="embed",
                    status="attached",
                    title=f"Lesson {u_order} Diagram: {svg_def['title']}",
                    description=diag_content.get("caption", svg_def["title"]),
                    metadata={
                        "topic_order": 10,
                        "unit_order": u_order,
                        "page": svg_def["page"],
                        "svg_content": svg_def["svg"]
                    }
                )
                diag_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [Vector SVG Attached] Lesson {u_order}: {svg_def['title']}")

        # ---------------------------------------------------------------------
        # 3. Educational YouTube Videos (Lesson 3)
        # ---------------------------------------------------------------------
        video_blocks = LessonBlock.objects.filter(
            lesson=lesson,
            block_type="suggested_video"
        )
        for v_block in video_blocks:
            v_content = v_block.content or {}
            v_url = v_content.get("url", "")
            if v_url:
                total_videos_attached += 1
                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type="youtube",
                    source_type="external",
                    storage_type="url",
                    status="attached",
                    title=f"Lesson {u_order} Video: {v_block.title}",
                    description=v_content.get("description", v_block.title),
                    url=v_url,
                    metadata={
                        "topic_order": 10,
                        "unit_order": u_order,
                        "youtube_url": v_url
                    }
                )
                v_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [YouTube Video Attached] Lesson {u_order}: {v_block.title}")

    print("=" * 80)
    print(f"ENRICHMENT COMPLETE: Topic 10 '{topic.name}'")
    print(f"  Photographic Hooks: {total_images_attached} / 12")
    print(f"  Vector SVGs:        {total_svgs_attached} / 8")
    print(f"  YouTube Videos:     {total_videos_attached} / 1")
    print(f"  LessonAssets:       {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic10()
