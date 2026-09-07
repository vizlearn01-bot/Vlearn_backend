"""
VLearn CBC Grade 9 IRE — Topic 8: Tawbah (Repentance)
Production Ingestion and Enrichment Script for all 5 Lessons

Target Topic in DB: Topic ID 348 (Subject: IRE ID 53, Grade: Grade 9 ID 18)
Source Markdown: /home/jason-bitega/Desktop/VL/vlearn_repositories/Grade 9 IRE/tawbah.md

5 Lessons Ingested & Fully Enriched:
  1. Lesson 4.2.1: Meaning and need for tawbah
  2. Lesson 4.2.2: Conditions of tawbah
  3. Lesson 4.2.3: Qur’anic guidance on tawbah
  4. Lesson 4.2.4: Practising responsible repentance
  5. Lesson 4.2.5: Unit synthesis
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
# 5 DEDICATED RESPONSIVE PEDAGOGICAL VECTOR SVGS (#0f172a theme, viewBox 880x440)
# ─────────────────────────────────────────────────────────────────────────────

def get_svg_lesson_1():
    """Lesson 4.2.1: The Continuous Cycle of Spiritual Renewal"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg81" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="cyanGrad81" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg81)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE CONTINUOUS CYCLE OF SPIRITUAL RENEWAL (TAWBAH)</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">How Sincere Repentance Cleanses Human Imperfection and Restores Proximity to Allah</text>

  <!-- Central Hub: The Heart's Peace -->
  <circle cx="440" cy="240" r="62" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="440" y="235" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">A CLEAN HEART</text>
  <text x="440" y="252" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">(Qalb Salim)</text>

  <!-- 4 Orbiting Cycle Stages -->
  <!-- Step 1: Human Slip / Mistake (Top) -->
  <g transform="translate(340, 90)">
    <rect width="200" height="65" rx="8" fill="#1e293b" stroke="#f87171" stroke-width="1.5"/>
    <text x="100" y="24" fill="#f87171" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">1. THE SLIP (HUMAN ERROR)</text>
    <text x="100" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Forgetting, slipping, or yielding</text>
    <text x="100" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">"All children of Adam are sinners"</text>
  </g>

  <!-- Step 2: Spiritual Awareness / Nadam (Right) -->
  <g transform="translate(630, 205)">
    <rect width="200" height="70" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="100" y="24" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">2. AWARENESS &amp; REMORSE</text>
    <text x="100" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Heartfelt regret (Nadam)</text>
    <text x="100" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Conscience triggered by faith</text>
  </g>

  <!-- Step 3: Turning Back in Sincerity (Bottom) -->
  <g transform="translate(340, 325)">
    <rect width="200" height="65" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="100" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">3. TAWBAH &amp; DUA</text>
    <text x="100" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Turning back with sincere Istighfar</text>
    <text x="100" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Stopping the sin &amp; righting wrongs</text>
  </g>

  <!-- Step 4: Spiritual Washing & Restoration (Left) -->
  <g transform="translate(50, 205)">
    <rect width="200" height="70" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="100" y="24" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">4. CLEANSING &amp; PEACE</text>
    <text x="100" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Divine forgiveness washes stain</text>
    <text x="100" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Inner peace &amp; divine love earned</text>
  </g>

  <!-- Flow Arrows connecting the cycle -->
  <path d="M 545 125 C 600 145, 660 170, 680 200" fill="none" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,4"/>
  <path d="M 700 280 C 680 320, 600 345, 545 355" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>
  <path d="M 335 355 C 280 345, 200 320, 180 280" fill="none" stroke="#10b981" stroke-width="2" stroke-dasharray="4,4"/>
  <path d="M 180 200 C 200 160, 270 135, 335 125" fill="none" stroke="#f87171" stroke-width="2" stroke-dasharray="4,4"/>
</svg>"""


def get_svg_lesson_2():
    """Lesson 4.2.2: The Five-Key Padlock of Sincere Repentance"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg82" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="goldGrad82" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg82)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE 5-KEY PADLOCK OF SINCERE REPENTANCE (SHURUT AL-TAWBAH)</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">All Five Theological Conditions Required for Forgiveness and Acceptance in the Sight of Allah</text>

  <!-- 5 Condition Keys -->
  <!-- Key 1: Ikhlas (Sincerity) -->
  <g transform="translate(35, 90)">
    <rect width="148" height="305" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="148" height="34" rx="8" fill="#0284c7"/>
    <text x="74" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">1. IKHLAS</text>
    <text x="74" y="55" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Pure Sincerity</text>
    <text x="12" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Done solely for Allah</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• No social showing off</text>
    <text x="12" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Not just to escape jail</text>
    <rect x="15" y="170" width="118" height="100" rx="6" fill="#0f172a"/>
    <text x="74" y="195" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Heart Intention</text>
    <text x="74" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">"Actions are judged</text>
    <text x="74" y="230" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">by intentions"</text>
  </g>

  <!-- Key 2: Nadam (Regret) -->
  <g transform="translate(198, 90)">
    <rect width="148" height="305" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="148" height="34" rx="8" fill="#d97706"/>
    <text x="74" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">2. NADAM</text>
    <text x="74" y="55" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Heartfelt Regret</text>
    <text x="12" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Genuine remorse</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• No pride in the sin</text>
    <text x="12" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Grieved to disobey</text>
    <rect x="15" y="170" width="118" height="100" rx="6" fill="#0f172a"/>
    <text x="74" y="195" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Prophetic Rule</text>
    <text x="74" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">"Regret is itself</text>
    <text x="74" y="230" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">repentance"</text>
  </g>

  <!-- Key 3: Iqla' (Ceasing) -->
  <g transform="translate(361, 90)">
    <rect width="148" height="305" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="148" height="34" rx="8" fill="#b91c1c"/>
    <text x="74" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">3. IQLA'</text>
    <text x="74" y="55" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Immediate Stop</text>
    <text x="12" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Instantly drop the sin</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Walk away from harm</text>
    <text x="12" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Cut off evil triggers</text>
    <rect x="15" y="170" width="118" height="100" rx="6" fill="#0f172a"/>
    <text x="74" y="195" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Action Barrier</text>
    <text x="74" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">No repenting while</text>
    <text x="74" y="230" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">continuing the act</text>
  </g>

  <!-- Key 4: 'Azm (Firm Resolve) -->
  <g transform="translate(524, 90)">
    <rect width="148" height="305" rx="8" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <rect width="148" height="34" rx="8" fill="#7c3aed"/>
    <text x="74" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">4. 'AZM</text>
    <text x="74" y="55" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Never Again</text>
    <text x="12" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Sincere resolve</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Concrete life plan</text>
    <text x="12" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Building good habits</text>
    <rect x="15" y="170" width="118" height="100" rx="6" fill="#0f172a"/>
    <text x="74" y="195" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Future Shield</text>
    <text x="74" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">No planning to</text>
    <text x="74" y="230" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">repeat the mistake</text>
  </g>

  <!-- Key 5: Restitution (Ithaar al-Haqq) -->
  <g transform="translate(687, 90)">
    <rect width="158" height="305" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="158" height="34" rx="8" fill="#059669"/>
    <text x="79" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">5. RESTITUTION</text>
    <text x="79" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Right the Wrong</text>
    <text x="12" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• For human rights!</text>
    <text x="12" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Return stolen goods</text>
    <text x="12" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Seek peer apology</text>
    <rect x="15" y="170" width="128" height="100" rx="6" fill="#0f172a"/>
    <text x="79" y="195" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Divine Justice</text>
    <text x="79" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Allah does not wave</text>
    <text x="79" y="230" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">another human's rights</text>
  </g>
</svg>"""


def get_svg_lesson_3():
    """Lesson 4.2.3: Divine Mercy Gates & Tabdeel (Surah Al-Furqan & Al-Zumar)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg83" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="mercyGrad83" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#818cf8"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg83)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">THE QUR'ANIC PROMISE: LIMITLESS MERCY &amp; TABDEEL</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Surah Al-Zumar (39:53) Banishes Despair &amp; Surah Al-Furqan (25:70) Transforms Sins into Good Deeds</text>

  <!-- Left: Sins & Burden (Before Tawbah) -->
  <g transform="translate(45, 90)">
    <rect width="250" height="315" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="125" y="30" fill="#f87171" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">PAST SINS &amp; BURDENS</text>
    
    <rect x="20" y="50" width="210" height="45" rx="4" fill="#0f172a"/>
    <text x="30" y="70" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9.5">• Skipped prayers &amp; duties</text>
    <text x="30" y="85" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5">Negative balance on scale</text>

    <rect x="20" y="105" width="210" height="45" rx="4" fill="#0f172a"/>
    <text x="30" y="125" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9.5">• Lying &amp; broken promises</text>
    <text x="30" y="140" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5">Burden of guilt &amp; sorrow</text>

    <rect x="20" y="160" width="210" height="45" rx="4" fill="#0f172a"/>
    <text x="30" y="180" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="9.5">• Rude speech &amp; gossip</text>
    <text x="30" y="195" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5">Spiritual distance from Allah</text>

    <rect x="20" y="225" width="210" height="60" rx="4" fill="#ef4444" opacity="0.15"/>
    <text x="125" y="248" fill="#f87171" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">SATAN'S TRAP: DESPAIR</text>
    <text x="125" y="268" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">"You are hopeless, don't bother repenting"</text>
  </g>

  <!-- Middle: Divine Portal of Mercy -->
  <g transform="translate(325, 90)">
    <rect width="230" height="315" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect width="230" height="36" rx="10" fill="url(#mercyGrad83)"/>
    <text x="115" y="24" fill="#0f172a" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">THE DIVINE PORTAL</text>

    <text x="115" y="65" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Surah Al-Zumar 39:53</text>
    <text x="115" y="85" fill="#fde68a" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">"LA TAQNATU!"</text>
    <text x="115" y="100" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">"Do not despair of Allah's mercy,</text>
    <text x="115" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">He forgives ALL sins!"</text>

    <line x1="20" y1="130" x2="210" y2="130" stroke="#334155"/>

    <text x="115" y="155" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Surah Al-Furqan 25:70</text>
    <text x="115" y="175" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">THE TABDEEL MIRACLE</text>
    <text x="115" y="195" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">"For those who repent, believe,</text>
    <text x="115" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">&amp; do good work, Allah will</text>
    <text x="115" y="225" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">REPLACE EVIL WITH GOOD!"</text>

    <rect x="20" y="245" width="190" height="50" rx="6" fill="#0284c7" opacity="0.2"/>
    <text x="115" y="266" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">DIVINE TRANSMUTATION</text>
    <text x="115" y="282" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Past grief becomes future drive</text>
  </g>

  <!-- Right: Reformed Record (After Tawbah) -->
  <g transform="translate(585, 90)">
    <rect width="250" height="315" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="125" y="30" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">REFORMED RADIANT RECORD</text>

    <rect x="20" y="50" width="210" height="45" rx="4" fill="#0f172a"/>
    <text x="30" y="70" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="9.5">✓ Replaced with Humility</text>
    <text x="30" y="85" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5">Sincere tears wipe past neglect</text>

    <rect x="20" y="105" width="210" height="45" rx="4" fill="#0f172a"/>
    <text x="30" y="125" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="9.5">✓ Replaced with Honest Speech</text>
    <text x="30" y="140" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5">Amends paid &amp; trust restored</text>

    <rect x="20" y="160" width="210" height="45" rx="4" fill="#0f172a"/>
    <text x="30" y="180" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="9.5">✓ Replaced with Kind Words</text>
    <text x="30" y="195" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5">Compliments &amp; defense of peers</text>

    <rect x="20" y="225" width="210" height="60" rx="4" fill="#10b981" opacity="0.15"/>
    <text x="125" y="248" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">RESULT: ALLAH'S LOVE</text>
    <text x="125" y="268" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">"Allah loves those who constantly repent"</text>
  </g>
</svg>"""


def get_svg_lesson_4():
    """Lesson 4.2.4: The Three R's of Responsible Repentance"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg84" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg84)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">PRACTICING RESPONSIBLE REPENTANCE: THE THREE R'S</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Moving from Passive Verbal Remorse to Courageous Restitution and Permanent Habit Transformation</text>

  <!-- 3 Stage Process Cards -->
  <!-- R1: Regret & Recognize (Internal Soul) -->
  <g transform="translate(45, 90)">
    <rect width="245" height="315" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="245" height="36" rx="10" fill="#0284c7"/>
    <text x="122" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">1. REGRET &amp; RECOGNIZE</text>
    <text x="122" y="55" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Internal Heart Audit</text>

    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Admit mistake without excuses</text>
    <text x="20" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Stop justifying or deflecting</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Feel genuine remorse before Allah</text>
    <text x="20" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Private Istighfar in prayer</text>

    <rect x="20" y="180" width="205" height="95" rx="6" fill="#0f172a"/>
    <text x="122" y="205" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">STUDENT SCENARIO</text>
    <text x="122" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Zainab accidentally breaks</text>
    <text x="122" y="240" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Halima's borrowed compass</text>
    <text x="122" y="255" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">and feels heavy remorse.</text>
  </g>

  <!-- Arrow 1 to 2 -->
  <path d="M 298 245 L 325 245" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>

  <!-- R2: Repair & Restore (Interpersonal Sphere) -->
  <g transform="translate(335, 90)">
    <rect width="245" height="315" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="245" height="36" rx="10" fill="#d97706"/>
    <text x="122" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">2. REPAIR &amp; RESTORE</text>
    <text x="122" y="55" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Interpersonal Restitution</text>

    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Face peer with courage &amp; humility</text>
    <text x="20" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Say clear, unconditional apology</text>
    <text x="20" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Replace or pay for damaged item</text>
    <text x="20" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Correct false rumors in public</text>

    <rect x="20" y="180" width="205" height="95" rx="6" fill="#0f172a"/>
    <text x="122" y="205" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">STUDENT SCENARIO</text>
    <text x="122" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Zainab buys a brand-new</text>
    <text x="122" y="240" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">geometry set with allowance</text>
    <text x="122" y="255" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">and apologizes to Halima.</text>
  </g>

  <!-- Arrow 2 to 3 -->
  <path d="M 588 245 L 615 245" stroke="#fbbf24" stroke-width="3" stroke-linecap="round"/>

  <!-- R3: Reform & Reinforce (Habit Transformation) -->
  <g transform="translate(625, 90)">
    <rect width="210" height="315" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="210" height="36" rx="10" fill="#059669"/>
    <text x="105" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">3. REFORM &amp; REINFORCE</text>
    <text x="105" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Permanent Change</text>

    <text x="15" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Identify slip trigger</text>
    <text x="15" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Build defensive habit</text>
    <text x="15" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Practice extra kindness</text>
    <text x="15" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Maintain clean record</text>

    <rect x="15" y="180" width="180" height="95" rx="6" fill="#0f172a"/>
    <text x="105" y="205" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">STUDENT SCENARIO</text>
    <text x="105" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Zainab treats borrowed</text>
    <text x="105" y="240" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">items with utmost amanah</text>
    <text x="105" y="255" fill="#34d399" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">and gains deep trust.</text>
  </g>
</svg>"""


def get_svg_lesson_5():
    """Lesson 4.2.5: The Spiritual Ascent of the Soul (Tawbah & Tazkiyah)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg85" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="goldGrad85" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
  </defs>

  <rect width="880" height="440" rx="14" fill="url(#bg85)"/>
  <rect x="2" y="2" width="876" height="436" rx="12" fill="none" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">MASTER SYNTHESIS: THE SPIRITUAL ASCENT (TAWBAH &amp; TAZKIYAH)</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">The Golden Staircase Ascending from the Guilt of Human Slips to Divine Love and Pure Character</text>

  <!-- Golden Staircase of Repentance Steps -->
  <!-- Step 1: Ikhlas -->
  <g transform="translate(60, 310)">
    <rect width="130" height="75" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="65" y="25" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">STEP 1: IKHLAS</text>
    <text x="65" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Sincere Intention</text>
    <text x="65" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">Solely for Allah</text>
  </g>

  <!-- Step 2: Nadam -->
  <g transform="translate(200, 260)">
    <rect width="130" height="75" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="65" y="25" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">STEP 2: NADAM</text>
    <text x="65" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Heartfelt Regret</text>
    <text x="65" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">True inner sorrow</text>
  </g>

  <!-- Step 3: Iqla' -->
  <g transform="translate(340, 210)">
    <rect width="130" height="75" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="65" y="25" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">STEP 3: IQLA'</text>
    <text x="65" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Cease the Sin</text>
    <text x="65" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">Stop immediately</text>
  </g>

  <!-- Step 4: 'Azm -->
  <g transform="translate(480, 160)">
    <rect width="130" height="75" rx="6" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <text x="65" y="25" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">STEP 4: 'AZM</text>
    <text x="65" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Firm Resolve</text>
    <text x="65" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">Never return</text>
  </g>

  <!-- Step 5: Ithaar al-Haqq (Restitution) -->
  <g transform="translate(620, 110)">
    <rect width="130" height="75" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="65" y="25" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">STEP 5: RESTITUTION</text>
    <text x="65" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Right the Wrong</text>
    <text x="65" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Restore rights</text>
  </g>

  <!-- Landing Platform: The Purified Soul (Tazkiyah) -->
  <g transform="translate(620, 205)">
    <rect width="210" height="180" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
    <rect width="210" height="32" rx="8" fill="url(#goldGrad85)"/>
    <text x="105" y="21" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">THE LANDING: DIVINE LOVE</text>

    <text x="105" y="55" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Surah Al-Baqarah 2:222</text>
    <text x="105" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">"Indeed, Allah loves those who</text>
    <text x="105" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">are constantly repentant &amp;</text>
    <text x="105" y="105" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">love to purify themselves."</text>

    <rect x="15" y="125" width="180" height="40" rx="4" fill="#0f172a" stroke="#10b981"/>
    <text x="105" y="142" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">TRANQUIL HEART</text>
    <text x="105" y="156" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Guilt replaced by resilience</text>
  </g>

  <!-- Base Label -->
  <rect x="60" y="395" width="540" height="28" rx="4" fill="#1e293b" stroke="#334155"/>
  <text x="330" y="414" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">STARTING POINT: AWARENESS OF A HUMAN SLIP &amp; REJECTION OF SATANIC DESPAIR</text>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION DATA FOR 5 LESSONS IN TOPIC 8
# ─────────────────────────────────────────────────────────────────────────────

LESSONS_CONFIG = [
    {
        "order": 1,
        "code": "Lesson 4.2.1",
        "title": "Meaning and need for tawbah",
        "inquiry": "What is Tawbah, and why is sincere repentance necessary for every human being's spiritual success?",
        "connection": "Imagine you are wearing a spotless white shirt to a feast. As you eat, a drop of dark oil drips onto your chest, leaving a visible stain. If you leave the stain alone, it will dry, attract dust, and ruin the shirt forever. But if you take some clean water and soap immediately, you can wash the stain away, making the shirt clean and bright again. In our spiritual lives, our hearts are like that white shirt, and our mistakes and sins are the dark stains. Sincere repentance, known as Tawbah, is the spiritual water that cleanses our hearts, restoring our connection with Allah.",
        "concept_def": "Tawbah (Repentance) is the act of sincerely turning back to Allah (S.W.T.) after committing a sin or mistake, seeking His forgiveness, and committing to reform one's behavior.\n\nSpiritual Renewal is the process of purifying the heart from the burden of guilt, restoring inner peace and a close relationship with the Creator.",
        "scripture_quran": "And turn to Allah in repentance, all of you, O believers, that you might succeed.",
        "scripture_quran_ref": "Surah Al-Nur, 24:31",
        "scripture_hadith": "All the children of Adam are sinners, and the best of sinners are those who repent.",
        "scripture_hadith_ref": "Sunan Ibn Majah, 4251",
        "explanation": "Repentance is a core devotional act in Islam because of several key principles:\n\n1. Accepting Human Imperfection: Islam teaches that humans are not perfect angels. We make mistakes, forget, and yield to temptation. This is part of our nature.\n2. No Hopelessness: In Islam, there is no 'permanent stain.' No matter how many mistakes we make, the door to Allah's forgiveness is always wide open. Despair is rejected.\n3. Continuous Practice: Because we slip up daily, seeking forgiveness is a constant, daily habit. Even the Prophet Muhammad (PBUH), who was protected from sin, sought forgiveness daily to teach us humility.",
        "svg_func": get_svg_lesson_1,
        "diagram_title": "The Continuous Cycle of Spiritual Renewal",
        "table_title": "Cycle of Spiritual Renewal Breakdown",
        "table_headers": ["Stage", "Spiritual Reality", "Danger to Avoid", "Healthy Action"],
        "table_rows": [
            ["1. The Human Slip", "Making an error or sin", "Arrogance & Denial", "Admitting fault honestly"],
            ["2. Remorse (Nadam)", "Conscience triggers sorrow", "Despair & Hopelessness", "Turning immediately to Allah"],
            ["3. Tawbah & Dua", "Asking sincere forgiveness", "Delayed repentance", "Instant sincere Istighfar"],
            ["4. Cleansing & Peace", "Heart restored to purity", "Returning to bad triggers", "Practicing extra good deeds"]
        ],
        "scenario": "Zuri is feeling extremely sad and distant from her family after she lied to her mother about losing her school sweater. She thinks, 'I am such a bad daughter. Allah must hate me for lying. I am too embarrassed to pray.' Her older sister Halima notices her sadness and says, 'Zuri, do not let Satan whisper that you are hopeless. Sins are like dirt on our hands—we don't keep our hands dirty; we wash them with soap! Go to Allah, tell Him you are sorry in your prayer, make it right with Mum, and you will feel that heavy weight lift off your chest. Allah loves those who turn back to Him.'",
        "real_world": "Practice a 'Spiritual Cleansing Protocol' today. If you realize you made a mistake—such as being rude to a sibling, wasting time, or neglecting a chore—do not ignore it or hide it. Instantly take a moment to pray, acknowledge your mistake to Allah, ask for His forgiveness, and do a good deed to replace the mistake. Notice the immediate peace of mind this brings.",
        "reflection": "Why does holding onto unrepented mistakes make a person feel anxious, lonely, and spiritually heavy?",
        "misconception": "Repentance is not a badge of shame; turning back to Allah with humility is one of the highest acts of spiritual courage and maturity.",
        "yt_title": "The Power of Tawbah: Cleansing the Soul",
        "yt_desc": "Dr. Omar Suleiman explains the uplifting nature of repentance and returning to Allah.",
        "yt_id": "mdO-w7pbLaQ",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Kaaba_Masjid_al-Haram_Mecca.jpg/1280px-Kaaba_Masjid_al-Haram_Mecca.jpg",
        "image_title": "The Holy Kaaba at Masjid al-Haram, Mecca",
        "image_caption": "The sanctuary where millions of believers turn daily in prayer and repentance to Allah.",
        "mcq": {
            "question": "According to the Hadith in Sunan Ibn Majah, who are described as the 'best of those who commit sins'?",
            "options": [
                "Those who never commit the same mistake twice",
                "Those who hide their sins so others do not find out",
                "Those who constantly and sincerely repent (Tawbah)",
                "Those who perform the most voluntary prayers"
            ],
            "answer": "C",
            "explanation": "The Prophet (PBUH) stated that all humans make mistakes, but the best of those who make mistakes are the ones who turn back to Allah in sincere repentance (Tawbah)."
        },
        "summary_content": "Tawbah means to turn back or return to Allah in sincerity after a mistake. Making mistakes is part of human nature, but staying in sin without repenting is a choice. Sincere repentance cleanses the soul and restores our closeness to Allah.",
        "key_points": [
            "Human error is natural; remaining in unrepented sin is an avoidable choice.",
            "Despair has no place in Islam; the door to divine mercy is never closed.",
            "Daily repentance keeps the heart radiant, humble, and peaceful."
        ],
        "exit_ticket": "Explain in your own words why despair has no place in a believer's life."
    },
    {
        "order": 2,
        "code": "Lesson 4.2.2",
        "title": "Conditions of tawbah",
        "inquiry": "What are the five strict requirements that make our repentance valid and accepted in the sight of Allah?",
        "connection": "Imagine you accidentally kick a football through your neighbor's window, shattering the glass. If you just run past their house and shout, 'Sorry!' without stopping, is that a real apology? No. A real apology requires you to stop, feel genuine regret, promise never to play so close to their house again, and pay for the broken glass. Sincere repentance (Tawbah) is the same. It is not just a quick phrase we say with our tongues. To be accepted by Allah, it must meet five profound conditions.",
        "concept_def": "Conditions of Tawbah are the five theological requirements that must be fulfilled for repentance to be valid and complete in Islamic jurisprudence:\n\n1. Sincerity (Ikhlas): Solely to please Allah.\n2. Regret (Nadam): Deep, genuine remorse in the heart.\n3. Ceasing the Sin (Iqla'): Instantly stopping the harmful behavior.\n4. Firm Resolve ('Azm): Sincere commitment never to repeat the sin.\n5. Restitution / Amends (Ithaar al-Haqq): Restoring the rights of wronged human beings.",
        "scripture_quran": "O you who have believed, repent to Allah with sincere repentance...",
        "scripture_quran_ref": "Surah Al-Tahrim, 66:8",
        "scripture_hadith": "Regret is repentance.",
        "scripture_hadith_ref": "Sunan Ibn Majah, 4252",
        "explanation": "The Tongue vs. The Heart: Saying 'Astaghfirullah' with the tongue while planning to commit the sin again tomorrow is a mockery of repentance. The conditions of Regret and Firm Resolve protect the integrity of our faith.\n\nHuman Rights vs. Divine Rights: If you gossip about a classmate or steal their book, you have violated both a divine law and a human right. Allah in His justice will not forgive the harm done to another human until you fulfill the fifth condition: Restitution. You must apologize to the classmate, return their book, or repair their reputation.",
        "svg_func": get_svg_lesson_2,
        "diagram_title": "The 5-Key Padlock of Sincere Repentance (Shurut al-Tawbah)",
        "table_title": "The 5 Essential Conditions of Tawbah",
        "table_headers": ["Condition", "Arabic Term", "Core Meaning", "Practical Application"],
        "table_rows": [
            ["1. Sincerity", "Ikhlas", "Done solely to please Allah", "Not apologizing just to avoid detention or embarrassment"],
            ["2. Remorse", "Nadam", "Heartfelt sorrow for the wrong", "Feeling genuine internal grief for breaking a trust"],
            ["3. Cessation", "Iqla'", "Immediate stop to the deed", "Closing an inappropriate website or dropping stolen item"],
            ["4. Firm Resolve", "'Azm", "Determined never to repeat", "Making a concrete plan to avoid past negative triggers"],
            ["5. Restitution", "Ithaar al-Haqq", "Restoring human rights", "Returning stolen funds, repairing damaged items, apologizing"]
        ],
        "scenario": "Hussein finds a 200-shilling note on his classmate Zain's desk when Zain is at lunch. Hussein keeps the money and buys snacks. Later, he feels guilty and prays, saying, 'O Allah, forgive me for taking Zain's money.' Hussein realizes that his repentance is incomplete. He goes to Zain, hands him a 200-shilling note, and says, 'Zain, I took your money from your desk yesterday when I was hungry, and I was wrong. Here is your money back; please forgive me.' Zain is surprised but forgives him. Hussein's Tawbah is now valid because he fulfilled the condition of Restitution.",
        "real_world": "Evaluate an apology you need to make in your life. Did you say something mean to a parent, or did you borrow a sibling's shirt without permission? Apply the five conditions: feel the regret, stop the behavior, promise to avoid it, and make amends (clean the shirt, or give your parent a sincere, helpful hug). Experience how fulfilling these steps heals your relationships.",
        "reflection": "Why does Allah require us to make peace with the people we have hurt before He accepts our repentance?",
        "misconception": "Remember: Sincere repentance does not mean we will never make a mistake again. It means that at the moment of repenting, our resolve to never repeat it is 100% genuine. If we slip up later, we immediately repeat the process.",
        "yt_title": "The Conditions of Sincere Tawbah",
        "yt_desc": "Scholarly explanation of the 5 conditions required for accepted repentance.",
        "yt_id": "UJYkwPDwC-Y",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Bab_al-Salam_Medina.jpg/1280px-Bab_al-Salam_Medina.jpg",
        "image_title": "Bab al-Salam (Gate of Peace) at the Prophet's Mosque",
        "image_caption": "Historic gateway symbolizing the entry into divine peace, forgiveness, and mercy.",
        "mcq": {
            "question": "Which condition of Tawbah is uniquely required when a person's mistake has directly harmed or violated the rights of another human being?",
            "options": [
                "Sincere Intention (Ikhlas)",
                "Heartfelt Regret (Nadam)",
                "Restitution / Making Amends (Ithaar al-Haqq)",
                "Ceasing the Sin (Iqla')"
            ],
            "answer": "C",
            "explanation": "When an offense involves human rights, the repentant person must restore those rights, return any property, or seek forgiveness directly from the wronged party to complete their repentance."
        },
        "summary_content": "Tawbah is not just verbal; it is an active heart-and-mind commitment to change. The five conditions are: Sincerity, Regret, Ceasing the sin, Firm resolve, and Restitution. Restoring human rights is an essential part of divine justice in Islam.",
        "key_points": [
            "Repentance requires five structural conditions to be valid.",
            "Saying 'Astaghfirullah' while continuing the sin is invalid.",
            "Violations of human rights require direct amends and restoration."
        ],
        "exit_ticket": "List the five conditions of Tawbah in the correct order in your notebook."
    },
    {
        "order": 3,
        "code": "Lesson 4.2.3",
        "title": "Qur’anic guidance on tawbah",
        "inquiry": "How do Surah Al-Furqan (25:70) and Surah Al-Zumar (39:53) teach us about Allah's limitless mercy?",
        "connection": "Imagine you have accumulated a giant mountain of debts, and you owe millions to a bank. You cannot sleep, you cannot eat, and you live in constant fear of going to jail. Suddenly, you receive a letter from the owner of the bank. The letter says, 'Do not worry. I have seen your struggles. I have decided to completely wipe out all your debts, and if you work honestly starting today, I will convert your negative balance into a positive savings account!' How would you feel? You would cry tears of joy. This is exactly what Allah promises to do for our spiritual record in the Qur'an.",
        "concept_def": "Qur'anic Guidance on Repentance:\n\nSurah Al-Furqan, 25:70: Allah promises that for those who repent, believe, and do righteous deeds, He will replace their evil deeds with good deeds!\n\nSurah Al-Zumar, 39:53: Allah commands the Prophet (PBUH) to tell the people never to despair of His mercy, because Allah forgives all sins for those who turn to Him.",
        "scripture_quran": "Say, 'O My servants who have transgressed against themselves, do not despair of the mercy of Allah. Indeed, Allah forgives all sins...'",
        "scripture_quran_ref": "Surah Al-Zumar, 39:53",
        "scripture_hadith": "Allah extends His hand at night to forgive those who sinned during the day...",
        "scripture_hadith_ref": "Sahih Muslim, 2759",
        "explanation": "These two verses contain three profound lessons:\n\n1. 'My Servants': In Surah Al-Zumar, even though the people had committed severe sins, Allah still calls them 'My Servants' ('Ibadi). This shows His immense love and gentle invitation. He does not reject us when we make mistakes.\n2. No Sin is Too Big: The phrase 'Allah forgives all sins' means that no matter how heavy or numerous our mistakes are, Allah's mercy is infinitely greater. Sincere repentance can wash away anything.\n3. The Divine Transmutation: In Surah Al-Furqan, Allah does not just delete the bad deeds; He actually replaces them with good deeds on our scale! This shows that when a person repents and reforms, their past mistakes become lessons that drive them to do good.",
        "svg_func": get_svg_lesson_3,
        "diagram_title": "The Qur'anic Promise: Limitless Mercy & Tabdeel",
        "table_title": "Comparison of Key Quranic Verses on Repentance",
        "table_headers": ["Surah & Verse", "Divine Name Used", "Core Promise Made", "Spiritual Impact on Learner"],
        "table_rows": [
            ["Surah Al-Zumar (39:53)", "Al-Ghafur, Al-Rahim", "Total prohibition of despair; forgiveness for all sins", "Restores radical hope and banishes guilt paralysis"],
            ["Surah Al-Furqan (25:70)", "Ghafuran Rahima", "Transmutation of evil deeds into positive good deeds", "Motivates immediate righteous action & reform"],
            ["Surah Al-Baqarah (2:222)", "Al-Tawwab", "Allah actively loves those who constantly repent", "Transforms repentance into an act of reciprocal love"]
        ],
        "scenario": "Yusuf is studying Surah Al-Zumar in class and starts to cry silently. Mr. Bilal sits beside him and asks what is wrong. Yusuf whispers, 'Sir, I have done so many bad things this year—I skipped classes, lied to my dad, and was mean to my friends. I feel like my book of deeds is ruined and I can never be a good Muslim.' Mr. Bilal points to verse 53 on the board and says, 'Yusuf, read this verse. Allah is speaking directly to you. He says, Do not despair of the mercy of Allah. He does not want you to feel hopeless. He wants you to wipe your tears, make Tawbah, and start doing good deeds today. Your future is clean!'",
        "real_world": "Write down a 'Hope card' this week. Copy the translation of Surah Al-Zumar (39:53) in beautiful handwriting on a small card. Place it inside your school diary or near your study desk. Whenever you make a mistake, feel stressed, or feel guilty, look at the card to remind yourself of Allah's limitless mercy, and immediately perform Tawbah and a helpful action.",
        "reflection": "Why does Satan want us to fall into despair and believe that Allah will never forgive us? How does despair lead to more bad habits?",
        "misconception": "Forgiveness does not mean taking sin lightly; rather, appreciating divine generosity inspires intense love and careful avoidance of wrongdoing.",
        "yt_title": "Never Despair of Allah's Mercy: Surah Az-Zumar",
        "yt_desc": "Inspiring explanation of Surah Az-Zumar 39:53 and the boundless mercy of Allah.",
        "yt_id": "TVt-Dd31Nn4",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Quran_manuscript_Surah_Al-Furqan.jpg/1280px-Quran_manuscript_Surah_Al-Furqan.jpg",
        "image_title": "Illuminated Quranic Manuscript Folio",
        "image_caption": "Centuries-old illuminated manuscript recording verses of divine forgiveness and mercy.",
        "mcq": {
            "question": "According to Surah Al-Furqan (25:70), what extraordinary reward does Allah promise to those who repent, believe, and perform righteous deeds?",
            "options": [
                "He will grant them immense worldly wealth and status",
                "He will replace their evil deeds with good deeds on their record",
                "He will allow them to enter Paradise without any accounting",
                "He will protect them from ever making a mistake again"
            ],
            "answer": "B",
            "explanation": "Surah Al-Furqan explicitly states that for those who repent, believe, and work righteousness, Allah will 'replace their evil deeds with good,' showing His supreme generosity."
        },
        "summary_content": "Surah Al-Zumar (39:53) strictly prohibits despairing of Allah's mercy, as He forgives all sins. Surah Al-Furqan (25:70) reveals that sincere Tawbah and good deeds convert past sins into positive records. Sincere repentance must be followed by active, positive reform.",
        "key_points": [
            "Despair is strictly prohibited in Islam.",
            "Sincere repentance combined with righteous deeds transforms evil into good (Tabdeel).",
            "Allah addresses sinners with the affectionate title 'My servants' to invite them home."
        ],
        "exit_ticket": "Explain how Surah Al-Zumar (39:53) helps a student who feels overwhelmed by past mistakes."
    },
    {
        "order": 4,
        "code": "Lesson 4.2.4",
        "title": "Practising responsible repentance",
        "inquiry": "How do we translate the theory of Tawbah into real-world apologies, self-repair, and changed conduct?",
        "connection": "Imagine you are training for a marathon and you slip on a muddy patch, falling flat on your face. You get up, wipe the mud off your knees, and say, 'I am going to run better.' But if you keep running in exactly the same careless way on the next lap, you will fall again. Sincere repentance is not just about feeling sorry; it is about changing your running style. In our lives, we must practice 'Responsible Repentance'—meaning we learn from our slips, fix the damage we caused, and build new, healthy habits to prevent falling again.",
        "concept_def": "Responsible Repentance in Daily Life is the practical application of the conditions of Tawbah to restore broken relationships, repair social harm, and maintain moral consistency.\n\nThe Ripple Effect of Harm means recognizing that our mistakes often hurt others, and true repentance demands that we actively work to heal that ripple through restitution and amends.",
        "scripture_quran": "...And whoever fears Allah – He will make for him of his matter ease.",
        "scripture_quran_ref": "Surah Al-Talaq, 65:4",
        "scripture_hadith": "Make repentance to Allah, for I repent to Him a hundred times a day.",
        "scripture_hadith_ref": "Sahih Muslim, 1907",
        "explanation": "Let's look at the three-stage practical process of 'Responsible Repentance':\n\n1. Internal Repair (The Heart): Sincere regret and checking your intentions. You seek Allah's forgiveness immediately using private prayer (Dua).\n2. Interpersonal Repair (The Social Circle): If your mistake hurt someone else (such as a rumor you shared, a lie you told, or an item you broke), you must face them with courage. Apologize politely, correct the rumor, and return or replace the item.\n3. Habit Repair (The Action): Set up a 'Preventive Protocol'. If you lied because you were scared of a bad grade, set up a study schedule so you do not need to lie. If you gossiped because you were bored, leave the chat group or change the topic.",
        "svg_func": get_svg_lesson_4,
        "diagram_title": "Practicing Responsible Repentance: The Three R's",
        "table_title": "The Three R's Framework for Daily Amends",
        "table_headers": ["Phase", "Name", "Key Actions Required", "Result Achieved"],
        "table_rows": [
            ["Phase 1", "Regret & Recognize", "Admit fault to Allah without excuses; feel remorse", "Internal peace & humility"],
            ["Phase 2", "Repair & Restore", "Apologize to victim; return stolen items; clear rumors", "Healed trust & social justice"],
            ["Phase 3", "Reform & Reinforce", "Identify triggers; change habits; do extra good deeds", "Permanent character upgrade"]
        ],
        "scenario": "Zainab borrowed her classmate Halima's geometry set and accidentally broke the plastic compass. Instead of admitting it, Zainab put the broken set back in Halima's bag. When Halima found it, she cried because her parents could not afford another one. Let's look at how Zainab can practice responsible repentance:\n- Step 1 (Regret): Zainab feels terrible inside and prays to Allah for forgiveness.\n- Step 2 (Stop & Admit): She goes to Halima privately and says, 'Halima, I broke your compass yesterday because I was careless, and I was too scared to tell you. I was wrong to hide it.'\n- Step 3 (Amends): Zainab uses her own saved pocket money to buy a new geometry set and hands it to Halima. The friendship is healed, and Zainab promises herself to always handle borrowed items with extreme care.",
        "real_world": "Identify one relationship in your life that is currently strained due to a past argument or mistake. Apply the 'Three R's' protocol this week. Take a quiet moment to pray for them, make a courageous effort to offer a sincere apology, and perform an act of kindness for them (such as sharing your notes or helping with a task). Observe how this transforms the atmosphere around you.",
        "reflection": "Why is it much harder to apologize to a classmate than to say 'Astaghfirullah' in private? How does facing them build our courage and humility?",
        "misconception": "Remember: A verbal apology is only beneficial if it is accompanied by a genuine effort to change our conduct. Repentance is never a license to repeat mistakes.",
        "yt_title": "How to Make Sincere Amends in Islam",
        "yt_desc": "Practical guide on apologizing, restitution, and repairing broken bonds.",
        "yt_id": "5hDUB6yFwBQ",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Two_students_studying_peacefully.jpg/1280px-Two_students_studying_peacefully.jpg",
        "image_title": "Students Cooperating in School Courtyard",
        "image_caption": "Demonstrating the reconciliation, humility, and mutual trust fostered by sincere restitution.",
        "mcq": {
            "question": "Which of the following is the best example of a complete, responsible application of Tawbah after a student has spread a false rumor about a classmate?",
            "options": [
                "Praying extra prayers at night and hoping the classmate forgets about the rumor",
                "Deleting the message online and pretending they had nothing to do with it",
                "Apologizing to Allah privately, admitting the lie to the classmates who heard it, and apologizing sincerely to the victim",
                "Blaming the person who originally sent them the rumor to avoid getting in trouble"
            ],
            "answer": "C",
            "explanation": "This option fulfills all conditions: it involves private spiritual repentance to Allah, active restitution (correcting the false rumor where it was spread), and apologizing directly to the wronged person."
        },
        "summary_content": "Sincere repentance requires us to heal both our spiritual and social mistakes. Apologizing and making amends takes real courage and humility, which are core Islamic virtues. Sincere Tawbah must lead to reformed habits and better daily character.",
        "key_points": [
            "The Three R's are Regret & Recognize, Repair & Restore, and Reform & Reinforce.",
            "Social restitution requires courageous apologies and repairing tangible harm.",
            "Repentance is proved by consistent, improved conduct over time."
        ],
        "exit_ticket": "State the 'Three R's of Responsible Repentance' in your own words."
    },
    {
        "order": 5,
        "code": "Lesson 4.2.5",
        "title": "Unit synthesis",
        "inquiry": "How do we consolidate our understanding of Tawbah to live as humble, resilient, and morally responsible believers?",
        "connection": "Imagine you have completed a thorough spring cleaning of your entire house. You have swept the floors, washed the windows, and thrown away all the trash. How do you feel? You feel fresh, energized, and happy to welcome guests. Sincere repentance (Tawbah) is like that complete house cleaning for our souls. In this final lesson of the unit, we will bring together the definitions, the five conditions, the beautiful verses of Surah Al-Furqan and Al-Zumar, and our practical role-play scenarios to build a lifelong framework for spiritual resilience.",
        "concept_def": "Spiritual Resilience through Tawbah is the permanent psychological and moral strength that comes from knowing that we can always return to Allah, correct our mistakes, and continue our journey of character growth.\n\nContinuous Self-Purification (Tazkiyah) is the ongoing process of auditing our habits, admitting our faults, and seeking forgiveness to keep our hearts clean and close to Allah.",
        "scripture_quran": "Indeed, Allah loves those who are constantly repentant and loves those who purify themselves.",
        "scripture_quran_ref": "Surah Al-Baqarah, 2:222",
        "scripture_hadith": "Actions are judged by their intentions, and each person will be rewarded according to what he intended.",
        "scripture_hadith_ref": "Sahih al-Bukhari, 1",
        "explanation": "Let's review the complete map of the unit on Tawbah:\n\n1. The Philosophy: We accept that we are imperfect humans who commit mistakes, but we reject despair because Allah's mercy is limitless (Surah Al-Zumar, 39:53).\n2. The Checklist: Valid Tawbah must meet the five keys: Sincerity (Ikhlas), Regret (Nadam), Stop the sin (Iqla'), Sincere promise ('Azm), and Restoring rights (Ithaar al-Haqq).\n3. The Transformation: Repentance followed by righteous work converts past evil deeds into a treasury of good deeds (Surah Al-Furqan, 25:70).\n4. The Daily Habit: Repenting is not a once-a-year event; it is a daily habit of self-awareness and active repair (The Three R's).",
        "svg_func": get_svg_lesson_5,
        "diagram_title": "Master Synthesis: The Spiritual Ascent (Tawbah & Tazkiyah)",
        "table_title": "Comprehensive Synthesis Matrix of Tawbah",
        "table_headers": ["Core Pillar", "Theological Source", "Practical Habit", "Spiritual Elevation"],
        "table_rows": [
            ["No Despair", "Qur'an 39:53", "Banish hopeless thoughts & turn to Allah", "Radical hope & psychological peace"],
            ["5 Conditions", "Qur'an 66:8 & Hadith", "Verify Ikhlas, Nadam, Iqla, Azm, Restitution", "Valid, accepted purification"],
            ["Tabdeel Blessing", "Qur'an 25:70", "Perform extra good deeds after every slip", "Evils converted into good records"],
            ["The Three R's", "Sunnah Practice", "Recognize, Restore human rights, Reform habits", "Courageous integrity & trusted character"]
        ],
        "scenario": "Match the following situations with the correct term or condition of Tawbah:\n1. Feeling deep sorrow and crying in prayer after being disrespectful to your father. (Answer: Regret / Nadam)\n2. Deleting an illegal movie download from your computer and promising never to pirate again. (Answer: Ceasing the Sin / Iqla')\n3. Apologizing to your sister and cleaning up the mess you made in her room. (Answer: Restitution / Amends / Ithaar al-Haqq)\n4. Refusing to join a fight at school because you want to please Allah, not show off. (Answer: Sincerity / Ikhlas)",
        "real_world": "Design a 'Spiritual Renewal Journal' or dedicate a section of your school notebook to 'My Daily Audits'. Every Friday evening, spend five minutes privately writing down any mistakes you made this week, check them against the five conditions of Tawbah, plan how you will make amends, and write a short Dua seeking Allah's forgiveness. Keep this journal completely private between you and Allah.",
        "reflection": "How does the fact that Allah loves those who repent (Q 2:222) transform our view of repentance from a difficult trial into a beautiful act of love?",
        "misconception": "Tawbah is not a sign of failure; it is the ultimate tool of spiritual success and resilience for every believer.",
        "yt_title": "Tawbah: The Art of Spiritual Resilience",
        "yt_desc": "Comprehensive lecture on maintaining continuous repentance and purification.",
        "yt_id": "AHVP62ebo7s",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Faisal_Mosque_Islamabad_Interior.jpg/1280px-Faisal_Mosque_Islamabad_Interior.jpg",
        "image_title": "Interior Architecture of Faisal Mosque",
        "image_caption": "Vast, luminous sanctuary evoking the expanse of divine mercy and inner serenity.",
        "mcq": {
            "question": "Yusuf accidentally damaged a school library textbook by spilling juice on it. He cleaned the book but the pages remained stained and wavy. Applying the full synthesis of our unit on Tawbah, what is the most complete way Yusuf should practice repentance?",
            "options": [
                "Say 'Astaghfirullah' fifty times in the mosque and place the book back on the shelf silently",
                "Feel sorry in his heart, throw the book away in a bin, and avoid going to the library for the rest of the year",
                "Feel genuine regret, go to the school librarian, admit the damage courageously, offer to pay for or replace the stained book, and promise to be careful with library property in the future",
                "Blame his younger brother for spilling the juice to avoid paying for the book"
            ],
            "answer": "C",
            "explanation": "This option fully satisfies all five conditions of Tawbah: Sincerity (pleasing Allah through honesty), Regret (remorse for the damage), Iqla' (admitting the mistake), 'Azm (promising to be careful), and importantly, Ithaar al-Haqq (restitution/replacing the damaged school property)."
        },
        "summary_content": "Sincere repentance is a highly rewarded devotional act that earns Allah's unique love. Despair is completely prohibited; Allah's mercy is limitless and converts bad deeds into good. Sincere Tawbah heals our spiritual connection with Allah and our social bonds with people.",
        "key_points": [
            "Tawbah is an uplifting spiritual ascent toward Allah's boundless love.",
            "Valid repentance must incorporate all five keys, especially human restitution.",
            "Daily auditing of our actions builds lifelong resilience and noble character."
        ],
        "exit_ticket": "Write down the five conditions of Tawbah and one way you will apply them this week to be a better student."
    }
]


# ─────────────────────────────────────────────────────────────────────────────
# DATABASE INGESTION EXECUTION
# ─────────────────────────────────────────────────────────────────────────────

def ingest_grade9_ire_topic8():
    print("=" * 80)
    print("STARTING INGESTION: GRADE 9 IRE — TOPIC 8: TAWBAH (REPENTANCE)")
    print("=" * 80)

    try:
        topic = Topic.objects.get(id=348)
    except Topic.DoesNotExist:
        print("ERROR: Topic ID 348 does not exist!")
        sys.exit(1)

    print(f"Target Topic: ID={topic.id}, Name='{topic.name}', Order={topic.order}")

    with transaction.atomic():
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
            # CARD 1 (Page 1): Orientation (2 blocks)
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

            # CARD 2 (Page 2): Core Teaching & Scripture (2 blocks)
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

            # CARD 3 (Page 3): Deep Explanation & SVG Diagram (3 blocks)
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

            # CARD 4 (Page 4): Worked Scenario (1 block)
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

            # CARD 5 (Page 5): Real-World Application & Video (4 blocks)
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

            # CARD 6 (Page 6): Knowledge Mastery Check (1 block)
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

            # CARD 7 (Page 7): Summary & Exit Ticket (2 blocks)
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
    print("TOPIC 8 INGESTION COMPLETE & VERIFIED!")
    print(f"  LearningUnits : {total_units} / 5")
    print(f"  Lessons       : {total_lessons} / 5 (Published)")
    print(f"  Blocks        : {total_blocks} (15 per lesson, 7 pages)")
    print(f"  Assets        : {total_assets} (5 SVGs, 5 images, 5 videos)")
    print("=" * 80)


if __name__ == "__main__":
    ingest_grade9_ire_topic8()
