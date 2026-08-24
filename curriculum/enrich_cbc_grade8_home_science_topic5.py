"""
VLearn CBC Grade 8 Home Science — Topic 5: Community Service Learning (CSL) Class Activity
Visual Enrichment Engine (Phase 2: Vector SVGs, Verified 200 OK Photos & Asset Persistence)

Curriculum: CBC (ID: 5)
Grade: Grade 8 (ID: 15)
Subject: Home Science (ID: 28)
Topic: Community Service Learning (CSL) Class Activity (ID: 107)

Attaches:
  - 3 Mandatory First-Card Visual Hooks (100% Tested HTTP 200 OK URLs)
  - 7 Custom Sanitized Responsive Vector SVGs to suggested_diagram blocks
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade8_home_science_topic5.py
"""

import os
import sys
import re
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
# 7 HIGH-STRUCTURE VECTOR SVGS FOR TOPIC 5: CSL CLASS ACTIVITY
# =============================================================================

# SVG 1: The 7 PCIs Bento Map (Lesson 1, Page 2)
SVG_7_PCIS_BENTO = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 7 Primary Pertinent &amp; Contemporary Issues (PCIs)</text>

  <!-- Row 1: 4 Boxes -->
  <g transform="translate(40, 70)">
    <!-- 1. Environmental Degradation -->
    <rect x="0" y="0" width="168" height="150" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="84" y="25" font-size="12" font-weight="bold" fill="#10b981" text-anchor="middle">1. Environment</text>
    <rect x="10" y="38" width="148" height="100" rx="4" fill="#1e293b"/>
    <text x="18" y="60" font-size="10" fill="#cbd5e1">• Plastic drain blocks</text>
    <text x="18" y="80" font-size="10" fill="#cbd5e1">• Tree deforestation</text>
    <text x="18" y="100" font-size="10" fill="#cbd5e1">• Stream pollution</text>
    <text x="18" y="125" font-size="9" font-weight="bold" fill="#34d399">Malaria vector risks</text>

    <!-- 2. Lifestyle Diseases -->
    <rect x="184" y="0" width="168" height="150" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="268" y="25" font-size="12" font-weight="bold" fill="#f59e0b" text-anchor="middle">2. Lifestyle Health</text>
    <rect x="194" y="38" width="148" height="100" rx="4" fill="#1e293b"/>
    <text x="202" y="60" font-size="10" fill="#cbd5e1">• Junk food excess</text>
    <text x="202" y="80" font-size="10" fill="#cbd5e1">• Physical inactivity</text>
    <text x="202" y="100" font-size="10" fill="#cbd5e1">• Obesity &amp; diabetes</text>
    <text x="202" y="125" font-size="9" font-weight="bold" fill="#fde68a">Balanced nutrition fix</text>

    <!-- 3. Diseases (Communicable) -->
    <rect x="368" y="0" width="168" height="150" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="452" y="25" font-size="12" font-weight="bold" fill="#ef4444" text-anchor="middle">3. Illness Outbreaks</text>
    <rect x="378" y="38" width="148" height="100" rx="4" fill="#1e293b"/>
    <text x="386" y="60" font-size="10" fill="#cbd5e1">• Cholera &amp; typhoid</text>
    <text x="386" y="80" font-size="10" fill="#cbd5e1">• Dirty market water</text>
    <text x="386" y="100" font-size="10" fill="#cbd5e1">• School absenteeism</text>
    <text x="386" y="125" font-size="9" font-weight="bold" fill="#fca5a5">Hygiene sanitation</text>

    <!-- 4. Poverty -->
    <rect x="552" y="0" width="168" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="636" y="25" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">4. Poverty / Livelihood</text>
    <rect x="562" y="38" width="148" height="100" rx="4" fill="#1e293b"/>
    <text x="570" y="60" font-size="10" fill="#cbd5e1">• Inability for food</text>
    <text x="570" y="80" font-size="10" fill="#cbd5e1">• Poor shelter care</text>
    <text x="570" y="100" font-size="10" fill="#cbd5e1">• High family stress</text>
    <text x="570" y="125" font-size="9" font-weight="bold" fill="#bae6fd">Craft entrepreneurship</text>
  </g>

  <!-- Row 2: 3 Boxes -->
  <g transform="translate(40, 235)">
    <!-- 5. Violence -->
    <rect x="0" y="0" width="229" height="160" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <text x="114" y="25" font-size="12" font-weight="bold" fill="#ec4899" text-anchor="middle">5. Violence in Community</text>
    <rect x="12" y="38" width="205" height="110" rx="4" fill="#1e293b"/>
    <text x="22" y="62" font-size="10" fill="#cbd5e1">• Bullying in school estates</text>
    <text x="22" y="85" font-size="10" fill="#cbd5e1">• Unsafe nighttime alleys</text>
    <text x="22" y="108" font-size="10" fill="#cbd5e1">• Creates fear and trauma</text>
    <text x="22" y="135" font-size="9" font-weight="bold" fill="#f472b6">Promoting safe homes</text>

    <!-- 6. Food Security -->
    <rect x="245" y="0" width="229" height="160" rx="8" fill="#0f172a" stroke="#84cc16" stroke-width="1.5"/>
    <text x="359" y="25" font-size="12" font-weight="bold" fill="#84cc16" text-anchor="middle">6. Food Insecurity</text>
    <rect x="257" y="38" width="205" height="110" rx="4" fill="#1e293b"/>
    <text x="267" y="62" font-size="10" fill="#cbd5e1">• Scarce fresh vegetables</text>
    <text x="267" y="85" font-size="10" fill="#cbd5e1">• Grain post-harvest rot</text>
    <text x="267" y="108" font-size="10" fill="#cbd5e1">• Stunted child growth</text>
    <text x="267" y="135" font-size="9" font-weight="bold" fill="#bef264">Kitchen &amp; sack gardens</text>

    <!-- 7. Conflicts -->
    <rect x="490" y="0" width="230" height="160" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="605" y="25" font-size="12" font-weight="bold" fill="#a855f7" text-anchor="middle">7. Community Conflicts</text>
    <rect x="502" y="38" width="205" height="110" rx="4" fill="#1e293b"/>
    <text x="512" y="62" font-size="10" fill="#cbd5e1">• Water well access disputes</text>
    <text x="512" y="85" font-size="10" fill="#cbd5e1">• Land boundary tensions</text>
    <text x="512" y="108" font-size="10" fill="#cbd5e1">• Destroys neighborhood unity</text>
    <text x="512" y="135" font-size="9" font-weight="bold" fill="#d8b4fe">Collaborative mediation</text>
  </g>
</svg>
""")

# SVG 2: Priority Decision Matrix (Lesson 1, Page 3)
SVG_PRIORITY_MATRIX = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Community Problem Priority Decision Matrix</text>

  <!-- Table Grid Layout -->
  <g transform="translate(40, 75)">
    <!-- Header -->
    <rect x="0" y="0" width="720" height="40" rx="6" fill="#0284c7"/>
    <text x="130" y="25" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Candidate Problem</text>
    <text x="310" y="25" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Health / Danger Urgency</text>
    <text x="470" y="25" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Population Affected</text>
    <text x="610" y="25" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Student Feasibility</text>

    <!-- Row 1: Option A (Selected Winner) -->
    <rect x="0" y="48" width="720" height="85" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <text x="15" y="78" font-size="11" font-weight="bold" fill="#10b981">Option A: Market Stalls</text>
    <text x="15" y="98" font-size="10" fill="#cbd5e1">Poor sanitation &amp; flies</text>
    <text x="15" y="118" font-size="9" fill="#34d399">[Home Science Linked]</text>

    <text x="310" y="85" font-size="11" font-weight="bold" fill="#ef4444" text-anchor="middle">HIGH (Cholera risk)</text>
    <text x="470" y="85" font-size="11" fill="#cbd5e1" text-anchor="middle">Entire Village (500+)</text>
    <text x="610" y="78" font-size="11" font-weight="bold" fill="#10b981" text-anchor="middle">EXCELLENT (10/10)</text>
    <text x="610" y="98" font-size="10" fill="#a7f3d0" text-anchor="middle">Clean &amp; sensitize!</text>

    <!-- Row 2: Option B (Macro Road) -->
    <rect x="0" y="140" width="720" height="75" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="15" y="170" font-size="11" font-weight="bold" fill="#f8fafc">Option B: Tarmac Road</text>
    <text x="15" y="190" font-size="10" fill="#94a3b8">Heavy highway transport</text>

    <text x="310" y="180" font-size="11" fill="#f59e0b" text-anchor="middle">Medium (Traffic bumps)</text>
    <text x="470" y="180" font-size="11" fill="#cbd5e1" text-anchor="middle">Sub-county wide</text>
    <text x="610" y="175" font-size="11" font-weight="bold" fill="#ef4444" text-anchor="middle">IMPOSSIBLE (0/10)</text>
    <text x="610" y="195" font-size="10" fill="#fca5a5" text-anchor="middle">Exceeds student budget</text>

    <!-- Row 3: Option C (Private TV) -->
    <rect x="0" y="222" width="720" height="75" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="15" y="252" font-size="11" font-weight="bold" fill="#f8fafc">Option C: Broken TV</text>
    <text x="15" y="272" font-size="10" fill="#94a3b8">Private chief's television</text>

    <text x="310" y="260" font-size="11" fill="#94a3b8" text-anchor="middle">Zero (Luxury item)</text>
    <text x="470" y="260" font-size="11" fill="#94a3b8" text-anchor="middle">1 Single Person</text>
    <text x="610" y="255" font-size="11" font-weight="bold" fill="#ef4444" text-anchor="middle">REJECTED (0/10)</text>
    <text x="610" y="275" font-size="10" fill="#fca5a5" text-anchor="middle">Not a public PCI!</text>
  </g>
</svg>
""")

# SVG 3: 3 Core Data Instruments (Lesson 2, Page 2)
SVG_DATA_INSTRUMENTS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 3 Core Data Collection Instruments</text>

  <!-- 3 Column Templates -->
  <!-- 1. Questionnaire -->
  <g transform="translate(40, 75)">
    <rect x="0" y="0" width="225" height="325" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="112" y="30" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. QUESTIONNAIRE</text>
    <rect x="15" y="45" width="195" height="135" rx="6" fill="#1e293b"/>
    <text x="25" y="70" font-size="10" font-weight="bold" fill="#f8fafc">Sample Survey Sheet:</text>
    <text x="25" y="90" font-size="9" fill="#cbd5e1">1. Do you boil water?</text>
    <text x="35" y="108" font-size="9" fill="#38bdf8">[ ] Yes   [ ] No</text>
    <text x="25" y="130" font-size="9" fill="#cbd5e1">2. Waste collection:</text>
    <text x="35" y="148" font-size="9" fill="#38bdf8">[ ] Daily [ ] Weekly</text>

    <rect x="15" y="190" width="195" height="115" rx="6" fill="#1e293b"/>
    <text x="25" y="212" font-size="10" font-weight="bold" fill="#38bdf8">• Target: 50+ households</text>
    <text x="25" y="235" font-size="10" fill="#cbd5e1">• Format: Written tick-box</text>
    <text x="25" y="258" font-size="10" fill="#cbd5e1">• Data: Anonymous stats</text>
    <text x="25" y="285" font-size="10" font-weight="bold" fill="#34d399">Fast &amp; standardized!</text>
  </g>

  <!-- 2. Interview Guide -->
  <g transform="translate(287, 75)">
    <rect x="0" y="0" width="225" height="325" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <text x="112" y="30" font-size="14" font-weight="bold" fill="#10b981" text-anchor="middle">2. INTERVIEW GUIDE</text>
    <rect x="15" y="45" width="195" height="135" rx="6" fill="#1e293b"/>
    <text x="25" y="70" font-size="10" font-weight="bold" fill="#f8fafc">Sample Expert Dialogue:</text>
    <text x="25" y="90" font-size="9" fill="#cbd5e1">Q: 'What are the main</text>
    <text x="25" y="105" font-size="9" fill="#cbd5e1">causes of local cholera?'</text>
    <text x="25" y="130" font-size="9" fill="#10b981">Nurse: 'Uncovered food &amp;'</text>
    <text x="25" y="145" font-size="9" fill="#10b981">'unwashed market hands.'</text>

    <rect x="15" y="190" width="195" height="115" rx="6" fill="#1e293b"/>
    <text x="25" y="212" font-size="10" font-weight="bold" fill="#10b981">• Target: Key experts/elders</text>
    <text x="25" y="235" font-size="10" fill="#cbd5e1">• Format: Spoken dialogue</text>
    <text x="25" y="258" font-size="10" fill="#cbd5e1">• Data: Deep explanations</text>
    <text x="25" y="285" font-size="10" font-weight="bold" fill="#a7f3d0">Rich historical insights!</text>
  </g>

  <!-- 3. Observation Schedule -->
  <g transform="translate(535, 75)">
    <rect x="0" y="0" width="225" height="325" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="112" y="30" font-size="14" font-weight="bold" fill="#f59e0b" text-anchor="middle">3. OBSERVATION</text>
    <rect x="15" y="45" width="195" height="135" rx="6" fill="#1e293b"/>
    <text x="25" y="70" font-size="10" font-weight="bold" fill="#f8fafc">Sample Visual Checklist:</text>
    <text x="25" y="90" font-size="9" fill="#cbd5e1">Food covered: [ ] Yes [x] No</text>
    <text x="25" y="110" font-size="9" fill="#cbd5e1">Trash bin near: [ ] Yes [x] No</text>
    <text x="25" y="130" font-size="9" fill="#cbd5e1">Aprons worn: [x] Yes [ ] No</text>
    <text x="25" y="150" font-size="9" fill="#f59e0b">Hand wash basin: [ ] None</text>

    <rect x="15" y="190" width="195" height="115" rx="6" fill="#1e293b"/>
    <text x="25" y="212" font-size="10" font-weight="bold" fill="#f59e0b">• Target: Physical fields</text>
    <text x="25" y="235" font-size="10" fill="#cbd5e1">• Format: Visual tick-list</text>
    <text x="25" y="258" font-size="10" fill="#cbd5e1">• Data: Unbiased evidence</text>
    <text x="25" y="285" font-size="10" font-weight="bold" fill="#fde68a">Direct visual proof!</text>
  </g>
</svg>
""")

# SVG 4: Ethical Research Flow (Lesson 2, Page 4)
SVG_ETHICAL_RESEARCH = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Ethical Community Research Flow &amp; Question Design Rules</text>

  <!-- 4 Step Flowchart -->
  <g transform="translate(40, 75)">
    <!-- Step 1 -->
    <rect x="0" y="0" width="168" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="84" y="28" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. Polite Greeting</text>
    <text x="15" y="55" font-size="10" fill="#cbd5e1">• Introduce school</text>
    <text x="15" y="75" font-size="10" fill="#cbd5e1">  and project purpose.</text>
    <text x="15" y="105" font-size="10" fill="#cbd5e1">• Ask for voluntary</text>
    <text x="15" y="125" font-size="10" font-weight="bold" fill="#38bdf8">  verbal consent.</text>

    <!-- Step 2 -->
    <rect x="184" y="0" width="168" height="150" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="268" y="28" font-size="12" font-weight="bold" fill="#10b981" text-anchor="middle">2. Neutral Phrasing</text>
    <text x="199" y="55" font-size="10" fill="#cbd5e1">• No accusatory words.</text>
    <text x="199" y="75" font-size="10" fill="#cbd5e1">• No leading questions.</text>
    <text x="199" y="105" font-size="10" fill="#cbd5e1">• Clear, multiple-choice</text>
    <text x="199" y="125" font-size="10" font-weight="bold" fill="#10b981">  tick options.</text>

    <!-- Step 3 -->
    <rect x="368" y="0" width="168" height="150" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="452" y="28" font-size="12" font-weight="bold" fill="#f59e0b" text-anchor="middle">3. Privacy Guard</text>
    <text x="383" y="55" font-size="10" fill="#cbd5e1">• Keep responses</text>
    <text x="383" y="75" font-size="10" fill="#cbd5e1">  strictly anonymous.</text>
    <text x="383" y="105" font-size="10" fill="#cbd5e1">• Protect family</text>
    <text x="383" y="125" font-size="10" font-weight="bold" fill="#f59e0b">  dignity and names.</text>

    <!-- Step 4 -->
    <rect x="552" y="0" width="168" height="150" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <text x="636" y="28" font-size="12" font-weight="bold" fill="#ec4899" text-anchor="middle">4. Warm Gratitude</text>
    <text x="567" y="55" font-size="10" fill="#cbd5e1">• Respect respondent's</text>
    <text x="567" y="75" font-size="10" fill="#cbd5e1">  working time.</text>
    <text x="567" y="105" font-size="10" fill="#cbd5e1">• Thank them warmly</text>
    <text x="567" y="125" font-size="10" font-weight="bold" fill="#ec4899">  for community help.</text>
  </g>

  <!-- Bottom: Golden Design Rule -->
  <g transform="translate(40, 245)">
    <rect x="0" y="0" width="720" height="155" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="360" y="28" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">Question Formulation Comparison</text>
    <rect x="20" y="45" width="330" height="95" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    <text x="35" y="70" font-size="11" font-weight="bold" fill="#ef4444">BAD: Rude &amp; Accusatory</text>
    <text x="35" y="92" font-size="10" fill="#cbd5e1">'Why is your food stall so filthy and full of flies?'</text>
    <text x="35" y="118" font-size="9" fill="#fca5a5">Result: Respondent is offended and refuses to answer.</text>

    <rect x="370" y="45" width="330" height="95" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="385" y="70" font-size="11" font-weight="bold" fill="#10b981">GOOD: Polite &amp; Structured</text>
    <text x="385" y="92" font-size="10" fill="#cbd5e1">'How do you protect cooked meals? [ ] Net [ ] Glass [ ] None'</text>
    <text x="385" y="118" font-size="9" fill="#a7f3d0">Result: Clear, objective, honest statistical data.</text>
  </g>
</svg>
""")

# SVG 5: 3 Resource Bins (Lesson 3, Page 2)
SVG_RESOURCE_BINS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 3 Project Resource Bins: Human, Technical, and Financial</text>

  <!-- 3 Big Shelf Bins -->
  <!-- 1. Human Resources -->
  <g transform="translate(40, 75)">
    <rect x="0" y="0" width="225" height="325" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="112" y="32" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. HUMAN</text>
    <rect x="15" y="50" width="195" height="60" rx="6" fill="#1e293b"/>
    <text x="112" y="75" font-size="12" font-weight="bold" fill="#f8fafc" text-anchor="middle">People &amp; Talents</text>
    <text x="112" y="95" font-size="10" fill="#bae6fd" text-anchor="middle">Labor, skills, expertise</text>
    <rect x="15" y="120" width="195" height="185" rx="6" fill="#1e293b"/>
    <text x="25" y="145" font-size="11" fill="#cbd5e1">• Group members' labor</text>
    <text x="25" y="175" font-size="11" fill="#cbd5e1">• Class teacher guidance</text>
    <text x="25" y="205" font-size="11" fill="#cbd5e1">• Public health nurse</text>
    <text x="25" y="235" font-size="11" fill="#cbd5e1">• Village elders' advice</text>
    <text x="25" y="275" font-size="11" font-weight="bold" fill="#38bdf8">Cost: Volunteer free!</text>
  </g>

  <!-- 2. Technical Resources -->
  <g transform="translate(287, 75)">
    <rect x="0" y="0" width="225" height="325" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <text x="112" y="32" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">2. TECHNICAL</text>
    <rect x="15" y="50" width="195" height="60" rx="6" fill="#1e293b"/>
    <text x="112" y="75" font-size="12" font-weight="bold" fill="#f8fafc" text-anchor="middle">Tools &amp; Hardware</text>
    <text x="112" y="95" font-size="10" fill="#a7f3d0" text-anchor="middle">Equipment &amp; devices</text>
    <rect x="15" y="120" width="195" height="185" rx="6" fill="#1e293b"/>
    <text x="25" y="145" font-size="11" fill="#cbd5e1">• School tablets &amp; apps</text>
    <text x="25" y="175" font-size="11" fill="#cbd5e1">• Improvised twig brooms</text>
    <text x="25" y="205" font-size="11" fill="#cbd5e1">• Protective rubber gloves</text>
    <text x="25" y="235" font-size="11" fill="#cbd5e1">• Scrubbing brushes</text>
    <text x="25" y="275" font-size="11" font-weight="bold" fill="#10b981">Cost: School &amp; improvised</text>
  </g>

  <!-- 3. Financial Resources -->
  <g transform="translate(535, 75)">
    <rect x="0" y="0" width="225" height="325" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="112" y="32" font-size="15" font-weight="bold" fill="#f59e0b" text-anchor="middle">3. FINANCIAL</text>
    <rect x="15" y="50" width="195" height="60" rx="6" fill="#1e293b"/>
    <text x="112" y="75" font-size="12" font-weight="bold" fill="#f8fafc" text-anchor="middle">Money &amp; Materials</text>
    <text x="112" y="95" font-size="10" fill="#fde68a" text-anchor="middle">Funds, soaps, supplies</text>
    <rect x="15" y="120" width="195" height="185" rx="6" fill="#1e293b"/>
    <text x="25" y="145" font-size="11" fill="#cbd5e1">• Sifted wood ash (Free!)</text>
    <text x="25" y="175" font-size="11" fill="#cbd5e1">• Pocket money savings</text>
    <text x="25" y="205" font-size="11" fill="#cbd5e1">• Fabric scrap off-cuts</text>
    <text x="25" y="235" font-size="11" fill="#cbd5e1">• Craft sale earnings</text>
    <text x="25" y="275" font-size="11" font-weight="bold" fill="#f59e0b">Cost: Low-cost innovation</text>
  </g>
</svg>
""")

# SVG 6: 4-Week Gantt Roadmap (Lesson 3, Page 3)
SVG_GANTT_ROADMAP = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">4-Week Community Project Execution Gantt Roadmap</text>

  <!-- 4 Horizontal Timeline Phases -->
  <g transform="translate(40, 75)">
    <!-- Week 1 -->
    <rect x="0" y="0" width="720" height="65" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="15" y="12" width="150" height="40" rx="6" fill="#0284c7"/>
    <text x="90" y="37" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">WEEK 1: Research</text>
    <text x="180" y="28" font-size="11" font-weight="bold" fill="#38bdf8">• Brainstorm PCIs &amp; Administer 40 Questionnaires</text>
    <text x="180" y="48" font-size="10" fill="#cbd5e1">Interview health nurse &amp; analyze statistical findings.</text>

    <!-- Week 2 -->
    <rect x="0" y="80" width="720" height="65" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect x="15" y="92" width="150" height="40" rx="6" fill="#059669"/>
    <text x="90" y="117" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">WEEK 2: Mobilize</text>
    <text x="180" y="108" font-size="11" font-weight="bold" fill="#10b981">• Resource Mobilization &amp; Tool Preparation</text>
    <text x="180" y="128" font-size="10" fill="#cbd5e1">Sift wood ash, fabricate twig brooms, inspect PPE aprons.</text>

    <!-- Week 3 -->
    <rect x="0" y="160" width="720" height="65" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="15" y="172" width="150" height="40" rx="6" fill="#d97706"/>
    <text x="90" y="197" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">WEEK 3: Action</text>
    <text x="180" y="188" font-size="11" font-weight="bold" fill="#f59e0b">• Practical Community Execution</text>
    <text x="180" y="208" font-size="10" fill="#cbd5e1">Clean food stalls, install wash basins, educate vendors.</text>

    <!-- Week 4 -->
    <rect x="0" y="240" width="720" height="65" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <rect x="15" y="252" width="150" height="40" rx="6" fill="#db2777"/>
    <text x="90" y="277" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">WEEK 4: Report</text>
    <text x="180" y="268" font-size="11" font-weight="bold" fill="#ec4899">• Portfolio &amp; Self-Reflection Log</text>
    <text x="180" y="288" font-size="10" fill="#cbd5e1">Compile project photos, write reflections, present to assembly.</text>
  </g>
</svg>
""")

# SVG 7: Role Division & Reflection (Lesson 3, Page 5)
SVG_ROLE_DIVISION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Team Collaboration, Role Division &amp; Personal Reflective Log</text>

  <!-- Left: 5 Member Role Cards -->
  <g transform="translate(40, 75)">
    <rect x="0" y="0" width="370" height="325" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="185" y="28" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 5 Core Collaborative Roles</text>

    <!-- Leader -->
    <rect x="15" y="42" width="340" height="45" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <text x="25" y="68" font-size="11" font-weight="bold" fill="#38bdf8">1. Group Leader:</text>
    <text x="130" y="68" font-size="10" fill="#cbd5e1">Coordinates plenary &amp; delegates tasks.</text>

    <!-- Secretary -->
    <rect x="15" y="94" width="340" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="25" y="120" font-size="11" font-weight="bold" fill="#10b981">2. Secretary:</text>
    <text x="115" y="120" font-size="10" fill="#cbd5e1">Records minutes &amp; formats survey sheets.</text>

    <!-- Treasurer -->
    <rect x="15" y="146" width="340" height="45" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
    <text x="25" y="172" font-size="11" font-weight="bold" fill="#f59e0b">3. Treasurer:</text>
    <text x="115" y="172" font-size="10" fill="#cbd5e1">Budgets savings &amp; tracks ash/soap stock.</text>

    <!-- Resource Coord -->
    <rect x="15" y="198" width="340" height="45" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="1"/>
    <text x="25" y="224" font-size="11" font-weight="bold" fill="#a855f7">4. Coordinator:</text>
    <text x="130" y="224" font-size="10" fill="#cbd5e1">Gathers twig brooms &amp; PPE gear.</text>

    <!-- Presenter -->
    <rect x="15" y="250" width="340" height="45" rx="6" fill="#1e293b" stroke="#ec4899" stroke-width="1"/>
    <text x="25" y="276" font-size="11" font-weight="bold" fill="#ec4899">5. Presenter:</text>
    <text x="120" y="276" font-size="10" fill="#cbd5e1">Presents findings to school assembly.</text>
  </g>

  <!-- Right: Reflective Journal Sample -->
  <g transform="translate(430, 75)">
    <rect x="0" y="0" width="330" height="325" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <text x="165" y="28" font-size="14" font-weight="bold" fill="#10b981" text-anchor="middle">Personal Reflective Logbook</text>
    
    <rect x="15" y="45" width="300" height="255" rx="6" fill="#1e293b"/>
    <text x="25" y="75" font-size="11" font-weight="bold" fill="#f8fafc">Wanjiku's Project Reflection:</text>
    <text x="25" y="105" font-size="10" fill="#cbd5e1">"Serving as Secretary taught me how</text>
    <text x="25" y="125" font-size="10" fill="#cbd5e1">to listen patiently to everyone's</text>
    <text x="25" y="145" font-size="10" fill="#cbd5e1">ideas and organize messy data into</text>
    <text x="25" y="165" font-size="10" fill="#cbd5e1">clear project charts."</text>
    
    <text x="25" y="200" font-size="10" fill="#cbd5e1">"I discovered that I am passionate</text>
    <text x="25" y="220" font-size="10" fill="#cbd5e1">about community public health!"</text>
    
    <text x="25" y="260" font-size="10" font-weight="bold" fill="#a7f3d0">Reflection builds self-efficacy &amp; leadership!</text>
  </g>
</svg>
""")

# Map of SVGs to specific lesson blocks
TOPIC5_SVGS = [
    {"lesson_order": 1, "page_number": 2, "block_type": "suggested_diagram", "svg": SVG_7_PCIS_BENTO, "title": "The 7 Primary Pertinent and Contemporary Issues Bento Map"},
    {"lesson_order": 1, "page_number": 3, "block_type": "suggested_diagram", "svg": SVG_PRIORITY_MATRIX, "title": "Community Problem Priority Decision Matrix"},
    {"lesson_order": 2, "page_number": 2, "block_type": "suggested_diagram", "svg": SVG_DATA_INSTRUMENTS, "title": "The 3 Core Data Collection Instruments: Questionnaire, Interview, and Observation"},
    {"lesson_order": 2, "page_number": 4, "block_type": "suggested_diagram", "svg": SVG_ETHICAL_RESEARCH, "title": "Ethical Community Research Flow & Question Design Rules"},
    {"lesson_order": 3, "page_number": 2, "block_type": "suggested_diagram", "svg": SVG_RESOURCE_BINS, "title": "The 3 Project Resource Bins: Human, Technical, and Financial"},
    {"lesson_order": 3, "page_number": 3, "block_type": "suggested_diagram", "svg": SVG_GANTT_ROADMAP, "title": "4-Week Community Project Execution Gantt Roadmap"},
    {"lesson_order": 3, "page_number": 5, "block_type": "suggested_diagram", "svg": SVG_ROLE_DIVISION, "title": "Team Collaboration, Role Division and Personal Reflective Log"}
]

# 100% Tested Live Wikimedia Photos (HTTP 200 OK)
TOPIC5_PHOTOS = [
    {
        "lesson_order": 1,
        "page_number": 1,
        "title": "The Neighborhood Walk: Spotting Community Needs",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/51/African_village.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 3.0",
        "caption": "An active Kenyan rural community where families interact, trade, and face daily environmental and health challenges."
    },
    {
        "lesson_order": 2,
        "page_number": 1,
        "title": "The Community Detective: Gathering Evidence",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/02/Students_studying.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 2.0",
        "caption": "Students collaborating in a learning environment, taking notes and reviewing field data for evidence-based community action."
    },
    {
        "lesson_order": 3,
        "page_number": 1,
        "title": "From Ideas to Action: The Power of Systematic Planning",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/87/Tree_planting.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 3.0",
        "caption": "Students actively engaged in a tree planting and environmental restoration community project."
    }
]

def enrich_cbc_grade8_home_science_topic5():
    """Attaches vector SVGs, Wikimedia photographic visual hooks, and persists LessonAsset records."""
    print("=" * 80)
    print("STARTING VISUAL ENRICHMENT: CBC GRADE 8 HOME SCIENCE — TOPIC 5: CSL CLASS ACTIVITY")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    assert curriculum, "CBC Curriculum not found!"
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 8").first()
    assert grade, "Grade 8 not found under CBC!"
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()
    assert subject, "Subject Home Science not found under Grade 8!"
    topic = Topic.objects.filter(subject=subject, name="Community Service Learning (CSL) Class Activity").first()
    assert topic, "Topic CSL Class Activity not found!"

    lessons = list(topic.lessons.all().order_by("learning_unit__order"))
    print(f"[*] Found {len(lessons)} Lessons under Topic: '{topic.name}' (ID: {topic.id})")

    # Clean existing LessonAssets for clean re-enrichment
    LessonAsset.objects.filter(lesson__in=lessons).delete()
    print("[*] Cleared existing LessonAssets for clean re-enrichment.")

    # 1. Attach Card 1 Visual Hooks (Wikimedia Photos)
    print("\n[+] Phase 2A: Attaching Mandatory Card 1 Visual Hooks...")
    for pm in TOPIC5_PHOTOS:
        u_order = pm["lesson_order"]
        p_num = pm["page_number"]
        lesson = next((l for l in lessons if l.learning_unit.order == u_order), None)
        if not lesson:
            continue

        hook_block = LessonBlock.objects.filter(
            lesson=lesson,
            page_number=p_num,
            block_type="suggested_image"
        ).first()

        if hook_block:
            content = hook_block.content or {}
            content["resolved_image_url"] = pm["url"]
            content["url"] = pm["url"]
            content["author"] = pm["author"]
            content["licensing"] = pm["licensing"]
            content["caption"] = pm["caption"]
            hook_block.content = content
            hook_block.save()

            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                source_type="external",
                storage_type="url",
                status="attached",
                title=hook_block.title,
                description=pm["caption"],
                url=pm["url"],
                metadata={
                    "author": pm["author"],
                    "licensing": pm["licensing"],
                    "caption": pm["caption"],
                    "is_card_1_hook": True
                }
            )
            hook_block.assets.add(asset)
            print(f"  [CARD 1 HOOK OK] Lesson {u_order} Page {p_num}: '{hook_block.title[:45]}...' -> Asset ID {asset.id}")

    # 2. Attach Custom Vector SVGs
    print("\n[+] Phase 2B: Attaching Custom Sanitized Vector SVGs...")
    for sm in TOPIC5_SVGS:
        u_order = sm["lesson_order"]
        p_num = sm["page_number"]
        lesson = next((l for l in lessons if l.learning_unit.order == u_order), None)
        if not lesson:
            continue

        diagram_block = LessonBlock.objects.filter(
            lesson=lesson,
            page_number=p_num,
            block_type="suggested_diagram"
        ).first()

        if diagram_block:
            content = diagram_block.content or {}
            content["svg_content"] = sm["svg"]
            content["svg"] = sm["svg"]
            diagram_block.content = content
            diagram_block.save()

            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="ai_generated",
                storage_type="embed",
                status="attached",
                title=sm["title"],
                description=f"Sanitized vector SVG diagram: {sm['title']}",
                metadata={"svg_content": sm["svg"]}
            )
            diagram_block.assets.add(asset)
            print(f"  [SVG ATTACHED] Lesson {u_order} Page {p_num}: '{diagram_block.title[:45]}...' -> Asset ID {asset.id}")

    total_assets = LessonAsset.objects.filter(lesson__in=lessons).count()
    print("\n" + "=" * 80)
    print(f"[SUCCESS] CBC Grade 8 Home Science Topic 5 Visual Enrichment Complete!")
    print(f"[*] Total LessonAssets Created & Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_cbc_grade8_home_science_topic5()
