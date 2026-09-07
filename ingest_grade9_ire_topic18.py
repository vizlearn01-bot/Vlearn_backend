"""
VLearn CBC Grade 9 IRE — Topic 18: History of Islam: Islam in Kenya
Production Ingestion and Enrichment Script for all 7 Lessons

Target Topic in DB: Topic ID 358 (Subject: IRE ID 53, Grade: Grade 9 ID 18)
Source Markdown: /home/jason-bitega/Desktop/VL/vlearn_repositories/Grade 9 IRE/islam-in-kenya.md

7 Lessons Ingested & Fully Enriched:
  1. Lesson 7.1.1: Geography and scope
  2. Lesson 7.1.2: Coast: spread and contact
  3. Lesson 7.1.3: Western Kenya
  4. Lesson 7.1.4: Central Kenya
  5. Lesson 7.1.5: North Eastern Kenya
  6. Lesson 7.1.6: Culture and civilisation
  7. Lesson 7.1.7: Synthesis: Islam and Kenyan development
"""

import os
import sys
import re
import xml.etree.ElementTree as ET
import django
from django.db import transaction

# Setup Django Environment
sys.path.append("/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)


def clean_text(text: str) -> str:
    """Removes bracket citations and internal pedagogical tags while preserving markdown."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(
        r'\[(VISUAL|QURAN REFERENCE|HADITH REFERENCE|BIBLE PASSAGE|BIBLE REFERENCE|CRITICAL THINKING|VALUES|'
        r'MISCONCEPTION|MISCONCEPTION CHECK|INTERACTION|ETHICAL SCENARIO|KEY VERSE|'
        r'REAL WORLD APPLICATION|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|REFLECTION|'
        r'COMPARISON TABLE|INFOGRAPHIC|SVG|DIAGRAM)[^\]]*\]',
        '',
        text,
        flags=re.IGNORECASE
    )
    text = re.sub(r'\[Source:[^\]]*\]', '', text, flags=re.IGNORECASE)
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    return text.strip()


# ─────────────────────────────────────────────────────────────────────────────
# 7 DEDICATED RESPONSIVE PEDAGOGICAL VECTOR SVGS (#0f172a theme, viewBox 880x440)
# ─────────────────────────────────────────────────────────────────────────────

def get_svg_lesson_1():
    """Lesson 7.1.1: The Four Geographic Pillars of Islam in Kenya"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg181" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg181)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE FOUR GEOGRAPHIC REGIONS OF ISLAM IN KENYA</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Debunking the Coastal Misconception: Islam as a National Kenyan Heritage Across 4 Historic Regions</text>

  <!-- Region 1: The Coast -->
  <g transform="translate(45, 85)">
    <rect width="185" height="290" rx="8" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <rect width="185" height="38" rx="8" fill="#0369a1"/>
    <text x="92" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">1. THE COAST</text>
    
    <circle cx="92" cy="72" r="22" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="92" y="78" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">8th C.</text>
    
    <text x="92" y="118" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Cradle of Swahili Islam</text>
    <text x="14" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="14" dy="0">• Lamu, Mombasa, Malindi</tspan>
      <tspan x="14" dy="18">• Indian Ocean Trade</tspan>
      <tspan x="14" dy="18">• Monsoon wind navigation</tspan>
      <tspan x="14" dy="18">• Intermarriage with Bantu</tspan>
      <tspan x="14" dy="18">• Birth of Kiswahili</tspan>
      <tspan x="14" dy="18">• Coral stone architecture</tspan>
    </text>
    <rect x="14" y="242" width="157" height="24" rx="4" fill="#0f172a"/>
    <text x="92" y="258" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Maritime Synthesis</text>
  </g>

  <!-- Region 2: Western Kenya -->
  <g transform="translate(245, 85)">
    <rect width="185" height="290" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="185" height="38" rx="8" fill="#047857"/>
    <text x="92" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">2. WESTERN KENYA</text>
    
    <circle cx="92" cy="72" r="22" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
    <text x="92" y="78" fill="#34d399" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">19th C.</text>
    
    <text x="92" y="118" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">The Wanga Kingdom</text>
    <text x="14" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="14" dy="0">• Mumias, Kakamega, Kisumu</tspan>
      <tspan x="14" dy="18">• Nabongo Mumia alliance</tspan>
      <tspan x="14" dy="18">• Influx of trade caravans</tspan>
      <tspan x="14" dy="18">• Royal conversion to Islam</tspan>
      <tspan x="14" dy="18">• Settled Nubian soldiers</tspan>
      <tspan x="14" dy="18">• Early inland literacy</tspan>
    </text>
    <rect x="14" y="242" width="157" height="24" rx="4" fill="#0f172a"/>
    <text x="92" y="258" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Royal Patronage</text>
  </g>

  <!-- Region 3: Central Kenya -->
  <g transform="translate(450, 85)">
    <rect width="185" height="290" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="185" height="38" rx="8" fill="#6b21a8"/>
    <text x="92" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">3. CENTRAL KENYA</text>
    
    <circle cx="92" cy="72" r="22" fill="#581c87" stroke="#a855f7" stroke-width="1.5"/>
    <text x="92" y="78" fill="#c084fc" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">1896+</text>
    
    <text x="92" y="118" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">The Railway Catalyst</text>
    <text x="14" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="14" dy="0">• Nairobi (Pumwani, Kibera)</tspan>
      <tspan x="14" dy="18">• Uganda Railway workers</tspan>
      <tspan x="14" dy="18">• Indian Muslim artisans</tspan>
      <tspan x="14" dy="18">• Swahili trade posts</tspan>
      <tspan x="14" dy="18">• Nyeri, Murang'a, Machakos</tspan>
      <tspan x="14" dy="18">• Urban Muslim hubs</tspan>
    </text>
    <rect x="14" y="242" width="157" height="24" rx="4" fill="#0f172a"/>
    <text x="92" y="258" fill="#c084fc" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Inland Infrastructure</text>
  </g>

  <!-- Region 4: North Eastern Kenya -->
  <g transform="translate(655, 85)">
    <rect width="185" height="290" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="185" height="38" rx="8" fill="#b45309"/>
    <text x="92" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">4. NORTH EASTERN</text>
    
    <circle cx="92" cy="72" r="22" fill="#78350f" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="92" y="78" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Pastoral</text>
    
    <text x="92" y="118" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Nomadic Scholarship</text>
    <text x="14" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="14" dy="0">• Garissa, Wajir, Mandera</tspan>
      <tspan x="14" dy="18">• Somali &amp; Oromo migrations</tspan>
      <tspan x="14" dy="18">• Camel caravan networks</tspan>
      <tspan x="14" dy="18">• Mobile Duksi tree schools</tspan>
      <tspan x="14" dy="18">• Quran memorization slates</tspan>
      <tspan x="14" dy="18">• Maslah dispute resolution</tspan>
    </text>
    <rect x="14" y="242" width="157" height="24" rx="4" fill="#0f172a"/>
    <text x="92" y="258" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Nomadic Resilience</text>
  </g>

  <!-- Footer -->
  <rect x="45" y="395" width="795" height="30" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="440" y="415" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">"We made you peoples and tribes that you may know one another." — Surah Al-Hujurat 49:13</text>
</svg>"""


def get_svg_lesson_2():
    """Lesson 7.1.2: The Coastal Indian Ocean Trade Network & Swahili Heritage Flow"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg182" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg182)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">COASTAL INDIAN OCEAN NETWORK &amp; SWAHILI GENESIS</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">The Synergy of Monsoon Winds, Peaceful Maritime Trade, and African-Bantu Cultural Synthesis</text>

  <!-- Step 1: Monsoon Winds -->
  <g transform="translate(45, 90)">
    <rect width="230" height="280" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="230" height="38" rx="8" fill="#0284c7"/>
    <text x="115" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. MONSOON WINDS</text>
    
    <text x="16" y="65" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600">The Maritime Bridge</text>
    <text x="16" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="16" dy="0">• Kaskazi (NE monsoon winds)</tspan>
      <tspan x="16" dy="18">  blew dhows from Arabia</tspan>
      <tspan x="16" dy="20">• Kusi (SE monsoon winds)</tspan>
      <tspan x="16" dy="18">  returned dhows months later</tspan>
      <tspan x="16" dy="20">• Forced long layovers</tspan>
      <tspan x="16" dy="18">  in Kenyan port towns</tspan>
      <tspan x="16" dy="20">• Peaceful merchant presence</tspan>
    </text>
    <rect x="16" y="235" width="198" height="26" rx="4" fill="#0f172a"/>
    <text x="115" y="252" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Predictable Seasonal Travel</text>
  </g>

  <!-- Step 2: Trade & Intermarriage -->
  <g transform="translate(325, 90)">
    <rect width="230" height="280" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="230" height="38" rx="8" fill="#059669"/>
    <text x="115" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. MARITIME COMMERCE</text>
    
    <text x="16" y="65" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600">Peaceful Social Integration</text>
    <text x="16" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="16" dy="0">• Traded spices, porcelain,</tspan>
      <tspan x="16" dy="18">  cloth, ivory &amp; timber</tspan>
      <tspan x="16" dy="20">• Arab &amp; Persian merchants</tspan>
      <tspan x="16" dy="18">  intermarried with local Bantu</tspan>
      <tspan x="16" dy="20">• Upright business ethics</tspan>
      <tspan x="16" dy="18">  attracted local communities</tspan>
      <tspan x="16" dy="20">• Zero military conquest</tspan>
    </text>
    <rect x="16" y="235" width="198" height="26" rx="4" fill="#0f172a"/>
    <text x="115" y="252" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Organic Assimilation</text>
  </g>

  <!-- Step 3: Swahili Civilisation -->
  <g transform="translate(605, 90)">
    <rect width="230" height="280" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="230" height="38" rx="8" fill="#b45309"/>
    <text x="115" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">3. SWAHILI SYNTHESIS</text>
    
    <text x="16" y="65" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600">The Birth of a Civilization</text>
    <text x="16" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="16" dy="0">• Kiswahili: Bantu grammar</tspan>
      <tspan x="16" dy="18">  with ~35% Arabic loanwords</tspan>
      <tspan x="16" dy="20">• Coral stone city-states</tspan>
      <tspan x="16" dy="18">  (Lamu, Mombasa, Gedi)</tspan>
      <tspan x="16" dy="20">• Carved geometric doors</tspan>
      <tspan x="16" dy="18">• Islamic law (Kadhi courts)</tspan>
      <tspan x="16" dy="20">• Lingua franca of East Africa</tspan>
    </text>
    <rect x="16" y="235" width="198" height="26" rx="4" fill="#0f172a"/>
    <text x="115" y="252" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">National Cultural Monument</text>
  </g>

  <!-- Footer -->
  <rect x="45" y="392" width="790" height="30" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="440" y="412" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Swahili culture: African in its Bantu roots, Islamic in its spiritual heart, cosmopolitan in trade.</text>
</svg>"""


def get_svg_lesson_3():
    """Lesson 7.1.3: Western Kenya Caravan Pathways & Nabongo Mumia's Alliance"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg183" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg183)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">WESTERN KENYA: THE WANGA KINGDOM &amp; NABONGO MUMIA</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Historical Chronicle of Royal Hospitality, Caravan Trade Alliances, and the Influx of Islam to Mumias</text>

  <!-- Timeline Cards -->
  <!-- 1870s: Caravans arrive -->
  <g transform="translate(45, 85)">
    <rect width="185" height="290" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="185" height="38" rx="8" fill="#0284c7"/>
    <text x="92" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1870s: CARAVANS</text>
    
    <circle cx="92" cy="72" r="22" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="92" y="78" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Trade</text>
    
    <text x="92" y="118" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Inland Expedition</text>
    <text x="14" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="14" dy="0">• Swahili-Arab traders</tspan>
      <tspan x="14" dy="18">  reach Wanga Kingdom</tspan>
      <tspan x="14" dy="18">• Sudi bin Ali &amp; Sheriff Juma</tspan>
      <tspan x="14" dy="18">• Welcomed by King</tspan>
      <tspan x="14" dy="18">  Nabongo Shiundu</tspan>
      <tspan x="14" dy="18">• Trading beads &amp; textiles</tspan>
    </text>
    <rect x="14" y="242" width="157" height="24" rx="4" fill="#0f172a"/>
    <text x="92" y="258" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">First Contact</text>
  </g>

  <!-- 1882: Mumia Ascends -->
  <g transform="translate(245, 85)">
    <rect width="185" height="290" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="185" height="38" rx="8" fill="#059669"/>
    <text x="92" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1882: NABONGO</text>
    
    <circle cx="92" cy="72" r="22" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
    <text x="92" y="78" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Mumia</text>
    
    <text x="92" y="118" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Visionary Leadership</text>
    <text x="14" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="14" dy="0">• Nabongo Mumia becomes King</tspan>
      <tspan x="14" dy="18">• Adopts Kanzu &amp; Kofia</tspan>
      <tspan x="14" dy="18">• Employs literate Muslim</tspan>
      <tspan x="14" dy="18">  scribes and advisors</tspan>
      <tspan x="14" dy="18">• Mumias becomes major</tspan>
      <tspan x="14" dy="18">  diplomatic capital</tspan>
    </text>
    <rect x="14" y="242" width="157" height="24" rx="4" fill="#0f172a"/>
    <text x="92" y="258" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Royal Alliance</text>
  </g>

  <!-- 1900s: Widespread Conversion -->
  <g transform="translate(450, 85)">
    <rect width="185" height="290" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="185" height="38" rx="8" fill="#b45309"/>
    <text x="92" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1900s: ISLAM</text>
    
    <circle cx="92" cy="72" r="22" fill="#78350f" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="92" y="78" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Faith</text>
    
    <text x="92" y="118" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Royal Conversion</text>
    <text x="14" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="14" dy="0">• Nabongo Mumia embraces Islam</tspan>
      <tspan x="14" dy="18">• Chiefs &amp; royal family follow</tspan>
      <tspan x="14" dy="18">• First mosques &amp; madrasas</tspan>
      <tspan x="14" dy="18">  built in Mumias</tspan>
      <tspan x="14" dy="18">• Literacy &amp; Arabic script</tspan>
      <tspan x="14" dy="18">  spread among Wanga</tspan>
    </text>
    <rect x="14" y="242" width="157" height="24" rx="4" fill="#0f172a"/>
    <text x="92" y="258" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Center of Western Islam</text>
  </g>

  <!-- 1910s+: Nubian Settlements -->
  <g transform="translate(655, 85)">
    <rect width="185" height="290" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="185" height="38" rx="8" fill="#6b21a8"/>
    <text x="92" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1910s+: NUBIANS</text>
    
    <circle cx="92" cy="72" r="22" fill="#581c87" stroke="#a855f7" stroke-width="1.5"/>
    <text x="92" y="78" fill="#c084fc" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Growth</text>
    
    <text x="92" y="118" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Inland Expansion</text>
    <text x="14" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="14" dy="0">• Retired Sudanese soldiers</tspan>
      <tspan x="14" dy="18">  (Nubians) settle in Kibos</tspan>
      <tspan x="14" dy="18">• Expansion to Kisumu,</tspan>
      <tspan x="14" dy="18">  Bungoma, &amp; Kakamega</tspan>
      <tspan x="14" dy="18">• Permanent community mosques</tspan>
      <tspan x="14" dy="18">• Enduring Islamic identity</tspan>
    </text>
    <rect x="14" y="242" width="157" height="24" rx="4" fill="#0f172a"/>
    <text x="92" y="258" fill="#c084fc" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Community Resilience</text>
  </g>

  <!-- Footer -->
  <rect x="45" y="395" width="795" height="30" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="440" y="415" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Nabongo Mumia's visionary alliance transformed Mumias into the heart of Islamic learning in Western Kenya.</text>
</svg>"""


def get_svg_lesson_4():
    """Lesson 7.1.4: Central Kenya & Railway Line Expansion"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg184" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg184)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">CENTRAL KENYA: THE UGANDA RAILWAY AS A CULTURAL CATALYST</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">The Spread of Islam into Nairobi, Nyeri, Murang'a and Machakos Along the 'Iron Snake' (1896–1901)</text>

  <!-- Train track line across middle -->
  <line x1="60" y1="120" x2="820" y2="120" stroke="#64748b" stroke-width="4"/>
  <line x1="60" y1="130" x2="820" y2="130" stroke="#64748b" stroke-width="4"/>
  <!-- Ties -->
  <path d="M70,115 L70,135 M120,115 L120,135 M170,115 L170,135 M220,115 L220,135 M270,115 L270,135 M320,115 L320,135 M370,115 L370,135 M420,115 L420,135 M470,115 L470,135 M520,115 L520,135 M570,115 L570,135 M620,115 L620,135 M670,115 L670,135 M720,115 L720,135 M770,115 L770,135 M810,115 L810,135" stroke="#475569" stroke-width="3"/>

  <!-- 3 Major Railway Station Nodes -->
  <!-- Station 1: Coast Origin -->
  <g transform="translate(60, 150)">
    <rect width="230" height="225" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="230" height="34" rx="8" fill="#0284c7"/>
    <text x="115" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">MOMBASA ORIGIN</text>
    <text x="15" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600">The Railway Construction Hub</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="15" dy="0">• Construction begins in 1896</tspan>
      <tspan x="15" dy="18">• Recruited 32,000 Indian laborers,</tspan>
      <tspan x="15" dy="18">  many of whom were Muslims</tspan>
      <tspan x="15" dy="18">• Swahili porters and traders</tspan>
      <tspan x="15" dy="18">• Transported food, supplies &amp; faith</tspan>
      <tspan x="15" dy="18">• Opened interior to coastal contact</tspan>
    </text>
    <rect x="15" y="185" width="200" height="24" rx="4" fill="#0f172a"/>
    <text x="115" y="201" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Gateway to the Interior</text>
  </g>

  <!-- Station 2: Nairobi Depot -->
  <g transform="translate(325, 150)">
    <rect width="230" height="225" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect width="230" height="34" rx="8" fill="#059669"/>
    <text x="115" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">NAIROBI URBAN DEPOT</text>
    <text x="15" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600">Kibera &amp; Pumwani Settlements</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="15" dy="0">• Kibera: Settled by Nubian soldiers</tspan>
      <tspan x="15" dy="18">• Pumwani: Swahili-Arab traders</tspan>
      <tspan x="15" dy="18">  &amp; early local converts</tspan>
      <tspan x="15" dy="18">• Pumwani Riyadh Mosque (1920s)</tspan>
      <tspan x="15" dy="18">• Jamia Mosque Nairobi established</tspan>
      <tspan x="15" dy="18">• Becomes national economic capital</tspan>
    </text>
    <rect x="15" y="185" width="200" height="24" rx="4" fill="#0f172a"/>
    <text x="115" y="201" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Historic Muslim Townships</text>
  </g>

  <!-- Station 3: Central Hinterlands -->
  <g transform="translate(590, 150)">
    <rect width="230" height="225" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="230" height="34" rx="8" fill="#b45309"/>
    <text x="115" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">CENTRAL TRADING HUBS</text>
    <text x="15" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600">Nyeri, Murang'a &amp; Machakos</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="15" dy="0">• Swahili trading posts established</tspan>
      <tspan x="15" dy="18">• Fair business practices attract</tspan>
      <tspan x="15" dy="18">  local Kikuyu and Kamba people</tspan>
      <tspan x="15" dy="18">• Local conversions to Islam</tspan>
      <tspan x="15" dy="18">• Permanent community madrasas</tspan>
      <tspan x="15" dy="18">• Harmonious commercial ties</tspan>
    </text>
    <rect x="15" y="185" width="200" height="24" rx="4" fill="#0f172a"/>
    <text x="115" y="201" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Peaceful Business Contact</text>
  </g>

  <!-- Footer -->
  <rect x="45" y="392" width="790" height="30" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="440" y="412" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">The railway track brought steel and trains, but workers and merchants brought faith, community, and brotherhood.</text>
</svg>"""


def get_svg_lesson_5():
    """Lesson 7.1.5: North Eastern Pastoralist Networks & Islamic Scholarship"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg185" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg185)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">NORTH EASTERN KENYA: PASTORALIST HERITAGE &amp; DUKSI SCHOOLS</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">The Nomadic Sanctuary of Quranic Memorization, Somali-Oromo Migrations &amp; Maslah Justice</text>

  <!-- 3 Core Pillars of North Eastern Islam -->
  <!-- Pillar 1: Duksi Tree School -->
  <g transform="translate(45, 85)">
    <rect width="235" height="290" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="235" height="42" rx="10" fill="#b45309"/>
    <text x="117" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13.5" font-weight="700" text-anchor="middle">THE DUKSI TREE SCHOOL</text>
    
    <text x="18" y="70" fill="#fde68a" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Mobile Nomadic Literacy</text>
    <text x="18" y="96" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="18" dy="0">• Conducted under acacia shade</tspan>
      <tspan x="18" dy="20">• Children write on wooden slates</tspan>
      <tspan x="18" dy="16">  (Looh) using charcoal ink</tspan>
      <tspan x="18" dy="20">• Full Quranic memorization (Hifz)</tspan>
      <tspan x="18" dy="20">• Teacher travels with camel herds</tspan>
      <tspan x="18" dy="20">• Requires zero expensive buildings</tspan>
    </text>
    <rect x="18" y="235" width="199" height="30" rx="6" fill="#0f172a"/>
    <text x="117" y="255" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Resilience &amp; Devotion</text>
  </g>

  <!-- Pillar 2: Pastoralist Migrations -->
  <g transform="translate(322, 85)">
    <rect width="235" height="290" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="235" height="42" rx="10" fill="#0284c7"/>
    <text x="117" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13.5" font-weight="700" text-anchor="middle">PASTORALIST MIGRATIONS</text>
    
    <text x="18" y="70" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Somali &amp; Oromo Heritage</text>
    <text x="18" y="96" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="18" dy="0">• Garissa, Wajir, Mandera, Marsabit</tspan>
      <tspan x="18" dy="20">• Entire clans migrated with Islam</tspan>
      <tspan x="18" dy="16">  as a complete way of life</tspan>
      <tspan x="18" dy="20">• Camel caravans connected the</tspan>
      <tspan x="18" dy="16">  interior to coastal ports</tspan>
      <tspan x="18" dy="20">• Deep oral poetry tradition</tspan>
    </text>
    <rect x="18" y="235" width="199" height="30" rx="6" fill="#0f172a"/>
    <text x="117" y="255" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Faith Across Vast Lands</text>
  </g>

  <!-- Pillar 3: Maslah Dispute Resolution -->
  <g transform="translate(595, 85)">
    <rect width="235" height="290" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="235" height="42" rx="10" fill="#059669"/>
    <text x="117" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13.5" font-weight="700" text-anchor="middle">MASLAH JUSTICE SYSTEM</text>
    
    <text x="18" y="70" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Customary-Shariah Synthesis</text>
    <text x="18" y="96" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="18" dy="0">• Shariah values integrated with</tspan>
      <tspan x="18" dy="16">  traditional pastoralist Xeer</tspan>
      <tspan x="18" dy="20">• Council of respected elders</tspan>
      <tspan x="18" dy="20">• Resolves grazing, water, &amp; clan</tspan>
      <tspan x="18" dy="16">  disputes peacefully</tspan>
      <tspan x="18" dy="20">• Prevents blood feuds</tspan>
    </text>
    <rect x="18" y="235" width="199" height="30" rx="6" fill="#0f172a"/>
    <text x="117" y="255" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Communal Reconciliation</text>
  </g>

  <!-- Footer -->
  <rect x="45" y="392" width="790" height="30" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="440" y="412" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Under the shade of the desert tree, generations memorized the Holy Qur'an on wooden slates.</text>
</svg>"""


def get_svg_lesson_6():
    """Lesson 7.1.6: Swahili-Islamic Cultural Synthesis (Bento Grid)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg186" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg186)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE MUSEUM OF KENYAN ISLAMIC MATERIAL HERITAGE</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Where Practical Utility, Artistic Beauty and Spiritual Values Merge in Daily Kenyan Life</text>

  <!-- Bento Grid: 4 Artifact Panels -->
  <!-- Panel 1: Kanzu & Kofia -->
  <g transform="translate(45, 80)">
    <rect width="380" height="135" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="45" cy="45" r="22" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="45" y="52" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">👔</text>
    <text x="80" y="38" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="700">The Kanzu &amp; Kofia (Dress &amp; Modesty)</text>
    <text x="80" y="56" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Traditional Robe &amp; Embroidered Cap</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="20" dy="0">• Ankle-length white tunic worn by men across East Africa</tspan>
      <tspan x="20" dy="18">• Represents dignity, modesty (Haya), and cleanliness</tspan>
      <tspan x="20" dy="18">• Paired with handcrafted embroidered Kofia for formal events</tspan>
    </text>
  </g>

  <!-- Panel 2: Swahili Carved Door -->
  <g transform="translate(455, 80)">
    <rect width="380" height="135" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <circle cx="45" cy="45" r="22" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
    <text x="45" y="52" fill="#10b981" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">🚪</text>
    <text x="80" y="38" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="700">The Carved Swahili Door (Architecture)</text>
    <text x="80" y="56" fill="#10b981" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Lamu &amp; Mombasa Stone Town Craftsmanship</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="20" dy="0">• Carved from local East African hardwood (Mvule)</tspan>
      <tspan x="20" dy="18">• Intricate Islamic geometric rosettes and lotus motifs</tspan>
      <tspan x="20" dy="18">• Symbolizes hospitality, protection, and social status</tspan>
    </text>
  </g>

  <!-- Panel 3: Dallah & Hospitality -->
  <g transform="translate(45, 230)">
    <rect width="380" height="135" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="45" cy="45" r="22" fill="#78350f" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="45" y="52" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">☕</text>
    <text x="80" y="38" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="700">The Dallah (Culinary Hospitality)</text>
    <text x="80" y="56" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Brass Coffee Pot &amp; Sweet Kahwa</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="20" dy="0">• Used to brew spiced coffee flavored with cardamom &amp; ginger</tspan>
      <tspan x="20" dy="18">• Served to welcoming guests alongside Halwa or dates</tspan>
      <tspan x="20" dy="18">• Emblematic of the sacred Islamic duty to honor visitors</tspan>
    </text>
  </g>

  <!-- Panel 4: Musalla & Leso -->
  <g transform="translate(455, 230)">
    <rect width="380" height="135" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <circle cx="45" cy="45" r="22" fill="#581c87" stroke="#a855f7" stroke-width="1.5"/>
    <text x="45" y="52" fill="#c084fc" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">📜</text>
    <text x="80" y="38" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="700">The Musalla &amp; Moral Leso / Khanga</text>
    <text x="80" y="56" fill="#c084fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Spiritual Cleanliness &amp; Moral Wisdom</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="20" dy="0">• Woven palm-leaf prayer mat creating pure prayer space</tspan>
      <tspan x="20" dy="18">• Colorful Leso fabrics bearing moral Swahili proverbs (Mji)</tspan>
      <tspan x="20" dy="18">• Blends everyday African attire with ethical social messages</tspan>
    </text>
  </g>

  <!-- Footer -->
  <rect x="45" y="380" width="790" height="32" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="440" y="401" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">"O children of Adam, We have bestowed upon you clothing to conceal your private parts and as adornment..." — Surah Al-A'raf 7:26</text>
</svg>"""


def get_svg_lesson_7():
    """Lesson 7.1.7: Master Historical Synthesis: The Four Streams Converging into Kenya"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg187" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="resGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="50%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg187)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE FOUR HISTORICAL STREAMS OF ISLAM IN KENYA</text>
  <text x="440" y="52" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Synthesizing Regional Heritage: How Four Tributaries Converge into Kenyan National Identity and Unity</text>

  <!-- 4 Regional Channels Feeding into Central Reservoir -->
  <!-- Stream 1: Coast -->
  <g transform="translate(45, 75)">
    <rect width="180" height="120" rx="8" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <rect width="180" height="26" rx="8" fill="#0369a1"/>
    <text x="90" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">COASTAL STREAM (8th C.)</text>
    <text x="12" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
      <tspan x="12" dy="0">• Indian Ocean trade routes</tspan>
      <tspan x="12" dy="16">• Swahili civilization &amp; towns</tspan>
      <tspan x="12" dy="16">• Kiswahili national language</tspan>
      <tspan x="12" dy="16">• Stone architecture &amp; arts</tspan>
    </text>
  </g>

  <!-- Stream 2: Western -->
  <g transform="translate(245, 75)">
    <rect width="180" height="120" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="180" height="26" rx="8" fill="#047857"/>
    <text x="90" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">WESTERN STREAM (19th C.)</text>
    <text x="12" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
      <tspan x="12" dy="0">• The Wanga Kingdom</tspan>
      <tspan x="12" dy="16">• King Nabongo Mumia alliance</tspan>
      <tspan x="12" dy="16">• Inland caravan literacy</tspan>
      <tspan x="12" dy="16">• Nubian veteran settlements</tspan>
    </text>
  </g>

  <!-- Stream 3: Central -->
  <g transform="translate(455, 75)">
    <rect width="180" height="120" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="180" height="26" rx="8" fill="#6b21a8"/>
    <text x="90" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">CENTRAL STREAM (1896+)</text>
    <text x="12" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
      <tspan x="12" dy="0">• Uganda Railway 'Iron Snake'</tspan>
      <tspan x="12" dy="16">• Pumwani &amp; Kibera townships</tspan>
      <tspan x="12" dy="16">• Indian &amp; Swahili workers</tspan>
      <tspan x="12" dy="16">• Urban civic development</tspan>
    </text>
  </g>

  <!-- Stream 4: North Eastern -->
  <g transform="translate(655, 75)">
    <rect width="180" height="120" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="180" height="26" rx="8" fill="#b45309"/>
    <text x="90" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">NORTH EASTERN STREAM</text>
    <text x="12" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
      <tspan x="12" dy="0">• Pastoralist Somali-Oromo</tspan>
      <tspan x="12" dy="16">• Mobile Duksi tree schools</tspan>
      <tspan x="12" dy="16">• Quranic slate memorization</tspan>
      <tspan x="12" dy="16">• Maslah community justice</tspan>
    </text>
  </g>

  <!-- Flow Arrows converging down -->
  <path d="M135,200 L300,225 M335,200 L380,225 M545,200 L500,225 M745,200 L580,225" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>

  <!-- Central Converged Reservoir: National Identity -->
  <g transform="translate(100, 230)">
    <rect width="680" height="135" rx="10" fill="url(#resGrad)" stroke="#38bdf8" stroke-width="2"/>
    <rect x="4" y="4" width="672" height="127" rx="8" fill="#0f172a"/>
    
    <text x="340" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">CONVERGENCE: MODERN KENYAN NATIONAL FLOURISHING &amp; UNITY</text>
    <text x="340" y="46" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Four distinct regional histories enriching Kenya's shared national fabric</text>

    <!-- 4 Fruit Badges -->
    <g transform="translate(25, 60)">
      <rect width="145" height="55" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="72" y="22" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">National Language</text>
      <text x="72" y="40" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Kiswahili Lingua Franca</text>
    </g>
    <g transform="translate(180, 60)">
      <rect width="145" height="55" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
      <text x="72" y="22" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Peace &amp; Cohesion</text>
      <text x="72" y="40" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Interfaith Harmony &amp; Maslah</text>
    </g>
    <g transform="translate(335, 60)">
      <rect width="145" height="55" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
      <text x="72" y="22" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Social Services</text>
      <text x="72" y="40" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Hospitals, Schools &amp; Waqf</text>
    </g>
    <g transform="translate(490, 60)">
      <rect width="145" height="55" rx="6" fill="#1e293b" stroke="#c084fc" stroke-width="1"/>
      <text x="72" y="22" fill="#c084fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Shared Culture</text>
      <text x="72" y="40" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Pilau, Kanzu, Arts &amp; Music</text>
    </g>
  </g>

  <!-- Footer Banner -->
  <rect x="100" y="385" width="680" height="30" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="440" y="405" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600" text-anchor="middle">Diverse in regional origins, united in faith, committed to the prosperity of Kenya.</text>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# LESSON DATA SPECIFICATION (7 Lessons, 7 Cards Each)
# ─────────────────────────────────────────────────────────────────────────────

TOPIC_18_LESSONS = [
    {
        "unit_order": 1,
        "lesson_title": "Geography and scope",
        "inquiry": "Where did Islam spread in Kenya, and what geographic regions form our national Islamic heritage?",
        "hook": "Imagine you are examining a giant tapestry of Kenya woven with thousands of vibrant threads. Some threads represent the white sand beaches of Mombasa, others represent the green hills of Kakamega, the busy avenues of Nairobi, and the vast arid savannahs of Garissa and Wajir. Each thread is distinctive, yet together they weave an indomitable national tapestry. In this lesson, we embark on a historical expedition across Kenya to locate the four primary geographic regions where Islam spread, discovering how this faith became an integral pillar of our Kenyan identity.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Kenya_relief_location_map.jpg/800px-Kenya_relief_location_map.jpg",
        "image_title": "Geographic Map of Kenya",
        "image_caption": "Physical relief map of Kenya highlighting the four historic regions where Islam took root: Coast, Western, Central, and North Eastern.",
        "concept_name": "The Four Geographic Pillars of Islam in Kenya",
        "concept_explanation": "Islam in Kenya is not confined to a single enclave or community; it is a nationwide heritage deeply established across four geographic regions: the Coast (maritime origins), Western Kenya (caravans and Wanga Kingdom), Central Kenya (railway expansion and urban townships), and North Eastern Kenya (nomadic pastoralist migrations). Its spread was peaceful, facilitated by trade, diplomacy, intermarriage, and shared values.",
        "scripture_quran": "O mankind, indeed We have created you from male and female and made you peoples and tribes that you may know one another...",
        "scripture_quran_ref": "Surah Al-Hujurat 49:13",
        "scripture_hadith": "The believers in their mutual kindness, compassion, and sympathy are just like one body...",
        "scripture_hadith_ref": "Sahih al-Bukhari 6011",
        "deep_explanation": "The national dispersion of Islam in Kenya encompasses four distinct regional historical channels:\n1. The Coast: The ancient cradle where Muslim traders arrived from the 8th century via the Indian Ocean trade network, producing the Swahili stone-town civilization.\n2. Western Kenya: Spread during the late 19th century via caravan routes, achieving historic momentum when King Nabongo Mumia of the Wanga Kingdom embraced Islam.\n3. Central Kenya: Spurred by the Uganda Railway construction (1896–1901), fostering permanent Muslim settlements in Nairobi (Pumwani, Kibera) and trading hubs in Nyeri and Machakos.\n4. North Eastern Kenya: Embraced through historical migrations of Somali and Oromo pastoralists, preserving faith through mobile Duksi schools and Maslah reconciliation councils.",
        "diagram_title": "The Four Geographic Regions of Islam in Kenya",
        "svg_func": get_svg_lesson_1,
        "table_title": "The Four Geographic Regions of Islam in Kenya",
        "table_headers": ["Region", "Time of Major Influx", "Primary Catalyst of Spread", "Key Historical Centers"],
        "table_rows": [
            ["Coast", "8th Century onwards", "Indian Ocean trade, monsoon winds & intermarriage", "Lamu, Mombasa, Malindi, Gedi"],
            ["Western Kenya", "Late 19th Century (1870s+)", "Swahili-Arab caravans & Nabongo Mumia's alliance", "Mumias, Kakamega, Kisumu, Bungoma"],
            ["Central Kenya", "Turn of 20th Century (1896+)", "Uganda Railway construction & urban depots", "Nairobi (Pumwani, Kibera), Nyeri, Machakos"],
            ["North Eastern", "Historical nomadic migrations", "Pastoralist clan movements & Duksi scholarship", "Garissa, Wajir, Mandera, Marsabit"]
        ],
        "scenario": "During a geography symposium, Yusuf remarks: 'I assumed Muslims in Kenya only live at the Coast, since that is where the oldest ruins are.' His classmate Halima replies: 'Yusuf, that is a very common misconception. While the Coast is historically the oldest, my grandparents are from Mumias in Western Kenya, which has had a vibrant Muslim royal heritage for over a century! We also have major Islamic populations in North Eastern counties like Garissa and Wajir, and in Nairobi. Islam is a nationwide Kenyan heritage, not merely a coastal one.'",
        "real_world": "Create a 'Regional Heritage Portfolio' in your IRE exercise book. Draw an outline map of Kenya and shade the four historic regions in distinct colors. Write down the name of at least one county and historical town in each region. Appreciating this nationwide geographic distribution reinforces national cohesion and mutual respect among Kenyan students.",
        "reflection": "How does recognizing Islam as a national Kenyan heritage help dismantle regional stereotypes and promote unity? Why did trade routes prove far more effective in spreading faith than military force?",
        "misconception": "Misconception: Assuming that Islam is an exclusively coastal religion in Kenya. Historical evidence proves that millions of Kenyan Muslims across Western, Central, and North Eastern Kenya have practiced and enriched the faith for generations.",
        "yt_id": "g5fD8_3vK2s",
        "yt_title": "Historical Geography of Islam in Kenya",
        "yt_desc": "Documentary overview of the four geographic regions of Kenya where Islam took root and flourished.",
        "mcq": {
            "question": "Which of the following represents the correct set of the four primary geographic regions where Islam spread and developed in Kenya?",
            "options": [
                "A. Coast, Western Kenya, Central Kenya, and North Eastern Kenya.",
                "B. Coast, Lake Victoria, Rift Valley, and Mount Kenya only.",
                "C. Nairobi, Kisumu, Nakuru, and Mombasa exclusively.",
                "D. Northern Coast, Southern Coast, Lamu Archipelago, and Malindi only."
            ],
            "answer": "A",
            "explanation": "The official KICD Junior School curriculum design designates these four primary geographic regions to trace the comprehensive history and spread of Islam in Kenya."
        },
        "summary_content": "Islam is an integral national heritage in Kenya, established across the Coast, Western, Central, and North Eastern regions. Its expansion occurred peacefully through trade routes, royal alliances, railway infrastructure, and pastoralist migrations.",
        "key_points": [
            "Islam is a nationwide Kenyan faith spanning four distinct geographic regions.",
            "The Coast was the earliest entry point via the 8th-century Indian Ocean trade.",
            "Western Kenya flourished through Nabongo Mumia; Central Kenya through the railway.",
            "North Eastern Kenya preserves a rich pastoralist heritage through Duksi schools."
        ],
        "exit_ticket": "List the four primary geographic regions where Islam spread in Kenya and name one town in each region."
    },
    {
        "unit_order": 2,
        "lesson_title": "Coast: spread and contact",
        "inquiry": "What factors led to the early spread of Islam at the Kenyan Coast, and what was the impact of cultural contact?",
        "hook": "Imagine an ancient, bustling seaport where wooden ships with massive triangular sails glide into the harbor. Merchants shout in Arabic, Persian, and Bantu tongues, trading fragrant spices, gold, porcelain, and timber. Through this vibrant trade, people are exchanging more than merchandise—they are sharing ideas, hospitality, and prayer. This is how Islam began along the Kenyan Coast over 1,200 years ago. In this lesson, we explore the early maritime contact between Muslim merchants and local coastal communities that gave birth to the Swahili civilization.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Lamu_Fort.jpg/800px-Lamu_Fort.jpg",
        "image_title": "Lamu Old Town UNESCO Heritage",
        "image_caption": "Historic Lamu Old Town showcasing traditional Swahili coral architecture, narrow stone streets, and enduring Islamic heritage.",
        "concept_name": "Indian Ocean Trade & the Genesis of Swahili Civilization",
        "concept_explanation": "Islam was introduced to the Kenyan Coast around the 8th century through the Indian Ocean maritime trade network, propelled by the predictable monsoon winds. Peaceful merchant contact, settlement, and intermarriage with local Bantu populations produced the Swahili civilization—characterized by the Kiswahili language, coral stone architecture, and autonomous island city-states.",
        "scripture_quran": "And We have certainly honored the children of Adam and carried them on land and sea...",
        "scripture_quran_ref": "Surah Al-Isra 17:70",
        "scripture_hadith": "The honest and trustworthy merchant will be with the prophets, the truthful, and the martyrs.",
        "scripture_hadith_ref": "Sunan at-Tirmidhi 1209",
        "deep_explanation": "The coastal expansion of Islam was shaped by four interrelated historical factors:\n1. The Monsoon Wind Engine: Predictable seasonal winds—the Kaskazi blowing southwest from Arabia and the Kusi blowing northeast—compelled foreign merchants to reside on the Kenyan coast for months, fostering peaceful integration.\n2. Intermarriage & Social Synthesis: Muslim traders married local Bantu women, giving rise to Swahili-speaking Muslim families who combined African cultural foundations with Islamic values.\n3. Emergence of Swahili City-States: Prosperous independent trading ports developed in Lamu, Mombasa, Pate, and Malindi, featuring coral stone mosques with carved mihrabs pointing toward Mecca.\n4. Birth of Kiswahili: The local Bantu language assimilated approximately 35% Arabic vocabulary, evolving into Kiswahili—the lingua franca of East Africa.",
        "diagram_title": "Coastal Indian Ocean Network & Swahili Genesis",
        "svg_func": get_svg_lesson_2,
        "table_title": "Key Catalysts of the Spread of Islam along the Kenyan Coast",
        "table_headers": ["Historical Factor", "Mechanism of Action", "Enduring Cultural / Religious Legacy"],
        "table_rows": [
            ["Monsoon Winds", "Seasonal Kaskazi & Kusi winds enabled maritime dhow navigation", "Established permanent trading settlements and ports"],
            ["Commerce & Ethics", "Fair trading in spices, timber, gold & ceramics", "Trustworthy merchant reputation attracted local conversions"],
            ["Intermarriage", "Marriages between Arab/Persian traders and Bantu women", "Emergence of the Swahili ethnic community and language"],
            ["Stone Architecture", "Construction of coral stone mosques, wells & houses", "UNESCO World Heritage sites in Lamu and Gedi ruins"]
        ],
        "scenario": "During an IRE heritage exhibition, Yusuf exhibits a scale model of an ancient carved Swahili door from Lamu. He explains: 'Observe the intricate floral and geometric rosettes carved into the timber. The wood is indigenous East African hardwood, the craftsmen were local Bantu-Swahili artisans, and the geometric motifs represent Islamic art. This door is physical proof that early coastal contact was not a violent conquest, but a peaceful cultural exchange that enriched both traditions.'",
        "real_world": "Explore the Arabic roots of Kenya's national language. Identify five common Kiswahili words derived from Arabic: Kitabu (from Kitab - book), Kalamu (from Qalam - pen), Wakati (from Waqt - time), Safari (from Safar - journey), and Habari (from Khabar - news). Write them in your notebook to celebrate how Kiswahili unites African roots with Islamic linguistic heritage.",
        "reflection": "How did the predictable monsoon winds act as a natural bridge connecting Kenya to the wider world? What lessons on peaceful coexistence can modern Kenyans draw from early coastal history?",
        "misconception": "Misconception: Believing that the Swahili people are foreign Arabs. Historical, linguistic, and archaeological research confirms that Swahili culture is fundamentally African Bantu in its linguistic grammar and people, enriched by Islamic faith and cosmopolitan Indian Ocean commerce.",
        "yt_id": "k8X2-V1q9Dw",
        "yt_title": "The Rise of the Swahili Civilization and Islam at the Coast",
        "yt_desc": "Historical overview of monsoon winds, dhow trade, Lamu, Mombasa, and the birth of Kiswahili.",
        "mcq": {
            "question": "What unique East African language and civilization developed along the Kenyan Coast as an organic synthesis of local African Bantu heritage and Islamic-Arab trade contact?",
            "options": [
                "A. Classical Arabic language and civilization.",
                "B. Swahili language and stone-town civilization.",
                "C. Nubian language and military culture.",
                "D. Cushitic pastoralist culture."
            ],
            "answer": "B",
            "explanation": "Peaceful trade, intermarriage, and daily interaction between Bantu coastal communities and Arab-Muslim traders gave birth to the Swahili language (Kiswahili) and its stone-town civilization."
        },
        "summary_content": "Islam reached the Kenyan Coast via the Indian Ocean trade around the 8th century, aided by monsoon winds. Peaceful interaction, fair business ethics, and intermarriage with Bantu communities created the Swahili civilization and the Kiswahili language.",
        "key_points": [
            "Indian Ocean trade and monsoon winds facilitated the arrival of Islam at the Coast.",
            "Contact was peaceful, commercial, and diplomatic, without military conquest.",
            "Intermarriage between Bantu women and Muslim merchants formed the Swahili people.",
            "Kiswahili developed as a vibrant Bantu language enriched with Arabic vocabulary."
        ],
        "exit_ticket": "State two major factors that facilitated the peaceful spread of Islam along the Kenyan Coast."
    },
    {
        "unit_order": 3,
        "lesson_title": "Western Kenya",
        "inquiry": "How did Islam spread to Western Kenya, and what role did local leaders play in its propagation?",
        "hook": "Imagine a powerful, respected African monarch presiding over a vast, prosperous kingdom. One day, a peaceful trade caravan arrives, led by merchants who pray in disciplined, shoulder-to-shoulder rows five times a day and maintain impeccable honesty in weighing goods. The monarch is so deeply impressed by their integrity, manners, and faith that he welcomes them into his royal court, adopts their attire, and eventually embraces their faith—ushering his kingdom into a new era of literacy and international commerce. This is the true history of how Islam took root in Western Kenya.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Nabongo_Mumia.jpg/800px-Nabongo_Mumia.jpg",
        "image_title": "King Nabongo Mumia of the Wanga Kingdom",
        "image_caption": "Historic portrait of King Nabongo Mumia, the visionary paramount chief of the Wanga Kingdom who embraced Islam and championed regional development.",
        "concept_name": "Nabongo Mumia & the Wanga Islamic Sanctuary",
        "concept_explanation": "Islam reached Western Kenya in the late 19th century through Swahili-Arab trade caravans entering the powerful Wanga Kingdom in Kakamega. King Nabongo Mumia formed a strategic alliance with Muslim merchants, adopted Islamic dress (the Kanzu and Kofia), and embraced Islam along with his royal court, transforming Mumias into the primary epicenter of Islamic propagation, literacy, and commerce in Western Kenya.",
        "scripture_quran": "...And say, 'My Lord, increase me in knowledge.'",
        "scripture_quran_ref": "Surah Ta-Ha 20:114",
        "scripture_hadith": "Whoever guides someone to goodness will have a reward like one who did it.",
        "scripture_hadith_ref": "Sahih Muslim 1893",
        "deep_explanation": "The history of Islam in Western Kenya unfolded through three transformative phases:\n1. Swahili-Arab Caravans (1870s): Traders such as Sudi bin Ali and Sheriff Juma journeyed from the coast to trade in ivory and textiles, establishing trading stations with the permission of King Nabongo Shiundu.\n2. The Visionary Alliance of Nabongo Mumia: Ascending the throne in 1882, King Mumia welcomed Muslim scholars and scribes, utilizing their literacy to organize administrative records. He adopted the Kanzu, embraced Islam, and appointed Muslim headmen across his realm.\n3. Nubian Veteran Settlements (1910s): Following colonial military service, Sudanese Muslim soldiers (Nubians) settled in Kibos (Kisumu), Bungoma, and Kakamega, constructing permanent community mosques and madrasas that reinforced the faith.",
        "diagram_title": "Western Kenya Caravan Pathways & Nabongo Mumia's Alliance",
        "svg_func": get_svg_lesson_3,
        "table_title": "Milestones of the Spread of Islam in Western Kenya",
        "table_headers": ["Time Period", "Key Historical Event", "Historical Significance for Islam in Western Kenya"],
        "table_rows": [
            ["1870s", "Caravans of Sudi bin Ali reach Wanga court", "First formal commercial and diplomatic contact with Swahili traders"],
            ["1882", "King Nabongo Mumia ascends the throne", "Alliance formed; adoption of Islamic dress and administrative literacy"],
            ["1900s", "Nabongo Mumia and chiefs embrace Islam", "Mumias established as the premier capital of Islamic propagation"],
            ["1910s+", "Settlement of Nubian veterans in Kibos & Kisumu", "Establishment of permanent urban mosques, madrasas, and communities"]
        ],
        "scenario": "Hussein conducts a research presentation on traditional African leadership. He notes: 'Some think traditional Kenyan kings resisted external ideas. But King Nabongo Mumia of the Wanga Kingdom was an extraordinary statesman. He recognized that Muslim traders possessed valuable skills in literacy, writing, and international diplomacy. By welcoming them and embracing Islam, he opened Western Kenya to the world, built schools, and established a peaceful, educated community that remains a proud pillar of Western Kenya's heritage today.'",
        "real_world": "Emulate the virtue of hospitality (Karam) practiced by Nabongo Mumia. When new students join your class or neighborhood—especially those from different cultural backgrounds—welcome them warmly, introduce them to friends, and assist them in adjusting. Genuine hospitality bridges cultural divides and fosters lasting peace.",
        "reflection": "How did King Nabongo Mumia's adoption of the Kanzu demonstrate cultural respect and leadership? What does the peaceful royal embrace of Islam in Western Kenya teach us about inter-community diplomacy?",
        "misconception": "Misconception: Assuming that Western Kenya was completely untouched by Islamic history until modern times. Historical records show that the Wanga Kingdom in Mumias was a major Islamic political and educational hub starting in the late 19th century.",
        "yt_id": "c1fD9_4xW2k",
        "yt_title": "The Wanga Kingdom and Nabongo Mumia's Islamic Legacy",
        "yt_desc": "Historical documentary detailing King Nabongo Mumia, the caravan routes, and the spread of Islam in Western Kenya.",
        "mcq": {
            "question": "Who was the renowned monarch (Nabongo) of the Wanga Kingdom whose royal alliance and conversion led to the flourishing of Islam in Western Kenya?",
            "options": [
                "A. Nabongo Shiundu",
                "B. Nabongo Mumia",
                "C. Sultan Seyyid Said",
                "D. King Lewanika"
            ],
            "answer": "B",
            "explanation": "King Nabongo Mumia was the visionary ruler of the Wanga Kingdom who welcomed coastal traders, adopted Islamic practices, and embraced Islam, making Mumias the heart of Islam in Western Kenya."
        },
        "summary_content": "Islam reached Western Kenya via 19th-century trade caravans entering the Wanga Kingdom. King Nabongo Mumia welcomed Muslim traders, embraced Islam, and made Mumias a vibrant center of Islamic learning, further strengthened by Nubian settlements in Kisumu and Bungoma.",
        "key_points": [
            "Swahili-Arab trade caravans reached the Wanga Kingdom in the 1870s.",
            "Nabongo Mumia embraced Islam, becoming its principal royal patron in Western Kenya.",
            "Mumias became the regional center for Islamic literacy, governance, and trade.",
            "Nubian Muslim veterans settled in Kisumu (Kibos) and Bungoma, establishing permanent mosques."
        ],
        "exit_ticket": "Describe the central role played by King Nabongo Mumia in propagating Islam in Western Kenya."
    },
    {
        "unit_order": 4,
        "lesson_title": "Central Kenya",
        "inquiry": "How did Islam spread to Central Kenya, and what was the impact of the Uganda Railway construction?",
        "hook": "Imagine thousands of railway workers and artisans from Kenya, India, and coastal towns laboring under scorching heat to lay an iron track across deep ravines, over raging rivers, and through wild savannahs. This iron track was the Uganda Railway—popularly dubbed the 'Iron Snake'—constructed over 125 years ago. Along with the heavy steel tracks, something else moved into the interior: diverse cultures, new languages, and Islamic faith. In this lesson, we uncover how the construction of this railway brought the first Muslim communities to Nairobi and Central Kenya.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Uganda_Railway_1899.jpg/800px-Uganda_Railway_1899.jpg",
        "image_title": "The Uganda Railway Construction (1899)",
        "image_caption": "Archival photograph of the Uganda Railway line under construction, linking Mombasa to the Kenyan interior and catalyzing inland settlements.",
        "concept_name": "The Uganda Railway & Urban Muslim Settlements in Central Kenya",
        "concept_explanation": "The construction of the Uganda Railway (1896–1901) was the primary catalyst for the inland migration and establishment of Muslim communities in Central Kenya. Indian Muslim artisans, Swahili rail workers, and Nubian soldiers established prayer tents along the route that evolved into historic mosques and vibrant urban Muslim settlements, particularly in Nairobi (Pumwani and Kibera), Nyeri, and Machakos.",
        "scripture_quran": "...And cooperate in righteousness and piety, but do not cooperate in sin and aggression...",
        "scripture_quran_ref": "Surah Al-Ma'idah 5:2",
        "scripture_hadith": "Verily, Allah loves that when any of you does a job, he performs it with excellence (itqan).",
        "scripture_hadith_ref": "Shu'ab al-Iman 4930",
        "deep_explanation": "The development of Islam in Central Kenya occurred across three major avenues:\n1. The Railway Labor Force: Over 32,000 workers were recruited, including thousands of Indian Muslim artisans (carpenters, blacksmiths, engineers) and Swahili porters who built prayer facilities at railway halts.\n2. Historic Nairobi Townships: As Nairobi expanded from a swampy rail depot into a city, dedicated Muslim settlements emerged. Kibera was allocated to retired Sudanese Nubian soldiers, while Pumwani developed as an indigenous Swahili-African township featuring Nairobi's first major mosques (such as the Pumwani Riyadh Mosque).\n3. Central Trading Posts: Coastal traders established shops in Machakos, Nyeri, and Murang'a (Fort Hall), introducing local Kikuyu and Kamba communities to Islam through fair commerce and ethical conduct.",
        "diagram_title": "Central Kenya & Railway Line Expansion",
        "svg_func": get_svg_lesson_4,
        "table_title": "Early Muslim Settlements and Hubs in Central Kenya",
        "table_headers": ["Settlement / Hub", "Founding Community", "Historic Contribution to Islam in Central Kenya"],
        "table_rows": [
            ["Kibera (Nairobi)", "Retired Sudanese Nubian soldiers", "Established early residential quarters, schools & community mosques"],
            ["Pumwani (Nairobi)", "Swahili-Arab traders & local converts", "Became Nairobi's premier Muslim cultural hub; Pumwani Riyadh Mosque"],
            ["Nairobi CBD", "Indian Muslim artisans & traders", "Founded Jamia Mosque Nairobi, Kenya's iconic national Islamic center"],
            ["Nyeri & Machakos", "Coastal caravan merchants & traders", "Introduced Islam to Kikuyu and Kamba communities through ethical trade"]
        ],
        "scenario": "During a historical excursion through Nairobi, Yusuf visits the historic Pumwani Riyadh Mosque. The imam explains: 'This mosque was founded in the early 20th century by hardworking Swahili rail workers, traders, and local Central Kenyan converts. Despite having very modest incomes, they pooled their shillings to erect this sanctuary for worship and education. It proves that Kenyan Muslims have been central to Nairobi's development since its foundation as a railway depot.'",
        "real_world": "Practice cooperative community service (Ta'awun). Just as early railway workers pooled their meager wages to build schools and prayer halls, collaborate with classmates to improve your school. Organize a study-group circle for struggling students, clean up the school grounds, or contribute books to your classroom library. Great institutions begin with collective cooperation.",
        "reflection": "How did the Uganda Railway transform Nairobi from a remote railway depot into a cosmopolitan center of diverse cultures? What does the history of Pumwani teach us about self-reliance in community development?",
        "misconception": "Misconception: Assuming that Nairobi's Muslim population is a recent development. In reality, Muslim communities in Pumwani, Kibera, and Ngara have been integral to Nairobi's urban fabric since the 1890s.",
        "yt_id": "m9G4-X1w8Lc",
        "yt_title": "The Uganda Railway and the History of Islam in Nairobi",
        "yt_desc": "Historical narrative exploring how the construction of the railway established Muslim communities in Kibera, Pumwani, and Central Kenya.",
        "mcq": {
            "question": "Which major national infrastructure project served as the primary catalyst for the inland spread of Islam and early Muslim settlements in Nairobi and Central Kenya?",
            "options": [
                "A. The construction of the Great North Road.",
                "B. The construction of the Uganda Railway (1896–1901).",
                "C. The expansion of the Kilindini Harbour.",
                "D. The development of the Masinga Hydroelectric Dam."
            ],
            "answer": "B",
            "explanation": "The Uganda Railway (1896–1901) brought thousands of Indian Muslim artisans, Swahili workers, and Nubian soldiers into the interior, leading to the establishment of early Muslim settlements in Nairobi (Pumwani, Kibera) and Central Kenya."
        },
        "summary_content": "The Uganda Railway was the principal catalyst for the expansion of Islam into Central Kenya. Indian Muslim artisans, Swahili workers, and Nubian soldiers established historic urban communities in Nairobi (Pumwani and Kibera), Nyeri, and Machakos.",
        "key_points": [
            "The Uganda Railway (1896–1901) brought thousands of Muslim artisans and workers inland.",
            "Nairobi's early Muslim communities formed in Kibera (Nubians) and Pumwani (Swahili).",
            "Jamia Mosque Nairobi and Pumwani Riyadh Mosque emerged as iconic institutional anchors.",
            "Trading posts in Nyeri and Machakos introduced Islam peacefully to local communities."
        ],
        "exit_ticket": "Name two early Muslim settlements in Nairobi and identify the historical communities that established them."
    },
    {
        "unit_order": 5,
        "lesson_title": "North Eastern Kenya",
        "inquiry": "How did Islam spread to North Eastern Kenya, and how did pastoralist migrations shape its heritage?",
        "hook": "Imagine an immense, golden savannah stretching toward the horizon under an expansive blue sky. Under the cooling shade of a thorn acacia tree, nomadic pastoralists rest beside their camels. As the evening sun dips, an elder consults a pocket compass, aligns the group toward Mecca, and leads the Maghrib prayer directly on the clean desert sand. Nearby, children sit in a circle, writing Quranic verses on wooden slates with charcoal ink. This nomadic resilience is the heart of North Eastern Kenya. In this lesson, we discover how Islam became the foundational way of life for the pastoralist communities of Garissa, Wajir, and Mandera.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Camels_in_Kenya.jpg/800px-Camels_in_Kenya.jpg",
        "image_title": "Camel Caravans of North Eastern Kenya",
        "image_caption": "Camels grazing in North Eastern Kenya, symbolizing the pastoralist lifestyle, trade caravan heritage, and mobile Islamic education.",
        "concept_name": "Pastoralist Migrations, Duksi Schools & Maslah Reconciliation",
        "concept_explanation": "Islam in North Eastern Kenya (Garissa, Wajir, Mandera, Marsabit) was integrated into the fabric of society through the historical migrations of Somali and Oromo pastoralist communities. Faith was preserved in nomadic environments through mobile Quranic tree schools (Duksi) using wooden slates (Looh), and community harmony was maintained through the Maslah dispute-resolution system which synthesized Shariah with customary law.",
        "scripture_quran": "And indeed, this Ummah of yours is one Ummah, and I am your Lord, so worship Me.",
        "scripture_quran_ref": "Surah Al-Anbiya 21:92",
        "scripture_hadith": "The best of you are those who learn the Qur'an and teach it.",
        "scripture_hadith_ref": "Sahih al-Bukhari 5027",
        "deep_explanation": "The Islamic heritage of North Eastern Kenya is distinguished by three unique hallmarks:\n1. Clan Migrations as Complete Lifestyle: Unlike regions where Islam spread via isolated trade posts, entire pastoralist clans moved across the Horn of Africa, carrying Islamic jurisprudence, worship, and social values as their total cultural identity.\n2. The Mobile Duksi System: Nomadic scholars accompanied herders, establishing tree-shaded open-air schools (Duksi) where children memorized the entire Qur'an on wooden slates (Looh) using homemade ink, demonstrating remarkable pedagogical adaptability.\n3. Maslah Conflict Resolution: Clan elders and Islamic scholars harmonized Shariah principles with traditional pastoralist customary codes (Xeer) to create Maslah—a community justice system that resolves land, water, and grazing disputes through restorative compensation and reconciliation.",
        "diagram_title": "North Eastern Pastoralist Networks & Islamic Scholarship",
        "svg_func": get_svg_lesson_5,
        "table_title": "Hallmarks of North Eastern Kenya's Islamic Heritage",
        "table_headers": ["Dimension", "Traditional Pastoralist Practice", "Integration with Islamic Heritage"],
        "table_rows": [
            ["Education", "Nomadic Duksi schools under acacia trees", "Memorization of Qur'an on wooden slates (Looh) with homemade ink"],
            ["Justice & Law", "Maslah elders' councils using customary Xeer", "Application of Shariah principles for peaceful dispute settlement"],
            ["Trade & Mobility", "Camel caravans across savannahs and semi-arid lands", "Maintained constant trade and scholarly links with coastal ports"],
            ["Social Values", "Strong clan solidarity and hospitality to travelers", "Fulfillment of Islamic brotherhood, charity, and guest honors"]
        ],
        "scenario": "During cultural heritage week, Halima shares a story about her grandfather's youth in Wajir: 'My grandfather did not attend a modern brick-and-mortar school. He studied in a mobile Duksi school under acacia trees. His teacher wrote verses on a wooden slate, which the boys memorized while watching their camels. When the rains moved, the teacher packed the slates onto a camel, and the school migrated with the herd. This heroic dedication enabled my grandfather to memorize the entire Qur'an by age twelve, proving that true love for knowledge transcends material hardship.'",
        "real_world": "Cultivate the pastoralist work ethic in your academic revision. If children in mobile Duksi schools successfully memorized the entire Qur'an under thorn trees without electricity, desks, or textbooks, value your educational opportunities. Minimize smartphone distractions, organize your study schedule diligently, and dedicate your full effort to mastering your school curriculum.",
        "reflection": "How does the mobile Duksi school demonstrate that education can adapt to any environment? How did the Maslah justice system maintain peace among pastoralist clans without formal police forces?",
        "misconception": "Misconception: Believing that nomadic pastoralists lacked formal education. The Duksi system is a highly rigorous, time-tested educational institution that produced exceptional scholars of Arabic, theology, and Qur'anic memorization.",
        "yt_id": "v7X2-K9w3Lc",
        "yt_title": "Duksi Schools and Islamic Heritage in North Eastern Kenya",
        "yt_desc": "Documentary exploring the mobile Duksi Quranic schools, camel caravans, and the Maslah justice system in Garissa and Wajir.",
        "mcq": {
            "question": "What is the traditional name for the mobile Quranic schools utilized by pastoralists in North Eastern Kenya to teach children Qur'an memorization on wooden slates under trees?",
            "options": [
                "A. Madrasa",
                "B. Duksi",
                "C. Halaqah",
                "D. Zawiyah"
            ],
            "answer": "B",
            "explanation": "Duksi is the traditional Somali term for the mobile, tree-shaded Quranic schools that travel alongside pastoralist herders, ensuring the continuous religious education of nomadic youth."
        },
        "summary_content": "Islam took root in North Eastern Kenya through Somali and Oromo pastoralist migrations. Mobile Duksi schools preserved Quranic literacy on wooden slates, while Maslah councils synthesized Shariah with customary law to ensure peaceful dispute resolution.",
        "key_points": [
            "Islam spread in North Eastern Kenya through pastoralist Somali and Oromo migrations.",
            "Duksi schools preserved Quranic memorization and literacy across nomadic communities.",
            "Wooden slates (Looh) and charcoal ink provided resilient, mobile learning materials.",
            "The Maslah system harmonized Shariah with customary law for peaceful conflict resolution."
        ],
        "exit_ticket": "Explain how the nomadic pastoralist lifestyle of North Eastern Kenya adapted its religious education system."
    },
    {
        "unit_order": 6,
        "lesson_title": "Culture and civilisation",
        "inquiry": "How did Islamic heritage contribute to the physical culture, architecture, dress, and arts of Kenya?",
        "hook": "Imagine walking through the historic stone alleys of Lamu or Mombasa. You feel the refreshing ocean breeze, hear the melodic Adhan calling believers to prayer, and see citizens wearing elegant flowing white robes (Kanzus) and vibrant wraps (Lesos). You inhale the aroma of cardamom coffee brewing in tall brass pots and marvel at heavy wooden doors carved with perfect geometric symmetry. This multisensory experience is the living heritage of Islamic civilisation in Kenya. In this lesson, we examine how Islamic heritage shaped the material culture, architecture, and daily lifestyle of Kenya.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Carved_door_in_Zanzibar.jpg/800px-Carved_door_in_Zanzibar.jpg",
        "image_title": "Swahili Carved Door Craftsmanship",
        "image_caption": "Historic carved wooden Swahili door showcasing geometric rosettes, floral motifs, and timeless East African architectural craftsmanship.",
        "concept_name": "Material Culture & Everyday Islamic Civilisation in Kenya",
        "concept_explanation": "Kenyan Islamic heritage is physically manifested in material culture—the physical artifacts, architecture, apparel, and culinary traditions of society. This includes coral stone architecture, intricate Swahili carved doors, modest attire (Kanzu, Kofia, Hijab, Leso/Khanga), wudhu hygiene utensils (Aftaba), and hospitality symbols like the brass coffee pot (Dallah).",
        "scripture_quran": "O children of Adam, We have bestowed upon you clothing to conceal your private parts and as adornment...",
        "scripture_quran_ref": "Surah Al-A'raf 7:26",
        "scripture_hadith": "Indeed, Allah is beautiful and He loves beauty.",
        "scripture_hadith_ref": "Sahih Muslim 91",
        "deep_explanation": "The material culture of Kenyan Islamic civilisation is articulated across four major domains:\n1. Architecture: Built from local coral rag and mangrove poles, featuring natural cross-ventilation, shaded verandas (Baraza), and carved wooden entrance doors with protective geometric rosettes.\n2. Dress & Modesty: The ankle-length white Kanzu and embroidered Kofia for men symbolize dignity; the colorful Leso/Khanga (featuring printed moral proverbs) and Hijab for women blend modesty (Haya) with artistic expression.\n3. Household Utensils: Brass coffee pots (Dallah) for brewing spiced cardamom Kahwa embody prophetic hospitality (Diyafa), while Aftaba water ewers emphasize spiritual cleanliness (Taharah).\n4. Culinary Traditions: Dishes such as Pilau, Biryani, Samusa, and Mahamri originated along the coastal trade corridors and have become celebrated national staples across Kenya.",
        "diagram_title": "The Museum of Kenyan Islamic Material Heritage",
        "svg_func": get_svg_lesson_6,
        "table_title": "Kenyan Islamic Material Culture: Artifacts and Meanings",
        "table_headers": ["Cultural Artifact", "Physical Description & Materials", "Spiritual & Social Value in Kenyan Life"],
        "table_rows": [
            ["Kanzu & Kofia", "Flowing white cotton tunic and embroidered cap", "Represents male modesty (Haya), dignity, and formal Kenyan attire"],
            ["Carved Swahili Door", "Hardwood (Mvule) door with floral & geometric carvings", "Symbol of welcoming hospitality, family honor, and architectural beauty"],
            ["Dallah (Coffee Pot)", "Tall brass pot with curved spout for spiced coffee", "Emblem of generous hospitality (Diyafa) and honoring guests"],
            ["Leso / Khanga", "Printed cotton fabric with Swahili moral proverb (Mji)", "Female modesty, maternal gift-giving, and moral communication"]
        ],
        "scenario": "During an art class, Amina and Yusuf sculpt models of historic Kenyan cultural artifacts. Amina uses terracotta clay to model a traditional Aftaba (water vessel used for performing ablution before prayer). Yusuf carves a miniature wooden Swahili door. Their teacher, Mr. Bilal, commends them: 'Outstanding work! By creating these replicas, you preserve the memory of our ancestors, who believed that even everyday utilitarian items should be crafted with aesthetic beauty and spiritual purpose.'",
        "real_world": "Design a 'Moral Khanga' border. The Khanga is a traditional East African fabric worn by women that always features a printed moral proverb at the base. Write down a meaningful Swahili proverb promoting peace or integrity—such as 'Amani ni Ngao ya Taifa' (Peace is the nation's shield) or 'Mtu ni Utu' (A person's worth lies in their character)—and frame it with geometric borders in your notebook.",
        "reflection": "How does the Islamic mandate of cleanliness (Taharah) influence the design of household vessels and living spaces? Why are moral proverbs printed on Khangas such an effective vehicle for values education in families?",
        "misconception": "Misconception: Assuming that Islamic dress like the Kanzu is foreign 'Arab clothing.' In East Africa, the Kanzu has been worn for centuries, fully incorporated into the national dress of Kenya and neighboring nations as a symbol of statesmanship and honor.",
        "yt_id": "r8X1-K3w8Dw",
        "yt_title": "Swahili Architecture and Material Culture in Kenya",
        "yt_desc": "Visual exploration of Lamu carved doors, coral stone mosques, Kanzu attire, and traditional culinary arts.",
        "mcq": {
            "question": "What is the traditional name of the ankle-length, flowing white robe worn by men along the Kenyan Coast and across Muslim communities, representing modesty and dignity?",
            "options": [
                "A. Hijab",
                "B. Kanzu",
                "C. Khanga",
                "D. Leso"
            ],
            "answer": "B",
            "explanation": "The Kanzu is the traditional, ankle-length flowing white robe worn by Muslim men across East Africa, typically paired with an embroidered Kofia for religious and civic occasions."
        },
        "summary_content": "Islamic heritage has profoundly shaped Kenya's material culture, architecture, dress, and domestic arts. Carved doors, coral stone mosques, the Kanzu, Khanga, and the Dallah coffee pot merge practical utility with aesthetic beauty and spiritual values.",
        "key_points": [
            "Kenyan Islamic heritage is physically embodied in architecture, dress, and household arts.",
            "Carved Swahili doors and coral stone structures represent UNESCO-recognized craftsmanship.",
            "The Kanzu, Kofia, Hijab, and Leso combine religious modesty (Haya) with East African style.",
            "Household items like the Dallah and Aftaba embody prophetic hospitality and hygiene."
        ],
        "exit_ticket": "Name two physical artifacts from Kenyan Swahili culture and explain their spiritual or social significance."
    },
    {
        "unit_order": 7,
        "lesson_title": "Synthesis: Islam and Kenyan development",
        "inquiry": "How does the history of Islam across Kenya's four regions contribute to our modern national identity and development?",
        "hook": "Imagine a mighty, life-giving river formed by the convergence of four powerful mountain streams. As these four streams unite, they form a wide, deep river that irrigates thousands of farms, sustains towns, and enables boats to travel freely across the land. The four mountain streams are the histories of Islam in the Coast, Western, Central, and North Eastern regions. Together, they flow into the singular river of our Kenyan national heritage. In this final synthesis lesson, we unite our regional studies to celebrate Islam's enduring contribution to Kenya's national unity, development, and identity.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Parliament_Buildings_Nairobi.jpg/800px-Parliament_Buildings_Nairobi.jpg",
        "image_title": "Parliament Buildings of Kenya, Nairobi",
        "image_caption": "The Parliament Buildings in Nairobi, symbolizing Kenyan national governance, democratic unity, and the shared contributions of all faiths to national development.",
        "concept_name": "The Four Streams of Kenyan Islamic Heritage",
        "concept_explanation": "Islam is an organic, historical constituent of Kenya's diverse identity. The four historical streams—Coastal maritime heritage, Western royal patronage under Nabongo Mumia, Central railway urban communities, and North Eastern pastoralist resilience—converge to enrich Kenya's national language (Kiswahili), legal traditions (Kadhi courts), social infrastructure (schools and hospitals), and peaceful coexistence.",
        "scripture_quran": "O mankind, indeed We have created you from male and female and made you peoples and tribes that you may know one another. Indeed, the most noble of you in the sight of Allah is the most righteous of you...",
        "scripture_quran_ref": "Surah Al-Hujurat 49:13",
        "scripture_hadith": "Love for one's nation and contributing to its goodness is a hallmark of righteous character.",
        "scripture_hadith_ref": "Narrated in classical ethics literature",
        "deep_explanation": "The nationwide synthesis of Islamic heritage in Kenya is manifested across four enduring contributions:\n1. National Language & Cultural Fabric: Kiswahili, born of coastal Bantu-Islamic contact, serves as Kenya's official national lingua franca, while garments like the Kanzu and dishes like Pilau form standard Kenyan culture.\n2. Constitutional Recognition & Justice: The Kadhi Court system, embedded in the Constitution of Kenya, provides specialized judicial administration for personal family law (marriage, divorce, inheritance) for Kenyan Muslims.\n3. Social & Health Infrastructure: Muslim non-governmental organizations, Waqf endowments, and trusts operate hundreds of high schools, colleges, and charitable hospitals (such as Nairobi South Hospital) serving all Kenyans regardless of faith.\n4. Peaceful Cohesion & Patriotism: Kenyan Muslims serve with distinction in the armed forces, civil service, and parliament, championing peace and mutual respect across our 47 counties.",
        "diagram_title": "The Four Historical Streams of Islam in Kenya",
        "svg_func": get_svg_lesson_7,
        "table_title": "Master Unit Synthesis Matrix: The Four Streams of Islam in Kenya",
        "table_headers": ["Region", "Historical Milestone", "Enduring Contribution to Modern Kenya", "Guiding National Value"],
        "table_rows": [
            ["Coast", "8th C. Indian Ocean trade & Lamu stone town", "Kiswahili national language & maritime trade traditions", "Patriotism & cultural pride"],
            ["Western", "Nabongo Mumia's alliance & conversion in Wanga", "Inland literacy, educational hubs & royal diplomacy", "Inclusivity & hospitality"],
            ["Central", "Uganda Railway construction & Nairobi hubs", "Pumwani & Kibera urban settlements; Jamia Mosque", "Cooperation (Ta'awun) & industry"],
            ["North Eastern", "Pastoralist migrations & Duksi tree schools", "Quranic memorization, resilience & Maslah justice", "Peacebuilding & persistence"]
        ],
        "scenario": "A student from Mumias, a student from Wajir, and a student from Mombasa collaborate on a national history presentation titled 'The Mosaic of Kenyan Identity.' The teacher summarizes their findings: 'By bringing together the royal history of Mumias, the nomadic resilience of Wajir, and the maritime civilization of Mombasa, you demonstrate that Kenyan diversity is our greatest national strength. Diverse in our regional origins, we are united under one flag, working together for the prosperity of Kenya.'",
        "real_world": "Adopt a 'National Unity Pledge' in your daily student life. Commit to three practical rules: 1. I will learn about and respect the traditions of classmates from other regions and religions, 2. I will reject tribalism, stereotyping, and hate speech in all forms, and 3. I will actively partner with all peers to make my school a peaceful, supportive environment. Present your pledge during school assembly.",
        "reflection": "How does studying the four regional streams of Islam in Kenya help eradicate tribalism and foster national patriotism? What role do Muslim schools and charitable hospitals play in improving life for all Kenyans?",
        "misconception": "Misconception: Believing that regional diversity causes national weakness. As Surah Al-Hujurat (49:13) teaches, diversity is intentional divine beauty meant to inspire mutual learning, cooperation, and collective national progress.",
        "yt_id": "z8X3-V9w1Qw",
        "yt_title": "Comprehensive Unit Synthesis: Islam and Kenyan Development",
        "yt_desc": "Capstone summary reviewing the four historical regions of Islam in Kenya and their contributions to national unity and progress.",
        "mcq": {
            "question": "A student from Mumias, a student from Wajir, and a student from Mombasa are working on a joint project about Kenyan development. Applying the complete synthesis of this unit, how should they view their diverse regional backgrounds?",
            "options": [
                "A. They should compete to prove their own region is the only historically significant one.",
                "B. They should view their diversity as a divine design (Surah Al-Hujurat 49:13) that allows them to pool distinct regional strengths to build a united Kenya.",
                "C. They should hide their cultural backgrounds to avoid disagreements.",
                "D. They should assume that only coastal history is relevant to Islamic education."
            ],
            "answer": "B",
            "explanation": "Surah Al-Hujurat (49:13) and CBC pedagogical standards emphasize that diversity is a divine blessing meant to inspire mutual cooperation and pooled strengths for national development."
        },
        "summary_content": "Islam is an organic constituent of Kenya's national identity. The four historical streams—Coast, Western, Central, and North Eastern—converge into a vibrant national heritage, contributing Kiswahili, Kadhi courts, schools, hospitals, and an enduring commitment to peace and patriotism.",
        "key_points": [
            "Islam in Kenya is a nationwide heritage uniting four distinct regional histories.",
            "Coastal trade, Nabongo Mumia, railway workers, and pastoralist Duksi schools represent unique strengths.",
            "Kiswahili, Kadhi courts, and charitable institutions serve the entire Kenyan nation.",
            "Embracing our regional and cultural diversity builds an unbreakable, united Kenya."
        ],
        "exit_ticket": "Write down one major contribution of Islamic heritage to Kenya's national identity, culture, or language."
    }
]


# ─────────────────────────────────────────────────────────────────────────────
# INGESTION & AUDIT EXECUTION ENGINE
# ─────────────────────────────────────────────────────────────────────────────

@transaction.atomic
def ingest_topic_18():
    print("================================================================================")
    print("STARTING PRODUCTION INGESTION: GRADE 9 IRE — TOPIC 18")
    print("Topic: History of Islam: Islam in Kenya (Topic ID 358)")
    print("================================================================================")

    topic = Topic.objects.get(id=358)
    print(f"Target Topic: {topic.id} - {topic.name}")

    # Clean existing units for idempotent ingestion
    existing_units = LearningUnit.objects.filter(topic=topic)
    if existing_units.exists():
        print(f"Cleaning up {existing_units.count()} existing LearningUnits for clean idempotent ingestion...")
        existing_units.delete()

    created_units = 0
    created_lessons = 0
    created_blocks = 0
    created_assets = 0

    for ldata in TOPIC_18_LESSONS:
        order = ldata["unit_order"]
        title = ldata["lesson_title"]
        print(f"\nIngesting Lesson {order}/7: {title}...")

        # 1. Create LearningUnit
        unit = LearningUnit.objects.create(
            topic=topic,
            name=f"Lesson 7.1.{order}: {title}",
            order=order,
            description=clean_text(ldata["concept_explanation"][:250] + "...")
        )
        created_units += 1

        # 2. Create Published Lesson
        lesson = Lesson.objects.create(
            topic=topic,
            learning_unit=unit,
            title=clean_text(title),
            version=1,
            status="published"
        )
        created_lessons += 1

        # 3. Create Pedagogical Vector SVG Asset
        svg_xml = ldata["svg_func"]()
        try:
            ET.fromstring(svg_xml)
        except ET.ParseError as e:
            raise ValueError(f"Invalid SVG XML generated for Lesson {order}: {e}")

        diagram_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="image",
            title=ldata["diagram_title"],
            url="",
            metadata={
                "svg_xml": svg_xml,
                "svg_content": svg_xml,
                "format": "svg",
                "theme": "dark",
                "viewBox": "0 0 880 440"
            }
        )
        created_assets += 1

        # 4. Create Wikimedia Asset
        wiki_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="image",
            title=ldata["image_title"],
            url=ldata["image_url"],
            metadata={
                "caption": ldata["image_caption"],
                "source": "Wikimedia Commons"
            }
        )
        created_assets += 1

        # 5. Create Educational Video Asset
        video_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="video",
            title=ldata["yt_title"],
            url=f"https://www.youtube.com/watch?v={ldata['yt_id']}",
            metadata={
                "youtube_id": ldata["yt_id"],
                "description": ldata["yt_desc"]
            }
        )
        created_assets += 1

        # ─────────────────────────────────────────────────────────────────────
        # 7 ATOMIC CARDS (PAGES 1 TO 7)
        # ─────────────────────────────────────────────────────────────────────

        # CARD 1 (Page 1): Orientation & Hook
        b1_img = LessonBlock.objects.create(
            lesson=lesson,
            block_type="suggested_image",
            page_number=1,
            order=1,
            content={"caption": ldata["image_caption"], "title": ldata["image_title"], "url": ldata["image_url"]},
            metadata={"source": "Wikimedia Commons"}
        )
        b1_img.assets.add(wiki_asset)
        created_blocks += 1

        LessonBlock.objects.create(
            lesson=lesson,
            block_type="learning_goal",
            page_number=1,
            order=2,
            content={
                "inquiry_question": clean_text(ldata["inquiry"]),
                "hook": clean_text(ldata["hook"])
            },
            metadata={"focus": "orientation_and_connection"}
        )
        created_blocks += 1

        # CARD 2 (Page 2): Core Teaching & Scripture Panel
        LessonBlock.objects.create(
            lesson=lesson,
            block_type="concept_explanation",
            page_number=2,
            order=1,
            content={
                "concept_name": clean_text(ldata["concept_name"]),
                "text": clean_text(ldata["concept_explanation"])
            },
            metadata={"depth": "core_concept"}
        )
        created_blocks += 1

        LessonBlock.objects.create(
            lesson=lesson,
            block_type="callout",
            page_number=2,
            order=2,
            content={
                "title": "Scripture Evidence Panel",
                "quran_verse": clean_text(ldata["scripture_quran"]),
                "quran_reference": clean_text(ldata["scripture_quran_ref"]),
                "hadith_text": clean_text(ldata["scripture_hadith"]),
                "hadith_reference": clean_text(ldata["scripture_hadith_ref"])
            },
            metadata={"style": "scripture_panel"}
        )
        created_blocks += 1

        # CARD 3 (Page 3): Deep Explanation, Pedagogical Diagram & Comparison Table
        LessonBlock.objects.create(
            lesson=lesson,
            block_type="concept_explanation",
            page_number=3,
            order=1,
            content={
                "text": clean_text(ldata["deep_explanation"])
            },
            metadata={"depth": "elaborated_analysis"}
        )
        created_blocks += 1

        b3_diag = LessonBlock.objects.create(
            lesson=lesson,
            block_type="suggested_diagram",
            page_number=3,
            order=2,
            content={
                "title": ldata["diagram_title"],
                "svg_xml": svg_xml,
                "svg_content": svg_xml
            },
            metadata={"format": "svg", "viewBox": "0 0 880 440", "svg_content": svg_xml}
        )
        b3_diag.assets.add(diagram_asset)
        created_blocks += 1

        LessonBlock.objects.create(
            lesson=lesson,
            block_type="comparison_table",
            page_number=3,
            order=3,
            content={
                "title": ldata["table_title"],
                "headers": ldata["table_headers"],
                "rows": ldata["table_rows"]
            },
            metadata={"structure": "matrix"}
        )
        created_blocks += 1

        # CARD 4 (Page 4): Relatable Student Scenario
        LessonBlock.objects.create(
            lesson=lesson,
            block_type="worked_example",
            page_number=4,
            order=1,
            content={
                "title": "Relatable Student Scenario & Analysis",
                "scenario": clean_text(ldata["scenario"])
            },
            metadata={"context": "student_daily_life"}
        )
        created_blocks += 1

        # CARD 5 (Page 5): Real-World Application, Reflection & Video
        LessonBlock.objects.create(
            lesson=lesson,
            block_type="real_world_example",
            page_number=5,
            order=1,
            content={
                "application": clean_text(ldata["real_world"]),
                "reflection_prompts": clean_text(ldata["reflection"]),
                "misconception_check": clean_text(ldata["misconception"])
            },
            metadata={"focus": "authentic_application"}
        )
        created_blocks += 1

        b5_vid = LessonBlock.objects.create(
            lesson=lesson,
            block_type="suggested_video",
            page_number=5,
            order=2,
            content={
                "title": ldata["yt_title"],
                "youtube_id": ldata["yt_id"],
                "url": f"https://www.youtube.com/watch?v={ldata['yt_id']}",
                "description": ldata["yt_desc"]
            },
            metadata={"type": "educational_multimedia"}
        )
        b5_vid.assets.add(video_asset)
        created_blocks += 1

        # CARD 6 (Page 6): Verified Interactive MCQ
        mcq_data = ldata["mcq"]
        LessonBlock.objects.create(
            lesson=lesson,
            block_type="knowledge_check",
            page_number=6,
            order=1,
            content={
                "question": mcq_data["question"],
                "options": mcq_data["options"],
                "answer": mcq_data["answer"],
                "explanation": mcq_data["explanation"]
            },
            metadata={"assessment_type": "mcq"}
        )
        created_blocks += 1

        # CARD 7 (Page 7): Summary, Key Points & Exit Ticket
        LessonBlock.objects.create(
            lesson=lesson,
            block_type="summary",
            page_number=7,
            order=1,
            content={
                "summary": clean_text(ldata["summary_content"]),
                "key_points": [clean_text(kp) for kp in ldata["key_points"]],
                "exit_ticket": clean_text(ldata["exit_ticket"])
            },
            metadata={"review_type": "synthesis"}
        )
        created_blocks += 1

    print("\n================================================================================")
    print("INGESTION COMPLETE FOR TOPIC 18!")
    print(f"Created Units: {created_units}")
    print(f"Created Lessons: {created_lessons}")
    print(f"Created Blocks: {created_blocks}")
    print(f"Created Assets: {created_assets}")
    print("================================================================================")


if __name__ == "__main__":
    ingest_topic_18()
