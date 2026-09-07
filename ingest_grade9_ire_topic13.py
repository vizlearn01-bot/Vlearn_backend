"""
VLearn CBC Grade 9 IRE — Topic 13: Iddah (The Waiting Period)
Production Ingestion and Enrichment Script for all 5 Lessons

Target Topic in DB: Topic ID 353 (Subject: IRE ID 53, Grade: Grade 9 ID 18)
Source Markdown: /home/jason-bitega/Desktop/VL/vlearn_repositories/Grade 9 IRE/iddah.md

5 Lessons Ingested & Fully Enriched:
  1. Lesson 6.2.1: Meaning and categories
  2. Lesson 6.2.2: Rationale and wisdom
  3. Lesson 6.2.3: Rules of iddah
  4. Lesson 6.2.4: Importance and support
  5. Lesson 6.2.5: Unit synthesis
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
# 5 DEDICATED RESPONSIVE PEDAGOGICAL VECTOR SVGS (#0f172a theme, viewBox 880x440)
# ─────────────────────────────────────────────────────────────────────────────

def get_svg_lesson_1():
    """Lesson 6.2.1: Categories & Durations of Iddah"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg131" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg131)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">CATEGORIES &amp; DURATIONS OF IDDAH (THE WAITING PERIOD)</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Prescribed Waiting Periods in Islamic Family Law Across Marital Situations and Physical States</text>

  <!-- 4 Comparative Cards -->
  <!-- Card 1: Widow -->
  <g transform="translate(45, 85)">
    <rect width="180" height="260" rx="8" fill="#1e293b" stroke="#f87171" stroke-width="1.5"/>
    <rect width="180" height="34" rx="8" fill="#7f1d1d"/>
    <text x="90" y="22" fill="#fecaca" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">1. THE WIDOW</text>
    
    <text x="90" y="56" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Husband Passed Away</text>

    <rect x="10" y="70" width="160" height="60" rx="4" fill="#0f172a"/>
    <text x="90" y="92" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Physical State:</text>
    <text x="90" y="112" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Any (Non-pregnant)</text>

    <rect x="10" y="140" width="160" height="70" rx="4" fill="#0f172a"/>
    <text x="90" y="160" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Prescribed Duration:</text>
    <text x="90" y="180" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">4 Months &amp; 10 Days</text>
    <text x="90" y="196" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">(Surah Al-Baqarah 2:234)</text>

    <text x="90" y="235" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">Honors marriage &amp; grief</text>
  </g>

  <!-- Card 2: Pregnant Woman -->
  <g transform="translate(245, 85)">
    <rect width="180" height="260" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="180" height="34" rx="8" fill="#065f46"/>
    <text x="90" y="22" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">2. PREGNANT WOMAN</text>

    <text x="90" y="56" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Divorced or Widowed</text>

    <rect x="10" y="70" width="160" height="60" rx="4" fill="#0f172a"/>
    <text x="90" y="92" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Physical State:</text>
    <text x="90" y="112" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Carrying a Child</text>

    <rect x="10" y="140" width="160" height="70" rx="4" fill="#0f172a"/>
    <text x="90" y="160" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Prescribed Duration:</text>
    <text x="90" y="180" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">Until Delivery</text>
    <text x="90" y="196" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">(Surah At-Talaq 65:4)</text>

    <text x="90" y="235" fill="#34d399" font-family="system-ui, sans-serif" font-size="8" font-weight="700" text-anchor="middle">★ Overrides all other terms</text>
  </g>

  <!-- Card 3: Menstruating Divorcee -->
  <g transform="translate(445, 85)">
    <rect width="180" height="260" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="180" height="34" rx="8" fill="#0369a1"/>
    <text x="90" y="22" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">3. DIVORCEE (REGULAR)</text>

    <text x="90" y="56" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Marriage Dissolved</text>

    <rect x="10" y="70" width="160" height="60" rx="4" fill="#0f172a"/>
    <text x="90" y="92" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Physical State:</text>
    <text x="90" y="112" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Menstruating Regularly</text>

    <rect x="10" y="140" width="160" height="70" rx="4" fill="#0f172a"/>
    <text x="90" y="160" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Prescribed Duration:</text>
    <text x="90" y="180" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">3 Menstrual Cycles</text>
    <text x="90" y="196" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">(Surah Al-Baqarah 2:228)</text>

    <text x="90" y="235" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">Verifies womb is empty</text>
  </g>

  <!-- Card 4: Menopausal Divorcee -->
  <g transform="translate(645, 85)">
    <rect width="180" height="260" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="180" height="34" rx="8" fill="#92400e"/>
    <text x="90" y="22" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">4. DIVORCEE (NON-MEN)</text>

    <text x="90" y="56" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Marriage Dissolved</text>

    <rect x="10" y="70" width="160" height="60" rx="4" fill="#0f172a"/>
    <text x="90" y="92" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Physical State:</text>
    <text x="90" y="112" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Postmenopausal / Irregular</text>

    <rect x="10" y="140" width="160" height="70" rx="4" fill="#0f172a"/>
    <text x="90" y="160" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Prescribed Duration:</text>
    <text x="90" y="180" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">3 Lunar Months</text>
    <text x="90" y="196" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">(Surah At-Talaq 65:4)</text>

    <text x="90" y="235" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">Clear calendar timeline</text>
  </g>

  <!-- Bottom Key Rules Banner -->
  <g transform="translate(45, 360)">
    <rect width="780" height="55" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="390" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">CORE LEGAL PRINCIPLES OF IDDAH</text>
    <text x="390" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Pregnancy Overrides All Categories • Remarriage Strictly Prohibited • Obligatory Act of Worship (Ibadah)</text>
  </g>
</svg>"""


def get_svg_lesson_2():
    """Lesson 6.2.2: The Three Shields of Iddah (Wisdom & Rationale)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg132" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg132)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">DIVINE WISDOM (HIKMAH): THE THREE PROTECTIVE SHIELDS OF IDDAH</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Safeguarding Biological Lineage, Preserving Family Bonds, and Honoring Human Grief</text>

  <!-- Shield 1: Biological Clarity -->
  <g transform="translate(45, 90)">
    <rect width="240" height="250" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="240" height="38" rx="10" fill="#0369a1"/>
    <text x="120" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">SHIELD 1: BIOLOGICAL CLARITY</text>
    
    <text x="120" y="60" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Hifz al-Nasab (Lineage)</text>

    <rect x="15" y="75" width="210" height="155" rx="6" fill="#0f172a"/>
    <text x="25" y="98" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Verification of Womb:</text>
    <text x="25" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Confirms if pregnancy exists</text>
    <text x="25" y="140" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Protection of Children:</text>
    <text x="25" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Guarantees legal fatherhood</text>
    <text x="25" y="172" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  and inheritance rights</text>
    <text x="25" y="198" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Prevents mixed lineage disputes</text>
  </g>

  <!-- Shield 2: Reconciliation Buffer -->
  <g transform="translate(320, 90)">
    <rect width="240" height="250" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="240" height="38" rx="10" fill="#059669"/>
    <text x="120" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">SHIELD 2: RECONCILIATION</text>

    <text x="120" y="60" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Cooling-off Period (Talaq Raj'i)</text>

    <rect x="15" y="75" width="210" height="155" rx="6" fill="#0f172a"/>
    <text x="25" y="98" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• De-escalates Anger:</text>
    <text x="25" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Prevents hasty separations</text>
    <text x="25" y="140" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Home Stay Encouraged:</text>
    <text x="25" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Couple remains in same house</text>
    <text x="25" y="172" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  fostering dialogue &amp; affection</text>
    <text x="25" y="198" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Marriage resumable without new contract</text>
  </g>

  <!-- Shield 3: Emotional Healing & Dignity -->
  <g transform="translate(595, 90)">
    <rect width="240" height="250" rx="10" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <rect width="240" height="38" rx="10" fill="#6d28d9"/>
    <text x="120" y="24" fill="#ede9fe" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">SHIELD 3: EMOTIONAL DIGNITY</text>

    <text x="120" y="60" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Hidad &amp; Marital Respect</text>

    <rect x="15" y="75" width="210" height="155" rx="6" fill="#0f172a"/>
    <text x="25" y="98" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Honors Deceased Spouse:</text>
    <text x="25" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  4 months 10 days mourning</text>
    <text x="25" y="140" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Psychological Reset:</text>
    <text x="25" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Protects widow from pressure</text>
    <text x="25" y="172" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  to remarry immediately</text>
    <text x="25" y="198" fill="#f87171" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Not a punishment; a sacred right</text>
  </g>

  <!-- Bottom Synthesis Banner -->
  <g transform="translate(45, 360)">
    <rect width="790" height="55" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="395" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">THE MAQASID AL-SHARIAH FOUNDATION</text>
    <text x="395" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Protects Lineage (Nasab) • Protects Family Stability (Usrah) • Protects Psychological Dignity (Nafs)</text>
  </g>
</svg>"""


def get_svg_lesson_3():
    """Lesson 6.2.3: Rules of Iddah: Divorcee vs Widow"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg133" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg133)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">RULES OF IDDAH: DIVORCED WOMEN VS. WIDOWED WOMEN</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Contrasting Legal Rulings on Residence, Financial Maintenance, Appearance, and Leaving Home</text>

  <!-- Column 1: Divorced Woman -->
  <g transform="translate(45, 85)">
    <rect width="380" height="260" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="380" height="34" rx="8" fill="#0369a1"/>
    <text x="190" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">DIVORCED WOMAN (TALAQ RAJ'I)</text>

    <!-- Row 1: Residence -->
    <rect x="15" y="46" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="62" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Primary Residence:</text>
    <text x="25" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">Must remain in marital home with husband; eviction strictly haram</text>

    <!-- Row 2: Maintenance -->
    <rect x="15" y="96" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="112" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Financial Maintenance (Nafaqah):</text>
    <text x="25" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">100% provided by husband (food, shelter, clothing, medical care)</text>

    <!-- Row 3: Beautification -->
    <rect x="15" y="146" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="162" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Appearance &amp; Beautification:</text>
    <text x="25" y="178" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">Allowed; dressing well is encouraged to foster spousal reconciliation</text>

    <!-- Row 4: Leaving Home -->
    <rect x="15" y="196" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="212" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Movement Outside:</text>
    <text x="25" y="228" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">Should remain in home; leaves only for valid necessity with notification</text>
  </g>

  <!-- Column 2: Widowed Woman -->
  <g transform="translate(455, 85)">
    <rect width="380" height="260" rx="8" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <rect width="380" height="34" rx="8" fill="#6d28d9"/>
    <text x="190" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">WIDOWED WOMAN (HIDAD / MOURNING)</text>

    <!-- Row 1: Residence -->
    <rect x="15" y="46" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="62" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Primary Residence:</text>
    <text x="25" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">Stays in home where husband passed away; must sleep there at night</text>

    <!-- Row 2: Maintenance -->
    <rect x="15" y="96" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="112" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Financial Maintenance (Nafaqah):</text>
    <text x="25" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">From inheritance share / estate; community support if in need</text>

    <!-- Row 3: Beautification -->
    <rect x="15" y="146" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="162" fill="#f87171" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Appearance &amp; Beautification (Hidad):</text>
    <text x="25" y="178" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">Avoids makeup, perfume, bright/flashy jewelry; dresses modestly</text>

    <!-- Row 4: Leaving Home -->
    <rect x="15" y="196" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="212" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Movement Outside:</text>
    <text x="25" y="228" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">Fully permitted during daytime for work, teaching, errands, medical needs</text>
  </g>

  <!-- Universal Injunction -->
  <g transform="translate(45, 360)">
    <rect width="790" height="55" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="395" y="24" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">UNIVERSAL PROHIBITION DURING IDDAH</text>
    <text x="395" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Marriage proposals and remarriage contracts are strictly invalid and forbidden until the waiting period expires</text>
  </g>
</svg>"""


def get_svg_lesson_4():
    """Lesson 6.2.4: Circle of Social Support During Iddah"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg134" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg134)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE CIRCLE OF SOCIAL RESPONSIBILITY DURING IDDAH</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">A Comprehensive Multi-Tiered Safety Net Protecting Women from Vulnerability and Neglect</text>

  <!-- 3 Support Rings/Cards -->
  <!-- Tier 1: Spousal / Estate Obligations -->
  <g transform="translate(45, 90)">
    <rect width="240" height="250" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="240" height="38" rx="10" fill="#0369a1"/>
    <text x="120" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">TIER 1: SPOUSAL / ESTATE</text>

    <text x="120" y="60" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Legal Financial Maintenance</text>

    <rect x="15" y="75" width="210" height="155" rx="6" fill="#0f172a"/>
    <text x="25" y="98" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Shelter Guarantee:</text>
    <text x="25" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Surah At-Talaq 65:6: Lodge</text>
    <text x="25" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  them where you live comfortably</text>
    <text x="25" y="152" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Zero Oppression:</text>
    <text x="25" y="168" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Forbidden to cut off food</text>
    <text x="25" y="182" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  or harass her into leaving early</text>
    <text x="25" y="208" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Prevents sudden homelessness</text>
  </g>

  <!-- Tier 2: Extended Family Network -->
  <g transform="translate(320, 90)">
    <rect width="240" height="250" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="240" height="38" rx="10" fill="#059669"/>
    <text x="120" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">TIER 2: FAMILY NETWORK</text>

    <text x="120" y="60" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Domestic &amp; Emotional Relief</text>

    <rect x="15" y="75" width="210" height="155" rx="6" fill="#0f172a"/>
    <text x="25" y="98" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Practical Assistance:</text>
    <text x="25" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Running errands, buying groceries,</text>
    <text x="25" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  and assisting with child supervision</text>
    <text x="25" y="152" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Emotional Solidarity:</text>
    <text x="25" y="168" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Validating grief without intrusive</text>
    <text x="25" y="182" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  questioning or harmful gossip</text>
    <text x="25" y="208" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Cushions psychological shock</text>
  </g>

  <!-- Tier 3: Community & Ummah -->
  <g transform="translate(595, 90)">
    <rect width="240" height="250" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="240" height="38" rx="10" fill="#d97706"/>
    <text x="120" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">TIER 3: UMMAH &amp; STATE</text>

    <text x="120" y="60" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Collective Civic Duty</text>

    <rect x="15" y="75" width="210" height="155" rx="6" fill="#0f172a"/>
    <text x="25" y="98" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Prophetic Injunction:</text>
    <text x="25" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  "One who cares for a widow is</text>
    <text x="25" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  like a warrior in the way of Allah"</text>
    <text x="25" y="152" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Institutional Aid:</text>
    <text x="25" y="168" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Mosque welfare, zakat support,</text>
    <text x="25" y="182" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  and job security protection</text>
    <text x="25" y="208" fill="#f87171" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Eradicates stigma &amp; isolation</text>
  </g>

  <!-- Bottom Message -->
  <g transform="translate(45, 360)">
    <rect width="790" height="55" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="395" y="24" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">IDDAH IS A SACRED SOCIAL COVENANT</text>
    <text x="395" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Not an individual burden or punishment; a community-wide responsibility upholding human honor</text>
  </g>
</svg>"""


def get_svg_lesson_5():
    """Lesson 6.2.5: The Master Temple of Iddah (Unit Synthesis)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg135" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg135)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">MASTER SYNTHESIS: THE TEMPLE OF COMPREHENSIVE PROTECTION</text>
  <text x="440" y="52" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">How Iddah Harmonizes Spiritual Devotion, Biological Justice, Emotional Healing, and Economic Security</text>

  <!-- Roof Pediment: A Just & Stable Ummah -->
  <g transform="translate(140, 70)">
    <polygon points="300,0 600,45 0,45" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="300" y="32" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">A JUST, STABLE, AND COMPASSIONATE SOCIETY (UMMAH)</text>
  </g>

  <!-- 4 Supporting Pillars -->
  <!-- Pillar 1: Biological Clarity -->
  <g transform="translate(60, 125)">
    <rect width="170" height="225" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="170" height="30" rx="6" fill="#0284c7"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">PILLAR 1: BIOLOGY</text>

    <rect x="10" y="38" width="150" height="175" rx="4" fill="#0f172a"/>
    <text x="18" y="58" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Hifz al-Nasab</text>
    <text x="18" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Verifies pregnancy</text>
    <text x="18" y="98" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Paternity Protection</text>
    <text x="18" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Guarantees children's</text>
    <text x="18" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  identity &amp; inheritance</text>
    <text x="18" y="152" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">3 Cycles / Delivery</text>
    <text x="18" y="168" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="7.5">Absolute biological clarity</text>
  </g>

  <!-- Pillar 2: Relational Reconciliation -->
  <g transform="translate(250, 125)">
    <rect width="170" height="225" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="170" height="30" rx="6" fill="#059669"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">PILLAR 2: REUNION</text>

    <rect x="10" y="38" width="150" height="175" rx="4" fill="#0f172a"/>
    <text x="18" y="58" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Cooling-off Space</text>
    <text x="18" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Prevents impulse divorce</text>
    <text x="18" y="98" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Preserves Family</text>
    <text x="18" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Shared home facilitates</text>
    <text x="18" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  apology &amp; renewal</text>
    <text x="18" y="152" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Talaq Raj'i Gateway</text>
    <text x="18" y="168" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="7.5">Bridge to resume marriage</text>
  </g>

  <!-- Pillar 3: Ethical Mourning -->
  <g transform="translate(440, 125)">
    <rect width="170" height="225" rx="6" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <rect width="170" height="30" rx="6" fill="#6d28d9"/>
    <text x="85" y="20" fill="#ede9fe" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">PILLAR 3: DIGNITY</text>

    <rect x="10" y="38" width="150" height="175" rx="4" fill="#0f172a"/>
    <text x="18" y="58" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Hidad (Mourning)</text>
    <text x="18" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Honors marital bond</text>
    <text x="18" y="98" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Spiritual Reflection</text>
    <text x="18" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Modest appearance</text>
    <text x="18" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  shields from suitors</text>
    <text x="18" y="152" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">4 Months &amp; 10 Days</text>
    <text x="18" y="168" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="7.5">Psychological healing space</text>
  </g>

  <!-- Pillar 4: Economic Security -->
  <g transform="translate(630, 125)">
    <rect width="170" height="225" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="170" height="30" rx="6" fill="#d97706"/>
    <text x="85" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">PILLAR 4: SECURITY</text>

    <rect x="10" y="38" width="150" height="175" rx="4" fill="#0f172a"/>
    <text x="18" y="58" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Nafaqah Obligation</text>
    <text x="18" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Full housing &amp; food</text>
    <text x="18" y="98" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Community Care</text>
    <text x="18" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Ummah supports widows</text>
    <text x="18" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  preventing poverty</text>
    <text x="18" y="152" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Social Safety Net</text>
    <text x="18" y="168" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="7.5">Zero financial abandonment</text>
  </g>

  <!-- Foundation: Act of Worship (Ibadah) -->
  <g transform="translate(60, 360)">
    <rect width="740" height="48" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="370" y="22" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">FOUNDATION: SUBMISSION TO DIVINE LAW (IBADAH)</text>
    <text x="370" y="38" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Observing Iddah is an act of spiritual obedience earning divine reward and preserving human dignity</text>
  </g>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION FOR THE 5 LESSONS IN TOPIC 13
# ─────────────────────────────────────────────────────────────────────────────

LESSONS_CONFIG = [
    {
        "unit_order": 1,
        "lesson_title": "Meaning and categories",
        "inquiry": "What is Iddah, and how does Islam categorize the waiting periods for different women?",
        "hook": "Imagine a traveler who arrives at a border crossing between two countries. They cannot simply run across; there is a secure holding area where they must wait for their documents to be verified and their transition to be recorded. This brief pause ensures order, safety, and clarity for both nations. In Islamic family law, when a marriage ends due to divorce or the death of a husband, a woman does not instantly transition into single life or a new relationship. She observes a mandatory waiting period called Iddah. This pause safeguards lineage, preserves respect, and provides space for healing.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Quran_manuscript.jpg/800px-Quran_manuscript.jpg",
        "image_title": "Early Qur'anic Manuscript on Islamic Law",
        "image_caption": "Historic Qur'anic manuscript illustrating foundational legal injunctions on marriage, divorce, and the prescribed waiting period (Iddah).",
        "concept_name": "Iddah & Its Four Legal Categories",
        "concept_explanation": "Iddah (The Waiting Period) is the legally prescribed duration during which a Muslim woman must wait after the dissolution of her marriage (due to divorce or the death of her husband) before she can lawfully remarry. Observing Iddah is an obligatory act of worship (ibadah) and a mandatory legal statute. The duration of the waiting period is strictly determined by the cause of separation (death or divorce) and the woman's physical state (pregnancy, regular menstruation, or menopause). Remarriage during this period is strictly forbidden to ensure clarity of marital status and protection of lineage.",
        "scripture_quran": "And divorced women shall wait concerning themselves for three monthly periods...",
        "scripture_quran_ref": "Surah Al-Baqarah 2:228",
        "scripture_hadith": "And those who die among you and leave wives behind, their wives shall wait for four months and ten days...",
        "scripture_hadith_ref": "Surah Al-Baqarah 2:234",
        "deep_explanation": "Islamic Shariah establishes four distinct categories of Iddah based on biological and social conditions:\n1. The Widow: Every widow must observe an Iddah of four months and ten days, regardless of whether she still menstruates or not, honoring her deceased spouse and allowing psychological mourning.\n2. The Pregnant Woman: For both divorcees and widows, the Iddah terminates the exact moment she gives birth, whether that occurs one day or nine months after the separation. Pregnancy overrides all other calendar or cycle counts.\n3. The Menstruating Divorcee: A woman who has regular menstrual cycles observes three cycles (quru') to establish conclusively that she is not carrying a child from the prior marriage.\n4. The Postmenopausal or Non-Menstruating Divorcee: For women who have reached menopause or do not experience menstruation, the waiting period is three lunar months.",
        "diagram_title": "Comparative Matrix of Iddah Categories & Durations",
        "svg_func": get_svg_lesson_1,
        "table_title": "Comprehensive Classification of Iddah Durations",
        "table_headers": ["Marital Situation", "Physical State of Woman", "Required Iddah Duration", "Primary Legal Wisdom"],
        "table_rows": [
            ["Widow (Husband passed away)", "Any State (except pregnant)", "4 Months and 10 Days", "Honors deceased husband; dignified mourning period"],
            ["Divorcee or Widow", "Pregnant", "Until Delivery of Child", "Establishes child paternity; overrides all counts"],
            ["Divorcee (Regular)", "Menstruating regularly", "3 Menstrual Cycles (Quru')", "Confirms womb is empty; lineage protection"],
            ["Divorcee (Non-menstruating)", "Postmenopausal / irregular", "3 Lunar Months", "Clear calendar timeline replacing menstrual cycles"]
        ],
        "scenario": "Zainab is a young woman whose husband passed away in a road accident. A few weeks later, a well-meaning family friend suggests that Zainab should immediately marry a distant cousin so she can have financial support. Zainab's mother, Halima, politely declines and explains: 'We appreciate your concern, but Zainab is a widow and must observe her Iddah. In Islam, a widow must wait for four months and ten days before she can marry anyone else. This is a divine command that honors her marriage, respects her grief, and provides the essential space to heal and pray for her husband.'",
        "real_world": "In your family and neighborhood, you may encounter someone going through a divorce or mourning the loss of a spouse. Show respect and empathy by recognizing their need for privacy and emotional space. Understand that the boundaries set by Iddah are meant to protect their dignity. Avoid gossiping or pressuring them back into social circles prematurely. Your supportive, considerate behavior is a direct application of Islamic social manners (Muamalat).",
        "reflection": "Why does Islam prescribe a longer waiting period for a widow (4 months and 10 days) than for a regular non-pregnant divorcee (approximately 3 months)? How does this demonstrate respect for the sanctity of human relationships and the emotional gravity of death?",
        "misconception": "Misconception: Some assume Iddah is a punitive house arrest for women after divorce or bereavement. In reality, Iddah is an honorable divine protection that safeguards child paternity, guarantees financial support from the husband or estate, and preserves the dignity of both families.",
        "yt_id": "g4mH2wYkK6Q",
        "yt_title": "Understanding the Wisdom and Categories of Iddah in Islam",
        "yt_desc": "Comprehensive Islamic jurisprudence lecture detailing the categories, rules, and divine rationale of the waiting period (Iddah).",
        "mcq": {
            "question": "Amina is divorced by her husband and is currently four months pregnant. According to Islamic Shariah, how long is her waiting period (Iddah)?",
            "options": [
                "A. Exactly three menstrual cycles.",
                "B. Exactly three lunar months.",
                "C. Until she gives birth to her child.",
                "D. Four months and ten days."
            ],
            "answer": "C",
            "explanation": "For pregnant women (whether divorced or widowed), the Quran explicitly specifies that their Iddah term is until they give birth (Surah At-Talaq 65:4), as childbirth conclusively establishes paternity and secures the child's rights."
        },
        "summary_content": "Iddah is the mandatory waiting period observed by a woman following divorce or the death of her husband. Its primary categories are widows (4 months and 10 days), pregnant women (until delivery), menstruating divorcees (3 cycles), and postmenopausal divorcees (3 lunar months). Remarriage is strictly forbidden during this timeframe to guarantee clarity of paternity and marital status.",
        "key_points": [
            "Iddah is an obligatory act of worship (ibadah) and legal transition period.",
            "The duration depends on the cause of separation and the woman's biological state.",
            "Pregnancy overrides all other durations, ending upon childbirth.",
            "Remarriage during Iddah is strictly invalid in Islamic law."
        ],
        "exit_ticket": "Write down the specific Iddah duration for a widow and explain how it differs from a non-pregnant menstruating divorcee."
    },
    {
        "unit_order": 2,
        "lesson_title": "Rationale and wisdom",
        "inquiry": "What is the divine wisdom (Hikmah) behind the obligation of Iddah in Islam?",
        "hook": "Imagine a computer that is suddenly unplugged while a critical document is being saved. If you instantly cut the power, the data corrupts, files are lost, and it becomes impossible to know which folder the document belongs to. A safe shutdown sequence is required to keep the system orderly. Similarly, marriage is a complex bond that links families, finances, and children. If a marriage ends, an instant break would cause emotional, social, and legal chaos. In this lesson, we explore the profound divine wisdom (Hikmah) that Shariah protects through the institution of Iddah.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Kaaba_Masjid_Haraam_Makkah.jpg/800px-Kaaba_Masjid_Haraam_Makkah.jpg",
        "image_title": "The Sanctuary of Divine Law and Justice",
        "image_caption": "The holy sanctuary reminding believers that divine laws are established to preserve human welfare, justice, and order.",
        "concept_name": "The Three Dimensions of Divine Wisdom (Hikmah)",
        "concept_explanation": "The divine wisdom behind Iddah centers on three foundational pillars: Lineage Protection (Hifz al-Nasab), Spousal Reconciliation Opportunity (Islah), and Emotional Healing with Dignity (Hidad). Verifying pregnancy ensures that children are rightly attributed to their biological fathers, safeguarding their legal inheritance and identity. In revocable divorce (Talaq Raj'i), Iddah serves as a cooling-off buffer allowing spouses to rethink their separation in the privacy of their home. For widows, it provides an honorable interval for psychological mourning without worldly pressures.",
        "scripture_quran": "...And it is not lawful for them to conceal what Allah has created in their wombs if they believe in Allah and the Last Day...",
        "scripture_quran_ref": "Surah Al-Baqarah 2:228",
        "scripture_hadith": "And their husbands have more right to take them back in this [period] if they desire reconciliation...",
        "scripture_hadith_ref": "Surah Al-Baqarah 2:228",
        "deep_explanation": "Islamic jurisprudence demonstrates that Iddah fulfills vital functions across biology, psychology, and sociology:\n1. Scientific & Legal Clarity: If a woman remarried immediately after divorce and became pregnant, paternity would be disputed, leading to conflicts over maintenance, guardianship, and inheritance. Iddah eliminates this ambiguity entirely.\n2. The Reconciliation Buffer: Many divorces occur during emotional anger or temporary stress. Requiring the couple to reside under the same roof during revocable Iddah encourages reflection, apology, and reunion without needing a new dowry or marriage contract.\n3. Respecting the Marital Covenant: When a husband passes away, immediate remarriage would show profound callousness toward the deceased spouse and his grieving family. Four months and ten days honors the sanctity of the shared life.",
        "diagram_title": "The Three Protective Shields of Iddah",
        "svg_func": get_svg_lesson_2,
        "table_title": "Core Dimensions of Hikmah in Iddah",
        "table_headers": ["Dimension", "Social / Biological Problem Prevented", "Islamic Legal Remedy in Iddah"],
        "table_rows": [
            ["Biological & Lineage", "Paternity ambiguity and disputed child inheritance", "Mandatory waiting duration confirms whether pregnancy exists"],
            ["Marital Reconciliation", "Hasty, regretful divorce caused by temporary anger", "Cooling-off home residency enables peaceful spousal reunion"],
            ["Psychological & Grief", "Disrespecting deceased spouse and social pressure", "4 months 10 days of mourning (Hidad) allows healthy emotional recovery"],
            ["Socioeconomic Security", "Sudden abandonment and female impoverishment", "Husband or estate must provide full maintenance (Nafaqah)"]
        ],
        "scenario": "Omar and Fatima have an intense disagreement, and in a moment of anger, Omar pronounces a revocable divorce (Talaq Raj'i). The next morning, both feel remorse but do not know how to approach each other. Because Fatima remains in their home observing her Iddah, they continue their daily household routine. Seeing her care and dedication touches Omar's heart. After two weeks, they sit down, talk calmly, apologize for their harsh words, and Omar says, 'I take you back.' Their marriage is fully restored before the Iddah expires.",
        "real_world": "Apply the 'cooling-off' principle in your own relationships. When you experience a fierce argument with a sibling, classmate, or friend, avoid making irreversible decisions or severing friendships immediately. Give yourself a waiting period of several hours or days to let emotions cool down. Reflect on your own shortcomings and seek reconciliation. Self-restraint is the core of Islamic character (Akhlaq).",
        "reflection": "How does the requirement of keeping a divorced wife in her home during revocable Iddah actively facilitate family reconciliation? Why is immediate physical separation often destructive to marriages?",
        "misconception": "Misconception: Some believe Iddah is an unnecessary ancient relic that modern ultrasound scans make obsolete. In reality, Iddah serves multiple intertwined goals—reconciliation buffer, emotional healing, and psychological closure—that medical scans cannot address.",
        "yt_id": "V7LzN1FmQd0",
        "yt_title": "The Social and Psychological Wisdom of Iddah",
        "yt_desc": "Scholarly discussion on why Islamic law mandates a transition period for family protection and emotional wellbeing.",
        "mcq": {
            "question": "Which of the following is a primary biological and legal rationale for observing the Iddah period?",
            "options": [
                "A. To allow the woman to seek a wealthier spouse.",
                "B. To eliminate confusion regarding the paternity of any future child.",
                "C. To punish the wife for the breakdown of the marriage.",
                "D. To ensure the woman remains unmarried permanently."
            ],
            "answer": "B",
            "explanation": "Verifying pregnancy status is a central legal requirement in Islam to ensure the indisputable attribution of lineage (Nasab), safeguarding children's inheritance and parental care."
        },
        "summary_content": "The wisdom of Iddah encompasses biological lineage protection (Hifz al-Nasab), a family reconciliation buffer for revocable divorce, and an honorable mourning period for widows. It prevents emotional haste, protects children's legal rights, and maintains social harmony across generations.",
        "key_points": [
            "Iddah guarantees certainty of paternity and lineage protection.",
            "It acts as a cooling-off buffer allowing divorced couples to reconcile without a new contract.",
            "It provides widows with psychological space to process grief with dignity.",
            "It reflects the Maqasid al-Shariah: safeguarding faith, life, intellect, lineage, and property."
        ],
        "exit_ticket": "State two reasons why an immediate transition from marriage dissolution to remarriage is socially and emotionally harmful."
    },
    {
        "unit_order": 3,
        "lesson_title": "Rules of iddah",
        "inquiry": "What spiritual and social rules must a woman observe during her Iddah?",
        "hook": "Think of a student preparing for a national examination. During this intensive revision phase, they follow structured rules: they limit social distractions, adhere to a study schedule, and stay in an environment conducive to learning. These boundaries are not punitive; they are designed to guarantee their success. In a similar way, a woman observing Iddah follows specific Islamic guidelines designed to preserve her dignity, protect family integrity, and deepen her connection with Allah.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Al-Masjid_an-Nabawi_in_2017.jpg/800px-Al-Masjid_an-Nabawi_in_2017.jpg",
        "image_title": "Al-Masjid an-Nabawi in Madinah",
        "image_caption": "The Prophet's Mosque in Madinah, from where the noble Prophet (PBUH) taught clear guidance on family ethics, dignity, and bereavement.",
        "concept_name": "Rules Governing Residence, Maintenance, and Mourning (Hidad)",
        "concept_explanation": "The rules of Iddah differ significantly depending on whether the woman is divorced or widowed. For a revocably divorced woman, she resides in the marital home with full financial maintenance (Nafaqah) provided by her husband; she is permitted to beautify herself to encourage reconciliation. For a widow, she observes mourning (Hidad) for four months and ten days, refraining from beauty enhancements (perfume, makeup, flashy jewelry) and remaining in the home where her husband passed away, while being permitted to leave during daylight for essential needs (work, education, medical care). Remarriage and formal marriage proposals are strictly unlawful for all women in Iddah.",
        "scripture_quran": "O Prophet, when you [Muslims] divorce women, divorce them for their prescribed period and count the period... Do not turn them out of their houses, nor should they [themselves] leave...",
        "scripture_quran_ref": "Surah At-Talaq 65:1",
        "scripture_hadith": "A woman who is in her Iddah must remain in her home and not leave unless there is an urgent necessity.",
        "scripture_hadith_ref": "Sahih Muslim 1482",
        "deep_explanation": "A thorough understanding of Iddah rules contrasts two distinct legal contexts:\n1. Revocable Divorcee: She does not observe mourning. The Quran strictly commands the husband not to evict her from the marital house. Her maintenance (housing, food, clothing) is fully funded by the husband. Her presence and beautification in the home are halal and actively facilitate spousal reunion.\n2. Widowed Woman (Hidad): Mourning is an expression of loyalty and grief. She avoids cosmetic adornment, scents, and ostentatious clothing. Crucially, Shariah does not imprison her: she is permitted to leave during daytime hours to teach, run her business, or seek medical care, provided she sleeps in her primary home at night.\n3. Marriage Injunctions: Men are strictly prohibited from formally proposing to a woman in Iddah, preventing social conflict and emotional exploitation during vulnerability.",
        "diagram_title": "Dual Framework: Rules for Divorcees vs Widows",
        "svg_func": get_svg_lesson_3,
        "table_title": "Comparative Analysis of Iddah Regulations",
        "table_headers": ["Legal Aspect", "Divorced Woman (Revocable)", "Widowed Woman (In Mourning)"],
        "table_rows": [
            ["Primary Lodging", "Marital home with husband; eviction is strictly haram", "Home where husband passed away; must sleep there"],
            ["Financial Maintenance", "100% provided by ex-husband as a binding legal duty", "Inheritance share / estate wealth; community aid if needed"],
            ["Beautification / Adornment", "Fully permitted; beautifying is encouraged to aid reunion", "Forbidden (Hidad): avoids makeup, perfume, and flashy jewelry"],
            ["Daytime Movement", "Stays home; leaves only for valid necessity with notice", "Allowed to leave during daytime for work, school, and healthcare"],
            ["Remarriage / Proposals", "Strictly forbidden and legally void", "Strictly forbidden; subtle non-explicit interest hints only"]
        ],
        "scenario": "Amina's husband passed away last week. She works as a primary school teacher in Kisumu to provide for her three young children. An uninformed neighbor tells Amina, 'Since you are observing Iddah, you are completely forbidden from stepping outside your door for four months. You must resign from your teaching post.' Amina consults a local Kadhi, who clarifies: 'Islam is a faith of balance and justice. Because you need to work to sustain your household, you are fully permitted to go to school during the day. Observe modesty, avoid cosmetic perfume and flashy jewelry, and return to sleep in your home each night.'",
        "real_world": "In your community, protect the dignity and livelihoods of women observing Iddah. If a teacher, neighbor, or relative is in this period, do not stigmatize them or believe cultural myths that they are 'unlucky.' Support them by assisting with grocery runs or transport so they can fulfill their religious duties with peace of mind.",
        "reflection": "Why does Islam prohibit other men from proposing marriage to a woman during her Iddah? How does this rule protect her emotional tranquility and prevent inter-family friction?",
        "misconception": "Misconception: Cultural superstitions often dictate that a widow in Iddah must wear black, stay in dark rooms, and avoid speaking to anyone. These practices are cultural fabrications with no basis in the Quran or Sunnah. Widows are encouraged to engage with family and handle daily essentials.",
        "yt_id": "cQkH8B7zNlo",
        "yt_title": "Practical Rules of Iddah and Mourning (Hidad) in Islam",
        "yt_desc": "Fiqh breakdown explaining permissible actions, financial maintenance, and etiquette for women observing Iddah.",
        "mcq": {
            "question": "Which of the following is an accurate Islamic rule for a widow observing her Iddah and mourning (Hidad)?",
            "options": [
                "A. She is strictly forbidden from leaving her house even for medical emergencies.",
                "B. She must wear bright, celebratory clothing and gold jewelry throughout the period.",
                "C. She should avoid luxury beautification (makeup, perfume, flashy jewelry) and sleep in her home, while leaving for daytime essentials.",
                "D. She is legally permitted to marry another man during the first month."
            ],
            "answer": "C",
            "explanation": "A widow observes Hidad by avoiding cosmetic enhancements out of respect for her deceased husband, while being fully permitted to leave the home for necessary daytime activities like work, healthcare, and education."
        },
        "summary_content": "The rules of Iddah reflect balance: divorced women in revocable Iddah reside with their husbands with full maintenance to facilitate reconciliation, while widows observe Hidad (avoiding luxury adornment) while retaining the right to work and attend to daytime necessities.",
        "key_points": [
            "Divorced women receive full financial maintenance (Nafaqah) from their husbands.",
            "Widows observe Hidad for 4 months and 10 days, refraining from beautification.",
            "Widows are permitted to leave home during daytime for essential employment and medical care.",
            "Marriage contracts and formal proposals are strictly prohibited during Iddah."
        ],
        "exit_ticket": "List two key differences between the Iddah rules of a divorced woman and a widowed woman."
    },
    {
        "unit_order": 4,
        "lesson_title": "Importance and support",
        "inquiry": "Why is supporting a woman during her Iddah a vital collective responsibility for the Muslim community?",
        "hook": "Imagine a garden that has just been struck by a violent storm. Several fruit trees have been knocked over, their root systems exposed. If the gardener leaves them unattended, they will wither and die. But if the gardener erects supportive wooden stakes around them, waters them, and shields them from wind, the trees will heal, establish deep roots, and bear fruit once again. A woman undergoing divorce or widowhood has weathered a severe life storm. In this lesson, we examine how Islam commands family and society to act as supportive stakes to restore her strength.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Old_Quran_in_Wazir_Khan_Mosque.jpg/800px-Old_Quran_in_Wazir_Khan_Mosque.jpg",
        "image_title": "Community Sanctuary of Compassion",
        "image_caption": "Historic mosque setting exemplifying the community sanctuary where social welfare, zakat, and widow support are organized.",
        "concept_name": "Socioeconomic Protection & Collective Social Responsibility",
        "concept_explanation": "Iddah is designed as a secure transition protected by divine law, preventing vulnerable women from experiencing financial shock or emotional abandonment. Islamic law enforces binding financial maintenance (Nafaqah) upon the husband in revocable divorce, guaranteeing shelter and sustenance. For widows, the wider Muslim community (Ummah) carries a collective obligation (Fard Kifayah) to provide material, emotional, and social support. The Prophet (PBUH) equated caring for widows with the highest spiritual worship, ensuring society actively shields them from poverty.",
        "scripture_quran": "Lodge them [in a portion] of where you dwell, according to your means, and do not harm them in order to oppress them...",
        "scripture_quran_ref": "Surah At-Talaq 65:6",
        "scripture_hadith": "The one who looks after a widow and a poor person is like a warrior fighting for the cause of Allah...",
        "scripture_hadith_ref": "Sahih al-Bukhari 5353",
        "deep_explanation": "Community and institutional support during Iddah operates across three integrated levels:\n1. Protection from Sudden Homelessness: A husband is legally forbidden from abruptly evicting his divorced wife. Shariah mandates that she remain lodged comfortably according to his financial capacity.\n2. Spiritual Dignity of Care: The Hadith in Sahih al-Bukhari elevates widow care to the spiritual status of continuous night prayer and jihad. This establishes an institutional ethos where supporting widows is viewed as supreme worship.\n3. Preventing Coercion and Abuse: Surah At-Talaq explicitly commands husbands: 'do not harm them in order to oppress them.' Husbands cannot withhold basic necessities or create a toxic living atmosphere to compel the woman to forfeit her financial rights.",
        "diagram_title": "The Circle of Social Support During Iddah",
        "svg_func": get_svg_lesson_4,
        "table_title": "Three Tiers of Social Support During Iddah",
        "table_headers": ["Tier", "Support Provider", "Key Obligations & Responsibilities"],
        "table_rows": [
            ["Tier 1: Spousal / Estate", "Husband or Deceased's Estate", "Provide continuous lodging, food, clothing, and medical expenses without oppression"],
            ["Tier 2: Family Network", "Parents, Siblings, Relatives", "Assist with domestic tasks, childcare, grocery runs, and emotional reassurance"],
            ["Tier 3: Community & Ummah", "Mosque Committees, Zakat Funds, State", "Ensure widow welfare programs, prevent social stigma, and guarantee job protection"]
        ],
        "scenario": "Zainab's husband passed away unexpectedly, leaving her with four young children. She is anxious about how she will feed her family during her Iddah since she cannot work long hours outside. The local mosque committee in Mombasa holds a meeting. They assign volunteers to deliver nutritious weekly groceries to her door, and a youth team offers to walk her children to school and assist with tutoring. Zainab completes her Iddah in security, feeling the compassionate warmth of the Muslim community.",
        "real_world": "Identify widowed or divorced mothers in your school or neighborhood. Collaborate with your classmates or youth group to support them respectfully: offer free tutoring to their younger children, assist with carrying heavy loads from the market, or simply greet them with dignity. These actions embody the Islamic principle of social justice ('Adl) and earn vast divine rewards.",
        "reflection": "How does guaranteeing financial maintenance and housing for a divorced woman during Iddah prevent socioeconomic vulnerability and exploitation in society?",
        "misconception": "Misconception: Some think that once divorce is pronounced, the husband's financial obligations end instantly. Islamic law strictly mandates that the husband must house and feed his divorced wife throughout the entire duration of her Iddah.",
        "yt_id": "rJ3wR3L4q8M",
        "yt_title": "The Rights of Divorced Women and Widows in Islam",
        "yt_desc": "Exploration of the legal rights, community obligations, and financial protections granted to women during marital transitions.",
        "mcq": {
            "question": "According to Surah At-Talaq (65:6), what is the husband's mandatory obligation toward his divorced wife during her Iddah?",
            "options": [
                "A. He must evict her immediately so she can find alternative lodging.",
                "B. He must provide her with housing and maintenance according to his financial means.",
                "C. He has no financial obligations once the divorce is uttered.",
                "D. He must pay a state fine but is forbidden from allowing her in the home."
            ],
            "answer": "B",
            "explanation": "The Quran strictly commands husbands to lodge their divorced wives where they dwell according to their means, and forbids them from causing harm or oppression during the waiting period."
        },
        "summary_content": "Supporting women during Iddah is a shared Islamic obligation spanning spousal financial maintenance, family domestic assistance, and community welfare. By treating widow care as an act of supreme worship, Islam shields women from financial hardship and social isolation.",
        "key_points": [
            "Divorced women possess an absolute legal right to housing and maintenance (Nafaqah).",
            "The Prophet (PBUH) compared caring for widows to fighting in the cause of Allah.",
            "Family and community networks must provide practical and emotional solidarity.",
            "Preventing harm and coercion during transition periods is an explicit Quranic command."
        ],
        "exit_ticket": "State one Quranic verse reference and one Hadith proof demonstrating Islam's mandate to support women during Iddah."
    },
    {
        "unit_order": 5,
        "lesson_title": "Unit synthesis",
        "inquiry": "How do we unify our understanding of Iddah as a protective, spiritual, and social shield in Islam?",
        "hook": "Imagine compiling a master health and safety protocol for an international airport. You must include the physical fire safety systems, the electronic security scanners, the emergency medical protocols, and the training of airport personnel. If any single component is omitted, the entire safety infrastructure is compromised. In this final synthesis lesson, we unite all dimensions of Iddah—the categories, divine rationale, operational rules, and community support—to recognize Iddah as a master shield of social justice and compassion in Islam.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Samarkand_Kufic_Quran.jpg/800px-Samarkand_Kufic_Quran.jpg",
        "image_title": "Historic Kufic Qur'anic Codex",
        "image_caption": "Ancient Qur'anic codex reflecting the enduring, timeless authority of divine legislation in safeguarding family stability.",
        "concept_name": "The Master Architecture of Iddah as an Institution of Justice",
        "concept_explanation": "Iddah is a comprehensive institution of Islamic family law that harmonizes personal submission to Allah (Ibadah) with biological clarity, family reconciliation, psychological healing, and economic protection. Far from being a restrictive convention, it balances the rights of husbands, wives, and children, preserving the foundational fabric of the Ummah. By viewing Iddah through the holistic lens of Maqasid al-Shariah, learners recognize how divine law proactively prevents social decay and uplifts human dignity.",
        "scripture_quran": "...These are the limits [set by] Allah, and whoever transgresses the limits of Allah has certainly wronged himself...",
        "scripture_quran_ref": "Surah At-Talaq 65:1",
        "scripture_hadith": "The believers are but brothers, so make peace between your brothers and fear Allah that you may receive mercy.",
        "scripture_hadith_ref": "Surah Al-Hujurat 49:10",
        "deep_explanation": "Synthesizing the complete sub-strand yields four interlocking pillars of understanding:\n1. The Biological Pillar: Clarifying pregnancy through specific cycles or lunar months guarantees accurate attribution of paternity (Nasab) and protects child inheritance.\n2. The Relational Pillar: In revocable divorce, Iddah serves as a cooling-off bridge enabling couples to overcome momentary disputes and rebuild their family.\n3. The Ethical & Psychological Pillar: Prescribing Hidad for widows directs the heart toward remembrance, honoring the deceased spouse while shielding the woman from premature social pressures.\n4. The Socioeconomic Pillar: Enforcing Nafaqah and mobilizing community charity ensures women do not endure sudden financial crisis or homelessness during bereavement.",
        "diagram_title": "Master Synthesis: The Temple of Comprehensive Protection",
        "svg_func": get_svg_lesson_5,
        "table_title": "Master Unit Synthesis Framework: Four Pillars of Iddah",
        "table_headers": ["Pillar", "Divine Purpose (Hikmah)", "Practical Regulation in Shariah", "Socio-Spiritual Outcome"],
        "table_rows": [
            ["1. Biological", "Verify womb status & protect lineage", "3 cycles (divorcee) / until birth (pregnant)", "Preserves child rights and inheritance"],
            ["2. Relational", "Cooling-off buffer to prevent hasty separation", "Wife stays in marital home during Talaq Raj'i", "Reconciliation without new contract"],
            ["3. Ethical", "Dignified mourning & psychological space", "Hidad (modesty, no perfume/jewelry) for widows", "Honors deceased spouse and grief"],
            ["4. Economic", "Prevent sudden poverty & vulnerability", "Nafaqah by husband + community welfare", "Complete socioeconomic safety net"]
        ],
        "scenario": "A student named Yusuf remarks: 'Iddah seems like an outdated custom that restricts women's freedom.' His classmate Maryam applies the unit synthesis to reply: 'Actually, Yusuf, when you study Islamic family law deeply, you see that Iddah is an advanced system of justice. Biologically, it safeguards the unborn child's identity and inheritance. Emotionally, it provides a cooling-off period that saves marriages from hasty anger. Economically, it guarantees housing and food so women are never abandoned. And for widows, it honors grief and shields them from pressure. It is a compassionate shield, not a restriction.'",
        "real_world": "Prepare an educational infographic or summary leaflet on 'The Wisdom and Protections of Iddah' for your school Madrasa or Islamic Society notice board. Highlight how Shariah protects the legal, financial, and emotional rights of women, dispelling widespread cultural superstitions.",
        "reflection": "How does studying the comprehensive architecture of Iddah transform your perception of Islamic family law from mere legal rules to an enlightened framework of mercy and social justice?",
        "misconception": "Misconception: Believing that modern legal systems have surpassed the need for Iddah. In truth, modern family courts worldwide struggle with disputes over child support, custody, and post-divorce homelessness—challenges that Islamic Shariah resolved over 1,400 years ago through the balanced duties of Iddah.",
        "yt_id": "kX7F5sF9k2w",
        "yt_title": "Summary of Islamic Family Law: The Institution of Iddah",
        "yt_desc": "Comprehensive review of the categories, wisdom, rules, and community responsibilities of Iddah in Islamic jurisprudence.",
        "mcq": {
            "question": "A classmate says: 'Iddah restricts women without any purpose.' Applying the full synthesis of this unit, which of the following is the most source-grounded response?",
            "options": [
                "A. 'It is an ancient tradition that we must follow blindly without inquiry.'",
                "B. 'Iddah is a balanced legal shield protecting child lineage, offering reconciliation opportunities, and guaranteeing socioeconomic security during transition.'",
                "C. 'Iddah is exclusively designed to penalize women for marital breakdown.'",
                "D. 'Iddah is completely optional if medical tests are conducted.'"
            ],
            "answer": "B",
            "explanation": "This option captures the holistic synthesis of Iddah: biological lineage protection, marital reconciliation, psychological healing, and guaranteed financial security under Maqasid al-Shariah."
        },
        "summary_content": "The institution of Iddah represents a master architecture of divine justice, safeguarding lineage, facilitating family reconciliation, honoring bereavement, and guaranteeing socioeconomic maintenance. It balances the rights of all family members, reflecting the mercy and wisdom of Islamic Shariah.",
        "key_points": [
            "Iddah integrates biological clarity, family reconciliation, and dignified bereavement.",
            "Observing Iddah is an act of worship (ibadah) grounded in submission to Allah.",
            "Husbands and communities carry binding duties to guarantee financial and social support.",
            "Islamic family law protects vulnerable individuals through comprehensive, balanced legislation."
        ],
        "exit_ticket": "Write down the single most important insight you gained regarding Iddah and how you will use it to educate others in your community."
    }
]


# ─────────────────────────────────────────────────────────────────────────────
# INGESTION EXECUTION FUNCTION
# ─────────────────────────────────────────────────────────────────────────────

def ingest_grade9_ire_topic13():
    print("=" * 80)
    print("STARTING INGESTION: GRADE 9 IRE — TOPIC 13: IDDAH (THE WAITING PERIOD)")
    print("=" * 80)

    try:
        topic = Topic.objects.get(id=353)
    except Topic.DoesNotExist:
        print("ERROR: Topic ID 353 does not exist! Please create topic record first.")
        sys.exit(1)

    print(f"Target Topic: ID={topic.id}, Name='{topic.name}', Order={topic.order}")

    # Validate all SVGs before database transactions
    print("\nValidating all 5 custom vector SVGs for XML compliance...")
    for idx, cfg in enumerate(LESSONS_CONFIG, 1):
        svg_content = cfg["svg_func"]()
        try:
            ET.fromstring(svg_content)
            print(f"  [✓] SVG {idx}/5 ('{cfg['diagram_title']}') is valid XML.")
        except ET.ParseError as e:
            print(f"  [✗] XML Parse Error in SVG {idx}: {e}")
            sys.exit(1)

    with transaction.atomic():
        # Clean existing units if any
        existing_units = LearningUnit.objects.filter(topic=topic)
        if existing_units.exists():
            print(f"\nCleaning {existing_units.count()} existing units under Topic {topic.id}...")
            existing_units.delete()

        total_units = 0
        total_lessons = 0
        total_blocks = 0
        total_assets = 0

        for cfg in LESSONS_CONFIG:
            u_order = cfg["unit_order"]
            l_title = cfg["lesson_title"]

            # 1. Create LearningUnit
            unit = LearningUnit.objects.create(
                topic=topic,
                name=f"Lesson 6.2.{u_order}: {l_title}",
                order=u_order,
                description=clean_text(cfg["concept_explanation"][:250] + "...")
            )
            total_units += 1

            # 2. Create Published Lesson
            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=clean_text(l_title),
                status="published",
                version=1
            )
            total_lessons += 1

            # ─────────────────────────────────────────────────────────────────
            # CARD 1 (Page 1): Orientation & Hook (2 blocks)
            # ─────────────────────────────────────────────────────────────────
            img_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                title=clean_text(cfg["image_title"]),
                url=cfg["image_url"],
                metadata={
                    "caption": clean_text(cfg["image_caption"]),
                    "credit": "Wikimedia Commons"
                }
            )
            total_assets += 1

            b_img = LessonBlock.objects.create(
                lesson=lesson,
                page_number=1,
                page_title="Orientation & Hook",
                order=10,
                component_order=1,
                block_type="suggested_image",
                component_type="suggested_image",
                title=clean_text(cfg["image_title"]),
                content={
                    "title": clean_text(cfg["image_title"]),
                    "caption": clean_text(cfg["image_caption"]),
                    "url": cfg["image_url"]
                }
            )
            b_img.assets.add(img_asset)

            LessonBlock.objects.create(
                lesson=lesson,
                page_number=1,
                page_title="Orientation & Hook",
                order=20,
                component_order=2,
                block_type="learning_goal",
                component_type="learning_goal",
                title="Lesson Orientation & Inquiry",
                content={
                    "title": "Lesson Orientation & Inquiry",
                    "inquiry_question": clean_text(cfg["inquiry"]),
                    "hook": clean_text(cfg["hook"]),
                    "learning_goals": [
                        f"Understand the core meaning and rulings of {l_title}",
                        "Examine foundational Qur'anic verses and Hadith citations",
                        "Analyze practical real-life scenarios and social responsibilities"
                    ]
                }
            )

            # ─────────────────────────────────────────────────────────────────
            # CARD 2 (Page 2): Core Theological Concept (2 blocks)
            # ─────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=2,
                page_title="Core Theological Concept",
                order=30,
                component_order=1,
                block_type="concept_explanation",
                component_type="concept_explanation",
                title=clean_text(cfg["concept_name"]),
                content={
                    "title": clean_text(cfg["concept_name"]),
                    "explanation": clean_text(cfg["concept_explanation"]),
                    "text": clean_text(cfg["concept_explanation"])
                }
            )

            LessonBlock.objects.create(
                lesson=lesson,
                page_number=2,
                page_title="Core Theological Concept",
                order=40,
                component_order=2,
                block_type="callout",
                component_type="callout",
                title="Scripture Source Panel",
                content={
                    "title": "Scripture Source Panel",
                    "callout_type": "scripture",
                    "quran_verse": clean_text(cfg["scripture_quran"]),
                    "quran_reference": clean_text(cfg["scripture_quran_ref"]),
                    "hadith_text": clean_text(cfg["scripture_hadith"]),
                    "hadith_reference": clean_text(cfg["scripture_hadith_ref"]),
                    "text": clean_text(
                        f"**Qur'an ({cfg['scripture_quran_ref']}):**\n> \"{cfg['scripture_quran']}\"\n\n"
                        f"**Primary Reference ({cfg['scripture_hadith_ref']}):**\n> \"{cfg['scripture_hadith']}\""
                    )
                }
            )

            # ─────────────────────────────────────────────────────────────────
            # CARD 3 (Page 3): Deep Explanation & SVG Diagram (3 blocks)
            # ─────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=3,
                page_title="Deep Pedagogical Explanation",
                order=50,
                component_order=1,
                block_type="concept_explanation",
                component_type="concept_explanation",
                title="Theological Analysis & Principles",
                content={
                    "title": "Theological Analysis & Principles",
                    "explanation": clean_text(cfg["deep_explanation"]),
                    "text": clean_text(cfg["deep_explanation"])
                }
            )

            svg_str = cfg["svg_func"]()
            svg_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                title=clean_text(cfg["diagram_title"]),
                metadata={
                    "svg_xml": svg_str,
                    "svg_content": svg_str,
                    "theme": "#0f172a",
                    "viewBox": "0 0 880 440",
                    "responsive": True
                }
            )
            total_assets += 1

            b_diag = LessonBlock.objects.create(
                lesson=lesson,
                page_number=3,
                page_title="Deep Pedagogical Explanation",
                order=60,
                component_order=2,
                block_type="suggested_diagram",
                component_type="suggested_diagram",
                title=clean_text(cfg["diagram_title"]),
                content={
                    "title": clean_text(cfg["diagram_title"]),
                    "svg_xml": svg_str,
                    "svg_content": svg_str
                },
                metadata={
                    "svg_xml": svg_str,
                    "svg_content": svg_str
                }
            )
            b_diag.assets.add(svg_asset)

            LessonBlock.objects.create(
                lesson=lesson,
                page_number=3,
                page_title="Deep Pedagogical Explanation",
                order=70,
                component_order=3,
                block_type="comparison_table",
                component_type="comparison_table",
                title=clean_text(cfg["table_title"]),
                content={
                    "title": clean_text(cfg["table_title"]),
                    "headers": [clean_text(h) for h in cfg["table_headers"]],
                    "rows": [[clean_text(c) for c in row] for row in cfg["table_rows"]]
                }
            )

            # ─────────────────────────────────────────────────────────────────
            # CARD 4 (Page 4): Lived Reality Scenario (1 block)
            # ─────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=4,
                page_title="Lived Reality Scenario",
                order=80,
                component_order=1,
                block_type="worked_example",
                component_type="worked_example",
                title="Practical Student Scenario",
                content={
                    "title": "Practical Student Scenario",
                    "scenario": clean_text(cfg["scenario"]),
                    "text": clean_text(cfg["scenario"])
                }
            )

            # ─────────────────────────────────────────────────────────────────
            # CARD 5 (Page 5): Real-World Ethics & Video (4 blocks)
            # ─────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=5,
                page_title="Application & Reflection",
                order=90,
                component_order=1,
                block_type="real_world_example",
                component_type="real_world_example",
                title="Real-World Ethical Action",
                content={
                    "title": "Real-World Ethical Action",
                    "application": clean_text(cfg["real_world"]),
                    "text": clean_text(cfg["real_world"])
                }
            )

            LessonBlock.objects.create(
                lesson=lesson,
                page_number=5,
                page_title="Application & Reflection",
                order=100,
                component_order=2,
                block_type="reflection",
                component_type="reflection",
                title="Introspective Prompt",
                content={
                    "title": "Introspective Prompt",
                    "prompt": clean_text(cfg["reflection"]),
                    "text": clean_text(cfg["reflection"])
                }
            )

            LessonBlock.objects.create(
                lesson=lesson,
                page_number=5,
                page_title="Application & Reflection",
                order=110,
                component_order=3,
                block_type="common_misconception",
                component_type="common_misconception",
                title="Misconception Check",
                content={
                    "title": "Misconception Check",
                    "content": clean_text(cfg["misconception"]),
                    "correction": clean_text(cfg["misconception"]),
                    "text": clean_text(cfg["misconception"])
                }
            )

            yt_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="video",
                title=clean_text(cfg["yt_title"]),
                url=f"https://www.youtube.com/watch?v={cfg['yt_id']}",
                metadata={
                    "youtube_id": cfg["yt_id"],
                    "description": clean_text(cfg["yt_desc"])
                }
            )
            total_assets += 1

            b_vid = LessonBlock.objects.create(
                lesson=lesson,
                page_number=5,
                page_title="Application & Reflection",
                order=120,
                component_order=4,
                block_type="suggested_video",
                component_type="suggested_video",
                title=clean_text(cfg["yt_title"]),
                content={
                    "title": clean_text(cfg["yt_title"]),
                    "description": clean_text(cfg["yt_desc"]),
                    "url": f"https://www.youtube.com/watch?v={cfg['yt_id']}",
                    "youtube_id": cfg["yt_id"]
                }
            )
            b_vid.assets.add(yt_asset)

            # ─────────────────────────────────────────────────────────────────
            # CARD 6 (Page 6): Knowledge Mastery Check (1 block)
            # ─────────────────────────────────────────────────────────────────
            mcq_data = cfg["mcq"]
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=6,
                page_title="Knowledge Mastery Check",
                order=130,
                component_order=1,
                block_type="knowledge_check",
                component_type="knowledge_check",
                title="Mastery Knowledge Check",
                content={
                    "title": "Mastery Knowledge Check",
                    "question": clean_text(mcq_data["question"]),
                    "options": [clean_text(opt) for opt in mcq_data["options"]],
                    "answer": clean_text(mcq_data["answer"]),
                    "correct_answer": clean_text(mcq_data["answer"]),
                    "explanation": clean_text(mcq_data["explanation"])
                }
            )

            # ─────────────────────────────────────────────────────────────────
            # CARD 7 (Page 7): Summary & Exit Ticket (2 blocks)
            # ─────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=7,
                page_title="Summary & Exit Ticket",
                order=140,
                component_order=1,
                block_type="summary",
                component_type="summary",
                title="Summary & Vocabulary Review",
                content={
                    "title": "Summary & Vocabulary Review",
                    "content": clean_text(cfg["summary_content"]),
                    "text": clean_text(cfg["summary_content"]),
                    "takeaways": [clean_text(p) for p in cfg["key_points"]]
                }
            )

            LessonBlock.objects.create(
                lesson=lesson,
                page_number=7,
                page_title="Summary & Exit Ticket",
                order=150,
                component_order=2,
                block_type="mini_activity",
                component_type="mini_activity",
                title="Exit Ticket & Action Step",
                content={
                    "title": "Exit Ticket & Action Step",
                    "content": clean_text(cfg["exit_ticket"]),
                    "text": clean_text(cfg["exit_ticket"])
                }
            )

            total_blocks += 15
            print(f"  [+] Ingested Lesson {u_order}/5: '{l_title}' (7 cards, 15 blocks, 3 assets)")

    print("=" * 80)
    print("TOPIC 13 INGESTION COMPLETE & VERIFIED!")
    print(f"  LearningUnits : {total_units} / 5")
    print(f"  Lessons       : {total_lessons} / 5 (Published)")
    print(f"  Blocks        : {total_blocks} (15 per lesson, 7 pages)")
    print(f"  Assets        : {total_assets} (5 SVGs, 5 images, 5 videos)")
    print("=" * 80)


if __name__ == "__main__":
    ingest_grade9_ire_topic13()
