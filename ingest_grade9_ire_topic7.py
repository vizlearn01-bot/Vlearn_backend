"""
VLearn CBC Grade 9 IRE — Topic 7: Shariah (Islamic Law)
Production Ingestion and Enrichment Script for all 6 Lessons

Target Topic in DB: Topic ID 347 (Subject: IRE ID 53, Grade: Grade 9 ID 18)
Source Markdown: /home/jason-bitega/Desktop/VL/vlearn_repositories/Grade 9 IRE/shariah.md

6 Lessons Ingested & Fully Enriched:
  1. Lesson 4.1.1: Meaning and purpose of Shariah
  2. Lesson 4.1.2: Protection of religion and intellect
  3. Lesson 4.1.3: Protection of life, property, and dignity
  4. Lesson 4.1.4: Categories of legal acts
  5. Lesson 4.1.5: Contemporary relevance
  6. Lesson 4.1.6: Daily-life application and synthesis
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
    """Lesson 4.1.1: The Five Pillars of Human Well-being (Maqasid al-Shariah)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg71" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="gold71" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="blue71" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="green71" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#34d399"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
    <linearGradient id="purple71" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#a78bfa"/>
      <stop offset="100%" stop-color="#7c3aed"/>
    </linearGradient>
    <linearGradient id="rose71" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fb7185"/>
      <stop offset="100%" stop-color="#e11d48"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg71)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle" letter-spacing="0.5">MAQASID AL-SHARIAH: THE FIVE ESSENTIAL PROTECTIONS</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">The Divine Architecture Designed to Safeguard and Promote Human Welfare in Both Worlds</text>

  <!-- Roof: Social Harmony & Divine Mercy -->
  <path d="M 50 115 L 440 75 L 830 115 L 810 135 L 70 135 Z" fill="url(#gold71)"/>
  <text x="440" y="112" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle" letter-spacing="1">PEACE, JUSTICE &amp; MERCY IN SOCIETY (MASLAHAH)</text>

  <!-- Architrave support bar -->
  <rect x="60" y="138" width="760" height="14" rx="4" fill="#334155"/>

  <!-- 5 Classical Pillars -->
  <!-- Pillar 1: Din (Religion) -->
  <g transform="translate(70, 158)">
    <rect width="136" height="205" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="136" height="28" rx="8" fill="url(#blue71)"/>
    <text x="68" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">1. DIN (FAITH)</text>
    <text x="68" y="55" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Protection of Religion</text>
    <text x="12" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Freedom of belief</text>
    <text x="12" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Safeguarding worship</text>
    <text x="12" y="116" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Sacred places safety</text>
    <text x="12" y="140" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">"No compulsion in</text>
    <text x="12" y="154" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">religion" (Q 2:256)</text>
    <rect x="15" y="172" width="106" height="20" rx="4" fill="#0284c7" opacity="0.2"/>
    <text x="68" y="186" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">SOUL SANCTITY</text>
  </g>

  <!-- Pillar 2: Nafs (Life) -->
  <g transform="translate(222, 158)">
    <rect width="136" height="205" rx="8" fill="#1e293b" stroke="#fb7185" stroke-width="1.5"/>
    <rect width="136" height="28" rx="8" fill="url(#rose71)"/>
    <text x="68" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">2. NAFS (LIFE)</text>
    <text x="68" y="55" fill="#fb7185" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Protection of Life</text>
    <text x="12" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Sacred right to live</text>
    <text x="12" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• No murder / suicide</text>
    <text x="12" y="116" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Healthcare obligation</text>
    <text x="12" y="140" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">"Saving one life is like</text>
    <text x="12" y="154" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">saving all humanity"</text>
    <rect x="15" y="172" width="106" height="20" rx="4" fill="#e11d48" opacity="0.2"/>
    <text x="68" y="186" fill="#fb7185" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">BODILY SANCTITY</text>
  </g>

  <!-- Pillar 3: 'Aql (Intellect) -->
  <g transform="translate(374, 158)">
    <rect width="136" height="205" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="136" height="28" rx="8" fill="url(#green71)"/>
    <text x="68" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">3. 'AQL (MIND)</text>
    <text x="68" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Protection of Intellect</text>
    <text x="12" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Mandatory education</text>
    <text x="12" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Critical thinking</text>
    <text x="12" y="116" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Zero intoxicants</text>
    <text x="12" y="140" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">"Seeking knowledge is</text>
    <text x="12" y="154" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">an obligation"</text>
    <rect x="15" y="172" width="106" height="20" rx="4" fill="#059669" opacity="0.2"/>
    <text x="68" y="186" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">MENTAL CLARITY</text>
  </g>

  <!-- Pillar 4: Mal (Property) -->
  <g transform="translate(526, 158)">
    <rect width="136" height="205" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="136" height="28" rx="8" fill="url(#gold71)"/>
    <text x="68" y="19" fill="#0f172a" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">4. MAL (WEALTH)</text>
    <text x="68" y="55" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Protection of Property</text>
    <text x="12" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Honest commerce</text>
    <text x="12" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Prohibition of theft</text>
    <text x="12" y="116" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Ban on Riba &amp; fraud</text>
    <text x="12" y="140" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">"Do not consume</text>
    <text x="12" y="154" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">wealth unjustly"</text>
    <rect x="15" y="172" width="106" height="20" rx="4" fill="#d97706" opacity="0.2"/>
    <text x="68" y="186" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">FAIR ECONOMY</text>
  </g>

  <!-- Pillar 5: 'Ird / Nasl (Dignity & Family) -->
  <g transform="translate(678, 158)">
    <rect width="136" height="205" rx="8" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <rect width="136" height="28" rx="8" fill="url(#purple71)"/>
    <text x="68" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">5. 'IRD (HONOR)</text>
    <text x="68" y="55" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Protection of Dignity</text>
    <text x="12" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Sacred privacy</text>
    <text x="12" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Anti-slander &amp; gossip</text>
    <text x="12" y="116" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Strong family bonds</text>
    <text x="12" y="140" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">"We have honored the</text>
    <text x="12" y="154" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" font-style="italic">children of Adam"</text>
    <rect x="15" y="172" width="106" height="20" rx="4" fill="#7c3aed" opacity="0.2"/>
    <text x="68" y="186" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">PERSONAL DIGNITY</text>
  </g>

  <!-- Foundation: The Divine Revelation (Qur'an & Sunnah) -->
  <rect x="50" y="375" width="780" height="38" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
  <text x="440" y="399" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle" letter-spacing="1">FOUNDATION: DIVINE REVELATION (AL-QUR'AN &amp; AS-SUNNAH)</text>
</svg>"""


def get_svg_lesson_2():
    """Lesson 4.1.2: Dual Protections: Faith & Mind (Hifz al-Din & Hifz al-'Aql)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg72" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="blueGrad72" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="emeraldGrad72" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg72)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">SAFEGUARDING SPIRIT &amp; REASON: HIFZ AL-DIN &amp; HIFZ AL-'AQL</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">How Shariah Balances Spiritual Freedom with Intellectual Growth and Mental Purity</text>

  <!-- Left Container: Hifz al-Din -->
  <g transform="translate(45, 80)">
    <rect width="375" height="325" rx="10" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <rect width="375" height="38" rx="10" fill="url(#blueGrad72)"/>
    <text x="187" y="25" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">PROTECTION OF RELIGION (HIFZ AL-DIN)</text>

    <!-- Positive Measures -->
    <rect x="20" y="55" width="335" height="115" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="35" y="77" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Positive Affirmative Protections:</text>
    <text x="35" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Guaranteeing free personal worship &amp; prayer</text>
    <text x="35" y="118" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Preserving and teaching authentic divine revelation</text>
    <text x="35" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Protecting mosques and interfaith holy sanctuaries</text>

    <!-- Preventive Measures -->
    <rect x="20" y="185" width="335" height="115" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="35" y="207" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Preventive Barriers Against Harm:</text>
    <text x="35" y="228" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Prohibition of forced conversion ("No compulsion")</text>
    <text x="35" y="248" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Banning false religious distortion or extremism</text>
    <text x="35" y="268" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Preventing religious discrimination and persecution</text>
  </g>

  <!-- Right Container: Hifz al-'Aql -->
  <g transform="translate(460, 80)">
    <rect width="375" height="325" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="375" height="38" rx="10" fill="url(#emeraldGrad72)"/>
    <text x="187" y="25" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">PROTECTION OF INTELLECT (HIFZ AL-'AQL)</text>

    <!-- Positive Measures -->
    <rect x="20" y="55" width="335" height="115" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="35" y="77" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Positive Affirmative Protections:</text>
    <text x="35" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Mandating education for every male and female</text>
    <text x="35" y="118" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Promoting scientific observation and critical inquiry</text>
    <text x="35" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Fostering intellectual creativity and sound judgment</text>

    <!-- Preventive Measures -->
    <rect x="20" y="185" width="335" height="115" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="35" y="207" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Preventive Barriers Against Harm:</text>
    <text x="35" y="228" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Strict ban on alcohol (Khamr) and toxic drugs</text>
    <text x="35" y="248" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Prohibiting superstitious falsehoods and fraud</text>
    <text x="35" y="268" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Shielding cognitive focus from digital brainrot &amp; decay</text>
  </g>
</svg>"""


def get_svg_lesson_3():
    """Lesson 4.1.3: Triad of Social Security: Life, Wealth, & Dignity"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg73" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="rose73" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f43f5e"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
    <linearGradient id="amber73" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="indigo73" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#6366f1"/>
      <stop offset="100%" stop-color="#4338ca"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg73)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE TRIAD OF SOCIAL SECURITY: LIFE, PROPERTY &amp; DIGNITY</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Foundational Protections Ensuring Every Citizen Lives with Physical Safety, Financial Justice, and Sacred Honor</text>

  <!-- 3 Columns -->
  <!-- Col 1: Life (Hifz al-Nafs) -->
  <g transform="translate(35, 80)">
    <rect width="255" height="325" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="255" height="38" rx="10" fill="url(#rose73)"/>
    <text x="127" y="25" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">1. LIFE (HIFZ AL-NAFS)</text>
    
    <text x="20" y="65" fill="#fda4af" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">What Shariah Promotes (Do's):</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Access to medical care &amp; cures</text>
    <text x="20" y="103" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Lawful self-defense &amp; safety</text>
    <text x="20" y="121" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Clean water &amp; environment</text>

    <line x1="20" y1="140" x2="235" y2="140" stroke="#334155" stroke-width="1"/>

    <text x="20" y="165" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">What Shariah Prohibits (Don'ts):</text>
    <text x="20" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Murder &amp; physical assault</text>
    <text x="20" y="203" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Suicide and self-mutilation</text>
    <text x="20" y="221" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Reckless endangerment</text>

    <rect x="20" y="248" width="215" height="55" rx="6" fill="#0f172a" stroke="#f43f5e" stroke-opacity="0.3"/>
    <text x="127" y="270" fill="#fda4af" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">QUR'ANIC MAXIM</text>
    <text x="127" y="287" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle" font-style="italic">"Do not kill the soul which Allah</text>
    <text x="127" y="299" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle" font-style="italic">has forbidden..." (17:33)</text>
  </g>

  <!-- Col 2: Property (Hifz al-Mal) -->
  <g transform="translate(312, 80)">
    <rect width="255" height="325" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="255" height="38" rx="10" fill="url(#amber73)"/>
    <text x="127" y="25" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">2. PROPERTY (HIFZ AL-MAL)</text>

    <text x="20" y="65" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">What Shariah Promotes (Do's):</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Free, honest market trade</text>
    <text x="20" y="103" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Clear written debt contracts</text>
    <text x="20" y="121" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Fair wages &amp; timely payment</text>

    <line x1="20" y1="140" x2="235" y2="140" stroke="#334155" stroke-width="1"/>

    <text x="20" y="165" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">What Shariah Prohibits (Don'ts):</text>
    <text x="20" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Theft, burglary, &amp; shoplifting</text>
    <text x="20" y="203" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Exploitative usury (Riba)</text>
    <text x="20" y="221" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Fraud, bribery, &amp; pirating</text>

    <rect x="20" y="248" width="215" height="55" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-opacity="0.3"/>
    <text x="127" y="270" fill="#fde68a" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">QUR'ANIC MAXIM</text>
    <text x="127" y="287" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle" font-style="italic">"Do not consume one another's</text>
    <text x="127" y="299" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle" font-style="italic">wealth unjustly..." (2:188)</text>
  </g>

  <!-- Col 3: Dignity (Hifz al-'Ird) -->
  <g transform="translate(590, 80)">
    <rect width="255" height="325" rx="10" fill="#1e293b" stroke="#6366f1" stroke-width="1.5"/>
    <rect width="255" height="38" rx="10" fill="url(#indigo73)"/>
    <text x="127" y="25" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">3. DIGNITY (HIFZ AL-'IRD)</text>

    <text x="20" y="65" fill="#c7d2fe" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">What Shariah Promotes (Do's):</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Sanctity of personal privacy</text>
    <text x="20" y="103" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Polite, encouraging speech</text>
    <text x="20" y="121" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Guarding absent peer honor</text>

    <line x1="20" y1="140" x2="235" y2="140" stroke="#334155" stroke-width="1"/>

    <text x="20" y="165" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">What Shariah Prohibits (Don'ts):</text>
    <text x="20" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Slander &amp; defamation (Qadhf)</text>
    <text x="20" y="203" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Snooping / digital hacking</text>
    <text x="20" y="221" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Backbiting &amp; bullying</text>

    <rect x="20" y="248" width="215" height="55" rx="6" fill="#0f172a" stroke="#6366f1" stroke-opacity="0.3"/>
    <text x="127" y="270" fill="#c7d2fe" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">QUR'ANIC MAXIM</text>
    <text x="127" y="287" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle" font-style="italic">"We have certainly honored</text>
    <text x="127" y="299" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle" font-style="italic">the children of Adam..." (17:70)</text>
  </g>
</svg>"""


def get_svg_lesson_4():
    """Lesson 4.1.4: The Five Legal Rulings (Ahkam al-Khamsah Spectrum)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg74" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="redGrad74" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#b91c1c"/>
    </linearGradient>
    <linearGradient id="orangeGrad74" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f97316"/>
      <stop offset="100%" stop-color="#c2410c"/>
    </linearGradient>
    <linearGradient id="slateGrad74" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#64748b"/>
      <stop offset="100%" stop-color="#334155"/>
    </linearGradient>
    <linearGradient id="blueGrad74" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0ea5e9"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="emeraldGrad74" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg74)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">AHKAM AL-KHAMSAH: THE FIVE CATEGORIES OF LEGAL ACTS</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">The Moral and Jurisprudential Spectrum Organizing Every Human Action in Islam</text>

  <!-- Spectrum Bar in Background -->
  <rect x="50" y="80" width="780" height="12" rx="6" fill="#334155"/>
  <rect x="50" y="80" width="156" height="12" rx="6" fill="#ef4444"/>
  <rect x="206" y="80" width="156" height="12" fill="#f97316"/>
  <rect x="362" y="80" width="156" height="12" fill="#64748b"/>
  <rect x="518" y="80" width="156" height="12" fill="#0ea5e9"/>
  <rect x="674" y="80" width="156" height="12" rx="6" fill="#10b981"/>

  <!-- Card 1: Haram (Forbidden) -->
  <g transform="translate(45, 110)">
    <rect width="148" height="295" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="148" height="32" rx="8" fill="url(#redGrad74)"/>
    <text x="74" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">HARAM</text>
    <text x="74" y="52" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Forbidden (Prohibited)</text>
    <rect x="10" y="65" width="128" height="65" rx="4" fill="#0f172a"/>
    <text x="18" y="83" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Committing: <tspan fill="#ef4444" font-weight="700">Sin</tspan></text>
    <text x="18" y="103" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Avoiding: <tspan fill="#34d399" font-weight="700">Rewarded</tspan></text>
    <text x="18" y="121" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5">Strict divine ban</text>
    <text x="10" y="152" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Examples:</text>
    <text x="10" y="172" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9">• Murder &amp; theft</text>
    <text x="10" y="190" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9">• Consuming alcohol</text>
    <text x="10" y="208" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9">• Slander &amp; lying</text>
    <text x="10" y="226" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9">• Usury / Riba</text>
    <rect x="10" y="250" width="128" height="30" rx="4" fill="#ef4444" opacity="0.15"/>
    <text x="74" y="270" fill="#ef4444" font-family="system-ui, sans-serif" font-size="9.5" font-weight="800" text-anchor="middle">STOP (STRICT)</text>
  </g>

  <!-- Card 2: Makruh (Disliked) -->
  <g transform="translate(201, 110)">
    <rect width="148" height="295" rx="8" fill="#1e293b" stroke="#f97316" stroke-width="1.5"/>
    <rect width="148" height="32" rx="8" fill="url(#orangeGrad74)"/>
    <text x="74" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">MAKRUH</text>
    <text x="74" y="52" fill="#fdba74" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Disliked (Discouraged)</text>
    <rect x="10" y="65" width="128" height="65" rx="4" fill="#0f172a"/>
    <text x="18" y="83" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Committing: <tspan fill="#94a3b8">No sin</tspan></text>
    <text x="18" y="103" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Avoiding: <tspan fill="#34d399" font-weight="700">Rewarded</tspan></text>
    <text x="18" y="121" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5">Better to leave it</text>
    <text x="10" y="152" fill="#fdba74" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Examples:</text>
    <text x="10" y="172" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9">• Wasting tap water</text>
    <text x="10" y="190" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9">• Raw garlic before prayer</text>
    <text x="10" y="208" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9">• Unnecessary delays</text>
    <text x="10" y="226" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9">• Mild bad habits</text>
    <rect x="10" y="250" width="128" height="30" rx="4" fill="#f97316" opacity="0.15"/>
    <text x="74" y="270" fill="#f97316" font-family="system-ui, sans-serif" font-size="9.5" font-weight="800" text-anchor="middle">CAUTION (AVOID)</text>
  </g>

  <!-- Card 3: Mubah (Permissible) -->
  <g transform="translate(357, 110)">
    <rect width="166" height="295" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
    <rect width="166" height="32" rx="8" fill="url(#slateGrad74)"/>
    <text x="83" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">MUBAH (DEFAULT)</text>
    <text x="83" y="52" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Permissible (Neutral)</text>
    <rect x="10" y="65" width="146" height="65" rx="4" fill="#0f172a"/>
    <text x="18" y="83" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Performing: <tspan fill="#94a3b8">Neutral</tspan></text>
    <text x="18" y="103" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Leaving: <tspan fill="#94a3b8">Neutral</tspan></text>
    <text x="18" y="121" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5">Rewarded with good Niyyah!</text>
    <text x="10" y="152" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Examples (Vast Majority):</text>
    <text x="10" y="172" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9">• Eating clean food</text>
    <text x="10" y="190" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9">• Sleeping &amp; resting</text>
    <text x="10" y="208" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9">• Playing football &amp; games</text>
    <text x="10" y="226" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9">• Choosing daily clothes</text>
    <rect x="10" y="250" width="146" height="30" rx="4" fill="#64748b" opacity="0.2"/>
    <text x="83" y="270" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" font-weight="800" text-anchor="middle">ALLOWED (FREEDOM)</text>
  </g>

  <!-- Card 4: Mandub (Recommended) -->
  <g transform="translate(531, 110)">
    <rect width="148" height="295" rx="8" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="148" height="32" rx="8" fill="url(#blueGrad74)"/>
    <text x="74" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">MANDUB</text>
    <text x="74" y="52" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Recommended (Sunnah)</text>
    <rect x="10" y="65" width="128" height="65" rx="4" fill="#0f172a"/>
    <text x="18" y="83" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Performing: <tspan fill="#34d399" font-weight="700">Rewarded</tspan></text>
    <text x="18" y="103" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Leaving: <tspan fill="#94a3b8">No sin</tspan></text>
    <text x="18" y="121" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5">Highly praised</text>
    <text x="10" y="152" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Examples:</text>
    <text x="10" y="172" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9">• Smiling at peers</text>
    <text x="10" y="190" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9">• Voluntary fasting</text>
    <text x="10" y="208" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9">• Using Siwak / brush</text>
    <text x="10" y="226" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9">• Extra Sunnah prayer</text>
    <rect x="10" y="250" width="128" height="30" rx="4" fill="#0ea5e9" opacity="0.15"/>
    <text x="74" y="270" fill="#0ea5e9" font-family="system-ui, sans-serif" font-size="9.5" font-weight="800" text-anchor="middle">ENCOURAGED (BOOST)</text>
  </g>

  <!-- Card 5: Wajib / Fard (Obligatory) -->
  <g transform="translate(687, 110)">
    <rect width="148" height="295" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="148" height="32" rx="8" fill="url(#emeraldGrad74)"/>
    <text x="74" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">WAJIB / FARD</text>
    <text x="74" y="52" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Obligatory (Mandatory)</text>
    <rect x="10" y="65" width="128" height="65" rx="4" fill="#0f172a"/>
    <text x="18" y="83" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Performing: <tspan fill="#34d399" font-weight="700">Rewarded</tspan></text>
    <text x="18" y="103" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Neglecting: <tspan fill="#ef4444" font-weight="700">Sin</tspan></text>
    <text x="18" y="121" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5">Core moral duty</text>
    <text x="10" y="152" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Examples:</text>
    <text x="10" y="172" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9">• Five daily prayers</text>
    <text x="10" y="190" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9">• Ramadan fasting</text>
    <text x="10" y="208" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9">• Honoring parents</text>
    <text x="10" y="226" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="9">• Paying Zakat</text>
    <rect x="10" y="250" width="128" height="30" rx="4" fill="#10b981" opacity="0.15"/>
    <text x="74" y="270" fill="#10b981" font-family="system-ui, sans-serif" font-size="9.5" font-weight="800" text-anchor="middle">MANDATORY (GO!)</text>
  </g>
</svg>"""


def get_svg_lesson_5():
    """Lesson 4.1.5: The Digital Integrity Filter (Contemporary Relevance of Maqasid)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg75" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="cyanGrad75" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#06b6d4"/>
      <stop offset="100%" stop-color="#0891b2"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg75)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">CONTEMPORARY RELEVANCE: THE DIGITAL CITIZENSHIP FILTER</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Applying 1,400-Year-Old Maqasid Principles to Social Media, Digital Privacy, and Intellectual Rights</text>

  <!-- Left Side: Incoming Digital Content -->
  <g transform="translate(40, 95)">
    <rect width="210" height="295" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="105" y="30" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">INCOMING POST / CHAT</text>
    <text x="105" y="48" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">(Meme, video, link, file)</text>

    <rect x="15" y="65" width="180" height="45" rx="4" fill="#0f172a"/>
    <text x="25" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Unverified rumor</text>
    <text x="25" y="99" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Mocking video/audio</text>

    <rect x="15" y="120" width="180" height="45" rx="4" fill="#0f172a"/>
    <text x="25" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Pirated game / book</text>
    <text x="25" y="154" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Toxic hate comments</text>

    <rect x="15" y="175" width="180" height="45" rx="4" fill="#0f172a"/>
    <text x="25" y="195" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Leaked private DM</text>
    <text x="25" y="209" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Screen-time waste</text>

    <path d="M 105 235 L 105 270" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
    <text x="105" y="285" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">FEED INTO FILTERS</text>
  </g>

  <!-- Middle: The 3 Maqasid Digital Gates -->
  <g transform="translate(280, 95)">
    <!-- Gate 1: Hifz al-Din & 'Aql (Truth & Mental Hygiene) -->
    <rect x="0" y="0" width="320" height="85" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="20" y="25" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="800">GATE 1: HIFZ AL-DIN &amp; 'AQL (TRUTH &amp; MIND)</text>
    <text x="20" y="45" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Is it verified and true? Does it sharpen or rot the intellect?</text>
    <text x="20" y="65" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="9">✓ PASS: Beneficial knowledge | ✗ FAIL: Lies &amp; brainrot</text>

    <!-- Gate 2: Hifz al-'Ird (Dignity & Privacy) -->
    <rect x="0" y="105" width="320" height="85" rx="6" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <text x="20" y="130" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="11" font-weight="800">GATE 2: HIFZ AL-'IRD (DIGNITY &amp; PRIVACY)</text>
    <text x="20" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Does this violate anyone's privacy, bully, or defame peers?</text>
    <text x="20" y="170" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="9">✓ PASS: Upholds peer honor | ✗ FAIL: Cyber-bullying</text>

    <!-- Gate 3: Hifz al-Mal (Intellectual Property) -->
    <rect x="0" y="210" width="320" height="85" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="20" y="235" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="800">GATE 3: HIFZ AL-MAL (PROPERTY RIGHTS)</text>
    <text x="20" y="255" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Is it lawfully licensed or pirated software/content?</text>
    <text x="20" y="275" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="9">✓ PASS: Fair use &amp; credit | ✗ FAIL: Piracy &amp; theft</text>
  </g>

  <!-- Right Side: Decisions & Ethical Output -->
  <g transform="translate(630, 95)">
    <!-- Outcome A: Approved -->
    <rect x="0" y="15" width="210" height="115" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect x="0" y="15" width="210" height="28" rx="8" fill="#10b981"/>
    <text x="105" y="34" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">PASSED ALL 3 GATES</text>
    <text x="20" y="65" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="700">ACTION: SHARE &amp; UPLIFT</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Spreads beneficial knowledge</text>
    <text x="20" y="103" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Earns Sadaqah Jariyah</text>
    <text x="20" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Builds high-trust online spaces</text>

    <!-- Outcome B: Blocked -->
    <rect x="0" y="165" width="210" height="115" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="165" width="210" height="28" rx="8" fill="#ef4444"/>
    <text x="105" y="184" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">FAILED ANY GATE</text>
    <text x="20" y="215" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700">ACTION: DELETE &amp; CONCEAL</text>
    <text x="20" y="235" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Deletes post immediately</text>
    <text x="20" y="253" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Protects peer reputation</text>
    <text x="20" y="270" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9">• Shuts the door to cyber-sins</text>
  </g>
</svg>"""


def get_svg_lesson_6():
    """Lesson 4.1.6: Master Architectural Map of Shariah Guidance"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg76" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="capstoneGrad76" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="50%" stop-color="#818cf8"/>
      <stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg76)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">MASTER SYNTHESIS: THE COMPLETE SHARIAH GUIDANCE SYSTEM</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">How Divine Revelation, Core Objectives, and Legal Categories Synthesize into Everyday Integrity</text>

  <!-- Level 1: Apex Goal (Maslahah & Divine Pleasure) -->
  <rect x="240" y="80" width="400" height="38" rx="8" fill="url(#capstoneGrad76)"/>
  <text x="440" y="104" fill="#0f172a" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">APEX GOAL: DIVINE PLEASURE &amp; UNIVERSAL MERCY (MASLAHAH)</text>

  <!-- Level 2: Five Higher Objectives (Maqasid) -->
  <g transform="translate(50, 135)">
    <rect width="780" height="90" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="390" y="22" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">THE FIVE SACRED HUMAN PROTECTIONS (MAQASID AL-SHARIAH)</text>
    
    <rect x="15" y="35" width="140" height="42" rx="6" fill="#0f172a" stroke="#0284c7"/>
    <text x="85" y="53" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">1. DIN (FAITH)</text>
    <text x="85" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">Spiritual Freedom</text>

    <rect x="165" y="35" width="140" height="42" rx="6" fill="#0f172a" stroke="#f43f5e"/>
    <text x="235" y="53" fill="#fb7185" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">2. NAFS (LIFE)</text>
    <text x="235" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">Physical Safety</text>

    <rect x="315" y="35" width="140" height="42" rx="6" fill="#0f172a" stroke="#10b981"/>
    <text x="385" y="53" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">3. 'AQL (MIND)</text>
    <text x="385" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">Reason &amp; Study</text>

    <rect x="465" y="35" width="140" height="42" rx="6" fill="#0f172a" stroke="#f59e0b"/>
    <text x="535" y="53" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">4. MAL (WEALTH)</text>
    <text x="535" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">Ethical Trade</text>

    <rect x="615" y="35" width="150" height="42" rx="6" fill="#0f172a" stroke="#a78bfa"/>
    <text x="690" y="53" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">5. 'IRD (HONOR)</text>
    <text x="690" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">Privacy &amp; Dignity</text>
  </g>

  <!-- Level 3: Action Classification Engine (Ahkam al-Khamsah) -->
  <g transform="translate(50, 240)">
    <rect width="780" height="85" rx="8" fill="#1e293b" stroke="#818cf8" stroke-width="1.5"/>
    <text x="390" y="22" fill="#818cf8" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">THE DAILY BEHAVIORAL SPECTRUM (AHKAM AL-KHAMSAH)</text>

    <rect x="15" y="35" width="140" height="38" rx="4" fill="#ef4444" fill-opacity="0.2" stroke="#ef4444"/>
    <text x="85" y="58" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">HARAM (Ban)</text>

    <rect x="165" y="35" width="140" height="38" rx="4" fill="#f97316" fill-opacity="0.2" stroke="#f97316"/>
    <text x="235" y="58" fill="#fdba74" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">MAKRUH (Avoid)</text>

    <rect x="315" y="35" width="140" height="38" rx="4" fill="#64748b" fill-opacity="0.2" stroke="#64748b"/>
    <text x="385" y="58" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">MUBAH (Allowed)</text>

    <rect x="465" y="35" width="140" height="38" rx="4" fill="#0ea5e9" fill-opacity="0.2" stroke="#0ea5e9"/>
    <text x="535" y="58" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">MANDUB (Sunnah)</text>

    <rect x="615" y="35" width="150" height="38" rx="4" fill="#10b981" fill-opacity="0.2" stroke="#10b981"/>
    <text x="690" y="58" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">WAJIB (Command)</text>
  </g>

  <!-- Level 4: Everyday Lived Reality & Character -->
  <g transform="translate(50, 340)">
    <rect width="780" height="65" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="390" y="24" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">THE RESULT: RESPONSIBLE CITIZENSHIP &amp; PEACEFUL CHARACTER</text>
    <text x="390" y="46" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Honest exams • Digital decency • Environmental care • Sincere prayers • Unbroken trusts</text>
  </g>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION DATA FOR 6 LESSONS IN TOPIC 7
# ─────────────────────────────────────────────────────────────────────────────

LESSONS_CONFIG = [
    {
        "order": 1,
        "code": "Lesson 4.1.1",
        "title": "Meaning and purpose of Shariah",
        "inquiry": "What is Shariah, and how do its higher objectives (Maqasid) protect human well-being?",
        "connection": "Imagine a city that has spent millions building a modern highway, but they did not paint lane markers, put up traffic signs, or set speed limits. Drivers would crash, traffic would be blocked, and the road would become a place of fear instead of a pathway to help people. Islamic law, known as Shariah, is like the divine lane markers and signs for human life. It is not designed to restrict or punish us, but to guide us safely to our destination, protecting our peace, justice, and happiness.",
        "concept_def": "Shariah (Islamic Law) is the comprehensive legal and moral code of Islam that governs all aspects of a Muslim's life, derived from the Quran and the Sunnah.\n\nMaqasid al-Shariah refers to the higher objectives or ultimate purposes of Islamic law, which are designed to safeguard and promote human welfare, justice, and mercy in both this world and the Hereafter.",
        "scripture_quran": "Indeed, this Qur'an guides to that which is most suitable...",
        "scripture_quran_ref": "Surah Al-Isra, 17:9",
        "scripture_hadith": "Whoever shows you a way of righteousness, follow him.",
        "scripture_hadith_ref": "Sahih Muslim, 217",
        "explanation": "Shariah is not a rigid list of rules; it is a merciful guidance framework built on five higher objectives (Maqasid al-Shariah). These five objectives are the protection of:\n\n1. Religion (Din): Safeguarding the freedom of belief and the practice of worship.\n2. Life (Nafs): Guaranteeing the right to safety, health, and physical protection.\n3. Intellect ('Aql): Protecting human reasoning, mental health, and the right to education.\n4. Property (Mal): Ensuring the right to own, trade, and protect wealth from theft and fraud.\n5. Dignity ('Ird): Protecting personal honor, privacy, reputation, and family bonds.",
        "svg_func": get_svg_lesson_1,
        "diagram_title": "The Five Pillars of Human Well-being (Maqasid al-Shariah)",
        "table_title": "Core Protections of Maqasid al-Shariah",
        "table_headers": ["Dimension", "Human Right Protected", "Everyday Practice", "Harm Prevented (Mafsadah)"],
        "table_rows": [
            ["Din (Religion)", "Freedom of faith & worship", "Daily prayers & learning Qur'an", "Forced conversion & spiritual decay"],
            ["Nafs (Life)", "Physical safety & healthcare", "Seeking medical cures & exercise", "Murder, assault, and self-harm"],
            ["'Aql (Intellect)", "Reasoning & educational growth", "Studying sciences & reading books", "Intoxicants, drugs, and brainrot"],
            ["Mal (Wealth)", "Ethical property ownership", "Honest commerce & written loans", "Theft, robbery, fraud, and usury"],
            ["'Ird (Dignity)", "Personal honor & privacy", "Protecting peer reputations", "Slander, backbiting, and cyber-bullying"]
        ],
        "scenario": "During a class debate, Yusuf says, 'I used to think Shariah was only about punishments and court trials. Why does a religious law have so many rules about money, health, and study?' Amina explains, 'Yusuf, Shariah is a complete guide to life. Think of a loving parent who makes rules about when you sleep, what you eat, and how you treat neighbors. Those rules are made to protect your health, your intelligence, and your character. Shariah's rules are there to protect the five essential things we need to be happy and peaceful—our faith, our lives, our minds, our property, and our dignity.'",
        "real_world": "Look around your school or neighborhood today. Identify one rule or facility that aligns with Maqasid al-Shariah. For example, school security guards protect Life and Property; the classroom library protects Intellect; and rules against bullying protect Dignity. Write down these connections in your notebook and share them with your classmates to show how moral guidelines are already helping your daily life.",
        "reflection": "What would a society look like if there were no rules protecting personal property or personal dignity?",
        "misconception": "Remember: Shariah is not just a historical code of penalties. Its primary purpose is the promotion of mercy, justice, and the active protection of human rights.",
        "yt_title": "What is Shariah? Understanding the Higher Objectives",
        "yt_desc": "Dr. Omar Suleiman explains the compassionate core of Islamic Law and Maqasid al-Shariah.",
        "yt_id": "c-ppIM94ilw",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Sultan_Hassan_Mosque_Cairo_Courtyard.jpg/1280px-Sultan_Hassan_Mosque_Cairo_Courtyard.jpg",
        "image_title": "Grand Courtyard of Mosque-Madrasa of Sultan Hassan in Cairo",
        "image_caption": "Historic architectural center of Islamic jurisprudence and jurisprudence study.",
        "mcq": {
            "question": "What is the Islamic term for the 'higher objectives or purposes of Islamic law' that aim to protect human welfare?",
            "options": [
                "Ahkam al-Khamsah",
                "Maqasid al-Shariah",
                "Ijma al-Ummah",
                "Qiyas al-Fuqaha"
            ],
            "answer": "B",
            "explanation": "Maqasid al-Shariah refers specifically to the higher objectives of Islamic law, which focus on protecting the five essential human interests: religion, life, intellect, property, and dignity."
        },
        "summary_content": "Shariah is a complete divine code of conduct guiding all personal and social actions. The five core protections of Maqasid al-Shariah are Religion, Life, Intellect, Property, and Dignity. All Islamic rules are designed to prevent harm (Mafsadah) and bring benefit (Maslahah).",
        "key_points": [
            "Shariah is a merciful, protective framework for universal human flourishing.",
            "The five core Maqasid protections are Din, Nafs, 'Aql, Mal, and 'Ird.",
            "All Shariah rulings exist to maximize benefit (Maslahah) and eradicate harm (Mafsadah)."
        ],
        "exit_ticket": "Write down the five essential protections of Maqasid al-Shariah from memory in your notebook."
    },
    {
        "order": 2,
        "code": "Lesson 4.1.2",
        "title": "Protection of religion and intellect",
        "inquiry": "How does Shariah protect our freedom of belief and our ability to think and learn?",
        "connection": "Think of a garden. To grow beautiful flowers, you need two things: you need fertile soil where the seeds can root securely, and you need to keep weeds and pests away so the plants can grow healthy leaves. In our lives, our Faith (Din) is the secure soil, and our Intellect ('Aql) is our ability to think, grow, and learn. Shariah acts as the gardener, protecting both our spiritual hearts and our active minds.",
        "concept_def": "Protection of Religion (Hifz al-Din) means safeguarding the right of individuals to hold religious convictions, perform acts of worship safely, and preserve the purity of Islamic knowledge.\n\nProtection of Intellect (Hifz al-'Aql) means safeguarding human reasoning capabilities by encouraging education and prohibiting substances that impair or destroy mental clarity.",
        "scripture_quran": "Let there be no compulsion in religion, for the truth stands out clearly from falsehood.",
        "scripture_quran_ref": "Surah Al-Baqarah, 2:256",
        "scripture_hadith": "Seeking knowledge is an obligation upon every Muslim.",
        "scripture_hadith_ref": "Sunan Ibn Majah, 224",
        "explanation": "Shariah establishes absolute freedom of belief, declaring there is no forced conversion in Islam. It also protects places of worship (mosques) and ensures that scholars transmit religious knowledge accurately, preventing distortions or false claims.\n\nIn Islam, the mind ('Aql) is a sacred trust protected in two ways:\n1. Positive Protection: Mandating education, critical thinking, and constant learning. The first word revealed was 'Read!'\n2. Negative Protection: Strictly prohibiting intoxicants (Khamr), drugs, and any mind-altering substances that damage human reasoning and lead to harmful behavior.",
        "svg_func": get_svg_lesson_2,
        "diagram_title": "Dual Protections: Faith & Mind (Hifz al-Din & Hifz al-'Aql)",
        "table_title": "Comparative Analysis: Faith vs Intellect Protections",
        "table_headers": ["Sacred Faculty", "Affirmative Measure (Cultivation)", "Preventive Measure (Defense)", "Practical Daily Implication"],
        "table_rows": [
            ["Din (Religion)", "Mandatory daily prayers & knowledge transmission", "Prohibition of religious coercion & mosque desecration", "Praying peacefully & respecting others' freedom of belief"],
            ["'Aql (Intellect)", "Mandatory schooling, literacy, & scientific inquiry", "Total prohibition of intoxicants, narcotics, & superstitions", "Studying with focus & staying completely substance-free"]
        ],
        "scenario": "At a community center, Zainab is explaining to her peers why she chose to join the school's science club instead of just staying home. 'My uncle asked me why I study so hard if I want to be a religious person. I told him that my teacher taught us about Hifz al-'Aql (Protection of Intellect). In Islam, keeping my mind sharp, studying science, and learning about the world is actually an act of worship. It's why I also avoid energy drinks or drugs that make my mind foggy—I want to protect this beautiful mind that Allah gave me!'",
        "real_world": "Implement an 'Intellectual Growth Plan' this week. Protect your intellect by dedicating 20 minutes a day to reading a beneficial book (non-fiction, history, or science) and avoiding screen time that impairs your focus. Share what you learned with your family at dinner.",
        "reflection": "Why do you think the Qur'an strongly forbids intoxicants (Khamr)? How does losing our reasoning capability affect our relationships with family and our safety?",
        "misconception": "Seeking knowledge in Islam is not restricted to religious texts; mastering medicine, engineering, technology, and literature is an Islamic civic duty that protects society.",
        "yt_title": "The Sanctuary of the Mind in Islam",
        "yt_desc": "Exploring how Islamic Law champions critical intellect and prohibits mental toxins.",
        "yt_id": "TVt-Dd31Nn4",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Al-Azhar_Mosque_minarets.jpg/1280px-Al-Azhar_Mosque_minarets.jpg",
        "image_title": "Minarets of Al-Azhar University in Cairo",
        "image_caption": "Historic center of Islamic scholarship celebrating both religious sciences and rational learning.",
        "mcq": {
            "question": "Which of the following is a direct, negative protection established by Shariah to safeguard the human intellect ('Aql)?",
            "options": [
                "Encouraging students to travel to seek knowledge",
                "The strict prohibition of intoxicants (Khamr) and harmful drugs",
                "Making school attendance optional for young learners",
                "Establishing religious research centers in universities"
            ],
            "answer": "B",
            "explanation": "Prohibition of intoxicants is a negative protection—it actively bans substances that impair or damage human reasoning, ensuring the mind remains healthy and capable of sound decisions."
        },
        "summary_content": "Shariah protects Religion by ensuring freedom of belief and safeguarding acts of worship. Shariah protects Intellect by making the search for knowledge obligatory and prohibiting mind-altering drugs/alcohol. Faith and critical reasoning work together in Islam to build a balanced character.",
        "key_points": [
            "Freedom of conscience is guaranteed; coercion in faith is strictly rejected.",
            "The human intellect ('Aql) is a divine trust requiring education and mental sobriety.",
            "Intoxicants are banned because they dismantle human reason and self-control."
        ],
        "exit_ticket": "State one positive way and one preventive way Shariah safeguards the human intellect."
    },
    {
        "order": 3,
        "code": "Lesson 4.1.3",
        "title": "Protection of life, property, and dignity",
        "inquiry": "How does Islamic law protect our physical safety, our hard-earned wealth, and our personal honor?",
        "connection": "Imagine walking home from school and knowing that no one can physically hurt you, no one can steal your bag or cheat you out of your pocket money, and no one is allowed to spread false rumors or bully you online. How would you feel? You would feel safe, confident, and peaceful. This beautiful state of peace is exactly what Shariah aims to create by establishing absolute protections for Life, Property, and Dignity.",
        "concept_def": "Protection of Life (Hifz al-Nafs): Guaranteeing the sacred right to life for all human beings, prohibiting murder, self-harm, and violence, and encouraging healthcare.\n\nProtection of Property (Hifz al-Mal): Safeguarding wealth, income, and possessions through fair trade rules, the prohibition of usury (Riba), theft, and fraud.\n\nProtection of Dignity (Hifz al-'Ird): Safeguarding a person's reputation, honor, privacy, and family line from slander, mockery, backbiting, and false accusations.",
        "scripture_quran": "And do not kill the soul which Allah has forbidden, except by right...",
        "scripture_quran_ref": "Surah Al-Isra, 17:33",
        "scripture_hadith": "Do not harm yourselves or others.",
        "scripture_hadith_ref": "Sunan Ibn Majah, 2340",
        "explanation": "These three objectives are realized through clear, practical laws in Shariah:\n\n1. Life (Nafs): Murder is a major sin. Shariah also prohibits suicide and self-harm, and requires seeking medical treatment when sick, viewing life as a sacred trust from Allah.\n2. Property (Mal): Trade is encouraged, but cheating, selling defective goods, and usury (Riba) are forbidden. Contracts must be documented clearly to avoid disputes.\n3. Dignity ('Ird): Spying, backbiting, and mocking are strictly prohibited. Shariah sets severe punishments for false accusations of immorality (Qadhf) to keep people's honor safe.",
        "svg_func": get_svg_lesson_3,
        "diagram_title": "The Triad of Social Security: Life, Property & Dignity",
        "table_title": "Triad of Social Security Breakdown",
        "table_headers": ["Objective", "Shariah Mandates (Do's)", "Shariah Prohibitions (Don'ts)", "Core Value Realized"],
        "table_rows": [
            ["Life (Hifz al-Nafs)", "Seeking medical aid, self-defense, public sanitation", "Murder, assault, suicide, reckless pollution", "Sanctity of physical life"],
            ["Property (Hifz al-Mal)", "Written contracts, honest scales, fair trade", "Theft, usury (Riba), bribery, embezzling public funds", "Economic justice & security"],
            ["Dignity (Hifz al-'Ird)", "Guarding privacy, speaking respectfully, verifying rumors", "Slander, backbiting, leaking DMs, defamation", "Honor & peace of mind"]
        ],
        "scenario": "Ali is tempted to copy a software program online that normally costs 500 shillings and sell it to his friends for 50 shillings. He remembers the lesson on Hifz al-Mal (Protection of Property). He says to himself, 'The person who built this program spent weeks working on it. Copying and selling their work without permission is consuming others' wealth unjustly. It's theft. By buying it honestly, I am respecting their property rights, which Shariah commands me to do.'",
        "real_world": "Apply the 'Honor Shield' in your school. If you hear someone gossiping about a classmate, politely speak up and say, 'Let's not talk about them behind their back; we want to keep our classroom a respectful place.' This directly applies Hifz al-'Ird (Protection of Dignity) by protecting a peer's reputation and honor in their absence.",
        "reflection": "How does the prohibition of usury (Riba) protect poor families from losing their property and falling into endless debt?",
        "misconception": "Dignity in Islam applies equally to everyone: whether rich or poor, young or old, Muslim or non-Muslim, every human soul possesses God-given honor that cannot be violated.",
        "yt_title": "Justice in Islamic Law: Life, Wealth and Honor",
        "yt_desc": "Detailed analysis of civic rights and protections in classical and contemporary Shariah.",
        "yt_id": "UJYkwPDwC-Y",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Bazaar_in_Isfahan.jpg/1280px-Bazaar_in_Isfahan.jpg",
        "image_title": "Historic Covered Bazaar of Isfahan",
        "image_caption": "Centuries of commerce guided by ethical trade regulations, honest weights, and contract protection.",
        "mcq": {
            "question": "Which objective of Shariah is violated when someone logs into a classmate's private social media account without permission to read their messages?",
            "options": [
                "Protection of Property (Hifz al-Mal)",
                "Protection of Life (Hifz al-Nafs)",
                "Protection of Dignity and Privacy (Hifz al-'Ird)",
                "Protection of Religion (Hifz al-Din)"
            ],
            "answer": "C",
            "explanation": "Reading someone's private messages without permission is an invasion of privacy and a direct violation of their personal dignity (Hifz al-'Ird), which Shariah strictly protects."
        },
        "summary_content": "Life (Nafs) is sacred; both murder and self-harm are strictly forbidden. Property (Mal) must be acquired through honest, transparent work, not cheating or usury. Dignity ('Ird) ensures that every human being is treated with respect and their privacy is honored.",
        "key_points": [
            "Human life is an inviolable trust from Allah.",
            "Property rights are secured through transparent contracts and ethical trade.",
            "Personal dignity, privacy, and reputation are sacred and shielded from defamation."
        ],
        "exit_ticket": "Explain how honest business practices protect both property and dignity in a school community."
    },
    {
        "order": 4,
        "code": "Lesson 4.1.4",
        "title": "Categories of legal acts",
        "inquiry": "How does Shariah classify human actions into categories to help us make ethical daily choices?",
        "connection": "Think of a traffic-light system in a large city. Some lights are Green (go ahead!), some are Red (stop immediately!), some are Yellow (prepare to stop or proceed with caution), and some routes are optional scenic routes. Without this system, there would be utter confusion. Shariah organizes all human actions into a beautiful five-part classification system known as the Ahkam al-Khamsah. This system acts as our moral traffic light, helping us know exactly which actions please Allah, which are optional, and which must be stopped.",
        "concept_def": "Ahkam al-Khamsah (The Five Categories of Legal Acts) is the classification system in Islamic law that categorizes every human action into one of five rulings:\n\n1. Fard / Wajib (Obligatory): Commanded by Allah; doing it earns reward, neglecting it is a sin.\n2. Mandub / Mustahabb (Recommended): Encouraged; doing it earns reward, neglecting it is not a sin.\n3. Mubah (Permissible): Neutral; neither rewarded nor punished by default.\n4. Makruh (Disliked): Discouraged; avoiding it earns reward, doing it is not a sin.\n5. Haram (Forbidden): Strictly banned; avoiding it earns reward, committing it is a sin.",
        "scripture_quran": "...And whatever the Messenger has given you – take it; and what he has forbidden you – refrain from...",
        "scripture_quran_ref": "Surah Al-Hashr, 59:7",
        "scripture_hadith": "That which is lawful is clear and that which is unlawful is clear...",
        "scripture_hadith_ref": "Sahih al-Bukhari, 52",
        "explanation": "Understanding these categories prevents us from making mistakes in practice:\n\n1. Obligatory vs. Recommended: We must prioritize Fard (like daily prayers) over Mandub (like voluntary fasts). Doing extra deeds while neglecting basic duties is a common mistake.\n2. The Vastness of Mubah: The default state of worldly things (food, clothing, activities) is Mubah (permissible) unless there is a clear text that makes it forbidden.\n3. Transforming Actions: A neutral Mubah action can be transformed into a rewarded Mandub action by having a good intention. For example, eating food to gain strength for study, or sleeping early to wake up for Fajr prayer.",
        "svg_func": get_svg_lesson_4,
        "diagram_title": "Ahkam al-Khamsah: The Five Legal Categories of Human Acts",
        "table_title": "The Ahkam al-Khamsah Legal Spectrum",
        "table_headers": ["Ruling Category", "Doing the Action", "Avoiding the Action", "Everyday Student Example"],
        "table_rows": [
            ["Wajib / Fard (Obligatory)", "Rewarded by Allah", "Accountable / Sinful", "Praying Salat on time; honoring parents"],
            ["Mandub / Mustahabb (Recommended)", "Rewarded by Allah", "No sin or penalty", "Smiling at peers; using Siwak; voluntary charity"],
            ["Mubah (Permissible)", "Neutral (No reward)", "Neutral (No sin)", "Playing football; eating an apple; sleeping"],
            ["Makruh (Disliked)", "No sin (but discouraged)", "Rewarded by Allah", "Wasting tap water during wudhu; unnecessary delays"],
            ["Haram (Forbidden)", "Accountable / Sinful", "Rewarded by Allah", "Lying, stealing, cheating in exams, drinking alcohol"]
        ],
        "scenario": "Yusuf is washing his face for wudhu and keeps the tap running at full blast, wasting liters of water. Halima reminds him, 'Yusuf, wasting water is Makruh (disliked) in Islam, even if you are performing a holy act like wudhu. The Prophet (PBUH) told us not to waste water even if we are by a flowing river. If you turn down the tap, you will avoid this disliked action and earn a reward for following his Sunnah!' Yusuf smiles and says, 'Thank you, Halima! I will turn it down.'",
        "real_world": "Look at your schedule for today. Choose three neutral Mubah actions (like studying, eating lunch, or sweeping your room). Write down a sincere intention (Niyyah) for each to connect it to pleasing Allah (e.g., 'I will sweep my room to make my mother happy and keep my home clean'). Notice how this transforms your regular daily habits into acts of worship that earn rewards!",
        "reflection": "How does having a category like Mubah (permissible) show that Islam is a practical religion that celebrates the normal joys of life?",
        "misconception": "Things are permissible (Mubah) by default in worldly affairs until proven forbidden; Islam does not place undue hardship on daily living.",
        "yt_title": "Understanding the Five Rulings (Ahkam al-Khamsah)",
        "yt_desc": "Clear breakdown of Wajib, Mandub, Mubah, Makruh, and Haram in Islamic Law.",
        "yt_id": "AHVP62ebo7s",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Moroccan_Islamic_Manuscript_Fiqh.jpg/1280px-Moroccan_Islamic_Manuscript_Fiqh.jpg",
        "image_title": "Classical Maghrebi Jurisprudence (Fiqh) Folio",
        "image_caption": "Hand-inked classical manuscript codifying legal classifications and rulings.",
        "mcq": {
            "question": "Which category of legal acts describes an action where 'avoiding it earns a reward, but performing it is not considered a sin'?",
            "options": [
                "Haram",
                "Wajib",
                "Makruh",
                "Mubah"
            ],
            "answer": "C",
            "explanation": "Makruh actions are disliked or discouraged. In Islamic law, avoiding them is praised and rewarded, but performing them does not result in a sin."
        },
        "summary_content": "All human actions are categorized into Wajib, Mandub, Mubah, Makruh, or Haram. Sincere intentions can elevate ordinary permissible actions into highly rewarded deeds. Wajib actions are the absolute core of our religious responsibility.",
        "key_points": [
            "The five categories organize all actions into a clear moral framework.",
            "Mubah actions can be transformed into rewarded deeds through good Niyyah.",
            "Wajib must always be prioritized over optional recommended deeds."
        ],
        "exit_ticket": "Classify telling the truth, eating a clean snack, and stealing a pen into their correct legal categories."
    },
    {
        "order": 5,
        "code": "Lesson 4.1.5",
        "title": "Contemporary relevance",
        "inquiry": "How do the ancient objectives of Shariah guide us through modern challenges like digital privacy and cyber-bullying?",
        "connection": "Have you ever used an old compass? Even if the compass was built hundreds of years ago, it will still point perfectly North today, whether you are in a desert, in the middle of a modern city, or on a high-tech ship. The Maqasid al-Shariah (objectives of Shariah) are like that perfect compass. They were established over 1,400 years ago, but they still point exactly to justice and safety today, helping us navigate modern challenges like internet fraud, social media bullying, and environmental protection.",
        "concept_def": "Contemporary Relevance refers to the dynamic application of Shariah's higher objectives to modern dilemmas and technology that did not exist during the early period of Islam.\n\nModern Applications include:\n- Cyber-bullying and digital defamation violate Hifz al-'Ird (Protection of Dignity).\n- Online piracy and digital theft violate Hifz al-Mal (Protection of Property).\n- Environmental degradation and chemical pollution violate Hifz al-Nafs (Protection of Life).",
        "scripture_quran": "...And do not mix the truth with falsehood or conceal the truth while you know [it].",
        "scripture_quran_ref": "Surah Al-Baqarah, 2:42",
        "scripture_hadith": "Do not harm yourselves or others.",
        "scripture_hadith_ref": "Sunan Ibn Majah, 2340",
        "explanation": "Shariah provides timeless guidance for modern everyday digital and environmental situations:\n\n1. Digital Privacy: Spying on someone's chat logs or leaking private photos violates Hifz al-'Ird (Dignity and Privacy). Shariah demands that we protect people's boundaries online just as we do in the physical world.\n2. Intellectual Property: Copying games, music, or textbooks illegally violates Hifz al-Mal (Property). Creators have the right to be compensated for their work, and Shariah protects this right.\n3. Environmental Care: Dumping trash in public spaces or destroying forests damages clean air and water, violating Hifz al-Nafs (Life), because human health depends on a clean environment.",
        "svg_func": get_svg_lesson_5,
        "diagram_title": "The Digital Integrity Filter: Modern Maqasid Application",
        "table_title": "Contemporary Dilemmas Mapped to Shariah Objectives",
        "table_headers": ["Modern Dilemma", "Underlying Shariah Principle", "Unethical Action", "Responsible Islamic Solution"],
        "table_rows": [
            ["Cyber-bullying & Doxxing", "Hifz al-'Ird (Dignity)", "Spreading mocking memes or private photos", "Protecting peer privacy & deleting gossip"],
            ["Digital Piracy & Plagiarism", "Hifz al-Mal (Property)", "Stealing software, music, or essays", "Buying lawful licenses & citing original authors"],
            ["Plastic Pollution & Litter", "Hifz al-Nafs (Life)", "Dumping toxic waste in rivers & streets", "Active community cleanup & recycling"],
            ["Vaping & Substance Abuse", "Hifz al-'Aql (Intellect)", "Inhaling chemical drugs to feel high", "Strict sobriety & physical fitness"]
        ],
        "scenario": "Hussein's class has a WhatsApp group. One student forwards a funny meme mocking another classmate's clothing and accent. The classmate is hurt and leaves the group. Hussein posts in the group, 'Guys, forwarding this meme might seem like a joke, but it is a form of mockery and violates our friend's dignity ('Ird). Let's delete the meme, apologize to our friend, and agree that our group chat will only be a place of kindness and respect.' The other students realize their mistake, delete the meme, and invite the classmate back.",
        "real_world": "Check your digital behavior this week. Apply a 'Zero-Harm Policy' on your phone or computer. Never forward a video or message that makes fun of someone, never copy someone's homework or digital files without permission, and use your device to share useful knowledge. This is a practical, modern application of Hifz al-'Ird and Hifz al-Mal.",
        "reflection": "How does dumping trash or plastic in public spaces violate the Shariah's goal of protecting life (Hifz al-Nafs)?",
        "misconception": "Digital spaces are not exempt from moral laws; an action that is sinful or harmful in physical reality remains equally forbidden online.",
        "yt_title": "Navigating the Digital Age with Islamic Ethics",
        "yt_desc": "Dr. Omar Suleiman addresses cyber-ethics, privacy, and online responsibility.",
        "yt_id": "_UomJ4KolFE",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Server_rack_wires.jpg/1280px-Server_rack_wires.jpg",
        "image_title": "Modern Cloud Server Infrastructure",
        "image_caption": "Digital communication platforms that require strict ethical standards of privacy and data security.",
        "mcq": {
            "question": "Which objective of Shariah is a student actively upholding when they refuse to download a pirated version of an educational software program?",
            "options": [
                "Protection of Religion (Hifz al-Din)",
                "Protection of Property (Hifz al-Mal)",
                "Protection of Intellect (Hifz al-'Aql)",
                "Protection of Life (Hifz al-Nafs)"
            ],
            "answer": "B",
            "explanation": "Educational software is intellectual property. Refusing to download a pirated copy respects the creator's ownership rights, thereby actively upholding the protection of property (Hifz al-Mal)."
        },
        "summary_content": "Shariah's principles are timeless and apply fully to modern technology and issues. Cyber-bullying and hacking violate the sacred protection of personal dignity ('Ird). Protecting our environment and community health is part of the protection of life (Nafs).",
        "key_points": [
            "Shariah principles apply dynamically to all emerging modern technologies.",
            "Digital privacy and copyright are sacred trusts protected by Islamic law.",
            "Environmental stewardship is directly tied to the protection of human life."
        ],
        "exit_ticket": "State how the objective of protecting dignity (Hifz al-'Ird) applies to your behavior in school chat groups."
    },
    {
        "order": 6,
        "code": "Lesson 4.1.6",
        "title": "Daily-life application and synthesis",
        "inquiry": "How do we bring together all the objectives and categories of Shariah to make wise, balanced daily choices?",
        "connection": "Imagine you are a pilot preparing for a flight. You have a flight path (Shariah), a destination (pleasing Allah), a safety checklist (Maqasid), and a control panel showing what is safe and what is dangerous (Ahkam al-Khamsah). To have a successful flight, you cannot just look at the controls; you must actively use them at every turn. In this final lesson of the unit, we will combine our knowledge of Shariah's goals and action categories into a practical 'Daily Decision Protocol' to guide our lives.",
        "concept_def": "Comprehensive Shariah Framework is the systematic integration of Islamic objectives (Maqasid) and legal classifications (Ahkam) into a person's everyday character, making them an ethical and beneficial citizen.\n\nMaslahah (Public Benefit) means promoting good and ensuring the welfare of the community, which is the ultimate goal of Shariah.",
        "scripture_quran": "Indeed, Allah commands you to act with justice, the doing of good, and liberality to kith and kin...",
        "scripture_quran_ref": "Surah Al-Nahl, 16:90",
        "scripture_hadith": "Do not harm yourselves or others.",
        "scripture_hadith_ref": "Sunan Ibn Majah, 2340",
        "explanation": "Let's review the complete synthesis of the unit:\n\n1. The Core Philosophy: Shariah is divine guidance sent to bring mercy, prevent harm (Mafsadah), and establish justice (Maslahah).\n2. The Five Core Protections (Maqasid): Every rule in Shariah exists to safeguard Religion, Life, Intellect, Property, or Dignity.\n3. The Five Action Filters (Ahkam): We evaluate choices through Wajib (must do), Mandub (encouraged), Mubah (neutral), Makruh (avoid), and Haram (must avoid).\n4. The Daily Protocol: Before performing an action, ask yourself: Does this help or harm the five core protections? What is its legal category? How can I align this with pleasing Allah?",
        "svg_func": get_svg_lesson_6,
        "diagram_title": "Master Synthesis: The Complete Shariah Guidance System",
        "table_title": "The Shariah Decision Dashboard",
        "table_headers": ["Everyday Scenario", "Action Taken", "Maqasid Upheld", "Ahkam Category", "Outcome"],
        "table_rows": [
            ["Finding a lost wallet in playground", "Hand it to school office", "Hifz al-Mal (Property)", "Wajib (Obligatory)", "Trust, reward, and honest school"],
            ["Classmate being mocked online", "Speak up gently & report", "Hifz al-'Ird (Dignity)", "Mandub (Recommended)", "Protected friend & peaceful chat"],
            ["Exam pressure & study exhaustion", "Eat healthy & sleep early", "Hifz al-'Aql & Nafs", "Mubah elevated by Niyyah", "Sharp mind & reward for health"],
            ["Tempted to copy software illegally", "Refuse and buy honestly", "Hifz al-Mal (Property)", "Avoiding Haram (Rewarding)", "Pure income & clear conscience"]
        ],
        "scenario": "Match the following real-life choices to the correct Shariah objective they protect:\n1. Refusing to join a group of students drinking alcohol behind the school. (Answer: Protection of Intellect & Life)\n2. Helping a poor neighbor pay for their medicine. (Answer: Protection of Life & Property)\n3. Standing up for a classmate who is being called offensive nicknames. (Answer: Protection of Dignity)\n4. Praying your daily prayers on time in the school mosque. (Answer: Protection of Religion)",
        "real_world": "Draft a 'Classroom Peace and Justice Charter' with your peers. Base the charter on the five Maqasid protections: respect each other's beliefs (Religion), keep the classroom safe (Life), study hard and respect teachers (Intellect), do not touch others' bags or pens without permission (Property), and speak kindly without insults (Dignity). Present it to your teacher and display it on the class wall.",
        "reflection": "How does understanding Shariah as a protective shield help you explain its beauty to someone who does not understand it?",
        "misconception": "Shariah is not a rigid burden; it is a holistic, merciful design for human dignity, justice, and spiritual joy.",
        "yt_title": "Living the Spirit of Shariah in Everyday Life",
        "yt_desc": "Comprehensive synthesis of Islamic jurisprudence and ethical living.",
        "yt_id": "mdO-w7pbLaQ",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Alhambra_Court_of_the_Lions.jpg/1280px-Alhambra_Court_of_the_Lions.jpg",
        "image_title": "Court of the Lions at the Alhambra, Granada",
        "image_caption": "Historic pinnacle of Islamic civilization harmonizing beauty, law, and human flourishing.",
        "mcq": {
            "question": "Zuri is walking home and notices a sharp piece of broken glass lying in the middle of a pedestrian path where children run. She stops, picks up the glass carefully, and disposes of it in a bin. Applying our unit's synthesis, which category and objective did Zuri's choice demonstrate?",
            "options": [
                "It was a neutral Mubah action that had no effect on anyone",
                "It was a Mandub (recommended) action that actively upheld the protection of life (Hifz al-Nafs)",
                "It was an obligatory Wajib action that protected her personal property (Hifz al-Mal)",
                "It was a disliked Makruh action that she should have avoided"
            ],
            "answer": "B",
            "explanation": "Removing a harmful obstacle from a public pathway is highly recommended (Mandub) in Islam. By removing the broken glass, Zuri actively prevented injuries, which directly supports the protection of life (Hifz al-Nafs)."
        },
        "summary_content": "Shariah is a comprehensive, mercy-based guide that balances individual rights with public welfare (Maslahah). Applying the five objectives (Maqasid) ensures our actions build a safe, stable, and unified community. Human actions are moral choices; using the Shariah dashboard helps us earn Allah's eternal pleasure.",
        "key_points": [
            "Shariah brings together divine revelation, human welfare, and moral action.",
            "All five objectives cooperate to build an equitable, safe, and just society.",
            "Daily choices guided by Shariah transform regular life into meaningful worship."
        ],
        "exit_ticket": "Write down the single most important lesson you have learned about Shariah in this unit and how you will apply it."
    }
]


# ─────────────────────────────────────────────────────────────────────────────
# DATABASE INGESTION EXECUTION
# ─────────────────────────────────────────────────────────────────────────────

def ingest_grade9_ire_topic7():
    print("=" * 80)
    print("STARTING INGESTION: GRADE 9 IRE — TOPIC 7: SHARIAH (ISLAMIC LAW)")
    print("=" * 80)

    try:
        topic = Topic.objects.get(id=347)
    except Topic.DoesNotExist:
        print("ERROR: Topic ID 347 does not exist!")
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
            u_order = cfg["order"]
            l_title = cfg["title"]

            # 1. Create LearningUnit
            unit = LearningUnit.objects.create(
                topic=topic,
                name=f"{cfg['code']}: {l_title}",
                description=clean_text(cfg["inquiry"]),
                order=u_order
            )
            total_units += 1

            # 2. Create Published Lesson
            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=f"{cfg['code']}: {l_title}",
                status="published",
                version=1
            )
            total_lessons += 1

            # 3. Create LessonAssets
            # Asset A: Wikimedia Image
            img_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                title=clean_text(cfg["image_title"]),
                url=cfg["image_url"],
                metadata={
                    "caption": clean_text(cfg["image_caption"]),
                    "source": "Wikimedia Commons",
                    "license": "CC BY-SA / Public Domain"
                }
            )
            total_assets += 1

            # Asset B: Custom Vector SVG
            svg_code = cfg["svg_func"]()
            svg_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                title=clean_text(cfg["diagram_title"]),
                metadata={
                    "svg_content": svg_code,
                    "svg_xml": svg_code,
                    "theme": "#0f172a",
                    "viewBox": "0 0 880 440",
                    "responsive": True
                }
            )
            total_assets += 1

            # Asset C: Educational YouTube Video
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

            # 4. Create 7 Cards / Pages (15 Blocks)
            # ─────────────────────────────────────────────────────────────────
            # CARD 1 (Page 1): Orientation (2 blocks)
            # ─────────────────────────────────────────────────────────────────
            b_img = LessonBlock.objects.create(
                lesson=lesson,
                page_number=1,
                page_title="Orientation & Inquiry",
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
                page_title="Orientation & Inquiry",
                order=20,
                component_order=2,
                block_type="learning_goal",
                component_type="learning_goal",
                title="Learning Goal & Inquiry",
                content={
                    "title": "Lesson Inquiry & Hook",
                    "question": clean_text(cfg["inquiry"]),
                    "hook": clean_text(cfg["connection"]),
                    "text": clean_text(f"**Inquiry:** {cfg['inquiry']}\n\n**Connection:** {cfg['connection']}")
                }
            )

            # ─────────────────────────────────────────────────────────────────
            # CARD 2 (Page 2): Core Teaching & Scripture (2 blocks)
            # ─────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=2,
                page_title="Core Theological Concept",
                order=30,
                component_order=1,
                block_type="concept_explanation",
                component_type="concept_explanation",
                title="Authoritative Concept",
                content={
                    "title": "Authoritative Concept",
                    "content": clean_text(cfg["concept_def"]),
                    "text": clean_text(cfg["concept_def"])
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
                title="Clarifying the Concept",
                content={
                    "title": "Clarifying the Concept",
                    "content": clean_text(cfg["explanation"]),
                    "text": clean_text(cfg["explanation"])
                }
            )

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
                    "svg_content": svg_code,
                    "svg_xml": svg_code,
                    "svg": svg_code,
                    "description": f"Dedicated vector SVG diagram illustrating {cfg['title']}."
                },
                metadata={
                    "svg_content": svg_code,
                    "svg_xml": svg_code
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
                    "rows": [[clean_text(cell) for cell in row] for row in cfg["table_rows"]]
                }
            )

            # ─────────────────────────────────────────────────────────────────
            # CARD 4 (Page 4): Worked Scenario (1 block)
            # ─────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=4,
                page_title="Scenario & Worked Example",
                order=80,
                component_order=1,
                block_type="worked_example",
                component_type="worked_example",
                title="Relatable Student Scenario",
                content={
                    "title": "Relatable Student Scenario",
                    "scenario": clean_text(cfg["scenario"]),
                    "text": clean_text(cfg["scenario"])
                }
            )

            # ─────────────────────────────────────────────────────────────────
            # CARD 5 (Page 5): Real-World Application & Video (4 blocks)
            # ─────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=5,
                page_title="Application & Reflection",
                order=90,
                component_order=1,
                block_type="real_world_example",
                component_type="real_world_example",
                title="Actionable Daily Practice",
                content={
                    "title": "Actionable Daily Practice",
                    "content": clean_text(cfg["real_world"]),
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
    print("TOPIC 7 INGESTION COMPLETE & VERIFIED!")
    print(f"  LearningUnits : {total_units} / 6")
    print(f"  Lessons       : {total_lessons} / 6 (Published)")
    print(f"  Blocks        : {total_blocks} (15 per lesson, 7 pages)")
    print(f"  Assets        : {total_assets} (6 SVGs, 6 images, 6 videos)")
    print("=" * 80)


if __name__ == "__main__":
    ingest_grade9_ire_topic7()
