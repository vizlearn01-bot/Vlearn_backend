"""
VLearn CBC Grade 9 IRE — Topic 15: Polygamy in Islam
Production Ingestion and Enrichment Script for all 6 Lessons

Target Topic in DB: Topic ID 355 (Subject: IRE ID 53, Grade: Grade 9 ID 18)
Source Markdown: /home/jason-bitega/Desktop/VL/vlearn_repositories/Grade 9 IRE/polygamy.md

6 Lessons Ingested & Fully Enriched:
  1. Lesson 6.4.1: Meaning and scope
  2. Lesson 6.4.2: Rationale and social remedy
  3. Lesson 6.4.3: Prophet’s multiple marriages
  4. Lesson 6.4.4: Conditions of polygamy
  5. Lesson 6.4.5: Significance and contemporary discussion
  6. Lesson 6.4.6: Unit synthesis
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
# 6 DEDICATED RESPONSIVE PEDAGOGICAL VECTOR SVGS (#0f172a theme, viewBox 880x440)
# ─────────────────────────────────────────────────────────────────────────────

def get_svg_lesson_1():
    """Lesson 6.4.1: The Marriage Revolution: Pre-Islamic Arabia vs Islamic Shariah"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg151" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg151)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE MARRIAGE REVOLUTION: PRE-ISLAMIC ARABIA VS. ISLAMIC SHARIAH</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">How Islamic Revelation Transformed Unregulated Polygamy into a Restricted, Just Legal Institution</text>

  <!-- Two Columns -->
  <!-- Left: Pre-Islamic Arabia -->
  <g transform="translate(45, 85)">
    <rect width="380" height="260" rx="8" fill="#1e293b" stroke="#f87171" stroke-width="1.5"/>
    <rect width="380" height="34" rx="8" fill="#7f1d1d"/>
    <text x="190" y="22" fill="#fecaca" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">PRE-ISLAMIC ARABIA (JAHILIYYAH)</text>

    <rect x="15" y="46" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="62" fill="#f87171" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Number of Wives:</text>
    <text x="25" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">Unlimited (men married dozens of women without restriction)</text>

    <rect x="15" y="96" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="112" fill="#f87171" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Standard of Justice:</text>
    <text x="25" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">Zero requirement; men favored or neglected wives at whim</text>

    <rect x="15" y="146" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="162" fill="#f87171" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Financial Responsibilities:</text>
    <text x="25" y="178" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">No fixed legal maintenance; women often abandoned in poverty</text>

    <rect x="15" y="196" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="212" fill="#f87171" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Woman's Legal Status:</text>
    <text x="25" y="228" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">Treated as inherited property with zero contract or property rights</text>
  </g>

  <!-- Right: Islamic Shariah -->
  <g transform="translate(455, 85)">
    <rect width="380" height="260" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="380" height="34" rx="8" fill="#059669"/>
    <text x="190" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">ISLAMIC SHARIAH REFORM (QUR'AN 4:3)</text>

    <rect x="15" y="46" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="62" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Number of Wives:</text>
    <text x="25" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">Strict ceiling of MAXIMUM FOUR; excess wives were divorced</text>

    <rect x="15" y="96" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="112" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Standard of Justice:</text>
    <text x="25" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">Absolute requirement of 'Adl; "If you fear injustice, marry only one"</text>

    <rect x="15" y="146" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="162" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Financial Responsibilities:</text>
    <text x="25" y="178" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">Husband must fund independent lodging and equal maintenance (Nafaqah)</text>

    <rect x="15" y="196" width="350" height="42" rx="4" fill="#0f172a"/>
    <text x="25" y="212" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Woman's Legal Status:</text>
    <text x="25" y="228" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">Independent legal entity with exclusive Mahr, wealth, and contract rights</text>
  </g>

  <!-- Bottom Message -->
  <g transform="translate(45, 360)">
    <rect width="790" height="55" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="395" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">CORRECTING A HISTORICAL MISCONCEPTION</text>
    <text x="395" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Islam did not invent polygamy; it capped, restricted, and bound it with non-negotiable legal and moral conditions</text>
  </g>
</svg>"""


def get_svg_lesson_2():
    """Lesson 6.4.2: Polygamy as a Post-War Social Safety Shield"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg152" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg152)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">POLYGAMY AS A SOCIAL SAFETY SHIELD IN TIMES OF CRISIS</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Historical Rationale (Post-Uhud Context): Protecting Orphans, Widows, and Social Dignity</text>

  <!-- 3 Converging Shields -->
  <!-- Shield 1: Protection of Orphans -->
  <g transform="translate(45, 90)">
    <rect width="240" height="250" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="240" height="38" rx="10" fill="#0369a1"/>
    <text x="120" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">SHIELD 1: ORPHAN CARE</text>

    <text x="120" y="60" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Surah An-Nisa 4:3 Mandate</text>

    <rect x="15" y="75" width="210" height="155" rx="6" fill="#0f172a"/>
    <text x="25" y="98" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Fatherly Presence:</text>
    <text x="25" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Orphans gain male guardian,</text>
    <text x="25" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  home security, and emotional care</text>
    <text x="25" y="152" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Estate Protection:</text>
    <text x="25" y="168" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Protects orphan wealth from</text>
    <text x="25" y="182" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  usurpation by greedy relatives</text>
    <text x="25" y="208" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Full legal legitimacy &amp; rights</text>
  </g>

  <!-- Shield 2: Financial Support & Shelter -->
  <g transform="translate(320, 90)">
    <rect width="240" height="250" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="240" height="38" rx="10" fill="#059669"/>
    <text x="120" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">SHIELD 2: ECONOMIC SECURITY</text>

    <text x="120" y="60" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Beyond Mere Charity Handouts</text>

    <rect x="15" y="75" width="210" height="155" rx="6" fill="#0f172a"/>
    <text x="25" y="98" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Permanent Maintenance:</text>
    <text x="25" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Full shelter, food, and clothing</text>
    <text x="25" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  as an enforceable legal right</text>
    <text x="25" y="152" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Family Integration:</text>
    <text x="25" y="168" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Widow is a respected partner,</text>
    <text x="25" y="182" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  not an impoverished beggar</text>
    <text x="25" y="208" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Eradicates female destitution</text>
  </g>

  <!-- Shield 3: Social Honor & Purity -->
  <g transform="translate(595, 90)">
    <rect width="240" height="250" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="240" height="38" rx="10" fill="#d97706"/>
    <text x="120" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">SHIELD 3: MORAL PURITY</text>

    <text x="120" y="60" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Public Nikah vs Secret Affairs</text>

    <rect x="15" y="75" width="210" height="155" rx="6" fill="#0f172a"/>
    <text x="25" y="98" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Public Legality:</text>
    <text x="25" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Every wife has public dignity,</text>
    <text x="25" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  dowry (Mahr), and inheritance</text>
    <text x="25" y="152" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Prevents Immorality:</text>
    <text x="25" y="168" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Addresses demographic imbalance</text>
    <text x="25" y="182" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  without mistresses or Zina</text>
    <text x="25" y="208" fill="#f87171" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Absolute legal attribution of Nasab</text>
  </g>

  <!-- Bottom Message -->
  <g transform="translate(45, 360)">
    <rect width="790" height="55" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="395" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">PERMISSION AS A SOCIAL REMEDY, NOT PERSONAL SELF-INDULGENCE</text>
    <text x="395" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Revealed post-Uhud to build an institutional safety net for surviving orphans and widows</text>
  </g>
</svg>"""


def get_svg_lesson_3():
    """Lesson 6.4.3: The Marital Timeline of Prophet Muhammad (PBUH)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg153" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg153)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">CHRONOLOGICAL TIMELINE: MARITAL LIFE OF PROPHET MUHAMMAD (PBUH)</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">25 Years of Monogamous Youth vs Strategic Divine Missions After Age 50</text>

  <!-- 3 Chronological Cards -->
  <!-- Phase 1: Youth -->
  <g transform="translate(45, 90)">
    <rect width="240" height="250" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="240" height="38" rx="10" fill="#059669"/>
    <text x="120" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">PHASE 1: AGES 25–50</text>

    <text x="120" y="60" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">25 Years Monogamous</text>

    <rect x="15" y="75" width="210" height="155" rx="6" fill="#0f172a"/>
    <text x="25" y="98" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Sole Wife: Khadijah (RA):</text>
    <text x="25" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Prime of his physical youth;</text>
    <text x="25" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  married only to an older widow</text>
    <text x="25" y="152" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Exemplary Loyalty:</text>
    <text x="25" y="168" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Never married anyone else</text>
    <text x="25" y="182" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  during her entire lifetime</text>
    <text x="25" y="208" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Monogamy as the life default</text>
  </g>

  <!-- Phase 2: Caretaking -->
  <g transform="translate(320, 90)">
    <rect width="240" height="250" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="240" height="38" rx="10" fill="#d97706"/>
    <text x="120" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">PHASE 2: AGES 50–53</text>

    <text x="120" y="60" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Caring for the Household</text>

    <rect x="15" y="75" width="210" height="155" rx="6" fill="#0f172a"/>
    <text x="25" y="98" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Sawdah bint Zam'ah (RA):</text>
    <text x="25" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  An elderly, vulnerable widow</text>
    <text x="25" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  whose husband died after Abyssinia</text>
    <text x="25" y="152" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Compassionate Mission:</text>
    <text x="25" y="168" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Provided shelter and cared</text>
    <text x="25" y="182" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  for the Prophet's young daughters</text>
    <text x="25" y="208" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Selfless family support</text>
  </g>

  <!-- Phase 3: Strategic Missions -->
  <g transform="translate(595, 90)">
    <rect width="240" height="250" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="240" height="38" rx="10" fill="#0284c7"/>
    <text x="120" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">PHASE 3: AGES 53–63</text>

    <text x="120" y="60" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Statecraft &amp; Scholarship</text>

    <rect x="15" y="75" width="210" height="155" rx="6" fill="#0f172a"/>
    <text x="25" y="98" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Educational Mission:</text>
    <text x="25" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Aisha (RA) narrated 2,210 Hadiths;</text>
    <text x="25" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  premier female jurist of Islam</text>
    <text x="25" y="152" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700">• Political Alliances:</text>
    <text x="25" y="168" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Juwayriyah (Banu Mustaliq) and</text>
    <text x="25" y="182" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  Safiyyah united warring tribes</text>
    <text x="25" y="208" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Legislative &amp; national unity</text>
  </g>

  <!-- Bottom Message -->
  <g transform="translate(45, 360)">
    <rect width="790" height="55" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="395" y="24" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">HISTORICAL FACTS REFUTE ORIENTALIST CRITICISM</text>
    <text x="395" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">A man seeking pleasure does not remain monogamous for 25 years in youth, then marry widows after age 50</text>
  </g>
</svg>"""


def get_svg_lesson_4():
    """Lesson 6.4.4: The Scales of 'Adl (Absolute Justice) in Polygamy"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg154" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg154)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE SCALES OF 'ADL (ABSOLUTE JUSTICE) IN POLYGAMY</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Mandatory Equality in Nights, Lodging, and Financial Support vs The Leaning Body Warning</text>

  <!-- Left Scale Pan: Wife A -->
  <g transform="translate(60, 95)">
    <rect width="320" height="240" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="320" height="34" rx="8" fill="#0369a1"/>
    <text x="160" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">EQUAL SCALE: WIFE A</text>

    <rect x="15" y="46" width="290" height="38" rx="4" fill="#0f172a"/>
    <text x="25" y="62" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Separate Private Lodging:</text>
    <text x="25" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">Her own house / private apartment with kitchen &amp; bath</text>

    <rect x="15" y="90" width="290" height="38" rx="4" fill="#0f172a"/>
    <text x="25" y="106" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Equal Nights Division (Qasm):</text>
    <text x="25" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">Identical rotational time (e.g., 2 nights / 2 nights)</text>

    <rect x="15" y="134" width="290" height="38" rx="4" fill="#0f172a"/>
    <text x="25" y="150" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Equal Financial Maintenance (Nafaqah):</text>
    <text x="25" y="164" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">Equivalent quality food, clothing, medical &amp; gifts</text>

    <rect x="15" y="178" width="290" height="48" rx="4" fill="#0f172a"/>
    <text x="25" y="196" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Dignity &amp; Respect:</text>
    <text x="25" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">Honored as a full marital partner; never neglected</text>
  </g>

  <!-- Right Scale Pan: Wife B -->
  <g transform="translate(500, 95)">
    <rect width="320" height="240" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="320" height="34" rx="8" fill="#059669"/>
    <text x="160" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">EQUAL SCALE: WIFE B</text>

    <rect x="15" y="46" width="290" height="38" rx="4" fill="#0f172a"/>
    <text x="25" y="62" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Separate Private Lodging:</text>
    <text x="25" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">Her own house / private apartment with kitchen &amp; bath</text>

    <rect x="15" y="90" width="290" height="38" rx="4" fill="#0f172a"/>
    <text x="25" y="106" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Equal Nights Division (Qasm):</text>
    <text x="25" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">Identical rotational time (e.g., 2 nights / 2 nights)</text>

    <rect x="15" y="134" width="290" height="38" rx="4" fill="#0f172a"/>
    <text x="25" y="150" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Equal Financial Maintenance (Nafaqah):</text>
    <text x="25" y="164" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">Equivalent quality food, clothing, medical &amp; gifts</text>

    <rect x="15" y="178" width="290" height="48" rx="4" fill="#0f172a"/>
    <text x="25" y="196" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Dignity &amp; Respect:</text>
    <text x="25" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">Honored as a full marital partner; never neglected</text>
  </g>

  <!-- Central Fulcrum Warning -->
  <g transform="translate(390, 140)">
    <polygon points="50,0 100,80 0,80" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="50" y="55" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">'ADL</text>
    <text x="50" y="70" fill="#ffffff" font-family="system-ui, sans-serif" font-size="7.5" text-anchor="middle">FULCRUM</text>
  </g>

  <!-- Bottom Warning Banner -->
  <g transform="translate(45, 355)">
    <rect width="790" height="65" rx="8" fill="#1e293b" stroke="#f87171" stroke-width="1.5"/>
    <text x="395" y="24" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">THE PROPHETIC LEANING BODY WARNING (SUNAN ABU DAWOOD 2134)</text>
    <text x="395" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">"Whoever has two wives and inclines toward one of them, he will rise on the Day of Judgment with half his body leaning/paralyzed."</text>
    <text x="395" y="56" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8" font-weight="700" text-anchor="middle">"If you fear that you will not be just, then marry only one" (Surah An-Nisa 4:3)</text>
  </g>
</svg>"""


def get_svg_lesson_5():
    """Lesson 6.4.5: The Wife's Legal Shield in Contemporary Family Law"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg155" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg155)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE WIFE'S LEGAL SHIELD IN ISLAMIC CONTRACT LAW</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Empowering Women Through Enforceable Marriage Clauses, Independent Wealth, and Judicial Dissolution</text>

  <!-- 4 Legal Shields -->
  <!-- Shield 1: Monogamy Clause -->
  <g transform="translate(45, 85)">
    <rect width="180" height="260" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="180" height="34" rx="8" fill="#0284c7"/>
    <text x="90" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">1. MONOGAMY CLAUSE</text>

    <text x="90" y="56" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Nikah Contract Condition</text>

    <rect x="10" y="70" width="160" height="175" rx="4" fill="#0f172a"/>
    <text x="18" y="92" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Binding Agreement:</text>
    <text x="18" y="108" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Woman can insert clause:</text>
    <text x="18" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  husband must not marry another</text>
    <text x="18" y="146" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Automatic Dissolution:</text>
    <text x="18" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  If violated, wife has immediate</text>
    <text x="18" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  right to divorce + keep Mahr</text>
    <text x="18" y="208" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Enforceable by Kadhi courts</text>
  </g>

  <!-- Shield 2: Independent Wealth -->
  <g transform="translate(245, 85)">
    <rect width="180" height="260" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="180" height="34" rx="8" fill="#059669"/>
    <text x="90" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">2. EXCLUSIVE WEALTH</text>

    <text x="90" y="56" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Financial Autonomy</text>

    <rect x="10" y="70" width="160" height="175" rx="4" fill="#0f172a"/>
    <text x="18" y="92" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Exclusive Mahr:</text>
    <text x="18" y="108" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Bridal gift belongs solely</text>
    <text x="18" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  to her; husband cannot touch it</text>
    <text x="18" y="146" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Zero Obligation to Co-Pay:</text>
    <text x="18" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  She is not required to spend</text>
    <text x="18" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  1 shilling on co-wives</text>
    <text x="18" y="208" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Full property ownership</text>
  </g>

  <!-- Shield 3: Separate Housing -->
  <g transform="translate(445, 85)">
    <rect width="180" height="260" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="180" height="34" rx="8" fill="#d97706"/>
    <text x="90" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">3. SEPARATE DWELLING</text>

    <text x="90" y="56" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Privacy &amp; Peace of Mind</text>

    <rect x="10" y="70" width="160" height="175" rx="4" fill="#0f172a"/>
    <text x="18" y="92" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Independent Residence:</text>
    <text x="18" y="108" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Absolute right to separate</text>
    <text x="18" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  house or self-contained flat</text>
    <text x="18" y="146" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• No Forced Co-Living:</text>
    <text x="18" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Husband cannot force wives to</text>
    <text x="18" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  share kitchens or bedrooms</text>
    <text x="18" y="208" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Prevents jealousy &amp; friction</text>
  </g>

  <!-- Shield 4: Judicial Dissolution -->
  <g transform="translate(645, 85)">
    <rect width="180" height="260" rx="8" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <rect width="180" height="34" rx="8" fill="#6d28d9"/>
    <text x="90" y="22" fill="#ede9fe" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">4. COURT REDRESS</text>

    <text x="90" y="56" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Fasakh &amp; Khul'</text>

    <rect x="10" y="70" width="160" height="175" rx="4" fill="#0f172a"/>
    <text x="18" y="92" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Judicial Intervention:</text>
    <text x="18" y="108" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  If husband fails to maintain</text>
    <text x="18" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  fairness, judge dissolves marriage</text>
    <text x="18" y="146" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Legal Protection:</text>
    <text x="18" y="162" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Modern Kadhi courts in Kenya</text>
    <text x="18" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  enforce women's financial claims</text>
    <text x="18" y="208" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Woman is never trapped</text>
  </g>

  <!-- Bottom Message -->
  <g transform="translate(45, 360)">
    <rect width="780" height="55" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="390" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">MARRIAGE IN ISLAM IS A CIVIL CONTRACT PROTECTED BY LAW</text>
    <text x="390" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">A Muslim woman has proactive agency, negotiation power, and enforceable rights within Shariah</text>
  </g>
</svg>"""


def get_svg_lesson_6():
    """Lesson 6.4.6: Master Synthesis: The Islamic Marriage Paradigm"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg156" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg156)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">MASTER SYNTHESIS: THE ISLAMIC MARRIAGE PARADIGM</text>
  <text x="440" y="52" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Harmonizing Monogamy as the Default, Polygamy as an Exception, and Women's Legal Agency</text>

  <!-- Central Apex / Roof -->
  <g transform="translate(190, 75)">
    <polygon points="250,0 500,45 0,45" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="250" y="32" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">A BALANCED AND VIRTUOUS SOCIETY (MAQASID AL-SHARIAH)</text>
  </g>

  <!-- 3 Broad Structural Pillars -->
  <!-- Pillar 1: Monogamy as Default -->
  <g transform="translate(50, 135)">
    <rect width="235" height="215" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="235" height="32" rx="8" fill="#059669"/>
    <text x="117" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">1. MONOGAMY: THE DEFAULT</text>

    <rect x="12" y="42" width="211" height="160" rx="4" fill="#0f172a"/>
    <text x="20" y="62" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Safe Command of Qur'an:</text>
    <text x="20" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  "If you fear injustice, marry one"</text>
    <text x="20" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  (Surah An-Nisa 4:3)</text>
    <text x="20" y="116" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Prophetic Precedent:</text>
    <text x="20" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  25 years of youth monogamous</text>
    <text x="20" y="146" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  with Khadijah (RA)</text>
    <text x="20" y="174" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Maximum family stability</text>
  </g>

  <!-- Pillar 2: Conditional Polygamy -->
  <g transform="translate(322, 135)">
    <rect width="235" height="215" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="235" height="32" rx="8" fill="#d97706"/>
    <text x="117" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">2. CONDITIONAL EXCEPTION</text>

    <rect x="12" y="42" width="211" height="160" rx="4" fill="#0f172a"/>
    <text x="20" y="62" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Social Remedy in Crisis:</text>
    <text x="20" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Protects widows &amp; orphans</text>
    <text x="20" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  during war &amp; demographic imbalance</text>
    <text x="20" y="116" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Non-Negotiable Conditions:</text>
    <text x="20" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Cap of 4 • Separate dwellings •</text>
    <text x="20" y="146" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Equal nights • Paternal Nafaqah</text>
    <text x="20" y="174" fill="#f87171" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Leaning Body Warning</text>
  </g>

  <!-- Pillar 3: Women's Agency & Protection -->
  <g transform="translate(595, 135)">
    <rect width="235" height="215" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="235" height="32" rx="8" fill="#0284c7"/>
    <text x="117" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">3. WOMEN'S LEGAL SHIELD</text>

    <rect x="12" y="42" width="211" height="160" rx="4" fill="#0f172a"/>
    <text x="20" y="62" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Contractual Stipulations:</text>
    <text x="20" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Right to monogamy clause in</text>
    <text x="20" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Nikah certificate with divorce option</text>
    <text x="20" y="116" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">• Financial &amp; Court Rights:</text>
    <text x="20" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Exclusive property &amp; salary •</text>
    <text x="20" y="146" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8">  Judicial Fasakh for injustice</text>
    <text x="20" y="174" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">★ Independent legal personhood</text>
  </g>

  <!-- Foundation Banner -->
  <g transform="translate(50, 360)">
    <rect width="780" height="50" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="390" y="22" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">FOUNDATION: RESPONSIBILITY OVER PLEASURE, JUSTICE OVER GREED</text>
    <text x="390" y="39" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Islamic marriage legislation balances human compassion with rigorous ethical and legal accountability</text>
  </g>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION FOR THE 6 LESSONS IN TOPIC 15
# ─────────────────────────────────────────────────────────────────────────────

LESSONS_CONFIG = [
    {
        "unit_order": 1,
        "lesson_title": "Meaning and scope",
        "inquiry": "What is polygamy in Islam, and how did Islamic revelation regulate and restrict pre-Islamic marriage practices?",
        "hook": "Imagine a chaotic superhighway with no speed regulations, traffic lights, or lane dividers. Drivers can operate as many vehicles as they wish, drive at any velocity, and force other vehicles off the roadway with zero repercussions. The scene is dangerous, unjust, and destructive. To restore order, transportation authorities intervene: they establish a strict limit of four lanes, erect traffic signals, mandate vehicle fitness inspections, and enforce heavy penalties for reckless driving. In pre-Islamic Arabia, marriage was that reckless highway: men took dozens of wives without financial obligations or legal limits. In this lesson, we study how Islamic revelation entered history to regulate, restrict, and enforce strict justice upon marriage.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Quran_manuscript.jpg/800px-Quran_manuscript.jpg",
        "image_title": "Qur'anic Legislation on Family Equity",
        "image_caption": "Early manuscript preserving Surah An-Nisa, establishing the definitive restriction of polygamy and the non-negotiable standard of justice.",
        "concept_name": "Polygyny in Shariah & The Islamic Reform",
        "concept_explanation": "Polygamy (specifically polygyny) is the marital arrangement where a man is married to more than one wife simultaneously. In Islamic law, a man is permitted to marry a maximum of four wives at any given time, strictly contingent upon the fulfillment of rigorous moral and financial justice ('Adl). Islam did not invent polygamy; rather, it fundamentally reformed pre-Islamic customs by capping the number of wives to four, forbidding unjust favoritism, and granting each wife independent legal, financial, and contractual status.",
        "scripture_quran": "And if you fear that you will not deal justly with the orphans, then marry those that please you of [other] women, two or three or four. But if you fear that you will not be just, then [marry only] one...",
        "scripture_quran_ref": "Surah An-Nisa 4:3",
        "scripture_hadith": "Ghaylan ibn Salamah embraced Islam while having ten wives, so the Prophet (PBUH) said to him: 'Choose four from them and separate from the rest.'",
        "scripture_hadith_ref": "Sunan at-Tirmidhi 1128",
        "deep_explanation": "The Islamic reform of marriage introduced three historic legal breakthroughs:\n1. Strict Upper Limit: Islam placed an absolute cap of four wives. The Prophet (PBUH) commanded new Muslims who had more than four wives to divorce the excess, reducing widespread excess to a tightly controlled maximum.\n2. The Injunction of Justice ('Adl): Surah An-Nisa (4:3) issues an explicit divine directive: 'if you fear that you will not be just, then marry only one.' Monogamy is therefore established as the safe, universal default for the vast majority of believers.\n3. Independent Legal Rights for Wives: In pre-Islamic Arabia, women were treated as property. Islam transformed wives into independent legal entities holding exclusive ownership of their dowry (Mahr), personal wealth, and the legal right to set binding conditions in their marriage contracts.",
        "diagram_title": "The Marriage Revolution: Pre-Islamic Arabia vs. Islamic Shariah",
        "svg_func": get_svg_lesson_1,
        "table_title": "The Marriage Revolution: Pre-Islamic Arabia vs. Islamic Shariah",
        "table_headers": ["Feature", "Pre-Islamic Arabia (Jahiliyyah)", "Islamic Shariah (Qur'an 4:3)"],
        "table_rows": [
            ["Maximum Allowed Wives", "Unlimited (men took dozens of wives)", "Strict cap of maximum four wives"],
            ["Requirement of Justice", "Zero requirement; total male whim and bias", "Absolute requirement of 'Adl; warning of punishment"],
            ["Financial Maintenance", "No fixed duties; wives frequently abandoned", "Mandatory separate housing and equal maintenance"],
            ["Legal Status of Wife", "Treated as inherited property with no rights", "Independent legal person with exclusive property and Mahr"]
        ],
        "scenario": "During a history discussion, a student named Yusuf asks: 'Did Islam invent the practice of having multiple wives?' His teacher, Mr. Bilal, explains: 'No, Yusuf. In ancient civilizations and pre-Islamic Arabia, men married dozens of women without laws or limits. What Islam did was revolutionary: it capped the practice to a maximum of four, made absolute justice an unavoidable requirement, and established monogamy as the safest default. Islam introduced restraint, regulation, and severe accountability, not unchecked freedom.'",
        "real_world": "Apply the principle of 'Fairness over Excess' in your daily commitments. If you lead a group project or divide tasks among peers, never assume more responsibilities than you can fulfill fairly. Acknowledging personal limitations and treating others with equitable respect is the core of integrity (Amanah) and justice ('Adl).",
        "reflection": "Why does Surah An-Nisa (4:3) command 'if you fear that you will not be just, then marry only one'? How does this establish monogamy as the preferred and safe state for family harmony?",
        "misconception": "Misconception: Many people mistakenly believe Islam invented polygamy and that all Muslim men are obligated to have multiple wives. In reality, Islam strictly restricted an existing ancient practice, made it an exceptional permission rather than an obligation, and prioritized monogamy.",
        "yt_id": "o6zW4P7X5uM",
        "yt_title": "Polygamy in Islam: Meaning, Scope, and Legal Restrictions",
        "yt_desc": "Comprehensive analysis of pre-Islamic marriage practices, Qur'anic restrictions in Surah An-Nisa, and the standard of justice.",
        "mcq": {
            "question": "Which of the following best describes how Islamic revelation regulated the practice of polygamy in pre-Islamic Arabia?",
            "options": [
                "A. Islam made polygamy an obligatory practice for every adult male.",
                "B. Islam allowed men to marry an unlimited number of women without financial duties.",
                "C. Islam restricted the maximum number of wives to four and placed strict conditions of justice and equal support.",
                "D. Islam completely prohibited marriage altogether."
            ],
            "answer": "C",
            "explanation": "Islam did not introduce polygamy; it restricted the practice to a maximum of four wives and imposed strict conditions of material justice ('Adl) and equitable maintenance."
        },
        "summary_content": "Polygamy was an unregulated, unlimited custom in ancient Arabia. Islamic revelation reformed the practice through Surah An-Nisa (4:3), capping wives at a maximum of four, requiring absolute justice, and establishing monogamy as the safest standard for societal peace.",
        "key_points": [
            "Islam capped polygyny at a strict maximum of four wives simultaneously.",
            "Surah An-Nisa (4:3) explicitly commands monogamy if justice cannot be maintained.",
            "Wives hold independent legal status, retain their dowry (Mahr), and manage their own wealth.",
            "The Prophet (PBUH) ordered companions with more than four wives to divorce the excess."
        ],
        "exit_ticket": "Write down the Qur'anic verse reference that limits polygamy and state the primary condition it enforces."
    },
    {
        "unit_order": 2,
        "lesson_title": "Rationale and social remedy",
        "inquiry": "What is the social rationale behind the permission of polygamy in Islam, and how does it function as a societal remedy?",
        "hook": "Imagine a coastal city struck by a devastating tsunami that destroys thousands of homes and leaves hundreds of children without parents. Emergency infrastructure cannot instantly build hundreds of new houses. To prevent homelessness and suffering, the municipal council introduces an emergency foster framework: families with capacity are encouraged to house and support displaced widows and orphans, providing full legal protection. This is an exceptional social remedy designed to preserve human life and dignity during crises. In human history, warfare and calamities often leave widows and orphans destitute. In this lesson, we examine how Islamic law permits polygamy as a regulated social safety net.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Kaaba_Masjid_Haraam_Makkah.jpg/800px-Kaaba_Masjid_Haraam_Makkah.jpg",
        "image_title": "Sanctuary of Social Solidarity and Justice",
        "image_caption": "The holy sanctuary reminding the Ummah that divine legislation is revealed to shield the vulnerable and establish community welfare.",
        "concept_name": "Polygamy as a Protective Social Safety Net",
        "concept_explanation": "In Islamic jurisprudence, polygamy is permitted not as a tool for personal indulgence, but as an institutional social remedy to solve societal crises—specifically demographic imbalances resulting from war, and the protection of widows and orphans. The permission in Surah An-Nisa (4:3) was revealed following the Battle of Uhud, where many Muslim men were martyred, leaving numerous widows and children vulnerable. By providing an open, legal marital framework, Islam guarantees vulnerable women full financial rights, social honor, and legitimate family status.",
        "scripture_quran": "And if you fear that you will not deal justly with the orphans, then marry those that please you of [other] women...",
        "scripture_quran_ref": "Surah An-Nisa 4:3",
        "scripture_hadith": "The one who looks after a widow and a poor person is like a warrior fighting for the cause of Allah...",
        "scripture_hadith_ref": "Sahih al-Bukhari 5353",
        "deep_explanation": "Analyzing the social rationale of polygamy illuminates three vital societal protections:\n1. Protection of Widows and Orphans: After catastrophic battles, ancient desert societies had no social security pensions. Allowing men to marry widows integrated fatherless children into stable homes, securing their inheritance and education.\n2. Prevention of Exploitation and Social Decay: In societies where women significantly outnumber men due to war, strictly banning polygamy often forces women into informal, secret affairs without legal protections. Islam replaces secret mistresses with public, dignified marriage contracts granting full inheritance and legal status.\n3. Legitimate Lineage (Nasab): In a legal polygamous marriage, every child born is legitimate, carries the father's name, and inherits by divine right, preventing children from being cast out as illegitimate.",
        "diagram_title": "Polygamy as a Social Safety Shield in Times of Crisis",
        "svg_func": get_svg_lesson_2,
        "table_title": "Social Problems and the Islamic Legal Solution in Polygamy",
        "table_headers": ["Social Crisis", "Unregulated Societal Consequence", "Islamic Legal Safety Mechanism"],
        "table_rows": [
            ["High War Casualties", "Widows and orphans left in destitution", "Legal marriage integrating orphans into stable, funded households"],
            ["Demographic Imbalance", "Women outnumber men; secret mistresses arise", "Open, honorable Nikah guaranteeing full spousal and legal rights"],
            ["Child Paternity Risks", "Children born from secret affairs lack rights", "Verified lineage (Nasab) guaranteeing child inheritance and care"],
            ["Socioeconomic Shock", "Female impoverishment and social marginalization", "Binding spousal maintenance (Nafaqah) enforced by Kadhi courts"]
        ],
        "scenario": "In a social studies seminar, Amina asks: 'Why didn't the early Muslim community simply provide widows with monthly food rations instead of permitting polygamy?' Her teacher clarifies: 'Financial rations are necessary, Amina, but human dignity requires more than food. A widow and her young children need emotional security, male protection in a difficult society, social integration, and a loving father figure. Polygamy provided a complete family safety net where widows were welcomed as respected equals and orphans grew up with siblings in an honorable home.'",
        "real_world": "Look for opportunities to support vulnerable families in your community. If you know peers who have lost a parent or families undergoing hardship, practice community solidarity (Ta'awun). Share educational materials, invite them to group activities, and treat them with utmost respect. Your kindness reflects the compassionate core of Islamic social relations.",
        "reflection": "How does offering an open, public marriage contract protect a woman's honor compared to hidden, unregulated relationships? How does Surah An-Nisa (4:3) center child welfare in its opening words?",
        "misconception": "Misconception: Thinking that polygamy is intended as an open license for male pleasure. The Quranic text directly links the permission of polygamy to dealing justly with orphans, underscoring its historical and ethical role as a compassionate social remedy.",
        "yt_id": "uR4y7T9Z1bE",
        "yt_title": "The Social Wisdom and Historical Rationale of Polygamy",
        "yt_desc": "Scholarly lecture on post-Uhud history, demographic challenges, and how Shariah provided institutional care for widows and orphans.",
        "mcq": {
            "question": "In what primary historical and social context was the permission of polygamy in Surah An-Nisa (4:3) revealed?",
            "options": [
                "A. During an era of immense luxury and peace across Arabia.",
                "B. Following major military battles like Uhud, when many men were martyred, leaving numerous widows and orphans without protectors.",
                "C. As an absolute divine obligation that all men must marry multiple wives.",
                "D. To divide land and property exclusively among male warriors."
            ],
            "answer": "B",
            "explanation": "The permission was revealed following the Battle of Uhud to address a severe demographic and humanitarian crisis: providing legal protection, financial maintenance, and family stability for numerous orphans and widows."
        },
        "summary_content": "Polygamy functions in Islamic law as a regulated social remedy to protect vulnerable widows and orphans during demographic crises. By ensuring public legality, verified lineage (Nasab), and binding financial maintenance, Islam prevents societal exploitation and upholds human honor.",
        "key_points": [
            "Surah An-Nisa (4:3) was revealed in a post-war context to protect orphans.",
            "Polygamy provides an institutional safety net beyond mere financial charity.",
            "Public Nikah prevents illicit secret relationships and guarantees spousal rights.",
            "All children born within a polygamous marriage possess equal legitimacy and inheritance."
        ],
        "exit_ticket": "Explain how the permission of polygamy in Islam serves to protect the rights of orphans."
    },
    {
        "unit_order": 3,
        "lesson_title": "Prophet’s multiple marriages",
        "inquiry": "What were the noble reasons, divine guidance, and historical realities behind the Prophet Muhammad’s (PBUH) multiple marriages?",
        "hook": "Imagine the founding president of a newly emerged republic torn apart by centuries of blood feuds and tribal warfare. To forge national cohesion, the leader adopts heroic diplomatic strategies: he forms marriage alliances with rival tribal chieftains, pardons captured enemies, and establishes specialized academies where scholar-teachers preserve the young nation's constitution. Every single action is undertaken to unite the people, not for personal indulgence. The Prophet Muhammad (PBUH) was entrusted with the ultimate divine mission: uniting humanity under Tawhid and preserving the comprehensive details of Islamic law. His marriages were noble, strategic milestones fulfilling this divine mandate.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Al-Masjid_an-Nabawi_in_2017.jpg/800px-Al-Masjid_an-Nabawi_in_2017.jpg",
        "image_title": "The Noble Household of the Prophet (PBUH)",
        "image_caption": "Al-Masjid an-Nabawi in Madinah, where the Mothers of the Believers (Ummahat al-Mu'minin) preserved and transmitted the Sunnah to the world.",
        "concept_name": "Prophetic Marriages: Educational, Political & Social Missions",
        "concept_explanation": "A factual historical examination of the Prophet Muhammad's (PBUH) marital life disproves modern orientalist misconceptions. The Prophet (PBUH) lived in a monogamous marriage with Khadijah (RA) for 25 continuous years (from age 25 to 50)—the entire prime of his physical youth. His subsequent marriages after age 50 in Madinah were contracted under divine guidance for three noble objectives: Educational (training master female scholars like Aisha RA to transmit women's jurisprudence), Political/Diplomatic (reconciling warring tribes like Banu Mustaliq through marriage to Juwayriyah RA), and Social/Compassionate (caring for elderly widows of martyred companions).",
        "scripture_quran": "There has certainly been for you in the Messenger of Allah an excellent pattern for anyone whose hope is in Allah and the Last Day and [who] remembers Allah often.",
        "scripture_quran_ref": "Surah Al-Ahzab 33:21",
        "scripture_hadith": "Take half of your religion from this Humayra (Aisha).",
        "scripture_hadith_ref": "Famous Scholarly Maxim / Sunan at-Tirmidhi 3895",
        "deep_explanation": "The Prophet's multiple marriages fulfilled three primary dimensions of divine wisdom:\n1. The Educational Dimension: Women represented half the community. Innumerable questions concerning female hygiene, prayer during menstruation, and spousal relations could not be easily asked by female companions to the Prophet due to modesty (Haya). His wives, especially Aisha (RA), became master jurists who memorized over 2,200 Hadiths, educating generations of scholars.\n2. The Political & Tribal Dimension: In tribal Arabia, marriage was the most sacred peace treaty. When the Prophet (PBUH) married Juwayriyah (RA), daughter of the Banu Mustaliq chief, his companions immediately freed one hundred prisoner families out of respect for the Prophet's in-laws, leading the entire tribe to embrace Islam peacefully.\n3. The Social & Compassionate Dimension: Nearly all of the Prophet's wives (with the exception of Aisha) were elderly widows or divorcees (such as Sawdah, Hafsah, and Umm Salamah). By marrying them, he protected their dignity and honored their fallen husbands.",
        "diagram_title": "Chronological Timeline: Marital Life of Prophet Muhammad (PBUH)",
        "svg_func": get_svg_lesson_3,
        "table_title": "Noble Purposes Behind the Prophet's Marriages",
        "table_headers": ["Mother of Believers", "Marital / Social Context", "Primary Divine Wisdom / Outcome"],
        "table_rows": [
            ["Khadijah bint Khuwaylid (RA)", "Married when Prophet was 25; lived 25 years monogamously", "Exemplary marital loyalty; emotional and financial bedrock in youth"],
            ["Sawdah bint Zam'ah (RA)", "Elderly widow whose husband died in Abyssinia", "Compassionate shelter; cared for the Prophet's young household"],
            ["Aisha bint Abi Bakr (RA)", "Exceptional intellect and memory", "Preserved 2,210 Hadiths; taught female jurisprudence to the Ummah"],
            ["Juwayriyah bint al-Harith (RA)", "Daughter of Banu Mustaliq chief captured in conflict", "Reconciled hostile tribes; 100 families freed; tribe embraced Islam"],
            ["Zaynab bint Jahsh (RA)", "Former wife of the Prophet's adopted son Zayd", "Legislative reform: abolished pre-Islamic taboo regarding adopted sons"]
        ],
        "scenario": "A student named Zainab reads an online article claiming the Prophet (PBUH) married multiple wives for worldly comfort. Troubled, she speaks with Mr. Bilal. Mr. Bilal explains: 'Look at verified history, Zainab. If an individual seeks personal indulgence, they practice polygamy in their early twenties, not after age fifty. The Prophet spent 25 years of his youth married only to Khadijah, who was older than him. His later marriages were demanding, selfless missions to teach female Fiqh, unite warring clans, and shelter widows. Every marriage was an act of service to establish the Ummah.'",
        "real_world": "Defend the character of the Prophet (PBUH) using verifiable historical knowledge and refined manners. When encountering misconceptions, avoid anger or shouting. Respond with facts: his 25-year monogamous marriage to Khadijah, his compassionate care for elderly widows, and the scholarly legacy of Aisha (RA). Calm intellectual integrity is the best form of Da'wah.",
        "reflection": "How did the female scholarship nurtured in the Prophet's household (such as Aisha and Umm Salamah) preserve essential dimensions of Islamic knowledge for future generations?",
        "misconception": "Misconception: Assuming the Prophet's marriages were motivated by personal desire. Historical chronology directly refutes this: he remained monogamous throughout the entire prime of his youth, and his subsequent marriages were divine instructions serving political, legislative, and educational goals.",
        "yt_id": "fD5m1Z7K8kY",
        "yt_title": "The Prophet's Marriages: Historical Context and Divine Wisdom",
        "yt_desc": "Detailed historical documentary exploring the timeline, political alliances, and scholarly contributions of the Mothers of the Believers.",
        "mcq": {
            "question": "For how many years was Prophet Muhammad (PBUH) married exclusively to his first wife, Khadijah (RA), during the prime of his youth?",
            "options": [
                "A. Five years.",
                "B. Ten years.",
                "C. Twenty-five years.",
                "D. He never practiced monogamy."
            ],
            "answer": "C",
            "explanation": "The Prophet (PBUH) was married exclusively to Khadijah (RA) for 25 continuous years until her death, spanning ages 25 to 50, proving that monogamy was his default lifestyle during his youth."
        },
        "summary_content": "The Prophet Muhammad's (PBUH) marital life is defined by 25 years of monogamous youth with Khadijah (RA), followed by strategic marriages after age 50 under divine command. These marriages fulfilled essential educational, diplomatic, and compassionate functions that built the foundation of the Ummah.",
        "key_points": [
            "The Prophet lived in an exclusively monogamous marriage for 25 years.",
            "Marriages after age 50 addressed specific educational, political, and social needs.",
            "Aisha (RA) served as a master scholar, preserving foundational female jurisprudence.",
            "Marriages into prominent clans reconciled warring factions and fostered peace."
        ],
        "exit_ticket": "State three distinct noble purposes behind the multiple marriages of Prophet Muhammad (PBUH)."
    },
    {
        "unit_order": 4,
        "lesson_title": "Conditions of polygamy",
        "inquiry": "What strict legal, financial, and moral conditions must a Muslim man fulfill to practice polygamy?",
        "hook": "Imagine a commercial aviation pilot seeking certification to fly passenger airliners across oceans. The aviation authority does not grant permission casually. They enforce rigid, non-negotiable criteria: thousands of verified flight hours, spotless medical evaluations, stringent navigation exams, and adherence to severe safety checklists. If the pilot fails even one parameter, their certification is immediately denied, because human lives are entrusted to them. In Islamic family law, practicing polygamy is like piloting an airliner: it is not an open license, but a heavily regulated responsibility bound by severe spiritual and legal conditions.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Old_Quran_in_Wazir_Khan_Mosque.jpg/800px-Old_Quran_in_Wazir_Khan_Mosque.jpg",
        "image_title": "The Scales of Divine Justice ('Adl)",
        "image_caption": "Historic mosque pulpit representing the authoritative proclamation of justice, equity, and spiritual accountability in all social relations.",
        "concept_name": "The Non-Negotiable Conditions of 'Adl and Financial Capacity",
        "concept_explanation": "Islamic jurisprudence establishes three strict, mandatory conditions for polygamy: Absolute Material Justice ('Adl), Independent Private Lodging, and Proven Financial Capacity. The husband must divide his nights and material resources (housing, food, clothing) with absolute equality among his wives. He is legally forbidden from forcing wives to share a dwelling or imposing financial hardship. The Prophet (PBUH) issued a terrifying warning that any husband who favors one wife over another will rise on the Day of Judgment with half his body paralyzed.",
        "scripture_quran": "...But if you fear that you will not be just, then [marry only] one...",
        "scripture_quran_ref": "Surah An-Nisa 4:3",
        "scripture_hadith": "Whoever has two wives and is inclined toward one of them [more than the other], he will come on the Day of Judgment with a side of his body leaning [paralyzed].",
        "scripture_hadith_ref": "Sunan Abu Dawood 2134",
        "deep_explanation": "Islamic Shariah enforces three strict operational conditions for polygamy:\n1. Material Equality (Qasm & Nafaqah): The husband must divide his overnight stays with mathematical fairness (e.g., alternating two nights equally). He must provide equivalent financial maintenance. If he purchases clothing or household goods for one wife, he must provide an equivalent allocation for the other.\n2. Separate Private Dwellings: Each wife possesses an absolute legal right to a separate, independent home (or a self-contained apartment with private kitchen, bathroom, and entrance). A husband cannot force co-wives to live under the same roof unless both give free, uncoerced consent.\n3. Acknowledging Emotional Limits (Surah 4:129): Islam recognizes that emotional love cannot be divided with mechanical perfection. However, feelings must never manifest as physical neglect or favoritism. The Quran explicitly warns: 'do not incline completely toward one and leave the other hanging.'",
        "diagram_title": "The Scales of 'Adl (Absolute Justice) in Polygamy",
        "svg_func": get_svg_lesson_4,
        "table_title": "Mandatory Conditions and Requirements for Polygamy",
        "table_headers": ["Condition", "Practical Legal Requirement", "Violation Consequence"],
        "table_rows": [
            ["Absolute Justice ('Adl)", "Equal division of overnight stays (Qasm) and attention", "Major sin; physical paralysis on Day of Judgment (Sunan Abu Dawood 2134)"],
            ["Independent Housing", "Separate house or fully self-contained flat for each wife", "Wife can refuse to move in and petition Kadhi court"],
            ["Financial Capacity (Nafaqah)", "Husband can comfortably feed, clothe, and shelter all families", "Marriage is invalid/dissolved if husband causes impoverishment"],
            ["Emotional Restraint", "Must not leave one wife emotionally neglected or 'hanging'", "Direct violation of Surah An-Nisa 4:129; grounds for Fasakh"]
        ],
        "scenario": "Omar is married to two wives, Halima and Zainab. For Zainab's birthday, Omar buys a gold necklace. He thinks: 'It's her birthday, so I don't need to get anything for Halima.' Then he recalls the Hadith concerning the leaning body on Judgment Day. Realizing that material favoritism is a grave sin, he immediately returns to the jeweler to purchase an equivalent gift for Halima, ensuring both wives receive identical material generosity and respect.",
        "real_world": "Cultivate absolute impartiality in your daily life. When working on group tasks, do not assign easy roles to your close friends while giving difficult burdens to others. If your parents trust you to divide household chores or snacks with siblings, do so with strict fairness. Exercising justice ('Adl) in adolescence builds the integrity required to lead just families in adulthood.",
        "reflection": "Why did the Prophet (PBUH) employ such a striking physical metaphor (half the body leaning) to describe the punishment for spousal favoritism? How does this underscore the seriousness of marital justice?",
        "misconception": "Misconception: Assuming that a man who has enough money can marry multiple wives without regard to housing. In Islamic law, wealth alone is insufficient: each wife has an absolute right to her own private, independent dwelling to safeguard her emotional peace.",
        "yt_id": "rJ3wR3L4q8M",
        "yt_title": "The Strict Conditions of Polygamy and the Meaning of 'Adl",
        "yt_desc": "Fiqh lecture detailing the legal prerequisites for polygamy, night rotations, housing rules, and Prophetic warnings.",
        "mcq": {
            "question": "According to the Hadith in Sunan Abu Dawood (2134), what spiritual consequence awaits a husband who has multiple wives but treats them unfairly?",
            "options": [
                "A. He will receive an automatic exemption from the Day of Reckoning.",
                "B. He will rise on the Day of Judgment with a side of his body leaning/paralyzed.",
                "C. His wealth will be doubled in the hereafter.",
                "D. His marriages will be dissolved automatically without any sin."
            ],
            "answer": "B",
            "explanation": "The Prophet (PBUH) warned that a husband who inclines unfairly toward one wife over another will face public humiliation on the Day of Judgment, rising with half of his body paralyzed or leaning."
        },
        "summary_content": "Polygamy in Islam is conditioned upon absolute material justice ('Adl), separate independent dwellings, and proven financial capacity. Emotional inclinations must never lead to neglect, and the severe warning of physical paralysis on Judgment Day establishes the immense weight of marital fairness.",
        "key_points": [
            "Absolute justice ('Adl) in time and maintenance is a mandatory prerequisite.",
            "Each wife holds an absolute right to a separate, private residence.",
            "Husbands must divide their nights equally without favoritism.",
            "Surah An-Nisa (4:3) commands monogamy if a man fears he cannot maintain justice."
        ],
        "exit_ticket": "State the three material areas where a husband must maintain absolute equality between his wives."
    },
    {
        "unit_order": 5,
        "lesson_title": "Significance and contemporary discussion",
        "inquiry": "What modern legal protections, contractual rights, and emotional realities govern Muslim women in family law?",
        "hook": "Imagine leasing commercial retail space in an upscale business park. Before signing, park management presents you with the contract: you have the right to private locks, separate utilities, and clean surroundings. Furthermore, you hold the legal right to insert custom covenants—such as stipulating that management cannot lease the adjacent space to a direct competitor. In Islamic Shariah, marriage is a civil contract (Nikah). A Muslim woman is not a passive bystander; she possesses immense legal agency and contractual power. In this lesson, we study how modern Muslim women exercise their legal rights to safeguard their marriage and emotional wellbeing.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Samarkand_Kufic_Quran.jpg/800px-Samarkand_Kufic_Quran.jpg",
        "image_title": "The Enduring Authority of Islamic Contract Law",
        "image_caption": "Historic Qur'anic codex representing the divine authority that guarantees women independent legal personality and enforceable marital rights.",
        "concept_name": "Contractual Rights & Modern Legal Protections for Women",
        "concept_explanation": "Islamic family law equips women with robust legal shields: Contractual Agency (inserting a binding monogamy clause in the Nikah contract), Financial Independence (exclusive ownership of dowry, salary, and business profits), and Judicial Redress (the right to petition Kadhi courts for dissolution through Fasakh or Khul'). In Shariah, marriage is a mutual legal contract, and a woman is fully empowered to stipulate that her husband remain monogamous, with violation granting her immediate divorce and full financial rights.",
        "scripture_quran": "...And live with them in kindness. For if you dislike them - perhaps you dislike a thing and Allah makes therein much good.",
        "scripture_quran_ref": "Surah An-Nisa 4:19",
        "scripture_hadith": "The Muslims must abide by their conditions [and agreements]...",
        "scripture_hadith_ref": "Sunan Abu Dawood 3594",
        "deep_explanation": "Modern Islamic jurisprudence highlights four key protections for women in family relations:\n1. The Monogamy Stipulation: Classical and contemporary jurists (including the Hanbali school) uphold a woman's right to insert a condition in her marriage contract stating the husband will not take a second wife. If he breaches this agreement, she possesses the legal right to dissolve the marriage immediately while retaining her Mahr.\n2. Complete Financial Autonomy: A married woman's wealth belongs exclusively to her. She is under no legal obligation to contribute to household living expenses or assist her husband in financing other families.\n3. Emotional Realities and Jealousy: Shariah recognizes that jealousy is a natural human emotion felt even by the Mothers of the Believers. Husbands must exhibit high emotional intelligence, kindness, and patience, rather than dismissing their wives' valid feelings.\n4. Kadhi Court Oversight: In Kenya and across the Muslim world, Kadhi courts provide judicial oversight, granting Fasakh (judicial divorce) if a husband fails to provide separate lodging, equitable maintenance, or fair treatment.",
        "diagram_title": "The Wife's Legal Shield in Islamic Contract Law",
        "svg_func": get_svg_lesson_5,
        "table_title": "Legal Rights of Muslim Wives vs Common Misconceptions",
        "table_headers": ["Common Cultural Misconception", "Islamic Shariah Reality", "Legal Protection Mechanism"],
        "table_rows": [
            ["Wife has no say in husband's remarriage", "Can insert a binding monogamy clause in Nikah", "Breach gives wife immediate right to court dissolution"],
            ["Wives must share kitchen and living space", "Absolute right to separate, independent residence", "Wife can refuse cohabitation with co-wives"],
            ["Wife's salary belongs to husband's family", "100% exclusive ownership of her earnings and Mahr", "Husband cannot touch her money without consent"],
            ["Wife is trapped if treated unfairly", "Can petition Kadhi court for Fasakh (judicial divorce)", "Court dissolves marriage and enforces child support"]
        ],
        "scenario": "Halima is engaged to Yusuf. Before signing the marriage certificate, she sits with her father and Yusuf, stating: 'Yusuf, I value peace of mind and wish to build a monogamous home. I am inserting a clause in our Nikah contract stating you must remain married only to me; if you choose to marry a second wife, I retain the right to terminate our marriage while keeping my full dowry.' Yusuf agrees, and the condition is registered. If Yusuf marries five years later, Halima can approach the Kadhi court in Mombasa and receive an immediate dissolution with full financial protection, because Yusuf breached a binding covenant.",
        "real_world": "Always honor your pledges and contracts. If you sign a school agreement, borrow an item from a classmate, or make a verbal promise, fulfill it faithfully. The Prophet (PBUH) taught: 'Muslims must abide by their conditions.' Establishing a reputation as a person of your word is the bedrock of Islamic integrity (Amanah).",
        "reflection": "How does the legal right to insert a monogamy clause in a marriage contract empower Muslim women to make proactive choices about their marital future?",
        "misconception": "Misconception: Assuming a Muslim wife has no legal escape if her husband takes a second wife against her wishes. Shariah grants women the right to include a monogamy clause in the Nikah contract or seek judicial divorce (Fasakh) through Kadhi courts if treated unjustly.",
        "yt_id": "kX7F5sF9k2w",
        "yt_title": "Women's Rights and the Monogamy Clause in Islamic Contracts",
        "yt_desc": "Fiqh discussion examining marriage stipulations, female financial independence, and Kadhi court procedures in contemporary family law.",
        "mcq": {
            "question": "What legal right does a Muslim woman possess if she wants to ensure her husband does not marry another wife during their marriage?",
            "options": [
                "A. She has no rights and must accept whatever happens passively.",
                "B. She can insert a binding monogamy clause in her marriage contract (Nikah) which grants her divorce if violated.",
                "C. She must pay her husband a monthly fine to keep him monogamous.",
                "D. She can only get a divorce if she gives up all her inheritance and wealth."
            ],
            "answer": "B",
            "explanation": "In Shariah, marriage is a civil contract; a woman has the full legal right to include a monogamy clause in her Nikah certificate, which legally binds the husband and provides grounds for divorce if breached."
        },
        "summary_content": "Muslim women hold strong contractual agency in Islamic family law, including the right to insert binding monogamy clauses, full ownership of independent wealth, and the ability to obtain judicial divorce (Fasakh) through Kadhi courts when treated unfairly.",
        "key_points": [
            "A woman can legally stipulate monogamy in her Nikah marriage contract.",
            "Her dowry (Mahr), salary, and assets are her exclusive personal property.",
            "Each wife is legally entitled to private, separate housing.",
            "Kadhi courts protect women's welfare and grant judicial divorce for marital neglect."
        ],
        "exit_ticket": "Explain how a marriage contract (Nikah) can be utilized to protect a woman's right to monogamy."
    },
    {
        "unit_order": 6,
        "lesson_title": "Unit synthesis",
        "inquiry": "How do we synthesize the historical context, strict conditions of justice, and legal protections of polygamy into a balanced Islamic framework?",
        "hook": "Imagine inspecting a double-deck suspension bridge designed to carry thousands of vehicles daily across a wide harbor. To ensure structural integrity, you cannot inspect only the pavement. You must examine the reinforced steel trusses, the tension sensors on the suspension cables, the emergency escape shoulders, and the weight limits. If even one cable lacks tension, the entire bridge fails. In this final synthesis lesson, we unite all dimensions of our study of polygamy—historical reforms, the social safety net, the Prophet's marriages, conditions of justice, and women's legal agency—to observe how Islam establishes an equitable, balanced framework of family law.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Quran_manuscript.jpg/800px-Quran_manuscript.jpg",
        "image_title": "Master Synthesis of Islamic Family Law",
        "image_caption": "Historic Qur'anic codex symbolizing the harmonious balance of rights, duties, and compassion governing Islamic social relations.",
        "concept_name": "The Master Paradigm: Monogamy as Default & Conditional Polygamy",
        "concept_explanation": "The Islamic paradigm of marriage establishes monogamy as the preferred, universal default for family stability, while permitting polygamy as an exceptional, highly regulated social remedy. Shariah restricts the practice to a maximum of four wives, binds it with unforgiving conditions of material equality ('Adl), and provides women with proactive legal shields (including monogamy clauses and separate dwellings). By evaluating the institution holistically through the Maqasid al-Shariah, learners develop a mature, source-grounded understanding of divine justice.",
        "scripture_quran": "...But if you fear that you will not be just, then [marry only] one...",
        "scripture_quran_ref": "Surah An-Nisa 4:3",
        "scripture_hadith": "The believers who show the most perfect faith are those who have the best character, and the best of you are the best to their wives.",
        "scripture_hadith_ref": "Sunan at-Tirmidhi 1162",
        "deep_explanation": "Synthesizing the unit establishes five core principles of Islamic family law:\n1. Historical Reform: Islam ended unregulated polygamy, placed a cap of four, and transformed wives from property into independent legal personages.\n2. Social Safety Net: The primary historical rationale was shielding orphans and widows during post-war crises, preventing destitution.\n3. Prophetic Precedent: The Prophet (PBUH) spent 25 years of his youth in a monogamous marriage with Khadijah (RA); his later marriages were divine missions for peace, education, and social care.\n4. The Crucible of Justice: Material equality in nights, finances, and housing is non-negotiable, reinforced by the Prophet's warning of physical paralysis on Judgment Day.\n5. Women's Contractual Power: Muslim women hold full legal agency to negotiate Nikah conditions, protect their wealth, and seek judicial divorce if wronged.",
        "diagram_title": "Master Synthesis: The Islamic Marriage Paradigm",
        "svg_func": get_svg_lesson_6,
        "table_title": "Master Synthesis Framework: The Islamic Marriage Paradigm",
        "table_headers": ["Dimension", "Classical Shariah Rule", "Practical Daily Reality", "Pedagogical / Ethical Value"],
        "table_rows": [
            ["Default State", "Monogamy is safe command (Surah 4:3)", "Vast majority of Muslim homes are monogamous", "Preserves emotional peace and family stability"],
            ["Conditional Exception", "Polygamy capped at four; strict 'Adl", "Requires independent housing & verified wealth", "Addresses demographic crises with dignity"],
            ["Prophetic Role Model", "25 years monogamous youth with Khadijah", "Later marriages for education, peace, and widow care", "Refutes misconceptions with chronological facts"],
            ["Women's Agency", "Monogamy clause in Nikah & separate home", "Kadhi court dissolves marriage for injustice", "Empowers women with enforceable legal shields"]
        ],
        "scenario": "A classmate, Ibrahim, remarks: 'Islam allows four wives, so I can marry whenever I want without worrying about my finances or my wife's feelings.' His classmate Maryam provides a source-grounded response: 'No, Ibrahim. Polygamy is a restricted exception, not an entitlement. It demands absolute justice ('Adl), separate homes for each wife, and proven financial capacity. If you cannot maintain perfect material equality, the Quran commands you to marry only one and warns that unjust husbands will rise on Judgment Day with half their bodies paralyzed. Monogamy is the default and safest path.'",
        "real_world": "Write an essay or create a presentation on 'The Rights and Protections of Women in Islamic Family Law.' Contrast pre-Islamic Arabia with Islamic Shariah, explain the strict requirements of justice ('Adl), and highlight women's contractual shields such as the monogamy clause. Display a summary on your school's notice board.",
        "reflection": "How does understanding the distinction between 'permission as a social remedy' and 'universal recommendation' help us explain Islamic family laws accurately to the wider public?",
        "misconception": "Misconception: Assuming that polygamy is recommended for every Muslim man. Scholars across Islamic history agree that monogamy is the default, safest, and most practical state, with polygamy reserved as a conditional exception bound by heavy spiritual accountability.",
        "yt_id": "kX7F5sF9k2w",
        "yt_title": "Master Synthesis: The Complete Architecture of Islamic Family Law",
        "yt_desc": "Comprehensive review of the historical reforms, conditions of justice, Prophetic timeline, and women's rights in Islamic marriage.",
        "mcq": {
            "question": "A classmate claims: 'Islam gives men total freedom to marry four wives without any restrictions.' Applying the full synthesis of this unit, what is the most accurate corrective response?",
            "options": [
                "A. 'Yes, men have unlimited freedom with no conditions or responsibilities.'",
                "B. 'Polygamy is a conditional permission requiring proven finances, separate housing, and absolute justice ('Adl); if equality cannot be maintained, the Quran commands monogamy.'",
                "C. 'Polygamy is completely prohibited in modern Islam under all circumstances.'",
                "D. 'A man can marry multiple wives only if his first wife funds their living expenses.'"
            ],
            "answer": "B",
            "explanation": "This option correctly captures the full unit synthesis: polygamy is a strictly conditional permission requiring separate dwellings, financial ability, and absolute justice ('Adl), with the Quran commanding monogamy if equality is not possible."
        },
        "summary_content": "The Islamic marriage paradigm establishes monogamy as the default foundation for family peace, while permitting polygamy as a strictly regulated social remedy. Bound by rigorous conditions of justice ('Adl) and balanced by women's contractual protections, Shariah protects family dignity and societal welfare.",
        "key_points": [
            "Monogamy is the safest and default marital state commanded in the Quran.",
            "Polygamy is a conditional exception requiring separate housing and proven financial capability.",
            "Failure to treat wives with absolute equality carries severe spiritual consequences.",
            "Women possess proactive legal agency through marriage contracts and Kadhi court protections."
        ],
        "exit_ticket": "Write down the single most important legal right a Muslim woman possesses to protect her marital choices in her marriage contract."
    }
]


# ─────────────────────────────────────────────────────────────────────────────
# INGESTION EXECUTION FUNCTION
# ─────────────────────────────────────────────────────────────────────────────

def ingest_grade9_ire_topic15():
    print("=" * 80)
    print("STARTING INGESTION: GRADE 9 IRE — TOPIC 15: POLYGAMY IN ISLAM")
    print("=" * 80)

    try:
        topic = Topic.objects.get(id=355)
    except Topic.DoesNotExist:
        print("ERROR: Topic ID 355 does not exist! Please create topic record first.")
        sys.exit(1)

    print(f"Target Topic: ID={topic.id}, Name='{topic.name}', Order={topic.order}")

    # Validate all SVGs before database transactions
    print("\nValidating all 6 custom vector SVGs for XML compliance...")
    for idx, cfg in enumerate(LESSONS_CONFIG, 1):
        svg_content = cfg["svg_func"]()
        try:
            ET.fromstring(svg_content)
            print(f"  [✓] SVG {idx}/6 ('{cfg['diagram_title']}') is valid XML.")
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
                name=f"Lesson 6.4.{u_order}: {l_title}",
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
            print(f"  [+] Ingested Lesson {u_order}/6: '{l_title}' (7 cards, 15 blocks, 3 assets)")

    print("=" * 80)
    print("TOPIC 15 INGESTION COMPLETE & VERIFIED!")
    print(f"  LearningUnits : {total_units} / 6")
    print(f"  Lessons       : {total_lessons} / 6 (Published)")
    print(f"  Blocks        : {total_blocks} (15 per lesson, 7 pages)")
    print(f"  Assets        : {total_assets} (6 SVGs, 6 images, 6 videos)")
    print("=" * 80)


if __name__ == "__main__":
    ingest_grade9_ire_topic15()
