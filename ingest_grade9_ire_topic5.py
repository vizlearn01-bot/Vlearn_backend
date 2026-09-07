"""
VLearn CBC Grade 9 IRE — Topic 5: Belief in the Last Day (Yawm al-Qiyamah)
Production Ingestion and Enrichment Script for all 5 Lessons

Target Topic in DB: Topic ID 345 (Subject: IRE ID 53, Grade: Grade 9 ID 18)
Curriculum: CBC Kenya Grade 9 IRE Strand 3.0 (Pillars of Iman), Sub-strand 3.1
"""

import os
import sys
import re
import django
from django.db import transaction
from django.utils import timezone

# Setup Django Environment
sys.path.append("/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)


def clean_text(text: str) -> str:
    """Removes bracket citations and internal pedagogical tags."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(
        r'\[(VISUAL|QURAN REFERENCE|HADITH REFERENCE|BIBLE REFERENCE|REAL WORLD APPLICATION|REFLECTION|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|HISTORICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|MAP|TIMELINE|COMPARISON|INFOGRAPHIC|SVG)[^\]]*\]',
        '', text, flags=re.IGNORECASE
    )
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    return text.strip()


def clean_dict(data):
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, dict):
        return {k: clean_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_dict(item) for item in data]
    return data


# ─── 5 PEDAGOGICAL VECTOR SVGS (viewBox="0 0 880 440", theme #0f172a) ───────

def get_svg_lesson_1():
    """Lesson 3.1.1: Chronological Sequence of the Last Day (Yawm al-Qiyamah)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="stage1Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#9f1239"/>
    </linearGradient>
    <linearGradient id="stage2Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="stage3Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0ea5e9"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="stage4Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <filter id="shadow1" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <!-- Background Base -->
  <rect width="880" height="440" fill="url(#bg1)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <!-- Main Header -->
  <text x="440" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle" letter-spacing="0.5">CHRONOLOGICAL SEQUENCE OF THE LAST DAY (YAWM AL-QIYAMAH)</text>
  <text x="440" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Metaphysical Progression: From the First Blast to the Eternal Gathering on the Plain of Mahshar</text>

  <!-- Stage 1: The First Trumpet (Cosmic Cessation) -->
  <g transform="translate(35, 90)" filter="url(#shadow1)">
    <rect width="185" height="305" rx="12" fill="#1e293b" stroke="#f43f5e" stroke-width="1.8"/>
    <rect width="185" height="42" rx="12" fill="url(#stage1Grad)"/>
    <text x="92" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">1. COSMIC CESSATION</text>
    <text x="92" y="60" fill="#fb7185" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">FIRST TRUMPET BLAST</text>
    <text x="14" y="86" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10" font-weight="600">• Blown by Angel Israfeel</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Universal physical death</text>
    <text x="14" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Stars dim &amp; disperse</text>
    <text x="14" y="154" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Mountains crumble to dust</text>
    <text x="14" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Earthly life terminates</text>
    <text x="14" y="198" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• All creation falls silent</text>
    <rect x="12" y="240" width="161" height="48" rx="8" fill="#0f172a" stroke="#be123c" stroke-width="1"/>
    <text x="92" y="258" fill="#fb7185" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Surah Az-Zumar 39:68</text>
    <text x="92" y="274" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">"The Horn will be blown..."</text>
  </g>

  <!-- Flow Arrow 1 -> 2 -->
  <g transform="translate(220, 230)">
    <line x1="0" y1="0" x2="25" y2="0" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="4 2"/>
    <polygon points="25,-4 32,0 25,4" fill="#f59e0b"/>
  </g>

  <!-- Stage 2: The Second Trumpet & Ba'th -->
  <g transform="translate(252, 90)" filter="url(#shadow1)">
    <rect width="185" height="305" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="1.8"/>
    <rect width="185" height="42" rx="12" fill="url(#stage2Grad)"/>
    <text x="92" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">2. RESURRECTION</text>
    <text x="92" y="60" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">AL-BA'TH (RE-CREATION)</text>
    <text x="14" y="86" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10" font-weight="600">• Second Trumpet sounded</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Physical body rebuilt</text>
    <text x="14" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Souls reunited with frames</text>
    <text x="14" y="154" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Emergence from graves</text>
    <text x="14" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Divine power demonstrated</text>
    <text x="14" y="198" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Literal, physical reality</text>
    <rect x="12" y="240" width="161" height="48" rx="8" fill="#0f172a" stroke="#d97706" stroke-width="1"/>
    <text x="92" y="258" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Surah Ya-Sin 36:51</text>
    <text x="92" y="274" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">"From graves to Lord hasten"</text>
  </g>

  <!-- Flow Arrow 2 -> 3 -->
  <g transform="translate(437, 230)">
    <line x1="0" y1="0" x2="25" y2="0" stroke="#0ea5e9" stroke-width="2.5" stroke-dasharray="4 2"/>
    <polygon points="25,-4 32,0 25,4" fill="#0ea5e9"/>
  </g>

  <!-- Stage 3: The Gathering (Hashr) -->
  <g transform="translate(469, 90)" filter="url(#shadow1)">
    <rect width="185" height="305" rx="12" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.8"/>
    <rect width="185" height="42" rx="12" fill="url(#stage3Grad)"/>
    <text x="92" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">3. THE GATHERING</text>
    <text x="92" y="60" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">AL-HASHR (MAHSHAR)</text>
    <text x="14" y="86" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10" font-weight="600">• Assembled on vast plain</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• All human generations</text>
    <text x="14" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Worldly status erased</text>
    <text x="14" y="154" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Intense focus on destiny</text>
    <text x="14" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Wealth &amp; lineage useless</text>
    <text x="14" y="198" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Only righteous deeds count</text>
    <rect x="12" y="240" width="161" height="48" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
    <text x="92" y="258" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Surah Al-Kahf 18:47</text>
    <text x="92" y="274" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">"We gather and leave not one"</text>
  </g>

  <!-- Flow Arrow 3 -> 4 -->
  <g transform="translate(654, 230)">
    <line x1="0" y1="0" x2="25" y2="0" stroke="#10b981" stroke-width="2.5" stroke-dasharray="4 2"/>
    <polygon points="25,-4 32,0 25,4" fill="#10b981"/>
  </g>

  <!-- Stage 4: Divine Judgment (Hisab & Mizan) -->
  <g transform="translate(686, 90)" filter="url(#shadow1)">
    <rect width="185" height="305" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="1.8"/>
    <rect width="185" height="42" rx="12" fill="url(#stage4Grad)"/>
    <text x="92" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">4. DIVINE RECKONING</text>
    <text x="92" y="60" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">HISAB &amp; DESTINY</text>
    <text x="14" y="86" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10" font-weight="600">• Presentation of records</text>
    <text x="14" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Scales of Justice (Mizan)</text>
    <text x="14" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Body parts bear witness</text>
    <text x="14" y="154" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Crossing the Sirat bridge</text>
    <text x="14" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Intercession (Shafa'ah)</text>
    <text x="14" y="198" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Eternal Abode: Jannah/Fire</text>
    <rect x="12" y="240" width="161" height="48" rx="8" fill="#0f172a" stroke="#047857" stroke-width="1"/>
    <text x="92" y="258" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Surah Al-Anbiya 21:47</text>
    <text x="92" y="274" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">"We place scales of justice"</text>
  </g>
</svg>"""


def get_svg_lesson_2():
    """Lesson 3.1.2: The Divine Scale (Mizan) and Accounting (Hisab) Framework"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
    <linearGradient id="redGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#b91c1c"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <filter id="shadow2" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg2)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <!-- Header -->
  <text x="440" y="40" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE DIVINE SCALE (AL-MIZAN) &amp; ACCOUNTING (HISAB) FRAMEWORK</text>
  <text x="440" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">The Perfect Balance of Justice: Weighing Deeds, Sincerity, and Moral Character Before Allah</text>

  <!-- Center Scale Pillar & Fulcrum -->
  <g transform="translate(440, 75)">
    <!-- Vertical Column -->
    <rect x="-6" y="10" width="12" height="150" fill="#64748b" rx="4"/>
    <circle cx="0" cy="15" r="14" fill="url(#goldGrad)" stroke="#fef08a" stroke-width="2"/>
    <!-- Balanced Crossbeam slightly tipped toward good deeds (right side of picture/heavy side) -->
    <line x1="-240" y1="35" x2="240" y2="15" stroke="#f59e0b" stroke-width="5" stroke-linecap="round"/>
    <!-- Chains to Left Pan (Transgressions / Light) -->
    <line x1="-230" y1="35" x2="-260" y2="105" stroke="#94a3b8" stroke-width="1.5"/>
    <line x1="-230" y1="35" x2="-200" y2="105" stroke="#94a3b8" stroke-width="1.5"/>
    <!-- Chains to Right Pan (Righteous Deeds / Heavy) -->
    <line x1="230" y1="15" x2="200" y2="100" stroke="#94a3b8" stroke-width="1.5"/>
    <line x1="230" y1="15" x2="260" y2="100" stroke="#94a3b8" stroke-width="1.5"/>
    <!-- Base -->
    <path d="M -40,160 L 40,160 L 25,145 L -25,145 Z" fill="#475569"/>
    <!-- Central Multiplier Badge -->
    <rect x="-115" y="175" width="230" height="52" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.8"/>
    <text x="0" y="196" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">SUPREME MULTIPLIER: AKHLAQ</text>
    <text x="0" y="214" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">"Nothing is heavier on the Mizan than Good Character"</text>
  </g>

  <!-- Left Card: Heavy Side / Right Hand (Success) -->
  <g transform="translate(45, 95)" filter="url(#shadow2)">
    <rect width="280" height="305" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="1.8"/>
    <rect width="280" height="42" rx="12" fill="url(#greenGrad)"/>
    <text x="140" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">HEAVY SIDE: SUCCESS (HASANAT)</text>
    <rect x="20" y="52" width="240" height="20" rx="4" fill="#064e3b"/>
    <text x="140" y="66" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">BOOK RECEIVED IN RIGHT HAND</text>
    
    <text x="20" y="96" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Sincerity of Intention (Ikhlas)</text>
    <text x="20" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Noble Character (Husn al-Khuluq)</text>
    <text x="20" y="144" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Establishing Salat &amp; Daily Prayers</text>
    <text x="20" y="168" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Honest Transactions &amp; Charity</text>
    <text x="20" y="192" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Kindness to Parents &amp; Neighbours</text>
    <text x="20" y="216" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Sincere Repentance (Tawbah)</text>

    <rect x="18" y="244" width="244" height="46" rx="8" fill="#0f172a" stroke="#047857" stroke-width="1"/>
    <text x="140" y="262" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Surah Al-Qari'ah 101:6-7</text>
    <text x="140" y="278" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">"He whose scales are heavy is in pleasant life"</text>
  </g>

  <!-- Right Card: Light Side / Burdened Scale (Transgressions) -->
  <g transform="translate(555, 95)" filter="url(#shadow2)">
    <rect width="280" height="305" rx="12" fill="#1e293b" stroke="#ef4444" stroke-width="1.8"/>
    <rect width="280" height="42" rx="12" fill="url(#redGrad)"/>
    <text x="140" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">LIGHT SIDE: BURDEN (SAYYI'AT)</text>
    <rect x="20" y="52" width="240" height="20" rx="4" fill="#450a0a"/>
    <text x="140" y="66" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">BOOK IN LEFT HAND / BEHIND BACK</text>

    <text x="20" y="96" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Injustice &amp; Oppression (Dhulm)</text>
    <text x="20" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Pride, Arrogance &amp; Mockery</text>
    <text x="20" y="144" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Cheating, Dishonesty &amp; Theft</text>
    <text x="20" y="168" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Backbiting (Gheebah) &amp; Slander</text>
    <text x="20" y="192" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Ostentation (Riya' / Showing off)</text>
    <text x="20" y="216" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Unrepented Sins &amp; Corrupt Speech</text>

    <rect x="18" y="244" width="244" height="46" rx="8" fill="#0f172a" stroke="#b91c1c" stroke-width="1"/>
    <text x="140" y="262" fill="#f87171" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Surah Al-Haqqah 69:25</text>
    <text x="140" y="278" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">"I wish I had not been given my record"</text>
  </g>

  <!-- Bottom Hisab Protocol Pill -->
  <g transform="translate(325, 345)">
    <rect width="230" height="55" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="115" y="22" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">AL-HISAB (THE AUDIT)</text>
    <text x="115" y="38" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Questioned on youth, wealth, time &amp; deeds.</text>
    <text x="115" y="50" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Body limbs bear witness (Surah Ya-Sin 36:65)</text>
  </g>
</svg>"""


def get_svg_lesson_3():
    """Lesson 3.1.3: The Crossing of the Sirat Bridge & Prophetic Intercession (Shafa'ah)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="bridgeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="50%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#34d399"/>
    </linearGradient>
    <linearGradient id="shafaahGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <filter id="glow3" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.45"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg3)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="40" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE CROSSING OF THE SIRAT &amp; PROPHETIC INTERCESSION (SHAFA'AH)</text>
  <text x="440" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">Traversal Over the Abyss Guided by the Light of Iman and the Merciful Supplication of the Prophet (PBUH)</text>

  <!-- Left Card: The Sirat Bridge Dynamics -->
  <g transform="translate(45, 85)" filter="url(#glow3)">
    <rect width="250" height="320" rx="12" fill="#1e293b" stroke="#0284c7" stroke-width="1.8"/>
    <rect width="250" height="40" rx="12" fill="#0284c7"/>
    <text x="125" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">THE SIRAT BRIDGE</text>
    
    <text x="16" y="62" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">CHARACTERISTICS &amp; REALITY</text>
    <text x="16" y="84" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">• Path established over Jahannam</text>
    <text x="16" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Sharper than a sword, very thin</text>
    <text x="16" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Covered in dense darkness</text>
    <text x="16" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Iron hooks &amp; clamps (Kalalib)</text>

    <text x="16" y="180" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">CROSSING SPEEDS BY DEEDS</text>
    <text x="16" y="202" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Like a flash of lightning</text>
    <text x="16" y="222" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Like swift gusting wind</text>
    <text x="16" y="242" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Like fast galloping horses</text>
    <text x="16" y="262" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Running, walking, or crawling</text>

    <rect x="14" y="278" width="222" height="36" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
    <text x="125" y="294" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Surah Maryam 19:71-72</text>
    <text x="125" y="306" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">"Then We will save those who feared"</text>
  </g>

  <!-- Center Card: Prophetic Intercession (Shafa'ah) -->
  <g transform="translate(315, 85)" filter="url(#glow3)">
    <rect width="250" height="320" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="1.8"/>
    <rect width="250" height="40" rx="12" fill="url(#shafaahGrad)"/>
    <text x="125" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">PROPHETIC SHAFA'AH</text>

    <text x="16" y="62" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">THE PROPHET'S ADVOCACY</text>
    <text x="16" y="84" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">• Prophet Muhammad (PBUH) stands</text>
    <text x="16" y="104" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Constant prayer at the bridge:</text>
    
    <rect x="14" y="112" width="222" height="34" rx="6" fill="#0f172a" stroke="#d97706" stroke-width="1"/>
    <text x="125" y="126" fill="#fde68a" font-family="system-ui, sans-serif" font-size="9.5" font-weight="800" text-anchor="middle">"Rabbi Sallim, Sallim!"</text>
    <text x="125" y="139" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">(O My Lord, save them! Save them!)</text>

    <text x="16" y="168" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">DIVINE PREREQUISITES</text>
    <text x="16" y="190" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• 1. Permission (Idhn) from Allah</text>
    <text x="16" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• 2. Divine Approval (Rida) for soul</text>
    <text x="16" y="230" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• 3. Sincere Iman (not pure Shirk)</text>
    <text x="16" y="250" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Expression of Mercy, not arbitrary</text>

    <rect x="14" y="278" width="222" height="36" rx="6" fill="#0f172a" stroke="#d97706" stroke-width="1"/>
    <text x="125" y="294" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Surah Ta-Ha 20:109</text>
    <text x="125" y="306" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">"No intercession except by His permission"</text>
  </g>

  <!-- Right Card: The Light of Iman (Nur al-Iman) -->
  <g transform="translate(585, 85)" filter="url(#glow3)">
    <rect width="250" height="320" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="1.8"/>
    <rect width="250" height="40" rx="12" fill="#10b981"/>
    <text x="125" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">THE LIGHT OF IMAN</text>

    <text x="16" y="62" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">ILLUMINATION IN DARKNESS</text>
    <text x="16" y="84" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">• Believers receive radiant light</text>
    <text x="16" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Shines in front and on their right</text>
    <text x="16" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Proportional to sincerity in life</text>
    <text x="16" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Some light like mountain, some thumb</text>

    <text x="16" y="180" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">CONTRAST WITH HYPOCRISY</text>
    <text x="16" y="202" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Hypocrites have light extinguished</text>
    <text x="16" y="222" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Stumble in blinding abyss</text>
    <text x="16" y="242" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Safe arrival at Gates of Jannah</text>
    <text x="16" y="262" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Welcomed by angels in peace</text>

    <rect x="14" y="278" width="222" height="36" rx="6" fill="#0f172a" stroke="#047857" stroke-width="1"/>
    <text x="125" y="294" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Surah Al-Hadid 57:12</text>
    <text x="125" y="306" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" text-anchor="middle">"Their light running before them &amp; on right"</text>
  </g>
</svg>"""


def get_svg_lesson_4():
    """Lesson 3.1.4: The Eternal Abodes: Jannah (Paradise) vs. Jahannam (Hellfire)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="jannahGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="50%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="jahannamGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="50%" stop-color="#dc2626"/>
      <stop offset="100%" stop-color="#991b1b"/>
    </linearGradient>
    <filter id="shadow4" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg4)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <!-- Header -->
  <text x="440" y="40" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE ETERNAL ABODES: JANNAH (PARADISE) VS. JAHANNAM (HELLFIRE)</text>
  <text x="440" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">The Ultimate Consummation of Divine Justice, Sovereign Mercy, and Human Moral Responsibility</text>

  <!-- Left Card: Jannah (Paradise) -->
  <g transform="translate(45, 85)" filter="url(#shadow4)">
    <rect width="370" height="320" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect width="370" height="42" rx="12" fill="url(#jannahGrad)"/>
    <text x="185" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">JANNAH: DAR AL-SALAM (ABODE OF PEACE)</text>
    
    <rect x="25" y="52" width="160" height="20" rx="4" fill="#064e3b"/>
    <text x="105" y="66" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">THE PROMISE TO THE RIGHTEOUS</text>

    <circle cx="30" cy="95" r="4" fill="#34d399"/>
    <text x="42" y="94" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Supreme Delights:</text>
    <text x="42" y="109" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Flowing rivers of water, milk, honey, and pure drinks.</text>

    <circle cx="30" cy="135" r="4" fill="#34d399"/>
    <text x="42" y="134" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Perfect Existence:</text>
    <text x="42" y="149" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">No sickness, fatigue, sadness, malice, or death.</text>

    <circle cx="30" cy="175" r="4" fill="#34d399"/>
    <text x="42" y="174" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Ascending Ranks:</text>
    <text x="42" y="189" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Eight glorious gates; highest is Jannat al-Firdaws.</text>

    <circle cx="30" cy="215" r="4" fill="#34d399"/>
    <text x="42" y="214" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">The Ultimate Reward:</text>
    <text x="42" y="229" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Gazing upon the Countenance of Allah &amp; His Rida.</text>

    <rect x="20" y="252" width="330" height="48" rx="8" fill="#0f172a" stroke="#047857" stroke-width="1"/>
    <text x="185" y="271" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Surah Al-Kahf 18:107</text>
    <text x="185" y="287" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">"Gardens of Firdaws will be their lodging"</text>
  </g>

  <!-- Center 'VS' Hub -->
  <g transform="translate(440, 245)">
    <circle cx="0" cy="0" r="24" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="0" y="6" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="900" text-anchor="middle">VS</text>
  </g>

  <!-- Right Card: Jahannam (Hellfire) -->
  <g transform="translate(465, 85)" filter="url(#shadow4)">
    <rect width="370" height="320" rx="12" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <rect width="370" height="42" rx="12" fill="url(#jahannamGrad)"/>
    <text x="185" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">JAHANNAM: DAR AL-BAWAR (ABODE OF RUIN)</text>
    
    <rect x="25" y="52" width="180" height="20" rx="4" fill="#450a0a"/>
    <text x="115" y="66" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">CONSEQUENCE OF TRANSGRESSION</text>

    <circle cx="30" cy="95" r="4" fill="#f87171"/>
    <text x="42" y="94" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Divine Justice:</text>
    <text x="42" y="109" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Retribution for willful disbelief, cruelty, and tyranny.</text>

    <circle cx="30" cy="135" r="4" fill="#f87171"/>
    <text x="42" y="134" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Nature of Punishment:</text>
    <text x="42" y="149" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Intense heat, confinement, darkness, and bitterness.</text>

    <circle cx="30" cy="175" r="4" fill="#f87171"/>
    <text x="42" y="174" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Psychological Remorse:</text>
    <text x="42" y="189" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Endless sorrow over wasted opportunities and defiance.</text>

    <circle cx="30" cy="215" r="4" fill="#f87171"/>
    <text x="42" y="214" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">The Ultimate Loss:</text>
    <text x="42" y="229" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Permanent veil and separation from Allah's mercy.</text>

    <rect x="20" y="252" width="330" height="48" rx="8" fill="#0f172a" stroke="#b91c1c" stroke-width="1"/>
    <text x="185" y="271" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Surah An-Naba 78:21-22</text>
    <text x="185" y="287" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">"Hell is a place of ambush, for transgressors a return"</text>
  </g>
</svg>"""


def get_svg_lesson_5():
    """Lesson 3.1.5: The Daily Integrity & Muraqabah Funnel"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bg5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="filter1Grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#6366f1"/>
      <stop offset="100%" stop-color="#4f46e5"/>
    </linearGradient>
    <linearGradient id="filter2Grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="filter3Grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#06b6d4"/>
      <stop offset="100%" stop-color="#0891b2"/>
    </linearGradient>
    <linearGradient id="outcomeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <filter id="shadow5" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="880" height="440" fill="url(#bg5)" rx="14"/>
  <rect x="15" y="15" width="850" height="410" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="440" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE DAILY INTEGRITY &amp; MURAQABAH FUNNEL</text>
  <text x="440" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11.5" text-anchor="middle">How God-Consciousness and Awareness of the Last Day Shape Conduct Across All Spheres of Life</text>

  <!-- Filter 1: Private Choice (Top of Funnel) -->
  <g transform="translate(100, 80)" filter="url(#shadow5)">
    <rect width="680" height="66" rx="10" fill="#1e293b" stroke="#6366f1" stroke-width="1.8"/>
    <rect width="210" height="66" rx="10" fill="url(#filter1Grad)"/>
    <text x="105" y="28" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">FILTER 1: PRIVATE</text>
    <text x="105" y="46" fill="#e0e7ff" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">The Unseen Chamber</text>
    
    <text x="230" y="27" fill="#a5b4fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Question: "Is my action righteous when no human is observing?"</text>
    <text x="230" y="45" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Active awareness of Kiraman Katibin &amp; Al-Raqib (The Watchful).</text>
    <text x="230" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">• Academic honesty during exams; avoiding private cheating and secret sins.</text>
  </g>

  <!-- Downward Arrow 1 -->
  <polygon points="434,152 446,152 440,160" fill="#f59e0b"/>

  <!-- Filter 2: Public Speech & Digital Interaction (Middle) -->
  <g transform="translate(140, 166)" filter="url(#shadow5)">
    <rect width="600" height="66" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.8"/>
    <rect width="200" height="66" rx="10" fill="url(#filter2Grad)"/>
    <text x="100" y="28" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">FILTER 2: SPEECH</text>
    <text x="100" y="46" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Tongue &amp; Digital Screen</text>

    <text x="220" y="27" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Question: "Does my speech build truth and dignity?"</text>
    <text x="220" y="45" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• "Speak good or remain silent" (Bukhari 6018).</text>
    <text x="220" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">• No cyberbullying, backbiting (Gheebah), trolling, or forwarding unverified news.</text>
  </g>

  <!-- Downward Arrow 2 -->
  <polygon points="434,238 446,238 440,246" fill="#06b6d4"/>

  <!-- Filter 3: Social Contribution & Justice (Narrow End) -->
  <g transform="translate(180, 252)" filter="url(#shadow5)">
    <rect width="520" height="66" rx="10" fill="#1e293b" stroke="#06b6d4" stroke-width="1.8"/>
    <rect width="180" height="66" rx="10" fill="url(#filter3Grad)"/>
    <text x="90" y="28" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">FILTER 3: ACTION</text>
    <text x="90" y="46" fill="#cffafe" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">The Active Hand</text>

    <text x="200" y="27" fill="#67e8f9" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Question: "Am I protecting trusts (Amanah) and aiding others?"</text>
    <text x="200" y="45" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">• Serving parents, cleaning schools, assisting vulnerable neighbors.</text>
    <text x="200" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">• Returning lost items immediately; upholding justice in all relationships.</text>
  </g>

  <!-- Downward Arrow 3 -->
  <polygon points="434,324 446,324 440,332" fill="#10b981"/>

  <!-- Outcome Box: Sincere Heart & Easy Audit -->
  <g transform="translate(210, 338)" filter="url(#shadow5)">
    <rect width="460" height="65" rx="12" fill="url(#outcomeGrad)" stroke="#34d399" stroke-width="1.5"/>
    <text x="230" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="900" text-anchor="middle">HARVEST: A RADIANT RECORD &amp; AN EASY AUDIT (HISAB YASEER)</text>
    <text x="230" y="44" fill="#ecfdf5" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Inner peace in this world, radiant light on the Sirat bridge,</text>
    <text x="230" y="57" fill="#d1fae5" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">and joyful receipt of the Book of Deeds in the Right Hand.</text>
  </g>
</svg>"""


# ─── LESSONS COMPLETE DATA SPECIFICATION (TOPIC 5) ───────────────────────────

LESSONS_DATA = [
    # =========================================================================
    # LESSON 1: Resurrection and gathering
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Resurrection and Gathering (Al-Ba'th wal-Hashr)",
        "lesson_title": "Resurrection and gathering",
        "unit_description": "Investigation into the primary metaphysical milestones of Yawm al-Qiyamah: the sounding of the Trumpet, physical resurrection (Ba'th), and the universal assembly (Hashr) on the plain of Mahshar.",
        "diagram_title": "Chronological Sequence of the Last Day",
        "svg_fn": get_svg_lesson_1,
        "image": {
            "title": "The Great Gathering of Believers (The Plains of Makkah and Arafat during Hajj)",
            "url": "https://upload.wikimedia.org/wikipedia/commons/7/79/The_Kaaba_during_Hajj.jpg",
            "caption": "Millions of pilgrims assembled on the open plains of Makkah in simple white garments without distinction of worldly status, serving as an earthly pedagogical reminder of the Great Gathering (Hashr) on the plain of Mahshar before Allah (SWT).",
            "author": "Muhammad Mahdi Karim",
            "source": "Wikimedia Commons",
            "licensing": "GFDL 1.2 / CC BY-SA 3.0"
        },
        "youtube": {
            "youtube_id": "mdO-w7pbLaQ",
            "title": "When Allah Addresses the Gathering | Judgment Day | Dr. Omar Suleiman",
            "description": "An exploration of the Great Gathering (Hashr) on the plain of Mahshar, examining how every human soul stands before Allah with absolute accountability."
        },
        "inquiry_question": "What are the first major events of the Last Day, and how does belief in them shape our moral responsibility?",
        "connection": "Imagine a giant school assembly where every student who has ever attended the school, from the first day it opened until today, is gathered on the sports field. Each student is called by name to receive their final report card in front of everyone. This is a very small analogy for the Great Gathering (Hashr). In this lesson, we will explore the absolute beginning of the Last Day: the Resurrection (Ba'th) and the Gathering (Hashr), when all of humanity will be brought back to life to stand before Allah (S.W.T.).",
        "goals": [
            "Understand the meaning and reality of Resurrection (Ba'th) as the literal physical re-creation of human bodies.",
            "Describe the cosmic events accompanying the two blasts of the Trumpet sounded by Angel Israfeel.",
            "Explain the conditions and nature of the Great Gathering (Hashr) on the plain of Mahshar.",
            "Connect the conviction in physical resurrection to daily ethical responsibility and speech discipline."
        ],
        "authoritative_concept": (
            "### Theological Foundations of Ba'th and Hashr\n\n"
            "- **Resurrection (*Ba'th*):** The literal act of Allah bringing all deceased human beings back to physical and biological life on the Day of Judgment. The Qur'an affirms that the Originator who created human beings from nothing the first time can easily reassemble bones, flesh, and even fingertips (*Surah Al-Qiyamah 75:3-4*).\n"
            "- **Gathering (*Hashr*):** The universal assembly of all resurrected human beings on a vast, leveled plain known as the plain of *Mahshar* to await divine reckoning.\n"
            "- **The Trumpet (*Al-Sur*):** The cosmic instrument entrusted to Angel Israfeel. The first blast initiates universal cessation (*Sa'iq*), while the second blast inaugurates universal resurrection (*Ba'th*)."
        ),
        "scripture_panel": (
            "> \"And the Horn will be blown; and at once from the graves to their Lord they will hasten. They will say, 'O woe to us! Who has raised us up from our sleeping place?' [The reply will be], 'This is what the Most Merciful had promised, and the messengers told the truth.'\"\n"
            "— **Surah Ya-Sin (36:51-52)**\n\n"
            "> \"Whoever believes in Allah and the Last Day, let him speak good or remain silent. And whoever believes in Allah and the Last Day, let him honor his neighbor.\"\n"
            "— **Prophet Muhammad (PBUH)**, *Sahih al-Bukhari (6018)*"
        ),
        "deep_explanation": (
            "### The Unfolding Journey of the Last Day\n\n"
            "The journey of the Last Day begins with an orderly metaphysical sequence that demonstrates Allah's absolute sovereignty over the created cosmos:\n\n"
            "1. **The First Blast of the Trumpet (*Nafkhat al-Sa'iq*):**\n"
            "   Allah commands the Angel Israfeel to blow the Trumpet, instantly bringing all worldly biological life to an end. The physical order of the universe collapses—mountains are leveled into flying dust, oceans boil, and celestial bodies disperse (*Surah At-Takwir 81:1-6*). This marks the absolute conclusion of the earthly examination period.\n\n"
            "2. **The Second Blast of the Trumpet (*Nafkhat al-Ba'th*):**\n"
            "   Following a period decreed by Allah, Israfeel blows the Trumpet a second time. At this divine command, every decomposed particle of every human being is miraculously reconstructed from the earth. Souls are reunited with their physical bodies, and humanity emerges from their graves in full physical reality (*Surah Az-Zumar 39:68*).\n\n"
            "3. **The Gathering on the Plain of Mahshar (*Al-Hashr*):**\n"
            "   Humanity is driven together onto the plain of Mahshar. On this day, every person stands barefoot, unclad, and completely absorbed in their own destiny (*Sahih al-Bukhari 6527*). Worldly wealth, political power, academic titles, and family lineages are rendered entirely irrelevant. Only a person's faith and righteous deeds (*Hasanat*) provide shelter and dignity."
        ),
        "comparison_table": {
            "title": "Cosmic Sequence: First Trumpet vs. Second Trumpet",
            "headers": ["Dimension", "First Blast (Nafkhat al-Sa'iq)", "Second Blast (Nafkhat al-Ba'th)"],
            "rows": [
                ["Cosmic Impact", "Universal physical death and cosmic destruction", "Universal resurrection and biological re-creation"],
                ["State of Creation", "All living souls perish; worldly life ceases", "All humans emerge alive from graves; souls reunited with bodies"],
                ["Dominant Reality", "End of worldly trial and dissolution of nature", "Beginning of eternal reckoning and divine justice"],
                ["Qur'anic Citation", "Surah Az-Zumar (39:68) — '...all who are in heavens and earth swoon'", "Surah Ya-Sin (36:51) — '...from the graves to their Lord they hasten'"],
                ["Primary Human Response", "Absolute awe and termination of earthly deeds", "Realization of divine truth and profound accountability"]
            ]
        },
        "worked_example": {
            "scenario": "During a Grade 9 Integrated Science class discussing decomposition and soil nutrients, Yusuf wonders out loud: 'How is it scientifically or logically possible for a human body that has turned to dust, been dispersed by wind, or eaten by ocean organisms over thousands of years to be brought back to life?' His classmate Amina responds thoughtfully: 'Yusuf, consider how Allah created the entire cosmos out of absolute nothingness the first time. Re-creating a body that has decomposed is even simpler for the One who designed it originally. Just as a dry, dormant seed in a parched desert looks dead but sprouts into living greenery as soon as rain falls, Allah will regenerate all human bodies on the Day of Resurrection, exactly as He promised in Surah Ya-Sin.'",
            "analysis": "Amina demonstrates classical Qur'anic rational theology (*Kalam*): the Primary Creation (*Al-Khalq al-Awwal*) is logical proof of the Secondary Re-creation (*Al-I'adah*). Observing the seasonal rebirth of dormant plant life provides an observable earthly analogy for physical resurrection.",
            "takeaway": "Re-creating decomposed matter is effortless for the Originator of the universe; observing nature's renewal reinforces our certainty in literal resurrection."
        },
        "real_world_application": (
            "Apply the 'Speak Good or Remain Silent' protocol in daily communication. Before speaking in class, sending a WhatsApp message, or commenting online, pause and reflect: 'Is this word truthful, necessary, and kind?' If it does not build peace or benefit someone, practice intentional silence. Believing that every syllable will be presented on the Day of Gathering transforms daily communication into an act of worship."
        ),
        "reflection": "How does believing that you will be physically resurrected and stand before Allah affect how you make ethical choices when you are completely alone and unobserved?",
        "misconception": {
            "misconception": "Belief in the Last Day is meant to fill believers with paralyzing, hopeless dread and terror.",
            "correction": "Belief in the Last Day is designed to inspire moral responsibility, hope in Allah's ultimate justice, and proactive righteous engagement in this world."
        },
        "mcq": {
            "question": "What is the specific Islamic theological term for the event where all human beings are physically brought back to life from their graves?",
            "options": [
                "Hashr",
                "Ba'th",
                "Mizan",
                "Hisab"
            ],
            "answer": "Ba'th",
            "explanation": "Ba'th refers specifically to Resurrection—the physical re-creation and bringing back to life of all deceased humans by the command of Allah. Hashr refers to the subsequent gathering on the plain of Mahshar."
        },
        "summary": {
            "key_points": [
                "Resurrection (Ba'th) is the literal physical re-creation of all human beings by Allah.",
                "The First Trumpet blast ends all cosmic life; the Second Trumpet blast initiates universal resurrection.",
                "All humanity will be assembled on the plain of Mahshar during the Great Gathering (Hashr) in absolute equality.",
                "True conviction in the Last Day is demonstrated through disciplined speech, integrity, and proactive good deeds."
            ],
            "vocabulary": [
                {"term": "Ba'th", "definition": "Resurrection; the physical bringing back to life of all deceased human beings by Allah."},
                {"term": "Hashr", "definition": "The Gathering; the universal assembly of all resurrected humanity on the plain of Mahshar."},
                {"term": "Mahshar", "definition": "The vast, level plain where all human generations gather to await divine judgment."},
                {"term": "Al-Sur", "definition": "The cosmic Trumpet entrusted to Angel Israfeel to inaugurate cosmic death and resurrection."}
            ]
        },
        "exit_ticket": "Explain why the belief in physical Resurrection makes every action we perform in this world highly significant."
    },

    # =========================================================================
    # LESSON 2: Records, scale, and accounting
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Records, Scale, and Accounting (Kutub, Mizan, Hisab)",
        "lesson_title": "Records, scale, and accounting",
        "unit_description": "Comprehensive study of the divine audit: the individual record of deeds (Kutub), the absolute precision of the Divine Scale (Mizan), and the comprehensive questioning (Hisab) before the Creator.",
        "diagram_title": "The Divine Balance (Mizan) and Accounting Framework",
        "svg_fn": get_svg_lesson_2,
        "image": {
            "title": "Ancient Qur'anic Manuscript Foliage: The Divine Record and the Scale",
            "url": "https://upload.wikimedia.org/wikipedia/commons/5/50/Birmingham_Quran_manuscript.jpg",
            "caption": "Early illuminated Qur'anic manuscript leaf preserving Allah's immutable decree: 'And the weighing on that Day will be the truth. So those whose scales are heavy – it is they who are the successful' (Surah Al-A'raf 7:8).",
            "author": "Early Islamic Calligraphers (Birmingham Collection)",
            "source": "Wikimedia Commons",
            "licensing": "Public Domain"
        },
        "youtube": {
            "youtube_id": "UJYkwPDwC-Y",
            "title": "Heavy Words on Your Scale | Judgment Day | Dr. Omar Suleiman",
            "description": "Understanding the divine Scale (Mizan), the book of deeds, and how sincere character and righteous words tip the balance on the Day of Judgment."
        },
        "inquiry_question": "How are our deeds recorded, weighed, and audited, and how does this guarantee absolute justice?",
        "connection": "Imagine you enter a supermarket where every single item you place in your basket is automatically scanned by a high-tech camera, and a detailed invoice is printed at the exit. You cannot hide any item or claim you did not take it. This is a simple analogy for our spiritual life. Every thought, word, and action is being recorded by noble angels. On the Last Day, these records will be presented, weighed on a perfect scale (Mizan), and audited (Hisab) with absolute fairness.",
        "goals": [
            "Identify the role of the recording angels (Kiraman Katibin) and the personal book of deeds (Kutub al-A'mal).",
            "Understand the nature of the Divine Scale (Mizan) and the factors that make deeds spiritually heavy or light.",
            "Analyze the comprehensive process of individual accounting (Hisab) before Allah.",
            "Cultivate daily self-examination (Muhasabah) to prepare for an easy reckoning."
        ],
        "authoritative_concept": (
            "### The Tripartite Architecture of Divine Reckoning\n\n"
            "- **Record of Deeds (*Kutub al-A'mal*):** The complete ledger of an individual's lifetime actions, words, and intentions, faithfully transcribed by the recording angels (*Kiraman Katibin*).\n"
            "- **The Divine Scale (*Al-Mizan*):** The real, objective cosmic balance established on the Last Day to weigh the spiritual reality and moral quality of human deeds with infallible precision.\n"
            "- **The Reckoning (*Al-Hisab*):** The direct presentation and questioning of each individual before Allah concerning their life, youth, wealth, and practical application of knowledge (*Sunan at-Tirmidhi 2417*)."
        ),
        "scripture_panel": (
            "> \"And the weighing on that Day will be the truth. So those whose scales are heavy – it is they who are the successful. And those whose scales are light – they are the ones who will have lost themselves for what they used to do to Our verses.\"\n"
            "— **Surah Al-A'raf (7:8-9)**\n\n"
            "> \"Nothing will be heavier on the scale of the believer on the Day of Judgment than good character (*Akhlaq*). Indeed, Allah dislikes the rude, foul-mouthed person.\"\n"
            "— **Prophet Muhammad (PBUH)**, *Sunan at-Tirmidhi (2003)*"
        ),
        "deep_explanation": (
            "### The Three Sequential Phases of Divine Auditing\n\n"
            "The Day of Reckoning brings complete clarity through three distinct and transparent stages:\n\n"
            "1. **Receiving the Book (*Ita' al-Kutub*):**\n"
            "   Every individual is handed their personalized ledger. The righteous will receive their book in their **right hand** with boundless joy, declaring: *'Here, read my record!'* (*Surah Al-Haqqah 69:19*). The unrepentant wrongdoers will receive their book in their **left hand or behind their back**, overwhelmed with grief and lamenting every missed warning.\n\n"
            "2. **The Weighing on the Scale (*Al-Mizan*):**\n"
            "   Actions are placed on the Scale. Importantly, deeds are not judged simply by physical volume or external appearance, but by their internal **sincerity (*Ikhlas*) and moral beauty (*Akhlaq*)**. The Prophet (PBUH) taught that words of remembrance (*Dhikr*) and noble character possess immense mass, tipping the scale toward salvation.\n\n"
            "3. **The Audit (*Al-Hisab*):**\n"
            "   Allah audits each servant directly without an intermediary translator (*Sahih al-Bukhari 7443*). False denials are impossible, because Allah will cause the hands, feet, and skin to testify truthfully regarding every action (*Surah Ya-Sin 36:65*)."
        ),
        "comparison_table": {
            "title": "The Heavy Scale vs. The Light Scale on the Day of Judgment",
            "headers": ["Evaluation Factor", "The Heavy Scale (Success - Hasanat)", "The Light / Burdened Scale (Sayyi'at)"],
            "rows": [
                ["Internal Driver", "Sincerity (Ikhlas), love of Allah, and Tawhid", "Ostentation (Riya'), pride (Kibr), and hypocrisy"],
                ["Character Multiplier", "Noble conduct (Akhlaq), patience, and forgiveness", "Arrogance, cruelty, backbiting, and ridicule"],
                ["Core Actions", "Fard & Sunnah Salat, charity, truthfulness, Tawbah", "Cheating, unrepented injustices (Dhulm), oppression"],
                ["Book Reception", "Received in the Right Hand with public honor", "Received in the Left Hand / Behind Back with sorrow"],
                ["Eternal Destiny", "Pleasant life in Jannah (Surah Al-Qari'ah 101:7)", "Pit of blazing fire (Surah Al-Qari'ah 101:9-11)"]
            ]
        },
        "worked_example": {
            "scenario": "Hussein is studying for his end-of-term examinations. Frustrated by a difficult topic, he considers copying answers from his neighbor or writing notes on his desk. He thinks: 'No one is looking, and it will secure my grade.' Suddenly, he remembers the lesson on the Record of Deeds. He reflects: 'Even if the invigilator cannot see me, Kiraman Katibin are logging this instant. A high grade obtained through deception is an unrepented theft that will weigh heavily against me on the Mizan.' Hussein puts away the cheat notes and chooses to write honestly with what he has studied.",
            "analysis": "Hussein applies proactive self-accounting (*Muhasabah*). He realizes that worldly success obtained through moral compromise becomes a severe spiritual burden on the Mizan, whereas honest effort preserves integrity and earns divine blessing.",
            "takeaway": "Earthly gains obtained through cheating become heavy spiritual burdens on the Mizan; honesty protects the ledger of deeds."
        },
        "real_world_application": (
            "Implement a 'Daily Evening Audit' (*Muhasabah*) before sleeping. Spend five minutes in quiet reflection asking yourself: 'What did the recording angels write in my book today? Did I perform deeds that add weight to my Mizan (like honoring parents, praying on time, or helping a classmate)? Did I commit mistakes that need erasure through immediate sincere repentance (*Tawbah*)?' Regular self-auditing ensures an easy reckoning on the Last Day."
        ),
        "reflection": "How does the knowledge that your hands and skin will bear witness on the Day of Audit change your relationship with secret, private actions?",
        "misconception": {
            "misconception": "The spiritual weight of deeds on the Mizan is determined merely by mechanical repetition, regardless of inner intention.",
            "correction": "The Prophet (PBUH) taught that sincere devotion, humility, and exemplary character (*Akhlaq*) give deeds immense spiritual weight, while ostentation (*Riya'*) invalidates them."
        },
        "mcq": {
            "question": "According to the authentic Hadith of Tirmidhi, what is the heaviest thing that will be placed on the believer's Scale (Mizan) on the Day of Judgment?",
            "options": [
                "The amount of worldly wealth donated",
                "The physical size and strength of the body",
                "Good character and moral conduct (Akhlaq)",
                "The number of academic books read during life"
            ],
            "answer": "Good character and moral conduct (Akhlaq)",
            "explanation": "The Prophet (PBUH) explicitly taught that nothing is heavier on the scale of the believer on the Day of Judgment than good character (Akhlaq), demonstrating that daily interpersonal ethics are fundamental to salvation."
        },
        "summary": {
            "key_points": [
                "Every action, word, and intention is documented in our personal book of deeds by Kiraman Katibin.",
                "The Scale (Mizan) weighs good deeds against bad deeds with absolute divine justice and precision.",
                "Sincere devotion and noble moral conduct (Akhlaq) carry the supreme weight on the scale.",
                "Practicing daily self-accounting (Muhasabah) prepares the believer for a smooth, joyful audit."
            ],
            "vocabulary": [
                {"term": "Mizan", "definition": "The Divine Scale used to weigh the spiritual reality of deeds on the Last Day."},
                {"term": "Hisab", "definition": "The individual auditing and questioning process before Allah."},
                {"term": "Kiraman Katibin", "definition": "The noble recording angels assigned to write down every human action and utterance."},
                {"term": "Muhasabah", "definition": "The practice of daily self-examination and moral introspection before sleep."}
            ]
        },
        "exit_ticket": "Write down one heavy deed (high spiritual value) and one light deed (harmful) according to what we studied today."
    },

    # =========================================================================
    # LESSON 3: Intercession and siraat
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Intercession and the Sirat (Al-Shafa'ah wal-Sirat)",
        "lesson_title": "Intercession and siraat",
        "unit_description": "Investigation into the traversal of the Sirat bridge over Hellfire, the guiding light of faith (Nur al-Iman), and the theological conditions governing Prophetic Intercession (Shafa'ah).",
        "diagram_title": "The Crossing of the Sirat & Prophetic Intercession",
        "svg_fn": get_svg_lesson_3,
        "image": {
            "title": "Al-Masjid an-Nabawi: The Sanctuary of Prophet Muhammad (PBUH) in Madinah",
            "url": "https://upload.wikimedia.org/wikipedia/commons/c/c6/Al_Masjid_An_Nabawi.jpg",
            "caption": "The Prophet's Mosque in Madinah, honoring the Messenger of Allah (PBUH) who will stand by the Sirat bridge supplicating 'O Allah, save them, save them' and who is granted the Station of Praise (al-Maqam al-Mahmud) and the Great Intercession (al-Shafa'ah al-Kubra).",
            "author": "Ashique Mohammed",
            "source": "Wikimedia Commons",
            "licensing": "CC BY-SA 4.0"
        },
        "youtube": {
            "youtube_id": "TVt-Dd31Nn4",
            "title": "Crossing the Sirat | Judgment Day | Dr. Omar Suleiman",
            "description": "A deep dive into the crossing of the Sirat bridge over Hellfire, guided by the light of Iman and the mercy of the Prophet Muhammad's (PBUH) Shafa'ah."
        },
        "inquiry_question": "What is the nature of the Sirat bridge and Intercession, and how do they manifest Allah's mercy?",
        "connection": "Imagine a tightrope stretched over a deep canyon. It is windy, dark, and slippery. Only those who have been highly trained and have the perfect gear can cross it safely. The others will slip. This is a physical analogy for the Sirat—the bridge over Hellfire that every human must cross on the Last Day. In this dark hour, Allah in His mercy will grant unique assistance to the believers, including the light of their faith and the Intercession (Shafa'ah) of the Prophet Muhammad (PBUH). Let's study these profound concepts.",
        "goals": [
            "Define the Sirat as the physical path set across Hellfire leading into Paradise.",
            "Explain how the spiritual light of faith (Nur al-Iman) illuminates the believer's crossing.",
            "Describe the variable crossing speeds reflecting each person's earthly devotion.",
            "Analyze the theological criteria and scope of the Prophet's Intercession (Shafa'ah)."
        ],
        "authoritative_concept": (
            "### The Bridge and the Merciful Advocate\n\n"
            "- **The Bridge (*Al-Sirat*):** The perilous, narrow crossing established directly across the chasm of Hellfire (*Jahannam*) which all individuals must traverse to attain Paradise (*Jannah*). Stability and speed upon it correspond directly to righteous deeds and divine grace (*Sahih Muslim 186*).\n"
            "- **The Light of Faith (*Nur al-Iman*):** The individualized divine illumination granted to believers in the absolute darkness of the Last Day, shining before them and on their right side (*Surah Al-Hadid 57:12*).\n"
            "- **Intercession (*Al-Shafa'ah*):** The special permission granted by Allah to Prophet Muhammad (PBUH), angels, and righteous believers to petition for the salvation and elevation of believers (*Surah Ta-Ha 20:109*)."
        ),
        "scripture_panel": (
            "> \"On that Day no intercession will avail except that of one whom the Most Merciful has permitted and whose word He has approved.\"\n"
            "— **Surah Ta-Ha (20:109)**\n\n"
            "> \"The Sirat will be set over the bridge of Hellfire, and I will be the first of the Messengers to cross with my followers. The supplication of the Messengers on that Day will be: 'O Allah, save! Save!' (*Allahumma Sallim, Sallim*).\"\n"
            "— **Prophet Muhammad (PBUH)**, *Sahih al-Bukhari (806)*"
        ),
        "deep_explanation": (
            "### Crossing the Sirat: Justice Meets Divine Grace\n\n"
            "The crossing of the Sirat harmonizes absolute accountability with divine compassion:\n\n"
            "1. **The Reality of the Sirat:**\n"
            "   Classical Hadith descriptions describe the Sirat as thinner than a strand of hair and sharper than a polished blade, suspended over a dark, turbulent abyss. It is fitted with iron hooks (*Kalalib*) that snatch individuals based on specific unrepented violations committed in the world (*Sahih Muslim 195*).\n\n"
            "2. **The Light of Iman (*Nur*):**\n"
            "   The crossing occurs in pitch darkness. Believers receive an inner light whose brightness corresponds to their sincerity and good deeds. For some, it shines as vast as a mountain; for others, it flickers upon their toes (*Al-Mustadrak 3467*). Hypocrites receive no light and stumble into danger.\n\n"
            "3. **Variable Crossing Speeds:**\n"
            "   A person's earthly swiftness in obeying Allah dictates their transit speed across the Sirat: like a flash of lightning, a gust of wind, a galloping steed, running, walking, or crawling.\n\n"
            "4. **Prophetic Intercession (*Al-Shafa'ah al-Kubra*):**\n"
            "   Prophet Muhammad (PBUH) will prostrate beneath the Throne and praise Allah with words never before revealed, receiving divine permission: *'Raise your head, ask and you shall be given, intercede and your intercession will be accepted'* (*Sahih al-Bukhari 7510*). He will intercede to relieve the terror of the gathering and rescue believers who possessed even an atom's weight of faith."
        ),
        "comparison_table": {
            "title": "Sincere Faith vs. Hypocrisy on the Sirat Bridge",
            "headers": ["Criterion", "Sincere Believers (Ahl al-Iman)", "Hypocrites & Transgressors"],
            "rows": [
                ["Guiding Light", "Radiant, expansive light guiding every step (Surah Al-Hadid 57:12)", "No light; darkness engulfs them as their false light dies"],
                ["Crossing Speed", "Swift transit (lightning, wind, fast horses) according to deeds", "Slow stumbling, trembling, crawling, or falling into the abyss"],
                ["Prophetic Supplication", "Prophet prays actively: 'Rabbi Sallim Sallim' (Lord, save them!)", "Deprived of Prophetic defense due to rejection of truth"],
                ["Intercession Benefit", "Eligible for Shafa'ah by Allah's permission and contentment", "Excluded from intercession; no partners can assist them"],
                ["Final Outcome", "Safe arrival at the radiant gates of Jannah", "Falling into the fires of Jahannam (Surah Maryam 19:72)"]
            ]
        },
        "worked_example": {
            "scenario": "In a study group, Halima asks: 'If the Prophet (PBUH) is going to intercede for everyone who committed major sins, does that mean we can do whatever we want and just rely on his intercession?' Mr. Bilal clarifies: 'No, Halima. True belief in Shafa'ah should inspire greater diligence, not moral complacency. Firstly, the Qur'an establishes that no one can intercede except with Allah's explicit permission. Secondly, the fear of stumbling on the razor-sharp Sirat is so immense that no wise person would venture onto it burdened with sins. We must strive to cross like lightning, while placing humble hope in the Prophet's love and intercession for our unintentional shortcomings.'",
            "analysis": "Mr. Bilal articulates the essential balance between hope (*Raja'*) and reverent awe (*Khawf*). Relying on intercession while intentionally disobeying is spiritual delusion (*Ghurur*). Authentic reliance fosters deeper adherence to Prophetic morals.",
            "takeaway": "Belief in Shafa'ah inspires deep love for the Prophet (PBUH) and renewed commitment to righteous living, not moral complacency."
        },
        "real_world_application": (
            "Cultivate your 'Spiritual Light' for the Sirat through daily habits: maintain regular congregational prayers, practice truthful speech, assist vulnerable classmates, and send regular blessings upon the Prophet (*Salawat*). Loving the Prophet (PBUH) by emulating his manners (*Sunnah*) builds the spiritual radiance that guides your feet across the perilous crossing."
        ),
        "reflection": "How does the reality of Intercession show that Allah is not only an All-Just Judge, but also the Most Merciful and Forgiving?",
        "misconception": {
            "misconception": "Intercession is an automatic, independent pass that allows anyone to sin deliberately without consequences.",
            "correction": "Shafa'ah is strictly dependent on Allah's sovereign permission and pleasure; it is a manifestation of divine grace for those who preserved authentic faith despite human shortcomings."
        },
        "mcq": {
            "question": "Under what primary condition can the Prophet Muhammad (PBUH) or any other righteous servant perform Intercession (Shafa'ah) on the Day of Judgment?",
            "options": [
                "They can do it automatically for anyone they choose without limits",
                "They can only do it with the explicit permission and approval of Allah (S.W.T.)",
                "They can only do it for individuals who never committed any sins at all",
                "They can only do it if the person possessed immense worldly status"
            ],
            "answer": "They can only do it with the explicit permission and approval of Allah (S.W.T.)",
            "explanation": "Surah Ta-Ha (20:109) and Ayat al-Kursi (2:255) affirm that no intercession avails except by the sovereign permission and approval of Allah, proving that ultimate authority rests solely with the Creator."
        },
        "summary": {
            "key_points": [
                "Every human must cross the Sirat bridge over Hellfire; crossing speed corresponds to righteous deeds.",
                "Believers are guided across the dark chasm by the radiant light of their personal Iman.",
                "Allah will grant Prophet Muhammad (PBUH) the Great Intercession (Shafa'ah) as a manifestation of mercy.",
                "Shafa'ah requires Allah's permission and divine pleasure; it encourages deeper Prophetic emulation."
            ],
            "vocabulary": [
                {"term": "Sirat", "definition": "The bridge established across Hellfire leading to Paradise."},
                {"term": "Shafa'ah", "definition": "Intercession; petitioning Allah for the forgiveness and salvation of believers on the Last Day."},
                {"term": "Nur al-Iman", "definition": "The spiritual light of faith that illuminates the believer's path across the Sirat."},
                {"term": "Al-Maqam al-Mahmud", "definition": "The Station of Praise granted to Prophet Muhammad (PBUH) for the Great Intercession."}
            ]
        },
        "exit_ticket": "Write down how we can build our 'spiritual light' today through a practical action in school or at home."
    },

    # =========================================================================
    # LESSON 4: Paradise and Hellfire
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "The Eternal Abodes: Paradise and Hellfire (Jannah wa-Jahannam)",
        "lesson_title": "Paradise and Hellfire",
        "unit_description": "Theological exploration of the eternal destinations: the sublime delights and peace of Jannah contrasted with the sobering realities and divine justice of Jahannam.",
        "diagram_title": "The Eternal Abodes: Jannah vs. Jahannam",
        "svg_fn": get_svg_lesson_4,
        "image": {
            "title": "The Grand Gilded Gates of Al-Masjid an-Nabawi: Architecture of Heavenly Beauty",
            "url": "https://upload.wikimedia.org/wikipedia/commons/7/73/Al-Masjid_AL-Nabawi_Door.jpg",
            "caption": "The ornate, radiant gates of the Prophet's Mosque, reflecting Islamic artistic descriptions of the eight magnificent gates of Paradise (Jannah) awaiting the righteous who kept their covenant with Allah.",
            "author": "Belal El-Dweik",
            "source": "Wikimedia Commons",
            "licensing": "CC BY-SA 3.0"
        },
        "youtube": {
            "youtube_id": "_UomJ4KolFE",
            "title": "Your Eternal Home: Jannah | Judgment Day | Dr. Omar Suleiman",
            "description": "A comprehensive description of the eternal abodes—the boundless peace, gardens, and divine pleasure of Jannah contrasted with the consequences of injustice."
        },
        "inquiry_question": "What are the eternal abodes of Paradise and Hell, and how do they fulfill the divine promise of absolute justice?",
        "connection": "Imagine a long, grueling marathon. The runners have been training for months, running through heat and rain. At the finish line, there are two distinct outcomes: the successful runners are welcomed into a magnificent, air-conditioned garden with endless cold drinks, comfortable beds, and medals of honor. The cheaters and those who refused to participate are led to a harsh, dark holding cell where they face consequences for their rebellion. This is a physical analogy for the ultimate destinations of the Last Day: Paradise (Jannah) and Hellfire (Jahannam).",
        "goals": [
            "Describe the eternal characteristics, delights, and emotional peace of Paradise (Jannah).",
            "Understand the nature of Hellfire (Jahannam) as the realization of justice for unrepented transgression.",
            "Recognize the ascending ranks of Jannah (including Jannat al-Firdaws) and the descending depths of Jahannam.",
            "Appreciate the supreme reward of Jannah: beholding the Countenance of Allah and earning His Rida."
        ],
        "authoritative_concept": (
            "### The Ultimate Consummation of Creation\n\n"
            "- **Paradise (*Jannah*):** The eternal abode of absolute peace, perfection, and spiritual bliss created by Allah for those who had faith and performed righteous deeds (*Surah Al-Kahf 18:107*).\n"
            "- **Hellfire (*Jahannam*):** The eternal abode of physical and spiritual retribution created by Allah for those who knowingly rejected truth, committed tyranny, and died without repentance (*Surah An-Naba 78:21-22*).\n"
            "- **Jannat al-Firdaws:** The highest and most sublime rank of Paradise, situated directly beneath the Throne of the Most Merciful (*Sahih al-Bukhari 2790*)."
        ),
        "scripture_panel": (
            "> \"Indeed, those who have believed and done righteous deeds – they will have the Gardens of Paradise as a lodging, wherein they abide eternally. They desire not from it any transfer.\"\n"
            "— **Surah Al-Kahf (18:107-108)**\n\n"
            "> \"Indeed, Hell has been lying in wait, for the transgressors, a place of return, in which they will remain for ages.\"\n"
            "— **Surah An-Naba (78:21-23)**"
        ),
        "deep_explanation": (
            "### The Contrasting Realities of Jannah and Jahannam\n\n"
            "Jannah and Jahannam represent the ultimate fulfillment of divine justice, sovereign mercy, and human free will:\n\n"
            "1. **The Sublime Reality of Jannah:**\n"
            "   In Jannah, believers experience blessings that *'no eye has seen, no ear has heard, and no human mind has ever conceived'* (*Sahih al-Bukhari 3244*). It is free from all physical limitations: no illness, aging, fatigue, sadness, malice, or death. Rivers of pure water, fresh milk, unfermented wine, and clear honey flow continuously (*Surah Muhammad 47:15*).\n\n"
            "2. **The Levels of Jannah:**\n"
            "   Jannah contains numerous ascending ranks. Believers are positioned according to the depth of their sincere devotion and good deeds. The highest level is **Firdaws**, and the greatest delight of all is **viewing the Countenance of Allah (*Nazar ila Wajh Allah*)** and receiving His eternal pleasure (*Rida*).\n\n"
            "3. **The Reality of Jahannam:**\n"
            "   Jahannam is a manifestation of sovereign justice against unrepented oppression, arrogance, and denial of the Creator. It is described with intense heat, darkness, and anguish. Importantly, punishment is not arbitrary cruelty; it is the exact, deserved consequence of choices made in this temporary life."
        ),
        "comparison_table": {
            "title": "Contrasting the Eternal Destinies: Jannah vs. Jahannam",
            "headers": ["Dimension", "Paradise (Jannah)", "Hellfire (Jahannam)"],
            "rows": [
                ["Designation", "Dar al-Salam (Abode of Peace) & Bliss", "Dar al-Bawar (Abode of Ruin) & Retribution"],
                ["Environment", "Lush gardens, flowing rivers, pure drinks, radiant light", "Scorching heat, bitter thorns, dark confinement, and fire"],
                ["Emotional Reality", "Perpetual joy, serenity, no grief, rivalry, or exhaustion", "Deep remorse, bitter lamentation, and unfulfilled regret"],
                ["Companionship", "Reunited with prophets, martyrs, truthful, and righteous", "Mutual accusations, hatred, and isolation among oppressors"],
                ["Divine Relationship", "Honored with Allah's Rida and gazing upon His Countenance", "Veiled from divine mercy and experiencing divine justice"]
            ]
        },
        "worked_example": {
            "scenario": "Zainab is reading Surah Al-Kahf with her mother and asks: 'Why does the Qur'an describe Jannah with tangible earthly things like gold bracelets, green silk, flowing rivers, and delicious fruits? Will we actually have physical objects like that?' Her mother explains: 'Zainab, Allah uses words we already understand in our world to help our limited minds imagine the beauty of Paradise. But the Prophet (PBUH) taught that Jannah's realities are infinitely superior to anything on earth. The fruits never spoil, the garments never fade, and the peace is never interrupted. The physical metaphors give us a glimpse, but the true joy is living in the eternal presence and love of Allah.'",
            "analysis": "Zainab's mother explains classical Qur'anic hermeneutics: descriptions of Jannah utilize familiar earthly vocabulary as relatable pedagogical analogies for transcendent, incorruptible heavenly realities.",
            "takeaway": "Qur'anic descriptions use worldly imagery to make heavenly rewards tangible, but Jannah's reality exceeds human imagination."
        },
        "real_world_application": (
            "Adopt the 'Jannah Mindset' in daily decisions. When faced with difficult choices—such as waking up early for Fajr when tired, forgiving a friend who insulted you, or refusing to take money that isn't yours—remind yourself: 'This worldly struggle is brief, but Jannah is eternal.' Prioritizing everlasting peace over temporary comfort reframes daily sacrifices into meaningful milestones toward your true home."
        ),
        "reflection": "How does the description of Jannah as a place of absolute peace help you remain patient when you face sadness, loss, or injustice in this world?",
        "misconception": {
            "misconception": "Paradise and Hellfire are purely symbolic or psychological states rather than real, objective abodes.",
            "correction": "Orthodox Islamic creed establishes that Jannah and Jahannam are literal, already-created physical and spiritual abodes that will endure eternally."
        },
        "mcq": {
            "question": "Which of the following best describes the core characteristic of Jannah (Paradise) as presented in the Quran and authentic Sunnah?",
            "options": [
                "A temporary resting place before souls reincarnate on earth",
                "An eternal abode of absolute peace and joy with no sadness, pain, or death",
                "A place where people are ranked according to their worldly wealth and ancestry",
                "A symbolic state of mind that does not exist physically"
            ],
            "answer": "An eternal abode of absolute peace and joy with no sadness, pain, or death",
            "explanation": "Jannah is the eternal reality of complete physical and spiritual bliss created by Allah for the righteous, where sorrow, aging, sickness, and death are permanently abolished."
        },
        "summary": {
            "key_points": [
                "Jannah is the ultimate eternal reward for authentic faith and righteous actions.",
                "Jahannam represents the sovereign justice of Allah for deliberate rejection of truth and oppression of others.",
                "The greatest delight of Jannah is earning Allah's eternal pleasure (Rida) and viewing His Countenance.",
                "Worldly life is a brief planting season; the Hereafter is the place of the eternal harvest."
            ],
            "vocabulary": [
                {"term": "Jannah", "definition": "Paradise; the eternal gardens of supreme peace, bliss, and spiritual fulfillment."},
                {"term": "Jahannam", "definition": "Hellfire; the abode of divine justice and retribution for unrepented wrongdoing."},
                {"term": "Firdaws", "definition": "The highest and most exalted level within Paradise, situated directly beneath the Throne."},
                {"term": "Rida", "definition": "The eternal divine pleasure, contentment, and acceptance bestowed upon the people of Jannah."}
            ]
        },
        "exit_ticket": "Write down the name of the highest level of Jannah and one specific daily deed that can help us achieve it."
    },

    # =========================================================================
    # LESSON 5: Living with accountability
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Living with Accountability (Al-Muraqabah wal-Istiqaamah)",
        "lesson_title": "Living with accountability",
        "unit_description": "Application of Last Day consciousness to daily personal character, digital citizenship, moral integrity (Muraqabah), and social cohesion in contemporary society.",
        "diagram_title": "The Daily Integrity & Muraqabah Funnel",
        "svg_fn": get_svg_lesson_5,
        "image": {
            "title": "Tranquil Prayer Sanctuary in Medina: The Spirit of Muraqabah",
            "url": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Abu_Bakr_Mosque%2C_Medina_%28Interior%29.jpg",
            "caption": "A quiet prayer hall evoking the inner peace and focus of Muraqabah—living every moment with the constant, conscious awareness that Allah and the noble recording angels observe our secret and public actions.",
            "author": "Islamic Heritage Archive",
            "source": "Wikimedia Commons",
            "licensing": "CC BY-SA 4.0"
        },
        "youtube": {
            "youtube_id": "AHVP62ebo7s",
            "title": "How To Practice Daily Self Accountability & Muraqabah | Dr. Omar Suleiman",
            "description": "Practical strategies for developing Muraqabah (God-consciousness), internalizing the presence of the recording angels, and maintaining moral integrity in private and public."
        },
        "inquiry_question": "How does the constant awareness of the Last Day transform our daily character and public integrity?",
        "connection": "Imagine a camera crew is following you around your school, filming every action you take, every word you say, and even recording your computer screens, to broadcast it on national television next month. How would you behave? You would be extremely polite, you would study hard, and you would never throw litter on the floor. For a Muslim, believing in the Last Day means knowing that the noble angels are already recording everything, not for a television show, but for the ultimate audit before Allah. Let's look at how this awareness transforms our character.",
        "goals": [
            "Define personal accountability (Muraqabah) and its basis in Islamic theology.",
            "Explain how conviction in the Last Day drives personal integrity and honesty when unobserved.",
            "Apply Islamic ethical filters to daily speech, digital communications, and social interactions.",
            "Demonstrate how collective accountability fosters social trust, justice, and national cohesion in Kenya."
        ],
        "authoritative_concept": (
            "### God-Consciousness as the Engine of Moral Integrity\n\n"
            "- **Personal Accountability (*Al-Muraqabah*):** The spiritual state of constant, vigilant awareness that Allah is fully aware of our inner thoughts, motives, and outer deeds at every millisecond (*Surah Al-Hujurat 49:18*).\n"
            "- **Moral Integrity (*Al-Istiqaamah*):** Harmonious consistency between private convictions and public conduct, ensuring an individual remains honest regardless of whether human observers are present.\n"
            "- **Social Trust (*Al-Amanah*):** Recognizing that public property, school responsibilities, family trusts, and peer friendships are sacred trusts that will be audited before Allah."
        ),
        "scripture_panel": (
            "> \"Indeed, Allah knows the unseen of the heavens and the earth. And Allah is Seeing of what you do.\"\n"
            "— **Surah Al-Hujurat (49:18)**\n\n"
            "> \"Worship Allah as though you see Him; and if you cannot see Him, know that He surely sees you.\"\n"
            "— **Prophet Muhammad (PBUH)** on *Ihsan*, *Sahih al-Bukhari (50)*"
        ),
        "deep_explanation": (
            "### How Last Day Conviction Transforms Human Behavior\n\n"
            "Belief in the Last Day is the single most powerful internal motivator for ethical conduct in human society:\n\n"
            "1. **Incorruptible Private Honesty:**\n"
            "   External laws and security cameras only deter misconduct when surveillance is active. In contrast, a believer internalizes that the recording angels (*Kiraman Katibin*) never sleep or turn off. This prevents exam malpractice, secret embezzlement, and private deceit.\n\n"
            "2. **Guarding Speech and Digital Citizenship:**\n"
            "   Every spoken word and every typed text, tweet, or video forward is preserved in the individual's record (*Surah Qaf 50:18*). Awareness of the Mizan eliminates cyberbullying, gossip (*Gheebah*), character assassination, and the spread of unverified rumors.\n\n"
            "3. **Social Responsibility and Public Welfare:**\n"
            "   In Kenya, public resources, environmental cleanliness, and civic duties are recognized as moral trusts (*Amanah*). A youth rooted in Muraqabah protects public property, respects community elders, and supports the needy, viewing community service as investments into their eternal scale."
        ),
        "comparison_table": {
            "title": "Superficial Compliance vs. Authentic Muraqabah",
            "headers": ["Area of Conduct", "Superficial Compliance (External Monitoring)", "Authentic Muraqabah (God-Consciousness)"],
            "rows": [
                ["Primary Motivation", "Fear of teachers, police fines, or public embarrassment", "Love of Allah, reverent awe, and desire for His good pleasure"],
                ["Private Behavior", "Rules abandoned when cameras or supervisors are absent", "Identical moral standard maintained in private and public"],
                ["Digital Habits", "Engages in anonymous trolling, spreading gossip or piracy", "Types only truthful, beneficial, and dignified messages"],
                ["Social Impact", "Performs duties reluctantly or only for show (Riya')", "Serves community gladly as an act of worship and Sadaqah"],
                ["Last Day Readiness", "Caught unprepared at the sudden Reckoning", "Prepares a radiant book of deeds for an easy audit (Hisab Yaseer)"]
            ]
        },
        "worked_example": {
            "scenario": "Ali finds a high-end smartphone on a bench in the school library. No other students are present, and there are no security cameras in that corner. An internal impulse whispers: 'Keep it! You can sell it and buy a new gaming device. No one will ever trace it to you.' Ali pauses and remembers the lesson on the Record of Deeds and Muraqabah. He says to himself: 'Even if no teacher sees me, Allah is watching right now, and the noble angels are writing down my choice. This phone belongs to a classmate who is distressed. Keeping it is theft that will weigh heavily against me on the Last Day.' Ali picks up the phone and immediately carries it to the school administration office to find its owner.",
            "analysis": "Ali demonstrates true moral integrity (*Muraqabah*). His ethical choice is governed not by external police surveillance, but by living consciousness of the Last Day and certainty in divine accountability.",
            "takeaway": "Integrity is doing the right thing when no human is watching, knowing that Allah and His angels witness every action."
        },
        "real_world_application": (
            "Engage in the 'Secret Good Deed Challenge' this week. Perform one impactful good action that absolutely no one else knows about—not your parents, teachers, or best friends. It could be quietly cleaning up a messy classroom corner, donating anonymous pocket money to a needy pupil, or praying two rak'ahs in your bedroom at night. Secret deeds purify sincerity (*Ikhlas*) and build unshakeable confidence in Allah's record."
        ),
        "reflection": "Why is an individual who behaves honestly only when security cameras or teachers are watching not considered a person of true moral integrity?",
        "misconception": {
            "misconception": "Muraqabah is an abstract mystic concept meant only for elderly scholars and has no practical relevance to secondary school students.",
            "correction": "Muraqabah is the practical foundation of student integrity—governing exam honesty, digital communications on smartphones, and trustworthy peer friendships."
        },
        "mcq": {
            "question": "Zainab is about to post an embarrassing photo of a classmate online because she is angry with them. She suddenly remembers the belief in the Last Day and deletes the photo. Which core Islamic concept did Zainab demonstrate in this choice?",
            "options": [
                "Fear of school punishment and suspension",
                "Sincere accountability (Muraqabah) and concern for her Record of Deeds",
                "Personal pride and desire to win praise from others",
                "Lack of courage to confront her classmate directly"
            ],
            "answer": "Sincere accountability (Muraqabah) and concern for her Record of Deeds",
            "explanation": "Zainab's choice to delete the photo reflects Muraqabah—self-monitoring and active consciousness of Allah and the recording angels, prioritizing her eternal book of deeds over temporary anger."
        },
        "summary": {
            "key_points": [
                "Belief in the Last Day is the foundation of enduring personal integrity and public ethics.",
                "Constant awareness of the recording angels and Allah's sight leads to consistency in private and public conduct.",
                "Practicing Muraqabah transforms digital communication, school citizenship, and social responsibility.",
                "True success is preparing a clean, heavy Record of Deeds for the final audit before Allah."
            ],
            "vocabulary": [
                {"term": "Muraqabah", "definition": "The constant, vigilant self-awareness that Allah is observing our private and public deeds."},
                {"term": "Istiqaamah", "definition": "Moral uprightness and steadfast consistency in adhering to divine guidance."},
                {"term": "Amanah", "definition": "Sacred trust and moral responsibility placed upon human beings in society."},
                {"term": "Ihsan", "definition": "Spiritual excellence; worshipping and living as though you see Allah, knowing He sees you."}
            ]
        },
        "exit_ticket": "Write down one public action and one private action you will change this week because of your belief in the Last Day."
    }
]


# ─── MAIN INGESTION ROUTINE ──────────────────────────────────────────────────

def ingest_grade9_ire_topic5():
    """Ingests Topic 345 (Grade 9 IRE Topic 5) with full pedagogical enrichment."""
    print("=" * 80)
    print("STARTING VLEARN GRADE 9 IRE — TOPIC 5 (TOPIC ID 345) INGESTION")
    print("Belief in the Last Day (Yawm al-Qiyamah)")
    print("=" * 80)

    with transaction.atomic():
        # Validate Topic 345
        try:
            topic = Topic.objects.get(id=345)
        except Topic.DoesNotExist:
            print("[!] ERROR: Topic ID 345 does not exist in the database.")
            return

        subject = topic.subject
        grade = subject.grade if subject else None
        curriculum = grade.curriculum if grade else None

        print(f"Curriculum : {curriculum.name if curriculum else 'N/A'}")
        print(f"Grade      : {grade.name if grade else 'N/A'} (ID: {grade.id if grade else 'N/A'})")
        print(f"Subject    : {subject.name if subject else 'N/A'} (ID: {subject.id if subject else 'N/A'})")
        print(f"Topic      : {topic.name} (ID: {topic.id}, Order: {topic.order})")
        print("-" * 80)

        # Update topic metadata
        topic.name = "Belief in the Last Day (Yawm al-Qiyamah)"
        topic.description = (
            "Comprehensive study of the Pillars of Iman regarding the Last Day (Yawm al-Qiyamah): "
            "Resurrection (Ba'th) and Gathering (Hashr), the Record of Deeds (Kutub), the Divine Scale (Mizan), "
            "the Accounting (Hisab), the Sirat bridge, Prophetic Intercession (Shafa'ah), the eternal abodes "
            "of Paradise (Jannah) and Hellfire (Jahannam), and living with daily accountability (Muraqabah)."
        )
        topic.save()

        # Clean existing units under topic 345 (Strictly isolated to Topic 345)
        existing_units = LearningUnit.objects.filter(topic=topic)
        if existing_units.exists():
            print(f"[*] Removing {existing_units.count()} existing LearningUnits under Topic 345...")
            existing_units.delete()

        # Clean any orphan lessons under topic 345
        orphan_lessons = Lesson.objects.filter(topic=topic)
        if orphan_lessons.exists():
            print(f"[*] Removing {orphan_lessons.count()} orphan Lessons under Topic 345...")
            orphan_lessons.delete()

        total_units_created = 0
        total_lessons_created = 0
        total_blocks_created = 0
        total_assets_created = 0

        for cfg in LESSONS_DATA:
            u_order = cfg["unit_order"]
            u_name = cfg["unit_name"]
            l_title = cfg["lesson_title"]

            print(f"\n>>> [Unit {u_order}/5] Ingesting: '{l_title}'")

            # 1. Create LearningUnit
            unit = LearningUnit.objects.create(
                topic=topic,
                order=u_order,
                name=u_name,
                description=clean_text(cfg["unit_description"])
            )
            total_units_created += 1

            # 2. Create Published Lesson
            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=clean_text(l_title),
                status="published",
                version=1,
                published_at=timezone.now(),
                immutable_metadata={
                    "grade": "Grade 9",
                    "grade_id": grade.id if grade else None,
                    "subject": "IRE",
                    "subject_id": subject.id if subject else None,
                    "topic_id": topic.id,
                    "topic_order": topic.order,
                    "topic_name": topic.name,
                    "unit_order": u_order,
                    "unit_name": u_name,
                    "author": "VLearn Senior Curriculum Ingestion Specialist",
                    "curriculum_framework": "CBC Kenya Grade 9 IRE Strand 3.0 Sub-strand 3.1",
                    "enrichment_version": "v3_pedagogical_7cards",
                    "diagram_title": cfg["diagram_title"]
                }
            )
            total_lessons_created += 1

            # 3. Create LessonAssets
            # Asset 1: Authentic Wikimedia Commons Image
            img_info = cfg["image"]
            img_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                source_type="external",
                storage_type="url",
                status="attached",
                title=clean_text(img_info["title"]),
                description=clean_text(img_info["caption"]),
                url=img_info["url"],
                metadata={
                    "author": img_info.get("author", "Islamic Heritage Archive"),
                    "licensing": img_info.get("licensing", "Public Domain"),
                    "source": img_info.get("source", "Wikimedia Commons"),
                    "caption": clean_text(img_info["caption"])
                }
            )

            # Asset 2: Dedicated Vector SVG Diagram
            svg_content = cfg["svg_fn"]()
            svg_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="ai_generated",
                storage_type="url",
                status="attached",
                title=clean_text(cfg["diagram_title"]),
                description=f"High-quality pedagogical vector SVG diagram illustrating {l_title}.",
                url=f"https://vlearn.africa/assets/diagrams/ire/grade9_topic_5_lesson_{u_order}.svg",
                metadata={
                    "svg_content": svg_content,
                    "svg_xml": svg_content,
                    "viewBox": "0 0 880 440",
                    "theme": "#0f172a"
                }
            )

            # Asset 3: Educational YouTube Video
            yt_info = cfg["youtube"]
            yt_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="youtube",
                source_type="external",
                storage_type="url",
                status="attached",
                title=clean_text(yt_info["title"]),
                description=clean_text(yt_info["description"]),
                url=f"https://www.youtube.com/watch?v={yt_info['youtube_id']}",
                metadata={
                    "youtube_id": yt_info["youtube_id"],
                    "embed_url": f"https://www.youtube.com/embed/{yt_info['youtube_id']}"
                }
            )
            total_assets_created += 3

            # 4. Build 7 Cards / Pages (Standardized Pedagogical Blocks)

            # ───────────────────────────────────────────────────────────────────
            # CARD 1 (Page 1): Orientation & Inquiry
            # ───────────────────────────────────────────────────────────────────
            b_p1_img = LessonBlock.objects.create(
                lesson=lesson, page_number=1, page_title="Orientation & Inquiry",
                order=10, component_order=1,
                block_type="suggested_image", component_type="suggested_image",
                title=clean_text(img_info["title"]),
                content={
                    "title": clean_text(img_info["title"]),
                    "url": img_info["url"],
                    "caption": clean_text(img_info["caption"]),
                    "author": img_info.get("author", "Islamic Heritage Archive"),
                    "licensing": img_info.get("licensing", "Public Domain"),
                    "source": img_info.get("source", "Wikimedia Commons")
                }
            )
            b_p1_img.assets.add(img_asset)

            LessonBlock.objects.create(
                lesson=lesson, page_number=1, page_title="Orientation & Inquiry",
                order=20, component_order=2,
                block_type="learning_goal", component_type="learning_goal",
                title="Lesson Objectives & Inquiry Hook",
                content={
                    "inquiry_question": clean_text(cfg["inquiry_question"]),
                    "connection": clean_text(cfg["connection"]),
                    "goals": clean_dict(cfg["goals"]),
                    "markdown": f"### Inquiry Question\n\n**{clean_text(cfg['inquiry_question'])}**\n\n### Connection & Hook\n\n{clean_text(cfg['connection'])}\n\n### Learning Goals\n\n" + "\n".join([f"- {g}" for g in cfg["goals"]])
                }
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 2 (Page 2): Core Concept & Scripture Panel
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=2, page_title="Core Concept & Scripture",
                order=30, component_order=1,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Authoritative Concept",
                content={"markdown": clean_text(cfg["authoritative_concept"])}
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=2, page_title="Core Concept & Scripture",
                order=40, component_order=2,
                block_type="callout", component_type="callout",
                title="Scripture & Sources Panel",
                content={
                    "text": clean_text(cfg["scripture_panel"]),
                    "markdown": clean_text(cfg["scripture_panel"])
                }
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 3 (Page 3): Deep Explanation & Architecture Diagram
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=3, page_title="Deep Explanation & Diagram",
                order=50, component_order=1,
                block_type="concept_explanation", component_type="concept_explanation",
                title="In-Depth Analysis & Exposition",
                content={"markdown": clean_text(cfg["deep_explanation"])}
            )

            b_p3_diag = LessonBlock.objects.create(
                lesson=lesson, page_number=3, page_title="Deep Explanation & Diagram",
                order=60, component_order=2,
                block_type="suggested_diagram", component_type="suggested_diagram",
                title=f"Diagram: {clean_text(cfg['diagram_title'])}",
                metadata={
                    "svg_content": svg_content,
                    "svg_xml": svg_content,
                    "viewBox": "0 0 880 440"
                },
                content={
                    "title": f"Diagram: {clean_text(cfg['diagram_title'])}",
                    "caption": f"Pedagogical vector SVG architecture for {l_title}.",
                    "svg": svg_content,
                    "svg_xml": svg_content,
                    "svg_content": svg_content
                }
            )
            b_p3_diag.assets.add(svg_asset)

            # Comparison table on Card 3
            if "comparison_table" in cfg:
                LessonBlock.objects.create(
                    lesson=lesson, page_number=3, page_title="Deep Explanation & Diagram",
                    order=70, component_order=3,
                    block_type="comparison_table", component_type="comparison_table",
                    title=clean_text(cfg["comparison_table"]["title"]),
                    content=clean_dict(cfg["comparison_table"])
                )

            # ───────────────────────────────────────────────────────────────────
            # CARD 4 (Page 4): Worked Example & Relatable Scenario
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=4, page_title="Worked Example & Scenario",
                order=80, component_order=1,
                block_type="worked_example", component_type="worked_example",
                title="Relatable Student Scenario & Analysis",
                content={
                    "scenario": clean_text(cfg["worked_example"]["scenario"]),
                    "analysis": clean_text(cfg["worked_example"]["analysis"]),
                    "takeaway": clean_text(cfg["worked_example"]["takeaway"]),
                    "markdown": f"### Scenario\n\n{clean_text(cfg['worked_example']['scenario'])}\n\n### Analytical Breakdown\n\n{clean_text(cfg['worked_example']['analysis'])}\n\n### Core Takeaway\n\n**{clean_text(cfg['worked_example']['takeaway'])}**"
                }
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 5 (Page 5): Video, Real-World Application, Reflection & Misconception
            # ───────────────────────────────────────────────────────────────────
            b_p5_vid = LessonBlock.objects.create(
                lesson=lesson, page_number=5, page_title="Real-World Application & Reflection",
                order=90, component_order=1,
                block_type="suggested_video", component_type="suggested_video",
                title=clean_text(yt_info["title"]),
                content={
                    "title": clean_text(yt_info["title"]),
                    "url": f"https://www.youtube.com/watch?v={yt_info['youtube_id']}",
                    "youtube_id": yt_info["youtube_id"],
                    "description": clean_text(yt_info["description"])
                }
            )
            b_p5_vid.assets.add(yt_asset)

            LessonBlock.objects.create(
                lesson=lesson, page_number=5, page_title="Real-World Application & Reflection",
                order=100, component_order=2,
                block_type="real_world_example", component_type="real_world_example",
                title="Actionable Real-World Application",
                content={
                    "application": clean_text(cfg["real_world_application"]),
                    "markdown": f"### Real-World Application\n\n{clean_text(cfg['real_world_application'])}"
                }
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=5, page_title="Real-World Application & Reflection",
                order=110, component_order=3,
                block_type="reflection", component_type="reflection",
                title="Pause & Reflect",
                content={
                    "prompt": clean_text(cfg["reflection"]),
                    "markdown": f"### Pause & Reflect\n\n{clean_text(cfg['reflection'])}"
                }
            )

            if "misconception" in cfg:
                LessonBlock.objects.create(
                    lesson=lesson, page_number=5, page_title="Real-World Application & Reflection",
                    order=120, component_order=4,
                    block_type="common_misconception", component_type="common_misconception",
                    title="Common Misconception & Correction",
                    content={
                        "misconception": clean_text(cfg["misconception"]["misconception"]),
                        "correction": clean_text(cfg["misconception"]["correction"]),
                        "markdown": f"### Common Misconception\n\n❌ *{clean_text(cfg['misconception']['misconception'])}*\n\n### Factual Correction\n\n✓ **{clean_text(cfg['misconception']['correction'])}**"
                    }
                )

            # ───────────────────────────────────────────────────────────────────
            # CARD 6 (Page 6): Interactive Assessment / Knowledge Check
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=6, page_title="Knowledge Check & Assessment",
                order=130, component_order=1,
                block_type="knowledge_check", component_type="knowledge_check",
                title="Interactive Knowledge Check",
                content=clean_dict(cfg["mcq"])
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 7 (Page 7): Summary, Key Points & Mini-Activity
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=7, page_title="Summary & Exit Ticket",
                order=140, component_order=1,
                block_type="summary", component_type="summary",
                title="Unit Principles & Vocabulary Review",
                content={
                    "title": f"Summary: {l_title}",
                    "key_points": clean_dict(cfg["summary"]["key_points"]),
                    "vocabulary": clean_dict(cfg["summary"]["vocabulary"]),
                    "markdown": f"### Key Principles\n\n" + "\n".join([f"- {kp}" for kp in cfg["summary"]["key_points"]]) + "\n\n### Vocabulary Review\n\n" + "\n".join([f"- **{v['term']}**: {v['definition']}" for v in cfg["summary"]["vocabulary"]])
                }
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=7, page_title="Summary & Exit Ticket",
                order=150, component_order=2,
                block_type="mini_activity", component_type="mini_activity",
                title="Exit Ticket Challenge",
                content={
                    "activity": clean_text(cfg["exit_ticket"]),
                    "prompt": clean_text(cfg["exit_ticket"]),
                    "markdown": f"### Exit Ticket Challenge\n\n📝 **{clean_text(cfg['exit_ticket'])}**"
                }
            )

            blocks_count = lesson.blocks.count()
            total_blocks_created += blocks_count
            print(f"  [+] Created 7 Cards / Pages with {blocks_count} Blocks and 3 LessonAssets")

        print("\n" + "=" * 80)
        print("TOPIC 345 INGESTION & ENRICHMENT COMPLETE!")
        print(f"  - Subject           : {subject.name if subject else 'N/A'} (ID: {subject.id if subject else 'N/A'})")
        print(f"  - Topic             : {topic.name} (ID: {topic.id}, Order: {topic.order})")
        print(f"  - LearningUnits     : {total_units_created}")
        print(f"  - Lessons Published : {total_lessons_created}")
        print(f"  - LessonBlocks      : {total_blocks_created}")
        print(f"  - LessonAssets      : {total_assets_created}")
        print("=" * 80)


if __name__ == "__main__":
    ingest_grade9_ire_topic5()
