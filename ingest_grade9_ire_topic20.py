"""
VLearn CBC Grade 9 IRE — Topic 20: Muslim Institutions
Production Ingestion and Enrichment Script for all 9 Lessons

Target Topic in DB: Topic ID 360 (Subject: IRE ID 53, Grade: Grade 9 ID 18)
Source Markdown: /home/jason-bitega/Desktop/VL/vlearn_repositories/Grade 9 IRE/muslim-institutions.md

9 Lessons Ingested & Fully Enriched:
  1. Lesson 7.3.1: What is a Muslim institution?
  2. Lesson 7.3.2: The role of mosques (Masajid) in society
  3. Lesson 7.3.3: The role of madrasas in educational and moral development
  4. Lesson 7.3.4: The role of Muslim NGOs in community development
  5. Lesson 7.3.5: How institutions preserve Islamic values and heritage
  6. Lesson 7.3.6: Visit/interview preparation: ethical research and observation
  7. Lesson 7.3.7: Challenges facing Muslim institutions in Kenya
  8. Lesson 7.3.8: Proposing solutions to institutional challenges
  9. Lesson 7.3.9: Unit and strand synthesis: the sanctuary of Islamic heritage
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
# 9 DEDICATED RESPONSIVE PEDAGOGICAL VECTOR SVGS (#0f172a theme, viewBox 880x440)
# ─────────────────────────────────────────────────────────────────────────────

def get_svg_lesson_1():
    """Lesson 7.3.1: The Three Pillars of Muslim Institutions in Kenya"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg201" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg201)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE THREE PILLARS OF MUSLIM INSTITUTIONS IN KENYA</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">A Structured Social Ecosystem Serving Spiritual, Educational, and Humanitarian Needs</text>

  <!-- Pillar 1: Mosques (Masajid) -->
  <g transform="translate(45, 90)">
    <rect width="240" height="270" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="240" height="42" rx="10" fill="#0284c7"/>
    <text x="120" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. MOSQUES (MASAJID)</text>
    <rect x="20" y="56" width="200" height="24" rx="4" fill="#0f172a"/>
    <text x="120" y="72" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Spiritual &amp; Social Sanctuary</text>
    <text x="15" y="108" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="15" dy="0">• Five Daily &amp; Jumu'ah Salat</tspan>
      <tspan x="15" dy="20">• Circles of Knowledge (Halaqah)</tspan>
      <tspan x="15" dy="20">• Local Zakat &amp; Sadaqah Hub</tspan>
      <tspan x="15" dy="20">• Community Dispute Resolution</tspan>
      <tspan x="15" dy="20">• Absolute Equality in Rows</tspan>
      <tspan x="15" dy="20">• Center of Neighborhood Unity</tspan>
    </text>
    <rect x="20" y="228" width="200" height="26" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="120" y="245" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Spiritual Alignment</text>
  </g>

  <!-- Pillar 2: Madrasas (Islamic Schools) -->
  <g transform="translate(320, 90)">
    <rect width="240" height="270" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="240" height="42" rx="10" fill="#059669"/>
    <text x="120" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. MADRASAS (SCHOOLS)</text>
    <rect x="20" y="56" width="200" height="24" rx="4" fill="#0f172a"/>
    <text x="120" y="72" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Educational &amp; Moral Shield</text>
    <text x="15" y="108" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="15" dy="0">• Qur'anic Literacy &amp; Tajweed</tspan>
      <tspan x="15" dy="20">• Akhlaq (Virtues &amp; Ethics)</tspan>
      <tspan x="15" dy="20">• Fiqh of Purification &amp; Salat</tspan>
      <tspan x="15" dy="20">• Arabic &amp; Swahili-Ajami Texts</tspan>
      <tspan x="15" dy="20">• Preservation of Heritage</tspan>
      <tspan x="15" dy="20">• Upright Civic Character</tspan>
    </text>
    <rect x="20" y="228" width="200" height="26" rx="4" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <text x="120" y="245" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Moral Transformation</text>
  </g>

  <!-- Pillar 3: Muslim NGOs -->
  <g transform="translate(595, 90)">
    <rect width="240" height="270" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="240" height="42" rx="10" fill="#7e22ce"/>
    <text x="120" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">3. MUSLIM NGOS</text>
    <rect x="20" y="56" width="200" height="24" rx="4" fill="#0f172a"/>
    <text x="120" y="72" fill="#c084fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Development &amp; Relief</text>
    <text x="15" y="108" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="15" dy="0">• Solar Water Boreholes</tspan>
      <tspan x="15" dy="20">• Emergency Flood/Drought Aid</tspan>
      <tspan x="15" dy="20">• Orphan &amp; Widow Sponsorship</tspan>
      <tspan x="15" dy="20">• Community Health Clinics</tspan>
      <tspan x="15" dy="20">• Sadaqah Jariyah Projects</tspan>
      <tspan x="15" dy="20">• Universal Mercy to All</tspan>
    </text>
    <rect x="20" y="228" width="200" height="26" rx="4" fill="#0f172a" stroke="#a855f7" stroke-width="1"/>
    <text x="120" y="245" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Socio-Economic Service</text>
  </g>

  <!-- Foundation Banner -->
  <rect x="45" y="380" width="790" height="36" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
  <text x="440" y="403" fill="#fef08a" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600" text-anchor="middle">SURAH AN-NISA 4:58: "Indeed, Allah commands you to render trusts to whom they are due..."</text>
</svg>"""


def get_svg_lesson_2():
    """Lesson 7.3.2: The Multi-Faceted Role of the Mosque (Masjid)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg202" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg202)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE FOUR PILLARS OF THE MOSQUE IN SOCIETY</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Surah Al-Jinn 72:18 — The Civic, Spiritual, and Welfare Heart of the Community</text>

  <!-- Center Hub: The Mosque -->
  <g transform="translate(340, 150)">
    <circle cx="100" cy="70" r="65" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
    <text x="100" y="55" fill="#fef08a" font-family="system-ui, sans-serif" font-size="28" text-anchor="middle">🕌</text>
    <text x="100" y="80" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">AL-MASJID</text>
    <text x="100" y="96" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Community Core</text>
  </g>

  <!-- Top-Left: Spiritual Sanctuary -->
  <g transform="translate(50, 75)">
    <rect width="250" height="115" rx="8" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <text x="125" y="26" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. SPIRITUAL SANCTUARY</text>
    <text x="15" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="15" dy="0">• Five daily congregational prayers</tspan>
      <tspan x="15" dy="18">• Friday Jumu'ah communal assembly</tspan>
      <tspan x="15" dy="18">• Eradication of social class &amp; race</tspan>
      <tspan x="15" dy="18">• Standing shoulder-to-shoulder</tspan>
    </text>
  </g>

  <!-- Top-Right: Educational Hub -->
  <g transform="translate(580, 75)">
    <rect width="250" height="115" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="125" y="26" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. EDUCATIONAL HUB</text>
    <text x="15" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="15" dy="0">• Study circles (Halaqah) for all ages</tspan>
      <tspan x="15" dy="18">• Reference libraries &amp; archives</tspan>
      <tspan x="15" dy="18">• Khutbah guidance on civic issues</tspan>
      <tspan x="15" dy="18">• Evening tutoring for local youth</tspan>
    </text>
  </g>

  <!-- Bottom-Left: Welfare & Charity Point -->
  <g transform="translate(50, 250)">
    <rect width="250" height="115" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <text x="125" y="26" fill="#c084fc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. CHARITY &amp; WELFARE HUB</text>
    <text x="15" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="15" dy="0">• Zakat and Sadaqah collection</tspan>
      <tspan x="15" dy="18">• Food bank &amp; dry ration hampers</tspan>
      <tspan x="15" dy="18">• Clean drinking water for travelers</tspan>
      <tspan x="15" dy="18">• Disaster emergency shelter</tspan>
    </text>
  </g>

  <!-- Bottom-Right: Social Mediation -->
  <g transform="translate(580, 250)">
    <rect width="250" height="115" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="125" y="26" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">4. SOCIAL MEDIATION (ISLAAH)</text>
    <text x="15" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="15" dy="0">• Marital counseling &amp; reconciliation</tspan>
      <tspan x="15" dy="18">• Business partnership arbitration</tspan>
      <tspan x="15" dy="18">• Elder committees resolving feuds</tspan>
      <tspan x="15" dy="18">• Promoting local security &amp; peace</tspan>
    </text>
  </g>

  <!-- Connective Arrows/Lines -->
  <path d="M 300 132 L 340 185" stroke="#0284c7" stroke-width="2" stroke-dasharray="4,4"/>
  <path d="M 580 132 L 540 185" stroke="#10b981" stroke-width="2" stroke-dasharray="4,4"/>
  <path d="M 300 307 L 340 255" stroke="#a855f7" stroke-width="2" stroke-dasharray="4,4"/>
  <path d="M 580 307 L 540 255" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>

  <!-- Footer Banner -->
  <rect x="50" y="388" width="780" height="32" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="440" y="409" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Nairobi Jamia Mosque &amp; Lamu Riyadha Mosque embody this integrated model across Kenyan history.</text>
</svg>"""


def get_svg_lesson_3():
    """Lesson 7.3.3: The Madrasa Growth Garden"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg203" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg203)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE MADRASA GROWTH GARDEN: NURTURING CHARACTER</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">From Scriptural Seed to the Fruits of Moral Excellence (Akhlaq) in Society</text>

  <!-- Layer 4: The Fruits (Conduct in Society) -->
  <g transform="translate(60, 80)">
    <rect width="760" height="70" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="380" y="25" fill="#34d399" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">FRUITS: PRACTICAL MORAL CONDUCT IN DAILY LIFE</text>
    <text x="380" y="50" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Academic Integrity • Respect for Parents • Public Service • Kindness to Neighbors • Anti-Corruption Shield</text>
  </g>

  <!-- Upward Arrow -->
  <text x="440" y="172" fill="#10b981" font-size="20" font-weight="bold" text-anchor="middle">▲</text>

  <!-- Layer 3: The Stem & Branches (Moral Virtues - Akhlaq) -->
  <g transform="translate(100, 185)">
    <rect width="680" height="70" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="340" y="25" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">STEM &amp; BRANCHES: CORE ISLAMIC VIRTUES (AKHLAQ)</text>
    <text x="340" y="50" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Amanah (Trustworthiness) • Haya (Modesty) • Sidq (Truthfulness) • Sabr (Patience) • 'Adl (Justice)</text>
  </g>

  <!-- Upward Arrow -->
  <text x="440" y="277" fill="#38bdf8" font-size="20" font-weight="bold" text-anchor="middle">▲</text>

  <!-- Layer 2: The Seed (Scriptural Literacy) -->
  <g transform="translate(140, 290)">
    <rect width="600" height="55" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="300" y="24" fill="#fef08a" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">SEED: SCRIPTURAL &amp; LEGAL LITERACY</text>
    <text x="300" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Qur'an Recitation &amp; Tajweed • Hadith Studies • Fiqh of Ibadat • Arabic Language</text>
  </g>

  <!-- Layer 1: The Soil (Faith & Tawhid) -->
  <g transform="translate(180, 360)">
    <rect width="520" height="50" rx="8" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
    <text x="260" y="22" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">SOIL: IMAN (FAITH) &amp; DEVOTION TO ALLAH</text>
    <text x="260" y="40" fill="#64748b" font-family="system-ui, sans-serif" font-size="10.5" text-anchor="middle">The spiritual foundation without which character cannot take root.</text>
  </g>
</svg>"""


def get_svg_lesson_4():
    """Lesson 7.3.4: The Muslim NGO Sustainable Project Cycle"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg204" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg204)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE MUSLIM NGO PROFESSIONAL PROJECT CYCLE</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">How Islamic Values of Amanah and Sadaqah Jariyah Drive Sustainable Development</text>

  <!-- Step 1 -->
  <g transform="translate(30, 95)">
    <rect width="150" height="240" rx="8" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <circle cx="75" cy="35" r="18" fill="#0369a1"/>
    <text x="75" y="41" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">1</text>
    <text x="75" y="78" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">MOBILIZATION</text>
    <text x="12" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
      <tspan x="12" dy="0">• Zakat collection</tspan>
      <tspan x="12" dy="18">• Sadaqah funds</tspan>
      <tspan x="12" dy="18">• Donor accountability</tspan>
      <tspan x="12" dy="18">• Transparent trusts</tspan>
      <tspan x="12" dy="18">• Amanah auditing</tspan>
    </text>
    <rect x="10" y="200" width="130" height="25" rx="4" fill="#0f172a"/>
    <text x="75" y="217" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">Resource Trust</text>
  </g>

  <!-- Arrow 1->2 -->
  <text x="190" y="215" fill="#38bdf8" font-size="20" font-weight="bold" text-anchor="middle">→</text>

  <!-- Step 2 -->
  <g transform="translate(200, 95)">
    <rect width="150" height="240" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <circle cx="75" cy="35" r="18" fill="#059669"/>
    <text x="75" y="41" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">2</text>
    <text x="75" y="78" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">ASSESSMENT</text>
    <text x="12" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
      <tspan x="12" dy="0">• Rigorous field survey</tspan>
      <tspan x="12" dy="18">• Hydrogeological check</tspan>
      <tspan x="12" dy="18">• Vulnerability register</tspan>
      <tspan x="12" dy="18">• County coordination</tspan>
      <tspan x="12" dy="18">• Need prioritisation</tspan>
    </text>
    <rect x="10" y="200" width="130" height="25" rx="4" fill="#0f172a"/>
    <text x="75" y="217" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">Data-Driven Needs</text>
  </g>

  <!-- Arrow 2->3 -->
  <text x="360" y="215" fill="#34d399" font-size="20" font-weight="bold" text-anchor="middle">→</text>

  <!-- Step 3 -->
  <g transform="translate(370, 95)">
    <rect width="150" height="240" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <circle cx="75" cy="35" r="18" fill="#b45309"/>
    <text x="75" y="41" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">3</text>
    <text x="75" y="78" fill="#fef08a" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">EXECUTION</text>
    <text x="12" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
      <tspan x="12" dy="0">• Solar borehole drill</tspan>
      <tspan x="12" dy="18">• Classroom building</tspan>
      <tspan x="12" dy="18">• Medical clinic setup</tspan>
      <tspan x="12" dy="18">• Water piping to village</tspan>
      <tspan x="12" dy="18">• High-grade materials</tspan>
    </text>
    <rect x="10" y="200" width="130" height="25" rx="4" fill="#0f172a"/>
    <text x="75" y="217" fill="#fef08a" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">Engineering Quality</text>
  </g>

  <!-- Arrow 3->4 -->
  <text x="530" y="215" fill="#fef08a" font-size="20" font-weight="bold" text-anchor="middle">→</text>

  <!-- Step 4 -->
  <g transform="translate(540, 95)">
    <rect width="150" height="240" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <circle cx="75" cy="35" r="18" fill="#7e22ce"/>
    <text x="75" y="41" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">4</text>
    <text x="75" y="78" fill="#c084fc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">HANDOVER</text>
    <text x="12" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
      <tspan x="12" dy="0">• Local committee rota</tspan>
      <tspan x="12" dy="18">• Solar repair training</tspan>
      <tspan x="12" dy="18">• Maintenance reserve</tspan>
      <tspan x="12" dy="18">• Village ownership</tspan>
      <tspan x="12" dy="18">• Enduring asset</tspan>
    </text>
    <rect x="10" y="200" width="130" height="25" rx="4" fill="#0f172a"/>
    <text x="75" y="217" fill="#c084fc" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">Local Stewardship</text>
  </g>

  <!-- Arrow 4->5 -->
  <text x="700" y="215" fill="#c084fc" font-size="20" font-weight="bold" text-anchor="middle">→</text>

  <!-- Step 5 -->
  <g transform="translate(710, 95)">
    <rect width="140" height="240" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <circle cx="70" cy="35" r="18" fill="#be123c"/>
    <text x="70" y="41" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">5</text>
    <text x="70" y="78" fill="#fda4af" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">IMPACT</text>
    <text x="10" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
      <tspan x="10" dy="0">• Girl child in school</tspan>
      <tspan x="10" dy="18">• Cholera eliminated</tspan>
      <tspan x="10" dy="18">• Economic growth</tspan>
      <tspan x="10" dy="18">• Sadaqah Jariyah</tspan>
      <tspan x="10" dy="18">• Human dignity</tspan>
    </text>
    <rect x="8" y="200" width="124" height="25" rx="4" fill="#0f172a"/>
    <text x="70" y="217" fill="#fda4af" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">Generational Lift</text>
  </g>

  <!-- Footer Banner -->
  <rect x="30" y="365" width="820" height="45" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="440" y="392" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600" text-anchor="middle">"The most beloved of people to Allah are those who are most beneficial to people." — Hadith (At-Tirmidhi)</text>
</svg>"""


def get_svg_lesson_5():
    """Lesson 7.3.5: Preserving Islamic Values and Heritage in Kenya"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg205" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg205)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">FOUR DIMENSIONS OF ISLAMIC HERITAGE PRESERVATION IN KENYA</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Lamu Riyadha Archives, Historic Coral Architecture, and Living Cultural Ethics</text>

  <!-- Dimension 1: Written Manuscripts -->
  <g transform="translate(45, 85)">
    <rect width="185" height="275" rx="8" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <rect width="185" height="34" rx="8" fill="#0369a1"/>
    <text x="92" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">1. MANUSCRIPTS</text>
    <text x="12" y="58" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="12" dy="0">• 300+ yr Riyadha texts</tspan>
      <tspan x="12" dy="20">• Swahili-Arabic (Ajami)</tspan>
      <tspan x="12" dy="20">• Legal fatwas &amp; trade</tspan>
      <tspan x="12" dy="20">• Classic Islamic poetry</tspan>
      <tspan x="12" dy="20">• Archival conservation</tspan>
      <tspan x="12" dy="20">• Proof of early literacy</tspan>
    </text>
    <rect x="12" y="225" width="161" height="26" rx="4" fill="#0f172a"/>
    <text x="92" y="242" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Written Knowledge</text>
  </g>

  <!-- Dimension 2: Sacred Architecture -->
  <g transform="translate(245, 85)">
    <rect width="185" height="275" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="185" height="34" rx="8" fill="#059669"/>
    <text x="92" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">2. ARCHITECTURE</text>
    <text x="12" y="58" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="12" dy="0">• Mandhry Mosque (1507)</tspan>
      <tspan x="12" dy="20">• Coral stone walls</tspan>
      <tspan x="12" dy="20">• Carved Swahili mihrabs</tspan>
      <tspan x="12" dy="20">• Geometric woodwork</tspan>
      <tspan x="12" dy="20">• Ancient conical minarets</tspan>
      <tspan x="12" dy="20">• Lamu UNESCO town</tspan>
    </text>
    <rect x="12" y="225" width="161" height="26" rx="4" fill="#0f172a"/>
    <text x="92" y="242" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Built Monuments</text>
  </g>

  <!-- Dimension 3: Living Moral Ethics -->
  <g transform="translate(445, 85)">
    <rect width="185" height="275" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="185" height="34" rx="8" fill="#b45309"/>
    <text x="92" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">3. LIVING VALUES</text>
    <text x="12" y="58" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="12" dy="0">• Shariah commercial ethics</tspan>
      <tspan x="12" dy="20">• Honest weight &amp; measure</tspan>
      <tspan x="12" dy="20">• Family ties (Silat ar-Rahm)</tspan>
      <tspan x="12" dy="20">• Orphan protection</tspan>
      <tspan x="12" dy="20">• Community hospitality</tspan>
      <tspan x="12" dy="20">• Daily prayer discipline</tspan>
    </text>
    <rect x="12" y="225" width="161" height="26" rx="4" fill="#0f172a"/>
    <text x="92" y="242" fill="#fef08a" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Ethical Practice</text>
  </g>

  <!-- Dimension 4: Cultural Arts & Dress -->
  <g transform="translate(645, 85)">
    <rect width="185" height="275" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="185" height="34" rx="8" fill="#7e22ce"/>
    <text x="92" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">4. ARTS &amp; DRESS</text>
    <text x="12" y="58" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="12" dy="0">• Kanzu &amp; Kofia attire</tspan>
      <tspan x="12" dy="20">• Proverb Lesos &amp; Buibui</tspan>
      <tspan x="12" dy="20">• Kiswahili literature</tspan>
      <tspan x="12" dy="20">• Arabic calligraphy</tspan>
      <tspan x="12" dy="20">• Geometric motifs</tspan>
      <tspan x="12" dy="20">• East African identity</tspan>
    </text>
    <rect x="12" y="225" width="161" height="26" rx="4" fill="#0f172a"/>
    <text x="92" y="242" fill="#c084fc" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Cultural Identity</text>
  </g>

  <!-- Footer Banner -->
  <rect x="45" y="380" width="785" height="32" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="440" y="401" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Preserving heritage bridges centuries of faith, scholarship, and nation-building in Kenya.</text>
</svg>"""


def get_svg_lesson_6():
    """Lesson 7.3.6: Researcher's Ethical Fieldwork Protocol"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg206" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg206)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">GRADE 9 RESEARCHER'S ETHICAL FIELDWORK PROTOCOL</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Four Non-Negotiable Pillars for Visiting Mosques, Madrasas, and Community Centers</text>

  <!-- Pillar 1: Modest Dress & Decorum -->
  <g transform="translate(45, 90)">
    <rect width="185" height="265" rx="8" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <rect width="185" height="36" rx="8" fill="#0369a1"/>
    <text x="92" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">1. DECORUM &amp; DRESS</text>
    <text x="12" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="12" dy="0">• Loose, clean attire</tspan>
      <tspan x="12" dy="20">• Remove shoes at door</tspan>
      <tspan x="12" dy="20">• Greet with peace (Salam)</tspan>
      <tspan x="12" dy="20">• Silence during prayer</tspan>
      <tspan x="12" dy="20">• Walk quietly in halls</tspan>
      <tspan x="12" dy="20">• Honor sacred sanctity</tspan>
    </text>
    <rect x="12" y="215" width="161" height="26" rx="4" fill="#0f172a"/>
    <text x="92" y="232" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Adab al-Masjid</text>
  </g>

  <!-- Pillar 2: Informed Consent -->
  <g transform="translate(245, 90)">
    <rect width="185" height="265" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="185" height="36" rx="8" fill="#059669"/>
    <text x="92" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">2. INFORMED CONSENT</text>
    <text x="12" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="12" dy="0">• Seek permission first</tspan>
      <tspan x="12" dy="20">• Never record secretly</tspan>
      <tspan x="12" dy="20">• No photos of children</tspan>
      <tspan x="12" dy="20">• Protect vulnerable dignity</tspan>
      <tspan x="12" dy="20">• Explain project intent</tspan>
      <tspan x="12" dy="20">• Surah Al-Nur (24:27)</tspan>
    </text>
    <rect x="12" y="215" width="161" height="26" rx="4" fill="#0f172a"/>
    <text x="92" y="232" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Privacy &amp; Dignity</text>
  </g>

  <!-- Pillar 3: Respectful Inquiry -->
  <g transform="translate(445, 90)">
    <rect width="185" height="265" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="185" height="36" rx="8" fill="#b45309"/>
    <text x="92" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">3. INQUIRY PROTOCOL</text>
    <text x="12" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="12" dy="0">• 3-5 pre-written questions</tspan>
      <tspan x="12" dy="20">• Open-ended &amp; focused</tspan>
      <tspan x="12" dy="20">• Ask on service &amp; relief</tspan>
      <tspan x="12" dy="20">• Avoid intrusive queries</tspan>
      <tspan x="12" dy="20">• Listen without arguing</tspan>
      <tspan x="12" dy="20">• Thank interviewees</tspan>
    </text>
    <rect x="12" y="215" width="161" height="26" rx="4" fill="#0f172a"/>
    <text x="92" y="232" fill="#fef08a" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Targeted Questions</text>
  </g>

  <!-- Pillar 4: Objective Reporting -->
  <g transform="translate(645, 90)">
    <rect width="185" height="265" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="185" height="36" rx="8" fill="#7e22ce"/>
    <text x="92" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">4. OBJECTIVITY (SIDQ)</text>
    <text x="12" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">
      <tspan x="12" dy="0">• Record accurate facts</tspan>
      <tspan x="12" dy="20">• Zero fabrication of data</tspan>
      <tspan x="12" dy="20">• Note challenges fairly</tspan>
      <tspan x="12" dy="20">• Propose solutions</tspan>
      <tspan x="12" dy="20">• Share report with school</tspan>
      <tspan x="12" dy="20">• Practice Amanah in data</tspan>
    </text>
    <rect x="12" y="215" width="161" height="26" rx="4" fill="#0f172a"/>
    <text x="92" y="232" fill="#c084fc" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Academic Integrity</text>
  </g>

  <!-- Footer Banner -->
  <rect x="45" y="375" width="785" height="35" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="440" y="397" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Surah Al-Nur 24:27: "Do not enter houses other than your own until you have asked permission..."</text>
</svg>"""


def get_svg_lesson_7():
    """Lesson 7.3.7: Stagnant vs. Empowered Muslim Institutions"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg207" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg207)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">INSTITUTIONAL CHALLENGES: STAGNANT VS. EMPOWERED SYSTEMS</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Why Administrative Governance and Transparency Determine Institutional Survival</text>

  <!-- Left: The Stagnant Institution -->
  <g transform="translate(50, 85)">
    <rect width="365" height="270" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="365" height="38" rx="10" fill="#9f1239"/>
    <text x="182" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">THE STAGNANT INSTITUTION (CRISIS)</text>
    <text x="20" y="65" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11.5">
      <tspan x="20" dy="0">❌ Unpredictable cash donations only</tspan>
      <tspan x="20" dy="24">❌ Manual, missing paper exercise books</tspan>
      <tspan x="20" dy="24">❌ Low, erratic salaries causing teacher turnover</tspan>
      <tspan x="20" dy="24">❌ Youth &amp; women completely excluded</tspan>
      <tspan x="20" dy="24">❌ Donor distrust due to zero public audits</tspan>
      <tspan x="20" dy="24">❌ Decrepit facilities, leaking roofs, torn books</tspan>
    </text>
    <rect x="20" y="225" width="325" height="28" rx="6" fill="#0f172a" stroke="#f43f5e" stroke-width="1"/>
    <text x="182" y="243" fill="#fda4af" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Risk: Closure, Loss of Youth, Apathy</text>
  </g>

  <!-- Center Arrow / VS Divider -->
  <g transform="translate(425, 185)">
    <circle cx="15" cy="15" r="22" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="15" y="21" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">VS</text>
  </g>

  <!-- Right: The Empowered Institution -->
  <g transform="translate(465, 85)">
    <rect width="365" height="270" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="365" height="38" rx="10" fill="#065f46"/>
    <text x="182" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">THE EMPOWERED INSTITUTION (SUSTAINABLE)</text>
    <text x="20" y="65" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11.5">
      <tspan x="20" dy="0">✓ Permanent Waqf endowments (shops, orchards)</tspan>
      <tspan x="20" dy="24">✓ Transparent monthly digital accounting sheets</tspan>
      <tspan x="20" dy="24">✓ Fair, regular salaries for certified teachers</tspan>
      <tspan x="20" dy="24">✓ Active Youth &amp; Women sub-committees</tspan>
      <tspan x="20" dy="24">✓ High community trust and booming donations</tspan>
      <tspan x="20" dy="24">✓ Modern solar power, digital labs, clean water</tspan>
    </text>
    <rect x="20" y="225" width="325" height="28" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <text x="182" y="243" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Result: Enduring Growth &amp; Social Impact</text>
  </g>

  <!-- Footer Banner -->
  <rect x="50" y="375" width="780" height="35" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="440" y="397" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Surah Al-Ra'd 13:11: "Allah will not change the condition of a people until they change what is in themselves."</text>
</svg>"""


def get_svg_lesson_8():
    """Lesson 7.3.8: The Waqf Self-Reliance Loop"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg208" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg208)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE WAQF SELF-RELIANCE LOOP: SUSTAINABLE COMMUNITY FINANCE</text>
  <text x="440" y="56" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">How Shariah-Compliant Endowments Fund Community Development Permanently</text>

  <!-- Box 1: Donor Endows Asset -->
  <g transform="translate(45, 90)">
    <rect width="220" height="110" rx="8" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <text x="110" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. WAQF CAPITAL ASSET</text>
    <text x="15" y="55" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
      <tspan x="15" dy="0">• Commercial rental shops</tspan>
      <tspan x="15" dy="18">• Clean water filtration kiosk</tspan>
      <tspan x="15" dy="18">• Agricultural farm or orchard</tspan>
    </text>
    <rect x="15" y="82" width="190" height="20" rx="4" fill="#0f172a"/>
    <text x="110" y="96" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Capital Inalienable (Never Sold)</text>
  </g>

  <!-- Arrow 1->2 -->
  <text x="290" y="150" fill="#38bdf8" font-size="24" font-weight="bold" text-anchor="middle">→</text>

  <!-- Box 2: Continuous Revenue Generation -->
  <g transform="translate(330, 90)">
    <rect width="220" height="110" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="110" y="28" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. REVENUE GENERATION</text>
    <text x="15" y="55" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
      <tspan x="15" dy="0">• Monthly shop rent collected</tspan>
      <tspan x="15" dy="18">• Affordable water sales revenue</tspan>
      <tspan x="15" dy="18">• Seasonal harvest profits</tspan>
    </text>
    <rect x="15" y="82" width="190" height="20" rx="4" fill="#0f172a"/>
    <text x="110" y="96" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">100% Shariah-Compliant Income</text>
  </g>

  <!-- Arrow 2->3 -->
  <text x="575" y="150" fill="#34d399" font-size="24" font-weight="bold" text-anchor="middle">→</text>

  <!-- Box 3: Transparent Trust Management -->
  <g transform="translate(615, 90)">
    <rect width="220" height="110" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="110" y="28" fill="#fef08a" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. WAQF BOARD / TRUST</text>
    <text x="15" y="55" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">
      <tspan x="15" dy="0">• Audited public accounts</tspan>
      <tspan x="15" dy="18">• Professional bookkeeping</tspan>
      <tspan x="15" dy="18">• Zero corruption / Riba</tspan>
    </text>
    <rect x="15" y="82" width="190" height="20" rx="4" fill="#0f172a"/>
    <text x="110" y="96" fill="#fef08a" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Stewards of Community Trust</text>
  </g>

  <!-- Downward Arrow to Social Welfare Outputs -->
  <text x="725" y="235" fill="#fef08a" font-size="24" font-weight="bold" text-anchor="middle">▼</text>

  <!-- Bottom Panel: 3 Core Funded Services -->
  <g transform="translate(45, 255)">
    <rect width="790" height="105" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <text x="395" y="26" fill="#c084fc" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">4. PERPETUAL WELFARE OUTPUTS (NO DONATION DEPENDENCE)</text>
    
    <g transform="translate(20, 42)">
      <rect width="235" height="50" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1"/>
      <text x="117" y="22" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">SALARIES PAID</text>
      <text x="117" y="38" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Regular pay for madrasa teachers</text>
    </g>

    <g transform="translate(275, 42)">
      <rect width="235" height="50" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1"/>
      <text x="117" y="22" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">FREE EDUCATION</text>
      <text x="117" y="38" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Textbooks &amp; solar power funded</text>
    </g>

    <g transform="translate(530, 42)">
      <rect width="235" height="50" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1"/>
      <text x="117" y="22" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">COMMUNITY HEALTH</text>
      <text x="117" y="38" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Dispensary medicine &amp; clean water</text>
    </g>
  </g>

  <!-- Leftward Return Arrow creating the Loop -->
  <path d="M 45 310 L 20 310 L 20 145 L 40 145" fill="none" stroke="#a855f7" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="20" y="235" fill="#a855f7" font-size="14" font-weight="bold" text-anchor="middle">▲</text>

  <!-- Footer Banner -->
  <rect x="45" y="385" width="790" height="32" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="440" y="406" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Waqf creates independent community resilience that lasts across generations.</text>
</svg>"""


def get_svg_lesson_9():
    """Lesson 7.3.9: The Sanctuary of Kenyan Islamic Heritage (Strand 7 Synthesis)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg209" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg209)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="34" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">STRAND 7 SYNTHESIS: THE SANCTUARY OF ISLAMIC HERITAGE IN KENYA</text>
  <text x="440" y="52" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Integrating History, Community Institutions, and the Shield of Unity into National Cohesion</text>

  <!-- Top Level: 4 Historical Streams -->
  <g transform="translate(45, 68)">
    <rect width="790" height="65" rx="8" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <text x="395" y="22" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">THE FOUR HISTORICAL STREAMS (ISLAM IN KENYA)</text>
    <text x="395" y="46" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" text-anchor="middle">1. Coastal Maritime Trade (8th C.)  •  2. Western Caravan Alliances (Mumia)  •  3. Central Railway Artisans  •  4. North Eastern Pastoral Heritage</text>
  </g>

  <!-- Downward Arrows -->
  <text x="440" y="152" fill="#0284c7" font-size="18" font-weight="bold" text-anchor="middle">▼</text>

  <!-- Mid Level: 3 Custodial Institutions -->
  <g transform="translate(45, 160)">
    <rect width="790" height="75" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="395" y="22" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">THE THREE CUSTODIAL INSTITUTIONS (PRESERVATION ECOSYSTEM)</text>
    <text x="395" y="44" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Mosques (Spiritual/Civic Hub)   |   Madrasas (Moral/Scriptural Shield)   |   Muslim NGOs (Humanitarian Relief &amp; Waqf)</text>
    <text x="395" y="62" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Preserving written manuscripts, sacred architecture, and living moral character (Akhlaq)</text>
  </g>

  <!-- Downward Arrows -->
  <text x="440" y="254" fill="#10b981" font-size="18" font-weight="bold" text-anchor="middle">▼</text>

  <!-- Lower Level: The Shield of Unity -->
  <g transform="translate(45, 262)">
    <rect width="790" height="65" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="395" y="22" fill="#fef08a" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">THE SHIELD OF UNITY (ISLAAH &amp; TA'AWUN)</text>
    <text x="395" y="46" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" text-anchor="middle">Surah Al-Hujurat (49:10): Eliminating tribalism, sectarianism, rumors, and arrogance through collective brotherhood</text>
  </g>

  <!-- Downward Arrows -->
  <text x="440" y="344" fill="#fbbf24" font-size="18" font-weight="bold" text-anchor="middle">▼</text>

  <!-- Bottom Result: Harmonious Kenyan Society -->
  <g transform="translate(45, 350)">
    <rect width="790" height="68" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="395" y="24" fill="#c084fc" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">OUTCOME: A HARMONIOUS, ETHICAL, AND PROSPEROUS KENYAN NATION</text>
    <text x="395" y="48" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Upright citizens dedicated to justice, peace, educational excellence, and shared public welfare.</text>
  </g>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# 9 LESSON DEFINITIONS WITH 7 CANONICAL CARDS
# ─────────────────────────────────────────────────────────────────────────────

LESSONS_DATA = [
    # LESSON 1 (7.3.1)
    {
        "order": 1,
        "code": "7.3.1",
        "title": "What is a Muslim institution?",
        "inquiry": "What are social institutions, and why does the Muslim community establish specialized organizations to preserve its heritage?",
        "hook": "Think about the bones, muscles, and organs in your body. Each of them has a unique, important function, but they are all held together and supported by a strong skeletal system. Without this system, your body could not stand, walk, or protect its vital organs. In a society, social institutions are like that skeletal system. They provide the structure, the support, and the pathways for a community to live, learn, grow, and protect its values across generations.",
        "concept_name": "Definition and Pillars of Muslim Institutions",
        "concept_explanation": (
            "An **institution** is a structured, organized body established in a society to meet fundamental religious, educational, social, or humanitarian needs.\\n\\n"
            "In Kenya, the Muslim community operates through three primary institutions:\\n"
            "1. **Mosques (*Masajid*):** Centers of worship, spiritual guidance, community consultation, and social cohesion.\\n"
            "2. **Madrasas (Islamic Schools):** Centers of religious education, moral character development, and preservation of sacred knowledge.\\n"
            "3. **Muslim NGOs (Non-Governmental Organizations):** Structured bodies focused on humanitarian relief, socio-economic development, and social welfare."
        ),
        "scripture_quran": "Indeed, Allah commands you to render trusts to whom they are due and when you judge between people to judge with justice. Excellent is that which Allah instructs you. Indeed, Allah is ever Hearing and Seeing.",
        "scripture_quran_ref": "Surah An-Nisa (4:58)",
        "scripture_hadith": "Let there arise from among you a group of people inviting to all that is good, enjoining what is right and forbidding what is wrong. And those are the successful.",
        "scripture_hadith_ref": "Surah Ali 'Imran (3:104)",
        "deep_explanation": (
            "Muslim institutions do not work in isolation; they form an integrated ecosystem of community support:\\n\\n"
            "1. **Preservation of Heritage:** These organizations are the custodians of history, manuscripts, and ethical values. Without structured institutions, religious knowledge and historical records would be lost as generations pass away.\\n"
            "2. **Translating Values into Service:** Islam teaches that faith (*Iman*) must manifest as practical action. Institutions provide the organized pathways to collect charity, educate youth, drill water boreholes, and defend the rights of the vulnerable.\\n"
            "3. **Social Cohesion:** They bring together individuals from diverse ethnic and economic backgrounds under a shared, structured mission of public service, promoting national development in Kenya."
        ),
        "diagram_title": "The Three Pillars of Muslim Institutions in Kenya",
        "svg_fn": get_svg_lesson_1,
        "table_title": "Comparative Analysis: The Three Core Muslim Institutions",
        "table_headers": ["Institution Type", "Primary Focus", "Key Functions", "Community Benefit"],
        "table_rows": [
            ["Mosque (Masjid)", "Spiritual & Communal", "Daily prayers, Jumu'ah, Halaqah, dispute mediation", "Builds local peace, brotherhood, and spiritual alignment"],
            ["Madrasa (School)", "Educational & Moral", "Qur'an recitation, Fiqh, Islamic history, character", "Builds ethical youth, literacy, and historical preservation"],
            ["Muslim NGO", "Socio-Economic & Relief", "Boreholes, orphan care, emergency relief, clinics", "Alleviates poverty, improves public health and self-reliance"]
        ],
        "scenario": (
            "When a massive fire accidentally destroys several homes in a Nairobi neighborhood, the local Muslim institutions coordinate their response. "
            "The **Mosque** instantly opens its community hall to provide temporary shelter and hot meals. The local **Madrasa** organizes its teachers and students "
            "to collect clean clothes, blankets, and school stationery for the affected children. Meanwhile, a **Muslim NGO** arrives with building materials, emergency grants, "
            "and trauma counselors to assist the displaced families in rebuilding their homes. This seamless cooperation demonstrates how structured institutions uphold human life and dignity."
        ),
        "real_world": "Conduct a 'Community Institution Mapping' exercise this week. Research and write down the names of at least one mosque, one madrasa, and one Muslim charity or NGO operating in your county or town. Note down one specific service that each institution provides to the public (such as feeding programs, clean water, or free tutoring).",
        "reflection": "Why is it significantly more effective to establish structured institutions to alleviate poverty compared to individuals giving informal charity alone? How do institutions preserve the history and identity of minority communities across centuries?",
        "misconception": "Misconception: Muslim institutions are purely places of ritual prayer with no role in wider social development. Fact: Since the early Medina period, Muslim institutions have functioned as complete centers for education, healthcare, legal mediation, and humanitarian aid.",
        "image_title": "Jamia Mosque Nairobi Community Complex",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Jamia_Mosque_Nairobi_Kenya.jpg/800px-Jamia_Mosque_Nairobi_Kenya.jpg",
        "image_caption": "Nairobi's historic Jamia Mosque complex houses prayer halls, a reference library, medical clinics, and welfare distribution offices.",
        "yt_title": "Understanding Social Institutions in Community Development",
        "yt_id": "kY3w-Y1QnE8",
        "yt_desc": "An educational documentary on how faith-based social institutions coordinate civic services, education, and humanitarian relief.",
        "mcq": {
            "question": "Which of the following is the primary purpose of establishing structured Muslim institutions like mosques, madrasas, and NGOs in society?",
            "options": [
                "To compete with other communities and win material prizes.",
                "To provide a permanent, organized structure to preserve Islamic values, heritage, and serve human needs.",
                "To establish separate rules of law that contradict national guidelines.",
                "To discourage youth from participating in national development."
            ],
            "answer": "To provide a permanent, organized structure to preserve Islamic values, heritage, and serve human needs.",
            "explanation": "Muslim institutions exist to provide organized, sustainable systems to preserve the community's spiritual values, maintain historical heritage, and deliver vital social services."
        },
        "summary_content": "An institution is a structured organization established to meet fundamental religious, educational, and social needs. In Kenya, mosques, madrasas, and Muslim NGOs form an interconnected ecosystem that preserves Islamic heritage and drives community welfare.",
        "key_points": [
            "An institution is an organized, enduring body established to meet societal and religious needs.",
            "The three primary Muslim institutions in Kenya are mosques, madrasas, and Muslim NGOs.",
            "Institutions preserve heritage, translate faith into service, and foster national cohesion."
        ],
        "exit_ticket": "Name the three types of Muslim institutions studied today and write down one unique function for each."
    },

    # LESSON 2 (7.3.2)
    {
        "order": 2,
        "code": "7.3.2",
        "title": "The role of mosques (Masajid) in society",
        "inquiry": "What are the spiritual, educational, and social roles of the mosque in a Muslim community, and how does it foster local unity?",
        "hook": "Imagine a town with no streetlights, no community halls, and no central square where neighbors can meet, talk, or seek help. It would feel dark, disconnected, and lonely. For a Muslim community, the mosque (*Masjid*) is that light, that meeting place, and that heart of the neighborhood. It is far more than just a place of prayer; it is the sanctuary where the spiritual, social, and physical needs of the community are met daily.",
        "concept_name": "The Multi-Faceted Role of the Mosque (Masjid)",
        "concept_explanation": (
            "The mosque (*Masjid*, literally a place of prostration) serves as the central hub of Islamic community life, fulfilling four primary functions:\\n\\n"
            "1. **Spiritual Sanctuary:** Providing a dedicated, pure space for the five daily prayers, congregational Friday (*Jumu'ah*) prayers, and personal supplication.\\n"
            "2. **Educational Hub:** Hosting public lectures, circles of study (*Halaqah*), Qur'anic literacy, and community libraries.\\n"
            "3. **Charity Distribution Point:** Serving as a collection and distribution center for Zakat and Sadaqah to support local vulnerable families.\\n"
            "4. **Social Mediation Center:** The Imam and elder committee act as neutral mediators to resolve family, commercial, and neighborhood disputes (*Islaah*)."
        ),
        "scripture_quran": "And [He revealed] that the mosques are for Allah, so do not invoke with Allah anyone.",
        "scripture_quran_ref": "Surah Al-Jinn (72:18)",
        "scripture_hadith": "The mosques of Allah are only to be maintained by those who believe in Allah and the Last Day and establish prayer and give zakah and do not fear except Allah...",
        "scripture_hadith_ref": "Surah Al-Tawbah (9:18)",
        "deep_explanation": (
            "Let's explore how the mosque serves as a democratic, protective civic space in society:\\n\\n"
            "1. **A Space of Absolute Equality:** In the mosque, there are no reserved VIP seats. A government cabinet secretary, a primary school teacher, a wealthy merchant, and a penniless laborer stand shoulder-to-shoulder in the same row, prostrating before Allah. This daily ritual dismantles arrogance, classism, and tribalism.\\n"
            "2. **Civic Guidance (The Khutbah):** The Jumu'ah (Friday) sermon is not merely an abstract lecture; it is a vital platform to address contemporary local challenges. Imams use the pulpit to promote drug abuse prevention, environmental cleanliness, school attendance, and peaceful inter-community coexistence.\\n"
            "3. **Reconciliation and Mediation:** When disputes arise in families or businesses, community members approach the Imam. Applying Quranic principles of justice and reconciliation (*Islaah*), disputes are resolved peacefully without expensive court litigation."
        ),
        "diagram_title": "The Four Pillars of the Mosque in Society",
        "svg_fn": get_svg_lesson_2,
        "table_title": "Functional Breakdown of the Mosque in Community Life",
        "table_headers": ["Dimension", "Specific Activities", "Social Impact"],
        "table_rows": [
            ["Spiritual", "5 daily prayers, Jumu'ah congregational prayer, Tahajjud", "Fosters mindfulness of Allah and emotional tranquility"],
            ["Educational", "Halaqah study circles, library facilities, evening tutoring", "Eliminates religious illiteracy and supports academic progress"],
            ["Welfare", "Zakat distribution, food relief baskets, water supply points", "Directly alleviates acute poverty and hunger in the locality"],
            ["Civic/Judicial", "Marital mediation, contract witness, conflict resolution", "Maintains neighborhood peace and reduces court litigation"]
        ],
        "scenario": (
            "Mr. Bilal, the Imam of Al-Amin Mosque in Mombasa, notices that several young people in the neighborhood are dropping out of school "
            "due to a lack of quiet study spaces and electricity at home. He works with the mosque committee to convert the mosque’s upper gallery into "
            "a 'community study hall' during non-prayer hours. They install solar lights, set up sturdy desks, and invite retired teachers from the congregation "
            "to offer free evening tutoring in mathematics and sciences. Within a year, students' grades improve noticeably, and the mosque becomes a hub of hope and academic ambition."
        ),
        "real_world": "Visit or reflect on a mosque in your local area. Write a short journal entry (3-5 sentences) describing its non-worship facilities. Does it have a library? A clean water tap accessible to travelers? A welfare office? Write down one way you, as a student, can help maintain the mosque, such as participating in a cleaning campaign or volunteering to organize books in its study corner.",
        "reflection": "How does standing shoulder to shoulder in prayer help eliminate prejudice and racism in our minds? Why is the Imam’s role as a counselor and mediator vital for maintaining peace in a Kenyan neighborhood?",
        "misconception": "Misconception: A mosque is solely for elderly worshipers and must remain locked outside of prayer times. Fact: The Prophet's Mosque in Medina was an active community center open all day for diplomatic meetings, youth education, medical shelter, and social welfare.",
        "image_title": "Riyadha Mosque in Lamu Old Town",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Riyadha_Mosque_Lamu.jpg/800px-Riyadha_Mosque_Lamu.jpg",
        "image_caption": "The historic Riyadha Mosque in Lamu, established in the late 19th century, remains an internationally renowned center of Islamic scholarship and community life.",
        "yt_title": "The Role and Architecture of the Mosque in Islamic History",
        "yt_id": "Fj-6N9Y4Plo",
        "yt_desc": "An insightful exploration into how the mosque functioned historically as the civic, educational, and spiritual center of Islamic civilization.",
        "mcq": {
            "question": "Which of the following best describes the historical and social role of the mosque (Masjid) in Islamic history, beyond being a place of worship?",
            "options": [
                "It was a restricted fortress used only during times of war.",
                "It was a private club reserved exclusively for wealthy rulers.",
                "It served as a community hub for education, charity, and social conflict resolution.",
                "It was a commercial marketplace where merchants sold goods for profit."
            ],
            "answer": "It served as a community hub for education, charity, and social conflict resolution.",
            "explanation": "Since the time of the Prophet Muhammad (PBUH) in Medina, the mosque has functioned as the central hub for spiritual, educational, welfare, and social mediation activities for the entire community."
        },
        "summary_content": "Mosques are sacred institutions dedicated to Allah, fulfilling spiritual, educational, charitable, and dispute-resolution roles. They promote absolute social equality and serve as the daily civic heart of Muslim communities in Kenya.",
        "key_points": [
            "Surah Al-Jinn (72:18) confirms that mosques are established solely for the worship of Allah.",
            "The mosque serves four primary roles: spiritual sanctuary, educational hub, charity center, and social mediation.",
            "Congregational prayer dismantles social barriers by placing all worshipers shoulder-to-shoulder in complete equality."
        ],
        "exit_ticket": "State three practical ways a local mosque can support vulnerable and impoverished members of a Kenyan neighborhood."
    },

    # LESSON 3 (7.3.3)
    {
        "order": 3,
        "code": "7.3.3",
        "title": "The role of madrasas in educational and moral development",
        "inquiry": "What is the primary role of the madrasa in teaching religious literacy and cultivating moral character (akhlaq)?",
        "hook": "If you wanted to learn how to swim safely, you would not just read a book about water; you would go to a pool with a skilled instructor who would guide your movements, correct your breathing, and build your confidence. A madrasa is like that pool, but instead of swimming, it is where we learn how to navigate the waters of life using the moral compass of the Qur'an and Sunnah. It is where we build the character shield that protects our integrity.",
        "concept_name": "The Role of the Madrasa in Moral Literacy",
        "concept_explanation": (
            "A **Madrasa** (Islamic educational institution) is dedicated to transmitting religious knowledge, spiritual values, and moral literacy to the younger generation.\\n\\n"
            "The core educational roles of the madrasa include:\\n"
            "1. **Scriptural Literacy:** Teaching students how to read, recite, and memorize the Qur'an correctly using proper pronunciation (*Tajweed*).\\n"
            "2. **Moral Education (*Akhlaq*):** Instilling foundational virtues such as honesty (*Amanah*), modesty (*Haya*), and respect for parents and elders.\\n"
            "3. **Legal Literacy (*Fiqh*):** Teaching the correct steps of physical purification (*Taharah/Wudu*) and ritual prayer (*Salat*).\\n"
            "4. **Cultural and Language Preservation:** Transmitting the Arabic language and preserving historical Islamic records and local Swahili heritage."
        ),
        "scripture_quran": "Seeking knowledge is an obligation upon every Muslim.",
        "scripture_quran_ref": "Sunan Ibn Majah (224)",
        "scripture_hadith": "The scholars are the heirs of the Prophets, and the Prophets do not leave behind gold or silver, but they leave behind knowledge. So whoever takes it has taken an abundant share.",
        "scripture_hadith_ref": "Sunan Abu Dawood (3641)",
        "deep_explanation": (
            "Let's look at how the madrasa builds a resilient, upright character in youth:\\n\\n"
            "1. **Character over Rote Memorization:** An effective madrasa does not simply train children to recite words mechanically without comprehension. It focuses on holistic character transformation. Every lesson on the Qur'an is paired with practical behavioral ethics—such as truthfulness, keeping promises, and avoiding backbiting.\\n"
            "2. **Preservation of Heritage in Kenya:** Historically, in Coastal and North Eastern Kenya, madrasas and mobile tree-shaded schools (*Duksi*) were the primary institutions that preserved religious literacy, Swahili-Arabic manuscripts, and cultural memory during periods of foreign colonial rule.\\n"
            "3. **Bridging Sacred and Secular Learning:** Modern Kenyan madrasas increasingly integrate life skills, digital literacy, and academic homework tutoring, preparing students to be balanced, productive citizens who contribute positively to national development."
        ),
        "diagram_title": "The Madrasa Growth Garden: Nurturing Character",
        "svg_fn": get_svg_lesson_3,
        "table_title": "Curriculum Dimensions of the Madrasa System",
        "table_headers": ["Subject Area", "Core Content", "Behavioral Outcome"],
        "table_rows": [
            ["Qur'an & Tajweed", "Recitation, memorization, rules of articulation", "Spiritual devotion, discipline, and linguistic accuracy"],
            ["Akhlaq (Ethics)", "Modesty, honesty, filial piety, anti-bullying", "Integrity, compassion, and respectful social interaction"],
            ["Fiqh (Jurisprudence)", "Purification (Wudu/Ghusl), Salat, Sawm, Zakat", "Correct worship and lawful conduct in personal life"],
            ["Sirah & History", "Life of Prophet (PBUH), early Kenyan Muslim history", "Inspirational leadership models and cultural identity"]
        ],
        "scenario": (
            "Zainab attends madrasa every Saturday morning at her local mosque. In today's lesson, her teacher, Ustadh Juma, does not just test their memorization "
            "of Surah Al-Hujurat. Instead, he holds a 'Dignity Discussion' about verse 11 (prohibiting mockery and offensive nicknames). He asks students to identify "
            "common insults heard in school and drafts a 'Zero-Mockery Charter'. When Zainab goes to secular school on Monday and observes classmates teasing a student "
            "with a torn backpack, she refuses to laugh, politely defends the student, and shares her extra stationery, translating her madrasa learning into practical courage."
        ),
        "real_world": "Reflect on a specific moral virtue you recently learned in your religious studies (such as modesty, trustworthiness, or kindness). Write down a plan to practice this virtue in your secular school this week. For example: if you choose Amanah (trustworthiness), commit to completing your homework honestly without copying, and promptly return any borrowed items to your classmates.",
        "reflection": "Why does the Prophet (PBUH) describe scholars as the 'heirs of the Prophets' rather than inheritors of material wealth? How does religious moral education in youth shield a society from social vices like corruption and crime?",
        "misconception": "Misconception: Madrasa education is irrelevant to modern academic success. Fact: By teaching memorization techniques, linguistic discipline, focus, and strict ethical accountability, madrasa training consistently enhances students' secular academic performance and character.",
        "image_title": "Students in an East African Islamic Study Circle",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Madrasa_students_reading_Quran.jpg/800px-Madrasa_students_reading_Quran.jpg",
        "image_caption": "Madrasa learners reading and memorizing the Qur'an under the guidance of an instructor, developing linguistic discipline and spiritual focus.",
        "yt_title": "The Pedagogy of Islamic Education and Moral Development",
        "yt_id": "6v7T5k3m1yQ",
        "yt_desc": "An educational analysis of how Islamic schooling balances scriptural literacy, intellectual discipline, and character transformation (Tarbiyah).",
        "mcq": {
            "question": "What is the primary spiritual and moral objective of a madrasa education?",
            "options": [
                "To train students to win athletic championships and awards.",
                "To teach scriptural literacy and translate those teachings into excellent moral character (Akhlaq).",
                "To encourage students to isolate themselves from the rest of Kenyan society.",
                "To teach students how to run commercial businesses for personal profit."
            ],
            "answer": "To teach scriptural literacy and translate those teachings into excellent moral character (Akhlaq).",
            "explanation": "While academic and language skills are valuable, the ultimate goal of a madrasa is to provide scriptural understanding that directly manifests as moral integrity, character, and responsible citizenship."
        },
        "summary_content": "Madrasas are educational institutions dedicated to teaching Qur'anic literacy, worship jurisprudence, and moral character (Akhlaq). They preserve Kenya's Islamic heritage and cultivate upright, disciplined citizens.",
        "key_points": [
            "Seeking knowledge is an obligation commanded upon every Muslim in Sunan Ibn Majah (224).",
            "Madrasa education balances scriptural literacy (Qur'an/Tajweed) with behavioral character (Akhlaq).",
            "Historically, coastal madrasas and pastoral Duksi preserved written texts and religious identity under colonial pressure."
        ],
        "exit_ticket": "Explain in your own words why a person's religious education is incomplete if it does not transform their daily behavior towards others."
    },

    # LESSON 4 (7.3.4)
    {
        "order": 4,
        "code": "7.3.4",
        "title": "The role of Muslim NGOs in community development",
        "inquiry": "How do Muslim Non-Governmental Organizations (NGOs) apply Islamic values to deliver humanitarian relief and long-term development in Kenya?",
        "hook": "Imagine a remote village facing a devastating, multi-year drought. The soil is dry, the crops have died, and the cows are weak. The nearest clean water source is a five-kilometer walk under a scorching sun. Suddenly, a team of professionals arrives in vehicles. They conduct surveys, drill a deep borehole powered by solar panels, and install clean water kiosks throughout the village. This life-saving work is the professional mission of Non-Governmental Organizations (NGOs) driven by Islamic values of mercy and social justice.",
        "concept_name": "Muslim NGOs and Structured Humanitarian Action",
        "concept_explanation": (
            "**Muslim NGOs** are structured, non-profit, non-governmental organizations that collect, manage, and implement charitable funds to support humanitarian relief and sustainable community development.\\n\\n"
            "The four primary areas of NGO action include:\\n"
            "1. **Emergency Humanitarian Relief:** Providing food hampers, clean water, medical supplies, and temporary shelters during floods, droughts, or fires.\\n"
            "2. **Sustainable Development:** Drilling solar-powered water boreholes, building schools, health clinics, and vocational centers.\\n"
            "3. **Orphan and Widow Sponsorship:** Providing structured monthly educational, nutritional, and medical support to vulnerable families.\\n"
            "4. **Advocacy and Peacebuilding:** Promoting social justice, interfaith harmony, environmental stewardship, and youth empowerment."
        ),
        "scripture_quran": "Take, [O, Muhammad], from their wealth a charity by which you purify them and cause them increase, and invoke [Allah 's blessings] upon them. Indeed, your invocations are reassurance for them.",
        "scripture_quran_ref": "Surah Al-Tawbah (9:103)",
        "scripture_hadith": "The most beloved of people to Allah are those who are most beneficial to people.",
        "scripture_hadith_ref": "Jami' at-Tirmidhi (3254)",
        "deep_explanation": (
            "Let's look at how Muslim NGOs work professionally in Kenya:\\n\\n"
            "1. **Motivated by Islamic Philosophy (*Sadaqah Jariyah*):** Their work is grounded in ongoing charity. When an NGO drills a solar borehole or builds a secondary school, they create an enduring source of reward for donors while empowering communities for generations.\\n"
            "2. **Professional Project Management:** Unlike informal street handouts, NGOs conduct rigorous baseline surveys, hydrogeological surveys, maintain auditable accounts, and coordinate with Kenya's national and county governments to ensure long-term durability.\\n"
            "3. **Inclusive Humanitarian Service:** True Muslim NGOs (such as Islamic Relief Kenya, Direct Aid, and the Muslim World League) operate under the Islamic principle of universal mercy (*Rahmah*). They deliver clean water, medical treatment, and emergency relief to all vulnerable human beings, regardless of tribe, race, or religious affiliation."
        ),
        "diagram_title": "The Muslim NGO Professional Project Cycle",
        "svg_fn": get_svg_lesson_4,
        "table_title": "Core Sectors of Muslim NGO Development Work",
        "table_headers": ["Sector", "Typical Projects", "Long-Term Impact"],
        "table_rows": [
            ["Water & Sanitation (WASH)", "Solar boreholes, water kiosks, hygiene training", "Eliminates waterborne disease; frees girls to attend school"],
            ["Education", "School construction, teacher training, bursaries", "Breaks intergenerational poverty through literacy and skills"],
            ["Healthcare", "Mobile clinics, maternity centers, cataract surgeries", "Reduces maternal/infant mortality in marginalized counties"],
            ["Livelihoods", "Microfinance grants, agricultural drip-irrigation", "Transitions vulnerable households from aid dependency to self-reliance"]
        ],
        "scenario": (
            "Following heavy seasonal floods in Budalangi, Western Kenya, a Muslim NGO coordinates with local county authorities and the Kenya Red Cross. "
            "Instead of sending arbitrary food sacks, they conduct an immediate needs assessment. Discovering that contaminated drinking water poses an imminent threat, "
            "they deploy a mobile water-purification truck, distribute 1,000 insecticide-treated mosquito nets, set up emergency treatment centers, and provide "
            "hygiene supplies to displaced mothers. This organized, professional intervention prevents a cholera outbreak and protects vulnerable lives."
        ),
        "real_world": "Write a short essay or class presentation on 'The Importance of Organized Charity in Community Development.' Highlight how a clean water borehole built by an organization improves girls' education (by eliminating the hours spent fetching water) and protects families from waterborne diseases. Suggest how your school’s youth club can coordinate a small stationery-collection project for local orphanages.",
        "reflection": "How does the concept of Sadaqah Jariyah motivate Muslims to invest in long-term infrastructure like schools and solar boreholes? Why must humanitarian aid be provided to all human beings regardless of their religious beliefs?",
        "misconception": "Misconception: Islamic charitable funds (Zakat and Sadaqah) can only be given to Muslims. Fact: While certain categories of Zakat have specific guidelines, general humanitarian charity (Sadaqah) is universally encouraged for all human beings and animals in need.",
        "image_title": "Community Solar Water Well Project",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Water_well_Africa_community.jpg/800px-Water_well_Africa_community.jpg",
        "image_caption": "A community water borehole providing clean, safe drinking water to rural households, eliminating waterborne diseases and empowering local agriculture.",
        "yt_title": "Sustainable Community Development and Humanitarian Aid in Africa",
        "yt_id": "x7n8kZ5aP0w",
        "yt_desc": "An educational look at how structured NGOs design, drill, and maintain sustainable solar-powered water infrastructure in arid regions.",
        "mcq": {
            "question": "Which of the following describes the unique benefit of utilizing organized Non-Governmental Organizations (NGOs) to distribute charity compared to individuals giving direct cash?",
            "options": [
                "NGOs only help people who belong to the same political party.",
                "NGOs use professional planning, assessments, and engineering to build long-term, sustainable water, health, and education systems.",
                "NGOs charge high interest rates to make a commercial profit.",
                "NGOs encourage people to become dependent on temporary aid forever."
            ],
            "answer": "NGOs use professional planning, assessments, and engineering to build long-term, sustainable water, health, and education systems.",
            "explanation": "Muslim NGOs utilize structured, professional systems to manage charity (Zakat/Sadaqah) efficiently, translating donations into lasting development projects (like boreholes and clinics) that build community self-reliance."
        },
        "summary_content": "Muslim NGOs manage charitable endowments to provide emergency relief, sustainable clean water, healthcare, and education. Grounded in Sadaqah Jariyah and universal mercy, they foster long-term self-reliance across Kenyan communities.",
        "key_points": [
            "Surah Al-Tawbah (9:103) commands the systematic collection and administration of charity for social purification.",
            "Muslim NGOs focus on four areas: disaster relief, sustainable infrastructure, orphan care, and social justice.",
            "Sadaqah Jariyah (continuous charity) provides an enduring theological basis for building schools, clinics, and boreholes."
        ],
        "exit_ticket": "State one long-term socio-economic benefit of installing a solar-powered water well in a dry rural village."
    },

    # LESSON 5 (7.3.5)
    {
        "order": 5,
        "code": "7.3.5",
        "title": "How institutions preserve Islamic values and heritage",
        "inquiry": "How do mosques, madrasas, and archives work together to preserve Islamic values, arts, and historical memory in Kenya?",
        "hook": "Imagine you are given a priceless, ancient glass lantern that has been lit and passed down through ten generations of your family. To keep it safe, you would not leave it out in the wind and rain; you would place it inside a secure, beautiful cabinet with glass doors, where the light can shine brightly for everyone to see while being completely protected from the storm. Our social and religious institutions are that protective cabinet for our values, our history, and our unique heritage.",
        "concept_name": "Preserving Islamic Values and Cultural Heritage",
        "concept_explanation": (
            "**Heritage Preservation** is the active protection, documentation, and transmission of historical artifacts, written knowledge, sacred architecture, and moral traditions across generations.\\n\\n"
            "Muslim institutions preserve Kenya's heritage across four dimensions:\\n"
            "1. **Preserving Written Knowledge:** Collecting, restoring, and archiving ancient handwritten manuscripts, historical letters, and Qur'ans in libraries.\\n"
            "2. **Preserving Sacred Architecture:** Maintaining historic coral-stone mosques, intricately carved wooden doors (*mihrabs*), and traditional minarets along the Coast.\\n"
            "3. **Preserving Moral and Social Values:** Practicing and teaching the community how to implement daily worship, charitable support, and ethical commerce (*Muamalat*).\\n"
            "4. **Preserving Swahili-Islamic Culture:** Transmitting classical Kiswahili literature, Islamic poetry, and traditional modest attire (**Kanzu**, **Hijab**, and proverb-printed **Lesos**)."
        ),
        "scripture_quran": "Indeed, it is We who sent down the Qur'an and indeed, We will be its guardian.",
        "scripture_quran_ref": "Surah Al-Hijr (15:9)",
        "scripture_hadith": "And We have certainly honored the children of Adam and carried them on land and sea and provided for them of the good things and preferred them over much of what We have created, with [definite] preference.",
        "scripture_hadith_ref": "Surah Al-Isra (17:70)",
        "deep_explanation": (
            "Let's look at how this preservation occurs in Kenya:\\n\\n"
            "1. **The Treasure of Lamu Archives:** Lamu’s ancient Riyadha Mosque and coastal archival collections contain handwritten manuscripts dating back over 300 years. These records document early Swahili-Arabic grammar, Islamic jurisprudence, regional poetry, and maritime contracts, proving the profound literacy of early Kenyan Muslims.\\n"
            "2. **Monuments of Sacred Architecture:** Historic mosques (such as Mombasa's Mandhry Mosque, built in 1507) feature coral-rag walls, mangrove timber ceilings, and decorative stucco arches. Maintaining these architectural treasures demonstrates how early Muslims adapted Islamic art to local materials and climate.\\n"
            "3. **Living Heritage:** When institutions teach honest trade ethics, marital reconciliation, and charitable trusts, they are preserving a 'living heritage' that ensures Kenyan society remains morally grounded and socially resilient."
        ),
        "diagram_title": "Four Dimensions of Islamic Heritage Preservation in Kenya",
        "svg_fn": get_svg_lesson_5,
        "table_title": "Physical and Non-Physical Dimensions of Islamic Heritage",
        "table_headers": ["Category", "Heritage Elements", "Custodial Institution"],
        "table_rows": [
            ["Manuscripts & Texts", "Ajami poetry, legal fatwas, 300-year-old Qur'ans", "Mosque archives, Riyadha library, National Museums of Kenya"],
            ["Sacred Architecture", "Coral-stone mosques, carved wooden doors, mihrabs", "Historic mosque committees, Lamu World Heritage Site"],
            ["Living Moral Values", "Honesty in trade (Amanah), modesty, dispute mediation", "Madrasas, Councils of Imams, family welfare boards"],
            ["Linguistic & Cultural", "Classical Kiswahili, Kanzu and Kofia, Leso proverbs", "Community cultural societies, local artisan guilds"]
        ],
        "scenario": (
            "During a school history trip to Lamu Old Town, Yusuf is amazed to visit the historic library inside Riyadha Mosque. "
            "The curator, Ustadh Ahmad, carefully uses white cotton gloves to show students a 150-year-old manuscript. It is a collection of Swahili poetry "
            "written in Arabic script (*Ajami*), explaining the prophetic biography (*Sirah*) in a coastal dialect. Yusuf realizes that without this dedicated "
            "mosque archive, this priceless chapter of Kenyan history would have decayed or been lost. He resolves to write his school history paper on 'The Written Heritage of the Swahili Coast'."
        ),
        "real_world": "Choose a traditional Islamic object or custom in your family or local community (such as a hand-woven prayer mat, an antique family Qur'an, a traditional Dallah coffee pot, or the wearing of Kanzu and Lesos during Eid). Research its background: where was it made, and what does it symbolize? Write a short 5-sentence reflection on how this object connects you to East Africa's Islamic history.",
        "reflection": "Why is it vital for a nation to protect and restore its historical monuments and ancient libraries? How does an understanding of past civilizations inspire young citizens to contribute positively to modern society?",
        "misconception": "Misconception: Islamic heritage in Kenya is solely imported from abroad and has no local African identity. Fact: Kenyan Islamic heritage represents a unique Swahili synthesis where Islamic values blended harmoniously with local African languages, materials (coral and mangrove), and customs.",
        "image_title": "Intricately Carved Swahili Wooden Door in Lamu",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Lamu_carved_wooden_door.jpg/800px-Lamu_carved_wooden_door.jpg",
        "image_caption": "A masterfully carved Swahili door in Lamu Old Town featuring traditional Islamic geometric patterns and Arabic calligraphic inscriptions.",
        "yt_title": "The Architectural and Cultural Heritage of Lamu Old Town",
        "yt_id": "m1R3Q8xYVzU",
        "yt_desc": "A UNESCO documentary on Lamu Old Town, the oldest and best-preserved Swahili settlement in East Africa, highlighting its living Islamic heritage.",
        "mcq": {
            "question": "How did institutions like Lamu's Riyadha Mosque preserve early East African history and Swahili-Islamic culture?",
            "options": [
                "By selling old historical artifacts to foreign tourists.",
                "By collecting, translating, and safeguarding ancient handwritten manuscripts, letters, and books of poetry in mosque libraries.",
                "By banning the use of local African languages in education.",
                "By encouraging the community to forget their past and focus only on modern technology."
            ],
            "answer": "By collecting, translating, and safeguarding ancient handwritten manuscripts, letters, and books of poetry in mosque libraries.",
            "explanation": "Riyadha Mosque and coastal libraries acted as custodians of heritage by preserving ancient handwritten manuscripts, letters, and poetry written in Arabic and Swahili scripts, protecting written history from decay."
        },
        "summary_content": "Muslim institutions safeguard Kenya's Islamic heritage through ancient manuscripts, coral architecture, living moral values, and cultural attire. Preserving this heritage strengthens cultural identity, historical literacy, and social unity.",
        "key_points": [
            "Heritage preservation protects written knowledge, sacred architecture, and living moral virtues.",
            "Lamu's Riyadha Mosque archives preserve 300+ year-old Swahili-Arabic (Ajami) manuscripts.",
            "Swahili-Islamic architecture, such as coral stone and carved wood, reflects the harmonious integration of faith with local Kenyan climate."
        ],
        "exit_ticket": "State two physical examples of Islamic heritage (such as architecture or clothing) found along the Kenyan Coast."
    },

    # LESSON 6 (7.3.6)
    {
        "order": 6,
        "code": "7.3.6",
        "title": "Visit/interview preparation: ethical research and observation",
        "inquiry": "What are the ethical rules, behavioral etiquettes, and preparation steps required when conducting a research visit to a sacred institution?",
        "hook": "Imagine you are a professional journalist invited to interview a national leader. You would not show up wearing sports clothes, shouting over them, taking photos of their private files without asking, or arriving late. You would prepare thoughtful, respectful questions, dress professionally, show polite manners, listen carefully, and write down their answers accurately. When we visit a mosque, madrasa, or community center to learn about its function, we must apply a professional and ethical protocol to ensure we represent our school and our faith with excellence.",
        "concept_name": "Ethical Fieldwork and Research Etiquette",
        "concept_explanation": (
            "An **Ethical Research Protocol** is a set of rules, behavioral manners (*Adab*), and professional procedures that govern how a student researcher gathers data, interacts with participants, and observes a community institution.\\n\\n"
            "The 'Four Pillars of a Respectful Visit' include:\\n"
            "1. **Modest Dress & Decorum:** Wearing clean, modest attire; removing shoes before entering prayer spaces; walking quietly; and greeting hosts with *Salam*.\\n"
            "2. **Informed Consent:** Obtaining formal permission before recording audio, capturing video, or taking photographs.\\n"
            "3. **Respectful Inquiry:** Drafting polite, open-ended, purposeful questions focused on community service rather than controversial debates.\\n"
            "4. **Objective Reporting (*Sidq*):** Documenting and presenting findings with complete honesty and truthfulness, never fabricating or distorting facts."
        ),
        "scripture_quran": "O you who have believed, do not enter houses other than your own until you have asked permission and greeted their inhabitants. That is best for you that you may remember.",
        "scripture_quran_ref": "Surah Al-Nur (24:27)",
        "scripture_hadith": "And speak to people good words...",
        "scripture_hadith_ref": "Surah Al-Baqarah (2:83)",
        "deep_explanation": (
            "Let's break down the 'Step-by-Step Field Visit Preparation Guide' for Grade 9 researchers:\\n\\n"
            "1. **STEP 1: The Request (Formal Communication):** Draft a polite letter through your school administration to the Mosque Committee or Madrasa head, explaining who you are, the educational purpose of your visit, and the requested date.\\n"
            "2. **STEP 2: Etiquette Calibration:** Familiarize yourself with the sanctity of the space. Understand that the prayer hall is a sanctuary of quiet reflection. Plan to sit respectfully without interrupting ongoing worship.\\n"
            "3. **STEP 3: Questionnaire Design:** Prepare 3 to 5 open-ended, functional questions. Avoid intrusive inquiries into private personal finances. Good examples include:\\n"
            "   - *What educational programs do you offer to the youth?*\\n"
            "   - *How does this institution assist orphans and vulnerable families?*\\n"
            "   - *What are the primary operational challenges you experience?*\\n"
            "4. **STEP 4: Consent & Child Protection:** Never photograph children's faces or record an administrator's voice without explicit, verified permission. This protects child safety and human dignity."
        ),
        "diagram_title": "Grade 9 Researcher's Ethical Fieldwork Protocol",
        "svg_fn": get_svg_lesson_6,
        "table_title": "Field Research Preparation Checklist",
        "table_headers": ["Phase", "Required Action", "Ethical Rationale"],
        "table_rows": [
            ["Pre-Visit", "Draft formal letter of request and prepare 3-5 questions", "Shows respect for institutional leadership's time and schedules"],
            ["On Arrival", "Remove shoes, dress modestly, greet staff with Salam", "Honors the sacred decorum (Adab) of the spiritual institution"],
            ["During Interview", "Ask permission before audio recording or photography", "Upholds informed consent and safeguards participant privacy"],
            ["Post-Visit", "Send thank-you note and write truthful, objective report", "Fulfills Amanah (trust) and integrity in academic reporting"]
        ],
        "scenario": (
            "Fariha’s class is organizing a field study visit to a local Muslim community clinic and orphanage run by an NGO. Some of her classmates "
            "take out their smartphones to take selfies with the orphan children to post on social media to show they are doing charity work. "
            "Fariha intervenes: 'Wait friends! Taking photos of vulnerable children without their consent and posting them online violates their dignity and privacy. "
            "Our ethical research protocol requires us to put phones away. Let’s interview the clinic supervisor about how they distribute medicine and tutor the children, "
            "record their answers in our notebooks, and prepare a professional report.' The students immediately recognize the wisdom and conduct an ethical visit."
        ),
        "real_world": "Draft a 'Field Research Plan' today. Choose a local institution (such as your school library, a neighborhood clinic, or a religious center). Write down: 1. How you will seek formal permission to visit, 2. Three specific, polite questions you will ask the administrator, and 3. Two ethical rules you will enforce during your visit to safeguard participant privacy and dignity.",
        "reflection": "Why does Surah Al-Nur (24:27) command us to seek permission before entering spaces that are not our own? How does preparing interview questions in advance show courtesy and respect to busy community leaders?",
        "misconception": "Misconception: In school field research, taking photos of anyone in public spaces is always acceptable without asking. Fact: Ethical research and Kenyan child protection laws strictly require informed consent before recording or photographing any individual, especially minors.",
        "image_title": "Student Researcher Conducting Field Observation",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Student_taking_field_notes.jpg/800px-Student_taking_field_notes.jpg",
        "image_caption": "A student researcher conducting respectful interviews and taking structured field notes with informed consent and academic decorum.",
        "yt_title": "Research Ethics and Community Interview Etiquette",
        "yt_id": "bFk3VwZ1p2g",
        "yt_desc": "A practical guide for secondary school students on conducting ethical fieldwork, maintaining privacy, and gathering objective research data.",
        "mcq": {
            "question": "You are conducting a research interview with a madrasa administrator. You want to record their voice on your phone to ensure you do not miss any details. What is the most ethical action to take?",
            "options": [
                "Secretly turn on your phone's voice recorder and place it in your pocket.",
                "Record the voice first, and then tell them about it after the interview is finished.",
                "Politely explain why you want to record, ask for their explicit permission, and only record if they agree.",
                "Demand that they allow you to record because you are doing a school project."
            ],
            "answer": "Politely explain why you want to record, ask for their explicit permission, and only record if they agree.",
            "explanation": "Ethical research requires informed consent—always explaining your purpose and getting explicit permission before recording audio, video, or taking photographs of any person."
        },
        "summary_content": "Conducting fieldwork at community institutions requires strict adherence to modest dress, informed consent, respectful inquiry, and truthful reporting. These ethics fulfill Quranic commands of permission and decorum.",
        "key_points": [
            "Surah Al-Nur (24:27) establishes the divine requirement to ask permission before entering spaces not your own.",
            "The four ethical pillars: modest decorum, informed consent, respectful inquiry, and objective reporting.",
            "Never record audio or photograph vulnerable children without verified, written or verbal permission."
        ],
        "exit_ticket": "State two polite, open-ended questions you would ask an Imam to understand the educational activities of his mosque."
    },

    # LESSON 7 (7.3.7)
    {
        "order": 7,
        "code": "7.3.7",
        "title": "Challenges facing Muslim institutions in Kenya",
        "inquiry": "What are the key resource, administrative, and social challenges that hinder Muslim institutions from fully serving communities in Kenya?",
        "hook": "Imagine a beautifully designed modern hospital that has highly skilled, compassionate doctors and nurses. However, the hospital lacks medicine, has no electricity or clean running water, the medical equipment is broken, and there is no record system to track patients. Even with the best intentions, the doctors cannot save lives effectively. In a similar way, our community institutions—mosques, madrasas, and charities—face serious challenges that hinder their noble missions. Let's study these challenges to understand how we can help.",
        "concept_name": "Institutional Challenges and Systemic Obstacles",
        "concept_explanation": (
            "**Institutional Challenges** are the internal and external obstacles that limit the efficiency, outreach, transparency, and sustainability of community organizations.\\n\\n"
            "The four primary challenges facing Kenyan Muslim institutions include:\\n"
            "1. **Financial and Resource Constraints:** Relying solely on unpredictable, voluntary donations, which makes paying regular teacher salaries or maintaining buildings difficult.\\n"
            "2. **Administrative and Governance Gaps:** Lack of professional accounting software, digital record-keeping, formal audits, and long-term strategic plans in committee boards.\\n"
            "3. **Youth and Community Apathy:** Low volunteerism and participation, leaving institutions stagnant without new ideas, digital skills, or energetic leadership.\\n"
            "4. **Socio-Economic and Educational Pressures:** Difficulty in updating curricula to integrate modern life skills, poverty in rural areas, and misrepresentation in external media."
        ),
        "scripture_quran": "O you who have believed, do not consume one another's wealth unjustly but only [in business] by mutual consent...",
        "scripture_quran_ref": "Surah An-Nisa (4:29)",
        "scripture_hadith": "Indeed, Allah commands you to act with justice, the doing of good, and liberality to kith and kin...",
        "scripture_hadith_ref": "Surah Al-Nahl (16:90)",
        "deep_explanation": (
            "Let's look at the direct consequences of these challenges on community development:\\n\\n"
            "1. **The Madrasa Salary Crisis:** Many rural and low-income madrasas in Kenya cannot afford to pay their teachers (*Asatidh*) a stable, living wage. Consequently, qualified, dedicated educators are forced to resign to seek other livelihoods, resulting in classroom closures and disrupted student learning.\\n"
            "2. **The Transparency Deficit:** When donation boxes are emptied and expended without published bookkeeping or independent audits, rumors of financial mismanagement inevitably emerge. Community trust erodes, causing donations to decline further and trapping the institution in poverty.\\n"
            "3. **The Marginalization of Youth and Women:** In some committees, leadership remains exclusive to an aging cohort that resists input from younger generations. Consequently, mosques fail to address youth challenges such as mental health, exam stress, and cyber literacy, prompting young people to disengage."
        ),
        "diagram_title": "Institutional Challenges: Stagnant vs. Empowered Systems",
        "svg_fn": get_svg_lesson_7,
        "table_title": "Matrix of Institutional Challenges and Their Consequences",
        "table_headers": ["Challenge Category", "Underlying Cause", "Direct Impact on Community"],
        "table_rows": [
            ["Financial Instability", "Total reliance on erratic Friday donations", "Teacher resignations, unfinished classrooms, lack of books"],
            ["Poor Record-Keeping", "Manual ledgers in single exercise books", "Loss of financial transparency, donor distrust, lost funds"],
            ["Youth Exclusion", "Boards dominated exclusively by elderly males", "Programs fail to address digital literacy, mental health, or sports"],
            ["Facility Neglect", "Zero maintenance reserve fund", "Leaking roofs, unsanitary washrooms, broken desks"]
        ],
        "scenario": (
            "Hussein notices that his local madrasa's library shelves are covered in dust, the textbooks are falling apart, and the washrooms are broken. "
            "He overhears frustrated parents complaining that the madrasa is poorly run and threatening to withdraw their children. "
            "Hussein consults the headteacher and discovers that the school has received almost no donations for six months because the treasury accounts "
            "were kept informally in a single handwritten notebook that went missing. When donors asked for accounts, the committee could not produce them, "
            "causing donors to freeze their contributions. Hussein realizes that administrative incompetence, rather than a lack of generosity, is crippling the school."
        ),
        "real_world": "Conduct a 'School Resource Audit' today. Look around your classroom or school compound. Identify one small operational challenge (such as a broken desk, wasted dripping water tap, or a disorganised library corner). Write down a short proposal (3 sentences) identifying: 1. The root cause of the issue, and 2. One practical, zero-cost way you and your classmates can volunteer to help resolve it.",
        "reflection": "How does a lack of financial transparency destroy donor trust in community organizations? Why is it essential for youth to be actively included in the administrative committees of our community centers?",
        "misconception": "Misconception: A community institution fails simply because its neighborhood is poor. Fact: Many institutions fail because of poor governance, lack of strategic planning, and absence of transparent accounting rather than absolute lack of wealth.",
        "image_title": "Community Meeting on Institutional Governance",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Community_meeting_planning_session.jpg/800px-Community_meeting_planning_session.jpg",
        "image_caption": "Community elders and youth meeting to review institutional challenges, financial accounts, and development strategies.",
        "yt_title": "Addressing Governance and Resource Challenges in Community Organizations",
        "yt_id": "tK4V8pL2w1g",
        "yt_desc": "An analytical seminar on diagnosing financial mismanagement, volunteer burnout, and governance gaps in grassroots civil society organizations.",
        "mcq": {
            "question": "Which of the following is a major administrative challenge that prevents some local madrasas and mosques from running sustainably in Kenya?",
            "options": [
                "Having too many volunteers offering free help.",
                "Rigid government laws that ban the practice of worship.",
                "Lack of professional financial systems, digital record-keeping, and long-term strategic planning.",
                "The complete absence of textbooks in the East African region."
            ],
            "answer": "Lack of professional financial systems, digital record-keeping, and long-term strategic planning.",
            "explanation": "A lack of professional administrative structures (such as transparent accounting, digital filing, and strategic planning) causes operational stagnation and undermines donor trust, hindering sustainability."
        },
        "summary_content": "Kenyan Muslim institutions face financial fragility, governance gaps, and youth apathy. Recognizing these obstacles is the first vital step toward establishing transparent, professionally managed community institutions.",
        "key_points": [
            "Financial reliance on erratic cash donations creates salary crises and high teacher turnover.",
            "Manual, un-audited bookkeeping erodes donor trust and community participation.",
            "Excluding youth and women prevents institutions from designing modern, impactful community programs."
        ],
        "exit_ticket": "List two negative consequences of failing to include young people in local mosque and madrasa administrative committees."
    },

    # LESSON 8 (7.3.8)
    {
        "order": 8,
        "code": "7.3.8",
        "title": "Proposing solutions to institutional challenges",
        "inquiry": "What are the practical, sustainable solutions we can propose to empower and modernize our community institutions?",
        "hook": "Imagine a group of dry-land villagers standing around a broken water well. They spend hours complaining about the heat, the dust, and how thirsty they are. Nothing changes. But then, a group of young people decides to act: they clear the debris, repair the broken pump handle, dig deeper into the soil, and establish a weekly community maintenance rota. Within days, clean water returns. We must be the active problem-solvers who build solutions for our community institutions, rather than just complaining about their challenges.",
        "concept_name": "Institutional Reform and Sustainable Endowments (Waqf)",
        "concept_explanation": (
            "**Institutional Reform (Capacity Building)** is the process of modernizing, professionalizing, and securing the financial and social survival of community organizations.\\n\\n"
            "Four practical, sustainable solutions include:\\n"
            "1. **Professional Capacity Building:** Training mosque and madrasa committee members in modern bookkeeping, digital accounting spreadsheets, and transparent annual audits.\\n"
            "2. **Sustainable Financial Models (*Waqf*):** Establishing income-generating endowments (such as commercial rental stalls, solar water kiosks, or agricultural farms) whose continuous profits fund institutional operations.\\n"
            "3. **Active Youth and Women's Committees:** Establishing dedicated sub-committees to harness digital skills, organize sports leagues, and deliver counseling.\\n"
            "4. **Curriculum Modernization:** Integrating digital literacy, STEM tutoring, and life skills into traditional madrasa curricula to equip learners for modern citizenship."
        ),
        "scripture_quran": "Indeed, Allah will not change the condition of a people until they change what is in themselves.",
        "scripture_quran_ref": "Surah Al-Ra'd (13:11)",
        "scripture_hadith": "And say, 'Do [deeds], for Allah will see your deeds, and [so will] His Messenger and the believers...'",
        "scripture_hadith_ref": "Surah Al-Tawbah (9:105)",
        "deep_explanation": (
            "Let's explore the powerful Islamic financial mechanism of **Waqf** (Endowment):\\n\\n"
            "1. **The Waqf Solution:** A *Waqf* is an inalienable asset (such as real estate, agricultural land, or commercial stalls) permanently donated to a charitable trust. The principal asset can never be sold, mortgaged, or gifted away, but 100% of the recurring profits (rent or crop sales) are dedicated to funding a social institution (paying teachers' salaries, purchasing student textbooks, or stocking clinics). This creates an independent self-reliance loop immune to seasonal donation slumps.\\n"
            "2. **Transparency as a Growth Engine:** When a mosque board publishes an audited financial sheet on its public bulletin board and online monthly, donor trust skyrockets. People give generously because they see the verifiable impact of every shilling.\\n"
            "3. **Youth Integration:** Establishing a Youth Wing allows young people to apply their ICT skills—creating social media announcements, organizing environmental clean-up days, and setting up digital donor tracking systems."
        ),
        "diagram_title": "The Waqf Self-Reliance Loop: Sustainable Community Finance",
        "svg_fn": get_svg_lesson_8,
        "table_title": "Strategic Interventions to Modernize Muslim Institutions",
        "table_headers": ["Problem Area", "Proposed Solution", "Implementation Action", "Expected Outcome"],
        "table_rows": [
            ["Unstable funding", "Waqf Endowment", "Build rental kiosks on mosque perimeter", "Guaranteed monthly income for teachers' salaries"],
            ["Un-audited accounts", "Digital Bookkeeping", "Adopt open accounting software & publish reports", "Restores donor confidence; increases contributions"],
            ["Youth disengagement", "Youth Sub-Committees", "Launch ICT tutoring, sports, and cleanups", "High youth participation; vibrant community life"],
            ["Curricular gap", "Curriculum Integration", "Add life skills, basic coding, and English literacy", "Balanced students succeeding academically and morally"]
        ],
        "scenario": (
            "To solve their madrasa’s chronic funding shortages and textbook deficit, the Sabaki Mosque Youth Committee proposes a 'Waqf Clean Water Initiative'. "
            "They secure permission from the Mosque board to install a commercial clean-water filtration kiosk on the mosque's outer perimeter facing the local market. "
            "They purchase bulk municipal water, filter it to drinking standards, and sell it at an affordable rate to market traders and residents. "
            "They allocate 100% of the kiosk’s net profits to pay stable, competitive monthly salaries to the madrasa teachers and purchase free textbooks for every student. "
            "Within three months, the madrasa achieves complete financial independence."
        ),
        "real_world": "Put on your 'Community Consultant' hat today. Imagine you have been hired to advise a struggling local youth center or madrasa facing declining enrollment. Draft a 3-step proposal to increase youth engagement: 1. One digital tool you will introduce (such as a community WhatsApp announcement group or poster), 2. One inclusive activity you will organize (such as a tree-planting day or football cup), and 3. How you will ensure everyone's input is valued.",
        "reflection": "How does Surah Al-Ra'd (13:11) motivate us to take proactive personal responsibility for reforming our community rather than waiting passively for others? What makes a Waqf endowment superior to short-term emergency appeals?",
        "misconception": "Misconception: Waqf can only be established by multi-millionaires donating massive buildings. Fact: Anyone can contribute to a pooled cash Waqf (Waqf Nuqud) or collectively fund small revenue assets like a water kiosk or agricultural plot.",
        "image_title": "Solar Powered Water Kiosk Built as a Sustainable Endowment",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Solar_water_pump_installation_Africa.jpg/800px-Solar_water_pump_installation_Africa.jpg",
        "image_caption": "A community-run solar water pumping system that generates commercial revenue while funding local education and sanitation.",
        "yt_title": "The Power of Waqf: Social Finance and Economic Resilience",
        "yt_id": "p4L8vW1yH0c",
        "yt_desc": "An informative lecture on the legal and economic mechanics of Islamic endowments (Waqf) and how they sustainably fund public welfare.",
        "mcq": {
            "question": "A local madrasa is struggling to survive because voluntary community donations are very low during dry seasons, and teachers are resigning. Which of the following is the most sustainable, source-grounded solution the committee should implement?",
            "options": [
                "Cancel all classes permanently and advise the children to study online.",
                "Establish a Waqf (such as renting out a mosque-owned commercial stall or orchard) to generate a stable, monthly income to fund salaries and school supplies.",
                "Demand that the struggling parents pay high, mandatory tuition fees during the drought.",
                "Take out a high-interest bank loan (Riba) to cover operational costs temporarily."
            ],
            "answer": "Establish a Waqf (such as renting out a mosque-owned commercial stall or orchard) to generate a stable, monthly income to fund salaries and school supplies.",
            "explanation": "Establishing a Waqf (charitable endowment) provides a stable, independent, and Shariah-compliant financial system that generates continuous revenue to fund community services without placing financial burdens on struggling parents or violating the prohibition of usury (Riba)."
        },
        "summary_content": "Modernizing Muslim institutions requires capacity building, transparent digital accounting, youth participation, and sustainable Waqf endowments. Grounded in Surah Al-Ra'd (13:11), community self-reliance begins with internal reform.",
        "key_points": [
            "Surah Al-Ra'd (13:11) emphasizes that positive community transformation requires proactive internal change.",
            "A Waqf is an inalienable endowment whose generated revenues permanently fund public social services.",
            "Publishing transparent financial audits restores donor confidence and community trust."
        ],
        "exit_ticket": "Explain in one clear sentence how establishing a Waqf system ensures that a community clinic remains operational during economic downturns."
    },

    # LESSON 9 (7.3.9)
    {
        "order": 9,
        "code": "7.3.9",
        "title": "Unit and strand synthesis: the sanctuary of Islamic heritage",
        "inquiry": "How do history, unity, and our community institutions work together to protect, preserve, and pass down Islamic heritage in Kenya?",
        "hook": "Imagine you are looking at a magnificent, high-tech glass dome built to protect a beautiful, lush green forest in the middle of a dry, hot desert. The dome consists of hundreds of overlapping steel beams, all locked together. If you remove even a few of these steel beams, the entire dome will collapse, and the dry desert wind will destroy the fragile forest. Our community institutions—mosques, madrasas, and charities—and our active commitment to unity are those steel beams. Together, they form the protective dome that safeguards the green forest of our faith and heritage in Kenya.",
        "concept_name": "The Sanctuary of Kenyan Islamic Heritage",
        "concept_explanation": (
            "**The Sanctuary of Islamic Heritage** is the integrated, cohesive system where regional history, social institutions, and active unity intersect to nurture an ethical, enlightened, and peaceful Kenyan society.\\n\\n"
            "The synthesis of Strand 7 brings together three vital pillars:\\n"
            "1. **The Four Historical Streams:** Recognizing how Islam flourished peacefully across Coastal trade centers, Western caravan alliances (Nabongo Mumia), Central railway artisan communities, and North Eastern pastoral networks.\\n"
            "2. **The Shield of Unity:** Applying *Islaah* (mediation) and *Ta'awun* (cooperation) as commanded in Surah Al-Hujurat to eradicate tribalism, sectarianism, and prejudice.\\n"
            "3. **The Custodial Institutions:** Supporting Mosques, Madrasas, and Muslim NGOs as the physical and moral custodians of sacred knowledge and social justice."
        ),
        "scripture_quran": "The believers are but brothers, so make peace between your brothers. And fear Allah that you may receive mercy.",
        "scripture_quran_ref": "Surah Al-Hujurat (49:10)",
        "scripture_hadith": "And say, 'Do [deeds], for Allah will see your deeds, and [so will] His Messenger and the believers...'",
        "scripture_hadith_ref": "Surah Al-Tawbah (9:105)",
        "deep_explanation": (
            "Let's review how this entire Strand connects directly to our contemporary Kenyan citizenship:\\n\\n"
            "1. **History Inspires National Citizenship:** Understanding that Islam arrived through trade in Lamu and Mombasa, through royal alliances in Mumias, and through railway builders in Nairobi and Nakuru demonstrates that Muslims are integral to Kenya's national history and founding fabric.\\n"
            "2. **Institutions Shape Character:** Our mosques and madrasas are not mere physical structures; they are character factories. By inculcating honesty (*Amanah*), modesty (*Haya*), and justice (*'Adl*), they produce upright citizens who reject corruption and serve the common good.\\n"
            "3. **Unity Fosters Peace and National Development:** By actively practicing intra-faith tolerance (*Adab al-Ikhtilaf*) and interfaith peace, Kenyan Muslims contribute to national stability, economic prosperity, and social harmony."
        ),
        "diagram_title": "Strand 7 Synthesis: The Sanctuary of Islamic Heritage in Kenya",
        "svg_fn": get_svg_lesson_9,
        "table_title": "Comprehensive Synthesis Matrix: Strand 7.0 Islamic Heritage",
        "table_headers": ["Strand Component", "Core Concepts Studied", "Civic / Faith Application"],
        "table_rows": [
            ["Sub-strand 7.1: Islam in Kenya", "Coast, Western (Mumia), Central, North Eastern", "Inspires patriotic pride and awareness of shared national history"],
            ["Sub-strand 7.2: Unity of Muslims", "Hablullah, Islaah, Ta'awun, Adab al-Ikhtilaf", "Overcomes tribalism and sectarianism; fosters brotherhood"],
            ["Sub-strand 7.3: Muslim Institutions", "Masajid, Madrasas, NGOs, Waqf endowments", "Sustains character education, social welfare, and heritage preservation"],
            ["Capstone Outcome", "The Sanctuary of Heritage", "Upright, ethical citizens building a harmonious, prosperous Kenya"]
        ],
        "scenario": (
            "Let's test our synthesized knowledge! Match each historical or institutional scenario below to its correct Strand concept:\\n"
            "1. An ancient coastal mosque library containing 300-year-old written Swahili manuscripts. (Answer: **Lamu / Riyadha Mosque / Heritage Preservation**)\\n"
            "2. The 19th-century diplomatic alliance that welcomed Muslim traders into the interior of Western Kenya. (Answer: **Nabongo Mumia / Wanga Kingdom**)\\n"
            "3. A solar-powered water kiosk whose commercial profits perpetually fund madrasa teacher salaries. (Answer: **Waqf / Sustainable Finance / NGO**)\\n"
            "4. Resolving a heated dispute between two student youth groups peacefully using Quranic dialogue. (Answer: **Islaah / Conflict Resolution / Unity**)"
        ),
        "real_world": "Draft your personal 'VLearn Character and Heritage Charter' today. Write down three practical commitments you will make this academic term to support community heritage and unity: 1. I will attend study sessions regularly to build moral literacy, 2. I will volunteer to clean or organize resources at my local mosque or school library, and 3. I will reject and counter rumors and tribal slurs in my school and social chats. Keep this charter in your study room.",
        "reflection": "How does a strong, united, and morally upright Muslim community contribute to the progress and security of the entire Kenyan nation? Which lesson across Strand 7 on Islamic Heritage did you find most inspiring, and why?",
        "misconception": "Misconception: Islamic heritage in Kenya belongs solely to coastal communities. Fact: Islamic heritage is an integral part of Kenya's entire national fabric, spanning the Coast, Western, Central, and North Eastern regions.",
        "image_title": "Panoramic View of Lamu Waterfront and Islamic Heritage",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Lamu_Old_Town_waterfront.jpg/800px-Lamu_Old_Town_waterfront.jpg",
        "image_caption": "The Lamu waterfront, showing the maritime architectural heritage that has connected East Africa to the wider Islamic world for over a thousand years.",
        "yt_title": "The Rich History and Civilisation of Islam in Kenya",
        "yt_id": "j8W4yQ9kM3c",
        "yt_desc": "A comprehensive historical documentary synthesizing the arrival, expansion, institutional architecture, and cultural heritage of Islam in Kenya.",
        "mcq": {
            "question": "Amina wants to write a comprehensive article for the school magazine about the history and contributions of Islam in Kenya. Applying the full synthesis of Strand 7, which of the following outlines the most accurate, balanced, and source-grounded framework she should use?",
            "options": [
                "Focus exclusively on the 8th-century Coast, claiming that Islam is purely a coastal heritage that has no relevance to other Kenyan regions.",
                "Describe the historical spread across all four regions (Coast, Western, Central, North Eastern), highlight how mosques, madrasas, and NGOs preserve these values, and explain how practicing unity (Islaah and Ta'awun) builds a cohesive Kenyan society.",
                "Argue that Muslim institutions should operate in isolation and avoid cooperating with other religious or civic groups.",
                "List only the names and dates of ancient rulers without explaining how their values apply to daily moral character today."
            ],
            "answer": "Describe the historical spread across all four regions (Coast, Western, Central, North Eastern), highlight how mosques, madrasas, and NGOs preserve these values, and explain how practicing unity (Islaah and Ta'awun) builds a cohesive Kenyan society.",
            "explanation": "This option represents a complete synthesis of the entire strand, covering the four geographical regions, the role of institutions in preservation, and the practical application of unity to foster national social cohesion, in perfect alignment with the KICD curriculum outcomes."
        },
        "summary_content": "Strand 7 synthesizes Kenya's Islamic history across four regions, the custodial role of mosques, madrasas, and NGOs, and the vital practice of unity. Together, they form the sanctuary of heritage that nurtures ethical and responsible citizens.",
        "key_points": [
            "Islamic heritage spans four key regions in Kenya: Coastal trade, Western caravan routes, Central railway artisans, and North Eastern pastoral communities.",
            "Institutions (masajid, madrasas, NGOs) act as physical and ethical sanctuaries preserving sacred knowledge and providing welfare.",
            "Practicing active unity (Islaah and Ta'awun) protects communities from division, contributing directly to national peace and prosperity."
        ],
        "exit_ticket": "Write one sentence explaining how you will apply the 'Shield of Unity' to help your school and neighborhood remain peaceful and cooperative this term."
    }
]


# ─────────────────────────────────────────────────────────────────────────────
# INGESTION EXECUTION FUNCTION
# ─────────────────────────────────────────────────────────────────────────────

@transaction.atomic
def ingest_topic_20():
    print("================================================================================")
    print("STARTING INGESTION FOR TOPIC 20: Muslim Institutions (ID: 360)")
    print("================================================================================")

    try:
        topic = Topic.objects.get(id=360)
    except Topic.DoesNotExist:
        print("ERROR: Topic ID 360 not found!")
        sys.exit(1)

    print(f"Target Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")
    print(f"Subject: {topic.subject.name} (ID: {topic.subject.id})")

    # Clean existing units for idempotency
    existing_units = LearningUnit.objects.filter(topic=topic)
    print(f"Found {existing_units.count()} existing learning units. Deleting for fresh ingestion...")
    existing_units.delete()

    created_units = 0
    created_lessons = 0
    created_blocks = 0
    created_assets = 0

    for ldata in LESSONS_DATA:
        order = ldata["order"]
        unit_name = f"Lesson {ldata['code']}: {ldata['title']}"
        print(f"\\nIngesting Lesson {order}/9: {unit_name}...")

        # 1. Create LearningUnit
        unit = LearningUnit.objects.create(
            topic=topic,
            name=unit_name,
            order=order,
            description=clean_text(ldata["concept_explanation"][:250])
        )
        created_units += 1

        # 2. Create Published Lesson
        lesson = Lesson.objects.create(
            topic=topic,
            learning_unit=unit,
            title=ldata["title"],
            status="published",
            version=1
        )
        created_lessons += 1

        # 3. Create Vector SVG Diagram Asset
        svg_xml = ldata["svg_fn"]()
        try:
            ET.fromstring(svg_xml)
        except Exception as e:
            print(f"ERROR: Invalid SVG XML for lesson {order}: {e}")
            raise e

        diagram_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="diagram",
            title=ldata["diagram_title"],
            url="",
            metadata={
                "svg_xml": svg_xml,
                "svg_content": svg_xml,
                "format": "svg",
                "theme": "#0f172a",
                "viewBox": "0 0 880 440"
            }
        )
        created_assets += 1

        # 4. Create Wikimedia Image Asset
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

    print("\\n================================================================================")
    print("INGESTION COMPLETE FOR TOPIC 20!")
    print(f"Created Units: {created_units} (Expected: 9)")
    print(f"Created Lessons: {created_lessons} (Expected: 9)")
    print(f"Created Blocks: {created_blocks} (Expected: 108)")
    print(f"Created Assets: {created_assets} (Expected: 27)")
    print("================================================================================")


if __name__ == "__main__":
    ingest_topic_20()
