"""
VLearn CBC Grade 10 CRE — Sub-Strand 1.9.1: Background of Prophet Amos
Production Ingestion Script

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5)
Subject: CRE (ID: 46)
Topic: Sub-Strand 1.9.1: Background of Prophet Amos (Topic Order: 9)

8 Discrete Learning Units & Published Lessons:
  1. Tracing the Origin of Prophet Amos (6 Cards)
  2. Political Background to the Call of Prophet Amos (6 Cards)
  3. Social Background to the Call of Prophet Amos (6 Cards)
  4. Religious Background to the Call of Prophet Amos (6 Cards)
  5. The Call of Prophet Amos (6 Cards)
  6. The Five Visions of Prophet Amos (7 Cards)
  7. Relevance of Prophet Amos's Visions to Christians Today (6 Cards)
  8. Avoiding God's Judgment/Wrath (6 Cards)
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
    Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

def clean_text(text: str) -> str:
    """Removes bracket citations and internal metadata markers."""
    if not text:
        return ""
    # Strip bracket citations e.g. [1], [70], [73, 74], [23], etc.
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Strip internal pedagogical tags e.g. [VISUAL: ...], [BIBLE PASSAGE: ...], [VALUES], etc.
    text = re.sub(r'\[(VISUAL|BIBLE PASSAGE|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|ETHICAL APPLICATION|KEY VERSE|REAL WORLD APPLICATION|BIBLICAL CONTEXT|MCQ: HIGH|MCQ|TABLE)[^\]]*\]', '', text, flags=re.IGNORECASE)
    # Normalize unicode bullets
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    text = re.sub(r'^([^\n\-\*\d\>#][^\n]*)\n(- |\* )', r'\1\n\n\2', text, flags=re.MULTILINE)
    return text.strip()

def clean_dict(data):
    """Recursively cleans all strings in dictionary/list data structures."""
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, dict):
        return {k: clean_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_dict(item) for item in data]
    return data

# =============================================================================
# SANITIZED RESPONSIVE VECTOR SVG DEFINITIONS (viewBox="0 0 800 450")
# =============================================================================

# Lesson 1: Tekoa Geographic & Agrarian Context
SVG_LESSON_1 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="cardGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#334155"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="goldGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="blueGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="greenGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <filter id="shadow1" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="450" fill="url(#bg1)" rx="14"/>

  <!-- Header -->
  <text x="400" y="38" fill="#f8fafc" font-size="20" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">PROPHET AMOS: ORIGIN &amp; AGRARIAN CONTEXT</text>
  <text x="400" y="62" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">From the Wilderness of Tekoa (Judah) to the Royal Sanctuary at Bethel (Israel)</text>

  <!-- Left: Tekoa Origin Card -->
  <g filter="url(#shadow1)">
    <rect x="35" y="85" width="225" height="245" rx="10" fill="url(#cardGrad1)" stroke="#0284c7" stroke-width="2"/>
    <rect x="35" y="85" width="225" height="36" rx="10" fill="url(#blueGrad1)"/>
    <text x="147" y="108" fill="#ffffff" font-size="12" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">1. GEOGRAPHY: TEKOA</text>
    
    <circle cx="147" cy="150" r="20" fill="#0c4a6e"/>
    <text x="147" y="156" fill="#38bdf8" font-size="16" text-anchor="middle">🏜️</text>

    <text x="147" y="188" fill="#38bdf8" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Southern Kingdom (Judah)</text>
    <text x="48" y="212" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">• 10-12 miles south of Jerusalem</text>
    <text x="48" y="230" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">• Rugged hill country edge</text>
    <text x="48" y="248" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">• Overlooks Judean wilderness</text>
    <text x="48" y="266" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">• Harsh environment, hardy life</text>
    <text x="147" y="300" fill="#7dd3fc" font-size="9.5" font-weight="600" font-family="system-ui, sans-serif" text-anchor="middle">Amos 1:1</text>
  </g>

  <!-- Center Arrow / Calling Pathway -->
  <g filter="url(#shadow1)">
    <circle cx="400" cy="200" r="48" fill="url(#goldGrad1)" stroke="#fef08a" stroke-width="2"/>
    <text x="400" y="192" fill="#ffffff" font-size="12" font-weight="800" font-family="system-ui, sans-serif" text-anchor="middle">DIVINE CALL</text>
    <text x="400" y="208" fill="#ffffff" font-size="9.5" font-weight="600" font-family="system-ui, sans-serif" text-anchor="middle">"Go, Prophesy"</text>
    <text x="400" y="222" fill="#fef3c7" font-size="8.5" font-style="italic" font-family="system-ui, sans-serif" text-anchor="middle">Amos 7:15</text>
  </g>

  <!-- Flow Arrows -->
  <path d="M 265 200 L 345 200" stroke="#f59e0b" stroke-width="3" stroke-dasharray="6,4"/>
  <polygon points="345,195 355,200 345,205" fill="#f59e0b"/>
  <path d="M 455 200 L 535 200" stroke="#f59e0b" stroke-width="3" stroke-dasharray="6,4"/>
  <polygon points="535,195 545,200 535,205" fill="#f59e0b"/>

  <!-- Right: Occupations Card -->
  <g filter="url(#shadow1)">
    <rect x="540" y="85" width="225" height="245" rx="10" fill="url(#cardGrad1)" stroke="#059669" stroke-width="2"/>
    <rect x="540" y="85" width="225" height="36" rx="10" fill="url(#greenGrad1)"/>
    <text x="652" y="108" fill="#ffffff" font-size="12" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">2. RURAL LABOUR</text>
    
    <circle cx="652" cy="150" r="20" fill="#064e3b"/>
    <text x="652" y="156" fill="#34d399" font-size="16" text-anchor="middle">🐑</text>

    <text x="652" y="188" fill="#34d399" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Dual Working Background</text>
    <text x="552" y="212" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">• <tspan font-weight="700" fill="#a7f3d0">Noqed:</tspan> Sheep/livestock breeder</text>
    <text x="552" y="232" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">• <tspan font-weight="700" fill="#a7f3d0">Boles:</tspan> Sycamore fig dresser</text>
    <text x="552" y="252" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">• Manual scraping for ripening</text>
    <text x="552" y="272" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">• Direct solidarity with the poor</text>
    <text x="652" y="300" fill="#6ee7b7" font-size="9.5" font-weight="600" font-family="system-ui, sans-serif" text-anchor="middle">Amos 7:14</text>
  </g>

  <!-- Bottom Clarification Footer -->
  <rect x="35" y="345" width="730" height="80" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="400" y="370" fill="#fbbf24" font-size="12" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">THEOLOGICAL SIGNIFICANCE: DIVINE INITIATIVE OVER SOCIAL STATUS</text>
  <text x="400" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif" text-anchor="middle">Amos was not a professional prophet ("prophet's son"), nor from an elite dynasty.</text>
  <text x="400" y="412" fill="#94a3b8" font-size="10.5" font-family="system-ui, sans-serif" text-anchor="middle">God chose a hardworking rural laborer to cross national borders and confront northern royalty.</text>
</svg>"""

# Lesson 2: 8th Century BC Geopolitical Timeline & Regional Dynamics
SVG_LESSON_2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="goldGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="redGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#dc2626"/>
      <stop offset="100%" stop-color="#991b1b"/>
    </linearGradient>
    <linearGradient id="blueGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563eb"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>
    <filter id="shadow2" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bg2)" rx="14"/>

  <!-- Header -->
  <text x="400" y="38" fill="#f8fafc" font-size="20" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">8th CENTURY BCE GEOPOLITICAL DYNAMICS</text>
  <text x="400" y="62" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">The Era of King Jeroboam II: Outward Expansion vs. Deep Internal Decay</text>

  <!-- 3 Pillar Columns -->
  <!-- Pillar 1: Military & Territorial Expansion -->
  <g filter="url(#shadow2)">
    <rect x="35" y="85" width="225" height="235" rx="8" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <rect x="35" y="85" width="225" height="34" rx="8" fill="url(#blueGrad2)"/>
    <text x="147" y="107" fill="#ffffff" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">TERRITORIAL EXPANSION</text>
    
    <circle cx="147" cy="145" r="18" fill="#1e3a8a"/>
    <text x="147" y="151" fill="#93c5fd" font-size="14" text-anchor="middle">⚔️</text>

    <text x="147" y="178" fill="#60a5fa" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">King Jeroboam II (786-746 BCE)</text>
    <text x="48" y="202" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Restored borders to Dead Sea</text>
    <text x="48" y="222" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Captured Syrian trade cities</text>
    <text x="48" y="242" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Controlled King's Highway</text>
    <text x="48" y="262" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Strongest northern military</text>
  </g>

  <!-- Pillar 2: Geopolitical Lull -->
  <g filter="url(#shadow2)">
    <rect x="287" y="85" width="225" height="235" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="287" y="85" width="225" height="34" rx="8" fill="url(#goldGrad2)"/>
    <text x="399" y="107" fill="#ffffff" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">GEOPOLITICAL LULL</text>
    
    <circle cx="399" cy="145" r="18" fill="#78350f"/>
    <text x="399" y="151" fill="#fcd34d" font-size="14" text-anchor="middle">🛡️</text>

    <text x="399" y="178" fill="#fbbf24" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Temporary Assyrian Weakness</text>
    <text x="300" y="202" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Assyrian empire in decline</text>
    <text x="300" y="222" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• No external invasion threat</text>
    <text x="300" y="242" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Unprecedented peace &amp; luxury</text>
    <text x="300" y="262" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Generated deep complacency</text>
  </g>

  <!-- Pillar 3: False Sense of Security -->
  <g filter="url(#shadow2)">
    <rect x="540" y="85" width="225" height="235" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="540" y="85" width="225" height="34" rx="8" fill="url(#redGrad2)"/>
    <text x="652" y="107" fill="#ffffff" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">FALSE SECURITY</text>
    
    <circle cx="652" cy="145" r="18" fill="#7f1d1d"/>
    <text x="652" y="151" fill="#fca5a5" font-size="14" text-anchor="middle">⚠️</text>

    <text x="652" y="178" fill="#f87171" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Spiritual &amp; Moral Blindness</text>
    <text x="552" y="202" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Wealth equated to God's favor</text>
    <text x="552" y="222" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Covenant justice neglected</text>
    <text x="552" y="242" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Belief that Israel is invincible</text>
    <text x="552" y="262" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Blind to impending 721 BC fall</text>
  </g>

  <!-- Timeline Strip -->
  <rect x="35" y="335" width="730" height="90" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <line x1="60" y1="375" x2="740" y2="375" stroke="#64748b" stroke-width="2"/>
  
  <circle cx="120" cy="375" r="6" fill="#38bdf8"/>
  <text x="120" y="360" fill="#38bdf8" font-size="10" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">786 BCE</text>
  <text x="120" y="402" fill="#94a3b8" font-size="9" font-family="system-ui, sans-serif" text-anchor="middle">Jeroboam II Ascends</text>

  <circle cx="350" cy="375" r="6" fill="#f59e0b"/>
  <text x="350" y="360" fill="#fbbf24" font-size="10" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">~760 BCE</text>
  <text x="350" y="402" fill="#fde047" font-size="9" font-weight="600" font-family="system-ui, sans-serif" text-anchor="middle">Amos's Prophetic Call</text>

  <circle cx="580" cy="375" r="6" fill="#fb7185"/>
  <text x="580" y="360" fill="#fb7185" font-size="10" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">745 BCE</text>
  <text x="580" y="402" fill="#94a3b8" font-size="9" font-family="system-ui, sans-serif" text-anchor="middle">Assyria Resurges</text>

  <circle cx="710" cy="375" r="6" fill="#ef4444"/>
  <text x="710" y="360" fill="#ef4444" font-size="10" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">721 BCE</text>
  <text x="710" y="402" fill="#fca5a5" font-size="9" font-family="system-ui, sans-serif" text-anchor="middle">Fall of Samaria</text>
</svg>"""

# Lesson 3: Social Stratification Matrix in Samaria
SVG_LESSON_3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="eliteGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#92400e"/>
    </linearGradient>
    <linearGradient id="poorGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#475569"/>
      <stop offset="100%" stop-color="#334155"/>
    </linearGradient>
    <filter id="shadow3" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bg3)" rx="14"/>

  <text x="400" y="36" fill="#f8fafc" font-size="19" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">SOCIAL STRATIFICATION &amp; EXPLOITATION IN SAMARIA</text>
  <text x="400" y="58" fill="#94a3b8" font-size="12" font-family="system-ui, sans-serif" text-anchor="middle">Amos 2:6-7, 5:11-12, 8:5-6 — The Four Sins Against Human Dignity</text>

  <!-- Left: Stratification Pyramid/Blocks -->
  <g filter="url(#shadow3)">
    <!-- Elite Tier (Top 5%) -->
    <polygon points="175,80 75,180 275,180" fill="url(#eliteGrad)" stroke="#fbbf24" stroke-width="2"/>
    <text x="175" y="125" fill="#ffffff" font-size="12" font-weight="800" font-family="system-ui, sans-serif" text-anchor="middle">ELITE (5%)</text>
    <text x="175" y="145" fill="#fef3c7" font-size="9" font-family="system-ui, sans-serif" text-anchor="middle">Ivory Mansions</text>
    <text x="175" y="160" fill="#fef3c7" font-size="9" font-family="system-ui, sans-serif" text-anchor="middle">Wine Bowls &amp; Feasts</text>

    <!-- Poor Tier (Bottom 95%) -->
    <polygon points="75,185 275,185 325,320 25,320" fill="url(#poorGrad)" stroke="#64748b" stroke-width="1.5"/>
    <text x="175" y="235" fill="#ffffff" font-size="13" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">OPPRESSED MAJORITY (95%)</text>
    <text x="175" y="258" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Small Farmers • Landless Laborers</text>
    <text x="175" y="278" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Cheated Debtors • Impoverished Families</text>
    <text x="175" y="298" fill="#94a3b8" font-size="9.5" font-style="italic" font-family="system-ui, sans-serif" text-anchor="middle">Crushed by Heavy Taxes &amp; Bribery</text>
  </g>

  <!-- Right: The 4 Core Social Evils Grid -->
  <!-- Evil 1: Debt Slavery -->
  <g filter="url(#shadow3)">
    <rect x="350" y="80" width="200" height="110" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="365" y="104" fill="#f87171" font-size="11" font-weight="700" font-family="system-ui, sans-serif">1. DEBT SLAVERY</text>
    <text x="365" y="125" fill="#fca5a5" font-size="9" font-weight="600" font-family="system-ui, sans-serif">Amos 2:6</text>
    <text x="365" y="145" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Selling righteous for silver</text>
    <text x="365" y="163" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Needy for a pair of sandals</text>
    <text x="365" y="181" fill="#94a3b8" font-size="8.5" font-style="italic" font-family="system-ui, sans-serif">Human worth reduced to zero</text>
  </g>

  <!-- Evil 2: Land Grabbing -->
  <g filter="url(#shadow3)">
    <rect x="565" y="80" width="200" height="110" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="580" y="104" fill="#fbbf24" font-size="11" font-weight="700" font-family="system-ui, sans-serif">2. LAND GRABBING</text>
    <text x="580" y="125" fill="#fde047" font-size="9" font-weight="600" font-family="system-ui, sans-serif">Amos 2:7, 5:11</text>
    <text x="580" y="145" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Seizing ancestral estates</text>
    <text x="580" y="163" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Imposing heavy wheat taxes</text>
    <text x="580" y="181" fill="#94a3b8" font-size="8.5" font-style="italic" font-family="system-ui, sans-serif">Stripping poor families of food</text>
  </g>

  <!-- Evil 3: Judicial Corruption -->
  <g filter="url(#shadow3)">
    <rect x="350" y="205" width="200" height="115" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <text x="365" y="229" fill="#c084fc" font-size="11" font-weight="700" font-family="system-ui, sans-serif">3. COURT BRIBERY</text>
    <text x="365" y="250" fill="#e9d5ff" font-size="9" font-weight="600" font-family="system-ui, sans-serif">Amos 5:12</text>
    <text x="365" y="270" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Judges in city gates take bribes</text>
    <text x="365" y="288" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Denying justice to the poor</text>
    <text x="365" y="306" fill="#94a3b8" font-size="8.5" font-style="italic" font-family="system-ui, sans-serif">Justice turned into bitter wormwood</text>
  </g>

  <!-- Evil 4: Dishonest Trade -->
  <g filter="url(#shadow3)">
    <rect x="565" y="205" width="200" height="115" rx="8" fill="#1e293b" stroke="#06b6d4" stroke-width="1.5"/>
    <text x="580" y="229" fill="#22d3ee" font-size="11" font-weight="700" font-family="system-ui, sans-serif">4. DISHONEST COMMERCE</text>
    <text x="580" y="250" fill="#a5f3fc" font-size="9" font-weight="600" font-family="system-ui, sans-serif">Amos 8:5-6</text>
    <text x="580" y="270" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Rigged scales &amp; false weights</text>
    <text x="580" y="288" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Selling floor swept-up grain</text>
    <text x="580" y="306" fill="#94a3b8" font-size="8.5" font-style="italic" font-family="system-ui, sans-serif">Impatient for Sabbath to end</text>
  </g>

  <!-- Bottom Summary Banner -->
  <rect x="35" y="340" width="730" height="85" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="365" fill="#f87171" font-size="12" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">DIVINE VERDICT: EXPLOITATION IS A COVENANT BREACH</text>
  <text x="400" y="388" fill="#e2e8f0" font-size="10.5" font-family="system-ui, sans-serif" text-anchor="middle">Economic exploitation of the vulnerable is not merely a civil offense; it is direct rebellion against Yahweh.</text>
  <text x="400" y="408" fill="#94a3b8" font-size="10" font-style="italic" font-family="system-ui, sans-serif" text-anchor="middle">"The Lord has sworn by the Pride of Jacob: 'I will never forget anything they have done.'" (Amos 8:7)</text>
</svg>"""

# Lesson 4: Religious Syncretism vs Divine Rejection
SVG_LESSON_4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="templeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#5b21b6"/>
    </linearGradient>
    <linearGradient id="fireGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#dc2626"/>
      <stop offset="100%" stop-color="#991b1b"/>
    </linearGradient>
    <filter id="shadow4" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bg4)" rx="14"/>

  <text x="400" y="38" fill="#f8fafc" font-size="19" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">THE FAÇADE OF SYNCRETISM VS DIVINE REJECTION</text>
  <text x="400" y="62" fill="#94a3b8" font-size="12.5" font-family="system-ui, sans-serif" text-anchor="middle">Amos 4:4-5 &amp; Amos 5:21-24 — Why God Detests Empty, Hypocritical Worship</text>

  <!-- Left Card: The Outward Show (Bethel Shrines) -->
  <g filter="url(#shadow4)">
    <rect x="35" y="85" width="225" height="235" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect x="35" y="85" width="225" height="34" rx="8" fill="url(#templeGrad)"/>
    <text x="147" y="107" fill="#ffffff" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">OUTWARD RELIGION</text>
    
    <circle cx="147" cy="145" r="18" fill="#4c1d95"/>
    <text x="147" y="151" fill="#c4b5fd" font-size="14" text-anchor="middle">🏛️</text>

    <text x="147" y="178" fill="#a78bfa" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Crowded Shrines at Bethel</text>
    <text x="48" y="202" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Lavish morning sacrifices</text>
    <text x="48" y="222" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Golden calf cult of Jeroboam I</text>
    <text x="48" y="242" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Canaanite Baal fertility rites</text>
    <text x="48" y="262" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Grand temple musical choirs</text>
  </g>

  <!-- Middle: The Weekday Reality -->
  <g filter="url(#shadow4)">
    <rect x="287" y="85" width="225" height="235" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="287" y="85" width="225" height="34" rx="8" fill="#b45309"/>
    <text x="399" y="107" fill="#ffffff" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">WEEKDAY CRIMES</text>
    
    <circle cx="399" cy="145" r="18" fill="#78350f"/>
    <text x="399" y="151" fill="#fde047" font-size="14" text-anchor="middle">⚖️</text>

    <text x="399" y="178" fill="#fbbf24" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Moral Compartmentalization</text>
    <text x="300" y="202" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Monday cheating in markets</text>
    <text x="300" y="222" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Tuesday land grabbing</text>
    <text x="300" y="242" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Wednesday court bribery</text>
    <text x="300" y="262" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Treating worship as a bribe</text>
  </g>

  <!-- Right: Divine Rejection -->
  <g filter="url(#shadow4)">
    <rect x="540" y="85" width="225" height="235" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="540" y="85" width="225" height="34" rx="8" fill="url(#fireGrad)"/>
    <text x="652" y="107" fill="#ffffff" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">DIVINE REJECTION</text>
    
    <circle cx="652" cy="145" r="18" fill="#7f1d1d"/>
    <text x="652" y="151" fill="#fca5a5" font-size="14" text-anchor="middle">⚡</text>

    <text x="652" y="178" fill="#f87171" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">God's Radical Verdict</text>
    <text x="552" y="202" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• "I hate, I despise your feasts!"</text>
    <text x="552" y="222" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• "Assemblies are a stench to me"</text>
    <text x="552" y="242" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• "Away with your noisy songs!"</text>
    <text x="552" y="262" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Demands justice like a river</text>
  </g>

  <!-- Bottom Core Requirement Banner -->
  <rect x="35" y="340" width="730" height="85" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
  <text x="400" y="365" fill="#38bdf8" font-size="12.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">AMOS 5:24 — THE TRUE HEART OF COVENANT WORSHIP</text>
  <text x="400" y="388" fill="#f8fafc" font-size="12" font-weight="600" font-family="system-ui, sans-serif" text-anchor="middle">"Let justice roll down like waters, and righteousness like an ever-flowing stream."</text>
  <text x="400" y="408" fill="#94a3b8" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">True biblical worship cannot be separated from public fairness, social mercy, and personal holiness.</text>
</svg>"""

# Lesson 5: The Divine Mandate & Bethel Sanctuary Clash
SVG_LESSON_5 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="lionGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ea580c"/>
      <stop offset="100%" stop-color="#c2410c"/>
    </linearGradient>
    <linearGradient id="amosGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="amazGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <filter id="shadow5" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bg5)" rx="14"/>

  <text x="400" y="38" fill="#f8fafc" font-size="19" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">THE CALL OF AMOS &amp; THE CLASH AT BETHEL</text>
  <text x="400" y="62" fill="#94a3b8" font-size="12.5" font-family="system-ui, sans-serif" text-anchor="middle">Amos 3:8, 7:10-17 — Divine Compulsion vs State-Sanctioned Religion</text>

  <!-- Box 1: The Roaring Lion Mandate -->
  <g filter="url(#shadow5)">
    <rect x="35" y="85" width="220" height="235" rx="8" fill="#1e293b" stroke="#f97316" stroke-width="1.5"/>
    <rect x="35" y="85" width="220" height="34" rx="8" fill="url(#lionGrad)"/>
    <text x="145" y="107" fill="#ffffff" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">1. THE ROARING LION</text>
    
    <circle cx="145" cy="145" r="18" fill="#7c2d12"/>
    <text x="145" y="151" fill="#fdba74" font-size="14" text-anchor="middle">🦁</text>

    <text x="145" y="178" fill="#fb923c" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Amos 3:8 Compulsion</text>
    <text x="45" y="202" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• "The lion has roared..."</text>
    <text x="45" y="222" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Irresistible divine command</text>
    <text x="45" y="242" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Snapped from rural flock</text>
    <text x="45" y="262" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Unconditional obedience</text>
  </g>

  <!-- Box 2: Amos the Uncompromised Prophet -->
  <g filter="url(#shadow5)">
    <rect x="290" y="85" width="220" height="235" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect x="290" y="85" width="220" height="34" rx="8" fill="url(#amosGrad)"/>
    <text x="400" y="107" fill="#ffffff" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">2. PROPHET AMOS</text>
    
    <circle cx="400" cy="145" r="18" fill="#064e3b"/>
    <text x="400" y="151" fill="#6ee7b7" font-size="14" text-anchor="middle">📜</text>

    <text x="400" y="178" fill="#34d399" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">God's Humble Messenger</text>
    <text x="300" y="202" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• "I was no prophet's son"</text>
    <text x="300" y="222" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Not preaching for money</text>
    <text x="300" y="242" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Confronts royal sanctuary</text>
    <text x="300" y="262" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Pronounces exile &amp; doom</text>
  </g>

  <!-- Box 3: Amaziah the Corrupt State Priest -->
  <g filter="url(#shadow5)">
    <rect x="545" y="85" width="220" height="235" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="545" y="85" width="220" height="34" rx="8" fill="url(#amazGrad)"/>
    <text x="655" y="107" fill="#ffffff" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">3. PRIEST AMAZIAH</text>
    
    <circle cx="655" cy="145" r="18" fill="#3b0764"/>
    <text x="655" y="151" fill="#d8b4fe" font-size="14" text-anchor="middle">👑</text>

    <text x="655" y="178" fill="#c084fc" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Court Religion Defender</text>
    <text x="555" y="202" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• "Flee to Judah, earn bread!"</text>
    <text x="555" y="222" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Accuses Amos of treason</text>
    <text x="555" y="242" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Defends king's temple power</text>
    <text x="555" y="262" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Rejects true divine word</text>
  </g>

  <!-- Bottom Core Lesson -->
  <rect x="35" y="340" width="730" height="85" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="400" y="365" fill="#f59e0b" font-size="12" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">THE RADICAL DISTINCTION IN PROPHETIC MINISTRY</text>
  <text x="400" y="388" fill="#e2e8f0" font-size="10.5" font-family="system-ui, sans-serif" text-anchor="middle">False religious leaders serve political power and financial gain; true prophets obey God alone regardless of personal risk.</text>
  <text x="400" y="408" fill="#94a3b8" font-size="10" font-style="italic" font-family="system-ui, sans-serif" text-anchor="middle">"The Lord took me from tending the flock and said, 'Go, prophesy to my people Israel.'" (Amos 7:15)</text>
</svg>"""

# Lesson 6: The 5 Visions Progression Chart
SVG_LESSON_6 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="mercyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="shiftGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="judgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#dc2626"/>
      <stop offset="100%" stop-color="#991b1b"/>
    </linearGradient>
    <filter id="shadow6" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bg6)" rx="14"/>

  <text x="400" y="36" fill="#f8fafc" font-size="19" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">THE FIVE VISIONS OF PROPHET AMOS</text>
  <text x="400" y="58" fill="#94a3b8" font-size="12" font-family="system-ui, sans-serif" text-anchor="middle">Amos 7:1 - 9:4 — The Progression from Divine Patience to Inescapable Judgment</text>

  <!-- 5 Cards Layout -->
  <!-- Vision 1: Locusts -->
  <g filter="url(#shadow6)">
    <rect x="25" y="80" width="140" height="240" rx="8" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <rect x="25" y="80" width="140" height="32" rx="8" fill="url(#mercyGrad)"/>
    <text x="95" y="101" fill="#ffffff" font-size="10.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">1. LOCUSTS</text>
    
    <circle cx="95" cy="136" r="16" fill="#0c4a6e"/>
    <text x="95" y="142" fill="#38bdf8" font-size="13" text-anchor="middle">🦗</text>

    <text x="95" y="168" fill="#38bdf8" font-size="10" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Amos 7:1-3</text>
    <text x="32" y="190" fill="#cbd5e1" font-size="8.5" font-family="system-ui, sans-serif">• Stripping crops</text>
    <text x="32" y="208" fill="#cbd5e1" font-size="8.5" font-family="system-ui, sans-serif">• Economic ruin</text>
    <text x="32" y="235" fill="#4ade80" font-size="9" font-weight="700" font-family="system-ui, sans-serif">Amos Prays:</text>
    <text x="32" y="250" fill="#cbd5e1" font-size="8" font-style="italic" font-family="system-ui, sans-serif">"Lord, forgive!"</text>
    <text x="32" y="280" fill="#38bdf8" font-size="9" font-weight="700" font-family="system-ui, sans-serif">God Relents</text>
  </g>

  <!-- Vision 2: Fire -->
  <g filter="url(#shadow6)">
    <rect x="178" y="80" width="140" height="240" rx="8" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <rect x="178" y="80" width="140" height="32" rx="8" fill="url(#mercyGrad)"/>
    <text x="248" y="101" fill="#ffffff" font-size="10.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">2. FIRE</text>
    
    <circle cx="248" cy="136" r="16" fill="#0c4a6e"/>
    <text x="248" y="142" fill="#38bdf8" font-size="13" text-anchor="middle">🔥</text>

    <text x="248" y="168" fill="#38bdf8" font-size="10" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Amos 7:4-6</text>
    <text x="185" y="190" fill="#cbd5e1" font-size="8.5" font-family="system-ui, sans-serif">• Consuming deep</text>
    <text x="185" y="208" fill="#cbd5e1" font-size="8.5" font-family="system-ui, sans-serif">• Total scorch</text>
    <text x="185" y="235" fill="#4ade80" font-size="9" font-weight="700" font-family="system-ui, sans-serif">Amos Prays:</text>
    <text x="185" y="250" fill="#cbd5e1" font-size="8" font-style="italic" font-family="system-ui, sans-serif">"Lord, stop!"</text>
    <text x="185" y="280" fill="#38bdf8" font-size="9" font-weight="700" font-family="system-ui, sans-serif">God Relents</text>
  </g>

  <!-- Vision 3: Plumb Line (Turning Point) -->
  <g filter="url(#shadow6)">
    <rect x="331" y="80" width="140" height="240" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <rect x="331" y="80" width="140" height="32" rx="8" fill="url(#shiftGrad)"/>
    <text x="401" y="101" fill="#ffffff" font-size="10.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">3. PLUMB LINE</text>
    
    <circle cx="401" cy="136" r="16" fill="#78350f"/>
    <text x="401" y="142" fill="#fde047" font-size="13" text-anchor="middle">📐</text>

    <text x="401" y="168" fill="#fbbf24" font-size="10" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Amos 7:7-9</text>
    <text x="338" y="190" fill="#cbd5e1" font-size="8.5" font-family="system-ui, sans-serif">• Crooked wall</text>
    <text x="338" y="208" fill="#cbd5e1" font-size="8.5" font-family="system-ui, sans-serif">• Moral standard</text>
    <text x="338" y="235" fill="#f87171" font-size="9" font-weight="700" font-family="system-ui, sans-serif">Amos Silent:</text>
    <text x="338" y="250" fill="#cbd5e1" font-size="8" font-style="italic" font-family="system-ui, sans-serif">Standard set</text>
    <text x="338" y="280" fill="#f59e0b" font-size="9" font-weight="700" font-family="system-ui, sans-serif">Judgment Fixed</text>
  </g>

  <!-- Vision 4: Summer Fruit -->
  <g filter="url(#shadow6)">
    <rect x="484" y="80" width="140" height="240" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="484" y="80" width="140" height="32" rx="8" fill="url(#judgGrad)"/>
    <text x="554" y="101" fill="#ffffff" font-size="10.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">4. SUMMER FRUIT</text>
    
    <circle cx="554" cy="136" r="16" fill="#7f1d1d"/>
    <text x="554" y="142" fill="#fca5a5" font-size="13" text-anchor="middle">🧺</text>

    <text x="554" y="168" fill="#f87171" font-size="10" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Amos 8:1-3</text>
    <text x="491" y="190" fill="#cbd5e1" font-size="8.5" font-family="system-ui, sans-serif">• Ripe fruit (Qayits)</text>
    <text x="491" y="208" fill="#cbd5e1" font-size="8.5" font-family="system-ui, sans-serif">• End is near (Qets)</text>
    <text x="491" y="235" fill="#f87171" font-size="9" font-weight="700" font-family="system-ui, sans-serif">Amos Silent:</text>
    <text x="491" y="250" fill="#cbd5e1" font-size="8" font-style="italic" font-family="system-ui, sans-serif">Time expired</text>
    <text x="491" y="280" fill="#ef4444" font-size="9" font-weight="700" font-family="system-ui, sans-serif">Time Has Run Out</text>
  </g>

  <!-- Vision 5: Ruined Altar -->
  <g filter="url(#shadow6)">
    <rect x="637" y="80" width="140" height="240" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="637" y="80" width="140" height="32" rx="8" fill="url(#judgGrad)"/>
    <text x="707" y="101" fill="#ffffff" font-size="10.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">5. RUINED ALTAR</text>
    
    <circle cx="707" cy="136" r="16" fill="#7f1d1d"/>
    <text x="707" y="142" fill="#fca5a5" font-size="13" text-anchor="middle">🏛️</text>

    <text x="707" y="168" fill="#f87171" font-size="10" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Amos 9:1-4</text>
    <text x="644" y="190" fill="#cbd5e1" font-size="8.5" font-family="system-ui, sans-serif">• Striking pillars</text>
    <text x="644" y="208" fill="#cbd5e1" font-size="8.5" font-family="system-ui, sans-serif">• Crushing temple</text>
    <text x="644" y="235" fill="#f87171" font-size="9" font-weight="700" font-family="system-ui, sans-serif">Amos Silent:</text>
    <text x="644" y="250" fill="#cbd5e1" font-size="8" font-style="italic" font-family="system-ui, sans-serif">No escape</text>
    <text x="644" y="280" fill="#ef4444" font-size="9" font-weight="700" font-family="system-ui, sans-serif">Total Destruction</text>
  </g>

  <!-- Bottom Shift Banner -->
  <rect x="25" y="335" width="752" height="90" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="360" fill="#fde047" font-size="11.5" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">KEY PEDAGOGICAL INSIGHT: THE PLUMB LINE DIVIDE</text>
  <text x="400" y="382" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Visions 1-2 demonstrate God's patient mercy responding to intercession.</text>
  <text x="400" y="402" fill="#94a3b8" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Visions 3-5 reveal that persistent refusal to repent makes judgment inevitable against God's holy standard.</text>
</svg>"""

# Lesson 7: The Moral Plumb Line & Pillars of Prophetic Relevance
SVG_LESSON_7 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="plumbGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <filter id="shadow7" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bg7)" rx="14"/>

  <text x="400" y="36" fill="#f8fafc" font-size="19" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">THE MORAL PLUMB LINE: 3 TIMELESS PRINCIPLES</text>
  <text x="400" y="58" fill="#94a3b8" font-size="12" font-family="system-ui, sans-serif" text-anchor="middle">Applying Amos's Prophetic Visions to 21st-Century Christian Ethics and Society</text>

  <!-- Principle 1: Unchanging Standard -->
  <g filter="url(#shadow7)">
    <rect x="35" y="85" width="225" height="235" rx="8" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
    <rect x="35" y="85" width="225" height="34" rx="8" fill="url(#plumbGrad)"/>
    <text x="147" y="107" fill="#ffffff" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">1. UNCHANGING STANDARD</text>
    
    <circle cx="147" cy="145" r="18" fill="#0c4a6e"/>
    <text x="147" y="151" fill="#38bdf8" font-size="14" text-anchor="middle">📐</text>

    <text x="147" y="178" fill="#38bdf8" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">God's Word as Plumb Line</text>
    <text x="48" y="202" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• God measures truth, not wealth</text>
    <text x="48" y="222" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Popularity does not define right</text>
    <text x="48" y="242" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Absolute standard of righteousness</text>
    <text x="48" y="262" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Exposes systemic injustice</text>
  </g>

  <!-- Principle 2: The Limit of Patience -->
  <g filter="url(#shadow7)">
    <rect x="287" y="85" width="225" height="235" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="287" y="85" width="225" height="34" rx="8" fill="#b45309"/>
    <text x="399" y="107" fill="#ffffff" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">2. TIME TO REPENT</text>
    
    <circle cx="399" cy="145" r="18" fill="#78350f"/>
    <text x="399" y="151" fill="#fde047" font-size="14" text-anchor="middle">⏳</text>

    <text x="399" y="178" fill="#fbbf24" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Summer Fruit Principle</text>
    <text x="300" y="202" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Opportunity is not infinite</text>
    <text x="300" y="222" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Sin breeds unavoidable decay</text>
    <text x="300" y="242" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Reject spiritual complacency</text>
    <text x="300" y="262" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Act promptly upon conviction</text>
  </g>

  <!-- Principle 3: Inescapability of Justice -->
  <g filter="url(#shadow7)">
    <rect x="540" y="85" width="225" height="235" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect x="540" y="85" width="225" height="34" rx="8" fill="#047857"/>
    <text x="652" y="107" fill="#ffffff" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">3. UNIVERSAL ACCOUNT</text>
    
    <circle cx="652" cy="145" r="18" fill="#064e3b"/>
    <text x="652" y="151" fill="#6ee7b7" font-size="14" text-anchor="middle">⚖️</text>

    <text x="652" y="178" fill="#34d399" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">No Sanctuary for Greed</text>
    <text x="552" y="202" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• No power is above God's law</text>
    <text x="552" y="222" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Hidden corruptions are revealed</text>
    <text x="552" y="242" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Protection of the vulnerable</text>
    <text x="552" y="262" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Christians as active advocates</text>
  </g>

  <!-- Bottom Banner -->
  <rect x="35" y="340" width="730" height="85" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="400" y="365" fill="#38bdf8" font-size="12" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">CHRISTIAN SOCIAL WITNESS IN ACTION</text>
  <text x="400" y="388" fill="#e2e8f0" font-size="10.5" font-family="system-ui, sans-serif" text-anchor="middle">Like Amos, the church is called to be God's moral compass in society, confronting economic oppression and championing human dignity.</text>
  <text x="400" y="408" fill="#94a3b8" font-size="10" font-style="italic" font-family="system-ui, sans-serif" text-anchor="middle">Galatians 6:7 — "Do not be deceived: God cannot be mocked. A man reaps what he sows."</text>
</svg>"""

# Lesson 8: Pathway to Life & Ever-Flowing Stream of Justice
SVG_LESSON_8 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg8" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="riverGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#06b6d4"/>
    </linearGradient>
    <filter id="shadow8" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="url(#bg8)" rx="14"/>

  <text x="400" y="36" fill="#f8fafc" font-size="19" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">AVOIDING GOD'S JUDGMENT: "SEEK ME AND LIVE"</text>
  <text x="400" y="58" fill="#94a3b8" font-size="12" font-family="system-ui, sans-serif" text-anchor="middle">Amos 5:4-6, 14-15, 24 — The Three Pillars of Repentance and Restoration</text>

  <!-- 3 Steps Pathway -->
  <!-- Step 1: Genuine Repentance -->
  <g filter="url(#shadow8)">
    <rect x="35" y="85" width="225" height="235" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="35" y="85" width="225" height="34" rx="8" fill="#b91c1c"/>
    <text x="147" y="107" fill="#ffffff" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">1. HATE EVIL</text>
    
    <circle cx="147" cy="145" r="18" fill="#7f1d1d"/>
    <text x="147" y="151" fill="#fca5a5" font-size="14" text-anchor="middle">🛑</text>

    <text x="147" y="178" fill="#f87171" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Radical Repentance</text>
    <text x="48" y="202" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Renounce dishonest gains</text>
    <text x="48" y="222" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Abandon false idols &amp; pride</text>
    <text x="48" y="242" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Stop cheating in markets</text>
    <text x="48" y="262" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Turn away from hypocrisy</text>
  </g>

  <!-- Step 2: Seek Good -->
  <g filter="url(#shadow8)">
    <rect x="287" y="85" width="225" height="235" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="287" y="85" width="225" height="34" rx="8" fill="#b45309"/>
    <text x="399" y="107" fill="#ffffff" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">2. LOVE GOOD</text>
    
    <circle cx="399" cy="145" r="18" fill="#78350f"/>
    <text x="399" y="151" fill="#fde047" font-size="14" text-anchor="middle">❤️</text>

    <text x="399" y="178" fill="#fbbf24" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Cultivate Compassion</text>
    <text x="300" y="202" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Sincere love for neighbor</text>
    <text x="300" y="222" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Defend small &amp; vulnerable</text>
    <text x="300" y="242" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Align daily habits with grace</text>
    <text x="300" y="262" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Practice active integrity</text>
  </g>

  <!-- Step 3: Establish Justice -->
  <g filter="url(#shadow8)">
    <rect x="540" y="85" width="225" height="235" rx="8" fill="#1e293b" stroke="#06b6d4" stroke-width="1.5"/>
    <rect x="540" y="85" width="225" height="34" rx="8" fill="#0891b2"/>
    <text x="652" y="107" fill="#ffffff" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">3. ESTABLISH JUSTICE</text>
    
    <circle cx="652" cy="145" r="18" fill="#164e63"/>
    <text x="652" y="151" fill="#67e8f9" font-size="14" text-anchor="middle">⚖️</text>

    <text x="652" y="178" fill="#22d3ee" font-size="11" font-weight="700" font-family="system-ui, sans-serif" text-anchor="middle">Maintain Public Mishpat</text>
    <text x="552" y="202" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Fair verdicts in public courts</text>
    <text x="552" y="222" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Just compensation for workers</text>
    <text x="552" y="242" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Honest economic systems</text>
    <text x="552" y="262" fill="#cbd5e1" font-size="9.5" font-family="system-ui, sans-serif">• Ever-flowing river of righteousness</text>
  </g>

  <!-- Bottom River Banner -->
  <rect x="35" y="340" width="730" height="85" rx="8" fill="url(#riverGrad)"/>
  <text x="400" y="365" fill="#ffffff" font-size="13" font-weight="800" font-family="system-ui, sans-serif" text-anchor="middle">AMOS 5:14 — "SEEK GOOD AND NOT EVIL, THAT YOU MAY LIVE"</text>
  <text x="400" y="388" fill="#f0fdf4" font-size="11.5" font-weight="600" font-family="system-ui, sans-serif" text-anchor="middle">Then the Lord God Almighty will truly be with you, just as you claim He is.</text>
  <text x="400" y="408" fill="#e0f2fe" font-size="10" font-style="italic" font-family="system-ui, sans-serif" text-anchor="middle">Repentance leads to life, blessing, and the restoration of God's holy presence in society.</text>
</svg>"""

# =============================================================================
# CURRICULUM TOPIC & LESSON PAYLOAD DEFINITION
# =============================================================================

TOPIC_DATA = {
    "topic_order": 9,
    "topic_name": "Sub-Strand 1.9.1: Background of Prophet Amos",
    "topic_description": (
        "Comprehensive exploration of the origin, historical era, political climate under King Jeroboam II, "
        "social stratification and economic exploitation, empty religious syncretism at Bethel, divine call, "
        "the five symbolic visions of judgment, and practical pathways to life and justice in Prophet Amos."
    ),
    "units": [
        # ---------------------------------------------------------------------
        # LESSON 1
        # ---------------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Tracing the Origin of Prophet Amos",
            "unit_description": "Geographical origin in Tekoa, rural occupations as a shepherd and sycamore fig dresser, and the principle of divine initiative.",
            "lesson_title": "Tracing the Origin of Prophet Amos",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Ficus_sycomorus_fruit-Tel_Aviv.jpg",
            "image_caption": "Sycamore fig fruit (Ficus sycomorus), cultivated by Amos through manual scraping (boles) in the rugged hill country of Tekoa.",
            "svg_content": SVG_LESSON_1,
            "youtube_id": "m9p_d7zX4X0",
            "youtube_title": "BibleProject: Amos Overview",
            "youtube_description": "Explore the historical background, agrarian origin, and overarching prophetic message of Amos to the Northern Kingdom of Israel.",
            "pages": [
                # Card 1: Photographic Hook & Overview
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: Sycamore Figs & Tekoa Landscape",
                        "content": {
                            "caption": "Sycamore fig fruit (Ficus sycomorus), cultivated by Amos through manual scraping in the rugged hill country of Tekoa."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Focus: Tracing Amos's Roots",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will trace the geographical background of Amos from Tekoa in Judah, "
                                "explain his dual rural vocations as a shepherd (noqed) and sycamore fig dresser (boles), "
                                "and understand why God chooses ordinary, hardworking individuals for divine missions."
                            )
                        }
                    }
                ],
                # Card 2: Geographical Setting of Tekoa
                [
                    {
                        "type": "concept_explanation",
                        "title": "Geographical and Social Origin: Tekoa in Judah",
                        "content": {
                            "text": (
                                "Prophet Amos came from **Tekoa**, a small, rugged village situated in the dry hill country of Judah (the Southern Kingdom), "
                                "located approximately 10 to 12 miles south of Jerusalem and bordering the harsh Judean wilderness.\n\n"
                                "Living on the frontier of the wilderness demanded exceptional resilience, alertness, and physical endurance. "
                                "From this southern pastoral setting, God gave Amos a cross-border mission: to leave his home in Judah and journey north "
                                "to preach words of divine reckoning to the wealthy, powerful ruling class of the Northern Kingdom of Israel at Bethel."
                            )
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Biblical Anchor: Cross-Border Mission",
                        "content": {
                            "text": "Amos 1:1 — 'The words of Amos, one of the shepherds of Tekoa—the vision he saw concerning Israel two years before the earthquake, when Uzziah was king of Judah and Jeroboam son of Jehoash was king of Israel.'"
                        }
                    }
                ],
                # Card 3: Rural Occupations
                [
                    {
                        "type": "concept_explanation",
                        "title": "Amos's Rural Occupations: Shepherd & Sycamore Fig Dresser",
                        "content": {
                            "text": (
                                "Unlike the established professional court prophets of his era, Amos was an independent rural worker engaged in two primary tasks:\n\n"
                                "- **Shepherd (*Noqed*):** He bred and managed hardy desert sheep and livestock. The term *noqed* indicates an experienced animal manager accustomed to protecting flocks from predators in the rocky wilderness.\n"
                                "- **Dresser of Sycamore Figs (*Boles*):** He cultivated sycamore-fig trees (*Ficus sycomorus*). The fruit of the sycamore fig was a coarse, inexpensive food eaten primarily by the poor. To ripen and become sweet, each fig had to be manually punctured or scraped before harvest—a strenuous, labor-intensive task.\n\n"
                                "These occupations gave Amos an intimate understanding of the daily struggles of the working poor and an uncompromised moral independence."
                            )
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Misconception Clarified",
                        "content": {
                            "text": (
                                "Some assume Amos was a wealthy aristocratic landowner because he managed trees and sheep. "
                                "In reality, sycamore-fig dressing was considered a humble, low-status manual job. "
                                "Amos was a diligent, self-employed rural laborer who understood honest physical work."
                            )
                        }
                    }
                ],
                # Card 4: Pedagogical SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Vector Blueprint: Tekoa Origin & Agrarian Context",
                        "content": {
                            "caption": "Pedagogical diagram mapping Amos's geographical origin in Tekoa, his agrarian skills, and his divine call across the border to Bethel."
                        }
                    }
                ],
                # Card 5: Video & Interactive Matching
                [
                    {
                        "type": "suggested_video",
                        "title": "Video Study: Background of Amos",
                        "content": {
                            "description": "Watch how Amos's rural background in Judah prepared him to challenge the aristocratic elite in Israel."
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Interactive Matching: Amos's Biographical Elements",
                        "content": {
                            "text": (
                                "| Element | Historical & Geographic Meaning |\n"
                                "| :--- | :--- |\n"
                                "| **Tekoa** | Rugged village in Judah's hill country, 12 miles south of Jerusalem overlooking the wilderness. |\n"
                                "| **Noqed** | A skilled shepherd and livestock breeder accustomed to harsh wilderness conditions. |\n"
                                "| **Sycamore Fig Dressing** | Puncturing coarse, cheap fruit by hand to stimulate ripening; labor of the working class. |\n"
                                "| **Northern Kingdom (Israel)** | The target audience of Amos's cross-border prophetic ministry under King Jeroboam II. |"
                            )
                        }
                    }
                ],
                # Card 6: Mastery MCQ, Values & Real-World Application
                [
                    {
                        "type": "knowledge_check",
                        "title": "Mastery Assessment: Significance of Amos's Background",
                        "content": {
                            "question": "Which of the following best explains the significance of Amos's background as a shepherd and sycamore fig dresser when he was called to prophesy?",
                            "options": [
                                "It proved he had no theological competence to speak before royalty.",
                                "It demonstrated that God chooses ordinary, hardworking individuals from humble backgrounds to convey His divine messages, showing that vocation is based on divine initiative rather than social status.",
                                "It showed that he was a wealthy aristocrat who funded his own missionary journeys.",
                                "It meant he was only permitted to preach to agricultural laborers in Judah."
                            ],
                            "correct_answer": "It demonstrated that God chooses ordinary, hardworking individuals from humble backgrounds to convey His divine messages, showing that vocation is based on divine initiative rather than social status.",
                            "explanation": (
                                "God's call of Amos illustrates divine initiative: God does not rely on human credentials or elite status. "
                                "He equips and commissions faithful, industrious workers to speak His truth before kings."
                            )
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Real-World Application: School Leadership Dilemma",
                        "content": {
                            "text": (
                                "**Scenario:** In a high school Christian Union, some members argue that only top academic students from prominent, wealthy families should be appointed as leaders.\n\n"
                                "**Reflection:** How does God's choice of Amos challenge status-based leadership? True spiritual leadership is rooted in integrity, humility, and obedience to God rather than social prestige."
                            )
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Key Takeaway",
                        "content": {
                            "text": "Amos was a rural shepherd and fig dresser from Tekoa whose divine calling demonstrates that God empowers ordinary, faithful laborers to champion justice and speak truth to power."
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 2
        # ---------------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "Political Background to the Call of Prophet Amos",
            "unit_description": "Reign of King Jeroboam II in Israel, King Uzziah in Judah, territorial expansion, the geopolitical lull of Assyria, and the danger of false security.",
            "lesson_title": "Political Background to the Call of Prophet Amos",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e1/Drone_Aerial_View_of_the_Acropolis_and_Palace_Site_of_King_Omri_in_Samaria_Sebastia.jpg",
            "image_caption": "Aerial view of the royal acropolis and palace ruins at ancient Samaria, the capital city during the prosperous 8th-century BCE reign of King Jeroboam II.",
            "svg_content": SVG_LESSON_2,
            "youtube_id": "edllQ5H_cT0",
            "youtube_title": "The Divided Kingdom & 8th Century Prophets",
            "youtube_description": "Examine the political and military climate of the 8th century BCE under King Jeroboam II and King Uzziah.",
            "pages": [
                # Card 1: Photographic Hook & Overview
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: Acropolis of Samaria",
                        "content": {
                            "caption": "Ruins of the royal palace complex in Samaria, built during the peak of Israel's 8th-century BCE political power."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Focus: The 8th Century BCE Political Era",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will analyze the political environment during the reign of King Jeroboam II in Israel and King Uzziah in Judah, "
                                "explain how the geopolitical weakness of Assyria created a temporary period of peace, "
                                "and evaluate how outward political stability fostered a dangerous false sense of national security."
                            )
                        }
                    }
                ],
                # Card 2: The Reign of King Jeroboam II
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Prosperous Reign of King Jeroboam II (786–746 BCE)",
                        "content": {
                            "text": (
                                "Amos ministered during the mid-8th century BCE (around 760–750 BCE). In the Northern Kingdom of Israel, **King Jeroboam II** enjoyed a remarkable 41-year reign characterized by unprecedented political and economic expansion:\n\n"
                                "- **Territorial Restoration:** Jeroboam II recaptured territory from Damascus (Syria) and extended Israel's borders from Lebo-hamath in the north to the Dead Sea in the south (2 Kings 14:25).\n"
                                "- **Trade Route Control:** Dominating the King's Highway and coastal trade routes brought massive tax revenues and exotic luxury goods into Samaria and Bethel.\n"
                                "- **Military Superiority:** Israel maintained heavily fortified garrison cities and a well-equipped standing army, giving citizens a feeling of complete safety."
                            )
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Parallel Southern Stability",
                        "content": {
                            "text": "In the Southern Kingdom of Judah, King Uzziah (792–740 BCE) maintained strong defenses and a cooperative alliance with Israel, making the entire region outwardly stable and prosperous."
                        }
                    }
                ],
                # Card 3: Geopolitical Lull & False Security
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Geopolitical Lull of Assyria and the Trap of Complacency",
                        "content": {
                            "text": (
                                "During the reign of Jeroboam II, the primary Mesopotamian superpower—**Assyria**—was undergoing a temporary period of internal weakness and domestic rebellion. "
                                "This created a 50-year 'geopolitical lull' (approx. 790–745 BCE) during which Israel faced no immediate threat of foreign invasion.\n\n"
                                "**The Fatal Mindset:**\n"
                                "Because there was no military danger, the ruling class fell into deep complacency. "
                                "They mistakenly equated their military success and economic wealth with God's unconditional blessing. "
                                "They believed that as God's chosen people, they were invincible and that judgment would never come upon them."
                            )
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Prophetic Reality Check",
                        "content": {
                            "text": (
                                "Amos saw through this illusion. He warned that this political lull was temporary: "
                                "Assyria would rise again, and within a generation, unrepentant Israel would fall (fulfilled in 721 BCE with the Assyrian destruction of Samaria)."
                            )
                        }
                    }
                ],
                # Card 4: Pedagogical SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Vector Blueprint: 8th Century Geopolitical Timeline",
                        "content": {
                            "caption": "Timeline showing the reigns of Jeroboam II and Uzziah, the temporary Assyrian lull, and the countdown to the 721 BCE fall of Samaria."
                        }
                    }
                ],
                # Card 5: Video & Critical Reflection
                [
                    {
                        "type": "suggested_video",
                        "title": "Video Study: Geopolitical Dynamics in Ancient Israel",
                        "content": {
                            "description": "Examine how the temporary weakness of Assyria created the economic boom and moral complacency condemned by Amos."
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "The Political Corruption Chain",
                        "content": {
                            "text": (
                                "```\n"
                                "POLITICAL EXPANSION CYCLE IN 8th CENTURY ISRAEL:\n"
                                "[Assyrian Lull] ---> [Border Expansion] ---> [Trade Monopoly] ---> [Elite Wealth] ---> [Complacency & Moral Decay]\n"
                                "```\n\n"
                                "**Critical Question:** Why can prolonged political stability and economic prosperity sometimes blind a society to its moral corruption?"
                            )
                        }
                    }
                ],
                # Card 6: Mastery MCQ, Values & Governance Application
                [
                    {
                        "type": "knowledge_check",
                        "title": "Mastery Assessment: Geopolitical Weakness of Assyria",
                        "content": {
                            "question": "How did the geopolitical weakness of Assyria during the mid-8th century BCE affect the mindset of the Northern Kingdom of Israel?",
                            "options": [
                                "It filled the Israelites with constant panic, driving them to public repentance.",
                                "It led to a false sense of national invincibility and complacency, making the ruling elite believe God was pleased with them despite their moral decay.",
                                "It forced King Jeroboam II to surrender Israel's frontier territories to Judah.",
                                "It ruined Israel's economy by shutting down all Mediterranean trade."
                            ],
                            "correct_answer": "It led to a false sense of national invincibility and complacency, making the ruling elite believe God was pleased with them despite their moral decay.",
                            "explanation": (
                                "The temporary absence of foreign military threats created a false sense of security. "
                                "The elite believed they were untouchable and that their military dominance proved God's unconditional endorsement."
                            )
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Key Takeaway",
                        "content": {
                            "text": "Outward political triumphs and military stability under Jeroboam II masked deep covenant infidelity. True national security depends on moral righteousness and justice before God, not military might."
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 3
        # ---------------------------------------------------------------------
        {
            "unit_order": 3,
            "unit_name": "Social Background to the Call of Prophet Amos",
            "unit_description": "Extreme economic disparity, ivory-bed luxury of the elite, debt slavery, land grabbing, court bribery, and dishonest market scales.",
            "lesson_title": "Social Background to the Call of Prophet Amos",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Decorative_chain_of_lotus_buds_and_blossoms%2C_Samaria%2C_9th-8th_century_BC%2C_ivory_-_Harvard_Semitic_Museum_-_Cambridge%2C_MA_-_DSC06034.jpg",
            "image_caption": "Authentic 8th-century BCE Samaria ivory carving, reflecting the extreme luxury and ivory-paneled mansions of the ruling elite condemned by Prophet Amos.",
            "svg_content": SVG_LESSON_3,
            "youtube_id": "A14THPoc4-4",
            "youtube_title": "BibleProject: Biblical Justice & Amos",
            "youtube_description": "Explore the biblical concept of justice (mishpat and tsedaqah) and why Amos fiercely condemned economic exploitation.",
            "pages": [
                # Card 1: Photographic Hook & Overview
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: Samaria Ivory Inlays",
                        "content": {
                            "caption": "Carved ivory plaque excavated at ancient Samaria, testifying to the lavish mansions and ivory beds of the ruling class."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Focus: Social Injustice in Israel",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will analyze the extreme wealth gap in 8th-century BCE Israel, "
                                "identify the four major social evils condemned by Amos (debt slavery, land grabbing, court bribery, and dishonest scales), "
                                "and apply these lessons to promote ethical commerce and justice today."
                            )
                        }
                    }
                ],
                # Card 2: Extreme Economic Disparity
                [
                    {
                        "type": "concept_explanation",
                        "title": "Extreme Wealth Gap: Mansions of Ivory vs Grinding Poverty",
                        "content": {
                            "text": (
                                "While Israel's trade revenues soared, the wealth was concentrated in the hands of a small ruling minority (approx. top 5%), "
                                "leaving the vast majority of small farmers, day laborers, and craftsmen in acute distress.\n\n"
                                "- **The Aristocratic Elite:** Constructed multi-story summer and winter palaces decorated with imported ivory inlays (Amos 3:15). "
                                "They lounged on luxurious couches of ivory, feasted on choice lambs and fattened calves, drank vintage wine by the bowlful, and anointed themselves with the finest oils (Amos 6:4-6).\n"
                                "- **The Impoverished Majority:** Crushed by heavy agricultural taxes, extortionate rents, and predatory lending practices. "
                                "A single failed harvest meant losing ancestral land and being sold into servitude."
                            )
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Biblical Indictment",
                        "content": {
                            "text": "Amos 6:4, 6 — 'You lie on beds adorned with ivory and lounge on your couches. You dine on choice lambs... you drink wine by the bowlful and use the finest lotions, but you do not grieve over the ruin of Joseph.'"
                        }
                    }
                ],
                # Card 3: The 4 Core Social Evils
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Four Systematic Evils Condemned by Amos",
                        "content": {
                            "text": (
                                "Amos detailed specific ways the wealthy systematically robbed the vulnerable:\n\n"
                                "1. **Debt Slavery (Amos 2:6):** Creditors sold the righteous for silver and the needy for a pair of sandals. Human beings made in God's image were treated as commodities over petty, trivial debts.\n"
                                "2. **Land Grabbing (Amos 2:7, 5:11):** Powerful landlords manipulated legal loopholes and levied heavy taxes of grain to confiscate ancestral heritage plots, leaving families landless.\n"
                                "3. **Judicial Bribery (Amos 5:12):** The city gates—the civic courts of the ancient world—were thoroughly corrupted. Judges routinely accepted bribes from the rich, turning aside the poor who had no money to pay off the court.\n"
                                "4. **Dishonest Market Practices (Amos 8:5-6):** Merchants used rigged scales (heavy weights for buying, light weights for selling), inflated prices, and mixed swept-up grain dust with wheat to cheat buyers."
                            )
                        }
                    },
                    {
                        "type": "callout",
                        "title": "The Sabbath Contempt",
                        "content": {
                            "text": "Amos 8:5 — 'When will the New Moon be over that we may sell grain, and the Sabbath be ended that we may market wheat?—skimping on the measure, boosting the price and cheating with dishonest scales.'"
                        }
                    }
                ],
                # Card 4: Pedagogical SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Vector Blueprint: Social Stratification Matrix",
                        "content": {
                            "caption": "Infographic illustrating the 5% elite vs 95% oppressed majority and the four systematic social sins condemned by Amos."
                        }
                    }
                ],
                # Card 5: Video & Match-the-Evil Activity
                [
                    {
                        "type": "suggested_video",
                        "title": "Video Study: Amos & Social Oppression",
                        "content": {
                            "description": "Discover why God views economic oppression and judicial corruption as direct violations of His covenant."
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Ancient Evil vs Modern Equivalent",
                        "content": {
                            "text": (
                                "| Biblical Reference | Ancient Social Sin | Modern Equivalent |\n"
                                "| :--- | :--- | :--- |\n"
                                "| **Amos 2:6** | Selling the needy for sandals | Human trafficking, wage theft, exploitative child labor. |\n"
                                "| **Amos 5:12** | Bribery in city gates | Judicial corruption, paying bribes to escape criminal prosecution. |\n"
                                "| **Amos 8:5** | Tampered scales and bad wheat | Counterfeit products, false packaging weights, price-gouging. |\n"
                                "| **Amos 6:4** | Lounging on ivory beds | Luxury consumerism indifferent to poverty and homelessness. |\n"
                                "| **Amos 5:11** | Heavy straw/grain taxes | Extortionate rents and crushing predatory lending. |"
                            )
                        }
                    }
                ],
                # Card 6: Mastery MCQ, Values & Community Action
                [
                    {
                        "type": "knowledge_check",
                        "title": "Mastery Assessment: 'Selling the Needy for Sandals'",
                        "content": {
                            "question": "What does the phrase 'selling the needy for a pair of sandals' in Amos 2:6 signify about social conditions in ancient Israel?",
                            "options": [
                                "Sandals were the official currency recognized in international trade.",
                                "The rich placed so little value on human life that they would force an impoverished debtor into lifelong slavery over a petty, trivial debt.",
                                "The poor were refusing to work and trading away their footwear.",
                                "The king had introduced a national clothing subsidy program."
                            ],
                            "correct_answer": "The rich placed so little value on human life that they would force an impoverished debtor into lifelong slavery over a petty, trivial debt.",
                            "explanation": (
                                "Sandals symbolized a low-value, everyday item. "
                                "Amos used this metaphor to highlight the absolute disregard for human dignity among the ruling elite, who enslaved fellow covenant members over negligible debts."
                            )
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Values for Modern Youth: Business Integrity",
                        "content": {
                            "text": (
                                "**Core Christian Ethic:** God demands absolute honesty in commerce, fair treatment of employees, and compassion for the disadvantaged. "
                                "Exploiting others for financial gain brings divine judgment."
                            )
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Key Takeaway",
                        "content": {
                            "text": "Prophet Amos delivered a stinging indictment against economic exploitation, judicial corruption, and dishonest trade, proving that human dignity and social justice are central to God's covenant."
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 4
        # ---------------------------------------------------------------------
        {
            "unit_order": 4,
            "unit_name": "Religious Background to the Call of Prophet Amos",
            "unit_description": "Syncretism with Baal worship, golden calves at Bethel and Dan, empty religious ritualism, and God's rejection in Amos 5:21-24.",
            "lesson_title": "Religious Background to the Call of Prophet Amos",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/b/b5/Tel-dan-kultplatz-d-altar.JPG",
            "image_caption": "Remains of the ancient northern high place sanctuary and sacrificial altar at Tel Dan, identical in state-sponsored idolatrous ritual to the royal sanctuary at Bethel.",
            "svg_content": SVG_LESSON_4,
            "youtube_id": "7_CGP-12AE0",
            "youtube_title": "Idolatry & Syncretism in Ancient Israel",
            "youtube_description": "Understand the religious syncretism, golden calf shrines, and empty ritualism that provoked God's judgment through Amos.",
            "pages": [
                # Card 1: Photographic Hook & Overview
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: Ancient High Place Altar",
                        "content": {
                            "caption": "Reconstructed sacrificial altar precinct at Tel Dan, illustrating the monumental state sanctuaries of the Northern Kingdom."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Focus: Religious Hypocrisy and Syncretism",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will analyze the religious syncretism in 8th-century BCE Israel, "
                                "explain why God utterly rejected their elaborate feasts and sacrifices in Amos 5:21-24, "
                                "and understand why genuine faith requires harmony between public worship and daily moral action."
                            )
                        }
                    }
                ],
                # Card 2: Syncretism & Golden Calf Shrines
                [
                    {
                        "type": "concept_explanation",
                        "title": "Syncretism: Blending Yahweh Worship with Canaanite Idolatry",
                        "content": {
                            "text": (
                                "During the reign of Jeroboam II, religion was thriving outwardly. Pilgrims packed the national sanctuaries at **Bethel, Gilgal, and Dan**. "
                                "Sacrifices were offered daily, tithes were paid every three days, and temple choirs sang elaborate hymns of praise (Amos 4:4-5).\n\n"
                                "However, this religiosity was corrupted by **syncretism**—the fatal blending of true worship with pagan Canaanite fertility cults:\n\n"
                                "- **State-Sponsored Golden Calves:** Maintained at Bethel and Dan since the split of the kingdom under Jeroboam I as political alternatives to Jerusalem.\n"
                                "- **Baal & Asherah Cults:** Israelites engaged in pagan fertility rituals, sacred prostitution, and temple drinking parties under the guise of worshipping Yahweh.\n"
                                "- **Idolatrous Confidence:** They treated God like a pagan deity who could be appeased through expensive animal sacrifices while ignoring His moral laws."
                            )
                        }
                    },
                    {
                        "type": "callout",
                        "title": "The Sarcastic Call to Worship",
                        "content": {
                            "text": "Amos 4:4 — 'Go to Bethel and sin; go to Gilgal and sin yet more! Bring your sacrifices every morning, your tithes every three years... for this is what you love to do, O people of Israel.'"
                        }
                    }
                ],
                # Card 3: Hypocrisy & Divine Rejection
                [
                    {
                        "type": "concept_explanation",
                        "title": "Hypocrisy and Divine Abhorrence (Amos 5:21-24)",
                        "content": {
                            "text": (
                                "The wealthy class lived in severe moral contradiction:\n\n"
                                "- **On the Sabbath:** They attended the Bethel temple, offered choice fat beasts, burned expensive incense, and sang grand choral anthems.\n"
                                "- **On Monday Morning:** They returned to the marketplace to swindle poor widows, bribe courtroom judges, and seize ancestral lands.\n\n"
                                "**God's Fierce Response:**\n"
                                "God refused to be bought with ritual performances. Through Amos, He delivered one of the most blistering indictments in scripture:\n\n"
                                "> *'I hate, I despise your religious festivals; your assemblies are a stench to me. Even though you bring me burnt offerings and grain offerings, I will not accept them... Away with the noise of your songs! I will not listen to the music of your harps. But let justice roll on like a river, righteousness like a never-failing stream!'* (Amos 5:21-24)"
                            )
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Key Insight: Justice as True Worship",
                        "content": {
                            "text": "In God's covenant, worship without justice is an abomination. God evaluates Sunday praise by Monday lifestyle."
                        }
                    }
                ],
                # Card 4: Pedagogical SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Vector Blueprint: Façade of Syncretism vs Divine Rejection",
                        "content": {
                            "caption": "Pedagogical diagram showing the clash between outward ritual performance and weekday corruption, culminating in Amos 5:24."
                        }
                    }
                ],
                # Card 5: Video & School Ethical Scenario
                [
                    {
                        "type": "suggested_video",
                        "title": "Video Study: Amos 5 & True Worship",
                        "content": {
                            "description": "Explore the radical prophetic demand that justice (mishpat) and righteousness (tsedaqah) must accompany all true worship."
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "School Ethical Scenario: The Hypocritical Leader",
                        "content": {
                            "text": (
                                "**Scenario:** Clara is the chairperson of the school Christian Union. Every Sunday she leads worship with vibrant singing and prayer. "
                                "However, on weekdays, she actively helps friends cheat in national exams, mocks students from poor families, and steals supplies from the school lab.\n\n"
                                "**Prophetic Evaluation:**\n"
                                "1. Clara's behavior mirrors the religious elites of Bethel who offered lavish sacrifices while practicing weekday injustice.\n"
                                "2. Applying Amos 5:21-24, Clara must understand that God rejects outward religious displays if daily conduct is marked by dishonesty and cruelty."
                            )
                        }
                    }
                ],
                # Card 6: Mastery MCQ, Values & Core Takeaway
                [
                    {
                        "type": "knowledge_check",
                        "title": "Mastery Assessment: God's Response in Amos 5:21-24",
                        "content": {
                            "question": "According to Amos 5:21-24, what is God's response to abundant sacrifices and praise songs when social justice is absent?",
                            "options": [
                                "He accepts them as long as the offerings are physically unblemished.",
                                "He temporarily tolerates them while waiting for church attendance to rise.",
                                "He hates, despises, and rejects them, demanding instead that justice roll down like a river and righteousness like an ever-flowing stream.",
                                "He commands the worshippers to build larger shrines and amplify the choir volume."
                            ],
                            "correct_answer": "He hates, despises, and rejects them, demanding instead that justice roll down like a river and righteousness like an ever-flowing stream.",
                            "explanation": (
                                "In Amos 5:21-24, God explicitly rejects empty rituals and religious celebrations unaccompanied by ethical integrity and social justice."
                            )
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Key Takeaway",
                        "content": {
                            "text": "Religious syncretism and outward rituals cannot mask moral corruption. God desires a transformed heart that manifests in justice, fairness, and genuine love for one's neighbor."
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 5
        # ---------------------------------------------------------------------
        {
            "unit_order": 5,
            "unit_name": "The Call of Prophet Amos",
            "unit_description": "Divine initiative, the metaphor of the roaring lion (Amos 3:8), the confrontation with high priest Amaziah at Bethel, and prophetic courage.",
            "lesson_title": "The Call of Prophet Amos",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d2/Amos-prophet.jpg",
            "image_caption": "Historical icon depicting Prophet Amos holding a prophetic scroll, bearing witness to God's irresistible call to leave his rural life and confront the corrupt religious establishment.",
            "svg_content": SVG_LESSON_5,
            "youtube_id": "-evI7cq4GEI",
            "youtube_title": "The Prophets: Divine Calling and Authority",
            "youtube_description": "Understand how God called and empowered Old Testament prophets to speak His uncompromised word before kings and priests.",
            "pages": [
                # Card 1: Photographic Hook & Overview
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: Icon of Prophet Amos",
                        "content": {
                            "caption": "Historical depiction of Prophet Amos, who stood boldly before King Jeroboam II and high priest Amaziah at Bethel."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Focus: Amos's Calling & Bethel Confrontation",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will describe the divine initiative in Amos's call using the roaring lion metaphor (Amos 3:8), "
                                "analyze his historic confrontation with the high priest Amaziah at Bethel (Amos 7:10-17), "
                                "and identify key values of moral courage, integrity, and uncompromised obedience."
                            )
                        }
                    }
                ],
                # Card 2: Divine Initiative & The Roaring Lion
                [
                    {
                        "type": "concept_explanation",
                        "title": "Divine Initiative: The Compelling Voice of God",
                        "content": {
                            "text": (
                                "Amos did not volunteer to become a prophet, nor did he graduate from a guild of professional prophets ('sons of the prophets'). "
                                "His calling was a direct, sovereign intervention by Yahweh that seized him from his rural routine:\n\n"
                                "- **The Roaring Lion (Amos 3:8):** Amos captured the irresistible power of his call with a striking metaphor: "
                                "*'The lion has roared—who will not fear? The Sovereign Lord has spoken—who can but prophesy?'* "
                                "Just as wilderness beasts tremble when a lion roars, a person who hears God's voice is under an unavoidable mandate to speak.\n"
                                "- **The Command:** God commanded him: *'Go, prophesy to my people Israel'* (Amos 7:15). "
                                "Amos was compelled by divine authority to leave Judah and preach to the Northern Kingdom."
                            )
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Key Verse: Amos 7:14-15",
                        "content": {
                            "text": "'I was no prophet, nor was I a prophet’s son, but I was a shepherd and a dresser of sycamore-fig trees. But the Lord took me from tending the flock and said to me, \"Go, prophesy to my people Israel.\"'"
                        }
                    }
                ],
                # Card 3: The Confrontation with Amaziah at Bethel
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Historic Clash at Bethel: Amos vs Amaziah",
                        "content": {
                            "text": (
                                "When Amos arrived at the royal temple of Bethel, his preaching outraged the religious establishment:\n\n"
                                "1. **The Accusation of Treason:** **Amaziah**, the royal high priest of Bethel, sent a letter to King Jeroboam II accusing Amos of treason: "
                                "*'Amos is raising a conspiracy against you in the very heart of Israel. The land cannot bear all his words'* (Amos 7:10).\n"
                                "2. **The Insult:** Amaziah confronted Amos personally and commanded him to leave: "
                                "*'Get out, you seer! Go back to the land of Judah. Earn your bread there and do your prophesying there. Don't prophesy anymore at Bethel, because this is the king's sanctuary and the temple of the kingdom'* (Amos 7:12-13). "
                                "Amaziah treated Amos like a mercenary 'prophet-for-hire' who was preaching sensational doom just to make money.\n"
                                "3. **Amos's Bold Rebuttal:** Amos reaffirmed that he did not do this for wages or status. "
                                "He then delivered a personal prophecy of divine judgment upon Amaziah and his household for trying to silence God's word (Amos 7:16-17)."
                            )
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Prophet vs State Priest",
                        "content": {
                            "text": "Amaziah protected his political salary and royal status; Amos protected God's truth and covenant justice at the risk of his own life."
                        }
                    }
                ],
                # Card 4: Pedagogical SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Vector Blueprint: Divine Call & Bethel Clash",
                        "content": {
                            "caption": "Diagram depicting the Roaring Lion mandate, Amos's rural origin, and the sharp confrontation between Prophet Amos and High Priest Amaziah at Bethel."
                        }
                    }
                ],
                # Card 5: Video & Critical Thinking Comparison
                [
                    {
                        "type": "suggested_video",
                        "title": "Video Study: Amos Standing Before Kings & Priests",
                        "content": {
                            "description": "Watch how Amos courageously proclaimed God's judgment against corrupt institutional authorities at Bethel."
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Motive Comparison: Amos vs Amaziah",
                        "content": {
                            "text": (
                                "| Character | Position | Primary Motive | Response to Truth |\n"
                                "| :--- | :--- | :--- | :--- |\n"
                                "| **Amos** | Shepherd / Nabi | Obeying God's irresistible call | Speaks truth regardless of persecution. |\n"
                                "| **Amaziah** | Royal High Priest | Protecting institutional power & salary | Silences dissent and reports treason to the king. |"
                            )
                        }
                    }
                ],
                # Card 6: Mastery MCQ, Values & Integrity in Ministry
                [
                    {
                        "type": "knowledge_check",
                        "title": "Mastery Assessment: Amos's Defense to Amaziah",
                        "content": {
                            "question": "How did Amos defend himself when Amaziah told him to flee back to Judah to 'earn his bread'?",
                            "options": [
                                "He produced an official license from the prophetic guild of Jerusalem.",
                                "He claimed King Jeroboam II had granted him diplomatic immunity.",
                                "He declared that he was not a professional prophet-for-hire, but a shepherd and fig dresser whom God sovereignly commanded to speak.",
                                "He apologized to Amaziah and offered to pay a fine to the Bethel temple."
                            ],
                            "correct_answer": "He declared that he was not a professional prophet-for-hire, but a shepherd and fig dresser whom God sovereignly commanded to speak.",
                            "explanation": (
                                "In Amos 7:14-15, Amos made it clear that he was not a commercial prophet dependent on donations or royal patronage. "
                                "His authority rested solely on God's direct command: 'The Lord took me... and said, Go, prophesy.'"
                            )
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Key Takeaway",
                        "content": {
                            "text": "Amos's calling and confrontation at Bethel demonstrate that true servants of God are driven by divine obedience and moral integrity rather than popularity, money, or royal favor."
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 6
        # ---------------------------------------------------------------------
        {
            "unit_order": 6,
            "unit_name": "The Five Visions of Prophet Amos",
            "unit_description": "Locust swarm, consuming fire, the plumb line, the basket of summer fruit, and the ruined altar, tracing the shift from divine patience to unavoidable judgment.",
            "lesson_title": "The Five Visions of Prophet Amos",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/dd/Desert_Locust_swarm.jpg",
            "image_caption": "A devastating swarm of desert locusts, representing Amos's first symbolic vision of agricultural ruin and divine judgment upon Israel.",
            "svg_content": SVG_LESSON_6,
            "youtube_id": "m9p_d7zX4X0",
            "youtube_title": "The Five Visions of Judgment in Amos",
            "youtube_description": "Examine the five progressive visions revealed to Amos and the transition from intercession to inescapable destruction.",
            "pages": [
                # Card 1: Photographic Hook & Overview
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: Devastating Locust Swarm",
                        "content": {
                            "caption": "Swarm of desert locusts, symbolizing the impending agricultural and economic ruin in Amos's first vision."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Focus: The Five Symbolic Visions",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will identify and interpret each of the five symbolic visions of Amos (Amos 7:1-9, 8:1-3, 9:1-4), "
                                "explain the critical transition from the first two visions (intercession and mercy) to the final three visions (unavoidable judgment), "
                                "and understand God's balance of patience and justice."
                            )
                        }
                    }
                ],
                # Card 2: Visions of Mercy: Locusts & Fire
                [
                    {
                        "type": "concept_explanation",
                        "title": "Visions 1 & 2: Divine Forbearance and Prophetic Intercession",
                        "content": {
                            "text": (
                                "God showed Amos five sequential visions revealing the fate of the Northern Kingdom:\n\n"
                                "1. **The Swarm of Locusts (Amos 7:1-3):** Amos saw a massive plague of locusts devouring the late spring crops after the king's share had been harvested, threatening total famine. "
                                "Amos interceded urgently: *'Sovereign Lord, forgive! How can Jacob survive? He is so small!'* God relented and cancelled the plague.\n\n"
                                "2. **The Consuming Fire (Amos 7:4-6):** God called forth a supernatural judgment of fire that dried up the subterranean deep water and began devouring the farmland. "
                                "Amos interceded again: *'Sovereign Lord, I beg you, stop! How can Jacob survive? He is so small!'* God relented a second time and held back the fire.\n\n"
                                "**Key Lesson:** These first two visions prove that God is patient, merciful, and responsive to intercessory prayer."
                            )
                        }
                    },
                    {
                        "type": "callout",
                        "title": "The Role of the Intercessor",
                        "content": {
                            "text": "Prophets did not merely announce doom; like Amos, they passionately pleaded for God's mercy on behalf of a vulnerable people."
                        }
                    }
                ],
                # Card 3: The Turning Point: The Plumb Line
                [
                    {
                        "type": "concept_explanation",
                        "title": "Vision 3: The Plumb Line & The Crooked Wall (Amos 7:7-9)",
                        "content": {
                            "text": (
                                "In the third vision, the tone shifts dramatically:\n\n"
                                "- **The Vision:** Amos saw the Lord standing beside a vertical wall with a **plumb line** in His hand. A plumb line is a builder's tool (a weight suspended on a cord) used to test if a wall is straight.\n"
                                "- **The Interpretation:** God was measuring Israel against the absolute standard of His covenant Law. The wall of Israel was warped and leaning dangerously out of true alignment.\n"
                                "- **The Shift:** God declared: *'I will spare them no longer. The high places of Isaac will be destroyed and the sanctuaries of Israel will be ruined; with my sword I will rise against the house of Jeroboam'* (Amos 7:8-9).\n"
                                "- **Amos's Silence:** Unlike the first two visions, Amos did not pray or intercede. When the standard of justice is set and the wall is proven crooked, demolition is the only necessary response."
                            )
                        }
                    },
                    {
                        "type": "callout",
                        "title": "The Plumb Line Metaphor",
                        "content": {
                            "text": "A crooked wall cannot be reinforced; it will collapse under its own weight. Israel's moral corruption made national destruction inevitable."
                        }
                    }
                ],
                # Card 4: Visions of Finality: Summer Fruit & Ruined Altar
                [
                    {
                        "type": "concept_explanation",
                        "title": "Visions 4 & 5: Ripeness for Ruin and the Shattered Sanctuary",
                        "content": {
                            "text": (
                                "The final two visions confirmed that the time for repentance had passed:\n\n"
                                "4. **The Basket of Summer Fruit (*Qayits*) (Amos 8:1-3):** God showed Amos a basket of ripe summer fruit. God used a Hebrew wordplay: summer fruit (*qayits*) sounds like 'the end' (*qets*). "
                                "Israel was overripe in sin; their time had run out, and the end had arrived.\n\n"
                                "5. **The Ruined Altar at Bethel (Amos 9:1-4):** Amos saw the Lord standing beside the altar, commanding that the pillars and capitals be struck so the temple roof collapses upon the worshippers. "
                                "No corrupt citizen or priest could escape—whether they dig down to Sheol or climb up to the heavens, divine judgment would find them."
                            )
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Inescapability of Justice",
                        "content": {
                            "text": "Amos 9:2 — 'Though they dig down to the depths below, from there my hand will take them. Though they climb up to the heavens above, from there I will bring them down.'"
                        }
                    }
                ],
                # Card 5: Pedagogical SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Vector Blueprint: The 5 Visions Wheel of Justice",
                        "content": {
                            "caption": "Comprehensive progression diagram illustrating the five visions of Amos, the plumb line divide, and the move from divine patience to inescapable judgment."
                        }
                    }
                ],
                # Card 6: Video & Comparative Visual Table
                [
                    {
                        "type": "suggested_video",
                        "title": "Video Study: Understanding the 5 Visions",
                        "content": {
                            "description": "Watch an in-depth analysis of how Amos's five visions reveal both God's heart of mercy and the absolute certainty of His justice."
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Summary Table of the 5 Visions",
                        "content": {
                            "text": (
                                "| Vision # | Symbol & Passage | Meaning | Amos's Response | Divine Action |\n"
                                "| :--- | :--- | :--- | :--- | :--- |\n"
                                "| **1. Locusts** | Amos 7:1-3 | Threat of total crop destruction | Intercedes: 'Lord forgive!' | God relents and cancels plague. |\n"
                                "| **2. Fire** | Amos 7:4-6 | Judgment drying up deep springs | Intercedes: 'Lord stop!' | God relents and stops fire. |\n"
                                "| **3. Plumb Line** | Amos 7:7-9 | Measuring moral crookedness | Remains silent | God sets standard; destruction fixed. |\n"
                                "| **4. Summer Fruit** | Amos 8:1-3 | Israel ripe for the end (Qayits/Qets) | Remains silent | Time expired; judgment active. |\n"
                                "| **5. Ruined Altar** | Amos 9:1-4 | Collapse of Bethel temple on elite | Remains silent | Total inescapable exile and doom. |"
                            )
                        }
                    }
                ],
                # Card 7: Mastery MCQ, Values & Compassion
                [
                    {
                        "type": "knowledge_check",
                        "title": "Mastery Assessment: The Narrative Shift in the 5 Visions",
                        "content": {
                            "question": "What is the primary narrative shift between the first two visions (locusts and fire) and the third vision (the plumb line) in Amos?",
                            "options": [
                                "Amos successfully secures forgiveness in all five visions through relentless prayer.",
                                "In the first two visions, Amos intercedes and God relents; in the third vision, God's objective standard of justice is applied, Amos remains silent, and judgment becomes final.",
                                "The plumb line represents God awarding a building permit to King Jeroboam II.",
                                "The first two visions were directed at Judah, while the third vision was directed at Egypt."
                            ],
                            "correct_answer": "In the first two visions, Amos intercedes and God relents; in the third vision, God's objective standard of justice is applied, Amos remains silent, and judgment becomes final.",
                            "explanation": (
                                "The first two visions showcase God's mercy in response to intercession. "
                                "The plumb line marks the turning point where Israel's persistent crookedness renders destruction inevitable."
                            )
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Key Takeaway",
                        "content": {
                            "text": "The five visions illustrate that while God is profoundly patient and responsive to intercessory prayer, persistent injustice and unrepentance eventually exhaust divine forbearance, bringing inescapable judgment."
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 7
        # ---------------------------------------------------------------------
        {
            "unit_order": 7,
            "unit_name": "Relevance of Prophet Amos's Visions to Christians Today",
            "unit_description": "God's moral plumb line in modern life, the limit of patience, the inescapability of divine accountability, and avoiding spiritual complacency.",
            "lesson_title": "Relevance of Prophet Amos's Visions to Christians Today",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/af/Plumb-Bob_Pendant_LACMA_M.80.198.185.jpg",
            "image_caption": "Ancient plumb bob tool used by builders to ensure walls stand vertical and true, symbolizing God's absolute moral plumb line of justice for societies today.",
            "svg_content": SVG_LESSON_7,
            "youtube_id": "A14THPoc4-4",
            "youtube_title": "The Moral Plumb Line & Modern Ethics",
            "youtube_description": "Explore how the ancient plumb line of Amos challenges modern corruption, inequality, and institutional compromise.",
            "pages": [
                # Card 1: Photographic Hook & Overview
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: Ancient Plumb Line Tool",
                        "content": {
                            "caption": "Ancient bronze plumb bob, an essential measuring tool ensuring structural straightness in masonry."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Focus: Applying the Visions Today",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will apply the symbol of the Plumb Line to evaluate personal and societal ethics, "
                                "explain the danger of moral complacency in times of economic ease, "
                                "and understand the Christian duty to advocate for the vulnerable in contemporary society."
                            )
                        }
                    }
                ],
                # Card 2: God's Moral Plumb Line in Modern Society
                [
                    {
                        "type": "concept_explanation",
                        "title": "Principle 1: God's Unchanging Moral Plumb Line",
                        "content": {
                            "text": (
                                "The plumb line remains one of the most powerful metaphors in biblical ethics:\n\n"
                                "- **The Standard:** Just as a mason cannot change the law of gravity that guides a plumb line, human societies cannot rewrite God's moral laws. "
                                "God measures our personal lives, businesses, courts, and governments against His unchanging standard of truth, righteousness, and justice.\n"
                                "- **Exposing Crookedness:** A wall may look attractive from a distance with modern paint and decorations, but the plumb line reveals if it is structurally warped. "
                                "Similarly, a society may boast large skyscrapers, wealthy churches, and high GDP, but God's plumb line tests whether the poor are exploited and whether courts are fair."
                            )
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Scripture Connection",
                        "content": {
                            "text": "Hebrews 4:12 — 'For the word of God is alive and active. Sharper than any double-edged sword, it penetrates even to dividing soul and spirit... it judges the thoughts and attitudes of the heart.'"
                        }
                    }
                ],
                # Card 3: The Limit of Patience & Universal Accountability
                [
                    {
                        "type": "concept_explanation",
                        "title": "Principles 2 & 3: The Urgency of Repentance and Universal Accountability",
                        "content": {
                            "text": (
                                "The remaining visions provide two additional vital lessons for modern believers:\n\n"
                                "1. **The Limit of Divine Patience (The Summer Fruit):** Opportunity for repentance is a gift of grace that does not last indefinitely. "
                                "Delaying repentance while persisting in corruption hardens the heart and leads to moral ruin.\n\n"
                                "2. **Universal Accountability (The Ruined Altar):** Amos 9:2-3 warns that no power, wealth, or political connections can shield an individual from God's justice. "
                                "In modern society where the powerful often evade secular courts through bribery, Amos reassures believers that God's ultimate court is incorruptible."
                            )
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Guard Against Complacency",
                        "content": {
                            "text": "In times of financial success or national peace, Christians must guard against spiritual apathy. Success is measured by integrity, not bank accounts."
                        }
                    }
                ],
                # Card 4: Pedagogical SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Vector Blueprint: The Moral Plumb Line & Prophetic Ethics",
                        "content": {
                            "caption": "Diagram outlining the three timeless principles of the plumb line: God's unchanging standard, the urgency of repentance, and universal accountability."
                        }
                    }
                ],
                # Card 5: Video & Christian Social Witness
                [
                    {
                        "type": "suggested_video",
                        "title": "Video Study: Prophetic Ethics in the 21st Century",
                        "content": {
                            "description": "Discover how the prophetic voice of Amos inspires contemporary Christian engagement with human rights and poverty."
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "The Plumb Line Evaluation Framework",
                        "content": {
                            "text": (
                                "```\n"
                                "THE PLUMB LINE TEST FOR CONTEMPORARY SOCIETY:\n"
                                "1. Economic Justice: Are wages fair? Are business transactions honest?\n"
                                "2. Legal Integrity: Are courts accessible and impartial to the poor?\n"
                                "3. Religious Sincerity: Does worship translate into compassion on weekdays?\n"
                                "4. Protection of the Weak: Are widows, orphans, and refugees defended?\n"
                                "```"
                            )
                        }
                    }
                ],
                # Card 6: Mastery MCQ, Values & Civic Responsibility
                [
                    {
                        "type": "knowledge_check",
                        "title": "Mastery Assessment: The Plumb Line in Modern Ethics",
                        "content": {
                            "question": "How does the symbol of the 'Plumb Line' apply to modern Christian ethics and societal responsibility?",
                            "options": [
                                "It teaches that Christians should only pursue careers in civil engineering.",
                                "It serves as a reminder that God evaluates individuals and nations against His absolute standard of justice and righteousness rather than material wealth or outward rituals.",
                                "It guarantees that having large church buildings excuses corrupt business practices.",
                                "It suggests that God's moral laws change with every generation."
                            ],
                            "correct_answer": "It serves as a reminder that God evaluates individuals and nations against His absolute standard of justice and righteousness rather than material wealth or outward rituals.",
                            "explanation": (
                                "The plumb line represents God's objective, unbending standard of righteousness. "
                                "It reminds believers that all human activities, laws, and institutions are accountable to divine justice."
                            )
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Key Takeaway",
                        "content": {
                            "text": "Prophet Amos's visions challenge Christians today to reject spiritual complacency, align their lives with God's moral plumb line, and courageously defend the vulnerable in society."
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 8
        # ---------------------------------------------------------------------
        {
            "unit_order": 8,
            "unit_name": "Avoiding God's Judgment/Wrath",
            "unit_description": "God's core invitation in Amos 5:4-6 ('Seek me and live'), hating evil, loving good, establishing justice in the courts, and the school canteen dilemma.",
            "lesson_title": "Avoiding God's Judgment/Wrath",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Nahal_Arugot_%28Ein_Gedi%29_Israel.JPG",
            "image_caption": "A perennial, ever-flowing freshwater stream in the Judean wilderness, illustrating Amos 5:24: 'Let justice roll down like waters, and righteousness like an ever-flowing stream.'",
            "svg_content": SVG_LESSON_8,
            "youtube_id": "xmFPS0f-kzs",
            "youtube_title": "Repentance, Grace, and the Kingdom of God",
            "youtube_description": "Learn the biblical pathway to restoration and life through genuine repentance and the pursuit of righteousness.",
            "pages": [
                # Card 1: Photographic Hook & Overview
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: The Ever-Flowing Stream",
                        "content": {
                            "caption": "A perennial stream of living water flowing through the wilderness, representing life and restorative justice in Amos 5:24."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Focus: The Pathway to Life",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will explain God's gracious invitation to 'Seek me and live' (Amos 5:4-6), "
                                "identify the three concrete steps to avoid divine judgment (genuine repentance, establishing justice, and loving the good), "
                                "and resolve ethical dilemmas with moral integrity."
                            )
                        }
                    }
                ],
                # Card 2: God's Core Invitation: "Seek Me and Live"
                [
                    {
                        "type": "concept_explanation",
                        "title": "God's Grace: 'Seek the Lord and Live' (Amos 5:4-6)",
                        "content": {
                            "text": (
                                "The warnings of Prophet Amos were not intended to drive Israel into despair, but to awaken them to life. "
                                "God takes no pleasure in destruction; His deepest desire is reconciliation and restoration.\n\n"
                                "- **The Divine Command:** Through Amos, God repeatedly pleaded with His people: *'Seek me and live; do not seek Bethel, do not go to Gilgal, do not journey to Beersheba... Seek the Lord and live, or he will sweep through the house of Joseph like a fire'* (Amos 5:4-6).\n"
                                "- **Not Pilgrimages, But Heart Change:** Seeking God was not about visiting historic shrines or offering animal sacrifices. "
                                "It required a total turning away from idolatry, greed, and dishonesty to embrace God's holy character."
                            )
                        }
                    },
                    {
                        "type": "callout",
                        "title": "The Golden Verse: Amos 5:14-15",
                        "content": {
                            "text": "'Seek good, not evil, that you may live. Then the Lord God Almighty will be with you, just as you say he is. Hate evil, love good; maintain justice in the courts. Perhaps the Lord God Almighty will have mercy on the remnant of Joseph.'"
                        }
                    }
                ],
                # Card 3: Three Practical Actions for Life
                [
                    {
                        "type": "concept_explanation",
                        "title": "Three Concrete Steps to Avert Divine Judgment",
                        "content": {
                            "text": (
                                "In Amos 5:14-15, God provides three clear, practical actions for national and personal renewal:\n\n"
                                "1. **Hate Evil (Repentance):** Actively despise dishonesty, corruption, and selfishness. Repentance is not just feeling guilty; it is turning 180 degrees away from harmful practices.\n"
                                "2. **Love Good (Positive Transformation):** It is not enough to avoid doing bad things out of fear. Believers must actively champion honesty, compassion, charity, and kindness in everyday relationships.\n"
                                "3. **Maintain Justice in the Courts (*Mishpat*):** Justice must be institutionalized. In ancient Israel, this meant ending bribery at the city gates. Today, it means ensuring fair legal systems, honest business weights, equal education, and living wages for workers."
                            )
                        }
                    },
                    {
                        "type": "callout",
                        "title": "The Promise of Presence",
                        "content": {
                            "text": "When a nation practices justice, God promises: 'Then the Lord God Almighty will truly be with you, just as you claim He is.'"
                        }
                    }
                ],
                # Card 4: Pedagogical SVG Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Vector Blueprint: Pathway to Life & Stream of Justice",
                        "content": {
                            "caption": "Diagram illustrating the three pillars of renewal: Hate Evil -> Love Good -> Maintain Justice, leading to divine presence and life."
                        }
                    }
                ],
                # Card 5: Video & School Canteen Dilemma
                [
                    {
                        "type": "suggested_video",
                        "title": "Video Study: Seeking God and Practicing Justice",
                        "content": {
                            "description": "Examine how seeking God requires concrete public actions of righteousness and ethical integrity in daily life."
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Ethical Case Study: The School Canteen Dilemma",
                        "content": {
                            "text": (
                                "**Scenario:** The student council discovers that the school canteen manager is purchasing expired juice and snacks at cheap clearance prices and selling them to students at full price. "
                                "The student leaders are afraid to speak up because the manager is a close relative of a board member.\n\n"
                                "**Amos-Based Action Plan:**\n"
                                "1. *Hate Evil:* Recognize that endangering students' health for greedy profit is a grave moral sin.\n"
                                "2. *Love Good:* Protect vulnerable students who are consuming unsafe food.\n"
                                "3. *Maintain Justice:* Present formal, documented evidence to school authorities, choosing moral courage over intimidation."
                            )
                        }
                    }
                ],
                # Card 6: Mastery MCQ, Values & Core Conclusion
                [
                    {
                        "type": "knowledge_check",
                        "title": "Mastery Assessment: Practical Evidence of Seeking God",
                        "content": {
                            "question": "According to Amos 5:14-15, what is the practical, visible evidence of 'seeking the Lord' in daily life?",
                            "options": [
                                "Increasing the number of animal sacrifices during national religious festivals.",
                                "Moving away to an isolated wilderness hermitage to avoid secular people.",
                                "Seeking good and not evil, hating evil and loving good, and actively maintaining justice in public courts.",
                                "Forming political treaties and alliances with foreign superpowers."
                            ],
                            "correct_answer": "Seeking good and not evil, hating evil and loving good, and actively maintaining justice in public courts.",
                            "explanation": (
                                "In Amos 5:14-15, the prophet clarifies that seeking God is proven through concrete public actions: "
                                "actively pursuing good, renouncing evil, and establishing institutional justice."
                            )
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Key Takeaway",
                        "content": {
                            "text": "God's ultimate desire is not destruction, but life and restoration. By turning away from exploitation, loving goodness, and establishing justice in public life, individuals and nations experience God's grace and lasting peace."
                        }
                    }
                ]
            ]
        }
    ]
}

# =============================================================================
# DATABASE INGESTION EXECUTION
# =============================================================================

def ingest_grade10_cre_topic_1_9_1(replace: bool = True):
    print("=" * 80)
    print("STARTING VLEARN INGESTION: CBC GRADE 10 CRE SUB-STRAND 1.9.1")
    print("=" * 80)

    with transaction.atomic():
        # 1. Resolve Grade 10 & Subject CRE
        grade = Grade.objects.filter(id=5).first()
        if not grade:
            grade = Grade.objects.filter(name__icontains="Grade 10").first()
        if not grade:
            raise RuntimeError("Grade 10 (ID 5) not found!")

        subject = Subject.objects.filter(id=46).first()
        if not subject:
            subject = Subject.objects.filter(grade=grade, name__icontains="CRE").first()
        if not subject:
            raise RuntimeError("Subject CRE (ID 46) not found!")

        print(f"Verified Context: Grade='{grade.name}' (ID: {grade.id}), Subject='{subject.name}' (ID: {subject.id})")

        # 2. Resolve Topic 1.9.1 (Order 9)
        topic_order = TOPIC_DATA["topic_order"]
        topic_name = TOPIC_DATA["topic_name"]
        topic_desc = TOPIC_DATA["topic_description"]

        topic, t_created = Topic.objects.get_or_create(
            subject=subject,
            order=topic_order,
            defaults={
                "name": topic_name,
                "description": topic_desc
            }
        )
        if not t_created:
            topic.name = topic_name
            topic.description = topic_desc
            topic.save()

        print(f"Target Topic: '{topic.name}' (ID: {topic.id}, Order: {topic.order})")

        # If replacing, clear existing learning units & lessons for clean idempotent ingestion
        if replace:
            existing_units = LearningUnit.objects.filter(topic=topic)
            for u in existing_units:
                for l in u.lessons.all():
                    l.blocks.all().delete()
                    l.assets.all().delete()
                    l.delete()
                u.delete()
            print("  -> Cleared previous learning units, lessons, blocks, and assets for clean rebuild.")

        total_units = 0
        total_lessons = 0
        total_pages = 0
        total_blocks = 0
        total_assets = 0

        # 3. Ingest Each Learning Unit & Lesson
        for u_data in TOPIC_DATA["units"]:
            u_order = u_data["unit_order"]
            u_name = u_data["unit_name"]
            u_desc = u_data["unit_description"]
            l_title = u_data["lesson_title"]
            pages = u_data["pages"]

            # Create Learning Unit
            unit, _ = LearningUnit.objects.get_or_create(
                topic=topic,
                order=u_order,
                defaults={
                    "name": u_name,
                    "description": u_desc
                }
            )
            unit.name = u_name
            unit.description = u_desc
            unit.save()
            total_units += 1

            # Create Published Lesson (Version 1)
            lesson, _ = Lesson.objects.get_or_create(
                topic=topic,
                learning_unit=unit,
                defaults={
                    "title": l_title,
                    "status": "published",
                    "version": 1,
                    "immutable_metadata": {
                        "author": "VLearn Grade 10 CRE Topic 1.9.1 Ingestion Agent",
                        "curriculum": "CBC",
                        "grade_id": grade.id,
                        "subject_id": subject.id,
                        "topic_order": topic_order,
                        "unit_order": u_order
                    }
                }
            )
            lesson.title = l_title
            lesson.status = "published"
            lesson.version = 1
            lesson.save()
            total_lessons += 1

            # Clear any leftover blocks / assets
            lesson.blocks.all().delete()
            lesson.assets.all().delete()

            # Create LessonAsset 1: Authentic Photographic Wikimedia Hook
            img_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                source_type="external",
                storage_type="url",
                title=f"Visual Hook: {l_title}",
                url=u_data["image_url"],
                metadata={
                    "caption": u_data["image_caption"],
                    "source": "Wikimedia Commons",
                    "verified": True
                }
            )
            total_assets += 1

            # Create LessonAsset 2: Pedagogical Responsive Vector SVG Diagram
            svg_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="ai_generated",
                storage_type="url",
                title=f"Vector Blueprint: {l_title}",
                metadata={
                    "svg_content": u_data["svg_content"],
                    "responsive": True,
                    "viewBox": "0 0 800 450"
                }
            )
            total_assets += 1

            # Create LessonAsset 3: Curated Educational YouTube Video
            yt_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="youtube",
                source_type="external",
                storage_type="url",
                title=u_data["youtube_title"],
                url=f"https://www.youtube.com/watch?v={u_data['youtube_id']}",
                metadata={
                    "youtube_id": u_data["youtube_id"],
                    "description": u_data["youtube_description"]
                }
            )
            total_assets += 1

            # Ingest Progressive Pages & LessonBlocks
            block_order_counter = 1
            for page_idx, page_blocks in enumerate(pages, start=1):
                total_pages += 1
                for comp_idx, b_def in enumerate(page_blocks, start=1):
                    b_type = b_def["type"]
                    b_title = clean_text(b_def.get("title", ""))
                    b_content = clean_dict(b_def.get("content", {}))

                    # Inject resolved media assets into block content
                    if b_type == "suggested_image":
                        b_content["url"] = u_data["image_url"]
                        b_content["resolved_image_url"] = u_data["image_url"]
                        b_content["source"] = "Wikimedia Commons"
                    elif b_type == "suggested_diagram":
                        b_content["svg"] = u_data["svg_content"]
                        b_content["svg_xml"] = u_data["svg_content"]
                    elif b_type == "suggested_video":
                        b_content["url"] = f"https://www.youtube.com/watch?v={u_data['youtube_id']}"
                        b_content["youtube_id"] = u_data["youtube_id"]

                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=f"g10_cre_t1_9_1_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_order_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={
                            "topic_order": topic_order,
                            "unit_order": u_order,
                            "page_index": page_idx
                        }
                    )

                    # Explicitly link LessonAsset records to their corresponding LessonBlocks
                    if b_type == "suggested_image":
                        block.assets.add(img_asset)
                    elif b_type == "suggested_diagram":
                        block.assets.add(svg_asset)
                    elif b_type == "suggested_video":
                        block.assets.add(yt_asset)

                    block_order_counter += 1
                    total_blocks += 1

            print(f"  -> Ingested Unit {u_order}: '{u_name}' -> Lesson '{l_title}' ({len(pages)} Cards, {block_order_counter - 1} Blocks, 3 Linked Assets)")

        print("=" * 80)
        print("INGESTION COMPLETED SUCCESSFULLY!")
        print(f"  Target Topic: {topic.name} (ID: {topic.id})")
        print(f"  Learning Units Created: {total_units}")
        print(f"  Published Lessons Created: {total_lessons}")
        print(f"  Total Lesson Pages (Cards): {total_pages}")
        print(f"  Total Lesson Blocks: {total_blocks}")
        print(f"  Total Lesson Assets: {total_assets}")
        print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--no-replace" not in sys.argv
    ingest_grade10_cre_topic_1_9_1(replace=replace_flag)
