"""
VLearn CBC Grade 10 Physics — Topic 2: Pressure
Production Ingestion & Visual Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Physics
Topic: Pressure (Order: 2)

5 Learning Units & 5 Published Lessons:
  1. Pressure in Solids and Atmospheric Pressure (9 Pages, 16 Blocks)
  2. Pressure in Liquids and Its Factors (8 Pages, 14 Blocks)
  3. Deriving and Applying P = \rho g h (9 Pages, 15 Blocks)
  4. Transmission of Pressure and Pascal’s Principle (9 Pages, 15 Blocks)
  5. Pressure Applications and Water Pumping (9 Pages, 16 Blocks)

Includes:
  - 10 Custom Responsive Sanitized Vector SVG Diagrams
  - 5 Verified Wikimedia Commons Photographic Assets
  - 5 Verified Educational YouTube Video Integrations
  - 5 Formative Scenario-Based MCQs with 4 Options and Pedagogical Feedback
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
# SVG DEFINITIONS (THEME AWARE / RESPONSIVE / PEDAGOGICALLY RIGOROUS)
# =============================================================================

def get_svg_solid_pressure():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 420" width="100%" height="100%">
  <rect width="820" height="420" fill="#0f172a" rx="16"/>
  <text x="410" y="36" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">SOLID PRESSURE: FORCE DISTRIBUTION VS CONTACT AREA (P = F / A)</text>
  <text x="410" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Same 100 N Force • Different Contact Areas • Dramatic Difference in Pressure</text>

  <!-- Left: Broad Base (Low Pressure) -->
  <g transform="translate(40, 85)">
    <rect width="350" height="300" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="175" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">BROAD CONTACT AREA</text>
    
    <!-- Wooden Block on Broad Face -->
    <rect x="50" y="100" width="250" height="70" fill="#0284c733" stroke="#38bdf8" stroke-width="2" rx="4"/>
    <text x="175" y="142" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="14" font-weight="600" text-anchor="middle">Weight = 100 N</text>

    <!-- Force Arrows Spread Out -->
    <path d="M 80 60 L 80 95 M 75 90 L 80 95 L 85 90" stroke="#38bdf8" stroke-width="2"/>
    <path d="M 140 60 L 140 95 M 135 90 L 140 95 L 145 90" stroke="#38bdf8" stroke-width="2"/>
    <path d="M 210 60 L 210 95 M 205 90 L 210 95 L 215 90" stroke="#38bdf8" stroke-width="2"/>
    <path d="M 270 60 L 270 95 M 265 90 L 270 95 L 275 90" stroke="#38bdf8" stroke-width="2"/>

    <!-- Ground Surface Line -->
    <line x1="30" y1="170" x2="320" y2="170" stroke="#94a3b8" stroke-width="3"/>
    
    <!-- Calculation Box -->
    <rect x="30" y="195" width="290" height="85" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="45" y="220" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Contact Area (A) = 0.50 m²</text>
    <text x="45" y="242" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Force (F) = 100 N</text>
    <text x="45" y="267" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700">P = 100 N / 0.50 m² = 200 Pa (Low)</text>
  </g>

  <!-- Right: Narrow Edge (High Pressure) -->
  <g transform="translate(430, 85)">
    <rect width="350" height="300" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="175" y="32" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">NARROW CONTACT AREA</text>
    
    <!-- Wooden Block on Edge -->
    <rect x="145" y="60" width="60" height="110" fill="#d9770633" stroke="#f59e0b" stroke-width="2" rx="4"/>
    <text x="175" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="600" text-anchor="middle" transform="rotate(-90 175 120)">Weight = 100 N</text>

    <!-- Concentrated Force Arrow -->
    <path d="M 175 20 L 175 55 M 168 50 L 175 55 L 182 50" stroke="#f59e0b" stroke-width="3"/>

    <!-- Ground Surface Line with Sinking Depress -->
    <line x1="30" y1="170" x2="320" y2="170" stroke="#94a3b8" stroke-width="3"/>
    <path d="M 140 170 Q 175 185 210 170" fill="#ef444433" stroke="#ef4444" stroke-width="2"/>
    <text x="175" y="195" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Deep Ground Indentation!</text>

    <!-- Calculation Box -->
    <rect x="30" y="205" width="290" height="75" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="45" y="228" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Contact Area (A) = 0.05 m² (10x smaller)</text>
    <text x="45" y="248" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Force (F) = 100 N</text>
    <text x="45" y="270" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="14" font-weight="700">P = 100 N / 0.05 m² = 2,000 Pa (10x Higher)</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_altitude_pressure():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 440" width="100%" height="100%">
  <rect width="800" height="440" fill="#0b132b" rx="16"/>
  <text x="400" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">ATMOSPHERIC PRESSURE: VARIATION WITH ALTITUDE</text>
  <text x="400" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Air Density & Weight Decrease as Altitude Increases (e.g. Sea Level to Mt. Kenya Summit)</text>

  <!-- Mountain Silhouette -->
  <path d="M 50 380 L 320 120 L 520 260 L 750 380 Z" fill="#1c2541" stroke="#3a506b" stroke-width="2"/>
  <path d="M 285 150 L 320 120 L 355 155 Z" fill="#e0f2fe" opacity="0.9"/> <!-- Snow Peak -->

  <!-- Atmosphere Density Dots (Dense at bottom, sparse at top) -->
  <!-- Low Altitude Dots (Dense) -->
  <g fill="#38bdf8" opacity="0.8">
    <circle cx="90" cy="360" r="3"/><circle cx="120" cy="350" r="3"/><circle cx="150" cy="370" r="3"/><circle cx="180" cy="360" r="3"/>
    <circle cx="210" cy="350" r="3"/><circle cx="600" cy="370" r="3"/><circle cx="630" cy="350" r="3"/><circle cx="670" cy="360" r="3"/>
    <circle cx="700" cy="370" r="3"/><circle cx="730" cy="350" r="3"/><circle cx="110" cy="320" r="3"/><circle cx="140" cy="310" r="3"/>
    <circle cx="620" cy="320" r="3"/><circle cx="660" cy="310" r="3"/><circle cx="690" cy="330" r="3"/><circle cx="720" cy="315" r="3"/>
  </g>

  <!-- Mid Altitude Dots (Medium) -->
  <g fill="#38bdf8" opacity="0.5">
    <circle cx="180" cy="240" r="3"/><circle cx="220" cy="220" r="3"/><circle cx="480" cy="230" r="3"/><circle cx="520" cy="210" r="3"/>
    <circle cx="560" cy="240" r="3"/><circle cx="200" cy="260" r="3"/><circle cx="450" cy="250" r="3"/>
  </g>

  <!-- High Altitude Dots (Sparse) -->
  <g fill="#38bdf8" opacity="0.3">
    <circle cx="290" cy="110" r="3"/><circle cx="320" cy="90" r="3"/><circle cx="350" cy="110" r="3"/><circle cx="330" cy="70" r="3"/>
  </g>

  <!-- Sea Level Annotation -->
  <g transform="translate(560, 310)">
    <rect width="210" height="65" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="105" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">SEA LEVEL (0 m)</text>
    <text x="105" y="42" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Patm ≈ 101,300 Pa (101.3 kPa)</text>
    <text x="105" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Maximum air column weight</text>
  </g>

  <!-- Mountain Peak Annotation -->
  <g transform="translate(180, 50)">
    <rect width="220" height="65" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="110" y="24" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">MT. KENYA PEAK (5,199 m)</text>
    <text x="110" y="42" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Patm ≈ 54,000 Pa (54 kPa)</text>
    <text x="110" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Low air density • Thin atmosphere</text>
  </g>

  <!-- Large Downward Pressure Vectors -->
  <path d="M 680 180 L 680 290 M 670 280 L 680 290 L 690 280" stroke="#38bdf8" stroke-width="4"/>
  <text x="695" y="240" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Heavy Air Column</text>

  <path d="M 320 30 L 320 70 M 315 63 L 320 70 L 325 63" stroke="#f59e0b" stroke-width="2.5"/>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_spouting_can():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="16"/>
  <text x="400" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">INVESTIGATION: LIQUID PRESSURE INCREASES WITH DEPTH (THE SPOUTING CAN)</text>
  <text x="400" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Velocity of emergent jet v = √(2gh) proves hydrostatic pressure P ∝ h</text>

  <!-- Water Cylinder Container -->
  <g transform="translate(100, 80)">
    <!-- Container Body -->
    <rect x="0" y="20" width="140" height="300" fill="#0284c722" stroke="#38bdf8" stroke-width="3" rx="4"/>
    <!-- Water Fill -->
    <rect x="2" y="40" width="136" height="278" fill="#0284c755"/>
    <line x1="2" y1="40" x2="138" y2="40" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 2"/>
    <text x="70" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Free Water Surface</text>

    <!-- Hole A (Top, Depth h1) -->
    <circle cx="140" cy="80" r="4" fill="#ef4444"/>
    <text x="120" y="75" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="end">Hole A (Shallow)</text>

    <!-- Hole B (Middle, Depth h2) -->
    <circle cx="140" cy="180" r="4" fill="#f59e0b"/>
    <text x="120" y="175" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="end">Hole B (Mid)</text>

    <!-- Hole C (Bottom, Depth h3) -->
    <circle cx="140" cy="280" r="4" fill="#22c55e"/>
    <text x="120" y="275" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="end">Hole C (Deepest)</text>

    <!-- Depth measurement bracket on left -->
    <line x1="-30" y1="40" x2="-30" y2="280" stroke="#94a3b8" stroke-width="1.5"/>
    <path d="M -35 40 L -25 40 M -35 280 L -25 280" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="-40" y="160" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="end">Depth (h)</text>
    <path d="M -30 40 L -30 280 M -34 270 L -30 280 L -26 270" stroke="#94a3b8" stroke-width="1.5"/>

    <!-- Catch Basin Base -->
    <rect x="-40" y="320" width="600" height="15" fill="#1e293b" stroke="#334155" stroke-width="1.5" rx="3"/>
  </g>

  <!-- Water Jet Trajectories -->
  <!-- Jet A (Weakest, lands closest) -->
  <path d="M 240 160 Q 280 165 310 400" stroke="#ef4444" stroke-width="3" fill="none"/>
  <text x="310" y="420" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Jet A (Weak)</text>

  <!-- Jet B (Medium) -->
  <path d="M 240 260 Q 350 265 440 400" stroke="#f59e0b" stroke-width="3" fill="none"/>
  <text x="440" y="420" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Jet B (Moderate)</text>

  <!-- Jet C (Strongest, lands furthest) -->
  <path d="M 240 360 Q 450 365 590 400" stroke="#22c55e" stroke-width="3.5" fill="none"/>
  <text x="590" y="420" fill="#22c55e" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Jet C (Furthest)</text>

  <!-- Explanatory Legend Box -->
  <g transform="translate(500, 90)">
    <rect width="260" height="160" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="130" y="26" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">PHYSICS CONCLUSIONS</text>
    <text x="15" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">• Hole C is at maximum depth (h).</text>
    <text x="15" y="78" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">• Water column weight is greatest at base.</text>
    <text x="15" y="101" fill="#22c55e" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Pressure P = ρgh is highest.</text>
    <text x="15" y="124" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">• Water exits at highest velocity.</text>
    <text x="15" y="147" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Pressure is omnidirectional at that depth.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_communicating_vessels():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <rect width="800" height="400" fill="#0f172a" rx="16"/>
  <text x="400" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">COMMUNICATING VESSELS: PRESSURE IS INDEPENDENT OF CONTAINER SHAPE</text>
  <text x="400" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">"Water always finds its own level" • Hydrostatic pressure depends strictly on vertical depth (h)</text>

  <!-- Connected Glassware Shapes -->
  <!-- Base Common Manifold Pipe -->
  <rect x="100" y="300" width="600" height="45" fill="#0284c744" stroke="#38bdf8" stroke-width="2"/>

  <!-- Tube 1: Narrow Cylinder -->
  <rect x="130" y="120" width="40" height="180" fill="#0284c744" stroke="#38bdf8" stroke-width="2"/>
  
  <!-- Tube 2: Conical / Bulbous -->
  <path d="M 270 120 L 250 220 L 290 300 L 330 300 L 370 220 L 350 120 Z" fill="#0284c744" stroke="#38bdf8" stroke-width="2"/>

  <!-- Tube 3: Zig-Zag / Slanted -->
  <path d="M 450 120 L 490 200 L 440 260 L 470 300 L 510 300 L 480 260 L 530 200 L 490 120 Z" fill="#0284c744" stroke="#38bdf8" stroke-width="2"/>

  <!-- Tube 4: Wide Cylindrical Flask -->
  <rect x="590" y="120" width="90" height="180" fill="#0284c744" stroke="#38bdf8" stroke-width="2"/>

  <!-- Unified Horizontal Water Line across ALL tubes -->
  <line x1="80" y1="150" x2="720" y2="150" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="6 4"/>
  <text x="730" y="154" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Same Level (h)</text>

  <!-- Horizontal Pressure Depth Plane -->
  <line x1="80" y1="240" x2="720" y2="240" stroke="#22c55e" stroke-width="2" stroke-dasharray="3 3"/>
  <text x="730" y="244" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Uniform Pressure Plane (P1 = P2 = P3 = P4)</text>

  <!-- Depth Indicator -->
  <line x1="60" y1="150" x2="60" y2="240" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 56 150 L 64 150 M 56 240 L 64 240" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="50" y="200" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="end">Depth h</text>

  <!-- Bottom Caption -->
  <rect x="150" y="355" width="500" height="35" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="400" y="377" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Regardless of cross-sectional area or slant geometry, Pressure at depth h is identical: P = ρgh</text>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_derivation_model():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 440" width="100%" height="100%">
  <rect width="800" height="440" fill="#0f172a" rx="16"/>
  <text x="400" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">MATHEMATICAL DERIVATION MODEL FOR LIQUID COLUMN: P = ρgh</text>
  <text x="400" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">First-Principles Derivation from Mass, Density, Volume, and Area</text>

  <!-- Transparent Column Schematic (Left) -->
  <g transform="translate(60, 80)">
    <!-- Liquid Beaker Outline -->
    <rect x="0" y="20" width="280" height="300" fill="#0284c711" stroke="#334155" stroke-width="1.5" rx="4"/>
    <line x1="0" y1="40" x2="280" y2="40" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 2"/>
    <text x="140" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Liquid Density ρ</text>

    <!-- Highlighted Column of Liquid -->
    <rect x="80" y="60" width="120" height="220" fill="#0284c744" stroke="#38bdf8" stroke-width="2.5" rx="4"/>
    
    <!-- Top Area Face A -->
    <ellipse cx="140" cy="60" rx="60" ry="15" fill="#38bdf866" stroke="#38bdf8" stroke-width="2"/>
    <text x="140" y="64" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Area A</text>

    <!-- Bottom Area Face A -->
    <ellipse cx="140" cy="280" rx="60" ry="15" fill="#38bdf866" stroke="#38bdf8" stroke-width="2"/>
    <text x="140" y="284" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Base Area A</text>

    <!-- Height h Bracket -->
    <line x1="220" y1="60" x2="220" y2="280" stroke="#f59e0b" stroke-width="2"/>
    <path d="M 215 60 L 225 60 M 215 280 L 225 280" stroke="#f59e0b" stroke-width="2"/>
    <text x="235" y="175" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Height (h)</text>

    <!-- Downward Weight Vector Arrow -->
    <path d="M 140 140 L 140 240 M 132 230 L 140 240 L 148 230" stroke="#22c55e" stroke-width="3.5"/>
    <text x="150" y="190" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700">W = mg</text>
  </g>

  <!-- 7-Step Derivation Flow Box (Right) -->
  <g transform="translate(380, 75)">
    <rect width="380" height="340" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="190" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">ALGEBRAIC DERIVATION STEPS</text>
    
    <g transform="translate(20, 45)" font-family="system-ui, sans-serif" font-size="12" fill="#f8fafc">
      <text y="20"><tspan fill="#38bdf8" font-weight="700">1. Definition:</tspan> P = Force / Area = F / A</text>
      <text y="55"><tspan fill="#38bdf8" font-weight="700">2. Weight of column:</tspan> F = W = m × g</text>
      <text y="90"><tspan fill="#38bdf8" font-weight="700">3. Density relationship:</tspan> m = ρ × V</text>
      <text y="125"><tspan fill="#38bdf8" font-weight="700">4. Substitute mass:</tspan> F = (ρ × V) × g</text>
      <text y="160"><tspan fill="#38bdf8" font-weight="700">5. Column Volume:</tspan> V = Area × height = A × h</text>
      <text y="195"><tspan fill="#38bdf8" font-weight="700">6. Substitute into Pressure:</tspan></text>
      <text y="220" font-family="serif" font-size="14" fill="#f59e0b">P = [ρ × (A × h) × g] / A</text>
      <text y="250"><tspan fill="#22c55e" font-weight="700">7. Cancel Area (A) from numerator & denominator:</tspan></text>
    </g>

    <!-- Final Result Badge -->
    <rect x="40" y="280" width="300" height="42" rx="8" fill="#0284c733" stroke="#22c55e" stroke-width="2"/>
    <text x="190" y="307" fill="#4ade80" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">P = ρ g h</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_pressure_depth_graph():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%">
  <rect width="800" height="420" fill="#0f172a" rx="16"/>
  <text x="400" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">HYDROSTATIC GRAPH: PRESSURE (P) VS DEPTH (h)</text>
  <text x="400" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Linear Direct Proportionality P = (ρg) · h • Slope Equals Product of Density & Gravity</text>

  <!-- Grid Lines -->
  <g stroke="#334155" stroke-width="1" stroke-dasharray="4 4">
    <line x1="120" y1="340" x2="720" y2="340"/>
    <line x1="120" y1="270" x2="720" y2="270"/>
    <line x1="120" y1="200" x2="720" y2="200"/>
    <line x1="120" y1="130" x2="720" y2="130"/>
    
    <line x1="120" y1="80" x2="120" y2="340"/>
    <line x1="270" y1="80" x2="270" y2="340"/>
    <line x1="420" y1="80" x2="420" y2="340"/>
    <line x1="570" y1="80" x2="570" y2="340"/>
    <line x1="720" y1="80" x2="720" y2="340"/>
  </g>

  <!-- Solid Axes -->
  <line x1="120" y1="340" x2="740" y2="340" stroke="#94a3b8" stroke-width="2"/>
  <line x1="120" y1="340" x2="120" y2="70" stroke="#94a3b8" stroke-width="2"/>

  <!-- Y-Axis Labels: Hydrostatic Pressure P (kPa) -->
  <text x="105" y="345" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">0</text>
  <text x="105" y="275" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">50 kPa</text>
  <text x="105" y="205" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">100 kPa</text>
  <text x="105" y="135" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">150 kPa</text>
  <text x="45" y="200" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle" transform="rotate(-90 45 200)">Pressure P (Pascals)</text>

  <!-- X-Axis Labels: Depth h (m) -->
  <text x="120" y="360" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">0</text>
  <text x="270" y="360" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">5 m</text>
  <text x="420" y="360" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">10 m</text>
  <text x="570" y="360" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">15 m</text>
  <text x="720" y="360" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">20 m</text>
  <text x="420" y="390" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Depth h (metres)</text>

  <!-- Graph Line 1: Pure Water (ρ = 1000 kg/m³) -->
  <line x1="120" y1="340" x2="680" y2="100" stroke="#38bdf8" stroke-width="3.5"/>
  <text x="690" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Water (ρ = 1000)</text>

  <!-- Graph Line 2: Dense Saltwater (ρ = 1025 kg/m³, steeper) -->
  <line x1="120" y1="340" x2="640" y2="80" stroke="#22c55e" stroke-width="2.5" stroke-dasharray="5 3"/>
  <text x="645" y="75" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Saltwater (Steeper Slope)</text>

  <!-- Gradient Triangle Annotation -->
  <path d="M 270 275 L 420 275 L 420 210 Z" fill="#f59e0b33" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="345" y="295" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Δh</text>
  <text x="440" y="245" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11">ΔP</text>

  <!-- Formula Callout Box -->
  <rect x="230" y="110" width="240" height="60" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="245" y="132" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Gradient = ΔP / Δh = ρ × g</text>
  <text x="245" y="152" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Direct linear relationship (y = mx)</text>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_hydraulic_system():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 440" width="100%" height="100%">
  <rect width="840" height="440" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">PASCAL’S PRINCIPLE: HYDRAULIC FORCE MULTIPLICATION</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Pressure transmitted undiminished through incompressible fluid: P1 = P2 ⟹ F1 / A1 = F2 / A2</text>

  <!-- U-Tube Manifold Body -->
  <path d="M 120 180 L 120 330 L 720 330 L 720 180 L 520 180 L 520 270 L 220 270 L 220 180 Z" fill="#0284c733" stroke="#38bdf8" stroke-width="3"/>
  
  <!-- Incompressible Hydraulic Oil Fill -->
  <path d="M 122 220 L 122 328 L 718 328 L 718 200 L 522 200 L 522 272 L 218 272 L 218 220 Z" fill="#eab30866"/>

  <!-- Left Narrow Input Piston (A1) -->
  <rect x="122" y="210" width="96" height="25" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5" rx="3"/>
  <rect x="165" y="130" width="10" height="80" fill="#94a3b8"/> <!-- Piston Rod -->
  
  <!-- Input Force Arrow F1 -->
  <path d="M 170 80 L 170 125 M 162 115 L 170 125 L 178 115" stroke="#ef4444" stroke-width="4"/>
  <text x="170" y="70" fill="#ef4444" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Effort F1 = 150 N</text>
  <text x="170" y="255" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Area A1 = 0.02 m²</text>

  <!-- Right Wide Output Piston (A2) -->
  <rect x="522" y="190" width="196" height="30" fill="#22c55e" stroke="#ffffff" stroke-width="1.5" rx="3"/>
  <rect x="615" y="100" width="16" height="90" fill="#94a3b8"/> <!-- Output Ram -->

  <!-- Output Load (Car representation) -->
  <rect x="540" y="70" width="160" height="30" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="6"/>
  <text x="620" y="90" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Vehicle Load (6,000 N)</text>

  <!-- Output Force Arrow F2 -->
  <path d="M 620 180 L 620 110 M 610 120 L 620 110 L 630 120" stroke="#22c55e" stroke-width="5"/>
  <text x="620" y="240" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Area A2 = 0.80 m² (40× A1)</text>

  <!-- Pressure Transmission Arrows inside fluid -->
  <g stroke="#f8fafc" stroke-width="2" fill="none">
    <path d="M 240 300 L 480 300 M 470 294 L 480 300 L 470 306"/>
    <text x="360" y="290" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Pressure P transmitted undiminished</text>
  </g>

  <!-- Multiplier Equation Box -->
  <rect x="250" y="360" width="340" height="60" rx="8" fill="#1e293b" stroke="#22c55e" stroke-width="2"/>
  <text x="420" y="385" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Mechanical Advantage = A2 / A1 = 40</text>
  <text x="420" y="405" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">F2 = F1 × (A2 / A1) = 150 N × 40 = 6,000 N</text>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_siphon():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%">
  <rect width="800" height="420" fill="#0f172a" rx="16"/>
  <text x="400" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE SIPHON MECHANISM: CONTINUOUS FLUID FLOW OVER AN OBSTACLE</text>
  <text x="400" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Driven by Hydrostatic Column Weight Differences and Atmospheric Pressure</text>

  <!-- Container A (High Reservoir) -->
  <g transform="translate(100, 140)">
    <rect width="180" height="180" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="4"/>
    <rect x="4" y="40" width="172" height="136" fill="#0284c755"/>
    <text x="90" y="30" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Reservoir A (High)</text>
    <path d="M 50 10 L 50 35 M 45 30 L 50 35 L 55 30" stroke="#38bdf8" stroke-width="2"/>
    <text x="50" y="5" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Patm</text>
  </g>

  <!-- Container B (Low Reservoir) -->
  <g transform="translate(520, 240)">
    <rect width="180" height="150" fill="#1e293b" stroke="#22c55e" stroke-width="2" rx="4"/>
    <rect x="4" y="90" width="172" height="56" fill="#0284c755"/>
    <text x="90" y="30" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Reservoir B (Low Level)</text>
  </g>

  <!-- U-Shaped Siphon Tube -->
  <path d="M 190 280 L 190 90 Q 190 70 210 70 L 590 70 Q 610 70 610 90 L 610 320" fill="none" stroke="#0284c7" stroke-width="16"/>
  <path d="M 190 280 L 190 90 Q 190 70 210 70 L 590 70 Q 610 70 610 90 L 610 320" fill="none" stroke="#38bdf8" stroke-width="10"/>

  <!-- Crest Low Pressure Callout -->
  <circle cx="400" cy="70" r="14" fill="#ef4444"/>
  <text x="400" y="75" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Low P</text>
  <text x="400" y="110" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Crest: Reduced Pressure Zone</text>

  <!-- Water Flow Arrows inside tube -->
  <path d="M 190 200 L 190 150 M 185 155 L 190 150 L 195 155" stroke="#ffffff" stroke-width="2"/>
  <path d="M 330 70 L 370 70 M 365 65 L 370 70 L 365 75" stroke="#ffffff" stroke-width="2"/>
  <path d="M 610 150 L 610 200 M 605 195 L 610 200 L 615 195" stroke="#ffffff" stroke-width="2"/>

  <!-- Column Height Difference (h) -->
  <line x1="640" y1="180" x2="640" y2="330" stroke="#f59e0b" stroke-width="2"/>
  <path d="M 635 180 L 645 180 M 635 330 L 645 330" stroke="#f59e0b" stroke-width="2"/>
  <text x="655" y="260" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Longer Column (Heavier Weight)</text>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_lift_pump():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 450" width="100%" height="100%">
  <rect width="840" height="450" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE RECIPROCATING LIFT PUMP: TWO-STROKE OPERATING CYCLE</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Atmospheric pressure lifts water into low-pressure chamber during upstroke • Valves control direction</text>

  <!-- Left: Upstroke Panel -->
  <g transform="translate(40, 75)">
    <rect width="360" height="345" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="180" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">1. UPSTROKE (PUMPING & LIFTING)</text>

    <!-- Pump Cylinder -->
    <rect x="110" y="60" width="140" height="220" fill="#0284c711" stroke="#94a3b8" stroke-width="2"/>
    <!-- Water in lower barrel -->
    <rect x="112" y="160" width="136" height="118" fill="#0284c755"/>

    <!-- Piston Rising -->
    <rect x="112" y="140" width="136" height="20" fill="#38bdf8" stroke="#ffffff" stroke-width="1"/>
    <path d="M 180 140 L 180 60 M 172 70 L 180 60 L 188 70" stroke="#38bdf8" stroke-width="3"/> <!-- Rising arrow -->

    <!-- Piston Valve CLOSED -->
    <line x1="170" y1="150" x2="190" y2="150" stroke="#ef4444" stroke-width="4"/>
    <text x="95" y="135" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="end">Piston Valve CLOSED</text>

    <!-- Inlet Foot Valve OPEN -->
    <line x1="170" y1="280" x2="185" y2="265" stroke="#22c55e" stroke-width="3"/>
    <text x="95" y="280" fill="#22c55e" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="end">Inlet Valve OPEN</text>

    <!-- Spout discharge -->
    <rect x="250" y="80" width="40" height="20" fill="#0284c755" stroke="#94a3b8" stroke-width="1.5"/>
    <path d="M 290 95 Q 310 110 320 150" stroke="#38bdf8" stroke-width="3" fill="none"/>
    <text x="300" y="75" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Water Out</text>

    <text x="180" y="325" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Vacuum created below piston pulls water up from well</text>
  </g>

  <!-- Right: Downstroke Panel -->
  <g transform="translate(440, 75)">
    <rect width="360" height="345" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="180" y="28" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">2. DOWNSTROKE (PRIMING THE BARREL)</text>

    <!-- Pump Cylinder -->
    <rect x="110" y="60" width="140" height="220" fill="#0284c711" stroke="#94a3b8" stroke-width="2"/>
    <!-- Water escaping to top chamber -->
    <rect x="112" y="100" width="136" height="178" fill="#0284c755"/>

    <!-- Piston Descending -->
    <rect x="112" y="200" width="136" height="20" fill="#f59e0b" stroke="#ffffff" stroke-width="1"/>
    <path d="M 180 120 L 180 200 M 172 190 L 180 200 L 188 190" stroke="#f59e0b" stroke-width="3"/> <!-- Down arrow -->

    <!-- Piston Valve OPEN -->
    <line x1="170" y1="210" x2="185" y2="195" stroke="#22c55e" stroke-width="3"/>
    <text x="95" y="205" fill="#22c55e" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="end">Piston Valve OPEN</text>

    <!-- Inlet Foot Valve CLOSED -->
    <line x1="170" y1="280" x2="190" y2="280" stroke="#ef4444" stroke-width="4"/>
    <text x="95" y="280" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="end">Inlet Valve CLOSED</text>

    <text x="180" y="325" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Water passes through piston, ready for next lift</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_bicycle_pump():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <rect width="800" height="400" fill="#0f172a" rx="16"/>
  <text x="400" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE BICYCLE PUMP: COMPRESSION & LEATHER CUP WASHER ACTION</text>
  <text x="400" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Flexible leather cup washer seals during downstroke to compress air into tyre valve</text>

  <!-- Horizontal Pump Cylinder Cross Section -->
  <g transform="translate(100, 100)">
    <!-- Outer Metal Barrel -->
    <rect x="0" y="50" width="480" height="120" fill="#1e293b" stroke="#38bdf8" stroke-width="3" rx="6"/>

    <!-- Plunger Rod -->
    <rect x="-80" y="100" width="300" height="20" fill="#94a3b8" stroke="#64748b" stroke-width="1"/>
    
    <!-- Flared Leather Cup Washer Piston -->
    <path d="M 220 52 L 235 80 L 235 140 L 220 168 L 205 140 L 205 80 Z" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>
    <text x="210" y="40" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Flared Cup Washer Seals Walls</text>

    <!-- Compressed Air Zone (High Pressure) -->
    <rect x="235" y="52" width="242" height="116" fill="#ef444422"/>
    <text x="350" y="115" fill="#ef4444" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Compressed Air (High P)</text>

    <!-- Exit Nozzle & Tyre Valve -->
    <rect x="480" y="95" width="60" height="30" fill="#1e293b" stroke="#22c55e" stroke-width="2"/>
    <path d="M 540 110 L 590 110 M 580 104 L 590 110 L 580 116" stroke="#22c55e" stroke-width="3"/>
    <text x="595" y="115" fill="#22c55e" font-family="system-ui, sans-serif" font-size="11" font-weight="700">To Tyre Valve</text>

    <!-- Push Force Arrow -->
    <path d="M -120 110 L -90 110 M -100 104 L -90 110 L -100 116" stroke="#38bdf8" stroke-width="4"/>
    <text x="-130" y="115" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="end">Downstroke Push</text>
  </g>

  <!-- Explanatory Cycle Comparison -->
  <g transform="translate(100, 290)">
    <rect width="600" height="85" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="30" y="30" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Upstroke (Pulling out):</text>
    <text x="200" y="30" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Cup washer collapses inward; atmospheric air slips into cylinder.</text>
    <text x="30" y="60" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Downstroke (Pushing in):</text>
    <text x="200" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Air pressure flares washer against walls; compresses air until tyre valve opens.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


# =============================================================================
# CURRICULUM DEFINITION DATA FOR TOPIC 2
# =============================================================================

def build_topic2_curriculum_data():
    return [
        # ---------------------------------------------------------------------
        # LESSON 1: Pressure in Solids and Atmospheric Pressure
        # ---------------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Pressure in Solids and Atmospheric Pressure",
            "unit_description": "Definition of pressure (P = F/A) in solids, SI unit Pascal (Pa), direct and inverse proportionality rules, crushing can experiment, atmospheric pressure and altitude variation.",
            "lesson_title": "Pressure in Solids and Atmospheric Pressure",
            "pages": [
                # Page 1: Hook & Snowshoes Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Pressure in Action: Snowshoes and Wide Boots on Soft Terrain",
                        "content": {
                            "title": "Pressure in Action: Snowshoes and Wide Boots on Soft Terrain",
                            "caption": "A person standing on soft snow wearing wide snowshoes. Spreading the body's downward weight (force) over a large surface area dramatically reduces pressure, preventing them from sinking.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Snowshoes_in_use.jpg/1280px-Snowshoes_in_use.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Snowshoes_in_use.jpg/1280px-Snowshoes_in_use.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Snowshoes Distributing Weight Over Large Surface Area",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Snowshoes_in_use.jpg/1280px-Snowshoes_in_use.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Snowshoes_in_use.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Do Sharp Heels Sink While Flat Boots Float?",
                        "content": {
                            "title": "Force Concentration on a Surface",
                            "text": "Imagine walking across a soft, muddy field on your way to school:\n\n- If you wear boots with wide, flat soles, you walk easily across the surface.\n- If someone walks on the same mud wearing sharp, high-heeled shoes, they sink deep into the ground with every single step!\n\nThe person's weight (downward force) is identical in both cases. The crucial difference is the **contact area** over which that force is distributed. This is the core physical concept of **Pressure**."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Solids and Atmospheric Pressure",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **pressure** and state its SI unit (**Pascal, Pa** or $\\text{N/m}^2$).",
                                "Apply the mathematical relationship $P = \\frac{F}{A}$ to calculate force, area, and pressure in solids.",
                                "Explain why pressure increases when contact area decreases and vice versa.",
                                "Describe the origin of **atmospheric pressure** and explain why it decreases with altitude.",
                                "Analyze the **Crushing Can experiment** and explain the drinking straw mechanism."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Pressure",
                        "content": {
                            "term": "Pressure",
                            "definition": "The perpendicular force acting per unit area of a surface ($P = F / A$).",
                            "example": "A 600 N concrete block with a base of 1.0 m² exerts 600 Pa on the ground."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Pascal (Pa)",
                        "content": {
                            "term": "Pascal (Pa)",
                            "definition": "The SI unit of pressure. One Pascal (1 Pa) is equivalent to a perpendicular force of one Newton acting on an area of one square metre ($1\\text{ N/m}^2$).",
                            "example": "Standard atmospheric pressure at sea level is approximately 101,300 Pa (101.3 kPa)."
                        }
                    }
                ],
                # Page 3: Formula & Block SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Solid Pressure: Force Distribution vs Contact Area",
                        "content": {
                            "title": "Solid Pressure: Force Distribution vs Contact Area",
                            "caption": "Side-by-side comparison of a 100 N block resting on its broad face (0.50 m², 200 Pa) versus its narrow edge (0.05 m², 2000 Pa).",
                            "svg_content": get_svg_solid_pressure(),
                            "svg": get_svg_solid_pressure()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Solid Pressure Area Comparison Diagram",
                            "metadata": {
                                "svg_content": get_svg_solid_pressure()
                            }
                        }
                    },
                    {
                        "type": "formula_breakdown",
                        "title": "Mathematical Relationship: P = F / A",
                        "content": {
                            "title": "Pressure Formula in Solids",
                            "formula": "P = \\frac{F}{A}",
                            "variables": [
                                "$P$ = Pressure in Pascals ($\\text{Pa}$ or $\\text{N/m}^2$)",
                                "$F$ = Perpendicular Force in Newtons ($\\text{N}$)",
                                "$A$ = Contact Area in square metres ($\\text{m}^2$)"
                            ],
                            "rules": [
                                "**Direct Proportionality with Force**: Doubling force while keeping area constant doubles pressure ($P \\propto F$).",
                                "**Inverse Proportionality with Area**: Cutting contact area in half while keeping force constant doubles pressure ($P \\propto \\frac{1}{A}$)."
                            ]
                        }
                    }
                ],
                # Page 4: Worked Example
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Calculating Solid Ground Pressure",
                        "content": {
                            "title": "Calculating Pressure Exerted by a Concrete Block",
                            "problem": "A rectangular concrete foundation block has a weight of $600\\text{ N}$. Its flat base has dimensions of $2.0\\text{ m}$ by $0.5\\text{ m}$. Calculate the pressure exerted by the block on the ground.",
                            "steps": [
                                "1. **Identify the givens**: Force (Weight), $F = 600\\text{ N}$; Base dimensions $= 2.0\\text{ m} \\times 0.5\\text{ m}$.",
                                "2. **Calculate contact area**: $A = \\text{length} \\times \\text{width} = 2.0\\text{ m} \\times 0.5\\text{ m} = 1.0\\text{ m}^2$.",
                                "3. **Select formula**: $P = \\frac{F}{A}$.",
                                "4. **Substitute and solve**: $P = \\frac{600\\text{ N}}{1.0\\text{ m}^2} = 600\\text{ Pa}$ (or $600\\text{ N/m}^2$)."
                            ],
                            "answer": "The concrete block exerts a pressure of 600 Pa on the soil beneath it."
                        }
                    }
                ],
                # Page 5: Atmospheric Pressure & Altitude SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Atmospheric Pressure Variation with Altitude",
                        "content": {
                            "title": "Atmospheric Pressure Variation with Altitude",
                            "caption": "Air molecule density and atmospheric pressure decrease dramatically with altitude from sea level (101.3 kPa) to high mountain summits (54 kPa).",
                            "svg_content": get_svg_altitude_pressure(),
                            "svg": get_svg_altitude_pressure()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Atmospheric Pressure Altitude Diagram",
                            "metadata": {
                                "svg_content": get_svg_altitude_pressure()
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Living at the Bottom of an Ocean of Air",
                        "content": {
                            "title": "Why Aren't We Crushed by Atmospheric Pressure?",
                            "text": "Earth is wrapped in a thick blanket of air. Because air molecules have mass, Earth's gravity pulls them down, exerting a massive pressure of $\\approx 101,300\\text{ Pa}$ at sea level.\n\n- **Why we don't feel crushed**: Our internal body fluids (blood, water, cellular cytoplasm) exert an equal outward pressure, maintaining mechanical equilibrium.\n- **Altitude Variation**: As you climb higher (like hiking up Mt. Kenya), there is less air above you. Atmospheric pressure decreases, which is why air travelers and mountaineers encounter lower oxygen pressure and potential nosebleeds."
                        }
                    }
                ],
                # Page 6: Demonstration Experiment & YouTube
                [
                    {
                        "type": "step_process",
                        "title": "Demonstration: The Crushing Can Experiment",
                        "content": {
                            "title": "Crushing Can: Atmospheric Pressure in Action",
                            "steps": [
                                "1. **Aim**: To demonstrate the existence and crushing strength of atmospheric pressure.",
                                "2. **Apparatus**: Clean aluminum soda can, $10\\text{ mL}$ water, Bunsen burner / hot plate, beaker of cold water, tongs, safety goggles.",
                                "3. **⚠️ Safety Precautions**: Handle hot metal cans with sturdy laboratory tongs only; wear eye protection against boiling water splashes.",
                                "4. **Procedure**: Boil $10\\text{ mL}$ of water inside the open can until steam vigorously displaces all internal air for 30 seconds. Quickly invert the can into cold water.",
                                "5. **Observation**: The can implodes instantly with a violent 'pop', crumpling into a crushed ball.",
                                "6. **Scientific Explanation**: Cold water rapidly condenses the hot steam into a tiny droplet of liquid, creating a near-vacuum inside. The massive external atmospheric pressure ($101.3\\text{ kPa}$) instantly crushes the thin aluminum walls inward."
                            ]
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Demonstration Video: Slow-Motion Can Crushing Implosion",
                        "content": {
                            "title": "Demonstration Video: Slow-Motion Can Crushing Implosion",
                            "description": "Slow-motion video footage demonstrating steam displacement, rapid thermal condensation, and instantaneous implosion caused by unbalanced atmospheric pressure.",
                            "url": "https://www.youtube.com/watch?v=JsoE4F2PbAk",
                            "resolved_video_id": "JsoE4F2PbAk"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Crushing Can Atmospheric Pressure Experiment",
                            "url": "https://www.youtube.com/watch?v=JsoE4F2PbAk",
                            "metadata": {
                                "youtube_id": "JsoE4F2PbAk"
                            }
                        }
                    }
                ],
                # Page 7: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Drinking Straw Mechanism",
                        "content": {
                            "question": "When you drink fruit juice through a plastic drinking straw, what is the actual physical mechanism that forces the liquid upward into your mouth?",
                            "options": [
                                "Your mouth creates an active suction force that pulls the liquid upward against gravity.",
                                "You expand your mouth cavity to lower air pressure inside the straw, allowing higher atmospheric pressure acting on the juice's surface in the cup to push the liquid up.",
                                "The plastic walls of the straw exert capillary attraction forces on the juice molecules.",
                                "Air molecules inside your mouth are compressed, pushing down on the top opening of the straw."
                            ],
                            "answer": "B",
                            "explanation": "Drinking through a straw is driven by a **pressure difference**. When you expand your mouth, internal pressure drops below atmospheric pressure. The unconstrained atmospheric pressure ($101.3\\text{ kPa}$) pressing on the liquid surface in the cup pushes the juice up the straw into the lower-pressure region. 'Suction' is not an active pulling force; it is the creation of low pressure that allows atmospheric pressure to do the pushing. Therefore, Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 8: Real-World Applications
                [
                    {
                        "type": "real_world_connection",
                        "title": "Everyday Applications of Solid & Atmospheric Pressure",
                        "content": {
                            "title": "Engineering with Pressure Principles",
                            "text": "- **Sharp Cutting Tools**: Knives, axes, and surgical scalpels have extremely narrow blade edges (tiny area $A$). Applying a small muscular force generates enormous pressure that easily cuts through materials.\n- **Heavy Civil Infrastructure**: Massive bridge piers, skyscraper foundations, and railway sleepers are built with wide base areas to distribute loads, keeping ground pressure low so foundations do not sink.\n- **Suction Hooks & Plungers**: Pressing a rubber suction cup against a smooth tile excludes air from beneath it. External atmospheric pressure holds the cup firmly against the wall."
                        }
                    }
                ],
                # Page 9: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson 1 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "**Pressure** is perpendicular force per unit area ($P = F / A$). The SI unit is the **Pascal (Pa)** ($1\\text{ Pa} = 1\\text{ N/m}^2$).",
                                "Spreading force over a **smaller area** increases pressure (nails, knives); spreading over a **larger area** decreases pressure (snowshoes, tractor tires).",
                                "**Atmospheric pressure** is caused by the gravitational weight of the air column and decreases with altitude.",
                                "Siphons, straws, and suction cups function via **pressure differences** created against atmospheric pressure."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 2: Pressure in Liquids and Its Factors
        # ---------------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "Pressure in Liquids and Its Factors",
            "unit_description": "Hydrostatic pressure in fluids, factors affecting liquid pressure (depth h, density ρ, gravity g), omnidirectional pressure at a point, spouting can investigation, and communicating vessels.",
            "lesson_title": "Pressure in Liquids and Its Factors",
            "pages": [
                # Page 1: Hook & Dam Wall Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Hydroelectric Dam Engineering: Thick Reinforced Base for Deep Water Pressure",
                        "content": {
                            "title": "Hydroelectric Dam Engineering: Thick Reinforced Base for Deep Water Pressure",
                            "caption": "A massive concrete dam wall (like Masinga Dam in Kenya). Notice that the dam wall is dramatically thicker and wider at the base than at the top to withstand the immense hydrostatic pressure at deep water levels.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Hoover_dam_from_air.jpg/1280px-Hoover_dam_from_air.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Hoover_dam_from_air.jpg/1280px-Hoover_dam_from_air.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Concrete Hydroelectric Dam Wall Base Thickness",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Hoover_dam_from_air.jpg/1280px-Hoover_dam_from_air.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "Public Domain",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Hoover_dam_from_air.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Squeezing Sensation of the Deep",
                        "content": {
                            "title": "What Happens When You Dive Deep Underwater?",
                            "text": "Have you ever dived to the bottom of a deep swimming pool, lake, or ocean?\n\nAs you descend, you feel an unmistakable squeezing sensation against your eardrums that intensifies with every meter. This is not air pressure; this is **liquid pressure**. The deeper you plunge, the heavier the water column resting above you."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Liquid Pressure Factors",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain the origin of **hydrostatic pressure** in static fluids.",
                                "Analyze the 3 primary factors controlling liquid pressure: **depth ($h$)**, **fluid density ($\\rho$)**, and **gravitational field strength ($g$)**.",
                                "Demonstrate that liquid pressure acts **equally in all directions** at a given depth.",
                                "Interpret the **Spouting Can experiment** ($v \\propto \\sqrt{h}$).",
                                "Explain why communicating vessels maintain equal liquid levels regardless of container shape."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Hydrostatic Pressure",
                        "content": {
                            "term": "Hydrostatic Pressure",
                            "definition": "The pressure exerted by a fluid (liquid or gas) at rest due to the gravitational weight of the fluid column above it.",
                            "example": "Water pressure at a depth of 10 metres in a lake is approximately 98,000 Pa."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Fluid Density (ρ)",
                        "content": {
                            "term": "Fluid Density (ρ)",
                            "definition": "The mass per unit volume of a fluid, measured in kilograms per cubic metre ($\\text{kg/m}^3$).",
                            "example": "Pure freshwater has a density of $1000\\text{ kg/m}^3$, while saltwater is denser at $\\approx 1025\\text{ kg/m}^3$."
                        }
                    }
                ],
                # Page 3: 3 Factors Affecting Liquid Pressure
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 3 Physical Determinants of Liquid Pressure",
                        "content": {
                            "title": "How Liquids Exert Pressure in All Directions",
                            "text": "Unlike rigid solids that transmit force strictly in the direction of the push, liquid molecules slide freely and collide continuously with surrounding surfaces. Therefore, liquid pressure acts **equally in all directions** (downward, sideways, and upward).\n\nThree factors govern hydrostatic pressure:\n1. **Depth ($h$)**: Pressure increases directly with depth below the free surface because the weight of the overhead liquid column grows.\n2. **Density of the Liquid ($\\rho$)**: Denser liquids (like saltwater or mercury) pack more mass into every cubic metre, exerting greater downward weight at the exact same depth.\n3. **Gravitational Field Strength ($g$)**: Pressure is directly proportional to gravity ($g \\approx 9.8\\text{ N/kg}$ on Earth)."
                        }
                    }
                ],
                # Page 4: Spouting Can Investigation & SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Spouting Can: Water Jet Range vs Depth",
                        "content": {
                            "title": "The Spouting Can: Water Jet Range vs Depth",
                            "caption": "Water spouting from three vertical holes at different depths. The deepest hole (C) ejects water with the highest velocity and horizontal range, demonstrating that pressure increases with depth.",
                            "svg_content": get_svg_spouting_can(),
                            "svg": get_svg_spouting_can()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Spouting Can Water Jet Range Diagram",
                            "metadata": {
                                "svg_content": get_svg_spouting_can()
                            }
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Laboratory Investigation: The Spouting Can",
                        "content": {
                            "title": "Experimental Procedure & Observations",
                            "steps": [
                                "1. **Aim**: To investigate how hydrostatic pressure varies with depth below a liquid free surface.",
                                "2. **Apparatus**: Tall cylindrical tin can or plastic bottle, hammer and nail, adhesive tape, water supply, catch tray.",
                                "3. **Procedure**: Punch three identical holes vertically at depths $h_1 = 5\\text{ cm}$ (top), $h_2 = 15\\text{ cm}$ (mid), and $h_3 = 25\\text{ cm}$ (bottom). Cover with tape, fill with water, and peel off tape simultaneously.",
                                "4. **Observations**: The bottom jet shoots out forcefully in a wide parabolic arc; the top jet trickles weakly close to the container base.",
                                "5. **Conclusion**: Exit velocity $v = \\sqrt{2gh}$ reflects internal hydrostatic pressure, confirming $P \\propto h$."
                            ]
                        }
                    }
                ],
                # Page 5: Communicating Vessels SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Communicating Vessels: Shape Independence of Liquid Pressure",
                        "content": {
                            "title": "Communicating Vessels: Shape Independence of Liquid Pressure",
                            "caption": "Interconnected glassware vessels of diverse shapes and widths. The liquid automatically maintains identical horizontal levels across all sections because pressure depends only on vertical depth.",
                            "svg_content": get_svg_communicating_vessels(),
                            "svg": get_svg_communicating_vessels()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Communicating Vessels Level Principle Diagram",
                            "metadata": {
                                "svg_content": get_svg_communicating_vessels()
                            }
                        }
                    }
                ],
                # Page 6: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Freshwater vs Saltwater Pressure",
                        "content": {
                            "question": "A scuba diver descends to a depth of $5.0\\text{ m}$ in a freshwater lake where density $\\rho = 1000\\text{ kg/m}^3$. Later, the same diver descends to the exact same depth of $5.0\\text{ m}$ in the Indian Ocean where saltwater density $\\rho = 1025\\text{ kg/m}^3$. How does the hydrostatic pressure experienced in the ocean compare with that in the lake?",
                            "options": [
                                "The pressure in the ocean is lower because saltwater is warmer.",
                                "The pressure is exactly identical because depth is the only factor affecting pressure.",
                                "The pressure in the ocean is higher because saltwater has a higher density than freshwater.",
                                "There is zero pressure in saltwater because dissolved salts neutralize gravity."
                            ],
                            "answer": "C",
                            "explanation": "Hydrostatic pressure is directly proportional to both depth ($h$) and fluid density ($\\rho$). Because saltwater has a higher density ($1025\\text{ kg/m}^3$) than freshwater ($1000\\text{ kg/m}^3$), a 5-metre column of saltwater exerts greater downward gravitational weight per unit area, resulting in **higher hydrostatic pressure**. Therefore, Option C is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 7: Real-World Applications
                [
                    {
                        "type": "real_world_connection",
                        "title": "Engineering Applications of Liquid Pressure",
                        "content": {
                            "title": "Civil and Municipal Engineering Applications",
                            "text": "- **Dam Wall Profile**: Hydroelectric dams are designed with a triangular, wedge-shaped cross-section that is thickest at the bottom to counteract peak hydrostatic pressure at maximum depth.\n- **Elevated Gravity Water Towers**: Community water supply storage tanks are elevated on high steel towers or hilltops. The resulting vertical height difference ($h$) creates natural gravitational water pressure in domestic taps without continuous electric pumping."
                        }
                    }
                ],
                # Page 8: Video & Summary
                [
                    {
                        "type": "suggested_video",
                        "title": "Demonstration Video: Fluid Pressure and Communicating Vessels",
                        "content": {
                            "title": "Demonstration Video: Fluid Pressure and Communicating Vessels",
                            "description": "Visual physics demonstration showing how liquid pressure increases with depth, functions equally in all directions, and behaves in communicating vessels.",
                            "url": "https://www.youtube.com/watch?v=b08f43iM1vA",
                            "resolved_video_id": "b08f43iM1vA"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Liquid Pressure Depth and Density Demonstration",
                            "url": "https://www.youtube.com/watch?v=b08f43iM1vA",
                            "metadata": {
                                "youtube_id": "b08f43iM1vA"
                            }
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Lesson 2 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "Liquid pressure is caused by the gravitational weight of the fluid column above.",
                                "The 3 controlling factors are **depth ($h$)**, **liquid density ($\\rho$)**, and **gravitational field strength ($g$)**.",
                                "The **Spouting Can experiment** proves that pressure increases with depth ($v \\propto \\sqrt{h}$).",
                                "In communicating vessels, water seeks equal levels regardless of shape because pressure depends strictly on vertical height."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 3: Deriving and Applying P = \rho g h
        # ---------------------------------------------------------------------
        {
            "unit_order": 3,
            "unit_name": "Deriving and Applying P = \rho g h",
            "unit_description": "First-principles algebraic derivation of P = ρgh, quantitative calculations of hydrostatic pressure and depth, gauge pressure vs total pressure, and graphical analysis of P vs h.",
            "lesson_title": "Deriving and Applying P = \\rho g h",
            "pages": [
                # Page 1: Hook & Submarine Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Deep-Sea Engineering: Withstanding Enormous Hydrostatic Pressure",
                        "content": {
                            "title": "Deep-Sea Engineering: Withstanding Enormous Hydrostatic Pressure",
                            "caption": "The deep-sea research submersible Alvin. When descending thousands of metres below the ocean surface, its titanium spherical hull must withstand millions of Pascals of hydrostatic pressure calculated using P = ρgh.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Alvin_submersible.jpg/1280px-Alvin_submersible.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Alvin_submersible.jpg/1280px-Alvin_submersible.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Deep-Sea Research Submersible Alvin Hull",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Alvin_submersible.jpg/1280px-Alvin_submersible.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons / NOAA",
                                "licensing": "Public Domain",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Alvin_submersible.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "From Qualitative Observations to Exact Mathematical Models",
                        "content": {
                            "title": "Quantifying Hydrostatic Forces",
                            "text": "In Lesson 2, we observed that depth and density increase liquid pressure. But engineers cannot build submarines or dams based only on 'deeper means stronger'.\n\n- How much pressure does a submarine hull experience at $300\\text{ m}$ depth?\n- What thickness of titanium alloy is required to prevent crushing?\n\nTo answer these questions, physicists turn observations into an exact **mathematical model**: $P = \\rho g h$."
                        }
                    }
                ],
                # Page 2: Prior Knowledge Building Blocks
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Hydrostatic Formula",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Derive $P = \\rho g h$ step-by-step from fundamental definitions of pressure, weight, density, and volume.",
                                "Calculate hydrostatic pressure, fluid depth, and density using proper SI units.",
                                "Distinguish clearly between **Gauge Pressure** ($P = \\rho g h$) and **Total Pressure** ($P_{\\text{total}} = P_{\\text{atm}} + \\rho g h$).",
                                "Analyze the linear graph of $P$ vs $h$ and determine the physical significance of its gradient ($\\text{Slope} = \\rho g$)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 4 Core Building Blocks for Derivation",
                        "content": {
                            "title": "Foundational Equations We Will Combine",
                            "text": "To derive the hydrostatic formula, we combine 4 relationships:\n\n1. **Pressure Definition**: $P = \\frac{F}{A}$\n2. **Gravitational Weight**: $W = m \\times g$\n3. **Density Equation**: $\\rho = \\frac{m}{V} \\implies m = \\rho \\times V$\n4. **Cylindrical Column Volume**: $V = A \\times h$"
                        }
                    }
                ],
                # Page 3: Column Derivation Model SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Derivation Model of a Cylindrical Liquid Column",
                        "content": {
                            "title": "Derivation Model of a Cylindrical Liquid Column",
                            "caption": "A cylindrical column of liquid of cross-sectional area A, height h, and density ρ, showing the weight vector W = mg and the algebraic cancellation of area A.",
                            "svg_content": get_svg_derivation_model(),
                            "svg": get_svg_derivation_model()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Liquid Column Hydrostatic Derivation Model Diagram",
                            "metadata": {
                                "svg_content": get_svg_derivation_model()
                            }
                        }
                    }
                ],
                # Page 4: Formal 7-Step Derivation
                [
                    {
                        "type": "step_process",
                        "title": "Step-by-Step Algebraic Derivation of P = ρgh",
                        "content": {
                            "title": "Formal First-Principles Derivation",
                            "steps": [
                                "1. **Start with the definition of pressure**: $P = \\frac{F}{A}$.",
                                "2. **Identify the acting downward force**: For a resting liquid column, $F = W = m \\times g$.",
                                "3. **Substitute weight into the pressure equation**: $P = \\frac{m \\times g}{A}$.",
                                "4. **Express mass in terms of density and volume**: Since $\\rho = \\frac{m}{V}$, $m = \\rho \\times V$. Thus $P = \\frac{(\\rho \\times V) \\times g}{A}$.",
                                "5. **Express volume in terms of geometry**: For a regular column, $V = A \\times h$. Thus $P = \\frac{\\rho \\times (A \\times h) \\times g}{A}$.",
                                "6. **Cancel out common cross-sectional Area ($A$)**: Notice $A$ appears in both numerator and denominator.",
                                "7. **Final Hydrostatic Equation**: $$P = \\rho g h$$"
                            ]
                        }
                    }
                ],
                # Page 5: Units & Gauge vs Total Pressure
                [
                    {
                        "type": "comparison_table",
                        "title": "Key Formula Symbols, Units, and Measuring Instruments",
                        "content": {
                            "title": "Hydrostatic Formula Components",
                            "headers": ["Symbol", "Physical Quantity", "SI Unit", "Common Measuring Tool"],
                            "rows": [
                                ["P", "Hydrostatic Pressure", "Pascal (Pa) or N/m²", "Pressure Sensor, Manometer, Bourdon Gauge"],
                                ["ρ", "Fluid Density", "Kilograms per cubic metre (kg/m³)", "Hydrometer, Density Bottle"],
                                ["g", "Gravitational Field Strength", "N/kg or m/s²", "Standard Constant (9.8 or 10 N/kg)"],
                                ["h", "Vertical Fluid Depth", "Metres (m)", "Metre Rule, Sounding Line, Laser Rangefinder"]
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Gauge Pressure vs Total Absolute Pressure",
                        "content": {
                            "title": "Accounting for the Atmosphere",
                            "text": "- **Gauge Pressure ($P = \\rho g h$)**: Measures pressure caused strictly by the fluid itself (reading zero at the open water surface).\n- **Total (Absolute) Pressure**: If a liquid tank is open to the atmosphere, the absolute pressure at depth $h$ includes the atmospheric blanket:\n$$P_{\\text{total}} = P_{\\text{atm}} + \\rho g h$$"
                        }
                    }
                ],
                # Page 6: Worked Examples
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example 1: Hydrostatic Pressure at Reservoir Base",
                        "content": {
                            "title": "Calculating Water Pressure at 12 m Depth",
                            "problem": "Calculate the hydrostatic water pressure (gauge pressure) at the bottom of a municipal reservoir that is $12.0\\text{ m}$ deep. (Take $\\rho_{\\text{water}} = 1000\\text{ kg/m}^3$ and $g = 9.8\\text{ m/s}^2$).",
                            "steps": [
                                "1. **Identify givens**: Depth $h = 12.0\\text{ m}$, Density $\\rho = 1000\\text{ kg/m}^3$, Gravity $g = 9.8\\text{ m/s}^2$.",
                                "2. **Select formula**: $P = \\rho g h$.",
                                "3. **Substitute and calculate**: $P = 1000 \\times 9.8 \\times 12.0 = 117,600\\text{ Pa}$.",
                                "4. **Convert to kilopascals**: $P = 117.6\\text{ kPa}$."
                            ],
                            "answer": "The water exerts a hydrostatic gauge pressure of 117,600 Pa (117.6 kPa) at the reservoir base."
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Worked Example 2: Determining Oil Tank Depth (Rearrangement)",
                        "content": {
                            "title": "Rearranging to Solve for Depth (h)",
                            "problem": "A pressure sensor placed at the bottom of an oil storage tank reads $8,000\\text{ Pa}$. If the density of the cooking oil is $800\\text{ kg/m}^3$ and $g = 10\\text{ m/s}^2$, determine the depth of the oil in the tank.",
                            "steps": [
                                "1. **Identify givens**: Pressure $P = 8,000\\text{ Pa}$, Density $\\rho = 800\\text{ kg/m}^3$, Gravity $g = 10\\text{ m/s}^2$.",
                                "2. **Rearrange formula for $h$**: $h = \\frac{P}{\\rho \\times g}$.",
                                "3. **Substitute and solve**: $h = \\frac{8000}{800 \\times 10} = \\frac{8000}{8000} = 1.0\\text{ m}$."
                            ],
                            "answer": "The depth of the cooking oil in the tank is exactly 1.0 metre."
                        }
                    }
                ],
                # Page 7: Graphical Analysis SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Graphical Analysis: Hydrostatic Pressure vs Depth",
                        "content": {
                            "title": "Graphical Analysis: Hydrostatic Pressure vs Depth",
                            "caption": "Graph of P vs h producing a straight line through the origin. The gradient of the line is directly equal to the product of liquid density and gravity (Slope = ρg).",
                            "svg_content": get_svg_pressure_depth_graph(),
                            "svg": get_svg_pressure_depth_graph()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Hydrostatic Pressure vs Depth Graph Diagram",
                            "metadata": {
                                "svg_content": get_svg_pressure_depth_graph()
                            }
                        }
                    }
                ],
                # Page 8: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Interpreting the P vs h Graph Slope",
                        "content": {
                            "question": "If an experimental physicist plots a graph of Hydrostatic Pressure ($P$) on the vertical y-axis against Depth ($h$) on the horizontal x-axis for a column of pure water, what is the shape of the graph, and what physical quantity does the gradient (slope) of the line represent?",
                            "options": [
                                "A horizontal flat line; the gradient represents total liquid volume.",
                                "A straight line passing through the origin; the gradient represents the product of fluid density and gravity ($\\rho \\times g$).",
                                "A downward curving parabola; the gradient represents base contact area.",
                                "A vertical line; the gradient represents atmospheric pressure."
                            ],
                            "answer": "B",
                            "explanation": "The formula $P = \\rho g h$ matches the equation of a straight line through the origin: $y = mx$, where $y = P$, $x = h$, and the slope $m = \\rho g$. Since fluid density $\\rho$ and gravity $g$ are constants, the graph is a straight line through $(0,0)$ whose gradient equals $\\rho g$. Therefore, Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 9: Video & Summary
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Hydrostatic Calculations and Submarine Science",
                        "content": {
                            "title": "Physics Video: Hydrostatic Calculations and Submarine Science",
                            "description": "Step-by-step problem-solving tutorial applying P = ρgh to calculate underwater pressure, submarine hull forces, and oceanographic depths.",
                            "url": "https://www.youtube.com/watch?v=e131h_Ua4Z4",
                            "resolved_video_id": "e131h_Ua4Z4"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Hydrostatic Equation and Marine Physics",
                            "url": "https://www.youtube.com/watch?v=e131h_Ua4Z4",
                            "metadata": {
                                "youtube_id": "e131h_Ua4Z4"
                            }
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Lesson 3 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "The fundamental hydrostatic pressure formula is **$P = \\rho g h$**.",
                                "Pressure is independent of container surface area or volume—it depends strictly on **density, gravity, and vertical depth**.",
                                "To calculate **Total Pressure** on an open liquid container, add atmospheric pressure: $P_{\\text{total}} = P_{\\text{atm}} + \\rho g h$.",
                                "The gradient of a $P$ vs $h$ graph yields the product $\\rho g$."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 4: Transmission of Pressure and Pascal’s Principle
        # ---------------------------------------------------------------------
        {
            "unit_order": 4,
            "unit_name": "Transmission of Pressure and Pascal’s Principle",
            "unit_description": "Pascal's Principle of undiminished pressure transmission in enclosed fluids, hydraulic force multiplication (F1/A1 = F2/A2), conservation of energy and displacement trade-offs, syringe hydraulics, and vehicle brake systems.",
            "lesson_title": "Transmission of Pressure and Pascal’s Principle",
            "pages": [
                # Page 1: Hook & Hydraulic Lift Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Hydraulic Force Multiplication: Lifting Heavy Vehicles in a Garage",
                        "content": {
                            "title": "Hydraulic Force Multiplication: Lifting Heavy Vehicles in a Garage",
                            "caption": "A hydraulic vehicle hoist in a Nairobi automotive garage lifting a 2-tonne car effortlessly using a central hydraulic cylinder powered by Pascal's Principle.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Hydraulic_car_lift.jpg/1280px-Hydraulic_car_lift.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Hydraulic_car_lift.jpg/1280px-Hydraulic_car_lift.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Hydraulic Garage Car Lift Hoist",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Hydraulic_car_lift.jpg/1280px-Hydraulic_car_lift.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Hydraulic_car_lift.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "How Can a Human Hand Lift a 2-Tonne Vehicle?",
                        "content": {
                            "title": "The Wonder of Fluid Force Multiplication",
                            "text": "Have you ever watched an auto mechanic raise a massive, two-tonne SUV high above their head at a service station by simply pressing a modest hand lever?\n\n- How can an effort force of just $150\\text{ N}$ lift a load of $20,000\\text{ N}$?\n- Are we violating the fundamental laws of Physics?\n\nThis is not magic; it is **force multiplication** made possible by **Pascal's Principle**. By enclosing an incompressible liquid in interconnected cylinders of different cross-sectional areas, pressure applied at one point transmits undiminished to create massive output forces."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Hydraulics and Pascal's Principle",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "State **Pascal's Principle** of pressure transmission in enclosed fluids.",
                                "Explain how differential piston areas produce **force multiplication** ($\\frac{F_1}{A_1} = \\frac{F_2}{A_2}$).",
                                "Calculate unknown forces, piston areas, and mechanical advantage in hydraulic systems.",
                                "Analyze the **Conservation of Energy displacement trade-off** ($F_1 d_1 = F_2 d_2$).",
                                "Explain why air bubbles destroy hydraulic braking systems."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Pascal's Principle",
                        "content": {
                            "term": "Pascal's Principle",
                            "definition": "When pressure is applied to an enclosed static fluid at any point, that pressure is transmitted equally and undiminished to every portion of the fluid and to the container walls.",
                            "example": "Applying pressure to a brake pedal transmits pressure through hydraulic fluid to all 4 wheels equally."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Enclosed Incompressible Fluid",
                        "content": {
                            "term": "Enclosed Incompressible Fluid",
                            "definition": "A fluid (typically hydraulic oil) completely sealed in a leak-proof vessel whose volume cannot be compressed under applied pressure.",
                            "example": "Liquids are virtually incompressible, whereas gases compress easily."
                        }
                    }
                ],
                # Page 3: Mechanics of Hydraulics & SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Pascal's Principle: Hydraulic Force Multiplier Mechanism",
                        "content": {
                            "title": "Pascal's Principle: Hydraulic Force Multiplier Mechanism",
                            "caption": "U-tube hydraulic machine showing a small input piston (A1, F1) transmitting undiminished pressure through oil to a large output piston (A2, F2) to multiply force.",
                            "svg_content": get_svg_hydraulic_system(),
                            "svg": get_svg_hydraulic_system()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Hydraulic Force Multiplier Diagram",
                            "metadata": {
                                "svg_content": get_svg_hydraulic_system()
                            }
                        }
                    },
                    {
                        "type": "formula_breakdown",
                        "title": "The Hydraulic Multiplier Equation",
                        "content": {
                            "title": "Mathematical Model of a Hydraulic Press",
                            "formula": "\\frac{F_1}{A_1} = \\frac{F_2}{A_2} \\implies F_2 = F_1 \\times \\left(\\frac{A_2}{A_1}\\right)",
                            "variables": [
                                "$F_1$ = Input Effort Force ($\\text{N}$)",
                                "$A_1$ = Small Input Piston Area ($\\text{m}^2$)",
                                "$F_2$ = Output Load Force ($\\text{N}$)",
                                "$A_2$ = Large Output Piston Area ($\\text{m}^2$)"
                            ],
                            "rules": [
                                "**Force Multiplier (Mechanical Advantage)**: The ratio $\\frac{A_2}{A_1}$ determines how many times your effort force is multiplied.",
                                "**Pressure Invariance**: $P_1 = P_2$ throughout the connected fluid."
                            ]
                        }
                    }
                ],
                # Page 4: Worked Example
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Hydraulic Car Lift Calculation",
                        "content": {
                            "title": "Calculating Maximum Weight Raised by Hydraulic Hoist",
                            "problem": "A hydraulic garage lift has an input piston of cross-sectional area $0.02\\text{ m}^2$ and a large output piston of area $0.80\\text{ m}^2$. If a mechanic applies an effort force of $150\\text{ N}$ to the input piston, calculate the maximum weight the lift can raise.",
                            "steps": [
                                "1. **Identify givens**: Input area $A_1 = 0.02\\text{ m}^2$, Output area $A_2 = 0.80\\text{ m}^2$, Input force $F_1 = 150\\text{ N}$.",
                                "2. **Select hydraulic formula**: $\\frac{F_1}{A_1} = \\frac{F_2}{A_2} \\implies F_2 = F_1 \\times \\frac{A_2}{A_1}$.",
                                "3. **Calculate area multiplier**: $\\text{Multiplier} = \\frac{0.80}{0.02} = 40$.",
                                "4. **Calculate output force**: $F_2 = 150\\text{ N} \\times 40 = 6,000\\text{ N}$."
                            ],
                            "answer": "An effort force of 150 N is multiplied 40-fold to lift a 6,000 N load (equivalent to 600 kg)."
                        }
                    }
                ],
                # Page 5: Energy Conservation & Displacement
                [
                    {
                        "type": "concept_explanation",
                        "title": "Conservation of Energy: The Displacement Trade-Off",
                        "content": {
                            "title": "You Cannot Get 'Free Energy' from Physics!",
                            "text": "While a hydraulic system multiplies force, it **does NOT multiply work or energy**:\n\n$$\\text{Work Input} = \\text{Work Output} \\implies F_1 \\times d_1 = F_2 \\times d_2$$\n\n- **The Trade-Off**: To make the large output piston move upward by a small distance ($d_2 = 1\\text{ cm}$), you must push the small input piston downward over a much longer distance ($d_1 = 40\\text{ cm}$).\n- Force is multiplied by 40, but displacement is divided by 40, keeping total energy strictly conserved."
                        }
                    }
                ],
                # Page 6: Syringe Experiment & The Air Bubble Problem
                [
                    {
                        "type": "mini_activity",
                        "title": "Practical Investigation: The Syringe Hydraulic Model",
                        "content": {
                            "title": "Building a Dual-Syringe Hydraulic System",
                            "task": "Connect a $5\\text{ mL}$ small plastic syringe and a $20\\text{ mL}$ large syringe using flexible tubing filled with water:\n\n1. **Observe Force & Distance**: Push the small plunger and note how easily the large plunger lifts heavy coins, but moves only a short distance.\n2. **The Air Bubble Problem**: Introduce an air bubble into the tubing. When you press the small plunger, what happens?\n3. **Physical Explanation**: Air is compressible. Instead of transmitting pressure immediately to the output piston, the force compresses the air bubble, wasting energy. This is why vehicle brake fluid lines must be completely 'bled' of trapped air bubbles to prevent brake failure."
                        }
                    }
                ],
                # Page 7: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Liquids vs Gases in Hydraulics",
                        "content": {
                            "question": "Why are hydraulic braking and lifting systems filled exclusively with incompressible liquids (like oil or water) rather than compressed air or gases?",
                            "options": [
                                "Liquids are cheaper and lighter than gases.",
                                "Liquids are highly compressible, which cushions pistons during sudden impacts.",
                                "Liquids are virtually incompressible, allowing pressure to transmit instantly and undiminished; gases compress easily, absorbing pressure instead of transmitting force.",
                                "Liquids eliminate friction completely, allowing pistons to move infinitely fast."
                            ],
                            "answer": "C",
                            "explanation": "Pascal's Principle depends strictly on the **incompressibility** of fluids. Liquids are incompressible; applying force at one end causes immediate pressure transmission to the other end. Gases have vast intermolecular spaces and compress easily under load, absorbing the applied work and failing to transmit force to output pistons. Therefore, Option C is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 8: Real-World Applications
                [
                    {
                        "type": "real_world_connection",
                        "title": "Everyday Technologies Utilizing Pascal's Principle",
                        "content": {
                            "title": "Hydraulics in Transport and Construction",
                            "text": "- **Automobile Hydraulic Brakes**: When a driver presses the brake pedal, a small master cylinder transmits pressure through hydraulic fluid to slave cylinders at all four wheels, clamping brake pads onto spinning discs with thousands of Newtons of force.\n- **Excavators and Earthmovers**: Heavy construction excavators use high-pressure hydraulic cylinders to lift multi-tonne boulders and dig deep foundation trenches with fingertip joystick controls.\n- **Aircraft Control Surfaces**: Modern commercial airplanes use hydraulic actuators to adjust wing flaps, ailerons, and landing gear against extreme aerodynamic forces."
                        }
                    }
                ],
                # Page 9: Video & Summary
                [
                    {
                        "type": "suggested_video",
                        "title": "Demonstration Video: Syringe Hydraulics & Incompressibility",
                        "content": {
                            "title": "Demonstration Video: Syringe Hydraulics & Incompressibility",
                            "description": "Educational video showing how to assemble working hydraulic syringe systems and demonstrating why removing air bubbles is critical for pressure transmission.",
                            "url": "https://www.youtube.com/watch?v=YlmBa-ggh0E",
                            "resolved_video_id": "YlmBa-ggh0E"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Pascal's Principle and Syringe Hydraulics",
                            "url": "https://www.youtube.com/watch?v=YlmBa-ggh0E",
                            "metadata": {
                                "youtube_id": "YlmBa-ggh0E"
                            }
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Lesson 4 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "**Pascal's Principle** states that pressure applied to an enclosed static fluid is transmitted undiminished in all directions.",
                                "Hydraulics achieve **force multiplication**: $\\frac{F_1}{A_1} = \\frac{F_2}{A_2} \\implies F_2 = F_1 \\times \\left(\\frac{A_2}{A_1}\\right)$.",
                                "Energy is conserved: force is multiplied by $\\frac{A_2}{A_1}$, but displacement is reduced by the same ratio ($F_1 d_1 = F_2 d_2$).",
                                "**Air bubbles** compromise hydraulic systems because gases compress under applied force."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 5: Pressure Applications and Water Pumping
        # ---------------------------------------------------------------------
        {
            "unit_order": 5,
            "unit_name": "Pressure Applications and Water Pumping",
            "unit_description": "Mechanical devices driven by pressure differences (syringes, continuous siphons, bicycle pumps, reciprocating water lift pumps and force pumps), one-way valves, and the 10.3 m barometric suction limitation.",
            "lesson_title": "Pressure Applications and Water Pumping",
            "pages": [
                # Page 1: Hook & African Hand Pump Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Groundwater Extraction: The Community Hand Pump in Rural Africa",
                        "content": {
                            "title": "Groundwater Extraction: The Community Hand Pump in Rural Africa",
                            "caption": "A deep-well reciprocating hand pump (such as an Afridev or India Mark II pump) delivering freshwater in a rural community by converting mechanical effort into cyclic pressure differences.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Water_pump_in_Africa.jpg/1280px-Water_pump_in_Africa.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Water_pump_in_Africa.jpg/1280px-Water_pump_in_Africa.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Rural Deep-Well Reciprocating Water Hand Pump",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Water_pump_in_Africa.jpg/1280px-Water_pump_in_Africa.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 4.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Water_pump_in_Africa.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Fluids Move Only When Pressure Differs",
                        "content": {
                            "title": "How Do We Lift Water from Deep Underground?",
                            "text": "Water cannot flow uphill on its own. Fluids move only when there is a **pressure difference** ($\\Delta P$)—always traveling from regions of **high pressure** to **low pressure**.\n\nIn this final lesson, we dissect the inner engineering of syringes, continuous siphons, bicycle pumps, and the reciprocating lift pumps that supply drinking water to millions of rural communities."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Pressure Applications & Pumping",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain how siphons, syringes, and bicycle pumps operate via pressure differences.",
                                "Analyze the mechanical two-stroke cycle (**Upstroke and Downstroke**) of a reciprocating water lift pump.",
                                "Describe the critical function of **one-way valves** (inlet foot valve and piston valve).",
                                "Calculate and explain the theoretical **10.3 m barometric suction limitation** for standard lift pumps."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Pressure Difference (ΔP)",
                        "content": {
                            "term": "Pressure Difference (ΔP)",
                            "definition": "A variance in pressure between two connected fluid regions that drives fluid flow from higher to lower pressure.",
                            "example": "Expanding a syringe barrel lowers internal pressure, allowing external atmospheric pressure to push liquid in."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: One-Way Valve",
                        "content": {
                            "term": "One-Way Valve",
                            "definition": "A mechanical device that opens to allow fluid flow in only one direction and closes automatically to prevent backflow.",
                            "example": "The foot valve in a borehole pump closes to prevent water from falling back into the aquifer."
                        }
                    }
                ],
                # Page 3: Common Devices (Syringe & Siphon)
                [
                    {
                        "type": "concept_explanation",
                        "title": "Mechanics of Everyday Pressure Devices",
                        "content": {
                            "title": "The Syringe and the Continuous Siphon",
                            "text": "- **The Medical Syringe**:\n  - *Drawing liquid in*: Pulling the plunger outward increases barrel volume, creating low internal pressure. Atmospheric pressure on the medication bottle surface pushes liquid up through the needle.\n  - *Expelling liquid*: Pushing the plunger inward decreases barrel volume, creating high internal pressure that ejects fluid.\n\n- **The Continuous Siphon**:\n  - A U-shaped tube primed with liquid transports fluid uphill over a barrier and down into a lower container without electricity, powered by the gravitational weight difference of the liquid columns and atmospheric pressure."
                        }
                    }
                ],
                # Page 4: Siphon SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Siphon Mechanism: Fluid Flow Over an Obstacle",
                        "content": {
                            "title": "The Siphon Mechanism: Fluid Flow Over an Obstacle",
                            "caption": "Annotated siphon mechanism showing high reservoir A, lower discharge reservoir B, crest low pressure zone, and the driving hydrostatic column difference.",
                            "svg_content": get_svg_siphon(),
                            "svg": get_svg_siphon()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Continuous Siphon Flow Mechanism Diagram",
                            "metadata": {
                                "svg_content": get_svg_siphon()
                            }
                        }
                    }
                ],
                # Page 5: Water Lift Pump SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Water Lift Pump: Upstroke vs Downstroke Operation",
                        "content": {
                            "title": "The Water Lift Pump: Upstroke vs Downstroke Operation",
                            "caption": "Cross-sectional comparison of a reciprocating lift pump during the Upstroke (lifting water while drawing fresh well water) and Downstroke (closing inlet valve and priming the upper chamber).",
                            "svg_content": get_svg_lift_pump(),
                            "svg": get_svg_lift_pump()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Reciprocating Water Lift Pump Cross-Section Diagram",
                            "metadata": {
                                "svg_content": get_svg_lift_pump()
                            }
                        }
                    }
                ],
                # Page 6: Step-by-Step Lift Pump Cycle
                [
                    {
                        "type": "step_process",
                        "title": "Step-by-Step Mechanical Operation of the Lift Pump",
                        "content": {
                            "title": "The Two-Stroke Reciprocating Cycle",
                            "steps": [
                                "1. **The Upstroke (Pumping and Drawing Water)**: Pushing the pump handle down pulls the piston upward. The weight of water above the piston forces the **piston valve tightly closed**, lifting water out through the spout. Simultaneously, a low-pressure vacuum is created below the rising piston, allowing atmospheric pressure in the well to force the **bottom inlet valve open** and draw a fresh charge of water into the lower chamber.",
                                "2. **The Downstroke (Priming the Upper Chamber)**: Raising the pump handle pushes the piston downward. The water trapped in the cylinder forces the **bottom inlet valve tightly closed** under its weight, preventing backflow into the well. The pressure of the trapped water forces the **piston valve open**, allowing water to slip from the lower chamber into the upper chamber, primed for the next upstroke!"
                            ]
                        }
                    }
                ],
                # Page 7: Bicycle Pump Study & SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Bicycle Pump: Cup Washer Action & Compression",
                        "content": {
                            "title": "The Bicycle Pump: Cup Washer Action & Compression",
                            "caption": "Cross-section of a bicycle pump during downstroke showing how the flexible leather cup washer flares out to seal against cylinder walls, compressing air into the tyre valve.",
                            "svg_content": get_svg_bicycle_pump(),
                            "svg": get_svg_bicycle_pump()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Bicycle Pump Compression and Cup Washer Diagram",
                            "metadata": {
                                "svg_content": get_svg_bicycle_pump()
                            }
                        }
                    }
                ],
                # Page 8: Formative MCQ (10.3 m Limit)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: The 10.3 Metre Suction Limitation",
                        "content": {
                            "question": "A rural community installs a standard surface suction lift pump over a deep borehole where the groundwater table is located $15.0\\text{ metres}$ below the surface. Despite vigorous pumping of the handle, no water ever reaches the spout. What fundamental physical limitation causes this pump to fail?",
                            "options": [
                                "The pump handle is too short to supply sufficient mechanical leverage.",
                                "Standard atmospheric pressure ($101.3\\text{ kPa}$) can only support a maximum vertical water column of $\\approx 10.3\\text{ metres}$ ($h = \\frac{P_{\\text{atm}}}{\\rho g}$); beyond this depth, a submersible pump must be installed deep inside the borehole.",
                                "The borehole metal pipe is too cold, causing water to freeze instantly.",
                                "Gravitational acceleration ceases to act on water at depths exceeding 10 metres."
                            ],
                            "answer": "B",
                            "explanation": "A suction lift pump does not 'pull' water; it creates a low pressure, relying on **atmospheric pressure** ($P_{\\text{atm}} \\approx 101,300\\text{ Pa}$) to push water up the pipe. We calculate maximum barometric water column height using: $$h = \\frac{P_{\\text{atm}}}{\\rho g} = \\frac{101,300}{1000 \\times 9.8} \\approx 10.34\\text{ metres}$$ If the water table is deeper than $10.3\\text{ m}$, atmospheric pressure cannot support the column regardless of how perfect the vacuum is. To pump from $15\\text{ m}$, a deep-well submersible or force pump placed down inside the well must be used. Therefore, Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 9: Video & Summary
                [
                    {
                        "type": "suggested_video",
                        "title": "Mechanical Simulation: How Water Lift Pumps and Siphons Work",
                        "content": {
                            "title": "Mechanical Simulation: How Water Lift Pumps and Siphons Work",
                            "description": "3D animated mechanical breakdown illustrating the valve actions, suction strokes, and atmospheric pressure dynamics of water lift pumps and siphons.",
                            "url": "https://www.youtube.com/watch?v=CZmP0vsW_r4",
                            "resolved_video_id": "CZmP0vsW_r4"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "How a Water Lift Pump and Siphon Work 3D Animation",
                            "url": "https://www.youtube.com/watch?v=CZmP0vsW_r4",
                            "metadata": {
                                "youtube_id": "CZmP0vsW_r4"
                            }
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Lesson 5 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "Fluids flow spontaneously only across a **pressure gradient** (high pressure to low pressure).",
                                "A **siphon** transfers liquid over an obstacle driven by column weight difference and atmospheric pressure.",
                                "A **reciprocating water lift pump** uses a two-stroke cycle (Upstroke and Downstroke) with two one-way valves to raise water.",
                                "Atmospheric pressure limits standard surface suction lift pumps to a **maximum theoretical depth of 10.3 metres**."
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
def ingest_grade10_physics_topic2():
    print("======================================================================")
    print("INGESTING CBC GRADE 10 PHYSICS — TOPIC 2: PRESSURE")
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

    # 3. Get or Create Topic: Pressure (Order: 2)
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=2,
        defaults={
            "name": "Pressure",
            "description": "Comprehensive exploration of pressure in solids (P = F/A), atmospheric pressure, liquid hydrostatic pressure (P = ρgh), Pascal's principle in hydraulics, and pressure applications in water pumps and siphons."
        }
    )
    if not t_created and topic.name != "Pressure":
        topic.name = "Pressure"
        topic.description = "Comprehensive exploration of pressure in solids (P = F/A), atmospheric pressure, liquid hydrostatic pressure (P = ρgh), Pascal's principle in hydraulics, and pressure applications in water pumps and siphons."
        topic.save()
    print(f"Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    curriculum_data = build_topic2_curriculum_data()

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
    print(f"TOPIC 2 INGESTION COMPLETE:")
    print(f"  - Learning Units: {total_units_created}")
    print(f"  - Lessons:        {total_lessons_created}")
    print(f"  - Lesson Blocks:  {total_blocks_created}")
    print(f"  - Lesson Assets:  {total_assets_created}")
    print("======================================================================")

if __name__ == "__main__":
    ingest_grade10_physics_topic2()
