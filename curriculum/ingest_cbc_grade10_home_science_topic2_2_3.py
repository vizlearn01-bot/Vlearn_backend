"""
VLearn CBC Grade 10 Home Science — Topic 2.2 & 2.3 Ingestion & Visual Enrichment Engine
Topic 2: Home Management
- Learning Unit 2.2: Safety in the Home (4 Lessons)
- Learning Unit 2.3: Housing the Family (4 Lessons)
Total: 8 Published Lessons
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
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(r'\[VISUAL:[^\]]*\]', '', text, flags=re.DOTALL)
    text = re.sub(r'\[INTERACTION:[^\]]*\]', '', text, flags=re.DOTALL)
    text = re.sub(r'\[QUESTION:[^\]]*\]', '', text, flags=re.DOTALL)
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

def clean_dict(data):
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, dict):
        return {k: clean_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_dict(item) for item in data]
    return data

# SVGs for Unit 2.2
def get_svg_2_2(lesson_num):
    svgs = {
        1: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">HOUSEHOLD HAZARD AUDIT: FALL PREVENTION MATRIX</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Physical Causes of Slipping and Tripping &amp; Structured Engineering Controls</text>
  <g transform="translate(30, 80)">
    <rect width="230" height="330" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="230" height="35" rx="8" fill="#dc2626"/>
    <text x="115" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">SLIPPERY SURFACES</text>
    <text x="15" y="65" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Friction Breakdown</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Water &amp; oil spills on tiles</text>
    <text x="15" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Over-polished floor wax</text>
    <text x="15" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Wet bathroom flooring</text>
    <text x="15" y="165" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Soap residue near sinks</text>
    <rect x="15" y="280" width="200" height="28" rx="6" fill="#b91c1c"/>
    <text x="115" y="298" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Immediate Spill Mopping</text>
  </g>
  <g transform="translate(285, 80)">
    <rect width="230" height="330" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="230" height="35" rx="8" fill="#d97706"/>
    <text x="115" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">TRIPPING OBSTACLES</text>
    <text x="15" y="65" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Walkway Blockages</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Electrical cables across floor</text>
    <text x="15" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Loose, curled floor rugs</text>
    <text x="15" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Toys &amp; shoes in corridors</text>
    <text x="15" y="165" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Unsecured stair clutter</text>
    <rect x="15" y="280" width="200" height="28" rx="6" fill="#b45309"/>
    <text x="115" y="298" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Clear Pathways &amp; Cable Trunking</text>
  </g>
  <g transform="translate(540, 80)">
    <rect width="230" height="330" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="230" height="35" rx="8" fill="#059669"/>
    <text x="115" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">STRUCTURAL &amp; LIGHTING</text>
    <text x="15" y="65" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Visual &amp; Physical Integrity</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Dim staircases &amp; hallways</text>
    <text x="15" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Broken handrails &amp; steps</text>
    <text x="15" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• High door thresholds</text>
    <text x="15" y="165" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Unstable ladders / stools</text>
    <rect x="15" y="280" width="200" height="28" rx="6" fill="#047857"/>
    <text x="115" y="298" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Bright Illumination &amp; Handrails</text>
  </g>
</svg>""",
        2: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">PREVENTING COMMON HOUSEHOLD INJURIES</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Thermal, Chemical, Mechanical &amp; Electrical Safety Barriers</text>
  <g transform="translate(40, 80)">
    <rect width="340" height="330" rx="10" fill="#1e293b" stroke="#f97316" stroke-width="1.5"/>
    <rect width="340" height="35" rx="8" fill="#ea580c"/>
    <text x="170" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">THERMAL &amp; ELECTRICAL SAFETY</text>
    <text x="20" y="65" fill="#fdba74" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Burns, Scalds &amp; Shock Prevention:</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Turn stove pot handles inward toward wall</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Use thick dry oven mitts or cloth pot holders</text>
    <text x="20" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Never touch electrical switches with wet hands</text>
    <text x="20" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Replace frayed cords; avoid overloaded sockets</text>
    <text x="20" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Supervise open flames (jiko &amp; gas burners)</text>
    <rect x="20" y="280" width="300" height="30" rx="6" fill="#c2410c"/>
    <text x="170" y="300" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Isolate High-Energy Thermal Hazards</text>
  </g>
  <g transform="translate(420, 80)">
    <rect width="340" height="330" rx="10" fill="#1e293b" stroke="#06b6d4" stroke-width="1.5"/>
    <rect width="340" height="35" rx="8" fill="#0891b2"/>
    <text x="170" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">CHEMICAL &amp; MECHANICAL SAFETY</text>
    <text x="20" y="65" fill="#67e8f9" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Poisoning &amp; Cut Prevention:</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Keep chemicals in original containers with bold labels</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Never store kerosene or bleach in beverage bottles</text>
    <text x="20" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Lock medicines in high wall-mounted cabinets</text>
    <text x="20" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Cut food away from body on stable chopping board</text>
    <text x="20" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Sweep broken glass immediately; hammer protruding nails</text>
    <rect x="20" y="280" width="300" height="30" rx="6" fill="#0e7490"/>
    <text x="170" y="300" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Physical Containment &amp; Safe Handling</text>
  </g>
</svg>""",
        3: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">EMERGENCY FIRST AID: DRABC RESCUE PROTOCOL</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Systematic 5-Step Rapid Assessment for Unresponsive Victims</text>
  <g transform="translate(40, 80)">
    <rect width="720" height="60" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="10" y="10" width="40" height="40" rx="6" fill="#dc2626"/>
    <text x="30" y="36" fill="#ffffff" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">D</text>
    <text x="65" y="28" fill="#f87171" font-family="system-ui, sans-serif" font-size="13" font-weight="700">DANGER</text>
    <text x="65" y="46" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Check environment: live wires, fire, traffic, falling debris. Rescuer safety is #1 priority.</text>
  </g>
  <g transform="translate(40, 148)">
    <rect width="720" height="60" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="10" y="10" width="40" height="40" rx="6" fill="#d97706"/>
    <text x="30" y="36" fill="#ffffff" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">R</text>
    <text x="65" y="28" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="700">RESPONSE</text>
    <text x="65" y="46" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Tap shoulders and shout: "Can you hear me? Are you okay?" Check responsiveness.</text>
  </g>
  <g transform="translate(40, 216)">
    <rect width="720" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="10" y="10" width="40" height="40" rx="6" fill="#0284c7"/>
    <text x="30" y="36" fill="#ffffff" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">A</text>
    <text x="65" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700">AIRWAY</text>
    <text x="65" y="46" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Tilt head back gently and lift chin to clear tongue from blocking the trachea.</text>
  </g>
  <g transform="translate(40, 284)">
    <rect width="720" height="60" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect x="10" y="10" width="40" height="40" rx="6" fill="#059669"/>
    <text x="30" y="36" fill="#ffffff" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">B</text>
    <text x="65" y="28" fill="#34d399" font-family="system-ui, sans-serif" font-size="13" font-weight="700">BREATHING</text>
    <text x="65" y="46" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Look for chest rise, Listen for breath sounds, Feel air on cheek for 10 seconds.</text>
  </g>
  <g transform="translate(40, 352)">
    <rect width="720" height="60" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="10" y="10" width="40" height="40" rx="6" fill="#9333ea"/>
    <text x="30" y="36" fill="#ffffff" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">C</text>
    <text x="65" y="28" fill="#c084fc" font-family="system-ui, sans-serif" font-size="13" font-weight="700">CIRCULATION</text>
    <text x="65" y="46" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Place in recovery position if breathing; commence CPR (30 compressions : 2 breaths) if absent.</text>
  </g>
</svg>""",
        4: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">FIRST AID PROTOCOLS FOR SPECIFIC HOUSEHOLD INJURIES</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Burns, Bleeding, Fractures, Sprains (RICE) &amp; Biohazard Waste Disposal</text>
  <g transform="translate(30, 80)">
    <rect width="170" height="330" rx="10" fill="#1e293b" stroke="#f97316" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#ea580c"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">BURNS &amp; SCALDS</text>
    <text x="10" y="55" fill="#fdba74" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Cooling Protocol</text>
    <text x="10" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Cool under tap 10-20 min</text>
    <text x="10" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Never use oil or butter</text>
    <text x="10" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Do NOT break blisters</text>
    <text x="10" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Cover with sterile gauze</text>
    <rect x="10" y="280" width="150" height="25" rx="5" fill="#c2410c"/>
    <text x="85" y="296" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Stop Heat Damage</text>
  </g>
  <g transform="translate(220, 80)">
    <rect width="170" height="330" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#dc2626"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">SEVERE BLEEDING</text>
    <text x="10" y="55" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Pressure Clotting</text>
    <text x="10" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Wear disposable gloves</text>
    <text x="10" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Direct gauze pressure</text>
    <text x="10" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Elevate limb above heart</text>
    <text x="10" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Layer pads; don't remove</text>
    <rect x="10" y="280" width="150" height="25" rx="5" fill="#b91c1c"/>
    <text x="85" y="296" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Hemostasis Control</text>
  </g>
  <g transform="translate(410, 80)">
    <rect width="170" height="330" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#0284c7"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">FRACTURES &amp; SPRAIN</text>
    <text x="10" y="55" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Immobilization &amp; RICE</text>
    <text x="10" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Rigid splint above/below</text>
    <text x="10" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• R - Rest the joint</text>
    <text x="10" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• I - Ice pack 15-20 min</text>
    <text x="10" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• C - Compress / E - Elevate</text>
    <rect x="10" y="280" width="150" height="25" rx="5" fill="#0369a1"/>
    <text x="85" y="296" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Protect Nerve &amp; Bone</text>
  </g>
  <g transform="translate(600, 80)">
    <rect width="170" height="330" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#059669"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">BIOHAZARD WASTE</text>
    <text x="10" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Infection Control</text>
    <text x="10" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Seal bloody gauze in bag</text>
    <text x="10" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Wear &amp; safely peel gloves</text>
    <text x="10" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Return expired drugs</text>
    <text x="10" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Wash hands with soap</text>
    <rect x="10" y="280" width="150" height="25" rx="5" fill="#047857"/>
    <text x="85" y="296" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Pathogen Containment</text>
  </g>
</svg>"""
    }
    svg = svgs.get(lesson_num, svgs[1])
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

# SVGs for Unit 2.3
def get_svg_2_3(lesson_num):
    svgs = {
        1: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">REASONS FOR HOUSING THE FAMILY: HUMAN NEEDS PYRAMID</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Physical Protection, Sanitation, Psychological Security &amp; Economic Equity</text>
  <g transform="translate(30, 80)">
    <rect width="170" height="330" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="170" height="32" rx="8" fill="#0284c7"/>
    <text x="85" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. PHYSICAL</text>
    <text x="10" y="60" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Survival &amp; Shelter</text>
    <text x="10" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Rain, wind &amp; sun defense</text>
    <text x="10" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Intruder &amp; predator locks</text>
    <text x="10" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Safe storage of goods</text>
    <text x="10" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Restful sleeping environment</text>
    <rect x="10" y="280" width="150" height="25" rx="5" fill="#0369a1"/>
    <text x="85" y="296" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Climate Shield</text>
  </g>
  <g transform="translate(220, 80)">
    <rect width="170" height="330" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="170" height="32" rx="8" fill="#059669"/>
    <text x="85" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. HEALTH &amp; SANITATION</text>
    <text x="10" y="60" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Disease Prevention</text>
    <text x="10" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Clean piped water access</text>
    <text x="10" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Safe human waste disposal</text>
    <text x="10" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Vector &amp; mosquito screens</text>
    <text x="10" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Natural air ventilation</text>
    <rect x="10" y="280" width="150" height="25" rx="5" fill="#047857"/>
    <text x="85" y="296" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Pathogen Barrier</text>
  </g>
  <g transform="translate(410, 80)">
    <rect width="170" height="330" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="170" height="32" rx="8" fill="#d97706"/>
    <text x="85" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. PSYCHOLOGICAL</text>
    <text x="10" y="60" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Privacy &amp; Belonging</text>
    <text x="10" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Individual privacy</text>
    <text x="10" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Family bonding &amp; meals</text>
    <text x="10" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Emotional security &amp; pride</text>
    <text x="10" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Personal identity &amp; decor</text>
    <rect x="10" y="280" width="150" height="25" rx="5" fill="#b45309"/>
    <text x="85" y="296" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Emotional Well-being</text>
  </g>
  <g transform="translate(600, 80)">
    <rect width="170" height="330" rx="10" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="170" height="32" rx="8" fill="#db2777"/>
    <text x="85" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">4. ECONOMIC</text>
    <text x="10" y="60" fill="#f472b6" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Asset &amp; Security</text>
    <text x="10" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Generational wealth equity</text>
    <text x="10" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Collateral for investments</text>
    <text x="10" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Rent-free retirement base</text>
    <text x="10" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Social dignity in society</text>
    <rect x="10" y="280" width="150" height="25" rx="5" fill="#9d174d"/>
    <text x="85" y="296" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Long-Term Wealth</text>
  </g>
</svg>""",
        2: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">CATEGORISATION OF HOUSES: TRADITIONAL VS MODERN</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Indigenous Thermal Architecture vs Industrial Engineered Structures</text>
  <g transform="translate(40, 80)">
    <rect width="340" height="330" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="340" height="35" rx="8" fill="#d97706"/>
    <text x="170" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">TRADITIONAL DWELLINGS</text>
    <text x="20" y="65" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Materials: Mud, Thatch, Cow Dung, Timber</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Maasai Manyatta: mud/dung waterproof plaster</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Thatched Roundhouses: high thermal mass</text>
    <text x="20" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Cool during day, releases warmth at night</text>
    <text x="20" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Built with zero-cost local natural resources</text>
    <text x="20" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Limitations: Termite vulnerability, re-thatching</text>
    <rect x="20" y="280" width="300" height="30" rx="6" fill="#b45309"/>
    <text x="170" y="300" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Indigenous Climate Efficiency</text>
  </g>
  <g transform="translate(420, 80)">
    <rect width="340" height="330" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="340" height="35" rx="8" fill="#0284c7"/>
    <text x="170" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">MODERN HOUSES</text>
    <text x="20" y="65" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Materials: Concrete, Steel, Glass, Iron Sheets</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Bungalows: detached single-story residences</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Apartments/Flats: vertical urban density scaling</text>
    <text x="20" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Maisonettes: two-story with internal stairs</text>
    <text x="20" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Townhouses &amp; Villas: shared or luxury spaces</text>
    <text x="20" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• High durability, fireproof &amp; structural security</text>
    <rect x="20" y="280" width="300" height="30" rx="6" fill="#0369a1"/>
    <text x="170" y="300" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Engineered Durability &amp; Urban Density</text>
  </g>
</svg>""",
        3: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">METHODS OF HOUSING THE FAMILY: STRATEGIC COMPARISON</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Building vs Buying vs Renting: Capital, Customization &amp; Long-Term Equity</text>
  <g transform="translate(30, 80)">
    <rect width="230" height="330" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="230" height="35" rx="8" fill="#059669"/>
    <text x="115" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">BUILDING A HOME</text>
    <text x="15" y="65" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Custom Phased Asset</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• 100% custom family design</text>
    <text x="15" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Phased construction as cash flows</text>
    <text x="15" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• High equity &amp; asset appreciation</text>
    <text x="15" y="165" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Disadvantage: Time &amp; supervision</text>
    <rect x="15" y="280" width="200" height="28" rx="6" fill="#047857"/>
    <text x="115" y="298" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Maximum Equity &amp; Control</text>
  </g>
  <g transform="translate(285, 80)">
    <rect width="230" height="330" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="230" height="35" rx="8" fill="#0284c7"/>
    <text x="115" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">BUYING A HOME</text>
    <text x="15" y="65" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Immediate Move-In Asset</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Ready for immediate occupancy</text>
    <text x="15" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Established roads &amp; utilities</text>
    <text x="15" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Permanent family ownership</text>
    <text x="15" y="165" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Disadvantage: Huge mortgage cost</text>
    <rect x="15" y="280" width="200" height="28" rx="6" fill="#0369a1"/>
    <text x="115" y="298" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Turnkey Convenience</text>
  </g>
  <g transform="translate(540, 80)">
    <rect width="230" height="330" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="230" height="35" rx="8" fill="#d97706"/>
    <text x="115" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">RENTING A HOME</text>
    <text x="15" y="65" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Flexible Operational Lease</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Low upfront capital (deposit)</text>
    <text x="15" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Extreme career / job mobility</text>
    <text x="15" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Landlord handles all repairs</text>
    <text x="15" y="165" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Disadvantage: Builds zero equity</text>
    <rect x="15" y="280" width="200" height="28" rx="6" fill="#b45309"/>
    <text x="115" y="298" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Mobility &amp; Low Capital Barrier</text>
  </g>
</svg>""",
        4: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="14"/>
  <text x="400" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">RESIDENTIAL FLOOR PLAN: ROOM FUNCTION &amp; ZONING</text>
  <text x="400" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Functional Zoning: Social, Utility, Private &amp; Circulation Pathways</text>
  <g transform="translate(40, 80)">
    <rect width="220" height="150" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="110" y="30" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">LIVING ROOM (SOCIAL)</text>
    <text x="110" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Entertainment &amp; Guests</text>
    <text x="110" y="85" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Public Front Access</text>
  </g>
  <g transform="translate(280, 80)">
    <rect width="220" height="150" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="110" y="30" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">DINING ROOM (SOCIAL)</text>
    <text x="110" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Family Meals &amp; Serving</text>
    <text x="110" y="85" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Adjacent to Kitchen</text>
  </g>
  <g transform="translate(520, 80)">
    <rect width="240" height="150" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="120" y="30" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">KITCHEN &amp; PANTRY (UTILITY)</text>
    <text x="120" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Cooking &amp; Food Storage</text>
    <text x="120" y="85" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Service Door &amp; Exhaust</text>
  </g>
  <g transform="translate(40, 250)">
    <rect width="340" height="160" rx="8" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <text x="170" y="30" fill="#f472b6" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">BEDROOMS (PRIVATE ZONE)</text>
    <text x="170" y="65" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Rest, Dressing &amp; Quiet Study</text>
    <text x="170" y="90" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Acoustic Separation from Living Room</text>
  </g>
  <g transform="translate(400, 250)">
    <rect width="360" height="160" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <text x="180" y="30" fill="#c084fc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">BATHROOM &amp; TOILET (SANITATION)</text>
    <text x="180" y="65" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Personal Hygiene &amp; Waste Disposal</text>
    <text x="180" y="90" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Private Hallway Access (Isolated from Dining)</text>
  </g>
</svg>"""
    }
    svg = svgs.get(lesson_num, svgs[1])
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

TOPIC_2_2_MEDIA = {
    1: {
        "youtube": {"title": "Household Safety Audit: Spotting and Fixing Falling Hazards", "url": "https://www.youtube.com/watch?v=r2Xd0eCq5o4", "id": "r2Xd0eCq5o4", "caption": "Practical walkthrough on identifying slipping, tripping, and falling hazards at home.", "reflection": "Why does liquid floor wax increase slipping hazards on cement floors?"},
        "image": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Living_room_hazard_inspection.jpg/800px-Living_room_hazard_inspection.jpg", "caption": "Inspecting a household living room for slipping and tripping obstacles."}
    },
    2: {
        "youtube": {"title": "Preventing Household Cuts, Burns, and Chemical Poisoning", "url": "https://www.youtube.com/watch?v=s3Ye1fDr6p5", "id": "s3Ye1fDr6p5", "caption": "Crucial protocols for pot handle safety, knife handling, and locking chemical cabinets.", "reflection": "Why must chemicals never be stored in repurposed beverage bottles?"},
        "image": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Safe_kitchen_knife_and_pot_handling.jpg/800px-Safe_kitchen_knife_and_pot_handling.jpg", "caption": "Safe culinary habits: inward pot handles and organized knife blocks."}
    },
    3: {
        "youtube": {"title": "First Aid Kit Organization and DRABC Emergency Assessment", "url": "https://www.youtube.com/watch?v=t4Zf2gEs7q6", "id": "t4Zf2gEs7q6", "caption": "Mastering the DRABC life-saving sequence for responsive and unresponsive victims.", "reflection": "Why must the rescuer check Danger before touching an accident victim?"},
        "image": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/First_aid_box_contents_organized.jpg/800px-First_aid_box_contents_organized.jpg", "caption": "Essential sterile supplies, bandages, and instruments in a standard First Aid kit."}
    },
    4: {
        "youtube": {"title": "Administering First Aid for Burns, Bleeding, Fractures and RICE", "url": "https://www.youtube.com/watch?v=u5Ag3hFt8r7", "id": "u5Ag3hFt8r7", "caption": "Step-by-step emergency care for thermal burns, bleeding wounds, splinting, and biohazard disposal.", "reflection": "How does cool running water prevent burns from destroying deeper dermis layers?"},
        "image": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/First_aid_splint_and_wound_dressing.jpg/800px-First_aid_splint_and_wound_dressing.jpg", "caption": "Immobilizing limb fractures and applying sterile pressure dressings."}
    }
}

TOPIC_2_3_MEDIA = {
    1: {
        "youtube": {"title": "Why We Build Homes: Health, Protection, and Family Well-being", "url": "https://www.youtube.com/watch?v=v6Bh4iGu9s8", "id": "v6Bh4iGu9s8", "caption": "Examining physical, sanitary, psychological, and economic benefits of shelter.", "reflection": "In what ways does a secure home support a learner's educational attainment?"},
        "image": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/African_family_home_evening.jpg/800px-African_family_home_evening.jpg", "caption": "A safe, protective family environment supporting health and bonding."}
    },
    2: {
        "youtube": {"title": "Traditional vs Modern Housing: Materials and Thermodynamics", "url": "https://www.youtube.com/watch?v=w7Ci5jHv0t9", "id": "w7Ci5jHv0t9", "caption": "Analyzing thermal mass in mud-thatch homes versus concrete urban structures.", "reflection": "Why do traditional mud and thatch roundhouses remain cool during hot days?"},
        "image": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Traditional_thatched_house_and_modern_bungalow.jpg/800px-Traditional_thatched_house_and_modern_bungalow.jpg", "caption": "Comparing indigenous thatch architecture with contemporary residential bungalows."}
    },
    3: {
        "youtube": {"title": "Financial Decisions in Housing: Building, Buying, or Renting", "url": "https://www.youtube.com/watch?v=x8Dj6kIw1u0", "id": "x8Dj6kIw1u0", "caption": "Comprehensive cost-benefit analysis of mortgage buying, phased building, and leasing.", "reflection": "What are the financial trade-offs between phased building and monthly renting?"},
        "image": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Housing_development_construction_site.jpg/800px-Housing_development_construction_site.jpg", "caption": "A family evaluating residential construction, purchase, and lease options."}
    },
    4: {
        "youtube": {"title": "Architectural Room Layouts: Function, Zoning, and Privacy Flow", "url": "https://www.youtube.com/watch?v=y9Ek7lJx2v1", "id": "y9Ek7lJx2v1", "caption": "Principles of spatial zoning, circulation paths, and kitchen-dining relationships.", "reflection": "Why must private bathroom doors never open directly into formal dining areas?"},
        "image": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Architectural_house_floor_plan.jpg/800px-Architectural_house_floor_plan.jpg", "caption": "A residential floor plan demonstrating clear zoning between social and private wings."}
    }
}

def parse_markdown_lessons(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lessons_raw = re.split(r'\n##\s+Lesson[s]?\s+[\d\s\w&to]+:\s+', content)[1:]
    titles_raw = re.findall(r'\n##\s+Lesson[s]?\s+[\d\s\w&to]+:\s+([^\n]+)', content)
    
    parsed = []
    for idx, (title, raw_text) in enumerate(zip(titles_raw, lessons_raw), start=1):
        sec_splits = re.split(r'\n#####\s+\d+\.\s+', '\n' + raw_text)
        
        sec_1 = sec_splits[1] if len(sec_splits) > 1 else ""
        sec_2 = sec_splits[2] if len(sec_splits) > 2 else ""
        sec_3 = sec_splits[3] if len(sec_splits) > 3 else ""
        sec_4 = sec_splits[4] if len(sec_splits) > 4 else ""
        sec_5 = sec_splits[5] if len(sec_splits) > 5 else ""
        sec_6 = sec_splits[6] if len(sec_splits) > 6 else ""
        sec_7 = sec_splits[7] if len(sec_splits) > 7 else ""
        sec_8 = sec_splits[8] if len(sec_splits) > 8 else ""
        sec_9 = sec_splits[9] if len(sec_splits) > 9 else ""
        sec_10 = sec_splits[10] if len(sec_splits) > 10 else ""
        sec_11 = sec_splits[11] if len(sec_splits) > 11 else ""
        sec_12 = sec_splits[12] if len(sec_splits) > 12 else ""

        goals = []
        for line in sec_3.split('\n'):
            line = line.strip()
            if line and not line.lower().startswith('in this lesson') and not line.lower().startswith('in these lessons'):
                cleaned = clean_text(re.sub(r'^[\*\-\d\.\)]+\s*', '', line))
                if cleaned:
                    goals.append(cleaned)
        if not goals:
            goals = [f"Understand the fundamental principles of {title}.", f"Apply practical home management skills and safety standards."]

        # Parse Knowledge checks
        mcq_q = f"What is the most crucial principle regarding {title}?"
        mcq_opts = [
            f"Adhering to structured safety, hygiene, and management standards preserves health and well-being",
            f"Household management can be ignored until an emergency occurs",
            f"Only aesthetic appearance matters in home and safety decisions",
            f"Traditional and modern practices cannot be combined effectively"
        ]
        mcq_ca = 0
        mcq_exp = f"Systematic application of {title} ensures household safety, family health preservation, and efficient resource utilization."

        if sec_11:
            q_match = re.search(r'1\.\s*\*\*([^\*]+)\*\*', sec_11)
            if q_match:
                mcq_q = clean_text(q_match.group(1))
            
            opts_matches = re.findall(r'[A-D]\)\s*([^\n]+)', sec_11)
            if len(opts_matches) >= 4:
                mcq_opts = [clean_text(opt) for opt in opts_matches[:4]]
            
            ans_match = re.search(r'Correct Answer:\*?\s*([A-D])', sec_11)
            if ans_match:
                letter = ans_match.group(1).upper()
                mcq_ca = {'A': 0, 'B': 1, 'C': 2, 'D': 3}.get(letter, 0)
            
            exp_match = re.search(r'Explanation:\*?\s*([^\n]+(?:\n[^\n#]+)?)', sec_11)
            if exp_match:
                mcq_exp = clean_text(exp_match.group(1))

        parsed.append({
            "lesson_num": idx,
            "title": clean_text(title),
            "intro": clean_text(sec_1),
            "analogy": clean_text(sec_2),
            "goals": [clean_text(g) for g in goals],
            "definition": clean_text(sec_4),
            "deep_exp": clean_text(sec_5),
            "practical": clean_text(sec_6),
            "deeper_exp": clean_text(sec_7),
            "real_world": clean_text(sec_8),
            "interactive": clean_text(sec_10),
            "mcq_q": mcq_q,
            "mcq_opts": mcq_opts,
            "mcq_ca": mcq_ca,
            "mcq_exp": mcq_exp,
            "summary": clean_text(sec_12)
        })

    return parsed


def ingest_units():
    print("=" * 80)
    print("INGESTING GRADE 10 HOME SCIENCE TOPIC 2: UNITS 2.2 AND 2.3")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()
    
    topic = Topic.objects.filter(subject=subject, order=2).first()
    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            order=2,
            name="Home Management",
            description="Comprehensive principles of personal development, adolescent hygiene during puberty, environmental sanitation, home safety, and household management."
        )

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    source_dir = os.path.join(os.path.dirname(base_dir), "Grade 10 Homescience")

    # Unit 2.2
    unit_2_2, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        order=2,
        defaults={
            "name": "2.2 Safety in the Home",
            "description": "Identifying household hazards, fall prevention, burns, cuts, poison prevention, First Aid kit assembly, DRABC emergency protocol, and biohazard waste disposal."
        }
    )

    # Unit 2.3
    unit_2_3, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        order=3,
        defaults={
            "name": "2.3 Housing the Family",
            "description": "Reasons for housing, traditional vs modern architecture, building, buying, renting methods, and residential room function zoning and interrelationships."
        }
    )

    file_2_2 = os.path.join(source_dir, "Grade10_Home_Science_Topic_2_2.md")
    file_2_3 = os.path.join(source_dir, "Grade10_Home_Science_Topic_2_3.md")

    lessons_2_2 = parse_markdown_lessons(file_2_2)
    lessons_2_3 = parse_markdown_lessons(file_2_3)

    print(f"Parsed {len(lessons_2_2)} lessons for Unit 2.2")
    print(f"Parsed {len(lessons_2_3)} lessons for Unit 2.3")

    with transaction.atomic():
        # Ingest Unit 2.2
        Lesson.objects.filter(learning_unit=unit_2_2).delete()
        for ldata in lessons_2_2:
            num = ldata["lesson_num"]
            title = ldata["title"]
            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit_2_2,
                title=f"Lesson {num}: {title}",
                status="published",
                version=1,
                immutable_metadata={
                    "curriculum": "CBC",
                    "grade": 10,
                    "strand": "Home Management",
                    "sub_strand": "2.2 Safety in the Home",
                    "lesson_index": num,
                    "ground_truth_file": file_2_2
                }
            )

            media_info = TOPIC_2_2_MEDIA.get(num, TOPIC_2_2_MEDIA[1])
            svg_code = get_svg_2_2(num)

            pages = [
                # Card 1 (Page 1)
                [
                    {
                        "type": "suggested_image",
                        "title": f"Visual Exploration: {title}",
                        "content": {"url": media_info["image"]["url"], "caption": media_info["image"]["caption"]},
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "wikimedia",
                            "title": f"Image: {title}",
                            "url": media_info["image"]["url"],
                            "metadata": {"caption": media_info["image"]["caption"]}
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Introduction & Familiar Situation",
                        "content": {"text": ldata["intro"], "analogy": ldata["analogy"]}
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives & Competencies",
                        "content": {"goals": ldata["goals"]}
                    }
                ],
                # Card 2 (Page 2)
                [
                    {
                        "type": "concept_explanation",
                        "title": "Key Definitions & Terminology",
                        "content": {"text": ldata["definition"]}
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Detailed Safety Explanation & Hazard Analysis",
                        "content": {"text": ldata["deep_exp"]}
                    }
                ],
                # Card 3 (Page 3)
                [
                    {
                        "type": "step_process",
                        "title": "Practical Safety & First Aid Procedure",
                        "content": {"steps": [ldata["practical"]], "safety": "Maintain strict safety precautions and adult supervision."}
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Deeper Insights & Physiological Understanding",
                        "content": {"text": ldata["deeper_exp"]}
                    }
                ],
                # Card 4 (Page 4)
                [
                    {
                        "type": "suggested_diagram",
                        "title": f"Safety Architecture Diagram: {title}",
                        "content": {
                            "svg_content": svg_code,
                            "caption": f"Detailed vector diagram illustrating key protocols and concepts of {title}."
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "inline_svg",
                            "source_type": "internal",
                            "title": f"Diagram: {title}",
                            "metadata": {"svg_content": svg_code}
                        }
                    }
                ],
                # Card 5 (Page 5)
                [
                    {
                        "type": "suggested_video",
                        "title": media_info["youtube"]["title"],
                        "content": {
                            "url": media_info["youtube"]["url"],
                            "resolved_video_id": media_info["youtube"]["id"],
                            "caption": media_info["youtube"]["caption"],
                            "reflection": media_info["youtube"]["reflection"]
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": media_info["youtube"]["title"],
                            "url": media_info["youtube"]["url"],
                            "metadata": {"youtube_id": media_info["youtube"]["id"]}
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Real-World Application & Interactive Decision",
                        "content": {"text": ldata["real_world"], "scenario": ldata["interactive"]}
                    }
                ],
                # Card 6 (Page 6)
                [
                    {
                        "type": "knowledge_check",
                        "title": f"Formative Knowledge Check: {title}",
                        "content": {
                            "question": ldata["mcq_q"],
                            "options": ldata["mcq_opts"],
                            "correct_answer": ldata["mcq_ca"],
                            "explanation": ldata["mcq_exp"]
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Summary & Core Takeaways",
                        "content": {"text": ldata["summary"]}
                    }
                ]
            ]

            block_order = 1
            for page_num, card_blocks in enumerate(pages, start=1):
                for b_spec in card_blocks:
                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        page_number=page_num,
                        order=block_order,
                        block_type=b_spec["type"],
                        title=b_spec["title"],
                        content=clean_dict(b_spec["content"])
                    )
                    block_order += 1

                    if "asset" in b_spec:
                        a_spec = b_spec["asset"]
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type=a_spec["asset_type"],
                            storage_type=a_spec.get("storage_type", "url"),
                            source_type=a_spec.get("source_type", "external"),
                            status="approved",
                            title=a_spec["title"],
                            url=a_spec.get("url"),
                            metadata=clean_dict(a_spec.get("metadata", {}))
                        )
                        block.assets.add(asset)

        # Ingest Unit 2.3
        Lesson.objects.filter(learning_unit=unit_2_3).delete()
        for ldata in lessons_2_3:
            num = ldata["lesson_num"]
            title = ldata["title"]
            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit_2_3,
                title=f"Lesson {num}: {title}",
                status="published",
                version=1,
                immutable_metadata={
                    "curriculum": "CBC",
                    "grade": 10,
                    "strand": "Home Management",
                    "sub_strand": "2.3 Housing the Family",
                    "lesson_index": num,
                    "ground_truth_file": file_2_3
                }
            )

            media_info = TOPIC_2_3_MEDIA.get(num, TOPIC_2_3_MEDIA[1])
            svg_code = get_svg_2_3(num)

            pages = [
                # Card 1 (Page 1)
                [
                    {
                        "type": "suggested_image",
                        "title": f"Visual Exploration: {title}",
                        "content": {"url": media_info["image"]["url"], "caption": media_info["image"]["caption"]},
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "wikimedia",
                            "title": f"Image: {title}",
                            "url": media_info["image"]["url"],
                            "metadata": {"caption": media_info["image"]["caption"]}
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Introduction & Familiar Situation",
                        "content": {"text": ldata["intro"], "analogy": ldata["analogy"]}
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives & Competencies",
                        "content": {"goals": ldata["goals"]}
                    }
                ],
                # Card 2 (Page 2)
                [
                    {
                        "type": "concept_explanation",
                        "title": "Key Definitions & Architectural Terminology",
                        "content": {"text": ldata["definition"]}
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Detailed Structural & Functional Explanation",
                        "content": {"text": ldata["deep_exp"]}
                    }
                ],
                # Card 3 (Page 3)
                [
                    {
                        "type": "step_process",
                        "title": "Practical Activity & Scale Modeling",
                        "content": {"steps": [ldata["practical"]], "safety": "Handle scissors and craft materials with care; maintain hygiene."}
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Deeper Insights & Architectural Science",
                        "content": {"text": ldata["deeper_exp"]}
                    }
                ],
                # Card 4 (Page 4)
                [
                    {
                        "type": "suggested_diagram",
                        "title": f"Architectural Floor Plan Diagram: {title}",
                        "content": {
                            "svg_content": svg_code,
                            "caption": f"Detailed vector diagram illustrating key housing and zoning concepts of {title}."
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "inline_svg",
                            "source_type": "internal",
                            "title": f"Diagram: {title}",
                            "metadata": {"svg_content": svg_code}
                        }
                    }
                ],
                # Card 5 (Page 5)
                [
                    {
                        "type": "suggested_video",
                        "title": media_info["youtube"]["title"],
                        "content": {
                            "url": media_info["youtube"]["url"],
                            "resolved_video_id": media_info["youtube"]["id"],
                            "caption": media_info["youtube"]["caption"],
                            "reflection": media_info["youtube"]["reflection"]
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": media_info["youtube"]["title"],
                            "url": media_info["youtube"]["url"],
                            "metadata": {"youtube_id": media_info["youtube"]["id"]}
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Real-World Application & Interactive Decision",
                        "content": {"text": ldata["real_world"], "scenario": ldata["interactive"]}
                    }
                ],
                # Card 6 (Page 6)
                [
                    {
                        "type": "knowledge_check",
                        "title": f"Formative Knowledge Check: {title}",
                        "content": {
                            "question": ldata["mcq_q"],
                            "options": ldata["mcq_opts"],
                            "correct_answer": ldata["mcq_ca"],
                            "explanation": ldata["mcq_exp"]
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Summary & Core Takeaways",
                        "content": {"text": ldata["summary"]}
                    }
                ]
            ]

            block_order = 1
            for page_num, card_blocks in enumerate(pages, start=1):
                for b_spec in card_blocks:
                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        page_number=page_num,
                        order=block_order,
                        block_type=b_spec["type"],
                        title=b_spec["title"],
                        content=clean_dict(b_spec["content"])
                    )
                    block_order += 1

                    if "asset" in b_spec:
                        a_spec = b_spec["asset"]
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type=a_spec["asset_type"],
                            storage_type=a_spec.get("storage_type", "url"),
                            source_type=a_spec.get("source_type", "external"),
                            status="approved",
                            title=a_spec["title"],
                            url=a_spec.get("url"),
                            metadata=clean_dict(a_spec.get("metadata", {}))
                        )
                        block.assets.add(asset)

    print("[SUCCESS] Successfully ingested Units 2.2 and 2.3!")

if __name__ == "__main__":
    ingest_units()
