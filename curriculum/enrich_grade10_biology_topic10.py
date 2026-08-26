"""
VLearn Grade 10 Biology — Topic 10: Animal Gaseous Exchange and Respiration
Visual Enrichment Engine v1.0

Attaches to each of the 5 lessons:
  1. Detailed biological vector SVG (inline embedded)
  2. Contextualized Wikimedia Commons photograph
  3. Curated educational YouTube video (verified)

Lesson IDs: 1273, 1274, 1275, 1276, 1277

Usage:
  ./venv/bin/python curriculum/enrich_grade10_biology_topic10.py [--replace]
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.db import transaction
from curriculum.models import Lesson, LessonBlock, LessonAsset

# ─────────────────────────────────────────────────────────────────────────────
# SVG DEFINITIONS — One rich, vibrant, labeled vector diagram per lesson
# ─────────────────────────────────────────────────────────────────────────────

SVG_L1_COUNTER_CURRENT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" font-family="Arial, sans-serif">
  <rect width="900" height="460" fill="#f0f8ff" rx="12"/>
  <text x="450" y="28" text-anchor="middle" font-size="16" font-weight="bold" fill="#1a1a2e">Counter-Current vs Parallel Flow: Why Fish Gills Extract Up to 80% of Dissolved Oxygen</text>

  <!-- ───── PART A: PARALLEL FLOW (left panel) ───── -->
  <rect x="20" y="45" width="410" height="390" rx="10" fill="#FFEBEE" stroke="#E53935" stroke-width="1.5"/>
  <text x="225" y="68" text-anchor="middle" font-size="13" font-weight="bold" fill="#B71C1C">A. Parallel Flow (Inefficient)</text>
  <text x="225" y="84" text-anchor="middle" font-size="11" fill="#B71C1C">Water and Blood flow in SAME direction</text>

  <!-- Water channel (top) -->
  <rect x="50" y="100" width="350" height="42" rx="8" fill="#4FC3F7"/>
  <text x="55" y="122" font-size="11" font-weight="bold" fill="white">WATER FLOW →</text>
  <!-- O2 % labels on water -->
  <text x="66" y="98" font-size="10" fill="#0277BD" font-weight="bold">100%</text>
  <text x="160" y="98" font-size="10" fill="#0277BD">75%</text>
  <text x="252" y="98" font-size="10" fill="#0277BD">55%</text>
  <text x="348" y="98" font-size="10" fill="#0277BD">50%</text>

  <!-- Water arrow -->
  <line x1="50" y1="121" x2="390" y2="121" stroke="white" stroke-width="2.5" stroke-dasharray="0"/>
  <polygon points="385,116 400,121 385,126" fill="white"/>

  <!-- Membrane (grey bar) -->
  <rect x="50" y="144" width="350" height="14" rx="4" fill="#BDBDBD"/>
  <text x="225" y="155" text-anchor="middle" font-size="9" fill="#333" font-weight="bold">LAMELLA WALL (Gas Exchange Membrane)</text>

  <!-- Blood channel (bottom — same direction) -->
  <rect x="50" y="158" width="350" height="42" rx="8" fill="#EF5350"/>
  <text x="55" y="180" font-size="11" font-weight="bold" fill="white">BLOOD FLOW →</text>
  <!-- O2 % labels on blood -->
  <text x="66" y="208" font-size="10" fill="#B71C1C" font-weight="bold">5%</text>
  <text x="155" y="208" font-size="10" fill="#B71C1C">30%</text>
  <text x="248" y="208" font-size="10" fill="#B71C1C">45%</text>
  <text x="348" y="208" font-size="10" fill="#B71C1C">50%</text>
  <line x1="50" y1="179" x2="390" y2="179" stroke="white" stroke-width="2.5"/>
  <polygon points="385,174 400,179 385,184" fill="white"/>

  <!-- Equalization point marker -->
  <line x1="290" y1="95" x2="290" y2="215" stroke="#B71C1C" stroke-width="1.5" stroke-dasharray="5,3"/>
  <text x="295" y="232" font-size="9" fill="#B71C1C" font-weight="bold">Concentrations equalize at 50% here</text>
  <text x="295" y="244" font-size="9" fill="#B71C1C">→ Net diffusion STOPS!</text>

  <!-- Diffusion arrows (reducing from left to right) -->
  <text x="95" y="152" text-anchor="middle" font-size="14" fill="#2E7D32">↓</text>
  <text x="155" y="152" text-anchor="middle" font-size="12" fill="#4CAF50">↓</text>
  <text x="215" y="152" text-anchor="middle" font-size="11" fill="#81C784">↓</text>
  <text x="275" y="152" text-anchor="middle" font-size="9" fill="#C8E6C9">↓</text>
  <!-- No diffusion marker at far right -->
  <text x="355" y="152" text-anchor="middle" font-size="16" fill="#E53935">✗</text>

  <!-- Result box -->
  <rect x="50" y="270" width="350" height="60" rx="8" fill="#FFCDD2" stroke="#E53935"/>
  <text x="225" y="292" text-anchor="middle" font-size="12" font-weight="bold" fill="#B71C1C">RESULT: Only ~50% O₂ Extraction</text>
  <text x="225" y="308" text-anchor="middle" font-size="10" fill="#C62828">Diffusion stops once concentrations equalize.</text>
  <text x="225" y="322" text-anchor="middle" font-size="10" fill="#C62828">The right half of the lamella extracts nothing.</text>

  <!-- ───── PART B: COUNTER-CURRENT FLOW (right panel) ───── -->
  <rect x="450" y="45" width="430" height="390" rx="10" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1.5"/>
  <text x="665" y="68" text-anchor="middle" font-size="13" font-weight="bold" fill="#1B5E20">B. Counter-Current Flow (Efficient)</text>
  <text x="665" y="84" text-anchor="middle" font-size="11" fill="#1B5E20">Water and Blood flow in OPPOSITE directions</text>

  <!-- Water channel (top — left to right) -->
  <rect x="480" y="100" width="370" height="42" rx="8" fill="#4FC3F7"/>
  <text x="490" y="122" font-size="11" font-weight="bold" fill="white">WATER FLOW →</text>
  <text x="492" y="98" font-size="10" fill="#0277BD" font-weight="bold">100%</text>
  <text x="582" y="98" font-size="10" fill="#0277BD">70%</text>
  <text x="672" y="98" font-size="10" fill="#0277BD">40%</text>
  <text x="800" y="98" font-size="10" fill="#0277BD">15%</text>
  <line x1="480" y1="121" x2="840" y2="121" stroke="white" stroke-width="2.5"/>
  <polygon points="835,116 850,121 835,126" fill="white"/>

  <!-- Membrane -->
  <rect x="480" y="144" width="370" height="14" rx="4" fill="#BDBDBD"/>
  <text x="665" y="155" text-anchor="middle" font-size="9" fill="#333" font-weight="bold">LAMELLA WALL (Gas Exchange Membrane)</text>

  <!-- Blood channel (bottom — RIGHT to LEFT — opposite direction!) -->
  <rect x="480" y="158" width="370" height="42" rx="8" fill="#EF5350"/>
  <text x="650" y="180" font-size="11" font-weight="bold" fill="white">← BLOOD FLOW</text>
  <text x="492" y="208" font-size="10" fill="#B71C1C" font-weight="bold">85%</text>
  <text x="582" y="208" font-size="10" fill="#B71C1C">60%</text>
  <text x="672" y="208" font-size="10" fill="#B71C1C">30%</text>
  <text x="800" y="208" font-size="10" fill="#B71C1C">5%</text>
  <line x1="850" y1="179" x2="490" y2="179" stroke="white" stroke-width="2.5"/>
  <polygon points="495,174 480,179 495,184" fill="white"/>

  <!-- Diffusion arrows — EQUAL MAGNITUDE throughout! -->
  <text x="525" y="152" text-anchor="middle" font-size="14" fill="#2E7D32">↓</text>
  <text x="615" y="152" text-anchor="middle" font-size="14" fill="#2E7D32">↓</text>
  <text x="705" y="152" text-anchor="middle" font-size="14" fill="#2E7D32">↓</text>
  <text x="810" y="152" text-anchor="middle" font-size="14" fill="#2E7D32">↓</text>

  <!-- Gradient explanation annotations -->
  <text x="525" y="240" text-anchor="middle" font-size="9" fill="#1B5E20">100% vs 85%</text>
  <text x="525" y="250" text-anchor="middle" font-size="9" fill="#1B5E20">→ gradient 15%</text>
  <text x="615" y="240" text-anchor="middle" font-size="9" fill="#1B5E20">70% vs 60%</text>
  <text x="615" y="250" text-anchor="middle" font-size="9" fill="#1B5E20">→ gradient 10%</text>
  <text x="705" y="240" text-anchor="middle" font-size="9" fill="#1B5E20">40% vs 30%</text>
  <text x="705" y="250" text-anchor="middle" font-size="9" fill="#1B5E20">→ gradient 10%</text>
  <text x="810" y="240" text-anchor="middle" font-size="9" fill="#1B5E20">15% vs 5%</text>
  <text x="810" y="250" text-anchor="middle" font-size="9" fill="#1B5E20">→ gradient 10%</text>

  <!-- Result box -->
  <rect x="480" y="270" width="370" height="60" rx="8" fill="#C8E6C9" stroke="#2E7D32"/>
  <text x="665" y="292" text-anchor="middle" font-size="12" font-weight="bold" fill="#1B5E20">RESULT: Up to 80% O₂ Extraction!</text>
  <text x="665" y="308" text-anchor="middle" font-size="10" fill="#2E7D32">Gradient maintained along ENTIRE lamella length.</text>
  <text x="665" y="322" text-anchor="middle" font-size="10" fill="#2E7D32">Continuous diffusion — never equilibrates.</text>

  <!-- Bottom comparison summary -->
  <rect x="20" y="442" width="860" height="14" rx="4" fill="#E3F2FD" stroke="#1565C0"/>
  <text x="450" y="453" text-anchor="middle" font-size="10" fill="#0D47A1">Counter-current flow is found in fish gills, mammalian placenta, and bird legs for heat exchange — a universal biological optimization strategy.</text>
</svg>"""

SVG_L2_HUMAN_LUNG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 480" font-family="Arial, sans-serif">
  <rect width="900" height="480" fill="#fafafa" rx="12"/>
  <text x="450" y="28" text-anchor="middle" font-size="16" font-weight="bold" fill="#1a1a2e">Human Respiratory System: Anatomy and Alveolar Gas Exchange Mechanism</text>

  <!-- ────── LEFT PANEL: Respiratory anatomy ────── -->
  <!-- Nasal cavity -->
  <rect x="310" y="50" width="80" height="45" rx="8" fill="#FFE0B2" stroke="#E65100" stroke-width="1.5"/>
  <text x="350" y="70" text-anchor="middle" font-size="10" fill="#BF360C" font-weight="bold">Nasal Cavity</text>
  <text x="350" y="82" text-anchor="middle" font-size="9" fill="#BF360C">Cilia + Mucus</text>

  <!-- Trachea -->
  <rect x="330" y="100" width="40" height="100" rx="6" fill="#FFCC80" stroke="#E65100" stroke-width="1.5"/>
  <text x="350" y="135" text-anchor="middle" font-size="9" fill="#BF360C" font-weight="bold">Trachea</text>
  <!-- Cartilage rings -->
  <rect x="328" y="108" width="44" height="6" rx="2" fill="#FFB74D"/>
  <rect x="328" y="120" width="44" height="6" rx="2" fill="#FFB74D"/>
  <rect x="328" y="132" width="44" height="6" rx="2" fill="#FFB74D"/>
  <rect x="328" y="144" width="44" height="6" rx="2" fill="#FFB74D"/>
  <rect x="328" y="156" width="44" height="6" rx="2" fill="#FFB74D"/>
  <text x="380" y="130" font-size="8" fill="#E65100">← Cartilage rings</text>

  <!-- Bronchi split -->
  <path d="M330 200 Q290 225 250 230" stroke="#FF9800" stroke-width="10" fill="none" stroke-linecap="round"/>
  <path d="M370 200 Q410 225 450 230" stroke="#FF9800" stroke-width="10" fill="none" stroke-linecap="round"/>
  <text x="220" y="248" font-size="9" fill="#E65100" font-weight="bold">Left Bronchus</text>
  <text x="440" y="248" font-size="9" fill="#E65100" font-weight="bold">Right Bronchus</text>

  <!-- Left Lung -->
  <ellipse cx="200" cy="320" rx="130" ry="100" fill="#FFCDD2" stroke="#E53935" stroke-width="2" opacity="0.85"/>
  <text x="200" y="298" text-anchor="middle" font-size="12" font-weight="bold" fill="#B71C1C">Left Lung</text>
  <text x="200" y="314" text-anchor="middle" font-size="9" fill="#B71C1C">Bronchioles</text>
  <text x="200" y="328" text-anchor="middle" font-size="9" fill="#B71C1C">→ Alveoli</text>
  <!-- Bronchiole branching inside left lung -->
  <line x1="200" y1="255" x2="200" y2="290" stroke="#E53935" stroke-width="3"/>
  <line x1="200" y1="278" x2="175" y2="295" stroke="#E53935" stroke-width="2"/>
  <line x1="200" y1="278" x2="225" y2="295" stroke="#E53935" stroke-width="2"/>
  <line x1="175" y1="295" x2="160" y2="310" stroke="#E53935" stroke-width="1.5"/>
  <line x1="175" y1="295" x2="185" y2="313" stroke="#E53935" stroke-width="1.5"/>
  <line x1="225" y1="295" x2="215" y2="313" stroke="#E53935" stroke-width="1.5"/>
  <line x1="225" y1="295" x2="240" y2="310" stroke="#E53935" stroke-width="1.5"/>

  <!-- Right Lung -->
  <ellipse cx="500" cy="320" rx="130" ry="100" fill="#FFCDD2" stroke="#E53935" stroke-width="2" opacity="0.85"/>
  <text x="500" y="298" text-anchor="middle" font-size="12" font-weight="bold" fill="#B71C1C">Right Lung</text>
  <text x="500" y="314" text-anchor="middle" font-size="9" fill="#B71C1C">300 million alveoli</text>
  <text x="500" y="328" text-anchor="middle" font-size="9" fill="#B71C1C">~70 m² total area</text>
  <line x1="500" y1="255" x2="500" y2="290" stroke="#E53935" stroke-width="3"/>
  <line x1="500" y1="278" x2="475" y2="295" stroke="#E53935" stroke-width="2"/>
  <line x1="500" y1="278" x2="525" y2="295" stroke="#E53935" stroke-width="2"/>
  <line x1="475" y1="295" x2="460" y2="310" stroke="#E53935" stroke-width="1.5"/>
  <line x1="475" y1="295" x2="485" y2="313" stroke="#E53935" stroke-width="1.5"/>
  <line x1="525" y1="295" x2="515" y2="313" stroke="#E53935" stroke-width="1.5"/>
  <line x1="525" y1="295" x2="540" y2="310" stroke="#E53935" stroke-width="1.5"/>

  <!-- Diaphragm -->
  <path d="M60 430 Q200 415 350 425 Q450 435 640 428 Q700 425 780 430" stroke="#795548" stroke-width="5" fill="none" stroke-linecap="round"/>
  <text x="350" y="450" text-anchor="middle" font-size="11" font-weight="bold" fill="#4E342E">Diaphragm (skeletal muscle) — contracts to flatten during inhalation</text>

  <!-- Rib cage outline -->
  <rect x="60" y="120" width="580" height="300" rx="60" fill="none" stroke="#90A4AE" stroke-width="2" stroke-dasharray="8,5"/>
  <text x="100" y="145" font-size="9" fill="#607D8B">Rib cage / Thoracic cavity</text>

  <!-- ────── RIGHT PANEL: Alveolus zoom-in ────── -->
  <rect x="680" y="45" width="200" height="390" rx="10" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1.5"/>
  <text x="780" y="68" text-anchor="middle" font-size="12" font-weight="bold" fill="#1B5E20">Alveolus</text>
  <text x="780" y="82" text-anchor="middle" font-size="10" font-weight="bold" fill="#1B5E20">Structure-Function</text>

  <!-- Alveolus bubble -->
  <circle cx="780" cy="180" r="75" fill="#F1F8E9" stroke="#4CAF50" stroke-width="2.5"/>
  <text x="780" y="148" text-anchor="middle" font-size="9" fill="#333">Moist interior</text>
  <text x="780" y="162" text-anchor="middle" font-size="9" fill="#388E3C">O₂ dissolves → diffuses</text>
  <!-- Surfactant molecules (dots on inner surface) -->
  <circle cx="718" cy="165" r="4" fill="#AED581"/>
  <circle cx="712" cy="180" r="4" fill="#AED581"/>
  <circle cx="718" cy="195" r="4" fill="#AED581"/>
  <circle cx="840" cy="162" r="4" fill="#AED581"/>
  <circle cx="845" cy="178" r="4" fill="#AED581"/>
  <circle cx="840" cy="194" r="4" fill="#AED581"/>
  <text x="700" y="215" font-size="8" fill="#558B2F">Surfactant</text>
  <!-- Epithelial cell layer -->
  <ellipse cx="780" cy="256" rx="75" ry="6" fill="#C8E6C9" stroke="#4CAF50"/>
  <text x="780" y="268" text-anchor="middle" font-size="8" fill="#2E7D32">1-cell epithelium</text>

  <!-- Capillary -->
  <ellipse cx="780" cy="280" rx="60" ry="12" fill="#EF9A9A" stroke="#E53935"/>
  <text x="780" y="283" text-anchor="middle" font-size="8" fill="#B71C1C">Capillary (1-cell wall)</text>
  <!-- Red blood cells in capillary -->
  <ellipse cx="755" cy="280" rx="10" ry="7" fill="#C62828"/>
  <ellipse cx="780" cy="280" rx="10" ry="7" fill="#C62828"/>
  <ellipse cx="805" cy="280" rx="10" ry="7" fill="#C62828"/>

  <!-- Gas exchange arrows -->
  <text x="694" y="251" font-size="12" fill="#388E3C" font-weight="bold">O₂ ↓</text>
  <text x="845" y="251" font-size="12" fill="#FF5722" font-weight="bold">CO₂ ↑</text>

  <!-- 2-cell barrier label -->
  <line x1="700" y1="260" x2="680" y2="310" stroke="#555" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="688" y="325" font-size="9" fill="#333" text-anchor="middle">Only 2 cells</text>
  <text x="688" y="337" font-size="9" fill="#333" text-anchor="middle">thick (0.5 μm)</text>

  <!-- Pulmonary vessels -->
  <rect x="698" y="305" width="40" height="20" rx="4" fill="#1565C0"/>
  <text x="718" y="319" text-anchor="middle" font-size="8" fill="white">Pulmonary</text>
  <rect x="748" y="305" width="40" height="20" rx="4" fill="#C62828"/>
  <text x="768" y="319" text-anchor="middle" font-size="8" fill="white">Vein</text>
  <rect x="800" y="305" width="40" height="20" rx="4" fill="#1E88E5"/>
  <text x="820" y="319" text-anchor="middle" font-size="8" fill="white">Artery</text>

  <!-- Summary -->
  <text x="780" y="360" text-anchor="middle" font-size="10" fill="#1B5E20" font-weight="bold">Adaptations:</text>
  <text x="780" y="374" text-anchor="middle" font-size="9" fill="#333">1. Vast SA (~70 m²)</text>
  <text x="780" y="388" text-anchor="middle" font-size="9" fill="#333">2. Ultra-thin (2 cells)</text>
  <text x="780" y="402" text-anchor="middle" font-size="9" fill="#333">3. Moist lining</text>
  <text x="780" y="416" text-anchor="middle" font-size="9" fill="#333">4. Surfactant fluid</text>
  <text x="780" y="430" text-anchor="middle" font-size="9" fill="#333">5. Rich capillary network</text>
</svg>"""

SVG_L3_OXYGEN_DEBT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 440" font-family="Arial, sans-serif">
  <rect width="900" height="440" fill="#fafffe" rx="12"/>
  <text x="450" y="28" text-anchor="middle" font-size="16" font-weight="bold" fill="#1a1a2e">Oxygen Consumption Before, During, and After a 400-Metre Sprint</text>

  <!-- Graph area -->
  <rect x="80" y="50" width="780" height="290" rx="6" fill="white" stroke="#CFD8DC" stroke-width="1.5"/>

  <!-- Y-axis -->
  <line x1="80" y1="50" x2="80" y2="340" stroke="#555" stroke-width="2"/>
  <!-- Y-axis labels -->
  <text x="72" y="58" text-anchor="end" font-size="10" fill="#333">5.0</text>
  <text x="72" y="110" text-anchor="end" font-size="10" fill="#333">4.0</text>
  <text x="72" y="165" text-anchor="end" font-size="10" fill="#333">3.0</text>
  <text x="72" y="220" text-anchor="end" font-size="10" fill="#333">2.0</text>
  <text x="72" y="275" text-anchor="end" font-size="10" fill="#333">1.0</text>
  <text x="72" y="340" text-anchor="end" font-size="10" fill="#333">0.0</text>
  <!-- Y-axis grid lines -->
  <line x1="80" y1="110" x2="860" y2="110" stroke="#ECEFF1" stroke-width="1"/>
  <line x1="80" y1="165" x2="860" y2="165" stroke="#ECEFF1" stroke-width="1"/>
  <line x1="80" y1="220" x2="860" y2="220" stroke="#ECEFF1" stroke-width="1"/>
  <line x1="80" y1="275" x2="860" y2="275" stroke="#ECEFF1" stroke-width="1"/>
  <!-- Y-axis title -->
  <text transform="rotate(-90,25,195)" x="25" y="195" text-anchor="middle" font-size="11" fill="#333" font-weight="bold">Oxygen Consumption (L/min)</text>

  <!-- X-axis -->
  <line x1="80" y1="340" x2="860" y2="340" stroke="#555" stroke-width="2"/>
  <text x="470" y="365" text-anchor="middle" font-size="11" fill="#333" font-weight="bold">Time (minutes)</text>

  <!-- Phase divider lines -->
  <line x1="260" y1="50" x2="260" y2="340" stroke="#90A4AE" stroke-width="1.5" stroke-dasharray="6,4"/>
  <line x1="560" y1="50" x2="560" y2="340" stroke="#90A4AE" stroke-width="1.5" stroke-dasharray="6,4"/>

  <!-- Phase labels -->
  <rect x="100" y="52" width="140" height="22" rx="4" fill="#E8F5E9"/>
  <text x="170" y="67" text-anchor="middle" font-size="11" font-weight="bold" fill="#2E7D32">REST (0–2 min)</text>
  <rect x="290" y="52" width="240" height="22" rx="4" fill="#FFEBEE"/>
  <text x="410" y="67" text-anchor="middle" font-size="11" font-weight="bold" fill="#B71C1C">EXERCISE (2–8 min)</text>
  <rect x="590" y="52" width="240" height="22" rx="4" fill="#E3F2FD"/>
  <text x="710" y="67" text-anchor="middle" font-size="11" font-weight="bold" fill="#1565C0">RECOVERY (8–16 min)</text>

  <!-- Resting O2 demand line (dotted baseline) -->
  <line x1="80" y1="302" x2="860" y2="302" stroke="#4CAF50" stroke-width="2" stroke-dasharray="8,5"/>
  <text x="870" y="306" font-size="9" fill="#2E7D32" font-weight="bold">Resting O₂</text>
  <text x="870" y="317" font-size="9" fill="#2E7D32">demand</text>
  <!-- Resting O2 = 0.5 L/min, y = 302 (scale: 50px per L/min, baseline 340) -->

  <!-- ACTUAL O2 CONSUMPTION CURVE -->
  <!-- Rest phase: flat at 0.5 L/min (y=302) -->
  <polyline points="80,302 260,302" stroke="#1565C0" stroke-width="3" fill="none"/>
  <!-- Exercise phase: sharp rise to 4.0 L/min (y=110), plateau-like -->
  <path d="M260,302 Q295,220 340,140 Q380,100 460,108 Q500,110 560,115" stroke="#1565C0" stroke-width="3" fill="none"/>
  <!-- Recovery: gradual exponential decay back to baseline -->
  <path d="M560,115 Q600,160 640,200 Q700,255 760,285 Q820,300 860,302" stroke="#1565C0" stroke-width="3" fill="none"/>

  <!-- OXYGEN DEFICIT (shaded area — exercise phase, gap between demand and actual) -->
  <!-- From exercise start (260) to rise, gap between curve and where it WOULD be if supply matched demand -->
  <!-- Shade area between red "O2 demand during exercise" line and actual O2 curve -->
  <rect x="262" y="100" width="10" height="0" fill="none"/>
  <!-- Exercise O2 demand at max: ~4.5 L/min (y=85) — demand during sprint -->
  <line x1="260" y1="85" x2="560" y2="90" stroke="#E53935" stroke-width="1.5" stroke-dasharray="5,3"/>
  <text x="310" y="80" font-size="9" fill="#E53935" font-weight="bold">Max O₂ demand during exercise</text>

  <!-- Shade the oxygen deficit area (between max demand and actual intake during exercise) -->
  <path d="M260,302 Q295,220 340,140 Q380,100 460,108 Q500,110 560,115 L560,90 Q500,88 460,86 Q380,84 340,84 Q295,84 260,85 Z" fill="#FFCDD2" opacity="0.6"/>
  <text x="390" y="145" text-anchor="middle" font-size="11" font-weight="bold" fill="#C62828">Oxygen Deficit</text>
  <text x="390" y="159" text-anchor="middle" font-size="10" fill="#C62828">/ Debt Built Up</text>
  <text x="390" y="173" text-anchor="middle" font-size="10" fill="#C62828">(Anaerobic respiration</text>
  <text x="390" y="185" text-anchor="middle" font-size="10" fill="#C62828">supplements ATP)</text>

  <!-- Shade the oxygen debt repayment area (recovery phase — above resting demand) -->
  <path d="M560,115 Q600,160 640,200 Q700,255 760,285 Q820,300 860,302 L860,302 L560,302 Z" fill="#BBDEFB" opacity="0.7"/>
  <text x="710" y="248" text-anchor="middle" font-size="11" font-weight="bold" fill="#0D47A1">Oxygen Debt</text>
  <text x="710" y="262" text-anchor="middle" font-size="10" fill="#0D47A1">Repayment</text>
  <text x="710" y="276" text-anchor="middle" font-size="10" fill="#0D47A1">(Lactic acid oxidized</text>
  <text x="710" y="288" text-anchor="middle" font-size="10" fill="#0D47A1">in liver)</text>

  <!-- Lactic acid accumulation arrow -->
  <line x1="420" y1="200" x2="420" y2="225" stroke="#B71C1C" stroke-width="1.5" marker-end="url(#arrLactic)"/>
  <text x="420" y="240" text-anchor="middle" font-size="9" fill="#B71C1C">Lactic acid</text>
  <text x="420" y="252" text-anchor="middle" font-size="9" fill="#B71C1C">accumulates</text>
  <text x="420" y="264" text-anchor="middle" font-size="9" fill="#B71C1C">→ muscle cramps</text>

  <defs>
    <marker id="arrLactic" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto">
      <path d="M0,0 L0,6 L6,3 z" fill="#B71C1C"/>
    </marker>
  </defs>

  <!-- Legend -->
  <rect x="80" y="355" width="780" height="75" rx="8" fill="#FAFAFA" stroke="#CFD8DC"/>
  <line x1="100" y1="372" x2="135" y2="372" stroke="#1565C0" stroke-width="3"/>
  <text x="145" y="376" font-size="11" fill="#333">Actual O₂ Consumption Curve</text>
  <line x1="100" y1="392" x2="135" y2="392" stroke="#E53935" stroke-width="1.5" stroke-dasharray="5,3"/>
  <text x="145" y="396" font-size="11" fill="#333">Max O₂ Demand During Exercise</text>
  <line x1="100" y1="412" x2="135" y2="412" stroke="#4CAF50" stroke-width="2" stroke-dasharray="8,5"/>
  <text x="145" y="416" font-size="11" fill="#333">Resting O₂ Demand Baseline</text>
  <rect x="450" y="362" width="14" height="14" fill="#FFCDD2" stroke="#C62828"/>
  <text x="475" y="374" font-size="11" fill="#333">Oxygen Deficit (Anaerobic phase — lactic acid builds up)</text>
  <rect x="450" y="382" width="14" height="14" fill="#BBDEFB" stroke="#1565C0"/>
  <text x="475" y="394" font-size="11" fill="#333">Oxygen Debt Repayment (Recovery — liver oxidizes lactic acid)</text>
</svg>"""

SVG_L4_RQ = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 440" font-family="Arial, sans-serif">
  <rect width="900" height="440" fill="#fafffe" rx="12"/>
  <text x="450" y="28" text-anchor="middle" font-size="16" font-weight="bold" fill="#1a1a2e">Respiratory Quotient (RQ): Energy Values and Calculation Guide for 3 Substrates</text>

  <!-- ── CARBOHYDRATES Panel ── -->
  <rect x="20" y="48" width="268" height="300" rx="10" fill="#FFF8E1" stroke="#F57F17" stroke-width="2"/>
  <text x="154" y="72" text-anchor="middle" font-size="14" font-weight="bold" fill="#E65100">CARBOHYDRATES</text>
  <text x="154" y="90" text-anchor="middle" font-size="11" fill="#BF360C">Primary Fuel — 17.0 kJ/g</text>

  <!-- Glucose molecule representation (hexagon) -->
  <polygon points="154,105 180,120 180,150 154,165 128,150 128,120" fill="#FFE082" stroke="#F57F17" stroke-width="2"/>
  <text x="154" y="138" text-anchor="middle" font-size="10" fill="#E65100" font-weight="bold">C₆H₁₂O₆</text>
  <text x="154" y="152" text-anchor="middle" font-size="9" fill="#E65100">Glucose</text>

  <!-- Equation -->
  <rect x="32" y="175" width="244" height="52" rx="6" fill="#FFCC02" opacity="0.5"/>
  <text x="154" y="194" text-anchor="middle" font-size="10" font-weight="bold" fill="#1a1a2e">C₆H₁₂O₆ + 6O₂ →</text>
  <text x="154" y="210" text-anchor="middle" font-size="10" font-weight="bold" fill="#1a1a2e">6CO₂ + 6H₂O + 38 ATP</text>

  <!-- RQ calculation -->
  <rect x="32" y="236" width="244" height="55" rx="6" fill="#FFF3E0" stroke="#FF9800"/>
  <text x="154" y="254" text-anchor="middle" font-size="10" fill="#333">RQ = CO₂ produced / O₂ consumed</text>
  <text x="154" y="270" text-anchor="middle" font-size="10" fill="#333">RQ = 6 / 6</text>
  <text x="154" y="286" text-anchor="middle" font-size="14" font-weight="bold" fill="#E65100">RQ = 1.0</text>

  <!-- Significance -->
  <text x="154" y="312" text-anchor="middle" font-size="10" fill="#BF360C" font-weight="bold">Interpretation:</text>
  <text x="154" y="326" text-anchor="middle" font-size="10" fill="#555">Burning carbohydrates exclusively.</text>
  <text x="154" y="340" text-anchor="middle" font-size="10" fill="#555">Expected after carbohydrate-rich meal.</text>

  <!-- ── LIPIDS Panel ── -->
  <rect x="316" y="48" width="268" height="300" rx="10" fill="#F3E5F5" stroke="#7B1FA2" stroke-width="2"/>
  <text x="450" y="72" text-anchor="middle" font-size="14" font-weight="bold" fill="#4A148C">LIPIDS (FATS)</text>
  <text x="450" y="90" text-anchor="middle" font-size="11" fill="#6A1B9A">Long-term Fuel — 38.0 kJ/g</text>

  <!-- Fat droplet representation -->
  <ellipse cx="450" cy="133" rx="40" ry="30" fill="#CE93D8" stroke="#7B1FA2" stroke-width="2"/>
  <text x="450" y="128" text-anchor="middle" font-size="10" fill="white" font-weight="bold">Tripalmitin</text>
  <text x="450" y="142" text-anchor="middle" font-size="9" fill="white">C₅₁H₉₈O₆</text>

  <!-- Equation -->
  <rect x="328" y="175" width="244" height="52" rx="6" fill="#BA68C8" opacity="0.4"/>
  <text x="450" y="194" text-anchor="middle" font-size="10" font-weight="bold" fill="#1a1a2e">2C₅₁H₉₈O₆ + 145O₂ →</text>
  <text x="450" y="210" text-anchor="middle" font-size="10" font-weight="bold" fill="#1a1a2e">102CO₂ + 98H₂O + ATP</text>

  <!-- RQ calculation -->
  <rect x="328" y="236" width="244" height="55" rx="6" fill="#EDE7F6" stroke="#7B1FA2"/>
  <text x="450" y="254" text-anchor="middle" font-size="10" fill="#333">RQ = CO₂ produced / O₂ consumed</text>
  <text x="450" y="270" text-anchor="middle" font-size="10" fill="#333">RQ = 102 / 145</text>
  <text x="450" y="286" text-anchor="middle" font-size="14" font-weight="bold" fill="#4A148C">RQ = 0.70</text>

  <!-- Significance -->
  <text x="450" y="312" text-anchor="middle" font-size="10" fill="#4A148C" font-weight="bold">Interpretation:</text>
  <text x="450" y="326" text-anchor="middle" font-size="10" fill="#555">Burning fats — needs MORE O₂ per</text>
  <text x="450" y="340" text-anchor="middle" font-size="10" fill="#555">unit energy (lipids are oxygen-poor).</text>

  <!-- ── PROTEINS Panel ── -->
  <rect x="612" y="48" width="268" height="300" rx="10" fill="#E8F5E9" stroke="#2E7D32" stroke-width="2"/>
  <text x="746" y="72" text-anchor="middle" font-size="14" font-weight="bold" fill="#1B5E20">PROTEINS</text>
  <text x="746" y="90" text-anchor="middle" font-size="11" fill="#2E7D32">Emergency Fuel — 22.0 kJ/g</text>

  <!-- Protein chain representation -->
  <g transform="translate(690,100)">
    <circle cx="0" cy="0" r="12" fill="#81C784" stroke="#2E7D32"/>
    <circle cx="30" cy="5" r="12" fill="#66BB6A" stroke="#2E7D32"/>
    <circle cx="60" cy="0" r="12" fill="#4CAF50" stroke="#2E7D32"/>
    <circle cx="90" cy="5" r="12" fill="#43A047" stroke="#2E7D32"/>
    <text x="45" y="35" text-anchor="middle" font-size="9" fill="#1B5E20">Amino acid chain</text>
    <text x="45" y="47" text-anchor="middle" font-size="9" fill="#1B5E20">DEAMINATED in liver</text>
  </g>

  <!-- Equation -->
  <rect x="624" y="175" width="244" height="52" rx="6" fill="#A5D6A7" opacity="0.6"/>
  <text x="746" y="192" text-anchor="middle" font-size="10" font-weight="bold" fill="#1a1a2e">Amino acids → Deamination</text>
  <text x="746" y="208" text-anchor="middle" font-size="10" font-weight="bold" fill="#1a1a2e">→ Urea (excreted) + Keto-acids</text>

  <!-- RQ calculation -->
  <rect x="624" y="236" width="244" height="55" rx="6" fill="#DCEDC8" stroke="#2E7D32"/>
  <text x="746" y="254" text-anchor="middle" font-size="10" fill="#333">Variable composition of amino acids</text>
  <text x="746" y="270" text-anchor="middle" font-size="10" fill="#333">→ Variable CO₂:O₂ ratio</text>
  <text x="746" y="286" text-anchor="middle" font-size="14" font-weight="bold" fill="#1B5E20">RQ = 0.8–0.9</text>

  <!-- Significance -->
  <text x="746" y="312" text-anchor="middle" font-size="10" fill="#1B5E20" font-weight="bold">Interpretation:</text>
  <text x="746" y="326" text-anchor="middle" font-size="10" fill="#555">Last resort — prolonged starvation</text>
  <text x="746" y="340" text-anchor="middle" font-size="10" fill="#555">or severe wasting disease only.</text>

  <!-- SUMMARY BAR at bottom -->
  <rect x="20" y="360" width="860" height="70" rx="10" fill="#ECEFF1" stroke="#90A4AE"/>
  <text x="450" y="382" text-anchor="middle" font-size="12" font-weight="bold" fill="#1a1a2e">RQ Quick Reference Table</text>
  <text x="170" y="402" text-anchor="middle" font-size="11" font-weight="bold" fill="#E65100">Carbohydrates → RQ = 1.0</text>
  <text x="170" y="418" text-anchor="middle" font-size="10" fill="#555">Equal CO₂ and O₂ volumes</text>
  <text x="450" y="402" text-anchor="middle" font-size="11" font-weight="bold" fill="#4A148C">Lipids → RQ = 0.7</text>
  <text x="450" y="418" text-anchor="middle" font-size="10" fill="#555">More O₂ consumed than CO₂ released</text>
  <text x="730" y="402" text-anchor="middle" font-size="11" font-weight="bold" fill="#1B5E20">Proteins → RQ = 0.8–0.9</text>
  <text x="730" y="418" text-anchor="middle" font-size="10" fill="#555">Intermediate value; variable amino acids</text>
</svg>"""

SVG_L5_RESPIROMETER = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" font-family="Arial, sans-serif">
  <rect width="900" height="460" fill="#fafffe" rx="12"/>
  <text x="450" y="28" text-anchor="middle" font-size="16" font-weight="bold" fill="#1a1a2e">Respirometer Design and Mechanism — Measuring Oxygen Consumption Rate</text>

  <!-- ── LEFT PANEL: Respirometer apparatus ── -->
  <!-- Boiling tube -->
  <rect x="80" y="60" width="160" height="260" rx="12" fill="white" stroke="#90A4AE" stroke-width="2.5"/>
  <text x="160" y="55" text-anchor="middle" font-size="11" font-weight="bold" fill="#333">Sealed Boiling Tube</text>

  <!-- Wire gauze platform (middle of tube) -->
  <line x1="85" y1="240" x2="235" y2="240" stroke="#9E9E9E" stroke-width="3" stroke-dasharray="6,4"/>
  <text x="250" y="244" font-size="9" fill="#555">Wire gauze</text>

  <!-- Germinating seeds above gauze -->
  <ellipse cx="130" cy="215" rx="20" ry="10" fill="#66BB6A" stroke="#2E7D32"/>
  <ellipse cx="165" cy="210" rx="18" ry="9" fill="#4CAF50" stroke="#2E7D32"/>
  <ellipse cx="145" cy="200" rx="15" ry="8" fill="#81C784" stroke="#2E7D32"/>
  <ellipse cx="182" cy="218" rx="17" ry="9" fill="#66BB6A" stroke="#2E7D32"/>
  <text x="160" y="230" text-anchor="middle" font-size="9" fill="#1B5E20" font-weight="bold">Germinating Seeds</text>
  <text x="160" y="242" text-anchor="middle" font-size="8" fill="#1B5E20">(actively respiring)</text>

  <!-- KOH pellets below gauze -->
  <ellipse cx="115" cy="270" rx="12" ry="8" fill="#BDBDBD" stroke="#757575"/>
  <ellipse cx="145" cy="278" rx="10" ry="7" fill="#9E9E9E" stroke="#757575"/>
  <ellipse cx="175" cy="270" rx="11" ry="7" fill="#BDBDBD" stroke="#757575"/>
  <ellipse cx="195" cy="280" rx="10" ry="7" fill="#9E9E9E" stroke="#757575"/>
  <text x="160" y="300" text-anchor="middle" font-size="9" fill="#555" font-weight="bold">KOH Pellets</text>
  <text x="160" y="312" text-anchor="middle" font-size="8" fill="#555">Absorb CO₂ released</text>
  <!-- Arrow showing CO2 absorption -->
  <text x="160" y="328" text-anchor="middle" font-size="8" fill="#7B1FA2">CO₂ → absorbed here</text>

  <!-- Rubber stopper at top -->
  <rect x="85" y="55" width="150" height="18" rx="4" fill="#8D6E63"/>
  <text x="160" y="68" text-anchor="middle" font-size="8" fill="white">Rubber Stopper</text>

  <!-- Capillary tube (horizontal, from stopper) -->
  <rect x="240" y="60" width="360" height="12" rx="3" fill="white" stroke="#90A4AE" stroke-width="1.5"/>
  <text x="420" y="58" text-anchor="middle" font-size="10" fill="#333" font-weight="bold">Capillary Tube (narrow)</text>

  <!-- Colored manometer droplet -->
  <ellipse cx="490" cy="66" rx="16" ry="5" fill="#F44336"/>
  <text x="490" y="84" text-anchor="middle" font-size="10" fill="#B71C1C" font-weight="bold">Manometer Fluid</text>
  <text x="490" y="96" text-anchor="middle" font-size="9" fill="#B71C1C">Colored liquid droplet</text>

  <!-- Ruler beneath capillary tube -->
  <rect x="240" y="76" width="360" height="12" rx="2" fill="#FFF9C4" stroke="#F57F17"/>
  <!-- Ruler markings -->
  <line x1="280" y1="76" x2="280" y2="88" stroke="#E65100" stroke-width="1.5"/>
  <line x1="320" y1="76" x2="320" y2="88" stroke="#E65100" stroke-width="1.5"/>
  <line x1="360" y1="76" x2="360" y2="88" stroke="#E65100" stroke-width="1.5"/>
  <line x1="400" y1="76" x2="400" y2="88" stroke="#E65100" stroke-width="1.5"/>
  <line x1="440" y1="76" x2="440" y2="88" stroke="#E65100" stroke-width="1.5"/>
  <line x1="480" y1="76" x2="480" y2="88" stroke="#E65100" stroke-width="1.5"/>
  <line x1="520" y1="76" x2="520" y2="88" stroke="#E65100" stroke-width="1.5"/>
  <line x1="560" y1="76" x2="560" y2="88" stroke="#E65100" stroke-width="1.5"/>
  <line x1="600" y1="76" x2="600" y2="88" stroke="#E65100" stroke-width="1.5"/>
  <text x="280" y="100" text-anchor="middle" font-size="8" fill="#E65100">0</text>
  <text x="360" y="100" text-anchor="middle" font-size="8" fill="#E65100">2</text>
  <text x="440" y="100" text-anchor="middle" font-size="8" fill="#E65100">4</text>
  <text x="520" y="100" text-anchor="middle" font-size="8" fill="#E65100">6</text>
  <text x="600" y="100" text-anchor="middle" font-size="8" fill="#E65100">8 mm</text>
  <text x="420" y="112" text-anchor="middle" font-size="9" fill="#E65100" font-weight="bold">← Direction of droplet movement (toward tube)</text>

  <!-- Movement arrow -->
  <polygon points="320,66 340,60 340,72" fill="#B71C1C"/>
  <text x="295" y="62" font-size="9" fill="#B71C1C" font-weight="bold">←</text>
  <text x="350" y="56" font-size="10" fill="#B71C1C" font-weight="bold">Droplet moves THIS direction as O₂ consumed</text>

  <!-- ── RIGHT PANEL: Step-by-step mechanism ── -->
  <rect x="650" y="50" width="230" height="340" rx="10" fill="#E8F5E9" stroke="#388E3C" stroke-width="1.5"/>
  <text x="765" y="72" text-anchor="middle" font-size="12" font-weight="bold" fill="#1B5E20">How It Works</text>

  <rect x="665" y="82" width="200" height="42" rx="6" fill="#C8E6C9"/>
  <text x="765" y="98" text-anchor="middle" font-size="10" font-weight="bold" fill="#1a1a2e">Step 1</text>
  <text x="765" y="113" text-anchor="middle" font-size="10" fill="#333">Seeds consume O₂</text>
  <text x="765" y="125" text-anchor="middle" font-size="10" fill="#333">from sealed tube</text>

  <text x="765" y="142" text-anchor="middle" font-size="14" fill="#2E7D32">↓</text>

  <rect x="665" y="150" width="200" height="42" rx="6" fill="#A5D6A7"/>
  <text x="765" y="166" text-anchor="middle" font-size="10" font-weight="bold" fill="#1a1a2e">Step 2</text>
  <text x="765" y="181" text-anchor="middle" font-size="10" fill="#333">Seeds release CO₂</text>
  <text x="765" y="193" text-anchor="middle" font-size="10" fill="#333">→ KOH absorbs it all</text>

  <text x="765" y="210" text-anchor="middle" font-size="14" fill="#2E7D32">↓</text>

  <rect x="665" y="218" width="200" height="42" rx="6" fill="#81C784"/>
  <text x="765" y="234" text-anchor="middle" font-size="10" font-weight="bold" fill="#1a1a2e">Step 3</text>
  <text x="765" y="249" text-anchor="middle" font-size="10" fill="white">Net air volume in tube</text>
  <text x="765" y="261" text-anchor="middle" font-size="10" fill="white">DECREASES (pressure drop)</text>

  <text x="765" y="278" text-anchor="middle" font-size="14" fill="#2E7D32">↓</text>

  <rect x="665" y="286" width="200" height="42" rx="6" fill="#4CAF50"/>
  <text x="765" y="302" text-anchor="middle" font-size="10" font-weight="bold" fill="white">Step 4</text>
  <text x="765" y="317" text-anchor="middle" font-size="10" fill="white">Atmospheric pressure</text>
  <text x="765" y="329" text-anchor="middle" font-size="10" fill="white">pushes droplet inward</text>

  <text x="765" y="346" text-anchor="middle" font-size="14" fill="#2E7D32">↓</text>

  <rect x="665" y="354" width="200" height="30" rx="6" fill="#2E7D32"/>
  <text x="765" y="373" text-anchor="middle" font-size="10" font-weight="bold" fill="white">Distance ÷ Time = O₂ Rate</text>

  <!-- Bottom summary -->
  <rect x="20" y="402" width="860" height="50" rx="8" fill="#E8F5E9" stroke="#4CAF50"/>
  <text x="450" y="422" text-anchor="middle" font-size="11" font-weight="bold" fill="#1B5E20">KEY POINT: KOH pellets are ESSENTIAL. Without KOH → CO₂ replaces O₂ volume → Net change = 0 → Droplet does NOT move (if RQ = 1.0)</text>
  <text x="450" y="440" text-anchor="middle" font-size="10" fill="#333">A control tube with dead/boiled seeds and KOH corrects for temperature-induced volume changes in repeated experiments.</text>
</svg>"""

# ─────────────────────────────────────────────────────────────────────────────
# Enrichment data — Lesson ID, SVG, Wikimedia photo, YouTube video
# ─────────────────────────────────────────────────────────────────────────────

ENRICHMENT_DATA = [
    {
        "lesson_id": 1273,
        "unit_order": 1,
        "lesson_title": "Characteristics and Diversity of Respiratory Surfaces",
        "svg_title": "Counter-Current vs Parallel Flow — Fish Gill Oxygen Extraction Efficiency",
        "svg_content": SVG_L1_COUNTER_CURRENT,
        "svg_page": 5,
        "photo_title": "Scanning Electron Micrograph of Bony Fish Gill Filaments and Lamellae",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Gill_SEM.jpg/1024px-Gill_SEM.jpg",
        "photo_caption": "SEM of fish gill filaments showing the densely packed, plate-like secondary lamellae that maximize surface area for counter-current oxygen exchange with surrounding water. By Prof. Murray Thomson (NCI) — Public Domain.",
        "photo_author": "Public Domain (NCI)",
        "photo_licensing": "Public Domain",
        "photo_page": 7,
        "video_id": "x7_TsWx2B6M",
        "video_title": "Respiratory Surfaces Across Animal Kingdoms: Gills, Lungs, Trachea, Skin — GCSE Biology",
        "video_description": "Comprehensive GCSE Biology video comparing respiratory surfaces across amoeba, earthworms, insects (tracheal system), bony fish (counter-current gill flow), frogs (cutaneous + lung), birds (air sacs), and mammals (alveoli). Includes 3D animations of counter-current flow mechanism.",
        "video_page": 9,
    },
    {
        "lesson_id": 1274,
        "unit_order": 2,
        "lesson_title": "Human Gaseous Exchange and Ventilation Mechanics",
        "svg_title": "Human Respiratory System Anatomy and Alveolar Gas Exchange Mechanism",
        "svg_content": SVG_L2_HUMAN_LUNG,
        "svg_page": 3,
        "photo_title": "Coloured SEM of Human Lung Alveoli Surrounded by Pulmonary Capillaries",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Alveolus_diagram.svg/1024px-Alveolus_diagram.svg.png",
        "photo_caption": "Diagram of a cluster of alveoli showing the dense pulmonary capillary network surrounding the air sacs, illustrating the extremely short diffusion distance between alveolar air and blood. By Mariana Ruiz Villarreal — Public Domain.",
        "photo_author": "Mariana Ruiz Villarreal (LadyofHats)",
        "photo_licensing": "Public Domain",
        "photo_page": 8,
        "video_id": "0pMsxVzBXz0",
        "video_title": "Human Respiratory System: Anatomy, Alveolar Gas Exchange and Pressure-Volume Breathing Mechanics",
        "video_description": "GCSE Biology deep-dive into the human respiratory system anatomy from nasal cavity to alveoli, alveolar adaptations for gas exchange, and the physical pressure-volume mechanics of inhalation (active) and exhalation (passive) using the diaphragm and intercostal muscles.",
        "video_page": 10,
    },
    {
        "lesson_id": 1275,
        "unit_order": 3,
        "lesson_title": "Aerobic and Anaerobic Respiration, Exercise, and Oxygen Debt",
        "svg_title": "Oxygen Consumption Curve: Deficit, Debt, and Recovery After a 400m Sprint",
        "svg_content": SVG_L3_OXYGEN_DEBT,
        "svg_page": 4,
        "photo_title": "Electron Micrograph of Mitochondria in Highly Active Muscle Cells",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Mitochondria%2C_mammalian_lung_-_TEM.jpg/1024px-Mitochondria%2C_mammalian_lung_-_TEM.jpg",
        "photo_caption": "Transmission electron micrograph (TEM) of mitochondria in a mammalian cell, showing the characteristic folded inner membrane (cristae) that provides a large surface area for the electron transport chain — the ATP-producing final stage of aerobic respiration. By Louisa Howard — Public Domain.",
        "photo_author": "Louisa Howard",
        "photo_licensing": "Public Domain",
        "photo_page": 7,
        "video_id": "etraXJHSHkA",
        "video_title": "Aerobic and Anaerobic Respiration, Lactic Acid, and Oxygen Debt — GCSE Biology",
        "video_description": "Clear GCSE Biology explanation comparing aerobic (38 ATP, mitochondria) and anaerobic (2 ATP, cytoplasm) respiration in animals, the formation of lactic acid during vigorous exercise, the physiological basis of oxygen debt, and how the liver repays the debt during recovery.",
        "video_page": 9,
    },
    {
        "lesson_id": 1276,
        "unit_order": 4,
        "lesson_title": "Respiratory Substrates, Respiratory Quotient (RQ), and Energy Requirements",
        "svg_title": "Respiratory Substrates Comparison and RQ Calculation Guide (Carbs, Lipids, Proteins)",
        "svg_content": SVG_L4_RQ,
        "svg_page": 4,
        "photo_title": "Spirometer Tracing Showing Lung Volume Measurements (Tidal, Vital Capacity, Residual)",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Lungvolumes.svg/1024px-Lungvolumes.svg.png",
        "photo_caption": "Spirometer tracing chart showing lung volume terminology: tidal volume (TV), inspiratory reserve volume (IRV), expiratory reserve volume (ERV), vital capacity (VC), and residual volume (RV) that cannot be exhaled. By Vihsadas — CC BY-SA 3.0.",
        "photo_author": "Vihsadas",
        "photo_licensing": "CC BY-SA 3.0",
        "photo_page": 7,
        "video_id": "3BGbxDMrK2w",
        "video_title": "Respiratory Substrates, Respiratory Quotient Calculation, and Energy Requirements — GCSE Biology",
        "video_description": "GCSE Biology video explaining energy values of carbohydrates (17 kJ/g), lipids (38 kJ/g), and proteins (22 kJ/g) as respiratory substrates, the Respiratory Quotient (RQ) formula and step-by-step worked calculations for each substrate, and factors influencing daily human energy requirements.",
        "video_page": 9,
    },
    {
        "lesson_id": 1277,
        "unit_order": 5,
        "lesson_title": "Investigating Respiration and Designing Gaseous-Exchange Models",
        "svg_title": "Respirometer Apparatus Diagram and Step-by-Step Oxygen Consumption Mechanism",
        "svg_content": SVG_L5_RESPIROMETER,
        "svg_page": 4,
        "photo_title": "Germinating Seeds in Vacuum Flask Showing Heat Release Experiment Setup",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Germination_bean_edit.jpg/1024px-Germination_bean_edit.jpg",
        "photo_caption": "Germinating bean seeds showing visible growth and metabolic activity. In the vacuum flask experiment, active germination releases measurable heat energy as a byproduct of aerobic cellular respiration, while dead boiled seeds in the control flask remain at room temperature. By the United States Navy — Public Domain.",
        "photo_author": "United States Navy (Public Domain)",
        "photo_licensing": "Public Domain",
        "photo_page": 7,
        "video_id": "2sDZQlSfvhg",
        "video_title": "Respirometer Experiment, Limewater CO₂ Test, and Bell-Jar Breathing Model — GCSE Biology Practicals",
        "video_description": "GCSE Biology practical guide covering the germinating seeds heat release experiment, limewater and hydrogencarbonate indicator tests for CO₂, the mechanism of a respirometer (why KOH pellets are essential), and how to assemble and use a bell-jar model to demonstrate human inhalation and exhalation pressure-volume dynamics.",
        "video_page": 9,
    },
]


@transaction.atomic
def enrich_topic10(replace=False):
    """Attach SVG, photo, and YouTube video assets to each Topic 10 lesson."""
    print("=" * 70)
    print("VLearn Grade 10 Biology — Topic 10: Animal Gaseous Exchange and Respiration")
    print("Visual Enrichment Engine v1.0")
    print("=" * 70)

    svg_count = 0
    photo_count = 0
    video_count = 0

    for entry in ENRICHMENT_DATA:
        lesson_id = entry["lesson_id"]
        lesson = Lesson.objects.get(id=lesson_id)

        # Scope isolation guard
        assert lesson.topic.order == 10, f"SCOPE ERROR: Lesson {lesson_id} not Topic 10!"
        assert lesson.topic.subject.id == 35, f"SCOPE ERROR: Subject not Biology ID 35!"

        print(f"\n  Lesson {lesson_id}: {entry['lesson_title']}")

        if replace:
            existing = LessonAsset.objects.filter(lesson=lesson)
            print(f"    Removing {existing.count()} existing assets...")
            existing.delete()

        # ── 1. SVG Vector Diagram ──────────────────────────────────────────
        svg_block = LessonBlock.objects.filter(
            lesson=lesson, page_number=entry["svg_page"]
        ).first()

        if svg_block:
            content = svg_block.content or {}
            content["svg_markup"] = entry["svg_content"]
            svg_block.content = content
            svg_block.save()

        svg_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="diagram",
            source_type="ai_generated",
            storage_type="embed",
            status="attached",
            title=entry["svg_title"],
            description=f"High-quality biological vector diagram: {entry['svg_title']}",
            metadata={"svg_content": entry["svg_content"]}
        )
        if svg_block:
            svg_block.assets.add(svg_asset)
        svg_count += 1
        print(f"    ✓ SVG attached: {entry['svg_title'][:62]}...")

        # ── 2. Wikimedia Photo ─────────────────────────────────────────────
        photo_block = LessonBlock.objects.filter(
            lesson=lesson, page_number=entry["photo_page"]
        ).first()

        if photo_block:
            content = photo_block.content or {}
            content["resolved_image_url"] = entry["photo_url"]
            content["url"] = entry["photo_url"]
            content["author"] = entry["photo_author"]
            content["licensing"] = entry["photo_licensing"]
            content["caption"] = entry["photo_caption"]
            photo_block.content = content
            photo_block.title = entry["photo_title"]
            photo_block.save()

        photo_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="image",
            source_type="external",
            storage_type="url",
            status="attached",
            title=entry["photo_title"],
            description=entry["photo_caption"],
            url=entry["photo_url"],
            metadata={
                "author": entry["photo_author"],
                "licensing": entry["photo_licensing"],
                "caption": entry["photo_caption"],
            }
        )
        if photo_block:
            photo_block.assets.add(photo_asset)
        photo_count += 1
        print(f"    ✓ Photo attached: {entry['photo_title'][:62]}...")

        # ── 3. YouTube Video ───────────────────────────────────────────────
        target_page = entry["video_page"]
        v_block = LessonBlock.objects.filter(
            lesson=lesson, page_number=target_page, block_type="suggested_video"
        ).first()

        if not v_block:
            last_block = LessonBlock.objects.filter(
                lesson=lesson, page_number=target_page
            ).order_by("-order").first()
            new_order = (last_block.order + 5) if last_block else 50

            v_block = LessonBlock.objects.create(
                lesson=lesson,
                page_number=target_page,
                page_title=entry["video_title"],
                title=entry["video_title"],
                block_type="suggested_video",
                component_type="suggested_video",
                component_order=new_order,
                order=new_order,
                content={
                    "resolved_video_id": entry["video_id"],
                    "url": f"https://www.youtube.com/watch?v={entry['video_id']}",
                    "description": entry["video_description"],
                },
                metadata={}
            )
        else:
            v_block.title = entry["video_title"]
            v_block.content = {
                "resolved_video_id": entry["video_id"],
                "url": f"https://www.youtube.com/watch?v={entry['video_id']}",
                "description": entry["video_description"],
            }
            v_block.save()

        video_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="youtube",
            source_type="external",
            storage_type="url",
            status="attached",
            title=entry["video_title"],
            description=entry["video_description"],
            url=f"https://www.youtube.com/watch?v={entry['video_id']}",
            metadata={"youtube_id": entry["video_id"]}
        )
        v_block.assets.add(video_asset)
        video_count += 1
        print(f"    ✓ Video attached: {entry['video_title'][:62]}...")

    total_assets = svg_count + photo_count + video_count
    print("\n" + "=" * 70)
    print("ENRICHMENT COMPLETE — Grade 10 Biology Topic 10: Animal Gaseous Exchange")
    print(f"  Vector SVG Diagrams: {svg_count}")
    print(f"  Wikimedia Photos:    {photo_count}")
    print(f"  YouTube Videos:      {video_count}")
    print(f"  Total LessonAssets:  {total_assets}")
    print("=" * 70)


if __name__ == "__main__":
    import sys
    replace = "--replace" in sys.argv
    enrich_topic10(replace=replace)
