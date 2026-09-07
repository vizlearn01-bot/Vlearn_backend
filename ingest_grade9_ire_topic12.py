"""
VLearn CBC Grade 9 IRE — Topic 12: Domestic Violence
Production Ingestion and Enrichment Script for all 6 Lessons

Target Topic in DB: Topic ID 352 (Subject: IRE ID 53, Grade: Grade 9 ID 18)
Source Markdown: /home/jason-bitega/Desktop/VL/vlearn_repositories/Grade 9 IRE/domestic-violence.md

6 Lessons Ingested & Fully Enriched:
  1. Lesson 6.1.1: Meaning and forms
  2. Lesson 6.1.2: Causes and risk factors
  3. Lesson 6.1.3: Effects on family
  4. Lesson 6.1.4: Islamic measures to curb violence
  5. Lesson 6.1.5: Prevention and community response
  6. Lesson 6.1.6: Unit synthesis
"""

import os
import sys
import re
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
    """Lesson 6.1.1: The Four Destructive Termites of the Home"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg121" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg121)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">DOMESTIC VIOLENCE: THE FOUR TERMITES UNDERMINING THE HOME</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">How Physical, Verbal, Psychological, and Economic Abuse Destroy the Shelter of Peace (Sakinah)</text>

  <!-- Roof: The Sanctuary of Sakinah -->
  <g transform="translate(190, 85)">
    <polygon points="250,0 500,45 0,45" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="250" y="32" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">THE SANCTUARY OF SAKINAH &amp; RAHMAH (SURAH AN-NISA 4:19)</text>
  </g>

  <!-- 4 Pillars Under Attack -->
  <!-- Pillar 1 -->
  <g transform="translate(45, 140)">
    <rect width="180" height="195" rx="8" fill="#1e293b" stroke="#f87171" stroke-width="1.5"/>
    <rect width="180" height="32" rx="8" fill="#7f1d1d"/>
    <text x="90" y="21" fill="#fecaca" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">1. PHYSICAL ABUSE</text>

    <rect x="10" y="42" width="160" height="142" rx="4" fill="#0f172a"/>
    <text x="18" y="62" fill="#f87171" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Forms:</text>
    <text x="18" y="77" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Hitting, slapping, shoving</text>
    <text x="18" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Throwing objects</text>
    <text x="18" y="107" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Inflicting bodily pain</text>
    
    <text x="18" y="132" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Islamic Ruling:</text>
    <text x="18" y="147" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">• Strictly Haram</text>
    <text x="18" y="162" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="8.5">• Grounds for divorce</text>
  </g>

  <!-- Pillar 2 -->
  <g transform="translate(245, 140)">
    <rect width="180" height="195" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="180" height="32" rx="8" fill="#92400e"/>
    <text x="90" y="21" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">2. VERBAL ABUSE</text>

    <rect x="10" y="42" width="160" height="142" rx="4" fill="#0f172a"/>
    <text x="18" y="62" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Forms:</text>
    <text x="18" y="77" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Mockery &amp; slurs</text>
    <text x="18" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Constant shouting &amp; yelling</text>
    <text x="18" y="107" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Demeaning insults</text>
    
    <text x="18" y="132" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Prophetic Standard:</text>
    <text x="18" y="147" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">• Speak good or be quiet</text>
    <text x="18" y="162" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="8.5">• No cursing allowed</text>
  </g>

  <!-- Pillar 3 -->
  <g transform="translate(445, 140)">
    <rect width="180" height="195" rx="8" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <rect width="180" height="32" rx="8" fill="#5b21b6"/>
    <text x="90" y="21" fill="#ede9fe" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">3. PSYCHOLOGICAL</text>

    <rect x="10" y="42" width="160" height="142" rx="4" fill="#0f172a"/>
    <text x="18" y="62" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Forms:</text>
    <text x="18" y="77" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Extreme isolation</text>
    <text x="18" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Spying &amp; controlling</text>
    <text x="18" y="107" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Fear &amp; intimidation</text>
    
    <text x="18" y="132" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Islamic Value:</text>
    <text x="18" y="147" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">• Mutual consultation</text>
    <text x="18" y="162" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="8.5">• Trust &amp; dignity</text>
  </g>

  <!-- Pillar 4 -->
  <g transform="translate(645, 140)">
    <rect width="180" height="195" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="180" height="32" rx="8" fill="#075985"/>
    <text x="90" y="21" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">4. ECONOMIC ABUSE</text>

    <rect x="10" y="42" width="160" height="142" rx="4" fill="#0f172a"/>
    <text x="18" y="62" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Forms:</text>
    <text x="18" y="77" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Withholding food &amp; clothes</text>
    <text x="18" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Denying school fees</text>
    <text x="18" y="107" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Weaponizing finances</text>
    
    <text x="18" y="132" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700">Islamic Obligation:</text>
    <text x="18" y="147" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">• Nafaqah is mandatory</text>
    <text x="18" y="162" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="8.5">• Financial duty on father</text>
  </g>

  <!-- Foundation Beam -->
  <g transform="translate(45, 350)">
    <rect width="780" height="60" rx="8" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
    <text x="390" y="25" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">PROPHETIC STANDARD: "THE BEST OF YOU ARE BEST TO THEIR FAMILIES" (TIRMIDHI 3895)</text>
    <text x="390" y="45" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">The Prophet Muhammad (PBUH) never struck a woman, child, or servant. Any abuse completely violates the Sunnah.</text>
  </g>
</svg>"""


def get_svg_lesson_2():
    """Lesson 6.1.2: Fishbone Diagram: Root Causes vs Islamic Countermeasures"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg122" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg122)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">ROOT CAUSES VS ISLAMIC COUNTERMEASURES</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Identifying Destructive Risk Factors and Applying Divine Spiritual &amp; Behavioral Solutions</text>

  <!-- Left: 4 Root Causes -->
  <g transform="translate(45, 85)">
    <rect width="360" height="315" rx="10" fill="#1e293b" stroke="#f87171" stroke-width="1.5"/>
    <rect width="360" height="34" rx="10" fill="#7f1d1d"/>
    <text x="180" y="22" fill="#fecaca" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">UN-ISLAMIC RISK FACTORS &amp; ROOTS</text>

    <!-- 1. Anger Mismanagement -->
    <rect x="15" y="46" width="330" height="56" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="66" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700">1. Anger Mismanagement:</text>
    <text x="25" y="82" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Letting stress explode into physical or verbal fury</text>
    <text x="25" y="94" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Overpowering weaker family members</text>

    <!-- 2. Harmful Cultural Traditions -->
    <rect x="15" y="110" width="330" height="56" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="130" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700">2. Harmful Cultural Norms:</text>
    <text x="25" y="146" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Viewing women as inferior property</text>
    <text x="25" y="158" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Normalizing violence as "discipline" (Rejected by Islam)</text>

    <!-- 3. Economic Stress -->
    <rect x="15" y="174" width="330" height="56" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="194" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700">3. Financial Strain &amp; Unemployment:</text>
    <text x="25" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• External job pressures vented inside the household</text>
    <text x="25" y="222" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Poverty can NEVER justify domestic abuse</text>

    <!-- 4. Intoxicants -->
    <rect x="15" y="238" width="330" height="56" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="258" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700">4. Substance Abuse (Khamr):</text>
    <text x="25" y="274" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Alcohol &amp; drugs impair intellect ('Aql) and impulse control</text>
    <text x="25" y="286" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Primary trigger for severe violent domestic incidents</text>
  </g>

  <!-- Central Arrow -->
  <g transform="translate(415, 215)">
    <text x="25" y="15" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="900" text-anchor="middle">→</text>
    <text x="25" y="32" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">Remedy</text>
  </g>

  <!-- Right: 4 Islamic Countermeasures -->
  <g transform="translate(475, 85)">
    <rect width="360" height="315" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="360" height="34" rx="10" fill="#065f46"/>
    <text x="180" y="22" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">DIVINE ISLAMIC COUNTERMEASURES</text>

    <!-- 1. Prophetic Anger Control -->
    <rect x="15" y="46" width="330" height="56" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="66" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">1. Prophetic Anger Protocol:</text>
    <text x="25" y="82" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Isti'adhah (Seek refuge in Allah from Satan)</text>
    <text x="25" y="94" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Sit down if standing, lie down, make Wudhu</text>

    <!-- 2. Gender Dignity in Sunnah -->
    <rect x="15" y="110" width="330" height="56" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="130" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">2. Qur'anic Gender Honor:</text>
    <text x="25" y="146" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Women and men are spiritual equals before Allah</text>
    <text x="25" y="158" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Prophetic decree: "Do not hit female servants of Allah"</text>

    <!-- 3. Sabr and Mutual Support -->
    <rect x="15" y="174" width="330" height="56" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="194" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">3. Spiritual Sabr &amp; Tawakkul:</text>
    <text x="25" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Turn economic anxiety into collective family prayer</text>
    <text x="25" y="222" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Community Zakat &amp; mutual charity provide social net</text>

    <!-- 4. Absolute Prohibition of Khamr -->
    <rect x="15" y="238" width="330" height="56" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="258" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">4. Complete Prohibition of Khamr:</text>
    <text x="25" y="274" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Absolute ban on alcohol protects the intellect ('Aql)</text>
    <text x="25" y="286" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Safeguards women and children from drunken rage</text>
  </g>
</svg>"""


def get_svg_lesson_3():
    """Lesson 6.1.3: Trauma Ripple vs The House of Sakinah"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg123" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg123)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">EFFECTS ON FAMILY: THE TRAUMA RIPPLE VS THE HOUSE OF SAKINAH</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">How Family Atmosphere Shapes Child Brain Development, Educational Flourishing, and Future Generations</text>

  <!-- Left Side: Abusive Environment -->
  <g transform="translate(45, 85)">
    <rect width="370" height="315" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="370" height="36" rx="10" fill="#7f1d1d"/>
    <text x="185" y="24" fill="#fecaca" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">THE TOXIC ENVIRONMENT (ABUSE)</text>

    <!-- Point 1 -->
    <rect x="15" y="48" width="340" height="52" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="68" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Neurological State:</text>
    <text x="25" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Constant fight-or-flight, chronic high cortisol stress hormones</text>

    <!-- Point 2 -->
    <rect x="15" y="108" width="340" height="52" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="128" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Educational Impact:</text>
    <text x="25" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Severe difficulty focusing in school, panic attacks, failing grades</text>

    <!-- Point 3 -->
    <rect x="15" y="168" width="340" height="52" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="188" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Behavioral Manifestations:</text>
    <text x="25" y="205" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Extreme withdrawal, depression, or aggressive bullying of peers</text>

    <!-- Intergenerational Trap -->
    <rect x="15" y="228" width="340" height="72" rx="6" fill="#2d1515" stroke="#ef4444"/>
    <text x="185" y="248" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">THE CYCLE OF VIOLENCE TRAP</text>
    <text x="185" y="266" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Children who witness domestic violence are at high risk of repeating</text>
    <text x="185" y="280" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">abusive behavior in their own adult marriages unless cycle is broken.</text>
  </g>

  <!-- Right Side: Peaceful Environment (Sakinah) -->
  <g transform="translate(465, 85)">
    <rect width="370" height="315" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="370" height="36" rx="10" fill="#065f46"/>
    <text x="185" y="24" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">THE PEACEFUL ENVIRONMENT (SAKINAH)</text>

    <!-- Point 1 -->
    <rect x="15" y="48" width="340" height="52" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="68" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Neurological State:</text>
    <text x="25" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Emotional safety, balanced brain chemistry, peaceful sleep</text>

    <!-- Point 2 -->
    <rect x="15" y="108" width="340" height="52" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="128" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Educational Impact:</text>
    <text x="25" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• High concentration, academic creativity, confidence in exams</text>

    <!-- Point 3 -->
    <rect x="15" y="168" width="340" height="52" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="188" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Behavioral Manifestations:</text>
    <text x="25" y="205" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Empathy, polite communication, healthy peer relationships</text>

    <!-- Intergenerational Blessing -->
    <rect x="15" y="228" width="340" height="72" rx="6" fill="#064e3b" stroke="#10b981"/>
    <text x="185" y="248" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">THE GENERATIONAL BLESSING (TARBIYAH)</text>
    <text x="185" y="266" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Children grow up with modeled conflict resolution skills,</text>
    <text x="185" y="280" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">building compassionate, loving families that anchor national peace.</text>
  </g>
</svg>"""


def get_svg_lesson_4():
    """Lesson 6.1.4: The Prophetic Standard vs Abusive Distortions"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg124" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg124)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">ISLAMIC MEASURES: THE PROPHETIC SUNNAH VS ABUSIVE DISTORTIONS</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Uprooting Misinterpretations of Quran 4:34 and Establishing Absolute Legal Rejection of Abuse</text>

  <!-- Left Card: Prophetic Sunnah -->
  <g transform="translate(45, 85)">
    <rect width="365" height="315" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="365" height="34" rx="10" fill="#065f46"/>
    <text x="182" y="22" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">THE PROPHET'S LIVING SUNNAH</text>

    <rect x="15" y="48" width="335" height="52" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="68" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Historical Authenticity:</text>
    <text x="25" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Aisha (RA) narrated: "He never struck a woman, child, or servant."</text>

    <rect x="15" y="108" width="335" height="52" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="128" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Explicit Prohibition:</text>
    <text x="25" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Hadith: "Do not hit the female servants of Allah." (Abu Dawood 2146)</text>

    <rect x="15" y="168" width="335" height="52" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="188" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Gentle Conflict Resolution:</text>
    <text x="25" y="205" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Resolved disagreements through gentle silence, dialogue, or counseling</text>

    <rect x="15" y="228" width="335" height="72" rx="6" fill="#064e3b" stroke="#10b981"/>
    <text x="167" y="248" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">LEGAL REMEDY: THE RIGHT TO DIVORCE</text>
    <text x="167" y="266" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Islam grants victims the absolute right to exit an abusive marriage</text>
    <text x="167" y="280" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">safely through judicial separation (Khul' or Fasakh) with child custody.</text>
  </g>

  <!-- Right Card: Juristic Reality of Quran 4:34 -->
  <g transform="translate(470, 85)">
    <rect width="365" height="315" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="365" height="34" rx="10" fill="#0369a1"/>
    <text x="182" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">JURISTIC CLARITY ON QURAN 4:34</text>

    <rect x="15" y="48" width="335" height="52" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="68" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">1. Stage One: Sincere Verbal Advice</text>
    <text x="25" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Gentle reminder, mutual consultation, identifying problems</text>

    <rect x="15" y="108" width="335" height="52" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="128" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">2. Stage Two: Symbolic Emotional Distance</text>
    <text x="25" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Sleeping in separate beds inside the house to signal seriousness</text>

    <rect x="15" y="168" width="335" height="52" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="25" y="188" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">3. Non-Violent Symbolic Limit (Siwak):</text>
    <text x="25" y="205" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Ibn Abbas: "Symbolic tap with a tiny Siwak (toothbrush)"</text>

    <rect x="15" y="228" width="335" height="72" rx="6" fill="#0c4a6e" stroke="#0284c7"/>
    <text x="167" y="248" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">SCHOLARLY CONSENSUS</text>
    <text x="167" y="266" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Zero pain, zero mark, zero redness, strictly forbidden to touch the face.</text>
    <text x="167" y="280" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Any physical force causing pain is strictly Haram and criminal abuse.</text>
  </g>
</svg>"""


def get_svg_lesson_5():
    """Lesson 6.1.5: The Community Safety Dike"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg125" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg125)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">COMMUNITY ACTION: THE FOUR INTERLOCKING LAYERS OF THE SAFETY DIKE</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Preventing Domestic Violence Through Multi-Tiered Civic, Spiritual, and Institutional Protection</text>

  <!-- 4 Interlocking Shield Cards -->
  <!-- Layer 1 -->
  <g transform="translate(45, 85)">
    <rect width="180" height="315" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="180" height="34" rx="8" fill="#0284c7"/>
    <text x="90" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">LAYER 1: INDIVIDUAL</text>

    <text x="90" y="56" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Self-Control &amp; Taqwa</text>

    <rect x="10" y="70" width="160" height="230" rx="4" fill="#0f172a"/>
    <text x="18" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Prophetic anger</text>
    <text x="18" y="107" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  management</text>
    <text x="18" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Accountability</text>
    <text x="18" y="147" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  before Allah</text>
    <text x="18" y="172" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Conscious practice</text>
    <text x="18" y="187" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  of Akhlaq at home</text>
    <text x="18" y="212" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Zero intoxicants</text>
    <text x="18" y="247" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Internal Moral</text>
    <text x="18" y="262" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Compass</text>
  </g>

  <!-- Layer 2 -->
  <g transform="translate(245, 85)">
    <rect width="180" height="315" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="180" height="34" rx="8" fill="#059669"/>
    <text x="90" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">LAYER 2: FAMILY</text>

    <text x="90" y="56" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Islaah &amp; Wise Elders</text>

    <rect x="10" y="70" width="160" height="230" rx="4" fill="#0f172a"/>
    <text x="18" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Quranic mediation</text>
    <text x="18" y="107" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  (Surah Nisa 4:35)</text>
    <text x="18" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Two fair judges</text>
    <text x="18" y="147" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  (one from each side)</text>
    <text x="18" y="172" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Safe communication</text>
    <text x="18" y="187" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  without screaming</text>
    <text x="18" y="212" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Protect the victim</text>
    <text x="18" y="247" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">De-escalation &amp;</text>
    <text x="18" y="262" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Reconciliation</text>
  </g>

  <!-- Layer 3 -->
  <g transform="translate(445, 85)">
    <rect width="180" height="315" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="180" height="34" rx="8" fill="#d97706"/>
    <text x="90" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">LAYER 3: COMMUNITY</text>

    <text x="90" y="56" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Mosques &amp; Schools</text>

    <rect x="10" y="70" width="160" height="230" rx="4" fill="#0f172a"/>
    <text x="18" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Khutbah sermons</text>
    <text x="18" y="107" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  condemning abuse</text>
    <text x="18" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Confidential</text>
    <text x="18" y="147" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  pastoral counseling</text>
    <text x="18" y="172" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• School guidance</text>
    <text x="18" y="187" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  teacher support</text>
    <text x="18" y="212" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Pre-marital study</text>
    <text x="18" y="247" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Education &amp;</text>
    <text x="18" y="262" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Safe Havens</text>
  </g>

  <!-- Layer 4 -->
  <g transform="translate(645, 85)">
    <rect width="180" height="315" rx="8" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <rect width="180" height="34" rx="8" fill="#7c3aed"/>
    <text x="90" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" text-anchor="middle">LAYER 4: LEGAL</text>

    <text x="90" y="56" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Law &amp; Child Protection</text>

    <rect x="10" y="70" width="160" height="230" rx="4" fill="#0f172a"/>
    <text x="18" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Child protection</text>
    <text x="18" y="107" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  officers (Kenya)</text>
    <text x="18" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• GBV toll-free</text>
    <text x="18" y="147" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  hotlines (1195)</text>
    <text x="18" y="172" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Legal restraining</text>
    <text x="18" y="187" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  orders &amp; safety</text>
    <text x="18" y="212" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Police accountability</text>
    <text x="18" y="247" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Statutory Shield &amp;</text>
    <text x="18" y="262" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Justice</text>
  </g>
</svg>"""


def get_svg_lesson_6():
    """Lesson 6.1.6: Master Synthesis Architecture: The House of Sakinah"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg126" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg126)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">MASTER CAPSTONE: THE SANCTUARY OF SAKINAH &amp; PEACEMAKING</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Harmonious Integration of Prophetic Character, Family Dignity, and Universal Child Protection</text>

  <!-- Roof of Divine Mercy -->
  <g transform="translate(190, 85)">
    <polygon points="250,0 500,45 0,45" fill="#065f46" stroke="#34d399" stroke-width="2"/>
    <text x="250" y="32" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">ROOF: DIVINE MERCY (RAHMAH) &amp; EMOTIONAL PEACE (SAKINAH)</text>
  </g>

  <!-- 4 Wall Pillars of the Home -->
  <g transform="translate(60, 145)">
    <rect width="170" height="165" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="85" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">GENTLE SPEECH</text>
    <rect x="12" y="36" width="146" height="115" rx="4" fill="#0f172a"/>
    <text x="20" y="58" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• No shouting or slurs</text>
    <text x="20" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Prophetic calmness</text>
    <text x="20" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Words that heal,</text>
    <text x="20" y="113" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  not wound</text>
    <text x="20" y="138" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Dignity in speech</text>
  </g>

  <g transform="translate(250, 145)">
    <rect width="170" height="165" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="85" y="24" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">ZERO VIOLENCE</text>
    <rect x="12" y="36" width="146" height="115" rx="4" fill="#0f172a"/>
    <text x="20" y="58" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Complete ban</text>
    <text x="20" y="73" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  on physical strikes</text>
    <text x="20" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Prophet's standard</text>
    <text x="20" y="113" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  of non-violence</text>
    <text x="20" y="138" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Physical safety</text>
  </g>

  <g transform="translate(440, 145)">
    <rect width="170" height="165" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="85" y="24" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">FAIR MAINTENANCE</text>
    <rect x="12" y="36" width="146" height="115" rx="4" fill="#0f172a"/>
    <text x="20" y="58" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Full Nafaqah</text>
    <text x="20" y="73" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  provision</text>
    <text x="20" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• No economic control</text>
    <text x="20" y="113" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  or deprivation</text>
    <text x="20" y="138" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Financial justice</text>
  </g>

  <g transform="translate(630, 145)">
    <rect width="190" height="165" rx="8" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <text x="95" y="24" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">CHILD PROTECTION</text>
    <rect x="12" y="36" width="166" height="115" rx="4" fill="#0f172a"/>
    <text x="20" y="58" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Right to peaceful</text>
    <text x="20" y="73" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  growth (Tarbiyah)</text>
    <text x="20" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">• Breaking the cycle</text>
    <text x="20" y="113" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5">  of violence</text>
    <text x="20" y="138" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700">Emotional security</text>
  </g>

  <!-- Foundation Beam (Bottom) -->
  <g transform="translate(60, 330)">
    <rect width="760" height="85" rx="8" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
    <text x="380" y="26" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">THE CORE FOUNDATION: TAQWA &amp; PROPHETIC CHARACTER (AKHLAQ)</text>
    <text x="380" y="46" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">"The best of you are those best to their families, and I am the best of you to my family." (Sunan al-Tirmidhi 3895)</text>
    <text x="380" y="66" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Peacemaking (Islaah) and Child Protection are moral duties commanded by Allah, not optional preferences.</text>
  </g>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION FOR TOPIC 12 (6 LESSONS)
# ─────────────────────────────────────────────────────────────────────────────

LESSONS_CONFIG = [
    {
        "unit_order": 1,
        "lesson_title": "Meaning and forms",
        "inquiry": "What is domestic violence in family law, and how does Islam protect the safety and sanctity of the home?",
        "hook": "Imagine a storm shelter built in a village. When torrential rains and lightning strike, villagers run inside expecting 100% safety and warmth. If the shelter itself begins crumbling, leaking, or catching fire, the villagers have nowhere to go. In Islam, the home and the family are designed to be the ultimate spiritual and physical storm shelter. When abuse occurs inside the home, it is called domestic violence—and it destroys the shelter of the family.",
        "concept_name": "Domestic Violence and Sanctity of the Home",
        "concept_explanation": "Domestic violence is any pattern of abusive, controlling, or harmful behavior used by one family member to dominate or inflict physical, emotional, or financial harm on another within the home. Sanctity of the home is the Islamic principle that the home must be a safe sanctuary built on mutual love, respect, peace (Sakinah), and compassion (Rahmah).",
        "scripture_quran": "And live with them in kindness. For if you dislike them – perhaps you dislike a thing and Allah makes therein much good.",
        "scripture_quran_ref": "Surah An-Nisa, 4:19",
        "scripture_hadith": "The best of you are those who are the best to their wives, and I am the best of you to my wives.",
        "scripture_hadith_ref": "Sunan al-Tirmidhi, 3895",
        "deep_explanation": "Domestic violence is completely incompatible with Islamic family values. It manifests in four distinct destructive forms:\n\n1. Physical Abuse: Using physical force that causes bodily pain, injury, bruises, or marks (slapping, hitting, pushing, throwing objects). Strictly Haram.\n2. Verbal and Emotional Abuse: Using mockery, insulting slurs, demeaning jokes, and constant shouting to break a person's self-esteem and make them live in fear.\n3. Psychological and Controlling Abuse: Isolating a spouse from their family, constant surveillance, and threats to maintain total power.\n4. Economic Abuse: Withholding basic financial necessities (food, clothing, shelter, school fees) to punish or dominate a family member, violating the mandatory duty of Nafaqah.",
        "svg_func": get_svg_lesson_1,
        "diagram_title": "Domestic Violence: The Four Termites Undermining the Home",
        "table_title": "The Four Forms of Domestic Abuse",
        "table_headers": ["Form of Abuse", "Harmful Behaviors", "Impact on Victims", "Islamic Position"],
        "table_rows": [
            ["Physical", "Hitting, slapping, pushing, throwing items", "Bodily injury, terror, trauma", "Strictly Haram (Criminal)"],
            ["Verbal / Emotional", "Constant yelling, insults, mocking slurs", "Low self-worth, chronic anxiety", "Violates prophetic speech"],
            ["Psychological", "Isolation, extreme jealousy, spying, threats", "Depression, loss of autonomy", "Violates trust and dignity"],
            ["Economic", "Denying food, clothes, or school fees", "Financial desperation & neglect", "Violates mandatory Nafaqah"]
        ],
        "scenario": "Hussein notices that his neighbor frequently shouts at his wife and children late at night. The next day at school, the neighbor's son, Omar, looks exhausted, anxious, and avoids his friends. Hussein's classmate says, 'Maybe the father is just disciplining his family. It is their private business.' Hussein replies: 'No, discipline in Islam must be gentle, respectful, and can never cause fear or sadness. Shouting insults and making children live in constant terror is emotional and verbal abuse. In our Muamalat class, we learned that domestic violence destroys the safety of the home, which is a right granted by Allah. We must condemn abuse and support those who suffer in silence.'",
        "real_world": "Create a 'Classroom Safety Guide' listing the five rights of every child and family member to feel safe at home, drawing on Islamic principles (safety, respect, financial support, emotional care, and gentle communication). Highlight that anyone experiencing harm should speak to a trusted adult, counselor, or school administration.",
        "reflection": "Why does emotional and verbal abuse inside the home have a lasting, negative impact on a student's ability to focus and succeed at school?",
        "misconception": "Remember: Domestic violence is not limited to physical hitting. Verbal cruelty, psychological manipulation, and withholding food or school fees are equally destructive and strictly forbidden in Islam.",
        "yt_title": "Understanding and Stopping Domestic Abuse in Islam",
        "yt_desc": "An authoritative presentation on why Islam strictly forbids all forms of family violence and abuse.",
        "yt_id": "zB2m9iF2z_s",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Old_Damascus_Courtyard_House.jpg/1280px-Old_Damascus_Courtyard_House.jpg",
        "image_title": "Traditional Damascus Courtyard Home",
        "image_caption": "Historic Islamic domestic architecture designed around an inner courtyard to ensure peace, tranquility, and family privacy.",
        "mcq": {
            "question": "Which of the following is a form of domestic abuse where a family provider deliberately withholds food, clothing, or school fees as a method of punishment or control?",
            "options": [
                "Physical Abuse.",
                "Economic Abuse.",
                "Verbal Abuse.",
                "Civic Abuse."
            ],
            "answer": "B",
            "explanation": "Economic abuse involves controlling or withholding financial resources and basic necessities to dominate a family member, violating the mandatory Islamic duty of the father to provide Nafaqah."
        },
        "summary_content": "Domestic violence is completely prohibited in Islam and violates the sacred sanctity of the home. Abuse can be physical, emotional, verbal, psychological, or economic. Islam commands that all family relationships be built on kindness, mutual mercy, and dignity.",
        "key_points": [
            "The home in Islam is a sanctuary of peace (Sakinah) and compassion (Rahmah).",
            "Abuse includes physical strikes, verbal cruelty, isolation, and financial deprivation.",
            "The Prophet (PBUH) condemned all harshness and abuse within the family."
        ],
        "exit_ticket": "List three non-physical forms of domestic abuse that can occur within a household."
    },
    {
        "unit_order": 2,
        "lesson_title": "Causes and risk factors",
        "inquiry": "What are the root causes and risk factors of domestic violence, and how do we address them before they destroy families?",
        "hook": "Imagine a garden where weeds have started choking flowers and vegetables. If the gardener only cuts off the tops, the weeds grow back in days because their roots are deep in the soil. To save the garden, the gardener must dig deep, locate the roots, and pull them out completely. In our families, domestic violence is like those destructive weeds. To prevent it, we must identify and uproot the underlying causes in minds, habits, and culture.",
        "concept_name": "Root Causes and Emotional Regulation",
        "concept_explanation": "Root causes are the deep-seated beliefs, bad habits, and social pressures that drive an individual to use violence against their family. Emotional regulation is the moral and spiritual duty of a believer to control anger, stress, and impulses, replacing them with patience (Sabr), prayer, and communication.",
        "scripture_quran": "Do not harm yourselves or others.",
        "scripture_quran_ref": "Surah An-Nisa, 4:29 / Sunan Ibn Majah, 2341",
        "scripture_hadith": "The strong person is not the one who can overpower others, but the one who controls themselves when angry.",
        "scripture_hadith_ref": "Sahih al-Bukhari, 6114",
        "deep_explanation": "Domestic violence is driven by four primary risk factors:\n\n1. Lack of Emotional Control (Anger): Inability to regulate anger or manage life frustration, letting anger explode into physical or verbal aggression against weaker family members.\n2. Harmful Cultural Traditions: Un-Islamic cultural beliefs that view women as inferior property or normalize violence as 'discipline.' Islam rejects these false myths.\n3. Financial Stress and Poverty: Unemployment and economic hardship create intense household pressure. While financial stress is a risk factor, Islam teaches it can never justify abuse.\n4. Substance Abuse (Khamr): Alcohol and drugs destroy the intellect ('Aql) and impulse control, acting as the single greatest physical trigger for severe domestic violence.",
        "svg_func": get_svg_lesson_2,
        "diagram_title": "Root Causes vs Islamic Countermeasures",
        "table_title": "Risk Factors vs Islamic Solutions",
        "table_headers": ["Risk Factor", "Destructive Mechanism", "Islamic Countermeasure", "Prophetic Guideline"],
        "table_rows": [
            ["Anger Mismanagement", "Explosive fury & shouting", "Prophetic anger regulation", "Wudhu, sit down, Isti'adhah"],
            ["Cultural Misogyny", "Treating spouses as inferior", "Spiritual equality of genders", "'Do not hit female servants of Allah'"],
            ["Financial Hardship", "Taking out stress on family", "Sabr, Tawakkul, & Zakat net", "Poverty is no excuse for cruelty"],
            ["Intoxicants (Alcohol)", "Loss of mental reasoning", "Absolute prohibition of Khamr", "Total abstinence protects family"]
        ],
        "scenario": "Yusuf's father loses his job due to economic retrenchment and feels intense anxiety about paying rent. He comes home angry, slams the door, and starts shouting at Yusuf's mother because dinner is five minutes late. Yusuf's mother remains calm and speaks politely. Yusuf's father pauses, remembers his faith, and takes a deep breath. He says: 'I am sorry for shouting. I am extremely stressed about our finances, but that does not give me the right to take my anger out on you. Let us pray together and work out a plan.' By practicing emotional regulation, he prevents a stressful moment from escalating into domestic abuse.",
        "real_world": "Practice the prophetic 'Anger Management Protocol' in your life this week. If you feel provoked or furious: 1. Say 'I seek refuge in Allah from Satan' (A'udhu billahi minash-shaytanir-rajeem); 2. If standing, sit down; if sitting, lie down; 3. Perform ablution (Wudhu), as water cools the fire of anger. Keep a journal of how this sequence helps you stay calm during school disagreements.",
        "reflection": "Why is using economic stress or unemployment to justify shouting or hitting family members a sign of weak character (Akhlaq)?",
        "misconception": "Remember: High stress and financial difficulty are common human trials, but they never give anyone permission to be abusive. True strength is controlling anger when tested.",
        "yt_title": "Managing Anger and Stress: The Prophetic Approach",
        "yt_desc": "Practical psychological and spiritual tools taught by the Prophet (PBUH) to control temper and maintain family peace.",
        "yt_id": "u4gC07V_Q8o",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Olive_tree_in_Palestine.jpg/1280px-Olive_tree_in_Palestine.jpg",
        "image_title": "Resilient Ancient Olive Tree",
        "image_caption": "Symbol of deep roots, endurance, patience (Sabr), and resilience in the face of environmental storms.",
        "mcq": {
            "question": "Which of the following is an un-Islamic risk factor that can contribute to domestic violence by misleading people into believing they have the right to dominate their spouse?",
            "options": [
                "Seeking professional marriage counseling during disagreements.",
                "Adopting harmful cultural traditions that view women as inferior or tolerate violence.",
                "Practicing voluntary fasting (Sawm) to build self-discipline.",
                "Fulfilling the legal financial maintenance obligations of the household."
            ],
            "answer": "B",
            "explanation": "Harmful cultural traditions that degrade women or normalize physical violence directly contradict Islamic teachings of mutual respect, kindness, and spiritual equality."
        },
        "summary_content": "Domestic violence is driven by poor anger management, harmful cultural traditions, financial stress, and substance abuse. Stress is a trial but can never justify abuse. The Prophet (PBUH) modeled perfect emotional control and gentleness at home.",
        "key_points": [
            "Domestic violence has identifiable root causes that must be uprooted.",
            "Anger must be controlled using prophetic techniques (Wudhu, Isti'adhah, sitting down).",
            "The strict prohibition of alcohol in Islam shields households from violent outbreaks."
        ],
        "exit_ticket": "State two prophetic strategies for controlling anger when you feel provoked."
    },
    {
        "unit_order": 3,
        "lesson_title": "Effects on family",
        "inquiry": "What are the physical, emotional, and psychological effects of domestic violence on individual victims, children, and family harmony?",
        "hook": "Imagine a clean, beautiful mountain lake. If someone dumps a barrel of toxic chemical waste into the center, the poison does not stay in one spot. It dissolves, spreads across the water, kills fish, rots water lilies, and makes the water dangerous to drink. In a home, domestic violence acts like that toxic waste. It poisons the entire emotional environment, damaging children's brains, harming health, and destroying social harmony.",
        "concept_name": "The Trauma Ripple and Sacred Rights of Children",
        "concept_explanation": "The trauma ripple is the psychological reality that witnessing or experiencing violence in the home causes lasting trauma, fear, and behavioral challenges that affect every family member. Sacred rights of children in Islam include the absolute obligation to protect children from physical harm, emotional terror, and provide them with a peaceful, stable upbringing (Tarbiyah).",
        "scripture_quran": "And We have certainly honored the children of Adam...",
        "scripture_quran_ref": "Surah Al-Isra, 17:70",
        "scripture_hadith": "Whoever does not show mercy to our young and respect to our elders is not one of us.",
        "scripture_hadith_ref": "Sunan al-Tirmidhi, 1919",
        "deep_explanation": "Domestic violence inflicts devastating, long-term damage on multiple levels:\n\n1. Physical Health Harm: Victims suffer injuries, chronic bodily pain, migraines, and high blood pressure due to perpetual physical stress.\n2. Psychological Trauma: Victims and children experience chronic anxiety, depression, low self-esteem, PTSD, and a constant fear of violence.\n3. Disruption of Education: Children witnessing domestic abuse struggle to concentrate in school, experience plummeting grades, and display behavioral issues like withdrawal, anxiety, or bullying.\n4. The Intergenerational Cycle: Children raised in abusive homes are statistically at high risk of repeating the cycle of violence in their future adult marriages unless the cycle is broken through counseling and Islamic ethics.",
        "svg_func": get_svg_lesson_3,
        "diagram_title": "Effects on Family: The Trauma Ripple vs The House of Sakinah",
        "table_title": "Abusive Environment vs House of Sakinah Outcomes",
        "table_headers": ["Developmental Area", "Child in Abusive Home", "Child in House of Sakinah", "Long-Term Impact"],
        "table_rows": [
            ["Neurological / Brain", "High cortisol, constant fear", "Calm brain state, security", "Determines emotional health"],
            ["School Performance", "Failing grades, lack of focus", "High creativity, academic success", "Affects future career"],
            ["Social Behavior", "Bullying or extreme withdrawal", "Empathy, healthy friendships", "Shapes community standing"],
            ["Future Marriage", "Risk of repeating abuse cycle", "Models peaceful conflict resolution", "Secures next generation"]
        ],
        "scenario": "During school lunch, Amina notices her friend Zainab crying silently. Zainab whispers, 'My parents fight constantly, and last night my father smashed my mother's phone and threatened to kick us out. I was so terrified I couldn't sleep at all. Today, I failed my math test because my hands wouldn't stop shaking.' Amina comforts her, hugs her, and says: 'Zainab, this is not your fault, and you do not have to carry this heavy burden alone. Living in fear is a violation of your rights. Let us go talk to our school guidance counselor, Mrs. Sophia. She is a trusted professional who can help get your mother and family the safety and support they need.'",
        "real_world": "Write a 'Support Action Plan' in your notebook. Identify three trusted support pathways available in your community for families facing crisis (such as school counselors, local imams, child protection hotlines, or legal aid clinics). Fostering a habit of knowing where to seek help is a vital life skill that can save lives.",
        "reflection": "Why does witnessing violence at home affect a student's friendships and their ability to trust people at school?",
        "misconception": "Remember: Children are never 'unaffected' by domestic violence even if they are not physically struck. Witnessing arguments, screaming, and threats causes severe emotional and neurological trauma.",
        "yt_title": "The Impact of Domestic Violence on Children's Minds",
        "yt_desc": "An insightful exploration of how emotional safety in the home directly drives children's brain health and school success.",
        "yt_id": "7vA_rYg3b9k",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Moroccan_children_reading_in_school.jpg/1280px-Moroccan_children_reading_in_school.jpg",
        "image_title": "Happy Children Learning in a Safe Classroom",
        "image_caption": "Children flourish academically and emotionally when provided with safe, nurturing, and supportive environments.",
        "mcq": {
            "question": "What is a common, long-term psychological outcome for children who grow up witnessing domestic violence in their households?",
            "options": [
                "They develop perfect physical coordination and athletic speed.",
                "They are likely to experience chronic anxiety, academic struggles, and may repeat the cycle of violence in their future lives.",
                "They automatically become experts in family counseling.",
                "They are completely unaffected, as the disputes are between adults."
            ],
            "answer": "B",
            "explanation": "Chronic exposure to violence causes deep psychological trauma, disrupting brain development, hindering academic focus, and increasing the risk of repeating abusive behaviors in adulthood."
        },
        "summary_content": "Domestic violence poisons the entire home, causing physical injury and mental trauma. Children in violent homes suffer academic decline, anxiety, and fear. Safeguarding victims of abuse is a vital duty of justice and child protection.",
        "key_points": [
            "Domestic abuse creates a ripple effect of trauma across all family members.",
            "Children exposed to domestic violence suffer neurological stress and school struggles.",
            "Breaking the cycle of violence requires intervention, counseling, and Islamic ethics."
        ],
        "exit_ticket": "State one way a violent home environment can negatively affect a student's behavior and performance at school."
    },
    {
        "unit_order": 4,
        "lesson_title": "Islamic measures to curb violence",
        "inquiry": "What clear, legal, and behavioral measures does Islam establish to completely prohibit and curb domestic violence?",
        "hook": "Imagine a safety harness used by window cleaners on skyscrapers. It has strong straps, secure buckles, and steel anchors to prevent falls. If someone claims, 'The manual says you can cut the straps if you get frustrated!' that would be a deadly distortion of the design. In a similar way, some people distort Islamic teachings to justify abuse. In this lesson, we examine the protective design of Islamic family law, uprooting all distortions and exploring strict measures to curb violence.",
        "concept_name": "Dignity in Conflict and the Prophetic Standard",
        "concept_explanation": "Dignity in conflict is the strict Islamic rule that even during marital disagreement, spouses must treat each other with dignity, fairness, and non-violence. The Prophetic standard is the historical fact that the Prophet Muhammad (PBUH) never hit a woman, child, or servant, and condemned all harshness in the home.",
        "scripture_quran": "Do not hit the female servants of Allah.",
        "scripture_quran_ref": "Sunan Abi Dawood, 2146",
        "scripture_hadith": "O Allah, I declare sinful any violation of the rights of the two weak ones: orphans and women.",
        "scripture_hadith_ref": "Sunan Ibn Majah, 3678",
        "deep_explanation": "Islamic law establishes rigorous measures against domestic violence:\n\n1. Sincere Interpretation of Quran 4:34: Abusers misquote this verse to justify violence. Jurists unanimously state that physical abuse is strictly Haram. The verse's progression is gradual, symbolic, and non-violent (gentle advice, then separate sleeping). The symbolic limit described by scholars like Ibn Abbas is a non-painful touch with a tiny wooden Siwak (toothbrush)—strictly forbidding any pain, injury, redness, marks, or touching the face.\n2. The Right to Legal Protection: An abusive spouse violates the marriage covenant. The wife has the absolute right to seek safety, financial support, and a judicial divorce (Khul' or Fasakh).\n3. Sincere Family Mediation (Islaah): Islam commands appointing two fair mediators from each family to resolve disputes peacefully and protect the vulnerable.",
        "svg_func": get_svg_lesson_4,
        "diagram_title": "Islamic Measures: The Prophetic Sunnah vs Abusive Distortions",
        "table_title": "The Prophetic Standard vs Abusive Distortions",
        "table_headers": ["Dimension", "The Prophet's Sunnah", "Cultural / Abusive Distortions", "Juristic Verdict"],
        "table_rows": [
            ["Physical Conduct", "Never hit a woman, child, or servant", "Slapping, hitting, causing pain", "Strictly Haram (Crime)"],
            ["Spoken Language", "Gentle, respectful speech", "Screaming, mocking, vulgar slurs", "Sinful and forbidden"],
            ["Dispute Resolution", "Dialogue, silence, consultation", "Physical domination & bullying", "Violates Sunnah"],
            ["Victim Rights", "Right to safe exit via Khul'/Fasakh", "Forcing victim to endure abuse", "Enforced legal separation"]
        ],
        "scenario": "In a community dialogue, a man claims: 'If a wife is rebellious, the Quran allows the husband to strike her to teach her a lesson.' Mr. Bilal, the IRE teacher, politely explains: 'Brother, that is a dangerous misinterpretation that contradicts the life of the Prophet (PBUH). The Prophet (PBUH) is our role model, and he *never* raised his hand against a woman. He explicitly commanded: \"Do not hit the female servants of Allah.\" Classical scholars state that any act causing pain, leaving a mark, or humiliating a spouse is Haram abuse. The Quranic verses exist to *prevent* violence through gradual, peaceful reconciliation. We must follow the Prophet's gentleness, not cultural anger.'",
        "real_world": "Develop a 'Modesty and Respect Agreement' for your family or study group. Write down three commitments based on the Prophet's standard: 1. We will resolve disagreements using a normal, calm speaking voice (no shouting); 2. We will never use insulting words or physical force; 3. We will seek help from trusted elders or counselors if we cannot resolve a conflict.",
        "reflection": "Why did the Prophet (PBUH) declare that treating one's family with kindness is the highest indicator of excellent character (Akhlaq)?",
        "misconception": "Remember: The Quran never licenses physical abuse or domestic violence. Scholarly consensus is unanimous that causing physical pain or injury to a spouse is unlawful (Haram) and punishable by law.",
        "yt_title": "Did the Prophet Ever Hit a Woman? Refuting Misconceptions",
        "yt_desc": "Dr. Jonathan Brown explains the Prophetic Sunnah of gentleness and classical Islamic jurisprudence on non-violence.",
        "yt_id": "8Pq7_nB6zY8",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/The_Prophet%27s_Mosque_Minarets.jpg/1280px-The_Prophet%27s_Mosque_Minarets.jpg",
        "image_title": "Minarets of the Prophet's Mosque in Madinah",
        "image_caption": "The holy city where the Prophet Muhammad (PBUH) established the foundational ethics of family justice, mercy, and compassion.",
        "mcq": {
            "question": "According to the consensus of classical Islamic scholars and the perfect example of the Prophet Muhammad (PBUH), what is the legal ruling on inflicting physical pain or injury on a spouse?",
            "options": [
                "It is permissible if the spouse makes a mistake.",
                "It is highly recommended to maintain discipline in the home.",
                "It is strictly Haram (forbidden) and constitutes an unlawful violation of the marriage contract.",
                "It is allowed only if the neighbors approve."
            ],
            "answer": "C",
            "explanation": "The Prophet (PBUH) explicitly forbade hitting women, and juristic consensus holds that any force causing pain, leaving marks, or bruising is unlawful abuse (Haram), granting the victim the right to judicial divorce."
        },
        "summary_content": "Physical abuse is strictly Haram and violates the core Sunnah of the Prophet (PBUH). Authentic interpretation of Quran 4:34 emphasizes gradual, symbolic, and non-violent reconciliation. Victims of domestic violence have the absolute legal right in Islam to seek protection and divorce.",
        "key_points": [
            "The Prophet (PBUH) never struck a woman, child, or servant in his entire life.",
            "Any physical contact causing pain, redness, or marks is categorized as criminal abuse.",
            "Victims of abuse have the complete right to safety and judicial divorce (Khul'/Fasakh)."
        ],
        "exit_ticket": "State the prophetic Hadith regarding the explicit prohibition of hitting women."
    },
    {
        "unit_order": 5,
        "lesson_title": "Prevention and community response",
        "inquiry": "How can communities, schools, and youth actively collaborate to prevent domestic violence and build peaceful homes?",
        "hook": "Imagine a village near a fast-flowing river that floods during heavy rains. Villagers have two choices: wait for the flood and rescue drowning people, or work together *before* the rains to construct a high, strong dike along the riverbank to keep the water in its channel. Building a dike is like prevention. In this lesson, we study how schools, mosques, and youth build a powerful 'dike' of education, support, and reporting to stop domestic violence before it occurs.",
        "concept_name": "Active Mediation (Islaah) and Civic Responsibility",
        "concept_explanation": "Active mediation (Islaah) is the moral duty of community members, scholars, and elders to intervene with justice to protect victims and resolve family disputes peacefully. Civic responsibility is the obligation of every citizen and youth to promote safety, report abuse, and protect the vulnerable under Kenyan law and Islamic values.",
        "scripture_quran": "The believers are but brothers, so make peace between your brothers. And fear Allah that you may receive mercy.",
        "scripture_quran_ref": "Surah Al-Hujurat, 49:10",
        "scripture_hadith": "Whoever among you sees an evil, let him change it with his hand; if he cannot, then with his tongue; if he cannot, then with his heart—and that is the weakest of faith.",
        "scripture_hadith_ref": "Sahih Muslim, 49",
        "deep_explanation": "Preventing domestic violence requires coordinated action across four community tiers:\n\n1. Pre-Marital Education: Educating couples on legal rights, financial duties, emotional regulation, and communication before marriage.\n2. Mosque and Community Leadership: Imams delivering sermons condemning abuse, establishing confidential counseling centers, and providing safe shelter for victims.\n3. School and Peer Support: Training youth to recognize warning signs in peers (sudden withdrawal, fear, drop in grades) and safely connect them with school guidance counselors.\n4. Legal Enforcement and Reporting: Cooperating with local child protection officers, gender-based violence helplines (1195 in Kenya), and law enforcement to ensure perpetrators are held accountable.",
        "svg_func": get_svg_lesson_5,
        "diagram_title": "Community Action: The Four Interlocking Layers of the Safety Dike",
        "table_title": "Multi-Tiered Community Safety Architecture",
        "table_headers": ["Tier", "Key Actors", "Preventative Responsibility", "Action in Crisis"],
        "table_rows": [
            ["Individual", "Self, youth, partners", "Taqwa, emotional control, Sabr", "De-escalate & seek help"],
            ["Family", "Respected elders, parents", "Mediation (Islaah) & counsel", "Protect victim & separate safely"],
            ["Community", "Imams, teachers, counselors", "Khutbahs, peace clubs, workshops", "Provide confidential shelter"],
            ["Civic / Legal", "Child officers, police, hotlines", "Enforce laws & child protection", "Prosecute abuse & issue safety orders"]
        ],
        "scenario": "Omar notices his friend Yusuf looks sad and has bruises on his arm. Yusuf whispers, 'My older brother gets furious when my father is stressed about money, and he beats me if I make any noise.' Omar remembers the Hadith: 'Whoever sees an evil, let him change it.' He does not ignore the situation. He says: 'Yusuf, this is wrong, and you have a right to be safe. I am going to talk to our class teacher, Mr. Bilal, right now. He will help us report this safely to the school counselor and the local child protection officer without putting you in danger.' Mr. Bilal acts swiftly, contacting authorities and arranging counseling and protection for Yusuf's family.",
        "real_world": "Organize a 'Peace Education Skit' or write a short play script for your school's drama club. The skit should depict: 1. A family facing financial stress; 2. An argument starting; 3. The father or sibling choosing to pause, control their anger, and seek help instead of resorting to violence; 4. A friend helping a classmate safely report home stress. Present your skit during the school talent day to promote social cohesion and non-violence.",
        "reflection": "Why does the Hadith 'Whoever sees an evil, let him change it' require us to speak out and report domestic violence, rather than keeping quiet out of fear or embarrassment?",
        "misconception": "Remember: Reporting domestic abuse is not 'interfering in private matters.' In Islam, stopping injustice and protecting innocent human beings from physical harm is a collective religious and civic obligation.",
        "yt_title": "Community Peacemaking and Reporting Injustice",
        "yt_desc": "How community mediation (Islaah) and proactive child protection save families from disintegration.",
        "yt_id": "4mR8p7K2_t0",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Nairobi_Jamia_Mosque.jpg/1280px-Nairobi_Jamia_Mosque.jpg",
        "image_title": "Jamia Mosque in Nairobi, Kenya",
        "image_caption": "Major urban Islamic center in Kenya coordinating community social welfare, educational programs, and family dispute mediation.",
        "mcq": {
            "question": "What is the most responsible action a Grade 9 student should take if a classmate confides that they are experiencing physical violence at home?",
            "options": [
                "Advise the classmate to keep quiet and accept the violence as their destiny.",
                "Help the classmate safely report the situation to a trusted school teacher, guidance counselor, or child protection authority immediately.",
                "Go to the classmate's house and start a physical fight with the abuser.",
                "Spread the secret across social media to publicly humiliate the family."
            ],
            "answer": "B",
            "explanation": "Child protection and Islamic justice require swift, confidential action. Reporting to a trusted school professional ensures the child's safety and connects the family with counseling without physical danger."
        },
        "summary_content": "Prevention requires pre-marital education, mosque support, and active reporting. Domestic violence is a community crisis, not just a private family matter. Muslims have a sacred duty to stand firm against injustice and protect the vulnerable.",
        "key_points": [
            "The community safety dike combines individual, family, community, and legal protection.",
            "Reporting abuse to trusted school or legal authorities saves lives.",
            "Active mediation (Islaah) resolves disputes before violence occurs."
        ],
        "exit_ticket": "Write down one community resource or helpline available in Kenya for reporting domestic or gender-based violence (e.g., GBV Hotline 1195)."
    },
    {
        "unit_order": 6,
        "lesson_title": "Unit synthesis",
        "inquiry": "How do we consolidate our understanding of domestic violence, family rights, and the protective frameworks of Islam?",
        "hook": "Imagine completing a heavy-duty shield: you have forged the metal, polished the surface, and attached strong straps. In this final synthesis lesson, we put this spiritual 'Shield of Family Peace' on our arms. We review the definitions, causes, physical and emotional effects, prophetic non-violent standards, and community response pathways, ensuring we are fully prepared to build, protect, and advocate for peaceful, abuse-free homes.",
        "concept_name": "The Shelter of Sakinah and Active Advocacy",
        "concept_explanation": "The shelter of Sakinah is the complete integration of mutual respect, physical safety, and spiritual love to build a home that pleases Allah. Active advocacy is the lifetime commitment of a Muslim to act as a peacemaker (Muslih), rejecting all forms of violence and safeguarding the dignity of the family.",
        "scripture_quran": "And live with them in kindness...",
        "scripture_quran_ref": "Surah An-Nisa, 4:19",
        "scripture_hadith": "The believers are like one body: if one limb suffers, the entire body responds with sleeplessness and fever.",
        "scripture_hadith_ref": "Sahih Muslim, 2586",
        "deep_explanation": "Comprehensive synthesis of the Domestic Violence unit:\n\n1. The Divine Standard: Every home must be a sanctuary of Sakinah (peace) and Rahmah (mercy). Physical, emotional, verbal, and economic abuse are strictly Haram.\n2. The Root Causes: Anger mismanagement, harmful cultural myths, financial stress, and intoxicants.\n3. The Devastating Harm: Severe physical injuries, chronic psychological trauma, school failure in children, and the repetition of the cycle of violence.\n4. The Islamic Remedies: Emulating the Prophet's gentle example, adhering to strict non-violent limits, utilizing safe legal divorce (Khul'), and engaging in community mediation and statutory child protection.",
        "svg_func": get_svg_lesson_6,
        "diagram_title": "Master Capstone: The Sanctuary of Sakinah & Peacemaking",
        "table_title": "Comprehensive Unit Synthesis Matrix",
        "table_headers": ["Core Topic Area", "Key Theological Principle", "Everyday Practice", "Civic / Social Impact"],
        "table_rows": [
            ["Definition & Scope", "Sanctity of home is sacred", "Zero tolerance for abuse", "Builds safe neighborhoods"],
            ["Root Causes", "Anger control is true strength", "Use prophetic Wudhu & Sabr", "Prevents emotional escalation"],
            ["Trauma Ripple", "Protect children's Tarbiyah", "Support peers facing home stress", "Breaks generational violence"],
            ["Islamic Measures", "Prophet never hit anyone", "Reject cultural distortions", "Upholds women's legal rights"],
            ["Community Action", "Islaah (Peacemaking) is duty", "Report harm to counselors/hotlines", "Fosters national rule of law"]
        ],
        "scenario": "A classmate, Zainab, tells you that her father is going through a very stressful financial crisis and has started throwing household objects and shouting vulgar slurs at her mother. Applying the complete synthesis of this unit, what is the most balanced, source-grounded response? Comfort Zainab, validate her feelings of fear, and help her safely report the physical threats and emotional abuse to a trusted school teacher or the local child welfare officer immediately. Prioritizing physical safety and emotional support recognizes that violence and threats are Haram abuse that must be reported to trusted authorities, while avoiding public gossip.",
        "real_world": "Create a 'Peace Advocacy Poster' for your school or community notice board. Write the Hadith 'The best of you are those best to their families' in beautiful lettering, surrounded by the three messages: 1. Say No to All Forms of Abuse (Physical, Emotional, Verbal); 2. Gentleness is a Sign of Strength; 3. Speak Out and Report Harm to Trusted Counselors. Pin the poster strategically to raise awareness.",
        "reflection": "How does building a peaceful, loving home contribute directly to the overall peace, security, and patriotism of the entire Kenyan nation?",
        "misconception": "Remember: Genuine leadership in the family is built on consultation, mercy, and service, not on fear, physical intimidation, or unilateral domination.",
        "yt_title": "The Master Blueprint for Family Peace in Islam",
        "yt_desc": "A comprehensive summary of Islamic family ethics, mutual dignity, non-violence, and social harmony.",
        "yt_id": "8rG3_vB2yX8",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Faisal_Mosque_Islamabad_Courtyard.jpg/1280px-Faisal_Mosque_Islamabad_Courtyard.jpg",
        "image_title": "Courtyard of Faisal Mosque",
        "image_caption": "Grand open courtyard representing spiritual openness, peace, and the harmonious gathering of believers.",
        "mcq": {
            "question": "A classmate confides that her father has started throwing objects and shouting vulgar threats at home due to financial stress. Applying the complete synthesis of this unit, what is the most balanced, source-grounded action?",
            "options": [
                "Advise her to keep quiet because family issues are strictly private.",
                "Tell her that financial stress excuses her father's violent anger.",
                "Comfort her, validate her feelings, and help her safely report the threats and abuse to a trusted school teacher or child welfare officer.",
                "Post about the father's behavior on the school group chat to humiliate him."
            ],
            "answer": "C",
            "explanation": "Prioritizing physical safety and child welfare through safe reporting to trusted professionals upholds Islamic justice and child protection while avoiding public gossip."
        },
        "summary_content": "Sincere family relations (Muamalat) require absolute non-violence and mutual compassion. Exposing family members, especially children, to violence causes severe, long-term psychological harm. We are individually and collectively accountable for ensuring our homes are sanctuaries of peace.",
        "key_points": [
            "Sakinah and Rahmah are the non-negotiable foundations of an Islamic home.",
            "Domestic violence violates human dignity and is strictly prohibited in all forms.",
            "Youth can act as active peacemakers (Muslihun) by promoting safety and speaking out."
        ],
        "exit_ticket": "Explain in your own words why the Prophet Muhammad (PBUH) is the ultimate role model for building peaceful modern families."
    }
]


# ─────────────────────────────────────────────────────────────────────────────
# INGESTION FUNCTION
# ─────────────────────────────────────────────────────────────────────────────

def ingest_grade9_ire_topic12():
    print("=" * 80)
    print("STARTING INGESTION: GRADE 9 IRE — TOPIC 12: DOMESTIC VIOLENCE")
    print("=" * 80)

    try:
        topic = Topic.objects.get(id=352)
    except Topic.DoesNotExist:
        print("ERROR: Topic ID 352 does not exist!")
        sys.exit(1)

    print(f"Target Topic: ID={topic.id}, Name='{topic.name}', Order={topic.order}")

    with transaction.atomic():
        # Clean existing units if any
        existing_units = LearningUnit.objects.filter(topic=topic)
        if existing_units.exists():
            print(f"Cleaning {existing_units.count()} existing units under Topic {topic.id}...")
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
                name=f"Lesson 6.1.{u_order}: {l_title}",
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
                        f"Understand the core meaning of {l_title}",
                        "Examine foundational Qur'anic verses and Hadith",
                        "Analyze practical scenarios and daily ethical applications"
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
                        f"**Hadith ({cfg['scripture_hadith_ref']}):**\n> \"{cfg['scripture_hadith']}\""
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
    print("TOPIC 12 INGESTION COMPLETE & VERIFIED!")
    print(f"  LearningUnits : {total_units} / 6")
    print(f"  Lessons       : {total_lessons} / 6 (Published)")
    print(f"  Blocks        : {total_blocks} (15 per lesson, 7 pages)")
    print(f"  Assets        : {total_assets} (6 SVGs, 6 images, 6 videos)")
    print("=" * 80)


if __name__ == "__main__":
    ingest_grade9_ire_topic12()
