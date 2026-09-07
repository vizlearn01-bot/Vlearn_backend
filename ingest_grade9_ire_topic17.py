"""
VLearn CBC Grade 9 IRE — Topic 17: Contemporary Issues (Jihad, Terrorism, and Extremism)
Production Ingestion and Enrichment Script for all 6 Lessons

Target Topic in DB: Topic ID 357 (Subject: IRE ID 53, Grade: Grade 9 ID 18)
Source Markdown: /home/jason-bitega/Desktop/VL/vlearn_repositories/Grade 9 IRE/contemporary-issues.md

6 Lessons Ingested & Fully Enriched:
  1. Lesson 6.6.1: Jihad: correct interpretation
  2. Lesson 6.6.2: Terrorism and extremism: meanings
  3. Lesson 6.6.3: Causes
  4. Lesson 6.6.4: Effects
  5. Lesson 6.6.5: Prevention and response
  6. Lesson 6.6.6: Unit synthesis
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
    """Lesson 6.6.1: True Jihad vs Violent Distortion Matrix"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg171" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg171)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">TRUE JIHAD VS. VIOLENT EXTREMIST DISTORTION</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Rescuing the Sacred Islamic Concept of Striving (Jihad) from Criminal and Terrorist Misinterpretations</text>

  <!-- Left: True Islamic Jihad -->
  <g transform="translate(45, 80)">
    <rect width="375" height="300" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect width="375" height="42" rx="10" fill="#065f46"/>
    <text x="187" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">AUTHENTIC ISLAMIC JIHAD (STRIVING)</text>
    
    <text x="24" y="70" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Core Purpose: Moral Excellence &amp; Self-Defense</text>
    <text x="24" y="96" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11.5">
      <tspan x="24" dy="0">✓ Greater Jihad: Inner spiritual struggle against sin</tspan>
      <tspan x="24" dy="24">✓ Striving in education, righteous work &amp; charity</tspan>
      <tspan x="24" dy="24">✓ Defensive armed struggle strictly under legal state authority</tspan>
      <tspan x="24" dy="24">✓ Strict ban on targeting civilians, women &amp; children</tspan>
      <tspan x="24" dy="24">✓ Complete protection of houses of worship &amp; nature</tspan>
      <tspan x="24" dy="24">✓ Surah Al-Baqarah 2:190: "Do not transgress"</tspan>
    </text>
    
    <rect x="20" y="250" width="335" height="36" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
    <text x="187" y="273" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Outcome: Spiritual Purity, Justice &amp; Peace</text>
  </g>

  <!-- Right: Violent Terrorist Distortion -->
  <g transform="translate(460, 80)">
    <rect width="375" height="300" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <rect width="375" height="42" rx="10" fill="#991b1b"/>
    <text x="187" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">CRIMINAL EXTREMIST DISTORTION</text>
    
    <text x="24" y="70" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Core Reality: Unlawful Violence &amp; Terror</text>
    <text x="24" y="96" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11.5">
      <tspan x="24" dy="0">❌ Unprovoked slaughter, bombings &amp; kidnapping</tspan>
      <tspan x="24" dy="24">❌ Declared by illegal, self-appointed criminal gangs</tspan>
      <tspan x="24" dy="24">❌ Deliberately targets markets, schools &amp; hospitals</tspan>
      <tspan x="24" dy="24">❌ Ruthlessly murders innocent civilians and Muslims</tspan>
      <tspan x="24" dy="24">❌ Distorts Quranic verses by ripping them from context</tspan>
      <tspan x="24" dy="24">❌ Declared strictly Haram; grave crime against humanity</tspan>
    </text>
    
    <rect x="20" y="250" width="335" height="36" rx="6" fill="#450a0a" stroke="#ef4444" stroke-width="1"/>
    <text x="187" y="273" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Outcome: Horror, Ruin &amp; Divine Condemnation</text>
  </g>

  <!-- Footer Banner -->
  <rect x="45" y="394" width="790" height="30" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="440" y="414" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">"Fight in the way of Allah those who fight you, but do not transgress. Indeed, Allah does not like transgressors." — Surah Al-Baqarah 2:190</text>
</svg>"""


def get_svg_lesson_2():
    """Lesson 6.6.2: The Wasatiyyah (Moderation) Balance Scale"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg172" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg172)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE SPECTRUM OF RELIGIOUS PRACTICE: WASATIYYAH (MODERATION)</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Navigating Between the Pitfalls of Laxity and the Destructive Edge of Extremism</text>

  <!-- Left: Laxity / Neglect -->
  <g transform="translate(45, 95)">
    <rect width="230" height="270" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="230" height="38" rx="8" fill="#b45309"/>
    <text x="115" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">TAFRIT (LAXITY / NEGLECT)</text>
    
    <text x="18" y="65" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600">The Pitfall of Carelessness</text>
    <text x="18" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="18" dy="0">• Abandoning prayers &amp; duties</tspan>
      <tspan x="18" dy="20">• Moral apathy and compromise</tspan>
      <tspan x="18" dy="20">• Ignoring Islamic ethical codes</tspan>
      <tspan x="18" dy="20">• Loss of religious identity</tspan>
      <tspan x="18" dy="20">• Spiritual emptiness</tspan>
    </text>
    <rect x="18" y="220" width="194" height="28" rx="4" fill="#0f172a"/>
    <text x="115" y="238" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Deviation to the Left</text>
  </g>

  <!-- Center: Wasatiyyah (The Middle Path) -->
  <g transform="translate(305, 80)">
    <rect width="270" height="300" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2.5"/>
    <rect width="270" height="44" rx="10" fill="#059669"/>
    <text x="135" y="28" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">WASATIYYAH (MIDDLE PATH)</text>
    
    <circle cx="135" cy="85" r="26" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
    <text x="135" y="93" fill="#34d399" font-family="system-ui, sans-serif" font-size="18" font-weight="bold" text-anchor="middle">⚖</text>
    
    <text x="135" y="135" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">The Divine Standard of Islam</text>
    <text x="20" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11.5">
      <tspan x="20" dy="0">• Balance between faith &amp; worldly life</tspan>
      <tspan x="20" dy="20">• Compassion, mercy &amp; patience</tspan>
      <tspan x="20" dy="20">• Respect for diversity &amp; dialogue</tspan>
      <tspan x="20" dy="20">• Protecting human dignity for all</tspan>
      <tspan x="20" dy="20">• Surah Al-Baqarah 2:143: "Just Community"</tspan>
    </text>
    <rect x="20" y="250" width="230" height="32" rx="6" fill="#064e3b"/>
    <text x="135" y="271" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">The Balanced Straight Path (Sirat)</text>
  </g>

  <!-- Right: Ghuluww (Extremism) -->
  <g transform="translate(605, 95)">
    <rect width="230" height="270" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="230" height="38" rx="8" fill="#b91c1c"/>
    <text x="115" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">GHULUWW (EXTREMISM)</text>
    
    <text x="18" y="65" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600">The Pitfall of Fanaticism</text>
    <text x="18" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="18" dy="0">• Rigidity and intolerance</tspan>
      <tspan x="18" dy="20">• Declaring Muslims apostates (Takfir)</tspan>
      <tspan x="18" dy="20">• Hatred, cruelty and arrogance</tspan>
      <tspan x="18" dy="20">• Justifying unprovoked violence</tspan>
      <tspan x="18" dy="20">• Prophet (PBUH) warned: "Destroyed!"</tspan>
    </text>
    <rect x="18" y="220" width="194" height="28" rx="4" fill="#0f172a"/>
    <text x="115" y="238" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Deviation to the Right</text>
  </g>

  <!-- Bottom Banner -->
  <rect x="45" y="395" width="790" height="30" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="440" y="415" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">"Beware of extremism in religion, for those who came before you were destroyed by extremism." — Sunan an-Nasa'i 3057</text>
</svg>"""


def get_svg_lesson_3():
    """Lesson 6.6.3: Root Causes of Radicalization & Vulnerability Factors"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg173" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg173)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">ANATOMY OF RADICALIZATION: THE FOUR VULNERABILITY GEARS</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Understanding the Social, Psychological and Educational Factors Manipulated by Extremists</text>

  <!-- 4 Interlocking Driver Cards -->
  <!-- Gear 1: Religious Ignorance -->
  <g transform="translate(45, 85)">
    <rect width="185" height="290" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="185" height="38" rx="8" fill="#991b1b"/>
    <text x="92" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. RELIGIOUS IGNORANCE</text>
    
    <circle cx="92" cy="72" r="22" fill="#450a0a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="92" y="79" fill="#ef4444" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">!</text>
    
    <text x="92" y="118" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12.5" font-weight="600" text-anchor="middle">Distorted Concepts</text>
    <text x="14" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="14" dy="0">• Lack of authentic Fiqh</tspan>
      <tspan x="14" dy="18">• Cherry-picking verses</tspan>
      <tspan x="14" dy="18">  without context (Asbab)</tspan>
      <tspan x="14" dy="20">• Blind following of</tspan>
      <tspan x="14" dy="18">  unqualified internet voices</tspan>
      <tspan x="14" dy="20">• Black-and-white thinking</tspan>
    </text>
    <rect x="14" y="242" width="157" height="24" rx="4" fill="#0f172a"/>
    <text x="92" y="258" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Intellectual Vulnerability</text>
  </g>

  <!-- Gear 2: Socioeconomic Despair -->
  <g transform="translate(245, 85)">
    <rect width="185" height="290" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="185" height="38" rx="8" fill="#b45309"/>
    <text x="92" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. SOCIOECONOMIC</text>
    
    <circle cx="92" cy="72" r="22" fill="#78350f" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="92" y="79" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">$</text>
    
    <text x="92" y="118" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12.5" font-weight="600" text-anchor="middle">Grievance &amp; Poverty</text>
    <text x="14" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="14" dy="0">• Youth unemployment</tspan>
      <tspan x="14" dy="20">• Severe poverty &amp; despair</tspan>
      <tspan x="14" dy="20">• Feeling of injustice</tspan>
      <tspan x="14" dy="18">  and marginalization</tspan>
      <tspan x="14" dy="20">• Financial recruitment</tspan>
      <tspan x="14" dy="18">  promises by terror gangs</tspan>
    </text>
    <rect x="14" y="242" width="157" height="24" rx="4" fill="#0f172a"/>
    <text x="92" y="258" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Economic Frustration</text>
  </g>

  <!-- Gear 3: Social Isolation -->
  <g transform="translate(450, 85)">
    <rect width="185" height="290" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="185" height="38" rx="8" fill="#7e22ce"/>
    <text x="92" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. SOCIAL ISOLATION</text>
    
    <circle cx="92" cy="72" r="22" fill="#581c87" stroke="#a855f7" stroke-width="1.5"/>
    <text x="92" y="79" fill="#c084fc" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">👤</text>
    
    <text x="92" y="118" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12.5" font-weight="600" text-anchor="middle">Identity &amp; Alienation</text>
    <text x="14" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="14" dy="0">• Lack of family support</tspan>
      <tspan x="14" dy="20">• Peer rejection &amp; bullying</tspan>
      <tspan x="14" dy="20">• Identity crisis in youth</tspan>
      <tspan x="14" dy="20">• Craving for belonging</tspan>
      <tspan x="14" dy="18">  and false 'brotherhood'</tspan>
      <tspan x="14" dy="20">• Emotional vulnerability</tspan>
    </text>
    <rect x="14" y="242" width="157" height="24" rx="4" fill="#0f172a"/>
    <text x="92" y="258" fill="#c084fc" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Psychological Trap</text>
  </g>

  <!-- Gear 4: Online Recruitment -->
  <g transform="translate(655, 85)">
    <rect width="185" height="290" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="185" height="38" rx="8" fill="#0284c7"/>
    <text x="92" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">4. DIGITAL GROOMING</text>
    
    <circle cx="92" cy="72" r="22" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="92" y="79" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🌐</text>
    
    <text x="92" y="118" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12.5" font-weight="600" text-anchor="middle">Online Propaganda</text>
    <text x="14" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="14" dy="0">• Manipulation on social apps</tspan>
      <tspan x="14" dy="20">• Gaming chatrooms &amp; bots</tspan>
      <tspan x="14" dy="20">• Highly emotional videos</tspan>
      <tspan x="14" dy="20">• Secretive echo chambers</tspan>
      <tspan x="14" dy="20">• Targeting teens in private</tspan>
    </text>
    <rect x="14" y="242" width="157" height="24" rx="4" fill="#0f172a"/>
    <text x="92" y="258" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Recruitment Mechanism</text>
  </g>

  <!-- Footer -->
  <rect x="45" y="395" width="795" height="30" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="440" y="415" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Jamming ANY of these four gears stops the radicalization cycle completely.</text>
</svg>"""


def get_svg_lesson_4():
    """Lesson 6.6.4: The Impact of Peace vs The Devastation of Extremism"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg174" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg174)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE IMPACT OF PEACE (AMAN) VS. DEVASTATION OF TERRORISM</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">How Peace Fosters National Flourishing While Violent Extremism Shatters Human Wellbeing</text>

  <!-- Left: Flourishing Under Peace -->
  <g transform="translate(45, 80)">
    <rect width="375" height="300" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect width="375" height="42" rx="10" fill="#065f46"/>
    <text x="187" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">SOCIETY UNDER PEACE &amp; SECURITY (AMAN)</text>
    
    <text x="24" y="70" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Fulfilling All 5 Objectives of Shariah (Maqasid)</text>
    <text x="24" y="96" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11.5">
      <tspan x="24" dy="0">✓ Protection of Life: Children attend school safely</tspan>
      <tspan x="24" dy="24">✓ Economic Flourishing: Thriving markets, tourism &amp; jobs</tspan>
      <tspan x="24" dy="24">✓ Social Trust: Warm interfaith &amp; inter-ethnic unity</tspan>
      <tspan x="24" dy="24">✓ Mental Peace: Freedom from trauma and fear</tspan>
      <tspan x="24" dy="24">✓ Freedom of Faith: Mosques and churches worship peacefully</tspan>
      <tspan x="24" dy="24">✓ National budget invested in schools &amp; healthcare</tspan>
    </text>
    
    <rect x="20" y="250" width="335" height="36" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
    <text x="187" y="273" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">True Islamic Ideal: A Peaceful &amp; Prosperous Kenya</text>
  </g>

  <!-- Right: Devastation Under Terrorism -->
  <g transform="translate(460, 80)">
    <rect width="375" height="300" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <rect width="375" height="42" rx="10" fill="#991b1b"/>
    <text x="187" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">DEVASTATION OF VIOLENT EXTREMISM</text>
    
    <text x="24" y="70" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Destruction of All 5 Objectives of Shariah</text>
    <text x="24" y="96" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11.5">
      <tspan x="24" dy="0">❌ Loss of Life: Innocent fathers, mothers &amp; children slain</tspan>
      <tspan x="24" dy="24">❌ Economic Ruin: Burned markets, closed hotels &amp; poverty</tspan>
      <tspan x="24" dy="24">❌ Social Fracture: Suspicion &amp; prejudice across tribes</tspan>
      <tspan x="24" dy="24">❌ Psychological Scars: PTSD, grief &amp; lingering terror</tspan>
      <tspan x="24" dy="24">❌ Reputational Harm: Peaceful Muslims face Islamophobia</tspan>
      <tspan x="24" dy="24">❌ Billions wasted on emergency response &amp; policing</tspan>
    </text>
    
    <rect x="20" y="250" width="335" height="36" rx="6" fill="#450a0a" stroke="#ef4444" stroke-width="1"/>
    <text x="187" y="273" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Devastating Ruin Condemned by Quran &amp; Sunnah</text>
  </g>

  <!-- Footer -->
  <rect x="45" y="394" width="790" height="30" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="440" y="414" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">"...Whoever kills a soul... it is as if he had slain mankind entirely." — Surah Al-Ma'idah 5:32</text>
</svg>"""


def get_svg_lesson_5():
    """Lesson 6.6.5: The Community Peace Dike (Multi-Tier Shield)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg175" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg175)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE COMMUNITY PEACE DIKE: 4 LAYERS OF DEFENSE</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">A Comprehensive Actionable Strategy for Students, Families, Schools &amp; Society</text>

  <!-- Layer 4: Top - Safe Reporting Pathways -->
  <g transform="translate(100, 85)">
    <rect width="680" height="58" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="680" height="24" rx="8" fill="#0284c7"/>
    <text x="340" y="17" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">LAYER 4: SAFE REPORTING &amp; EARLY INTERVENTION</text>
    <text x="340" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Noticing warning signs early • Confidential reporting to teachers &amp; counselors • Saving friends from ruin</text>
  </g>

  <!-- Layer 3: Interfaith & Social Collaboration -->
  <g transform="translate(100, 155)">
    <rect width="680" height="58" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="680" height="24" rx="8" fill="#059669"/>
    <text x="340" y="17" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">LAYER 3: INTERFAITH DIALOGUE &amp; JOINT COMMUNITY SERVICE</text>
    <text x="340" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Clean-up days with Christian peers • Tree planting • Shattering stereotypes through joint action</text>
  </g>

  <!-- Layer 2: Emotional & Peer Inclusivity -->
  <g transform="translate(100, 225)">
    <rect width="680" height="58" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="680" height="24" rx="8" fill="#7e22ce"/>
    <text x="340" y="17" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">LAYER 2: SOCIAL INCLUSIVITY &amp; MENTORSHIP</text>
    <text x="340" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Supporting lonely and struggling classmates • Zero tolerance for bullying • Cultivating warm school brotherhood</text>
  </g>

  <!-- Layer 1: Foundation - Authentic Religious Education -->
  <g transform="translate(100, 295)">
    <rect width="680" height="70" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
    <rect width="680" height="26" rx="8" fill="#b45309"/>
    <text x="340" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">LAYER 1 (FOUNDATION): AUTHENTIC RELIGIOUS EDUCATION</text>
    <text x="340" y="46" fill="#fef08a" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Learning from certified IRE teachers, accredited Masajid &amp; classical scholarship</text>
    <text x="340" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5" text-anchor="middle">Mastering context (Asbab al-Nuzul) • Total immunity against online brainwashing</text>
  </g>

  <!-- Bottom Banner -->
  <rect x="100" y="385" width="680" height="30" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="440" y="405" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600" text-anchor="middle">"Hold firmly to the rope of Allah all together and do not become divided." — Surah Ali 'Imran 3:103</text>
</svg>"""


def get_svg_lesson_6():
    """Lesson 6.6.6: Master Peace Architecture: Islam as a Beacon of Security"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg176" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="shieldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="50%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg176)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE SHIELD OF HARMONIOUS COEXISTENCE &amp; NATIONAL UNITY</text>
  <text x="440" y="52" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Unit Synthesis: How Authentic Islamic Values Build Peace, Cohesion &amp; National Development in Kenya</text>

  <!-- Central Shield Design -->
  <g transform="translate(340, 75)">
    <!-- Outer Shield -->
    <path d="M100,10 L190,40 L190,160 C190,220 100,270 100,270 C100,270 10,220 10,160 L10,40 Z" fill="url(#shieldGrad)" stroke="#38bdf8" stroke-width="2.5"/>
    <!-- Inner Core -->
    <path d="M100,25 L175,50 L175,150 C175,200 100,245 100,245 C100,245 25,200 25,150 L25,50 Z" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="100" y="95" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">WASATIYYAH</text>
    <text x="100" y="115" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">The Middle Path</text>
    <circle cx="100" cy="155" r="22" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
    <text x="100" y="163" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">PEACE</text>
    <text x="100" y="200" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">KENYAN UNITY</text>
  </g>

  <!-- Left Supporting Pillars -->
  <g transform="translate(50, 95)">
    <!-- Pillar 1 -->
    <rect width="260" height="110" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="130" y="24" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. GREATER JIHAD (INNER STRIVING)</text>
    <text x="15" y="48" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
      <tspan x="15" dy="0">• Striving against personal sins &amp; laziness</tspan>
      <tspan x="15" dy="18">• Excelling in academic studies &amp; skills</tspan>
      <tspan x="15" dy="18">• Building honesty, humility &amp; kindness</tspan>
    </text>

    <!-- Pillar 2 -->
    <g transform="translate(0, 130)">
      <rect width="260" height="110" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="130" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. SACRED VALUE OF HUMAN LIFE</text>
      <text x="15" y="48" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
        <tspan x="15" dy="0">• Killing an innocent is like slaying all mankind</tspan>
        <tspan x="15" dy="18">• Absolute protection of non-combatants</tspan>
        <tspan x="15" dy="18">• Defending communal safety &amp; harmony</tspan>
      </text>
    </g>
  </g>

  <!-- Right Supporting Pillars -->
  <g transform="translate(570, 95)">
    <!-- Pillar 3 -->
    <rect width="260" height="110" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <text x="130" y="24" fill="#c084fc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. INTERFAITH BROTHERHOOD</text>
    <text x="15" y="48" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
      <tspan x="15" dy="0">• Celebrating divine diversity (Quran 49:13)</tspan>
      <tspan x="15" dy="18">• Joint civic service with Christian peers</tspan>
      <tspan x="15" dy="18">• Defeating stereotypes through cooperation</tspan>
    </text>

    <!-- Pillar 4 -->
    <g transform="translate(0, 130)">
      <rect width="260" height="110" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
      <text x="130" y="24" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">4. PROACTIVE CITIZENSHIP</text>
      <text x="15" y="48" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
        <tspan x="15" dy="0">• Tabayyun: Verifying all online information</tspan>
        <tspan x="15" dy="18">• Confidential reporting of extremist threats</tspan>
        <tspan x="15" dy="18">• Patriotism: Serving and protecting Kenya</tspan>
      </text>
    </g>
  </g>

  <!-- Deflected Threat Labels bouncing off shield -->
  <g transform="translate(280, 80)">
    <text x="0" y="0" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="700">✕ Extremism</text>
  </g>
  <g transform="translate(530, 80)">
    <text x="0" y="0" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="700">✕ Terrorism</text>
  </g>

  <!-- Footer Banner -->
  <rect x="50" y="388" width="780" height="30" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="440" y="408" fill="#34d399" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600" text-anchor="middle">"O mankind, We made you peoples and tribes that you may know one another." — Surah Al-Hujurat 49:13</text>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# LESSON DATA SPECIFICATION (6 Lessons, 7 Cards Each)
# ─────────────────────────────────────────────────────────────────────────────

TOPIC_17_LESSONS = [
    {
        "unit_order": 1,
        "lesson_title": "Jihad: correct interpretation",
        "inquiry": "What is the true meaning of Jihad, and how do we distinguish it from violence and extremism?",
        "hook": "Imagine a dedicated young athlete who wakes up at 5:00 AM every single morning to train in freezing rain, refusing junk food, and persevering through exhaustion to qualify for the national athletics championship. The word we use for this athlete's hard work, focus, and struggle against laziness is 'striving.' In Arabic, the word for this constant, positive struggle to improve oneself and do good is Jihad. In this lesson, we will rescue this sublime concept from modern distortions and understand its authentic, peaceful definition in Islam.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Sultan_Hassan_Mosque_Courtyard.jpg/800px-Sultan_Hassan_Mosque_Courtyard.jpg",
        "image_title": "Sanctuary of Spiritual Striving",
        "image_caption": "Historic mosque courtyard symbolizing inner spiritual peace, intellectual discipline, and the pursuit of righteousness.",
        "concept_name": "Jihad: The Sacred Striving for Moral and Social Good",
        "concept_explanation": "Jihad literally translates to 'exerting utmost effort' or 'striving' in the path of Allah (S.W.T.) to establish goodness, resist evil, and purify one's soul. Islamic jurisprudence establishes two distinct dimensions: Greater Jihad (Jihad al-Akbar), which is the primary, daily inner struggle against sinful desires and laziness; and Lesser Jihad (Jihad al-Asghar), which refers to strictly defensive military operations declared solely by a legitimate state authority with absolute prohibitions against harming civilians.",
        "scripture_quran": "Fight in the way of Allah those who fight you, but do not transgress. Indeed, Allah does not like transgressors.",
        "scripture_quran_ref": "Surah Al-Baqarah 2:190",
        "scripture_hadith": "Do not kill women, children, or the elderly, and do not damage crops or trees.",
        "scripture_hadith_ref": "Sunan Abu Dawood 2614",
        "deep_explanation": "The authentic Islamic doctrine of Jihad is governed by three rigorous legal boundaries:\n1. Self-Purification as Supreme Priority: When returning from a military expedition, the Prophet (PBUH) stated: 'We have returned from the lesser struggle to the greater struggle'—clarifying that mastering one's ego, maintaining honesty, and serving family ranks higher than physical conflict.\n2. Strict Defensive Prerequisite: Armed combat is legitimate only to defend innocent lives, religious freedom, or sovereignty against active aggression. It can never be declared by vigilante groups or criminal militias; only an established sovereign government holds legitimate authority.\n3. Inviolability of Civilians: Even during lawful defensive combat, targeting non-combatants—such as women, children, teachers, monks, farmers—and destroying infrastructure or environment is strictly forbidden (Haram).",
        "diagram_title": "True Jihad vs Violent Distortion Matrix",
        "svg_func": get_svg_lesson_1,
        "table_title": "Authentic Islamic Jihad vs Extremist Violent Distortion",
        "table_headers": ["Criteria", "Authentic Islamic Jihad (Shariah)", "Extremist Violent Distortion (Haram)"],
        "table_rows": [
            ["Primary Focus", "Inner character purification (Greater Jihad), education, and charity", "Senseless slaughter, extortion, and public terror"],
            ["Legal Authority", "Legitimate sovereign government (state) only", "Self-appointed vigilante gangs and outlaw militias"],
            ["Target Restrictions", "Strictly defensive combatants; non-combatants totally protected", "Deliberately slaughters civilians, women, students, and elders"],
            ["Infrastructure", "Prohibits damaging trees, crops, places of worship, or water wells", "Bombs schools, markets, mosques, and public transit"]
        ],
        "scenario": "During an online discussion on social media, Yusuf encounters a video where a masked extremist claims: 'We are launching a Jihad, so we must attack schools and public markets to force people to submit!' Yusuf's classmate Amina intervenes: 'Yusuf, this is a dangerous deception. Authentic Jihad, as taught by the Prophet (PBUH), is about moral striving and defense of the vulnerable. He strictly forbade harming civilians, women, or children. Attacking a school is not Jihad—it is a heinous crime that violates the core teachings of Islam.' Yusuf recognizes Amina's evidence-based clarity and reports the malicious content.",
        "real_world": "Embody the 'Greater Jihad' in your daily life as a Grade 9 student. Your Jihad is to rise on time for Fajr prayers, dedicate focused hours to mastering challenging academic subjects, respect your parents without resentment, and treat peers with empathy when tempted by anger. This persistent striving for moral excellence is the most beloved Jihad in the sight of Allah.",
        "reflection": "How does resisting negative peer pressure qualify as a form of Greater Jihad? Why does Islam restrict the authority to declare defensive struggle exclusively to sovereign governments?",
        "misconception": "Misconception: Thinking that Jihad translates to 'holy war' or unprovoked aggression against non-Muslims. The Arabic term for 'holy war' (Harb Muqaddasah) does not exist anywhere in the Qur'an or Sunnah; Jihad means 'striving,' and initiating unprovoked violence is strictly forbidden.",
        "yt_id": "8G8_9V1q5cQ",
        "yt_title": "Understanding the True Meaning of Jihad in Islam",
        "yt_desc": "Clarification of Greater Jihad vs Lesser Jihad, defensive ethics, and the prohibition of terrorism.",
        "mcq": {
            "question": "According to authentic Islamic jurisprudence, what did the Prophet Muhammad (PBUH) designate as the 'Greater Jihad' (Jihad al-Akbar)?",
            "options": [
                "A. Invading foreign territories to conquer agricultural lands.",
                "B. The persistent internal spiritual struggle to resist sins, laziness, and purify the soul.",
                "C. Taking the law into one's own hands to punish social wrongdoers.",
                "D. Accumulating political authority and material wealth by any means."
            ],
            "answer": "B",
            "explanation": "The Prophet (PBUH) taught that the greatest Jihad is the inner moral and spiritual struggle of the believer to conquer base impulses, resist temptation, and consistently obey Allah."
        },
        "summary_content": "Jihad fundamentally signifies 'striving' in righteousness. The highest form is the internal struggle against ego and sin (Greater Jihad). Armed combat (Lesser Jihad) is strictly defensive, subject to state authority, and bound by inviolable protections for civilians.",
        "key_points": [
            "Jihad means 'striving' to do good, resist evil, and build a righteous life.",
            "Greater Jihad is the inner spiritual struggle against selfishness, anger, and sin.",
            "Lesser Jihad is strictly defensive, must be declared by a state, and bans civilian harm.",
            "Violent terrorism directly violates every command of Surah Al-Baqarah (2:190) and the Sunnah."
        ],
        "exit_ticket": "Write down one daily action that counts as a 'Greater Jihad' in your life as a student."
    },
    {
        "unit_order": 2,
        "lesson_title": "Terrorism and extremism: meanings",
        "inquiry": "What are the definitions of terrorism and extremism, and why does Islam categorically condemn them?",
        "hook": "Imagine a gardener who becomes so fanatically obsessed with a single rosebush that they chop down all the surrounding fruit trees, poison the soil, and set fire to neighboring farms just to keep their rose untouched. The entire garden would be destroyed, and the gardener recognized as dangerous and unstable. This is what extremism does to religion and society. In this lesson, we will define terrorism and extremism, demonstrating why they are complete departures from the moderate, balanced path of Islam.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Scales_of_balance.svg/800px-Scales_of_balance.svg.png",
        "image_title": "The Balance Scale of Wasatiyyah",
        "image_caption": "The balanced scale representing Wasatiyyah (the middle path), rejecting both religious neglect and fanatical extremism.",
        "concept_name": "Wasatiyyah: The Rejection of Ghuluww (Extremism) and Terrorism",
        "concept_explanation": "Extremism (Ghuluww/Radicalism) is an uncompromising, fanatical deviation that rejects the moderate middle path of Islam (Wasatiyyah), leading to intolerance, hatred, and the unlawful declaration of other Muslims as apostates (Takfir). Terrorism is the criminal use of violence, fear, and intimidation against civilians for political or ideological ends. Islam categorically condemns both as grave sins that assault the sanctity of human life.",
        "scripture_quran": "...Whoever kills a soul unless for a soul or for corruption [done] in the land – it is as if he had slain mankind entirely. And whoever saves one – it is as if he had saved mankind entirely.",
        "scripture_quran_ref": "Surah Al-Ma'idah 5:32",
        "scripture_hadith": "A believer remains within the bounds of his religion as long as he does not shed blood unlawfully.",
        "scripture_hadith_ref": "Sahih al-Bukhari 6862",
        "deep_explanation": "Islam dismantles the foundations of terrorism through three theological pillars:\n1. Absolute Sanctity of Life (Hifz al-Nafs): Human life is sacred. In Surah Al-Ma'idah (5:32), the Qur'an compares taking a single innocent life to slaying all of humanity, making terrorism a cosmic crime against Allah and society.\n2. Wasatiyyah (The Balanced Middle Way): The Qur'an designates the Muslim Ummah as 'Ummatan Wasatan' (a middle, balanced community). The Prophet (PBUH) explicitly warned: 'Beware of extremism in religion, for those before you were destroyed because of extremism.'\n3. Prohibition of Takfir: Extremists justify their crimes by declaring those who disagree with them to be disbelievers (Takfir). The Prophet (PBUH) severely outlawed this, warning that falsely calling a fellow believer a kafir rebounds upon the accuser.",
        "diagram_title": "The Wasatiyyah (Moderation) Balance Scale",
        "svg_func": get_svg_lesson_2,
        "table_title": "The Spectrum of Practice: Laxity vs Wasatiyyah vs Extremism",
        "table_headers": ["Trait", "Tafrit (Laxity / Neglect)", "Wasatiyyah (Islamic Moderation)", "Ghuluww (Extremism / Radicalism)"],
        "table_rows": [
            ["Theological Stance", "Compromises moral principles; ignores religious duties", "Balanced fidelity to Qur'an & Sunnah with mercy", "Rigid, harsh, and literalist intolerance"],
            ["View of Others", "Indifferent to community guidance", "Respects diversity, seeks dialogue, and shows compassion", "Excommunicates dissenters (Takfir); preaches hatred"],
            ["Method of Influence", "Passive inaction", "Constructive dialogue, exemplary character & kindness", "Coercion, threats, psychological terror & violence"],
            ["Prophetic Rulings", "Warned against negligence", "Paved as the Straight Path (Sirat al-Mustaqim)", "Condemned: 'The extremists are destroyed' (Sahih Muslim)"]
        ],
        "scenario": "A radical faction releases an online manifesto claiming: 'We have detonated an explosive in a crowded marketplace to punish those who do not adopt our ideology; this is our duty!' Hussein's grandmother is heartbroken by the news. Hussein comforts her: 'Grandmother, rest assured that these criminals have zero connection to authentic Islam. The Qur'an states in Surah Al-Ma'idah (5:32) that killing one innocent person is like slaying all of mankind. Their terrorism directly violates the Prophet's teachings of mercy. They are outlaws, not martyrs.'",
        "real_world": "Build your personal shield of Wasatiyyah by actively practicing tolerance in daily interactions. If you witness a classmate insulting another student's ethnic background, tribe, or religious denomination, speak out calmly and firmly: 'We are all fellow Kenyans, and our faith commands us to be balanced, respectful, and merciful.' Defending mutual respect stops the seeds of extremism from taking root.",
        "reflection": "Why does taking innocent human lives in markets or schools completely destroy any claim of practicing a religion of peace? How does cultivating emotional balance protect us from radical anger?",
        "misconception": "Misconception: Believing that extremists are simply 'overly religious.' Extremism is not an excess of religion; it is a profound deviation and distortion of religion rooted in ignorance and pride, explicitly condemned by the Prophet (PBUH).",
        "yt_id": "4j1a9X1q7ZY",
        "yt_title": "Islam Against Extremism: The Concept of Wasatiyyah",
        "yt_desc": "Scholarly exposition on moderation, the prohibition of terrorism, and the Quranic mandate on the sanctity of life.",
        "mcq": {
            "question": "In Surah Al-Ma'idah (5:32), how does the Holy Qur'an describe the gravity of taking a single innocent human life?",
            "options": [
                "A. As a negligible error that requires no legal consequence.",
                "B. As an atrocity equivalent to slaying the entire human race.",
                "C. As permissible whenever pursuing a political objective.",
                "D. As acceptable if the victim belongs to a different tribe."
            ],
            "answer": "B",
            "explanation": "Surah Al-Ma'idah 5:32 equates the murder of a single innocent person to killing all of humanity, underscoring the absolute, inviolable sanctity of human life in Islamic law."
        },
        "summary_content": "Extremism is an intolerant deviation from Islam's moderate middle path (Wasatiyyah). Terrorism involves unlawful violence against civilians and is categorically condemned by Surah Al-Ma'idah (5:32), which protects the sanctity of human life above all else.",
        "key_points": [
            "Extremism (Ghuluww) represents a destructive deviation from the balanced middle way.",
            "Terrorism utilizes fear and violence against civilians, constituting a grave crime in Islam.",
            "Taking an innocent life is equivalent in the Qur'an to slaughtering all mankind.",
            "The Prophet (PBUH) repeatedly warned: 'Beware of extremism in religion, for it destroyed nations before you.'"
        ],
        "exit_ticket": "Define 'Wasatiyyah' in your own words and state why it is essential for social cohesion in Kenya."
    },
    {
        "unit_order": 3,
        "lesson_title": "Causes",
        "inquiry": "What are the root causes and risk factors that lead individuals toward radicalization and extremist behavior?",
        "hook": "Imagine a dry, decaying tree standing in an untended forest. When lightning strikes, the dead branches instantly erupt into flames, threatening to incinerate the whole forest. But if the forest is green, fertile, and well-watered, a lightning strike fizzles out harmlessly. Radicalization functions like that forest fire. Extremist recruiters deliberately search for individuals who are spiritually, socially, and emotionally vulnerable so they can ignite hatred in their hearts. In this lesson, we study the root drivers of radicalization to safeguard our youth and communities.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Gears_animation.gif/800px-Gears_animation.gif",
        "image_title": "The Interlocking Gears of Radicalization",
        "image_caption": "Visual model representing the complex socioeconomic, educational, and digital factors that drive individuals toward extremist ideologies.",
        "concept_name": "Radicalization Dynamics: The Four Vulnerability Drivers",
        "concept_explanation": "Radicalization is the social, educational, and psychological process through which an individual adopts extremist beliefs justifying violence. It does not stem from religious devotion, but rather from a toxic combination of four vulnerability drivers: religious ignorance (superficial knowledge), socioeconomic hopelessness (poverty and unemployment), social isolation (alienation and identity crises), and predatory digital manipulation.",
        "scripture_quran": "O you who have believed, be persistently standing firm in justice, witnesses for Allah, even if it be against yourselves or parents and relatives...",
        "scripture_quran_ref": "Surah An-Nisa 4:135",
        "scripture_hadith": "Beware! The people who went to extremes in religion were destroyed.",
        "scripture_hadith_ref": "Sahih Muslim 2670",
        "deep_explanation": "Scholars and security analysts categorize radicalization into four interacting dimensions:\n1. Religious Illiteracy & Scriptural Distortion: Individuals lacking authentic training in Islamic jurisprudence fall prey to recruiters who weaponize verses stripped of historical context (Asbab al-Nuzul) and legal qualifications.\n2. Socioeconomic Grievances & Marginalization: Chronic youth unemployment, poverty, and governance grievances generate despair, which criminal recruiters exploit by offering false promises of stipends, respect, or heroism.\n3. Identity Crisis & Social Disconnection: Youth suffering from alienation, family dysfunction, or school bullying seek belonging in extremist echo chambers that masquerade as warm, protective brotherhoods.\n4. Algorithmic Digital Manipulation: Violent networks leverage gaming forums, social media algorithms, and encrypted messaging apps to groom adolescents in private, away from parental supervision.",
        "diagram_title": "Anatomy of Radicalization: The Four Vulnerability Gears",
        "svg_func": get_svg_lesson_3,
        "table_title": "Deconstructing Radicalization Drivers: Vulnerabilities vs Protective Solutions",
        "table_headers": ["Vulnerability Driver", "Extremist Exploitation Method", "Community & School Protective Countermeasure"],
        "table_rows": [
            ["Religious Ignorance", "Cherry-picks verses out of context; promotes Takfir", "Authentic IRE curriculum; accredited scholars & critical thinking"],
            ["Socioeconomic Despair", "Promises financial stipends, marriage gifts & status", "Vocational training, youth entrepreneurship & community empowerment"],
            ["Social Alienation", "Offers deceptive 'brotherhood' and heroic belonging", "Supportive school clubs, mentorship programs & mental health counseling"],
            ["Digital Grooming", "Uses private chats, gaming platforms & propaganda videos", "Digital literacy, parental supervision & safe reporting protocols"]
        ],
        "scenario": "Zainab has a 20-year-old cousin, Musa, who graduated from college but remains unemployed despite sending dozens of applications. Frustrated and lonely, Musa spends entire nights online in anonymous chatrooms where a radical recruiter tells him: 'The government and society hate you; join our cause to establish true justice and earn honor!' Zainab notices Musa becoming secretive, angry, and hostile toward non-Muslims. She immediately alerts her father, who brings a respected IRE teacher to have a gentle, source-grounded conversation with Musa. The teacher exposes the recruiter's theological lies, and the family assists Musa in enrolling in an entrepreneurship incubation project. Musa breaks free from the trap and thanks his family for saving his future.",
        "real_world": "Safeguard your digital spaces. If you encounter strangers on social media, video game platforms, or chat groups who preach hatred against specific ethnic or religious groups, glorify violence, or ask you to keep secrets from your parents, do not engage. Block the user immediately, preserve screenshots, and inform a trusted teacher, parent, or school counselor.",
        "reflection": "Why does a thorough foundation in authentic Islamic sciences provide the strongest immunity against extremist recruiters? How can simple acts of welcoming a lonely student protect them from falling into radical networks?",
        "misconception": "Misconception: Claiming that religion itself causes terrorism. Global empirical research confirms that terrorists typically possess little or no authentic theological training; their radicalization is driven by psychological, political, and social vulnerabilities cloaked in religious rhetoric.",
        "yt_id": "7H1d5-Xm3kY",
        "yt_title": "Deconstructing the Root Causes of Youth Radicalization",
        "yt_desc": "Analysis of social isolation, online propaganda, religious illiteracy, and methods to protect vulnerable youth.",
        "mcq": {
            "question": "Which of the following is recognized by educators and security analysts as a primary driver of youth radicalization, rather than religious devotion?",
            "options": [
                "A. Comprehensive mastery of classical Islamic jurisprudence and ethics.",
                "B. Religious illiteracy combined with socioeconomic despair, social isolation, and online grooming.",
                "C. Active participation in interfaith dialogue and community development.",
                "D. Having stable emotional support from family and teachers."
            ],
            "answer": "B",
            "explanation": "Radicalization preys upon religious ignorance, which enables recruiters to distort scripture, combined with socioeconomic despair, loneliness, and digital grooming."
        },
        "summary_content": "Radicalization is a complex social and psychological process driven by religious ignorance, poverty, alienation, and digital propaganda. Authentic Islamic education and proactive communal support dismantle these vulnerability drivers before recruiters can exploit them.",
        "key_points": [
            "Radicalization thrives on religious illiteracy and out-of-context scriptural manipulation.",
            "Poverty, unemployment, and feelings of marginalization are exploited by recruiter networks.",
            "Lonely and isolated adolescents are primary targets for online grooming.",
            "Jamming any of the four vulnerability gears successfully halts the radicalization cycle."
        ],
        "exit_ticket": "Identify two digital warning signs that indicate an online group is attempting to manipulate teenagers into extremist thinking."
    },
    {
        "unit_order": 4,
        "lesson_title": "Effects",
        "inquiry": "What are the devastating consequences of terrorism and extremism on individuals, families, and our Kenyan nation?",
        "hook": "Imagine a bustling shopping arcade in downtown Nairobi where mothers are buying school uniforms, young entrepreneurs are selling electronics, and children are enjoying ice cream. In a split second, a horrific explosion detonates. In an instant, beloved family members are killed, livelihoods are incinerated, and survivors are left with irreversible physical and psychological scars. The laughter is replaced by screams of anguish and terror. In this lesson, we confront the real-world devastation caused by violent extremism, reinforcing why safeguarding peace is our foremost civic and religious obligation.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Nairobi_city_skyline.jpg/800px-Nairobi_city_skyline.jpg",
        "image_title": "Kenya's Vibrant National Fabric",
        "image_caption": "Nairobi city skyline symbolizing Kenyan progress, economic vibrancy, and the shared national prosperity protected by enduring peace.",
        "concept_name": "The Multi-Tier Catastrophe of Violent Extremism",
        "concept_explanation": "Violent extremism inflicts catastrophic damage that systematically violates all five higher objectives of Islamic law (Maqasid al-Shariah): destroying innocent human life (Hifz al-Nafs), devastating infrastructure and wealth (Hifz al-Mal), shattering mental health through trauma (Hifz al-'Aql), tearing apart social cohesion (Hifz al-Din), and subjecting peaceful Muslims to unfair stigma and Islamophobia.",
        "scripture_quran": "...And do not throw [yourselves] with your own hands into destruction [by transgressing]. And do good; indeed, Allah loves the doers of good.",
        "scripture_quran_ref": "Surah Al-Baqarah 2:195",
        "scripture_hadith": "There shall be no harming nor reciprocating of harm.",
        "scripture_hadith_ref": "Sunan Ibn Majah 2341",
        "deep_explanation": "The fallout of terrorism operates across four destructive vectors:\n1. Irreplaceable Human Carnage: Attacks rob communities of teachers, doctors, parents, and students, leaving thousands of traumatized orphans and fractured households.\n2. National Economic Devastation: Terror attacks destroy hotels, transport hubs, and markets, costing Kenya billions in lost foreign investment and tourism revenues, directly worsening youth unemployment.\n3. Psychological Trauma & Lingering Terror: Survivors and first responders experience post-traumatic stress disorder (PTSD), chronic anxiety, and debilitating grief.\n4. Communal Polarization & Islamophobia: Extremist atrocities breed inter-ethnic suspicion and anti-Muslim prejudice, undermining decades of harmonious coexistence between Christians and Muslims in Kenya.",
        "diagram_title": "The Impact of Peace vs The Devastation of Extremism",
        "svg_func": get_svg_lesson_4,
        "table_title": "Socio-Economic Comparison: Peace (Aman) vs Violent Extremism (Fasad)",
        "table_headers": ["Dimension", "Kenya Under Enduring Peace (Aman)", "Kenya Under Threat of Extremism (Fasad)"],
        "table_rows": [
            ["Education", "Schools and universities operate safely; learning thrives", "Campuses face closures, exam disruption, and perpetual fear"],
            ["Economy & Jobs", "Vibrant trade, foreign tourism, infrastructure development", "Business collapse, flight of capital, and rising poverty"],
            ["Social Relations", "Mutual respect and interfaith collaboration between faiths", "Suspicion, stereotyping, ethnic tension, and Islamophobia"],
            ["National Budget", "Billions invested in hospitals, modern roads, and bursaries", "Massive diversion of public funds into emergency defense operations"]
        ],
        "scenario": "A community library built through local fundraising to support Grade 9 revision is bombed by an extremist militia. The attack claims the life of the volunteer librarian and destroys thousands of textbooks. Schools across the sub-county close for a month due to security threats. Yusuf and his classmates are unable to study, while local market stalls lose all customers due to curfew restrictions. Yusuf laments: 'The terrorists claimed to fight for justice, yet they murdered a beloved elder, burned our school books, and destroyed our parents' livelihood. Their actions are pure corruption (Fasad) cursed by Allah.'",
        "real_world": "Actively strengthen social cohesion in your school. Deliberately form study groups with peers from different religious and ethnic communities. By working together on science projects, playing sports, and celebrating national events, you demonstrate that Kenyan youth stand united against hate. Peaceful solidarity is the most potent refutation of extremist agendas.",
        "reflection": "How does the destruction of educational institutions by extremists directly violate the prophetic command to seek knowledge? Why is it both unjust and inaccurate to hold peaceful Muslim citizens responsible for the crimes of rogue terror gangs?",
        "misconception": "Misconception: Believing that extremist violence only impacts non-Muslims. In reality, globally and regionally, the vast majority of victims murdered by extremist terror organizations are peaceful, practicing Muslims who reject their violent ideology.",
        "yt_id": "r9T5_Y7k1Wc",
        "yt_title": "The Human and Economic Cost of Terrorism in Kenya",
        "yt_desc": "Documentary exploring the devastation of extremist attacks on Kenyan families, national cohesion, and economic growth.",
        "mcq": {
            "question": "What is a primary long-term social damage inflicted by terrorist attacks on a diverse country like Kenya?",
            "options": [
                "A. It promotes mutual affection and rapid interfaith integration.",
                "B. It shatters social cohesion by creating fear, panic, and unjust suspicion between peaceful religious groups.",
                "C. It channels vast new investments into rural public healthcare.",
                "D. It eliminates youth unemployment across the nation."
            ],
            "answer": "B",
            "explanation": "Terrorism deliberately tears the social fabric of society, creating mutual suspicion, ethnic polarization, and prejudice that threatens national unity."
        },
        "summary_content": "Violent extremism violates every principle of Maqasid al-Shariah, causing loss of innocent life, economic collapse, deep psychological trauma, and destructive interfaith suspicion. Safeguarding national peace is both a civic necessity and a sacred religious duty.",
        "key_points": [
            "Terrorism assaults all five universal objectives of Shariah (Life, Mind, Wealth, Faith, Dignity).",
            "The devastation includes loss of innocent lives, destroyed infrastructure, and lingering PTSD.",
            "Peaceful Muslims often suffer dual harm: direct violence and resulting Islamophobic suspicion.",
            "Protecting Kenya's peace and interfaith harmony is a paramount religious and patriotic obligation."
        ],
        "exit_ticket": "List three ways an act of violent extremism in a community directly disrupts the lives and education of Junior School students."
    },
    {
        "unit_order": 5,
        "lesson_title": "Prevention and response",
        "inquiry": "How can youth, families, and schools work together to prevent radicalization and build a peaceful society?",
        "hook": "Imagine you spot a tiny water leak dripping from the roof of your school computer lab. If you ignore it, the water will saturate the ceiling boards, rot the beams, and eventually cause the entire roof to collapse onto the expensive equipment. But if you report it immediately, a technician can seal the pipe in ten minutes, preserving the lab. Preventing extremism follows the identical principle: early detection, supportive intervention, and communal teamwork fix vulnerabilities before destructive radicalization takes root. Let's master our roles in this mission.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Interfaith_dialogue.jpg/800px-Interfaith_dialogue.jpg",
        "image_title": "Interfaith Youth Collaboration",
        "image_caption": "Diverse youth working together on community development projects, demonstrating the power of unity, dialogue, and mutual respect.",
        "concept_name": "The Four-Tier Community Peace Dike",
        "concept_explanation": "Preventing radicalization is a shared societal duty grounded in the Islamic principle of mutual counsel (Nasihah) and proactive social welfare. The defense strategy relies upon four coordinated tiers: authentic religious literacy from certified scholars, peer inclusivity and mental health support, interfaith youth collaboration, and confidential reporting protocols to protect vulnerable individuals.",
        "scripture_quran": "And hold firmly to the rope of Allah all together and do not become divided. And remember the favor of Allah upon you...",
        "scripture_quran_ref": "Surah Ali 'Imran 3:103",
        "scripture_hadith": "All mankind is from Adam and Eve. An Arab has no superiority over a non-Arab, nor does a non-Arab have superiority over an Arab... except by piety and good action.",
        "scripture_hadith_ref": "Farewell Sermon of the Prophet (PBUH)",
        "deep_explanation": "A robust school and community prevention framework incorporates four practical pillars:\n1. Authentic Religious Education: Learners must study authentic Islamic sciences under certified teachers, mastering the context of verses (Asbab al-Nuzul) to remain immune to distorted extremist propaganda.\n2. Inclusivity & Anti-Bullying: Schools must foster a welcoming environment where isolated, introverted, or economically struggling students find genuine support, removing the emotional void recruiters exploit.\n3. Interfaith Cooperative Service: Organizing joint community service projects—such as tree planting, town cleanups, or charity drives—with Christian and other religious youth groups dissolves prejudices and cements national unity.\n4. Confidential Early Intervention: Recognizing warning signs (e.g., viewing violent manifestos, withdrawal from social life, sudden intolerance) and notifying trusted counselors is an act of care that rescues a friend from catastrophe.",
        "diagram_title": "The Community Peace Dike: 4 Layers of Defense",
        "svg_func": get_svg_lesson_5,
        "table_title": "Actionable Prevention Matrix: Roles Across School and Community",
        "table_headers": ["Stakeholder", "Primary Preventive Responsibility", "Concrete Action in Daily Practice"],
        "table_rows": [
            ["Individual Student", "Critical thinking & authentic learning", "Verifies online claims; avoids anonymous religious forums; befriends peers"],
            ["Family & Parents", "Emotional nurture & digital guidance", "Monitors internet habits with love; discusses social issues openly"],
            ["School & IRE Teachers", "Contextual theological instruction", "Teaches Wasatiyyah; debunks Takfir; hosts interfaith dialogue clubs"],
            ["Community Leaders", "Youth empowerment & recreational hubs", "Provides sports leagues, vocational workshops & mental health counseling"]
        ],
        "scenario": "Yusuf notices that his desk mate Omar has become unusually withdrawn, stopped playing soccer at break, and posted harsh social media comments declaring that 'those who do not belong to our sect are enemies.' Rather than mocking or ignoring him, Yusuf sits with Omar, listens empathetically to his frustrations regarding family financial distress, and invites him to join the school tree-planting club. Yusuf also discreetly confides his concerns to the school counselor. The counselor coordinates with Omar's parents and arranges academic and emotional support. Within weeks, Omar abandons his toxic online groups, reconnects with his peers, and thanks Yusuf for saving his life.",
        "real_world": "Launch a 'Youth Peace Club' in your school. Partner with other religious societies to coordinate a quarterly 'School Green Initiative' or a collaborative book-donation drive for underprivileged primary schools. Demonstrating constructive teamwork across diverse backgrounds visibly exemplifies the true Islamic spirit of compassion and civic responsibility.",
        "reflection": "Why is discreetly reporting an increasingly radicalized classmate to a school counselor an act of profound compassion rather than betrayal? How does working together on tangible charity initiatives dismantle stereotypes faster than lectures?",
        "misconception": "Misconception: Thinking that alerting school authorities about a friend's exposure to extremist propaganda is 'snitching' or getting them arrested. Early intervention by educators and counselors is purely therapeutic and educational—it protects the individual from criminal manipulation and saves their life.",
        "yt_id": "1m0GkX9r2Wk",
        "yt_title": "Preventing Violent Extremism Through Education and Community",
        "yt_desc": "Practical strategies for educators, youth, and communities to build resilience against radicalization and extremist narratives.",
        "mcq": {
            "question": "A student notices that a classmate has started watching violent militant videos during break times and preaching that it is an obligation to hate students of other faiths. What is the most responsible, Islamic action to take?",
            "options": [
                "A. Remain silent and ignore the behavior since it is a personal decision.",
                "B. Mock and publicly shame the classmate in front of the entire assembly.",
                "C. Circulate the classmate's private contact details across public social media.",
                "D. Speak privately and urgently with a trusted IRE teacher or school counselor to provide the classmate with professional mentorship and help."
            ],
            "answer": "D",
            "explanation": "Confidential reporting to a qualified educator or counselor guarantees safe, professional intervention that addresses radicalization early, protecting both the student and the wider school community."
        },
        "summary_content": "Preventing radicalization demands collective action through the 'Community Peace Dike': authentic education, social inclusivity, interfaith cooperation, and confidential early reporting. By supporting vulnerable youth and dismantling stereotypes, society creates an impenetrable barrier against extremism.",
        "key_points": [
            "Authentic education under qualified scholars provides intellectual immunity against extremist rhetoric.",
            "Supporting isolated classmates eliminates the emotional void manipulated by terror recruiters.",
            "Joint interfaith community projects foster enduring national unity and mutual respect.",
            "Discreetly alerting counselors about radical warning signs is an act of care that saves lives."
        ],
        "exit_ticket": "Propose one joint project your school's IRE society could organize with students of other faiths to improve your local community."
    },
    {
        "unit_order": 6,
        "lesson_title": "Unit synthesis",
        "inquiry": "How does the true Islamic concept of Jihad promote harmonious coexistence and peaceful development in Kenya?",
        "hook": "Imagine a majestic, powerful river flowing through a lush agricultural valley. When channeled through reinforced irrigation canals and modern hydro-dams, the river generates clean electricity for millions of homes and irrigates vast farms that feed the nation. But if criminals demolish the dikes, the river surges as an uncontrolled flood, submerging towns and destroying lives. Authentic Islamic teachings are like that life-giving, controlled river—a divine source of peace, moral energy, and social justice. In this synthesis lesson, we unite all strands of Jihad, Wasatiyyah, and civic duty to declare our unwavering dedication to peace in Kenya.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Mount_Kenya.jpg/800px-Mount_Kenya.jpg",
        "image_title": "Mount Kenya: National Strength & Permanence",
        "image_caption": "Mount Kenya standing tall and majestic, symbolizing national resilience, peace, and the harmonious unity of all Kenyan citizens.",
        "concept_name": "The Shield of Harmonious Coexistence & National Unity",
        "concept_explanation": "Authentic Islam establishes harmonious coexistence (Ta'ayush) and national cohesion as paramount religious obligations. Grounded in Wasatiyyah (the balanced middle path), true Jihad empowers Kenyan Muslims to excel spiritually, reject extremist terrorism, protect human dignity, and partner with fellow citizens of all faiths to build a prosperous, secure nation.",
        "scripture_quran": "O mankind, indeed We have created you from male and female and made you peoples and tribes that you may know one another. Indeed, the most noble of you in the sight of Allah is the most righteous of you. Indeed, Allah is Knowing and Acquainted.",
        "scripture_quran_ref": "Surah Al-Hujurat 49:13",
        "scripture_hadith": "None of you truly believes until he wishes for his brother what he wishes for himself.",
        "scripture_hadith_ref": "Sahih al-Bukhari 13",
        "deep_explanation": "Synthesizing the unit yields four universal principles uniting Islamic faith with patriotic citizenship:\n1. The True Hierarchy of Jihad: The greatest struggle is mastering the self (Greater Jihad), pursuing academic excellence, and providing ethical leadership, while violent distortions are recognized as un-Islamic crimes.\n2. Wasatiyyah as a National Anchor: By steering clear of religious neglect on the one side and rigid extremism on the other, Muslims serve as a balanced, stabilizing force for peace in Kenya.\n3. Sanctity of the Human Family: Surah Al-Hujurat (49:13) establishes that ethnic and religious diversity is intentional divine design meant for mutual acquaintance and cooperation, not conflict.\n4. Proactive Civic Guardianship: Every Muslim youth is an ambassador of peace, tasked with verifying information (Tabayyun), helping vulnerable peers, and protecting our motherland from extremist sabotage.",
        "diagram_title": "The Shield of Harmonious Coexistence & National Unity",
        "svg_func": get_svg_lesson_6,
        "table_title": "Master Unit Synthesis Matrix: Contemporary Issues in Islam",
        "table_headers": ["Core Topic Area", "Theological Foundation (Quran & Sunnah)", "Social Application in Kenya", "Ultimate National Outcome"],
        "table_rows": [
            ["Concept of Jihad", "Striving for goodness; Greater Jihad (Sunan Abu Dawood)", "Academic diligence, self-discipline & moral leadership", "Spiritual excellence & productive youth"],
            ["Rejection of Terror", "Sanctity of life; ban on civilian harm (5:32)", "Categorical condemnation of violence and Takfir", "Security, public safety & protected lives"],
            ["Counter-Radicalization", "Firmness against extremism (Sahih Muslim 2670)", "Addressing youth unemployment, isolation & fake news", "Resilient youth immune to grooming"],
            ["National Coexistence", "Divine purpose of human diversity (49:13)", "Active interfaith collaboration with Christian peers", "Enduring peace, unity & Kenyan development"]
        ],
        "scenario": "Evaluate the following four scenarios and match them with their correct Islamic principle:\n1. Halima wakes up early for Fajr and studies diligently to master quadratic equations. (Answer: Greater Jihad / Intellectual Striving)\n2. Hussein works with Christian peers to plant 500 indigenous trees along a riverbank. (Answer: Interfaith Cooperation / Environmental Amanah)\n3. An underground militia uses explosives in a crowded marketplace to enforce ideology. (Answer: Terrorism / Fasad / Severe Transgression)\n4. Amina notices a peer being groomed online by a radical group and alerts the counselor. (Answer: Active Prevention / Saving Lives)",
        "real_world": "Draft and sign a 'Classroom Peace Charter.' Collaborate as a class to articulate five practical covenants: 1. We celebrate ethnic and religious diversity as divine beauty, 2. We resolve conflicts through patient dialogue and mediation, 3. We support classmates experiencing loneliness or distress, 4. We verify all news before sharing online, and 5. We stand united as proud, patriotic Kenyan students. Display your signed charter prominently in your classroom.",
        "reflection": "How does the Quranic vision in Surah Al-Hujurat (49:13) inspire us to take pride in Kenyan diversity? What concrete responsibility do you bear as a Junior School student to keep your school a sanctuary of peace?",
        "misconception": "Misconception: Believing that being a devout Muslim conflicts with being a patriotic Kenyan citizen. In authentic Islamic theology, loving, defending, and serving one's country and neighbors with justice is an integral expression of sincere faith.",
        "yt_id": "X0Qp_9vK8hM",
        "yt_title": "Comprehensive Unit Synthesis: Contemporary Issues in Islam",
        "yt_desc": "Capstone summary reviewing authentic Jihad, the condemnation of extremism, and Islam's contribution to national peace and coexistence.",
        "mcq": {
            "question": "A student encounters an anonymous post in an online group cherry-picking a Quranic verse to claim that disrupting local non-Muslim businesses is a religious duty. Applying the complete synthesis of this unit, what is the most appropriate response?",
            "options": [
                "A. Forward the message to other chat groups to see what classmates think.",
                "B. Ignore the post completely and wait for someone else to resolve it.",
                "C. Post a polite, evidence-based reply stating that harming innocent businesses violates Islamic justice, and report the account to school authorities.",
                "D. Delete all social media accounts and refuse to communicate with peers."
            ],
            "answer": "C",
            "explanation": "This response actively refutes extremist misinformation using authentic Islamic principles of justice and employs safe reporting channels, exemplifying complete civic and religious responsibility."
        },
        "summary_content": "Authentic Islam is a religion of balance (Wasatiyyah) and mercy. True Jihad is the positive pursuit of moral and academic excellence. By categorically rejecting terrorism, countering radicalization, and embracing diversity (Surah Al-Hujurat 49:13), Kenyan Muslim youth act as catalysts for national unity and flourishing.",
        "key_points": [
            "Authentic Islam is founded upon the moderate middle path of Wasatiyyah.",
            "True Jihad is the noble striving to build character, protect life, and serve the nation.",
            "Surah Al-Hujurat (49:13) celebrates human diversity as an opportunity for mutual respect.",
            "Every student has an essential role in preventing extremism and building a peaceful Kenya."
        ],
        "exit_ticket": "Write one concise sentence summarizing why a patriotic Kenyan Muslim must actively reject extremism and champion peace."
    }
]


# ─────────────────────────────────────────────────────────────────────────────
# INGESTION & AUDIT EXECUTION ENGINE
# ─────────────────────────────────────────────────────────────────────────────

@transaction.atomic
def ingest_topic_17():
    print("================================================================================")
    print("STARTING PRODUCTION INGESTION: GRADE 9 IRE — TOPIC 17")
    print("Topic: Contemporary Issues (Jihad, Terrorism, and Extremism) (Topic ID 357)")
    print("================================================================================")

    topic = Topic.objects.get(id=357)
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

    for ldata in TOPIC_17_LESSONS:
        order = ldata["unit_order"]
        title = ldata["lesson_title"]
        print(f"\nIngesting Lesson {order}/6: {title}...")

        # 1. Create LearningUnit
        unit = LearningUnit.objects.create(
            topic=topic,
            name=f"Lesson 6.6.{order}: {title}",
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
    print("INGESTION COMPLETE FOR TOPIC 17!")
    print(f"Created Units: {created_units}")
    print(f"Created Lessons: {created_lessons}")
    print(f"Created Blocks: {created_blocks}")
    print(f"Created Assets: {created_assets}")
    print("================================================================================")


if __name__ == "__main__":
    ingest_topic_17()
