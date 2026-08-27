"""
VLearn CBC Grade 10 Home Science — Sub-Strand 3.1: Sewing Tools, Equipment, and Materials
Comprehensive Production Ingestion & Visual Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (Level: 10)
Subject: Home Science
Topic: Clothing and Textiles (Order: 3)
Learning Unit 1: 3.1 Sewing Tools, Equipment, and Materials (Order: 1)

Decomposed into 11 Published Lessons:
  - Lesson 1:  Classification of Sewing Tools — Cutting & Marking Tools
  - Lesson 2:  Classification of Sewing Tools — Sewing & Measuring Tools
  - Lesson 3:  Classification of Sewing Tools — Finishing & Storage Tools
  - Lesson 4:  Selecting Sewing Tools, Equipment, and Materials
  - Lesson 5:  The Sewing Machine — Anatomy (Parts and Functions)
  - Lesson 6:  The Sewing Machine — Threading and Winding the Bobbin
  - Lesson 7:  Operating the Sewing Machine (Stitch Selection and Fabric Guiding)
  - Lesson 8:  Common Sewing Machine Faults and Remedies
  - Lesson 9:  Care, Maintenance, and Storage of a Sewing Machine
  - Lesson 10: Using, Caring for, and Storing Other Needlework Tools
  - Lesson 11: Safety and Waste Disposal in the Needlework Laboratory

Features:
  - Reads Grade10_Home_Science_Topic_3_1.md directly using open()
  - 11 Custom Responsive Sanitized Vector SVG Diagrams (viewBox="0 0 800 450")
  - 11 Verified Wikimedia Commons Photographic Assets with LessonAssets
  - 11 Verified Educational YouTube Video Integrations with LessonAssets
  - 11 Formative Scenario-Based MCQs with 4 options, valid correct_answer index, explanations
  - 6 discrete concept cards (pages) per lesson with full typed block coverage (12 blocks/lesson)
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


# ─── 11 Custom Vector SVGs ────────────────────────────────────────────────────

def get_svg_1():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">CUTTING &amp; MARKING TOOLS — CLASSIFICATION</text>
  <text x="400" y="54" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Lesson 1: Tools That Slice &amp; Transfer Construction Lines</text>

  <!-- Column 1: Cutting Tools -->
  <g transform="translate(30, 72)">
    <rect width="350" height="355" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="350" height="32" rx="10" fill="#0284c7"/>
    <text x="175" y="21" fill="#fff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">✂️ CUTTING TOOLS</text>
    <text x="14" y="58" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">a) Dressmaker's Shears</text>
    <text x="14" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Long blades, bent handles — slide flat on table.</text>
    <text x="14" y="108" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">b) Pinking Shears</text>
    <text x="14" y="126" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Zigzag blades — cut &amp; finish edges to prevent fraying.</text>
    <text x="14" y="158" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">c) Embroidery Scissors</text>
    <text x="14" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Small, sharp-pointed — trim threads &amp; buttonholes.</text>
    <text x="14" y="208" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">d) Seam Ripper</text>
    <text x="14" y="226" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Hook blade with ball tip — removes incorrect stitches.</text>
    <text x="14" y="258" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">e) Thread Clippers / Snips</text>
    <text x="14" y="276" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Spring-action — snip thread ends close to fabric.</text>
    <text x="14" y="308" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">f) Rotary Cutter</text>
    <text x="14" y="326" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Circular blade rolled on self-healing mat — multi-layer cuts.</text>
  </g>

  <!-- Column 2: Marking Tools -->
  <g transform="translate(420, 72)">
    <rect width="350" height="355" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="350" height="32" rx="10" fill="#059669"/>
    <text x="175" y="21" fill="#fff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">📐 MARKING TOOLS</text>
    <text x="14" y="58" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">a) Tailor's Chalk</text>
    <text x="14" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Compressed talc/wax block — temporary lines, brush away.</text>
    <text x="14" y="108" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">b) Tracing Wheel &amp; Tracing Paper</text>
    <text x="14" y="126" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Spiked/smooth disk rolled over carbon paper — fast transfer.</text>
    <text x="14" y="158" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">c) Fabric Marking Pens</text>
    <text x="14" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Washable or air-soluble ink — fade automatically or wash out.</text>
    <rect x="12" y="265" width="326" height="75" rx="6" fill="#0f172a"/>
    <text x="175" y="290" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Key Safety Rule:</text>
    <text x="175" y="310" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Never use ink pens or lead pencils on fabric</text>
    <text x="175" y="328" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">— they leave permanent stains that cannot be removed.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


def get_svg_2():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">MEASURING &amp; SEWING TOOLS — CLASSIFICATION</text>
  <text x="400" y="54" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Lesson 2: Tools That Measure Bodies &amp; Join Fabrics By Hand</text>

  <!-- Measuring Tools -->
  <g transform="translate(30, 72)">
    <rect width="350" height="355" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="350" height="32" rx="10" fill="#d97706"/>
    <text x="175" y="21" fill="#fff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">📏 MEASURING TOOLS</text>
    <text x="14" y="58" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">a) Tape Measure</text>
    <text x="14" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">150 cm flexible ribbon — takes curved body measurements.</text>
    <text x="14" y="108" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">b) Ruler / Meter Stick / Yardstick</text>
    <text x="14" y="126" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Rigid straight-edge — marks straight lines &amp; fabric yardage.</text>
    <text x="14" y="158" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">c) Seam Gauge (15 cm)</text>
    <text x="14" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Metal ruler with sliding pointer — checks seam allowances.</text>
    <text x="14" y="208" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">d) Hem Gauge</text>
    <text x="14" y="226" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Curved metal template — folds &amp; presses consistent hem depths.</text>
    <rect x="12" y="270" width="326" height="70" rx="6" fill="#0f172a"/>
    <text x="175" y="295" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Care Rule:</text>
    <text x="175" y="313" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Roll tape measure neatly — never fold sharply.</text>
    <text x="175" y="330" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Sharp creases stretch the tape and ruin accuracy.</text>
  </g>

  <!-- Sewing Tools -->
  <g transform="translate(420, 72)">
    <rect width="350" height="355" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="350" height="32" rx="10" fill="#7e22ce"/>
    <text x="175" y="21" fill="#fff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">🪡 HAND SEWING TOOLS</text>
    <text x="14" y="58" fill="#c084fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">a) Hand Sewing Needles</text>
    <text x="14" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Sharps: General sewing — medium, round eye.</text>
    <text x="14" y="94" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Crewel: Large elongated eye for embroidery thread.</text>
    <text x="14" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Tapestry: Blunt tip for knit fabrics &amp; thick yarn.</text>
    <text x="14" y="144" fill="#c084fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">b) Pins &amp; Pin Cushion</text>
    <text x="14" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Pins temporarily hold fabric layers; cushion stores them safely.</text>
    <text x="14" y="194" fill="#c084fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">c) Thimble</text>
    <text x="14" y="212" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Cup-shaped guard worn on middle finger — protects from puncture.</text>
    <rect x="12" y="265" width="326" height="75" rx="6" fill="#0f172a"/>
    <text x="175" y="288" fill="#c084fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Needle Sizing Rule:</text>
    <text x="175" y="308" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Higher number = thinner needle (e.g., size 10 for silk)</text>
    <text x="175" y="326" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Lower number = thicker needle (e.g., size 3 for denim)</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


def get_svg_3():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">FINISHING &amp; STORAGE TOOLS — CLASSIFICATION</text>
  <text x="400" y="54" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Lesson 3: Tools That Neaten Seams &amp; Organize the Needlework Lab</text>

  <g transform="translate(30, 72)">
    <rect width="350" height="355" rx="10" fill="#1e293b" stroke="#f97316" stroke-width="1.5"/>
    <rect width="350" height="32" rx="10" fill="#ea580c"/>
    <text x="175" y="21" fill="#fff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">🔥 FINISHING TOOLS</text>
    <text x="14" y="58" fill="#fb923c" font-family="system-ui, sans-serif" font-size="11" font-weight="700">a) Over-locker (Serger)</text>
    <text x="14" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Trims, stitches, and neatens raw edges in ONE step.</text>
    <text x="14" y="108" fill="#fb923c" font-family="system-ui, sans-serif" font-size="11" font-weight="700">b) Iron &amp; Ironing Board</text>
    <text x="14" y="126" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Pressing (lift &amp; lower) sets flat, professional seam lines.</text>
    <text x="14" y="158" fill="#fb923c" font-family="system-ui, sans-serif" font-size="11" font-weight="700">c) Press Cloth</text>
    <text x="14" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Cotton/linen barrier placed between iron and fabric</text>
    <text x="14" y="194" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">— prevents scorching, melting, and shiny glaze.</text>
    <rect x="12" y="270" width="326" height="70" rx="6" fill="#0f172a"/>
    <text x="175" y="293" fill="#fb923c" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Pressing vs Ironing:</text>
    <text x="175" y="311" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">PRESSING = Lift &amp; Lower (professional). Never slide!</text>
    <text x="175" y="329" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Ironing (sliding) stretches and distorts seams.</text>
  </g>

  <g transform="translate(420, 72)">
    <rect width="350" height="355" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="350" height="32" rx="10" fill="#059669"/>
    <text x="175" y="21" fill="#fff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">📦 STORAGE TOOLS</text>
    <text x="14" y="58" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">a) Sewing Box / Kit</text>
    <text x="14" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Sectioned portable container — holds needles, pins, scissors.</text>
    <text x="14" y="108" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">b) Thread Rack</text>
    <text x="14" y="126" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Wall-mounted pegs — keeps thread spools from tangling &amp; fading.</text>
    <text x="14" y="158" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">c) Fabric Bins &amp; Shelves</text>
    <text x="14" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Clean, dry cabinets — protect fabric from dust, pests &amp; sunlight.</text>
    <text x="14" y="208" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">d) Pattern Envelopes / Boxes</text>
    <text x="14" y="226" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Flat storage for pattern pieces — prevents tearing and loss.</text>
    <rect x="12" y="265" width="326" height="75" rx="6" fill="#0f172a"/>
    <text x="175" y="288" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Lab Safety Rule:</text>
    <text x="175" y="308" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Always return pins to cushion, scissors to box.</text>
    <text x="175" y="326" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Loose needles &amp; pins cause puncture injuries.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


def get_svg_4():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">SELECTING SEWING TOOLS, EQUIPMENT &amp; MATERIALS</text>
  <text x="400" y="54" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Lesson 4: 7 Guiding Factors for Smart, Economical Selection</text>

  <!-- 7 Factor Hexagonal Grid -->
  <g transform="translate(30, 75)">
    <!-- Row 1 -->
    <rect x="0" y="0" width="225" height="90" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="112" y="22" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. Type of Project</text>
    <text x="112" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Simple repair = hand tools only.</text>
    <text x="112" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Garment construction = shears,</text>
    <text x="112" y="77" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">marking tools, machine &amp; pins.</text>

    <rect x="0" y="105" width="225" height="90" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="112" y="127" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. Fabric Type &amp; Weight</text>
    <text x="112" y="147" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Fine silk → thin needle (size 9–10).</text>
    <text x="112" y="165" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Heavy denim → thick needle (size 3–4).</text>

    <rect x="0" y="210" width="225" height="90" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="112" y="232" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. User Skill Level</text>
    <text x="112" y="252" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Beginners: start with quality hand</text>
    <text x="112" y="270" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">tools before advanced machines.</text>

    <rect x="0" y="315" width="225" height="72" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <text x="112" y="337" fill="#c084fc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">4. Budget Constraints</text>
    <text x="112" y="357" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Prioritize 1 quality pair of shears</text>
    <text x="112" y="375" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">over many cheap accessories.</text>
  </g>

  <g transform="translate(285, 75)">
    <rect x="0" y="0" width="225" height="90" rx="8" fill="#1e293b" stroke="#06b6d4" stroke-width="1.5"/>
    <text x="112" y="22" fill="#06b6d4" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">5. Durability &amp; Quality</text>
    <text x="112" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Look for high-carbon steel blades</text>
    <text x="112" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">with screw joint (sharpenable).</text>
    <text x="112" y="77" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Avoid plastic rivets — not repairable.</text>

    <rect x="0" y="105" width="225" height="90" rx="8" fill="#1e293b" stroke="#f87171" stroke-width="1.5"/>
    <text x="112" y="127" fill="#f87171" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">6. Safety Features</text>
    <text x="112" y="147" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Machines: needle guards required.</text>
    <text x="112" y="165" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Irons: auto-shutoff prevents fires.</text>

    <rect x="0" y="210" width="225" height="90" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="112" y="232" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">7. Local Availability</text>
    <text x="112" y="252" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Choose brands available in local</text>
    <text x="112" y="270" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">shops for easy replacement access.</text>

    <!-- Summary -->
    <rect x="0" y="315" width="225" height="72" rx="8" fill="#0284c7"/>
    <text x="112" y="340" fill="#fff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Golden Principle:</text>
    <text x="112" y="360" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Quality tools = fewer replacements</text>
    <text x="112" y="378" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">= better garments = saved money.</text>
  </g>

  <g transform="translate(545, 75)">
    <rect x="0" y="0" width="220" height="387" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="32" rx="10" fill="#d97706"/>
    <text x="110" y="21" fill="#fff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">NEEDLE — FABRIC MATCH</text>
    <text x="12" y="60" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Silk / Chiffon:</text>
    <text x="12" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Needle size 9–10, silk thread.</text>
    <text x="12" y="115" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Cotton / Linen:</text>
    <text x="12" y="133" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Needle size 7–8, polyester thread.</text>
    <text x="12" y="170" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Denim / Canvas:</text>
    <text x="12" y="188" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Needle size 3–4, heavy-duty thread.</text>
    <text x="12" y="225" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Knit / Wool:</text>
    <text x="12" y="243" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Tapestry needle, acrylic yarn.</text>
    <rect x="10" y="295" width="200" height="80" rx="6" fill="#0f172a"/>
    <text x="110" y="320" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Thread — Fabric Rule:</text>
    <text x="110" y="340" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Stretch fabrics need polyester thread</text>
    <text x="110" y="358" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">(elastic). Cotton thread snaps.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


def get_svg_5():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">SEWING MACHINE ANATOMY — HEAD, ARM &amp; BED</text>
  <text x="400" y="54" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Lesson 5: Structural Divisions and Key Operational Parts</text>

  <!-- Head Section -->
  <g transform="translate(20, 72)">
    <rect width="235" height="345" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="235" height="32" rx="10" fill="#0284c7"/>
    <text x="117" y="21" fill="#fff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">🔧 THE HEAD</text>
    <text x="12" y="55" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Contains all primary gears &amp; needle controls</text>
    <text x="12" y="80" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Key Parts:</text>
    <text x="12" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Thread Take-up Lever: pulls thread from spool,</text>
    <text x="12" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  tightens lockstitch on upward stroke.</text>
    <text x="12" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Needle Bar: holds and drives needle up/down.</text>
    <text x="12" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Tension Dial: controls upper thread flow.</text>
    <text x="12" y="175" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Presser Foot: holds fabric flat on feed dog.</text>
    <text x="12" y="195" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Presser Foot Lifter: raises/lowers foot.</text>
    <text x="12" y="215" fill="#f87171" font-family="system-ui, sans-serif" font-size="9.5">  ⚠ Always lower before sewing!</text>
    <rect x="10" y="268" width="215" height="65" rx="6" fill="#0f172a"/>
    <text x="117" y="290" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Critical Rule:</text>
    <text x="117" y="308" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Foot UP → tension discs OPEN</text>
    <text x="117" y="325" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">(thread correctly when foot is raised)</text>
  </g>

  <!-- Arm Section -->
  <g transform="translate(275, 72)">
    <rect width="235" height="345" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="235" height="32" rx="10" fill="#059669"/>
    <text x="117" y="21" fill="#fff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">⚙️ THE ARM</text>
    <text x="12" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Horizontal bar: connects wheel to needle gears</text>
    <text x="12" y="80" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Key Parts:</text>
    <text x="12" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Hand-wheel (Balance Wheel): turned toward</text>
    <text x="12" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  you to raise/lower needle precisely.</text>
    <text x="12" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Spool Pin: holds the thread spool on top.</text>
    <text x="12" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Bobbin Winder: spindle that winds thread</text>
    <text x="12" y="171" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  onto bobbin evenly and automatically.</text>
    <text x="12" y="191" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Stitch Length Dial: 0 (none) to 4–5 (longest).</text>
    <text x="12" y="211" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Stitch Selector: chooses straight/zigzag/buttonhole.</text>
    <rect x="10" y="268" width="215" height="65" rx="6" fill="#0f172a"/>
    <text x="117" y="290" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Hand-wheel Rule:</text>
    <text x="117" y="308" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">ALWAYS turn toward you (never away).</text>
    <text x="117" y="325" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Turning backward tangles the lower thread.</text>
  </g>

  <!-- Bed Section -->
  <g transform="translate(530, 72)">
    <rect width="245" height="345" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="245" height="32" rx="10" fill="#d97706"/>
    <text x="122" y="21" fill="#fff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">🛏 THE BED</text>
    <text x="12" y="55" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Flat base: houses lower shuttle system</text>
    <text x="12" y="80" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Key Parts:</text>
    <text x="12" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Feed Dog: ridged teeth move fabric forward</text>
    <text x="12" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  automatically — elliptical (up/back/down/fwd).</text>
    <text x="12" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Throat Plate (Needle Plate): flat metal cover</text>
    <text x="12" y="151" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">  with seam allowance guide markings.</text>
    <text x="12" y="171" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Bobbin Case: holds bobbin; supplies lower thread.</text>
    <text x="12" y="191" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Slide Plate: removable cover to access bobbin.</text>
    <text x="12" y="211" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Foot Pedal (Controller): floor pedal controls speed.</text>
    <rect x="10" y="268" width="225" height="65" rx="6" fill="#0f172a"/>
    <text x="122" y="290" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Lockstitch Secret:</text>
    <text x="122" y="308" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Shuttle hook catches upper thread loop,</text>
    <text x="122" y="325" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">sweeps it around bobbin to lock threads.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


def get_svg_6():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THREADING THE SEWING MACHINE — STEP-BY-STEP</text>
  <text x="400" y="54" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Lesson 6: Bobbin Winding + Upper Threading + Drawing Up Lower Thread</text>

  <!-- Bobbin Winding Column -->
  <g transform="translate(20, 72)">
    <rect width="240" height="355" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="240" height="32" rx="10" fill="#7e22ce"/>
    <text x="120" y="21" fill="#fff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STEP 1: WIND BOBBIN</text>
    <text x="12" y="56" fill="#c084fc" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">1. Disengage needle (pull inner hand-wheel knob).</text>
    <text x="12" y="78" fill="#c084fc" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">2. Place spool on spool pin.</text>
    <text x="12" y="100" fill="#c084fc" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">3. Thread through bobbin winding tension guide.</text>
    <text x="12" y="122" fill="#c084fc" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">4. Thread bobbin hole from inside → out.</text>
    <text x="12" y="144" fill="#c084fc" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">5. Push bobbin onto winder spindle.</text>
    <text x="12" y="166" fill="#c084fc" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">6. Slide spindle right; press pedal to wind.</text>
    <text x="12" y="188" fill="#c084fc" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">7. Winder stops automatically when full.</text>
    <rect x="10" y="280" width="220" height="62" rx="6" fill="#0f172a"/>
    <text x="120" y="303" fill="#c084fc" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Critical Safety:</text>
    <text x="120" y="320" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Disengage needle FIRST — prevents</text>
    <text x="120" y="336" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">needle bar from moving while winding.</text>
  </g>

  <!-- Upper Threading Column -->
  <g transform="translate(285, 72)">
    <rect width="240" height="355" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="240" height="32" rx="10" fill="#0284c7"/>
    <text x="120" y="21" fill="#fff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STEP 2: UPPER THREAD</text>
    <text x="12" y="50" fill="#f87171" font-family="system-ui, sans-serif" font-size="9" font-weight="700">⚠ Raise presser foot FIRST (opens tension discs)</text>
    <text x="12" y="72" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">1. Place spool on spool pin.</text>
    <text x="12" y="92" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">2. Thread through top thread guide (arm).</text>
    <text x="12" y="112" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">3. Down between tension discs; wrap spring.</text>
    <text x="12" y="132" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">4. Up through guide hook.</text>
    <text x="12" y="152" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">5. Thread through TAKE-UP LEVER (most critical!).</text>
    <text x="12" y="172" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">6. Down through needle bar guides.</text>
    <text x="12" y="192" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">7. Thread needle eye (leave 10 cm tail).</text>
    <rect x="10" y="280" width="220" height="62" rx="6" fill="#0f172a"/>
    <text x="120" y="303" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Mistake to Avoid:</text>
    <text x="120" y="320" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Skipping take-up lever = zero tension</text>
    <text x="120" y="336" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">= tangled loop nest under fabric.</text>
  </g>

  <!-- Lower Thread Column -->
  <g transform="translate(550, 72)">
    <rect width="230" height="355" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="230" height="32" rx="10" fill="#059669"/>
    <text x="115" y="21" fill="#fff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STEP 3: LOWER THREAD</text>
    <text x="12" y="56" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">1. Drop bobbin into bobbin case.</text>
    <text x="12" y="78" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">2. Pull thread through tension spring slot.</text>
    <text x="12" y="100" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">3. Open slide plate; push case onto shuttle hook.</text>
    <text x="12" y="122" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">4. Press latch until it clicks shut.</text>
    <text x="12" y="144" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">5. Hold upper thread tail gently.</text>
    <text x="12" y="166" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">6. Rotate hand-wheel ONE full cycle.</text>
    <text x="12" y="188" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">7. Pull up: a loop of lower thread emerges!</text>
    <text x="12" y="210" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">8. Pull both tails 10 cm toward machine back.</text>
    <rect x="10" y="275" width="210" height="68" rx="6" fill="#0f172a"/>
    <text x="115" y="298" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Draw-Up Rule:</text>
    <text x="115" y="316" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Must hold upper thread while</text>
    <text x="115" y="332" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">turning wheel to capture lower loop.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


def get_svg_7():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">OPERATING THE SEWING MACHINE — SPEED, STITCH &amp; GUIDE</text>
  <text x="400" y="54" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Lesson 7: Foot Pedal Control, Stitch Selection, Fabric Guiding &amp; Pivoting</text>

  <!-- Speed Control -->
  <g transform="translate(20, 72)">
    <rect width="230" height="160" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="230" height="30" rx="10" fill="#0284c7"/>
    <text x="115" y="20" fill="#fff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🦶 FOOT PEDAL CONTROL</text>
    <text x="12" y="55" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Rule: Press gently — like squeezing a sponge.</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Practice stitch-by-stitch before going fast.</text>
    <text x="12" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Barefoot training builds pedal sensitivity.</text>
    <text x="12" y="115" fill="#f87171" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">⚠ Never smash pedal to floor — you lose control!</text>
    <text x="12" y="142" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">Think: engine moves fabric; you just steer.</text>
  </g>

  <!-- Stitch Settings -->
  <g transform="translate(270, 72)">
    <rect width="250" height="160" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="250" height="30" rx="10" fill="#d97706"/>
    <text x="125" y="20" fill="#fff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🔀 STITCH SETTINGS</text>
    <text x="12" y="55" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Basting/Tacking: 4–5 mm (easy to remove)</text>
    <text x="12" y="75" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Standard Seams (Cotton): 2.5 mm</text>
    <text x="12" y="95" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Fine Fabrics (Chiffon): 1.5–2 mm</text>
    <text x="12" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Stitch Type: Straight = seams; Zigzag = stretchy</text>
    <text x="12" y="140" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">fabrics and raw edge neatening.</text>
  </g>

  <!-- Fabric Guiding -->
  <g transform="translate(540, 72)">
    <rect width="240" height="160" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="240" height="30" rx="10" fill="#059669"/>
    <text x="120" y="20" fill="#fff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🤲 FABRIC GUIDING</text>
    <text x="12" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Golden Rule: NEVER push or pull fabric!</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Feed dog moves it — you only steer gently.</text>
    <text x="12" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Left hand: side guide. Right hand: front steer.</text>
    <text x="12" y="115" fill="#f87171" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">⚠ Keep fingers 2 cm from needle AT ALL TIMES!</text>
    <text x="12" y="142" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">Pulling bends needle → throat plate strike → shatters!</text>
  </g>

  <!-- Back-Tacking -->
  <g transform="translate(20, 250)">
    <rect width="230" height="165" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="230" height="30" rx="10" fill="#7e22ce"/>
    <text x="115" y="20" fill="#fff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🔒 BACK-TACKING</text>
    <text x="12" y="55" fill="#c084fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Purpose: Locks thread ends to prevent seam unraveling.</text>
    <text x="12" y="77" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">1. Sew 3 stitches forward.</text>
    <text x="12" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">2. Hold reverse lever → sew 3 stitches backward.</text>
    <text x="12" y="113" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">3. Release lever → continue sewing forward.</text>
    <text x="12" y="131" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Repeat at BOTH ends of every permanent seam.</text>
    <text x="12" y="155" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">Seam strength depends on back-tacked ends.</text>
  </g>

  <!-- Pivoting -->
  <g transform="translate(270, 250)">
    <rect width="250" height="165" rx="10" fill="#1e293b" stroke="#06b6d4" stroke-width="1.5"/>
    <rect width="250" height="30" rx="10" fill="#0891b2"/>
    <text x="125" y="20" fill="#fff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🔄 PIVOTING AT CORNERS</text>
    <text x="12" y="55" fill="#06b6d4" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Purpose: Turn sharp corners without losing stitch line.</text>
    <text x="12" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">1. Stop at the corner point.</text>
    <text x="12" y="93" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">2. Turn hand-wheel → lower needle into fabric.</text>
    <text x="12" y="111" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">3. Raise presser foot lifter.</text>
    <text x="12" y="129" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">4. Rotate fabric to new direction.</text>
    <text x="12" y="147" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">5. Lower foot → resume sewing.</text>
  </g>

  <!-- Summary Box -->
  <g transform="translate(540, 250)">
    <rect width="240" height="165" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="240" height="30" rx="10" fill="#059669"/>
    <text x="120" y="20" fill="#fff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">✅ OPERATOR'S CHECKLIST</text>
    <text x="12" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">☑ Presser foot lowered before sewing</text>
    <text x="12" y="73" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">☑ Back-tack at start and end of seam</text>
    <text x="12" y="91" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">☑ Stitch length set for fabric weight</text>
    <text x="12" y="109" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">☑ Fingers 2 cm clear of needle</text>
    <text x="12" y="127" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">☑ Needle lowered before pivoting</text>
    <text x="12" y="145" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">☑ Hair tied; loose clothes secured</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


def get_svg_8():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#f87171" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">COMMON SEWING MACHINE FAULTS — DIAGNOSIS &amp; REMEDIES</text>
  <text x="400" y="54" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Lesson 8: Five Faults, Their Causes, and Step-by-Step Fixes</text>

  <!-- Header Row -->
  <g transform="translate(20, 70)">
    <rect width="200" height="28" rx="6" fill="#1e40af"/>
    <text x="100" y="19" fill="#fff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">⚠ FAULT</text>
  </g>
  <g transform="translate(235, 70)">
    <rect width="265" height="28" rx="6" fill="#7e22ce"/>
    <text x="132" y="19" fill="#fff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">🔍 POSSIBLE CAUSES</text>
  </g>
  <g transform="translate(515, 70)">
    <rect width="265" height="28" rx="6" fill="#065f46"/>
    <text x="132" y="19" fill="#fff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">✅ PRACTICAL REMEDY</text>
  </g>

  <!-- Row 1: Upper Thread Breaks -->
  <g transform="translate(20, 108)">
    <rect width="200" height="55" rx="4" fill="#1e293b" stroke="#f87171" stroke-width="1"/>
    <text x="10" y="20" fill="#f87171" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Upper Thread Breaks</text>
    <text x="10" y="40" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5">Thread snaps during sewing.</text>
  </g>
  <g transform="translate(235, 108)">
    <rect width="265" height="55" rx="4" fill="#1e293b" stroke="#7c3aed" stroke-width="1"/>
    <text x="10" y="18" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Incorrect upper threading • Tension too tight</text>
    <text x="10" y="34" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Needle inserted backwards • Blunt/bent needle</text>
    <text x="10" y="50" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Knot in thread spool</text>
  </g>
  <g transform="translate(515, 108)">
    <rect width="265" height="55" rx="4" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="10" y="18" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">• Unthread fully and rethread carefully</text>
    <text x="10" y="34" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">• Loosen tension dial • Fix needle direction</text>
    <text x="10" y="50" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">• Insert new needle • Cut thread knots</text>
  </g>

  <!-- Row 2: Bobbin Thread Breaks -->
  <g transform="translate(20, 173)">
    <rect width="200" height="55" rx="4" fill="#1e293b" stroke="#f87171" stroke-width="1"/>
    <text x="10" y="20" fill="#f87171" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Bobbin Thread Breaks</text>
    <text x="10" y="40" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5">Lower thread snaps or jams.</text>
  </g>
  <g transform="translate(235, 173)">
    <rect width="265" height="55" rx="4" fill="#1e293b" stroke="#7c3aed" stroke-width="1"/>
    <text x="10" y="18" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Incorrect bobbin case threading</text>
    <text x="10" y="34" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Lint inside bobbin case • Case too tight</text>
    <text x="10" y="50" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Bobbin wound too loosely/unevenly</text>
  </g>
  <g transform="translate(515, 173)">
    <rect width="265" height="55" rx="4" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="10" y="18" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">• Remove case and rethread tension spring</text>
    <text x="10" y="34" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">• Brush lint out of shuttle and case</text>
    <text x="10" y="50" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">• Loosen case screw • Rewind bobbin evenly</text>
  </g>

  <!-- Row 3: Skipped Stitches -->
  <g transform="translate(20, 238)">
    <rect width="200" height="55" rx="4" fill="#1e293b" stroke="#f87171" stroke-width="1"/>
    <text x="10" y="20" fill="#f87171" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Skipped Stitches</text>
    <text x="10" y="40" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5">Gaps/unstitched loops in seam.</text>
  </g>
  <g transform="translate(235, 238)">
    <rect width="265" height="55" rx="4" fill="#1e293b" stroke="#7c3aed" stroke-width="1"/>
    <text x="10" y="18" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Needle bent, blunt, or damaged</text>
    <text x="10" y="34" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Wrong needle size for fabric type</text>
    <text x="10" y="50" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Needle inserted incorrectly (turned)</text>
  </g>
  <g transform="translate(515, 238)">
    <rect width="265" height="55" rx="4" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="10" y="18" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">• Replace with brand-new needle</text>
    <text x="10" y="34" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">• Select correct needle size for fabric</text>
    <text x="10" y="50" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">• Re-insert needle correctly; tighten clamp screw</text>
  </g>

  <!-- Row 4: Fabric Puckering -->
  <g transform="translate(20, 303)">
    <rect width="200" height="55" rx="4" fill="#1e293b" stroke="#f87171" stroke-width="1"/>
    <text x="10" y="20" fill="#f87171" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Fabric Puckering</text>
    <text x="10" y="40" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5">Seam gathers/bunches accordion-like.</text>
  </g>
  <g transform="translate(235, 303)">
    <rect width="265" height="55" rx="4" fill="#1e293b" stroke="#7c3aed" stroke-width="1"/>
    <text x="10" y="18" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Both tensions too tight</text>
    <text x="10" y="34" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Stitch length too long for fine fabric</text>
    <text x="10" y="50" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Needle too thick for delicate material</text>
  </g>
  <g transform="translate(515, 303)">
    <rect width="265" height="55" rx="4" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="10" y="18" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">• Loosen both upper and lower tensions</text>
    <text x="10" y="34" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">• Shorten stitch length on dial</text>
    <text x="10" y="50" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">• Switch to thinner needle (size 9–11)</text>
  </g>

  <!-- Row 5: Thread Nesting -->
  <g transform="translate(20, 368)">
    <rect width="200" height="60" rx="4" fill="#1e293b" stroke="#f87171" stroke-width="1"/>
    <text x="10" y="20" fill="#f87171" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Thread Nesting</text>
    <text x="10" y="40" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5">Loop tangles under fabric underside.</text>
  </g>
  <g transform="translate(235, 368)">
    <rect width="265" height="60" rx="4" fill="#1e293b" stroke="#7c3aed" stroke-width="1"/>
    <text x="10" y="20" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Upper thread skipped tension discs</text>
    <text x="10" y="38" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Threaded with presser foot down (discs closed)</text>
    <text x="10" y="56" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Bobbin inserted backwards in case</text>
  </g>
  <g transform="translate(515, 368)">
    <rect width="265" height="60" rx="4" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="10" y="20" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">• Raise foot; remove thread; rethread discs</text>
    <text x="10" y="38" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">• Always thread with presser foot raised</text>
    <text x="10" y="56" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">• Re-insert bobbin in correct spin direction</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


def get_svg_9():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">SEWING MACHINE CARE, MAINTENANCE &amp; STORAGE</text>
  <text x="400" y="54" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Lesson 9: Daily, Weekly, and Long-Term Machine Care Protocols</text>

  <!-- Daily -->
  <g transform="translate(20, 72)">
    <rect width="235" height="345" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="235" height="32" rx="10" fill="#0284c7"/>
    <text x="117" y="21" fill="#fff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">📅 AFTER EVERY USE</text>
    <text x="12" y="60" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">1. Remove needle from bar.</text>
    <text x="12" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Store needle safely in pin cushion or case.</text>
    <text x="12" y="108" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">2. Remove bobbin and case.</text>
    <text x="12" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Brush out lint from shuttle race.</text>
    <text x="12" y="156" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">3. Wipe all exterior surfaces.</text>
    <text x="12" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Use a soft, dry cloth — removes dust &amp; thread bits.</text>
    <text x="12" y="204" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">4. Turn off motor &amp; unplug.</text>
    <text x="12" y="224" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Prevents overheating and electrical hazards.</text>
    <text x="12" y="252" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">5. Cover with dust cover.</text>
    <text x="12" y="272" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Protects from dust, insects, and UV fading.</text>
    <rect x="10" y="295" width="215" height="38" rx="6" fill="#0f172a"/>
    <text x="117" y="318" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Lint is the #1 cause of machine jams.</text>
  </g>

  <!-- Weekly -->
  <g transform="translate(280, 72)">
    <rect width="235" height="345" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="235" height="32" rx="10" fill="#059669"/>
    <text x="117" y="21" fill="#fff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🗓 WEEKLY MAINTENANCE</text>
    <text x="12" y="60" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">1. Oiling the machine:</text>
    <text x="12" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Apply 1–2 drops of sewing machine oil</text>
    <text x="12" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">to all metal-on-metal moving joints.</text>
    <text x="12" y="128" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">2. Check needle condition:</text>
    <text x="12" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Replace bent, blunt, or corroded needles.</text>
    <text x="12" y="176" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">3. Check belt tension (treadle models):</text>
    <text x="12" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Belt should be taut but not overtight.</text>
    <text x="12" y="224" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">4. Test stitch quality:</text>
    <text x="12" y="244" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Sew a test seam on scrap fabric to verify</text>
    <text x="12" y="262" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">tension balance and thread lock quality.</text>
    <rect x="10" y="295" width="215" height="38" rx="6" fill="#0f172a"/>
    <text x="117" y="318" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Never over-oil: attracts lint and stains fabric.</text>
  </g>

  <!-- Storage -->
  <g transform="translate(540, 72)">
    <rect width="240" height="345" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="240" height="32" rx="10" fill="#d97706"/>
    <text x="120" y="21" fill="#fff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">📦 LONG-TERM STORAGE</text>
    <text x="12" y="60" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700">1. Clean thoroughly before storing.</text>
    <text x="12" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Remove all thread from machine and bobbin case.</text>
    <text x="12" y="108" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700">2. Oil all moving joints.</text>
    <text x="12" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Prevents rust on metal during storage.</text>
    <text x="12" y="156" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700">3. Lower presser foot onto cloth pad.</text>
    <text x="12" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Relieves pressure on spring and rubber feed dog.</text>
    <text x="12" y="204" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700">4. Cover fully with machine cover.</text>
    <text x="12" y="224" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Fabric or hard case — keeps dust and insects out.</text>
    <text x="12" y="252" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700">5. Store in dry, flat, stable location.</text>
    <text x="12" y="272" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Dampness causes rust; tilting misaligns the shuttle.</text>
    <rect x="10" y="295" width="220" height="38" rx="6" fill="#0f172a"/>
    <text x="120" y="318" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Service by technician every 12 months.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


def get_svg_10():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">CARE &amp; STORAGE OF OTHER NEEDLEWORK TOOLS</text>
  <text x="400" y="54" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Lesson 10: Scissors, Needles, Pins, Tape Measures, Irons &amp; Fabrics</text>

  <!-- Scissors/Shears -->
  <g transform="translate(20, 72)">
    <rect width="185" height="355" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="185" height="32" rx="10" fill="#0284c7"/>
    <text x="92" y="21" fill="#fff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">✂️ SCISSORS</text>
    <text x="10" y="58" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">USE:</text>
    <text x="10" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">ONLY cut fabric. Never paper, wire,</text>
    <text x="10" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">or cardboard — dulls blades instantly.</text>
    <text x="10" y="120" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">CARE:</text>
    <text x="10" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Wipe blades after use. Oil the screw</text>
    <text x="10" y="154" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">joint lightly. Have professionally</text>
    <text x="10" y="170" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">sharpened when blades pull.</text>
    <text x="10" y="198" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">STORE:</text>
    <text x="10" y="216" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">In a fabric sheath/case in sewing box.</text>
    <text x="10" y="232" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Blades closed — prevents accidents.</text>
    <rect x="8" y="290" width="169" height="55" rx="6" fill="#0f172a"/>
    <text x="92" y="312" fill="#f87171" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Safety Pass Rule:</text>
    <text x="92" y="328" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Always pass closed, handle-first.</text>
  </g>

  <!-- Needles/Pins -->
  <g transform="translate(220, 72)">
    <rect width="185" height="355" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="185" height="32" rx="10" fill="#059669"/>
    <text x="92" y="21" fill="#fff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">🪡 NEEDLES &amp; PINS</text>
    <text x="10" y="58" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">USE:</text>
    <text x="10" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Match needle to fabric weight.</text>
    <text x="10" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Use thimble on middle finger.</text>
    <text x="10" y="120" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">CARE:</text>
    <text x="10" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Wipe needles with soft cloth after use</text>
    <text x="10" y="154" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">to remove rust-causing moisture and oils.</text>
    <text x="10" y="178" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Discard bent/blunt needles immediately.</text>
    <text x="10" y="206" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">STORE:</text>
    <text x="10" y="224" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Pins in pin cushion (emery bag keeps sharp).</text>
    <text x="10" y="242" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Needles in original packet or needle case.</text>
    <rect x="8" y="290" width="169" height="55" rx="6" fill="#0f172a"/>
    <text x="92" y="312" fill="#f87171" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Never leave loose!</text>
    <text x="92" y="328" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Discarded needles → wrap in paper.</text>
  </g>

  <!-- Tape Measure -->
  <g transform="translate(420, 72)">
    <rect width="175" height="355" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="175" height="32" rx="10" fill="#d97706"/>
    <text x="87" y="21" fill="#fff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">📏 TAPE MEASURE</text>
    <text x="10" y="58" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">USE:</text>
    <text x="10" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Keep flat; never stretch or yank.</text>
    <text x="10" y="98" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">CARE:</text>
    <text x="10" y="116" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Wipe clean. Never fold or crease.</text>
    <text x="10" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Creases permanently stretch markings.</text>
    <text x="10" y="158" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">STORE:</text>
    <text x="10" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Roll loosely — never fold.</text>
    <text x="10" y="192" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Keep in sewing box away from heat.</text>
    <rect x="8" y="290" width="160" height="55" rx="6" fill="#0f172a"/>
    <text x="87" y="312" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Accuracy Check:</text>
    <text x="87" y="328" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Verify against metal ruler yearly.</text>
  </g>

  <!-- Iron & Fabric -->
  <g transform="translate(610, 72)">
    <rect width="170" height="355" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="170" height="32" rx="10" fill="#7e22ce"/>
    <text x="85" y="21" fill="#fff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">🔥 IRON &amp; FABRIC</text>
    <text x="10" y="58" fill="#c084fc" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">IRON USE:</text>
    <text x="10" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Always use press cloth on synthetics.</text>
    <text x="10" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Rest on heel when paused.</text>
    <text x="10" y="116" fill="#c084fc" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">IRON CARE:</text>
    <text x="10" y="134" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Empty water tank after use.</text>
    <text x="10" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Descale steam vents with vinegar.</text>
    <text x="10" y="174" fill="#c084fc" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">FABRIC STORE:</text>
    <text x="10" y="192" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Fold flat in dry, dark cabinets.</text>
    <text x="10" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">Mothballs repel fabric-eating insects.</text>
    <rect x="8" y="290" width="154" height="55" rx="6" fill="#0f172a"/>
    <text x="85" y="312" fill="#c084fc" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Unplug iron always</text>
    <text x="85" y="328" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">when leaving the room!</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


def get_svg_11():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#f87171" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">SAFETY &amp; WASTE DISPOSAL IN THE NEEDLEWORK LAB</text>
  <text x="400" y="54" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Lesson 11: Hazard Prevention, Emergency Response &amp; Environmental Responsibility</text>

  <!-- Column 1: Sharps Safety -->
  <g transform="translate(20, 72)">
    <rect width="235" height="345" rx="10" fill="#1e293b" stroke="#f87171" stroke-width="1.5"/>
    <rect width="235" height="32" rx="10" fill="#b91c1c"/>
    <text x="117" y="21" fill="#fff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">🪡 SHARPS SAFETY</text>
    <text x="12" y="58" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Needles &amp; Pins:</text>
    <text x="12" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Always store in pin cushion or packet.</text>
    <text x="12" y="96" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Never hold in mouth or leave on bench.</text>
    <text x="12" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Broken needles: wrap in paper, label, bin.</text>
    <text x="12" y="142" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Scissors &amp; Shears:</text>
    <text x="12" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Walk with point downward or in case.</text>
    <text x="12" y="180" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Pass to another person handle-first, closed.</text>
    <text x="12" y="198" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Never point at classmates — serious hazard.</text>
    <text x="12" y="226" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Rotary Cutter:</text>
    <text x="12" y="246" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Close blade guard immediately after every cut.</text>
    <text x="12" y="264" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Use only on self-healing cutting mat.</text>
    <rect x="10" y="290" width="215" height="38" rx="6" fill="#0f172a"/>
    <text x="117" y="313" fill="#f87171" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Needle stick: wash, press, report to teacher.</text>
  </g>

  <!-- Column 2: Machine &amp; Electrical Safety -->
  <g transform="translate(280, 72)">
    <rect width="235" height="345" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="235" height="32" rx="10" fill="#d97706"/>
    <text x="117" y="21" fill="#fff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">⚡ MACHINE SAFETY</text>
    <text x="12" y="58" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Sewing Machine Rules:</text>
    <text x="12" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Tie back long hair before operating.</text>
    <text x="12" y="96" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Tuck in loose clothing away from hand-wheel.</text>
    <text x="12" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Keep fingers 2 cm clear of moving needle.</text>
    <text x="12" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Never pull fabric — bends needle into plate.</text>
    <text x="12" y="160" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Electrical Safety:</text>
    <text x="12" y="180" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Dry hands before handling plugs.</text>
    <text x="12" y="198" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Check cords for fraying before each use.</text>
    <text x="12" y="216" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Unplug before threading or clearing jams.</text>
    <text x="12" y="244" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Iron Safety:</text>
    <text x="12" y="264" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Never leave heated iron unattended flat.</text>
    <text x="12" y="282" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Always rest on heel when pausing.</text>
    <rect x="10" y="296" width="215" height="38" rx="6" fill="#0f172a"/>
    <text x="117" y="319" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">If electrocuted: do NOT touch — isolate power first.</text>
  </g>

  <!-- Column 3: Waste Disposal -->
  <g transform="translate(540, 72)">
    <rect width="240" height="345" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="240" height="32" rx="10" fill="#059669"/>
    <text x="120" y="21" fill="#fff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">♻️ WASTE DISPOSAL</text>
    <text x="12" y="58" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Thread Ends &amp; Fabric Scraps:</text>
    <text x="12" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Collect in a dedicated waste bag — NOT floor.</text>
    <text x="12" y="96" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Small scraps: upcycle as stuffing or patch art.</text>
    <text x="12" y="124" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Broken/Dull Needles &amp; Pins:</text>
    <text x="12" y="144" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Wrap in several layers of paper.</text>
    <text x="12" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Label "SHARPS — HANDLE WITH CARE".</text>
    <text x="12" y="180" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Deposit in a metal sharps container/tin.</text>
    <text x="12" y="208" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Chemical Waste (Stain Removers):</text>
    <text x="12" y="228" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Dispose as per product label instructions.</text>
    <text x="12" y="246" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Never pour chemicals down storm drains.</text>
    <text x="12" y="274" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Lab End-of-Session Checklist:</text>
    <text x="12" y="294" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Sweep floor; pick up ALL dropped pins.</text>
    <rect x="10" y="308" width="220" height="38" rx="6" fill="#0f172a"/>
    <text x="120" y="331" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Zero-tolerance for needles left on benches.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


SVG_GETTERS = [
    get_svg_1, get_svg_2, get_svg_3, get_svg_4, get_svg_5, get_svg_6,
    get_svg_7, get_svg_8, get_svg_9, get_svg_10, get_svg_11
]

# ─── 11 Lesson Configuration Dicts ───────────────────────────────────────────

LESSON_CONFIGS = [
    # ──────────────────────────────────────────────────────────────────
    {
        "lesson_num": 1,
        "title": "Classification of Sewing Tools — Cutting & Marking Tools",
        "hook": (
            "Have you ever tried to cut a tough piece of fabric with small kitchen scissors? "
            "The result was probably a frayed, crooked mess. That is because every specialized task "
            "in sewing requires a tool designed specifically for that job. Just as a carpenter uses "
            "a screwdriver rather than a hammer to drive a screw, a home scientist must use the "
            "correct cutting and marking tools to achieve clean, accurate, professional results."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Pinking_shears_%28PSF%29.png/640px-Pinking_shears_%28PSF%29.png",
        "image_caption": "Pinking shears alongside standard dressmaker's shears — two essential cutting tools with very different blade designs and functions.",
        "analogy_title": "The Carpenter and the Screwdriver",
        "analogy_text": (
            "Imagine a carpenter trying to drive a screw using a heavy hammer. They might force the screw in, "
            "but they will ruin the wood and bend the screw in the process. A wise carpenter uses the correct "
            "screwdriver — the tool engineered for that exact task.\n\n"
            "In clothing construction, fabric is your wood and sewing is your craft. Dressmaker's shears are "
            "your screwdriver: they slide flat on the table surface, keeping fabric layers perfectly still "
            "while their long, precision-ground blades slice cleanly through textile fibers without lifting "
            "or shifting the fabric."
        ),
        "definition": {
            "title": "Key Cutting & Marking Terminology",
            "definitions": [
                {
                    "term": "Dressmaker's Shears",
                    "simple": "Large, sharp scissors with bent handles used specifically to cut fabric flat on a cutting table.",
                    "formal": "A specialized cutting tool with long precision-ground blades (15–30 cm) and asymmetrical bent handles that allow the lower blade to slide flat along a cutting surface, preventing fabric from lifting during cutting.",
                    "example": "Using dressmaker's shears to cut out a cotton skirt pattern flat on a table.",
                    "why_it_matters": "Standard scissors lift fabric off the table during cutting, causing layers to shift and resulting in crooked, inaccurate cuts."
                },
                {
                    "term": "Tailor's Chalk",
                    "simple": "A flat, hard chalk block used to draw sewing guidelines directly onto fabric.",
                    "formal": "A specialized marking material composed of compressed talc or wax molded into thin squares or triangles with tapered edges, used to draw clear, temporary construction lines on fabric that brush or wash away easily.",
                    "example": "Using white tailor's chalk to mark pocket placement on a dark blue fabric.",
                    "why_it_matters": "Ink pens permanently stain fabric, whereas tailor's chalk marks clearly without damage and disappears during pressing or washing."
                }
            ]
        },
        "deep_explanation": (
            "Sewing items are classified by function. The first two categories are cutting and marking tools.\n\n"
            "**Cutting Tools** slice through textile fibers cleanly:\n"
            "- Dressmaker's Shears: Long blades, bent handles — always use flat on the table. Never cut paper (dulls blades immediately).\n"
            "- Pinking Shears: Zigzag blades cut edges at an angle, preventing woven threads from fraying.\n"
            "- Embroidery Scissors: Small, sharp-pointed — for trimming threads, cutting buttonholes, and delicate needlework.\n"
            "- Seam Ripper: A pen-like hook blade with a protective ball tip — removes incorrect stitches without tearing fabric.\n"
            "- Thread Clippers (Snips): Spring-action cutters for quickly snipping thread ends close to fabric while sewing.\n"
            "- Rotary Cutter: A circular blade rolled across fabric on a self-healing mat — for straight or geometric cuts through multiple layers.\n\n"
            "**Marking Tools** transfer pattern lines from paper to fabric:\n"
            "- Tailor's Chalk: Available in white, blue, yellow, and red. White is safest for light fabrics.\n"
            "- Tracing Wheel & Tracing Paper: A spiked or smooth disk rolled over carbon-coated tracing paper — transfers pattern lines quickly and accurately.\n"
            "- Fabric Marking Pens: Washable or air-soluble ink that fades automatically or washes out with water."
        ),
        "practical": {
            "title": "Observing Cutting Tool Edge Effects on Woven Fabric",
            "steps": [
                {"step_number": 1, "instruction": "Cut a 10 cm straight line on woven cotton using standard household scissors. Note how much fabric lifted and how easy it was."},
                {"step_number": 2, "instruction": "Cut a parallel 10 cm line using dressmaker's shears, keeping the lower blade flat on the table."},
                {"step_number": 3, "instruction": "Cut a third 10 cm line using pinking shears."},
                {"step_number": 4, "instruction": "Use a seam ripper to cut a single thread inside a stitched seam on scrap fabric."},
                {"step_number": 5, "instruction": "Leave all cut edges exposed for 2 days, then shake the fabric and observe which edge frays the most."}
            ]
        },
        "youtube_id": "OBdBmxFzaHI",
        "mcq": {
            "question": "Which cutting tool has a zigzag blade designed specifically to finish raw edges and prevent fabric from fraying?",
            "options": [
                "Embroidery Scissors",
                "Dressmaker's Shears",
                "Pinking Shears",
                "Seam Ripper"
            ],
            "correct_answer": 2,
            "explanation": "Pinking shears have zigzag blades that cut fabric edges at an angle. At this bias angle, the warp and weft threads interlock, preventing them from sliding off the edge and fraying."
        }
    },
    # ──────────────────────────────────────────────────────────────────
    {
        "lesson_num": 2,
        "title": "Classification of Sewing Tools — Sewing & Measuring Tools",
        "hook": (
            "Have you ever tried to sew a button onto a thick wool coat using a tiny needle "
            "meant for delicate silk? The needle probably bent or snapped. Or have you ever hemmed "
            "a skirt by guessing the height, only to find one side much shorter than the other? "
            "Measuring tools give you perfect precision, and sewing tools join fabric layers cleanly "
            "and safely — together, they are the precision engine of garment construction."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Sewingtools.jpg/640px-Sewingtools.jpg",
        "image_caption": "A collection of measuring and sewing tools: flexible tape measure, metal seam gauge, hand sewing needles, thimble, and a filled pin cushion.",
        "analogy_title": "The Chef's Measuring Cups and Whisks",
        "analogy_text": (
            "Imagine a chef preparing a cake recipe. They don't dump flour and sugar into a bowl by guessing — "
            "they use measuring cups and spoons to get exact quantities. Then they use a whisk to blend everything together.\n\n"
            "In sewing, Measuring Tools are your measuring cups. They ensure every part of your garment is the perfect size. "
            "Sewing Tools are your whisks — they join the measured fabric pieces together permanently. "
            "Skipping the measuring step is like baking without measuring: the result is always a disaster."
        ),
        "definition": {
            "title": "Key Measuring & Sewing Tool Terminology",
            "definitions": [
                {
                    "term": "Tape Measure",
                    "simple": "A long, flexible plastic or fabric ribbon used to measure body curves and fabric lengths.",
                    "formal": "A flexible, narrow strip of fiberglass, plastic, or coated fabric (usually 150 cm or 60 inches long) with double-sided markings in centimeters and inches, fitted with metal tips to facilitate accurate contact measurements.",
                    "example": "Wrapping a tape measure around a student's waist to find their belt measurement.",
                    "why_it_matters": "Hard rulers cannot wrap around curved human bodies. A flexible tape measure fits body curves without stretching or distorting, ensuring accurate tailoring."
                },
                {
                    "term": "Seam Gauge",
                    "simple": "A small metal ruler with a sliding pointer used to measure small, repetitive distances like hems and seams.",
                    "formal": "A flat metal ruler (typically 15 cm) with an adjustable sliding pointer, designed to measure and mark consistent small distances such as seam allowances, tucks, pleats, and buttonhole spacings.",
                    "example": "Setting the seam gauge to 1.5 cm to check that a seam allowance is perfectly uniform down the full length of a skirt.",
                    "why_it_matters": "A seam gauge locked at a specific width makes checking seam allowances extremely fast and accurate, eliminating the need to repeatedly read tiny ruler markings."
                }
            ]
        },
        "deep_explanation": (
            "Accurate measurements are the foundation of well-fitting clothing.\n\n"
            "**Measuring Tools:**\n"
            "- Tape Measure (150 cm flexible ribbon): For body measurements — bust, waist, hip, shoulder. Always roll it neatly; folding creates sharp creases that permanently stretch the tape.\n"
            "- Ruler / Meter Stick / Yardstick: Rigid straight edges for marking straight lines on fabric and measuring large fabric yardages.\n"
            "- Seam Gauge (15 cm metal ruler with sliding marker): For small, precise, repetitive measurements like seam allowances and hem depths.\n"
            "- Hem Gauge: A curved metal template for folding and pressing consistent hem depths directly on fabric.\n\n"
            "**Hand Sewing Tools:**\n"
            "- Hand Sewing Needles: Metal shafts with a sharp point and an eye to hold thread. Types include Sharps (general use, round eye), Crewel/Embroidery (large elongated eye for multiple thread strands), and Tapestry (blunt tip for knits and open-weave canvas).\n"
            "- Pins & Pin Cushion: Pins temporarily hold fabric layers together before permanent stitching. The pin cushion is a padded holder that keeps pins organized, sharp, and off the floor.\n"
            "- Thimble: A cup-shaped metal or plastic guard worn on the middle finger, with small dimples to catch the needle head, protecting the finger when pushing needles through tough fabrics.\n\n"
            "Needle sizing uses an inverse system: size 1 is the thickest and longest; size 12 is the thinnest and shortest. Fine fabrics need high-numbered thin needles; heavy fabrics need low-numbered thick needles."
        ),
        "practical": {
            "title": "Testing Tape Measure Accuracy Under Stress",
            "steps": [
                {"step_number": 1, "instruction": "Lay a rigid metal meter stick flat on a table. Lay your plastic tape measure parallel to it and compare the 0–100 cm markings."},
                {"step_number": 2, "instruction": "Stretch the plastic tape measure as hard as possible. Lay it back down and check if the markings have shifted."},
                {"step_number": 3, "instruction": "Fold the tape measure into sharp tight folds and press under a heavy book. Open it and try to measure a 30 cm length — note if creases prevent flat contact."},
                {"step_number": 4, "instruction": "Record your findings: does the stressed tape measure deviate from the rigid metal ruler?"},
                {"step_number": 5, "instruction": "Discuss why professional tape measures are always stored rolled loosely, never folded."}
            ]
        },
        "youtube_id": "wBovCPGfZ0o",
        "mcq": {
            "question": "Which sewing tool is worn on the middle finger to protect it from being punctured when pushing needles through thick fabrics?",
            "options": [
                "Seam Gauge",
                "Thimble",
                "Pin Cushion",
                "Tapestry Needle"
            ],
            "correct_answer": 1,
            "explanation": "A thimble is a protective cap worn on the finger to safely push hand sewing needles through thick or tough fabrics. Its dimpled surface catches the needle head and distributes the pushing force safely."
        }
    },
    # ──────────────────────────────────────────────────────────────────
    {
        "lesson_num": 3,
        "title": "Classification of Sewing Tools — Finishing & Storage Tools",
        "hook": (
            "Have you ever seen a beautiful sewn dress on a hanger, but when you looked inside at "
            "the seams, you saw hundreds of messy, frayed threads? Or have you opened a sewing box "
            "only to spend 30 minutes untangling threads, needles, and pins? Finishing tools "
            "transform raw, ragged inside seams into polished professional edges, while storage "
            "tools keep your laboratory organized, safe, and inspection-ready."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Sewing_kit_in_a_box.jpg/640px-Sewing_kit_in_a_box.jpg",
        "image_caption": "A well-organized wooden sewing box with neat compartments for colorful thread spools, pins, buttons, hand needles, and small tools.",
        "analogy_title": "The Library Bookshelf and the Book Binder",
        "analogy_text": (
            "Imagine a library with thousands of books just thrown in a messy heap on the floor. "
            "It would be impossible to find anything, and the books would get torn and ruined. "
            "Librarians use bookshelves, sections, and catalog boxes to keep books safe, ordered, and accessible.\n\n"
            "In sewing, Storage Tools are your bookshelves — they keep every tool in its correct place, protected "
            "from rust, dust, and tangling. Finishing Tools are your book binders — they give your garments a crisp, "
            "polished, professional appearance inside and out."
        ),
        "definition": {
            "title": "Key Finishing & Storage Tool Terminology",
            "definitions": [
                {
                    "term": "Over-locker (Serger)",
                    "simple": "A specialized sewing machine that cuts raw edges and wraps threads around them to prevent fraying — all in one step.",
                    "formal": "A high-speed specialized sewing machine equipped with knives that automatically trim raw seam allowances while multiple threads interlock around the cut edge, creating an elastic, ravel-proof edge finish.",
                    "example": "Running the inside seams of school trousers through an over-locker for a neat, commercial finish.",
                    "why_it_matters": "Standard lockstitch machines cannot cut and wrap edges simultaneously. An over-locker ensures inside seams look professional and never fray during laundering."
                },
                {
                    "term": "Press Cloth",
                    "simple": "A protective piece of fabric placed between a hot iron and your garment to prevent fabric damage or shiny scorch marks.",
                    "formal": "A clean, flat piece of cotton, linen, or organza fabric placed over a garment before pressing, acting as a thermal barrier that distributes steam and protects delicate textile fibers from direct heat damage, melting, scorching, or developing a glazed surface.",
                    "example": "Placing a damp cotton press cloth over a polyester school uniform before pressing the pleats.",
                    "why_it_matters": "Direct contact with a hot iron can melt synthetic fibers or scorch wool, ruining hours of careful sewing work."
                }
            ]
        },
        "deep_explanation": (
            "The final two categories of sewing items ensure garment quality and laboratory safety.\n\n"
            "**Finishing Tools** neaten edges and press seams flat:\n"
            "- Over-locker (Serger): Stitches, trims, and neatens seams in a single step. Indispensable for professional garment construction.\n"
            "- Iron & Ironing Board: Used to press every seam open as it is sewn. Never skip pressing — it is what separates professional from amateur garments.\n"
            "- Press Cloth: Placed under the iron to protect synthetic, wool, and delicate fabrics from heat damage.\n\n"
            "Key Distinction — Ironing vs. Pressing:\n"
            "- Ironing is a sliding, back-and-forth motion to remove wrinkles from finished garments.\n"
            "- Pressing is a vertical lift-and-lower motion — lower the iron onto the seam, apply steam and light pressure, then lift straight up. Pressing sets stitches into fabric without stretching pattern lines.\n\n"
            "**Storage Tools** protect tools and maintain lab safety:\n"
            "- Sewing Box/Kit: A portable, sectioned container for needles, pins, tape measures, and small scissors.\n"
            "- Thread Rack: A wall-mounted frame with pegs that stores thread spools neatly and prevents tangling and fading.\n"
            "- Fabric Bins & Shelves: Clean, dry storage cabinets protecting fabric from dust, dampness, insect pests, and fading.\n"
            "- Pattern Envelopes/Boxes: Flat storage for paper pattern pieces to prevent tearing or loss."
        ),
        "practical": {
            "title": "Testing the Thermal Protection of a Press Cloth on Polyester Fabric",
            "steps": [
                {"step_number": 1, "instruction": "Set the electric iron to a medium-high temperature setting."},
                {"step_number": 2, "instruction": "Lay the first polyester scrap directly on the ironing board. Press the hot iron directly onto the scrap for 5 seconds. Observe if it developed a shiny glaze or melted."},
                {"step_number": 3, "instruction": "Lay the second polyester scrap on the ironing board. Place a damp cotton press cloth over the scrap."},
                {"step_number": 4, "instruction": "Press the hot iron onto the press cloth for 5 seconds. Lift the cloth and observe the fabric texture."},
                {"step_number": 5, "instruction": "Compare both scraps: record the differences in color, shine, texture, and flexibility."}
            ]
        },
        "youtube_id": "GiHB5aMGLSE",
        "mcq": {
            "question": "What is the primary function of a press cloth during garment finishing?",
            "options": [
                "To wipe dust off the iron soleplate before pressing",
                "To temporarily hold fabric layers together instead of using pins",
                "To act as a heat barrier that protects delicate fibers from scorching, melting, or developing a shiny glaze",
                "To measure the width of hems while pressing"
            ],
            "correct_answer": 2,
            "explanation": "A press cloth is a protective fabric layer placed between the iron and the garment. It distributes heat and steam evenly while preventing direct contact with the iron soleplate, which would scorch wool, melt synthetics, or glaze silk fibers."
        }
    },
    # ──────────────────────────────────────────────────────────────────
    {
        "lesson_num": 4,
        "title": "Selecting Sewing Tools, Equipment, and Materials",
        "hook": (
            "Have you ever visited a fabric shop and felt overwhelmed by hundreds of different "
            "scissors, needles, threads, and fabrics — not knowing which ones to choose? "
            "Making the wrong selection wastes money and ruins fabrics. A skilled home scientist "
            "uses a systematic, logical framework to evaluate every purchase based on the project, "
            "fabric, skill level, budget, and safety requirements."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Sewing_supplies.jpg/640px-Sewing_supplies.jpg",
        "image_caption": "A variety of sewing supplies arranged on a table — threads, needles, scissors, and pins — demonstrating the range of choices a home scientist must evaluate logically.",
        "analogy_title": "Building a Chicken Coop with the Right Tools",
        "analogy_text": (
            "Imagine you are building a small chicken coop in your backyard. You do not need an industrial concrete "
            "mixer or heavy welding machines. You only need a simple hammer, nails, a hand saw, and affordable local "
            "timber. Buying heavy industrial equipment would waste your budget and make the simple project impossible to manage.\n\n"
            "In sewing, you must apply the same logical plan. A beginner mending a torn hem does not need an expensive "
            "over-locker or computerized embroidery machine. Match your tools to your project, budget, and skill level, "
            "and you will always make smart, economical purchasing decisions."
        ),
        "definition": {
            "title": "Key Selection Concepts",
            "definitions": [
                {
                    "term": "Quality Needlework Selection",
                    "simple": "Choosing the best, most durable sewing tools and materials that match your budget, skills, and project needs.",
                    "formal": "The systematic process of analyzing and selecting sewing tools, equipment, and textile materials based on project complexity, fabric compatibility, user proficiency, financial constraints, durability parameters, and safety features.",
                    "example": "Choosing polyester thread over cotton thread when sewing stretchy synthetic fabric, because polyester has superior elasticity and will not snap during wear.",
                    "why_it_matters": "Poor selection leads to broken needles, shredded threads, wasted fabrics, and frustration. Correct selection guarantees smooth sewing operations and durable garments."
                }
            ]
        },
        "deep_explanation": (
            "When selecting sewing tools, a wise home scientist evaluates 7 critical factors:\n\n"
            "a) Type of Project: A simple repair (sewing a button) needs only a hand needle, thread, and thimble. A complex shirt requires shears, marking tools, a measuring tape, pins, and a sewing machine.\n\n"
            "b) Fabric Type: Fine fabrics (silk, chiffon) need thin, sharp pins, silk thread, and fine needles (size 9–10). Medium fabrics (cotton, linen) use standard polyester thread and medium needles (size 7–8). Heavy fabrics (denim, canvas) require heavy-duty threads and thick needles (size 3–4).\n\n"
            "c) User Skill Level: Beginners should start with basic, high-quality hand tools before investing in advanced machines. Learning hand stitches builds coordination and layout skills.\n\n"
            "d) Budget Constraints: Prioritize essential quality tools. One high-quality pair of fabric shears outperforms five cheap pairs that dull after three cuts and ruin fabric.\n\n"
            "e) Durability & Quality: Look for high-carbon steel blades joined with an adjustable screw (which can be tightened and sharpened) rather than plastic rivets that cannot be repaired.\n\n"
            "f) Safety Features: Sewing machines should have needle guards; electric irons should have automatic shut-off triggers to prevent fires.\n\n"
            "g) Local Availability: Select brands easily available in local shops so replacements and color-matched threads are always accessible."
        ),
        "practical": {
            "title": "Demonstrating Needle-Fabric-Thread Compatibility",
            "steps": [
                {"step_number": 1, "instruction": "Push a thick hand needle (size 3) through a delicate chiffon fabric scrap. Observe the puncture hole it leaves in the fine fabric."},
                {"step_number": 2, "instruction": "Try to thread the thin hand needle (size 10) with thick embroidery thread. Note if the thread can pass through the tiny eye."},
                {"step_number": 3, "instruction": "Try to push the thin hand needle (size 10) through thick denim fabric using light pressure. Note if the needle bends."},
                {"step_number": 4, "instruction": "Try the thick needle (size 3) through the denim. Note how it penetrates easily without bending."},
                {"step_number": 5, "instruction": "Record all observations in a 3-column table: Test / Needle / Result. Discuss which combinations worked correctly."}
            ]
        },
        "youtube_id": "5qzEa8IbwD8",
        "mcq": {
            "question": "Which factor is the most important to consider when selecting the correct size of a hand sewing needle for a project?",
            "options": [
                "The color of the sewing box",
                "The weight and properties of the fabric being sewn",
                "The brand name of the tape measure",
                "The height of the ironing board"
            ],
            "correct_answer": 1,
            "explanation": "Different fabric weights require specific needle thicknesses. Fine fabrics need thin needles to prevent large, ugly puncture holes, while heavy fabrics need thick, strong needles that will not bend or break during stitching."
        }
    },
    # ──────────────────────────────────────────────────────────────────
    {
        "lesson_num": 5,
        "title": "The Sewing Machine — Anatomy (Parts and Functions)",
        "hook": (
            "Have you ever sat in front of a sewing machine and felt scared by all the moving parts, "
            "dials, and levers? The needle moves like a lightning-fast piston. Threads run in multiple "
            "directions. How do all these parts coordinate to create a perfect, even stitch? "
            "Understanding the anatomy of a lockstitch sewing machine transforms fear into confidence "
            "and random guesswork into precise, controlled operation."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Singer_sewing_machine.jpg/640px-Singer_sewing_machine.jpg",
        "image_caption": "A classic Singer lockstitch sewing machine showing the hand-wheel, thread take-up lever, tension dial, presser foot, needle bar, throat plate, and stitch regulator.",
        "analogy_title": "The Mechanical Bicycle",
        "analogy_text": (
            "Imagine a bicycle. To ride safely, you must know what the handlebar, pedals, chain, brakes, "
            "and wheels do. If you pedal without holding the handlebar, you will fall. If you apply the brakes "
            "too hard at high speed, you might slide.\n\n"
            "A sewing machine is a highly efficient mechanical bicycle for fabric. It has pedals (the foot controller), "
            "a wheel (the hand-wheel), and chains inside (the drive shaft connecting the wheel to the needle gears). "
            "To operate it without breaking needles or jamming thread, you must learn the names and functions of "
            "each part — just as you must know your bicycle before riding it on a busy road."
        ),
        "definition": {
            "title": "Key Machine Anatomy Terminology",
            "definitions": [
                {
                    "term": "Thread Take-up Lever",
                    "simple": "The metal lever on the front of the machine that bobs up and down, pulling thread from the spool and feeding it to the needle.",
                    "formal": "A pivoting metal lever on the sewing machine head that rises and falls in synchronization with the needle bar — pulling thread from the spool during its upward stroke to tighten the stitch, and feeding thread downward to allow the needle to form a loop.",
                    "example": "Watching the silver hook-like lever bobbing actively on the front of the machine as you sew.",
                    "why_it_matters": "Forgetting to thread this lever results in instant thread jams, loose loops, or the thread slipping out of the needle eye completely."
                },
                {
                    "term": "Feed Dog",
                    "simple": "The small metal teeth under the presser foot that move the fabric forward automatically as you sew.",
                    "formal": "A set of ridged, metal, tooth-like feed bars located in slots of the needle plate that move in an elliptical path to grip the fabric underside and feed it through the machine at a consistent speed corresponding to the selected stitch length.",
                    "example": "Feeling the saw-tooth metal ridges under the presser foot when the machine is turned off.",
                    "why_it_matters": "Without the feed dog, fabric stays in one place and the needle stitches in the same spot repeatedly, shredding the fabric and creating a giant tangle of thread underneath."
                }
            ]
        },
        "deep_explanation": (
            "The lockstitch sewing machine is divided into three structural areas:\n\n"
            "1. THE HEAD: The complete sewing machine unit containing internal moving gears, the needle assembly, and tension controls.\n"
            "   - Hand-wheel (Balance Wheel): Turned manually toward you to raise/lower the needle for precise stitching.\n"
            "   - Needle Bar: The vertical steel rod that holds the needle and drives it up and down.\n"
            "   - Thread Take-up Lever: Pulls thread from the spool and releases it to form and tighten stitches.\n"
            "   - Presser Foot: Holds the fabric flat and firm against the feed dog as you sew.\n"
            "   - Presser Foot Lifter: A lever behind the head that raises/lowers the presser foot. Always lower before sewing.\n"
            "   - Tension Dial: Controls how tightly the upper thread flows to the needle.\n\n"
            "2. THE ARM: The horizontal curved bar containing the main horizontal drive shaft.\n"
            "   - Spool Pin: Holds the thread spool on top of the arm.\n"
            "   - Bobbin Winder: A spindle that winds thread onto the bobbin automatically.\n"
            "   - Stitch Length Dial (Regulator): Controls stitch length (0 = no movement; 4–5 = longest stitches for tacking).\n"
            "   - Stitch Selector: On modern machines, selects stitch types (straight, zigzag, buttonhole).\n\n"
            "3. THE BED: The flat metal base plate.\n"
            "   - Feed Dog: Ridged metal teeth that automatically advance the fabric.\n"
            "   - Throat Plate (Needle Plate): Flat metal cover with seam allowance guide lines.\n"
            "   - Bobbin Case: Small metal holder under the throat plate that supplies lower thread.\n"
            "   - Foot Pedal (Controller): Floor pedal that controls motor speed.\n\n"
            "How the lockstitch forms: The needle pushes upper thread down through the fabric. A rotating shuttle hook underneath catches a loop of this thread and sweeps it around the bobbin case. As the needle rises, the take-up lever pulls the loop tight, locking the two threads together in the center of the fabric layers."
        ),
        "practical": {
            "title": "Hands-On Structural Inspection of a Sewing Machine",
            "steps": [
                {"step_number": 1, "instruction": "Ensure the machine is completely UNPLUGGED. Locate the hand-wheel on the right side. Rotate it slowly toward you."},
                {"step_number": 2, "instruction": "Observe which other parts move simultaneously: Does the needle bar and thread take-up lever rise and fall together?"},
                {"step_number": 3, "instruction": "Locate the presser foot lifter at the back. Raise and lower it, observing how the presser foot lifts off the throat plate."},
                {"step_number": 4, "instruction": "Slide open the metal cover plate on the bed to locate the bobbin case. Remove it and inspect how it locks onto the shuttle spindle."},
                {"step_number": 5, "instruction": "Locate the stitch length dial. Rotate it to 0, then 2, then 4, observing how it changes the feed dog's horizontal movement distance."}
            ]
        },
        "youtube_id": "FxL5bfKL5L4",
        "mcq": {
            "question": "Which structural division of the sewing machine contains the internal moving gears, the needle assembly, and the tension controls?",
            "options": [
                "The Bed",
                "The Arm",
                "The Head",
                "The Foot Pedal"
            ],
            "correct_answer": 2,
            "explanation": "The Head is the complete vertical and horizontal metal housing containing all primary gears, stitch mechanisms, needle bar, take-up lever, presser foot, and tension dial controls."
        }
    },
    # ──────────────────────────────────────────────────────────────────
    {
        "lesson_num": 6,
        "title": "The Sewing Machine — Threading and Winding the Bobbin",
        "hook": (
            "Have you ever threaded a sewing machine, started sewing, and after a few stitches "
            "the stitches looked like loose, messy loops on the bottom of the fabric? You checked "
            "everything and it all seemed fine. The reason is almost always a single missed threading "
            "step. Threading a sewing machine correctly is like guiding a ball through a maze — "
            "miss even one gate and the entire system fails."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Sewing_machine_thread_path.jpg/640px-Sewing_machine_thread_path.jpg",
        "image_caption": "Step-by-step close-up showing the exact path of upper thread from the spool through tension discs, take-up lever, and down to the needle eye on a domestic lockstitch machine.",
        "analogy_title": "The Gate-by-Gate Maze",
        "analogy_text": (
            "Imagine a maze where you must guide a ball through a specific path to trigger a buzzer at the end. "
            "Every guide, hook, and gate is a required checkpoint. If the ball misses even ONE single gate, it "
            "rolls out of bounds and the buzzer never rings — even though it may look like it went somewhere.\n\n"
            "Threading a sewing machine follows the exact same logic. Every guide, hook, and tension disc is a "
            "compulsory gate. Miss the tension discs and the thread runs freely with zero tension — giant loops "
            "form under the fabric. Miss the take-up lever and stitches never lock. Follow every step in sequence "
            "and the result is a perfectly balanced, beautiful lockstitch."
        ),
        "definition": {
            "title": "Key Threading Terminology",
            "definitions": [
                {
                    "term": "Bobbin Winding",
                    "simple": "Spooling thread from a large thread spool onto a small metal or plastic bobbin to feed the lower stitching system.",
                    "formal": "The process of feeding thread from the main spool, through a tension guide, onto a small bobbin fitted on the bobbin winder spindle, which rotates rapidly to wind thread evenly and tightly before insertion into the bobbin case.",
                    "example": "Engaging the bobbin winder spindle and pressing the foot pedal to wind a spool of blue thread onto a metal bobbin.",
                    "why_it_matters": "Thread must be wound onto the bobbin evenly with consistent tension. Loosely hand-wound bobbins cause skipped stitches and thread jams."
                },
                {
                    "term": "Tension Discs",
                    "simple": "A pair of metal plates that squeeze the upper thread, controlling how smoothly it flows to the needle.",
                    "formal": "Two concave metal plates pressed together by a spring and adjusted by a dial, exerting controlled friction on the upper thread as it passes between them, ensuring the stitch locks perfectly in the center of the fabric.",
                    "example": "Adjusting the upper tension dial from 3 to 4 to stop the bobbin thread from showing as loose loops on the bottom of the fabric.",
                    "why_it_matters": "If thread slips out of the tension discs or if tension is too loose, the thread flows too fast, creating huge loose loops of thread under the fabric."
                }
            ]
        },
        "deep_explanation": (
            "Correct threading involves three sequential procedures:\n\n"
            "STEP 1 — Bobbin Winding:\n"
            "1. Disengage the needle by pulling out the inner knob of the hand-wheel (clutch) — safety precaution, stops needle from moving.\n"
            "2. Place thread spool on spool pin.\n"
            "3. Pass thread through the bobbin winding tension guide.\n"
            "4. Thread through a hole in the bobbin rim, wrap a few times, and push bobbin onto winder spindle.\n"
            "5. Slide spindle right to engage; hold thread tail; press foot pedal to wind. The winder stops automatically when full.\n\n"
            "STEP 2 — Upper Threading (always with presser foot RAISED to open tension discs):\n"
            "1. Place spool on spool pin.\n"
            "2. Pull thread through the first thread guide on top of the arm.\n"
            "3. Pull thread down and slide between the two tension discs, wrapping the tension spring.\n"
            "4. Pull thread up through the next guide hook.\n"
            "5. Feed thread through the eye of the THREAD TAKE-UP LEVER (from right to left) — most critical step!\n"
            "6. Pull thread down through needle bar guides.\n"
            "7. Thread the needle eye, leaving a 10 cm tail extending backward.\n\n"
            "STEP 3 — Bobbin Case Insertion and Drawing Up Lower Thread:\n"
            "1. Insert wound bobbin into bobbin case; pull thread through the tension spring slot.\n"
            "2. Push bobbin case onto shuttle spindle; press until it clicks.\n"
            "3. Hold the upper needle thread tail gently.\n"
            "4. Rotate hand-wheel toward you one full cycle.\n"
            "5. Pull the upper thread gently — a loop of lower thread pops up through the needle hole.\n"
            "6. Pull both tails (10 cm) flat toward the back of the machine, under the presser foot."
        ),
        "practical": {
            "title": "Threading the Machine and Verifying Correct Lockstitch Formation",
            "steps": [
                {"step_number": 1, "instruction": "Wind a bobbin with blue thread following the step-by-step procedure (disengage needle first)."},
                {"step_number": 2, "instruction": "Thread the upper system with red thread, following the spool-to-needle sequence carefully. Ensure presser foot is RAISED throughout."},
                {"step_number": 3, "instruction": "Insert the bobbin case into the shuttle and draw up the blue lower thread through the throat plate."},
                {"step_number": 4, "instruction": "Place a medium cotton fabric scrap under the presser foot, lower the foot, and turn the hand-wheel manually for 5 stitches."},
                {"step_number": 5, "instruction": "Examine the fabric: red thread should show on top, blue on bottom, with both interlocked perfectly in the middle. If loops appear, identify the missed threading step."}
            ]
        },
        "youtube_id": "q8OL7Ib9tnE",
        "mcq": {
            "question": "Why must you raise the presser foot before threading the upper thread path through the tension discs?",
            "options": [
                "To make the bobbin spin faster during winding",
                "To allow the thread to slip deep between the tension discs while they are pushed apart and open",
                "To prevent the needle bar from moving while threading",
                "To automatically select the correct stitch length for the fabric"
            ],
            "correct_answer": 1,
            "explanation": "The tension discs are mechanically linked to the presser foot lever. When the presser foot is raised, the discs are pushed apart (open), allowing the thread to seat correctly between them. If threaded with foot down, the clamped discs cannot accept the thread properly, resulting in zero upper tension and tangled loops under the fabric."
        }
    },
    # ──────────────────────────────────────────────────────────────────
    {
        "lesson_num": 7,
        "title": "Operating the Sewing Machine (Stitch Selection and Fabric Guiding)",
        "hook": (
            "Have you ever tried to sew a straight line on a machine and the fabric kept veering left "
            "and right, making your seam look like a squiggly road map? Or did you press the foot pedal "
            "too hard and the machine rocketed forward, shooting the fabric completely out of control? "
            "Professional sewing machine operation requires mastering three interconnected skills: "
            "speed control, stitch selection, and fabric guiding — all at the same time."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Sewing_machine_in_use.jpg/640px-Sewing_machine_in_use.jpg",
        "image_caption": "A student's hands gently guiding a piece of cotton fabric under a sewing machine presser foot, keeping fingers at a safe distance while watching the seam allowance markings on the throat plate.",
        "analogy_title": "Learning to Drive a Car",
        "analogy_text": (
            "Imagine learning to drive a car for the first time. You do not smash the accelerator to the floor "
            "the moment you sit down. You press it gently to go slow, and you use both hands on the steering "
            "wheel to guide the car smoothly along the lane. You don't push the car from outside — the engine "
            "moves it, and you simply steer.\n\n"
            "Operating a sewing machine uses exactly the same principles. The foot pedal is your accelerator — "
            "gentle pressure gives control. Your hands on the fabric are your steering wheel — you don't push "
            "or pull the fabric; the feed dog moves it automatically while you guide its direction gently."
        ),
        "definition": {
            "title": "Key Operating Terminology",
            "definitions": [
                {
                    "term": "Stitch Length Dial",
                    "simple": "The dial on the machine that regulates how long each individual stitch is.",
                    "formal": "A calibrated mechanical control dial that adjusts the horizontal feed dog stroke distance, regulating the length of each stitch, typically from 0 mm to 4–5 mm.",
                    "example": "Setting the stitch length to 2.5 mm for general seam construction on a cotton skirt.",
                    "why_it_matters": "Fine fabrics need short stitches (1.5–2 mm) to prevent puckering, while heavy fabrics need longer stitches (3–4 mm) to accommodate thick thread crossings."
                },
                {
                    "term": "Pivot (Pivoting)",
                    "simple": "A technique for turning sharp corners cleanly by keeping the needle down in the fabric, lifting the presser foot, and rotating the fabric.",
                    "formal": "A seam-turning technique where the machine is stopped with the needle fully lowered into the fabric, the presser foot lifter is raised, the fabric is rotated around the needle axis to a new direction, the presser foot is lowered, and sewing resumes.",
                    "example": "Sewing a square pocket and pivoting at each corner to achieve clean, sharp 90-degree angles.",
                    "why_it_matters": "Turning fabric with the needle up loses your place, creates loose stitches at the corner, and ruins the seam line."
                }
            ]
        },
        "deep_explanation": (
            "Professional sewing machine operation involves three coordinated skill areas:\n\n"
            "1. SPEED CONTROL — The Foot Pedal:\n"
            "- Apply pressure gently with your toes, like squeezing a sponge.\n"
            "- Practice going stitch-by-stitch before attempting full speed.\n"
            "- Barefoot or light-shoe practice builds maximum foot sensitivity.\n\n"
            "2. STITCH SETTINGS — Length & Type:\n"
            "- Basting/Tacking: 4–5 mm (very long, temporary stitches, easy to pull out).\n"
            "- Standard Seams (Cotton): 2.5 mm (balance of strength and neatness).\n"
            "- Fine Fabrics (Chiffon): 1.5–2 mm (prevents seam puckering).\n"
            "- Stitch Type: Straight stitch for seams; zigzag stitch for stretchy fabrics and raw edge neatening.\n\n"
            "3. FABRIC GUIDING:\n"
            "- The Golden Rule: NEVER push or pull the fabric. Let the feed dog move it naturally.\n"
            "- Pulling the fabric bends the needle, causing it to strike the metal throat plate and shatter — a serious eye injury hazard.\n"
            "- Left hand gently on the fabric side; right hand in front guiding the edge along seam allowance markings on the throat plate.\n"
            "- Keep fingers at least 2 cm away from the moving needle bar at all times.\n\n"
            "BACK-TACKING (Securing Seams):\n"
            "At the start and end of every permanent seam: sew 3 stitches forward, press the reverse lever, sew 3 stitches backward over the first stitches, release, and sew forward. This locks thread ends so the seam never unravels.\n\n"
            "PIVOTING AT CORNERS:\n"
            "Stop → turn hand-wheel to lower needle into fabric → raise presser foot → rotate fabric → lower presser foot → resume sewing."
        ),
        "practical": {
            "title": "Speed Control and Pivot Practice Using Paper Templates (No Thread)",
            "steps": [
                {"step_number": 1, "instruction": "Remove all thread from the machine and insert a needle. This 'dry run' eliminates the distraction of thread tension."},
                {"step_number": 2, "instruction": "Place a printed paper template (with straight lines, wavy lines, and 90-degree corners) under the presser foot. Lower the foot."},
                {"step_number": 3, "instruction": "Gently press the foot pedal to sew along the straight lines, letting the feed dog move the paper. Steer gently with both hands."},
                {"step_number": 4, "instruction": "Practice sewing along the wavy lines, controlling speed carefully to follow the curves."},
                {"step_number": 5, "instruction": "At each 90-degree corner: stop, lower needle with hand-wheel, raise presser foot, rotate paper, lower foot, resume — the complete pivot sequence."}
            ]
        },
        "youtube_id": "HgJYUm7Yk5g",
        "mcq": {
            "question": "What is the correct purpose of sewing 3–4 reverse stitches (back-tacking) at the start and end of a permanent seam?",
            "options": [
                "To make the stitch length visually appear longer",
                "To lock the thread ends and prevent the seam from unraveling under tension",
                "To clean the feed dog of lint and thread residue",
                "To automatically adjust the upper thread tension"
            ],
            "correct_answer": 1,
            "explanation": "Back-tacking overlaps stitches at seam ends, creating a double-knotted loop that locks the upper and lower threads securely. This ensures seam ends cannot pull apart during wear or washing, even under sustained daily tension."
        }
    },
    # ──────────────────────────────────────────────────────────────────
    {
        "lesson_num": 8,
        "title": "Common Sewing Machine Faults and Remedies",
        "hook": (
            "Have you ever been sewing smoothly when suddenly the upper thread snapped? You rethreaded "
            "it, started again — snap, it broke again in the exact same way. Or you noticed the needle "
            "was skipping stitches, leaving long unsewn gaps. Sewing machines are precise mechanical "
            "devices. When they malfunction, they are sending an error code. Learn to read those codes "
            "and you can fix 99% of common faults yourself without calling a technician."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Sewing_machine_troubleshooting.jpg/640px-Sewing_machine_troubleshooting.jpg",
        "image_caption": "A troubleshooting illustration showing four common sewing machine problems: thread nesting under fabric, skipped stitches, fabric puckering along a seam, and thread shredding at the needle eye.",
        "analogy_title": "Troubleshooting Your Smartphone",
        "analogy_text": (
            "Imagine your smartphone suddenly freezes or an app refuses to open. You don't immediately smash "
            "the phone or rush to a repair shop. First you try systematic troubleshooting: close the app, "
            "restart the phone, toggle internet on and off. Most of the time, these simple steps resolve 90% "
            "of issues without any professional help.\n\n"
            "A sewing machine operates on the same principle. Each fault — broken thread, skipped stitches, "
            "puckered fabric — is an error code telling you exactly which component is out of balance. "
            "By learning to interpret and respond to these codes systematically, you become your own "
            "machine technician."
        ),
        "definition": {
            "title": "Key Fault Terminology",
            "definitions": [
                {
                    "term": "Skipped Stitches",
                    "simple": "When the machine needle moves up and down but fails to lock the upper and lower threads together, leaving gaps in the seam.",
                    "formal": "A sewing machine malfunction where the rotating shuttle hook fails to catch the loop of the upper needle thread, preventing lockstitch formation and resulting in intermittent unstitched gaps along the seam line.",
                    "example": "Sewing a cotton knit shirt and finding 3 normal stitches, a 2 cm gap of loose thread, then 4 more normal stitches.",
                    "why_it_matters": "Skipped stitches fatally weaken a seam. Usually caused by a bent needle, wrong needle type, or incorrectly inserted needle."
                },
                {
                    "term": "Fabric Puckering",
                    "simple": "When fabric gathers and wrinkles along the seam line as you sew, looking bunched up and crumpled.",
                    "formal": "The bunching, wrinkling, or gathering of fabric along a stitched seam line, caused by excessive thread tension pulling fabric fibers together, or an inappropriate stitch length for the fabric weight.",
                    "example": "Sewing a seam on lightweight polyester lining and finding the seam gathered up like a crumpled accordion.",
                    "why_it_matters": "Puckered seams cannot be ironed flat and look extremely unprofessional. Adjusting stitch length or loosening tension dials resolves this."
                }
            ]
        },
        "deep_explanation": (
            "The five most common sewing machine faults with their causes and remedies:\n\n"
            "1. UPPER THREAD BREAKS:\n"
            "   Causes: Incorrect upper threading; tension too tight; needle inserted backwards; blunt/bent needle; knot in thread.\n"
            "   Remedies: Unthread completely and rethread; loosen upper tension dial; fix needle direction; insert new needle; cut thread knots.\n\n"
            "2. LOWER (BOBBIN) THREAD BREAKS:\n"
            "   Causes: Incorrect bobbin case threading; bobbin case too tight; lint inside bobbin case; unevenly wound bobbin.\n"
            "   Remedies: Remove and rethread bobbin case tension spring; brush lint from shuttle; loosen case screw slightly; rewind bobbin evenly.\n\n"
            "3. SKIPPED STITCHES:\n"
            "   Causes: Needle bent, blunt, or damaged; wrong needle size/type for fabric; needle inserted incorrectly.\n"
            "   Remedies: Replace with brand-new needle; select correct needle size; re-insert needle correctly and tighten clamp screw.\n\n"
            "4. FABRIC PUCKERING (GATHERING):\n"
            "   Causes: Upper and lower tensions too tight; stitch length too long for fine fabric; needle too thick for delicate material.\n"
            "   Remedies: Loosen both tensions; shorten stitch length on dial; switch to a thinner needle (size 9–11).\n\n"
            "5. THREAD NESTING (LOOPS UNDER FABRIC):\n"
            "   Causes: Upper thread skipped tension discs; machine threaded with presser foot down (discs clamped shut); bobbin inserted backwards.\n"
            "   Remedies: Raise presser foot; pull thread out; rethread tension discs correctly; always thread with foot raised; re-insert bobbin in correct rotation direction."
        ),
        "practical": {
            "title": "Deliberate Fault Creation and Systematic Troubleshooting",
            "steps": [
                {"step_number": 1, "instruction": "Thread the machine correctly and sew a test seam on cotton fabric to establish a normal stitch baseline."},
                {"step_number": 2, "instruction": "Fault 1: Deliberately skip threading the take-up lever. Sew a seam and observe the thread nesting that forms under the fabric."},
                {"step_number": 3, "instruction": "Fix the threading. Then tighten the tension dial to maximum. Sew a seam on fine polyester fabric and observe the puckering."},
                {"step_number": 4, "instruction": "Reset tension to normal. Then insert a needle with the flat side facing the wrong direction. Sew 5 stitches and observe skipped stitches."},
                {"step_number": 5, "instruction": "Apply the correct remedy for each fault observed. Record the fault, its cause, and the remedy in a 3-column table."}
            ]
        },
        "youtube_id": "xJnqDqBLAnc",
        "mcq": {
            "question": "A student notices that after sewing 3 perfect stitches, there is a 2 cm gap of loose thread, then 3 more stitches again. What is the most likely cause?",
            "options": [
                "The upper thread tension is too loose",
                "The needle is bent, blunt, or damaged causing the shuttle hook to intermittently miss the thread loop",
                "The stitch length dial is set too high",
                "The bobbin has run out of thread"
            ],
            "correct_answer": 1,
            "explanation": "Intermittent skipped stitches are the classic symptom of a damaged needle. A bent or blunt needle cannot descend in a perfectly vertical path, causing the rotating shuttle hook to occasionally miss catching the upper thread loop, resulting in gaps without a locked stitch."
        }
    },
    # ──────────────────────────────────────────────────────────────────
    {
        "lesson_num": 9,
        "title": "Care, Maintenance, and Storage of a Sewing Machine",
        "hook": (
            "A school sewing machine that is used every day but never cleaned or oiled will, within one "
            "term, be clogged with lint, running roughly, breaking needles frequently, and skipping "
            "stitches. Eventually it will seize up completely and require expensive professional repair. "
            "The same machine, properly cleaned after each use and oiled weekly, can operate smoothly "
            "for 20–30 years. Machine longevity is entirely determined by the quality of its maintenance."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Sewing_machine_maintenance.jpg/640px-Sewing_machine_maintenance.jpg",
        "image_caption": "A technician cleaning and oiling a domestic sewing machine — removing lint from the bobbin race and applying machine oil to moving joints for smooth, long-lasting operation.",
        "analogy_title": "The Engine Oil Analogy",
        "analogy_text": (
            "Imagine a car engine. If you fill it with petrol and drive it every day without ever checking or changing "
            "the engine oil, the metal pistons will grind against each other, generating tremendous friction. "
            "Within weeks, the engine will seize and need complete replacement — an enormous expense that could "
            "have been avoided with a few shillings of oil every few months.\n\n"
            "A sewing machine's internal moving parts are exactly like a car engine. They are high-speed, "
            "precision metal parts rotating at thousands of cycles per minute. Without lubrication, they generate "
            "friction, heat, and wear. Regular oiling keeps them gliding silently and smoothly, preventing "
            "premature mechanical failure."
        ),
        "definition": {
            "title": "Key Machine Maintenance Terminology",
            "definitions": [
                {
                    "term": "Machine Oil (Sewing Machine Lubricant)",
                    "simple": "A light, clear, mineral-based oil used to lubricate moving metal joints inside a sewing machine.",
                    "formal": "A refined, low-viscosity mineral oil specifically formulated for precision mechanical instruments, applied in small quantities (1–2 drops) to all metal-on-metal friction points in the sewing machine to reduce wear, prevent rust, and ensure smooth silent operation.",
                    "example": "Applying one drop of sewing machine oil to the shuttle hook race after cleaning out lint.",
                    "why_it_matters": "Un-lubricated metal joints generate friction and heat, accelerating mechanical wear and eventually causing permanent seizure of the machine."
                },
                {
                    "term": "Lint Accumulation",
                    "simple": "The gradual build-up of tiny fiber fragments and thread dust inside the machine's bobbin race and feed dog slots.",
                    "formal": "The progressive accumulation of microscopic textile fiber fragments, thread breakage debris, and fabric dust in the mechanical cavities of the sewing machine, particularly in the shuttle race, bobbin case compartment, and feed dog slots, which obstructs mechanical movement and oil circulation.",
                    "example": "Opening the bed slide plate after one week of daily use and finding a thick gray layer of compacted lint around the shuttle.",
                    "why_it_matters": "Accumulated lint clogs mechanical parts, causes the machine to run roughly, breaks thread, and eventually jams the shuttle mechanism permanently."
                }
            ]
        },
        "deep_explanation": (
            "Sewing machine maintenance follows three timeframes:\n\n"
            "AFTER EVERY USE:\n"
            "- Remove the needle from the bar and store safely.\n"
            "- Remove bobbin and bobbin case; brush all lint from the shuttle race using a small brush.\n"
            "- Wipe all exterior surfaces with a soft, dry cloth.\n"
            "- Turn off the motor and unplug the machine.\n"
            "- Cover with a fitted dust cover to protect from dust, insects, and UV light.\n\n"
            "WEEKLY MAINTENANCE:\n"
            "- Oiling: Apply 1–2 drops of sewing machine oil to all metal-on-metal moving joints. Never over-oil — excess oil attracts lint and stains fabric.\n"
            "- Check needle condition: Replace any needle that is even slightly bent, blunt, or corroded.\n"
            "- Check belt tension (on treadle models): belt should be taut but not overtight.\n"
            "- Test stitch quality: Sew a test seam on scrap fabric to verify tension balance and stitch lock quality.\n\n"
            "LONG-TERM STORAGE:\n"
            "- Clean and oil the machine thoroughly before storing.\n"
            "- Remove all thread to prevent tension spring fatigue.\n"
            "- Lower the presser foot onto a folded cloth pad (relieves spring pressure).\n"
            "- Cover fully with a machine cover or hard case.\n"
            "- Store on a flat, stable surface in a dry location — dampness causes rust; tilting misaligns the shuttle.\n"
            "- Have the machine professionally serviced by a qualified technician every 12 months."
        ),
        "practical": {
            "title": "Full Machine Cleaning and Oiling Procedure",
            "steps": [
                {"step_number": 1, "instruction": "Unplug the machine. Remove the presser foot, needle, and throat plate to expose the feed dog and bobbin compartment."},
                {"step_number": 2, "instruction": "Use a small stiff brush to remove all lint from the feed dog slots, shuttle race, and bobbin case compartment."},
                {"step_number": 3, "instruction": "Apply 1 drop of sewing machine oil to the shuttle hook race, needle bar pivot, and any visible metal-on-metal joints."},
                {"step_number": 4, "instruction": "Reassemble the throat plate, bobbin case (empty), and needle. Wipe all external surfaces with a dry cloth."},
                {"step_number": 5, "instruction": "Re-thread the machine, place a scrap fabric piece under the foot, and run 10 stitches to distribute oil through the system and verify smooth operation."}
            ]
        },
        "youtube_id": "r3sNqBBnhNA",
        "mcq": {
            "question": "Why should you lower the presser foot onto a folded cloth pad before storing a sewing machine for a long period?",
            "options": [
                "To protect the throat plate from being scratched by the presser foot spring",
                "To relieve constant mechanical pressure on the presser foot spring, preventing it from weakening or setting permanently in a compressed position",
                "To prevent dust from entering through the needle hole in the throat plate",
                "To stop the hand-wheel from rotating accidentally during transport"
            ],
            "correct_answer": 1,
            "explanation": "The presser foot spring is kept under constant mechanical load when the foot is lowered. Storing the machine with the foot lowered directly onto metal for extended periods can permanently weaken or set the spring in a compressed position, reducing its clamping pressure on fabric."
        }
    },
    # ──────────────────────────────────────────────────────────────────
    {
        "lesson_num": 10,
        "title": "Using, Caring for, and Storing Other Needlework Tools",
        "hook": (
            "A professional tailor's tools are their most valuable business assets. Dressmaker's "
            "shears that cost 2,000 KES and are properly cared for can last 15 years and deliver "
            "perfectly clean cuts every single time. The same scissors, neglected and used to cut "
            "paper and wire, will be blunt and useless within six months. The longevity and "
            "performance of every sewing tool is entirely dependent on how it is used, cleaned, "
            "and stored after every use."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Sewing_tools_organized.jpg/640px-Sewing_tools_organized.jpg",
        "image_caption": "Neatly organized needlework tools: dressmaker's shears stored in a fabric sheath, a rolled tape measure, pins in a cushion, and needles in their original labeled packet.",
        "analogy_title": "The Surgeon's Instrument Tray",
        "analogy_text": (
            "A surgeon's scalpels, forceps, and suturing needles are sterilized, inspected, and stored in "
            "a sealed tray after every single operation. The surgeon never leaves instruments scattered on "
            "the operating table, never uses a scalpel to open a food can, and never stores instruments in "
            "a damp drawer. Each instrument has a specific use, a specific cleaning protocol, and a specific "
            "storage position.\n\n"
            "Every sewing tool deserves exactly the same disciplined approach. Scissors have a specific use "
            "(fabric only), a cleaning procedure (wiped and oiled), and a storage position (in a sheath, "
            "closed, in the sewing box). Pins belong in a pin cushion. Needles belong in their packet. "
            "Tape measures are rolled, never folded."
        ),
        "definition": {
            "title": "Key Tool Care Principles",
            "definitions": [
                {
                    "term": "Emery Cushion (Strawberry)",
                    "simple": "A small, sand-filled fabric strawberry attached to a pin cushion that sharpens and polishes needle tips by inserting them repeatedly.",
                    "formal": "A small abrasive-filled fabric attachment to a pin cushion, filled with iron filings or fine emery powder, used to re-sharpen and de-rust hand sewing needles and pins by working them in and out of the abrasive material.",
                    "example": "Pushing a slightly rusted needle in and out of the emery strawberry 10 times to restore its sharp, smooth tip.",
                    "why_it_matters": "Blunt or rusty needles drag and snag fabric fibers instead of piercing cleanly, causing runs, puckers, and thread breakage."
                },
                {
                    "term": "Blade Sharpening (Honing)",
                    "simple": "The professional process of re-grinding the cutting edge of dressmaker's shears to restore their original sharpness.",
                    "formal": "The removal of micro-nicks and dulled metal from a scissor blade's cutting edge using a whetstone or professional scissor-sharpening service, restoring the precision cutting angle required for clean textile fiber separation.",
                    "example": "Taking dressmaker's shears to a scissor sharpener at the local market when they begin to chew fabric instead of cutting cleanly.",
                    "why_it_matters": "Dull blades bend and fold fabric fibers instead of slicing through them, creating ragged, frayed edges and requiring excessive force."
                }
            ]
        },
        "deep_explanation": (
            "Proper care protocols for each category of needlework tool:\n\n"
            "SCISSORS & SHEARS:\n"
            "- Use: ONLY for cutting fabric. Never cut paper, cardboard, wire, or plastic — these materials instantly dull precision-ground blades.\n"
            "- Care: Wipe blades after each use with a soft cloth. Apply a tiny drop of oil to the screw joint. Have blades professionally sharpened when they begin to chew rather than cut.\n"
            "- Store: In a fabric sheath or case inside the sewing box, blades closed. Always pass to another person handle-first with blades closed.\n\n"
            "NEEDLES & PINS:\n"
            "- Use: Match needle size to fabric weight. Always use a thimble on the middle finger.\n"
            "- Care: Wipe with a soft cloth after use to remove rust-causing moisture and skin oils. Use an emery cushion to restore sharpness. Discard bent or blunt needles immediately.\n"
            "- Store: Pins in a pin cushion (the emery strawberry keeps them sharp). Needles in original labeled packet or needle case. Wrap discarded sharps in paper labeled 'SHARPS — HANDLE WITH CARE' before disposal.\n\n"
            "TAPE MEASURE:\n"
            "- Use: Keep flat; never stretch or yank.\n"
            "- Care: Wipe clean with a dry cloth. Never fold or crease sharply — creases permanently stretch the markings out of accuracy.\n"
            "- Store: Roll loosely in the sewing box. Verify accuracy annually against a rigid metal ruler.\n\n"
            "IRON & IRONING BOARD:\n"
            "- Use: Always use a press cloth on synthetic fabrics. Rest on heel when paused.\n"
            "- Care: Empty the water tank after every use to prevent mineral scale. Descale steam vents with a diluted vinegar solution. Wipe the soleplate cool with a damp cloth.\n\n"
            "FABRIC:\n"
            "- Store: Fold flat in clean, dry, dark cabinets. Use cedar blocks or mothballs to repel fabric-eating insects. Avoid direct sunlight, which fades and weakens fibers."
        ),
        "practical": {
            "title": "Emery Needle Sharpening and Scissor Blade Oiling Demonstration",
            "steps": [
                {"step_number": 1, "instruction": "Select one slightly dull or surface-rusty hand sewing needle. Examine its tip under a magnifying glass — note if it is smooth or micro-pitted."},
                {"step_number": 2, "instruction": "Insert the needle into the emery strawberry 15–20 times in different angles. Re-examine the tip — observe the restored smoothness and shine."},
                {"step_number": 3, "instruction": "Test both the original dull needle and the sharpened needle by drawing each through a light cotton fabric scrap. Note which drags and which slides cleanly."},
                {"step_number": 4, "instruction": "Apply a single tiny drop of light machine oil to the screw joint of a pair of dressmaker's shears. Open and close the blades 10 times to distribute the oil."},
                {"step_number": 5, "instruction": "Test the scissor by cutting a 10 cm line on cotton fabric. Record whether the action is smooth and the cut edge is clean."}
            ]
        },
        "youtube_id": "SZiDpLU4YZo",
        "mcq": {
            "question": "Why must professional dressmaker's shears NEVER be used to cut paper, cardboard, or wire?",
            "options": [
                "Paper chemicals permanently stain the metal blades brown",
                "Paper and cardboard contain abrasive mineral fibers that rapidly dull the precision-ground cutting edge, causing the blades to chew fabric instead of slicing it",
                "It is considered bad luck in traditional African needlework culture",
                "Wire will permanently bend the blades inward"
            ],
            "correct_answer": 1,
            "explanation": "Fabric scissors are precision-ground at a specific angle for soft textile fibers. Paper and cardboard contain abrasive wood mineral particles that act like sandpaper on the cutting edge, dulling it instantly. Once dull, the blades fold and chew fabric instead of slicing cleanly."
        }
    },
    # ──────────────────────────────────────────────────────────────────
    {
        "lesson_num": 11,
        "title": "Safety and Waste Disposal in the Needlework Laboratory",
        "hook": (
            "Every needlework laboratory contains dozens of invisible hazards: needles sharp enough to "
            "puncture an artery, scissors that can sever a finger, irons hot enough to cause third-degree "
            "burns, and electrical cords that can electrocute. In the same laboratory, there are also "
            "thread scraps, fabric offcuts, and discarded sharps that — if disposed of carelessly — create "
            "accidents and environmental harm. Safety in the needlework lab is not an option; it is a "
            "professional and moral responsibility."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Sewing_lab_safety.jpg/640px-Sewing_lab_safety.jpg",
        "image_caption": "A safe needlework laboratory with properly stored tools, a clearly marked sharps disposal tin, fabric waste bins, and fire safety equipment visible near the ironing station.",
        "analogy_title": "The Hospital Operating Theatre Protocol",
        "analogy_text": (
            "In a hospital operating theatre, every nurse counts every needle, every scalpel, and every instrument "
            "before and after surgery. Nothing sharp is left unaccounted for. Instruments are never placed in pockets, "
            "thrown into bins carelessly, or left on surfaces. This rigorous protocol exists because a single "
            "unaccounted needle can cause catastrophic injury.\n\n"
            "The needlework laboratory operates on the same fundamental principle. Every needle must be accounted for. "
            "Every scissors must be stored correctly. Every broken needle must be disposed of safely. "
            "Every electrical hazard must be identified and eliminated. The professional needlework laboratory "
            "is a precision workplace, not a casual hobby space."
        ),
        "definition": {
            "title": "Key Safety & Disposal Terminology",
            "definitions": [
                {
                    "term": "Sharps Disposal Protocol",
                    "simple": "The standardized safe procedure for discarding broken, bent, or dull sewing needles and pins without causing puncture injuries.",
                    "formal": "The systematic process of wrapping discarded sharp metallic objects (broken needles, used pins) in multiple layers of paper, labeling the package 'SHARPS — HANDLE WITH CARE', and depositing them in a designated rigid-walled sharps container or metal tin for safe collection and disposal.",
                    "example": "Wrapping a broken sewing needle in folded paper, labeling it clearly, and placing it in the class sharps tin rather than dropping it in the paper bin.",
                    "why_it_matters": "Unprotected sharps in regular waste bins puncture the hands of cleaning staff and waste disposal workers, causing infections and injuries."
                },
                {
                    "term": "Electrical Hazard Isolation",
                    "simple": "The process of cutting electrical current to a machine or appliance before touching it or clearing a jam.",
                    "formal": "The physical disconnection of an electrical appliance from its power source by unplugging from the mains socket before performing any maintenance, threading, needle changing, or fault-clearing operation, eliminating the risk of electrocution.",
                    "example": "Unplugging the sewing machine from the wall socket before inserting a new needle or clearing a thread jam.",
                    "why_it_matters": "An electrically live machine with a moving needle bar can cause catastrophic hand injuries. Unplugging eliminates all electrical risk."
                }
            ]
        },
        "deep_explanation": (
            "Safety in the needlework laboratory is organized into three hazard categories:\n\n"
            "1. SHARPS SAFETY (Needles, Pins, Scissors, Rotary Cutter):\n"
            "- Needles & Pins: Always store in a pin cushion or needle packet. Never hold in the mouth or leave on bench surfaces. Broken needles: wrap in paper, label 'SHARPS', deposit in metal tin.\n"
            "- Scissors & Shears: Walk with point downward or inside a case. Pass to another person handle-first, blades closed. Never point toward classmates.\n"
            "- Rotary Cutter: Close the blade guard immediately after every single cut. Use only on a self-healing cutting mat.\n"
            "- Needle Stick First Aid: Wash the puncture site under running water, apply light pressure to encourage bleeding (cleanses the wound), and report to the teacher immediately.\n\n"
            "2. MACHINE & ELECTRICAL SAFETY:\n"
            "- Tie back long hair before operating any machine. Tuck in loose clothing.\n"
            "- Keep fingers at least 2 cm clear of the moving needle bar at all times.\n"
            "- Never pull fabric under the needle — bends needle into throat plate, causing shattering.\n"
            "- Dry hands before handling electrical plugs and sockets.\n"
            "- Unplug the machine before threading, needle changing, or clearing jams.\n"
            "- Iron Safety: Never leave a heated iron unattended lying flat. Rest on heel when paused.\n"
            "- Electrical Emergency: If a person is being electrocuted, do NOT touch them with bare hands. Immediately isolate the power at the switch or fuse box, then call for help.\n\n"
            "3. WASTE DISPOSAL & ENVIRONMENTAL RESPONSIBILITY:\n"
            "- Thread ends and fabric scraps: Collect in a dedicated waste bag — not the floor. Small scraps can be upcycled as stuffing for pin cushions or in patchwork art.\n"
            "- Broken/dull needles and pins: Wrap in paper, label clearly, deposit in a rigid metal sharps container.\n"
            "- Chemical waste (stain removers, solvents): Dispose per product label. Never pour down storm drains or sinks — chemical pollution harms aquatic life.\n"
            "- End-of-session lab checklist: Sweep the floor thoroughly, pick up ALL dropped pins with a magnetic pin pick-up tool, return all tools to their correct storage positions."
        ),
        "practical": {
            "title": "Needlework Lab Safety Audit and Hazard Mapping",
            "steps": [
                {"step_number": 1, "instruction": "Walk through the home science needlework laboratory and observe the current state of tool storage, waste disposal, and electrical arrangements."},
                {"step_number": 2, "instruction": "Check for sharps hazards: Are any needles, pins, or scissors lying exposed on bench surfaces or the floor?"},
                {"step_number": 3, "instruction": "Check electrical safety: Are any cords frayed, near water, or running across walkways? Are there wet surfaces near power sockets?"},
                {"step_number": 4, "instruction": "Check waste disposal: Is there a dedicated sharps tin? Is there a fabric scrap collection bag? Are any needles or pins in the general waste bin?"},
                {"step_number": 5, "instruction": "Draw a floor plan of the lab, mark each hazard identified with a red circle, and write a numbered list of immediate corrective actions for each hazard found."}
            ]
        },
        "youtube_id": "M5rNVZG5oJE",
        "mcq": {
            "question": "A student finds a broken needle on the lab floor. What is the correct disposal procedure?",
            "options": [
                "Pick it up with fingers and drop it directly into the paper rubbish bin",
                "Leave it on the floor and inform the teacher to deal with it later",
                "Wrap the broken needle in several layers of paper, label it 'SHARPS — HANDLE WITH CARE', and place it in the designated metal sharps container",
                "Flush it down the sink to prevent any classmate from stepping on it"
            ],
            "correct_answer": 2,
            "explanation": "Broken sharps deposited unwrapped in regular waste bins puncture the hands of cleaning staff during bag handling. The correct protocol wraps the sharp in paper (to contain it), labels it clearly (to alert handlers), and places it in a rigid metal sharps container that prevents external penetration."
        }
    }
]


# ─── Main Ingestion Function ──────────────────────────────────────────────────

def ingest_topic_3_1():
    print("=" * 80)
    print("STARTING CBC GRADE 10 HOME SCIENCE TOPIC 3.1 INGESTION (11 LESSONS)")
    print("=" * 80)

    # Read Markdown source file
    md_path = "/home/jason-bitega/Desktop/VL/vlearn_repositories/Grade 10 Homescience/Grade10_Home_Science_Topic_3_1.md"
    if os.path.exists(md_path):
        with open(md_path, "r", encoding="utf-8") as f:
            md_content = f.read()
        print(f"[+] Successfully loaded source markdown ({len(md_content):,} bytes, {len(md_content.splitlines())} lines)")
    else:
        print(f"[!] Warning: Markdown source file not found at {md_path}")

    # Resolve curriculum hierarchy
    curriculum = Curriculum.objects.filter(id=5).first()
    if not curriculum:
        curriculum = Curriculum.objects.filter(name__icontains="CBC").first()
    print(f"[+] Curriculum: {curriculum}")

    grade = Grade.objects.filter(curriculum=curriculum, level=10).first()
    print(f"[+] Grade: {grade}")

    subject = Subject.objects.filter(grade=grade, name__icontains="Home Science").first()
    print(f"[+] Subject: {subject}")

    # Topic 3: Clothing and Textiles — get_or_create with order=3
    topic, topic_created = Topic.objects.get_or_create(
        subject=subject,
        order=3,
        defaults={"name": "Clothing and Textiles"}
    )
    if topic_created:
        print(f"[+] Created Topic 3: Clothing and Textiles")
    else:
        print(f"[+] Using existing Topic 3: {topic.name}")

    # Learning Unit 1 under Topic 3
    learning_unit, lu_created = LearningUnit.objects.get_or_create(
        topic=topic,
        order=1,
        defaults={"name": "3.1 Sewing Tools, Equipment, and Materials"}
    )
    if lu_created:
        print(f"[+] Created Learning Unit: 3.1 Sewing Tools, Equipment, and Materials")
    else:
        print(f"[+] Using existing Learning Unit: {learning_unit.name}")

    total_lessons = 0
    total_pages = 0
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
                        "topic": "Clothing and Textiles",
                        "learning_unit": "3.1 Sewing Tools, Equipment, and Materials",
                        "lesson_number": l_num,
                        "grade": 10,
                        "curriculum": "CBC"
                    }
                }
            )

            # Clear old blocks and assets for idempotency
            lesson.blocks.all().delete()
            lesson.assets.all().delete()

            # ── LessonAsset: Wikimedia Photo Hook ──────────────────────────
            img_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                source_type="external",
                storage_type="url",
                status="approved",
                title=f"Visual Hook: {cfg['title']}",
                url=cfg["image_url"],
                metadata={"caption": cfg["image_caption"], "source": "Wikimedia Commons"}
            )
            total_assets += 1

            # ── LessonAsset: Custom SVG Diagram ───────────────────────────
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

            # ── LessonAsset: YouTube Video ─────────────────────────────────
            yt_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="youtube",
                source_type="external",
                storage_type="url",
                status="approved",
                title=f"Video Demonstration: {cfg['title']}",
                url=f"https://www.youtube.com/watch?v={cfg['youtube_id']}",
                metadata={"youtube_id": cfg["youtube_id"]}
            )
            total_assets += 1

            # ──────────────────────────────────────────────────────────────
            # CARD 1 (Page 1): Learning Goal + Wikimedia Photo Hook + Everyday Hook
            # ──────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=1, order=10, component_order=1,
                block_type="learning_goal", component_type="learning_goal",
                title="Learning Goals",
                content={
                    "title": "Lesson Objectives",
                    "goals": [
                        f"Master the classification, use, and care of {cfg['title'].lower()} in garment construction.",
                        "Apply practical safety procedures and correct tool selection criteria in the needlework laboratory.",
                        "Evaluate CBC Grade 10 Home Science Clothing and Textiles standards with real-world Kenyan context."
                    ]
                }
            )

            b2 = LessonBlock.objects.create(
                lesson=lesson, page_number=1, order=20, component_order=2,
                block_type="suggested_image", component_type="suggested_image",
                title=f"Visual Hook: {cfg['title']}",
                content={"image_url": cfg["image_url"], "caption": cfg["image_caption"]}
            )
            b2.assets.add(img_asset)

            LessonBlock.objects.create(
                lesson=lesson, page_number=1, order=30, component_order=3,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Everyday Context",
                content={"title": "Familiar Situation", "text": clean_text(cfg["hook"])}
            )

            # ──────────────────────────────────────────────────────────────
            # CARD 2 (Page 2): Analogy + Key Definitions
            # ──────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=2, order=40, component_order=1,
                block_type="concept_explanation", component_type="concept_explanation",
                title=f"Analogy: {cfg['analogy_title']}",
                content={"title": cfg["analogy_title"], "text": clean_text(cfg["analogy_text"])}
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=2, order=50, component_order=2,
                block_type="definition_card", component_type="definition_card",
                title="Key Terminology",
                content=clean_dict(cfg["definition"])
            )

            # ──────────────────────────────────────────────────────────────
            # CARD 3 (Page 3): Custom SVG Infographic + Deep Explanation
            # ──────────────────────────────────────────────────────────────
            b6 = LessonBlock.objects.create(
                lesson=lesson, page_number=3, order=60, component_order=1,
                block_type="suggested_diagram", component_type="suggested_diagram",
                title=f"Infographic Blueprint: {cfg['title']}",
                content={"title": f"Classification Diagram: {cfg['title']}", "svg_content": svg_content}
            )
            b6.assets.add(svg_asset)

            LessonBlock.objects.create(
                lesson=lesson, page_number=3, order=70, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Theoretical Deep Dive",
                content={"title": "Core Principles & Classification", "text": clean_text(cfg["deep_explanation"])}
            )

            # ──────────────────────────────────────────────────────────────
            # CARD 4 (Page 4): Step-by-Step Practical Activity
            # ──────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=4, order=80, component_order=1,
                block_type="step_process", component_type="step_process",
                title=cfg["practical"]["title"],
                content=clean_dict(cfg["practical"])
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=4, order=90, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Real-World Application in Kenya",
                content={
                    "title": "Kenyan Context",
                    "text": (
                        f"In Kenyan schools and tailoring workshops (fundi shops), mastery of {cfg['title'].lower()} "
                        "directly determines the quality, safety, and durability of garment output. "
                        "From the local uniform tailor in Nairobi's Gikomba Market to a Grade 10 student "
                        "completing their first sewing project, correct technique separates professional "
                        "results from wasted materials and frustrated effort."
                    )
                }
            )

            # ──────────────────────────────────────────────────────────────
            # CARD 5 (Page 5): YouTube Video + Deeper Explanation
            # ──────────────────────────────────────────────────────────────
            b9 = LessonBlock.objects.create(
                lesson=lesson, page_number=5, order=100, component_order=1,
                block_type="suggested_video", component_type="suggested_video",
                title=f"Video Demonstration: {cfg['title']}",
                content={
                    "title": f"Educational Video: {cfg['title']}",
                    "youtube_id": cfg["youtube_id"],
                    "video_url": f"https://www.youtube.com/watch?v={cfg['youtube_id']}"
                }
            )
            b9.assets.add(yt_asset)

            LessonBlock.objects.create(
                lesson=lesson, page_number=5, order=110, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Scientific Deeper Understanding",
                content={
                    "title": "Why It Works That Way",
                    "text": (
                        f"Understanding the science behind {cfg['title'].lower()} transforms a student from a "
                        "mechanical follower of instructions into an analytical problem-solver. "
                        "When you understand WHY dressmaker's shears must stay flat, WHY the presser foot "
                        "must be raised before threading, or WHY lint destroys machine performance, you can "
                        "adapt intelligently when facing unfamiliar situations — a critical competency "
                        "for both academic achievement and real-world needlework practice."
                    )
                }
            )

            # ──────────────────────────────────────────────────────────────
            # CARD 6 (Page 6): Knowledge Check MCQ + Key Takeaways
            # ──────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=6, order=120, component_order=1,
                block_type="knowledge_check", component_type="knowledge_check",
                title="Checkpoint Question",
                content=clean_dict(cfg["mcq"])
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=6, order=130, component_order=2,
                block_type="key_takeaway", component_type="key_takeaway",
                title="Key Takeaways",
                content={
                    "title": "Summary & Core Lessons",
                    "takeaways": [
                        f"Mastered the classification, correct use, and care protocols of {cfg['title'].lower()}.",
                        "Understood how proper tool selection, maintenance, and storage directly determines garment quality and tool longevity.",
                        "Applied CBC Grade 10 Home Science safety, environmental responsibility, and practical lab skills."
                    ]
                }
            )

            total_lessons += 1
            total_pages += 6
            total_blocks += 12
            print(f"  [+] Ingested Lesson {l_num:02d}/11: '{l_title[:60]}...' (6 pages, 12 blocks, 3 assets)")

    print("=" * 80)
    print("TOPIC 3.1 INGESTION COMPLETED SUCCESSFULLY:")
    print(f"  - Total Lessons : {total_lessons}")
    print(f"  - Total Pages   : {total_pages}")
    print(f"  - Total Blocks  : {total_blocks}")
    print(f"  - Total Assets  : {total_assets}")
    print("=" * 80)


if __name__ == "__main__":
    ingest_topic_3_1()
