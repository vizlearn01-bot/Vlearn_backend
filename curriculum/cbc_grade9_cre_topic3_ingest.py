"""
VLearn CBC Grade 9 CRE — Topic 3: Judge Deborah
Ingestion and Enrichment Script for all 6 Lessons

Target Grade: Grade 9 (Grade ID: 18)
Target Subject: CRE (Subject ID: 50)
Target Topic: Topic 3: Judge Deborah (Order: 3)

Lessons Ingested:
1. Lesson 1: Introduction to the Era of the Judges (Judges 2:16-19, 17:6)
2. Lesson 2: The Calling and Court of Judge Deborah (Judges 4:1-5)
3. Lesson 3: The Battle of Mount Tabor and the Victory (Judges 4:6-16, 4:17-24)
4. Lesson 4: Leadership Traits of Deborah (Judges 4:4-9, 5:7)
5. Lesson 5: Lessons from the Song of Deborah and Barak (Judges 5:1-31)
6. Lesson 6: Applying Deborah's Leadership Today (Romans 12:4-8, Galatians 3:28)

Structure per Lesson: 6 Cards/Pages, 13 Blocks, 3 Assets (suggested_image, suggested_diagram, suggested_video)
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
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)


def clean_text(text: str) -> str:
    """Removes bracket citations, internal meta tags, and normalizes text."""
    if not text:
        return ""
    # Strip bracket citations e.g. [201], [525, 528], [68, 69, 525, 528]
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Strip internal pedagogical tags e.g. [VISUAL...], [BIBLE REFERENCE...], etc.
    text = re.sub(r'\[(VISUAL|BIBLE REFERENCE|BIBLE PASSAGE|REAL WORLD APPLICATION|REFLECTION|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|BIBLICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|ARTWORK|MAP|TIMELINE|COMPARISON|INFOGRAPHIC)[^\]]*\]', '', text, flags=re.IGNORECASE)
    # Normalize list bullet points
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


# ─── SVG VECTOR DIAGRAMS (viewBox="0 0 800 450", theme #0f172a) ───────────────

def get_svg_lesson1():
    """Lesson 1: The Cyclical Pattern of the Era of the Judges"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="peaceGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="sinGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#b91c1c"/>
    </linearGradient>
    <linearGradient id="oppressGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f97316"/>
      <stop offset="100%" stop-color="#c2410c"/>
    </linearGradient>
    <linearGradient id="repentGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="deliverGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <filter id="cardShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Background Base -->
  <rect width="800" height="450" fill="url(#bgGrad)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <!-- Header Section -->
  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE REPEATING CYCLE OF THE JUDGES</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">Israel's 6-Stage Historical Pattern of Sin, Oppression, and God's Merciful Deliverance (Judges 2:16-19)</text>

  <!-- Circular Pathway connecting stages -->
  <ellipse cx="400" cy="245" rx="280" ry="140" fill="none" stroke="#334155" stroke-width="2.5" stroke-dasharray="8 6"/>

  <!-- STAGE 1: Peace & Obedience (Top Left) -->
  <g transform="translate(140, 95)" filter="url(#cardShadow)">
    <rect width="180" height="85" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="180" height="26" rx="10" fill="url(#peaceGrad)"/>
    <text x="90" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. PEACE &amp; COVENANT</text>
    <text x="10" y="45" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Israel serves God</text>
    <text x="10" y="62" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Land has rest and security</text>
    <text x="10" y="76" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Prosperity under God's law</text>
  </g>

  <!-- STAGE 2: Sin & Idolatry (Top Right) -->
  <g transform="translate(480, 95)" filter="url(#cardShadow)">
    <rect width="180" height="85" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="180" height="26" rx="10" fill="url(#sinGrad)"/>
    <text x="90" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. SIN &amp; IDOLATRY</text>
    <text x="10" y="45" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Forsakes Yahweh</text>
    <text x="10" y="62" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Worships Baals &amp; Asherah</text>
    <text x="10" y="76" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Moral decline and anarchy</text>
  </g>

  <!-- STAGE 3: Oppression (Middle Right) -->
  <g transform="translate(560, 205)" filter="url(#cardShadow)">
    <rect width="190" height="85" rx="10" fill="#1e293b" stroke="#f97316" stroke-width="1.5"/>
    <rect width="190" height="26" rx="10" fill="url(#oppressGrad)"/>
    <text x="95" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. ENEMY OPPRESSION</text>
    <text x="10" y="45" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• God removes protection</text>
    <text x="10" y="62" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Foreign invaders rule</text>
    <text x="10" y="76" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Brutal suffering &amp; tribute</text>
  </g>

  <!-- STAGE 4: Repentance (Bottom Right) -->
  <g transform="translate(480, 310)" filter="url(#cardShadow)">
    <rect width="180" height="85" rx="10" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect width="180" height="26" rx="10" fill="url(#repentGrad)"/>
    <text x="90" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">4. CRY OF REPENTANCE</text>
    <text x="10" y="45" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Desperation in affliction</text>
    <text x="10" y="62" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Cries out to the Lord</text>
    <text x="10" y="76" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Turns from false idols</text>
  </g>

  <!-- STAGE 5: Deliverance by Judge (Bottom Left) -->
  <g transform="translate(140, 310)" filter="url(#cardShadow)">
    <rect width="180" height="85" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="180" height="26" rx="10" fill="url(#deliverGrad)"/>
    <text x="90" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">5. GOD RAISES A JUDGE</text>
    <text x="10" y="45" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Charismatic leader sent</text>
    <text x="10" y="62" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Military &amp; legal rescue</text>
    <text x="10" y="76" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Oppressors defeated</text>
  </g>

  <!-- Center Hub: Central Theocratic Truth -->
  <circle cx="400" cy="245" r="62" fill="#1e293b" stroke="#fbbf24" stroke-width="2.5" filter="url(#cardShadow)"/>
  <text x="400" y="235" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">THEOCRACY</text>
  <text x="400" y="250" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">God as King</text>
  <text x="400" y="265" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Judges 21:25</text>

  <!-- Footer Tagline -->
  <text x="400" y="424" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">VLEARN CBC GRADE 9 CRE • TOPIC 3: JUDGE DEBORAH • LESSON 1 PEDAGOGICAL CONCEPT MAP</text>
</svg>"""


def get_svg_lesson2():
    """Lesson 2: The Multi-Faceted Calling & Public Court of Deborah"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="blueGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="pinkGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ec4899"/>
      <stop offset="100%" stop-color="#be185d"/>
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <filter id="shadow2" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <!-- Background Base -->
  <rect width="800" height="450" fill="url(#bgGrad2)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <!-- Header Section -->
  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE CALLING AND ROLES OF JUDGE DEBORAH</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">Fourfold Calling &amp; Accessible Palm Court Ministry (Judges 4:1-5)</text>

  <!-- Center Hub: Deborah under the Palm Tree -->
  <g transform="translate(290, 100)" filter="url(#shadow2)">
    <rect width="220" height="240" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <rect width="220" height="38" rx="12" fill="url(#goldGrad)"/>
    <text x="110" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">PALM OF DEBORAH</text>
    
    <text x="110" y="65" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">LOCATION &amp; COURT</text>
    <text x="110" y="85" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" text-anchor="middle">Between Ramah &amp; Bethel</text>
    <text x="110" y="100" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Hill Country of Ephraim</text>

    <!-- Divider Line -->
    <line x1="20" y1="115" x2="200" y2="115" stroke="#334155" stroke-width="1.5"/>

    <text x="110" y="135" fill="#10b981" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">PALM COURT PRINCIPLE</text>
    <text x="110" y="155" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Public &amp; Accessible</text>
    <text x="110" y="172" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Non-Hierarchical Justice</text>
    <text x="110" y="189" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Listening &amp; Wise Counsel</text>
    <text x="110" y="206" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">• Resolving Tribal Disputes</text>
    <text x="110" y="226" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">"Israel went up to her"</text>
  </g>

  <!-- Surrounding Role 1: Prophetess (Top Left) -->
  <g transform="translate(45, 95)" filter="url(#shadow2)">
    <rect width="210" height="110" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="210" height="28" rx="10" fill="url(#blueGrad2)"/>
    <text x="105" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">1. PROPHETESS (NABI'AH)</text>
    <text x="12" y="48" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">• Receives divine revelation</text>
    <text x="12" y="65" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Speaks God's direct truth</text>
    <text x="12" y="82" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Spiritual discernment &amp; clarity</text>
    <text x="12" y="99" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="600">Judges 4:4</text>
  </g>

  <!-- Surrounding Role 2: Wife of Lappidoth (Bottom Left) -->
  <g transform="translate(45, 230)" filter="url(#shadow2)">
    <rect width="210" height="110" rx="10" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="210" height="28" rx="10" fill="url(#pinkGrad)"/>
    <text x="105" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">2. WIFE OF LAPPIDOTH</text>
    <text x="12" y="48" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">• Family &amp; marital integrity</text>
    <text x="12" y="65" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Balances family &amp; state duties</text>
    <text x="12" y="82" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Rooted in domestic faithfulness</text>
    <text x="12" y="99" fill="#ec4899" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">Judges 4:4</text>
  </g>

  <!-- Surrounding Role 3: Judge & Arbiter (Top Right) -->
  <g transform="translate(545, 95)" filter="url(#shadow2)">
    <rect width="210" height="110" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="210" height="28" rx="10" fill="url(#greenGrad)"/>
    <text x="105" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">3. JUDGE &amp; ARBITER (SHOPHET)</text>
    <text x="12" y="48" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">• Settles civil &amp; tribal cases</text>
    <text x="12" y="65" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Applies Mosaic covenant law</text>
    <text x="12" y="82" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Impartial justice for all tribes</text>
    <text x="12" y="99" fill="#10b981" font-family="system-ui, sans-serif" font-size="9" font-weight="600">Judges 4:5</text>
  </g>

  <!-- Surrounding Role 4: Mother in Israel (Bottom Right) -->
  <g transform="translate(545, 230)" filter="url(#shadow2)">
    <rect width="210" height="110" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="210" height="28" rx="10" fill="url(#goldGrad)"/>
    <text x="105" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">4. MOTHER IN ISRAEL</text>
    <text x="12" y="48" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">• Nurtures and defends nation</text>
    <text x="12" y="65" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Restores safety and peace</text>
    <text x="12" y="82" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Protective patriotic love</text>
    <text x="12" y="99" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="600">Judges 5:7</text>
  </g>

  <!-- Connecting Lines from Hub to Roles -->
  <line x1="255" y1="150" x2="290" y2="180" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4 3"/>
  <line x1="255" y1="285" x2="290" y2="240" stroke="#ec4899" stroke-width="1.5" stroke-dasharray="4 3"/>
  <line x1="510" y1="180" x2="545" y2="150" stroke="#10b981" stroke-width="1.5" stroke-dasharray="4 3"/>
  <line x1="510" y1="240" x2="545" y2="285" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4 3"/>

  <!-- Footer Tagline -->
  <text x="400" y="424" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">VLEARN CBC GRADE 9 CRE • TOPIC 3: JUDGE DEBORAH • LESSON 2 PEDAGOGICAL CONCEPT MAP</text>
</svg>"""


def get_svg_lesson3():
    """Lesson 3: Tactical Battle of Mount Tabor and Jael's Fulfillment"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="israelGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="canaanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#991b1b"/>
    </linearGradient>
    <linearGradient id="riverGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#06b6d4"/>
      <stop offset="100%" stop-color="#0e7490"/>
    </linearGradient>
    <linearGradient id="jaelGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <filter id="shadow3" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <!-- Background Base -->
  <rect width="800" height="450" fill="url(#bgGrad3)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <!-- Header Section -->
  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">THE BATTLE OF MOUNT TABOR &amp; DEFEAT OF SISERA</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">Strategic Mobilization, Divine Intervention at Kishon River, and Jael's Prophetic Victory (Judges 4:6-24)</text>

  <!-- Strategic Stage 1: Mount Tabor (Top Left) -->
  <g transform="translate(35, 95)" filter="url(#shadow3)">
    <rect width="215" height="135" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="215" height="28" rx="10" fill="url(#israelGrad)"/>
    <text x="107" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. MOUNT TABOR (ISRAEL)</text>
    <text x="12" y="48" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">• Barak &amp; Deborah lead</text>
    <text x="12" y="65" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• 10,000 men from Naphtali/Zebulun</text>
    <text x="12" y="82" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• High ground tactical advantage</text>
    <text x="12" y="99" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">• Charge command: "Up! The Lord goes"</text>
    <text x="12" y="118" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="8.5">Judges 4:14</text>
  </g>

  <!-- Strategic Stage 2: Sisera's 900 Chariots (Top Right) -->
  <g transform="translate(550, 95)" filter="url(#shadow3)">
    <rect width="215" height="135" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="215" height="28" rx="10" fill="url(#canaanGrad)"/>
    <text x="107" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. CANAANITE CHARIOTS</text>
    <text x="12" y="48" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">• Sisera commands 900 iron chariots</text>
    <text x="12" y="65" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Overwhelming military technology</text>
    <text x="12" y="82" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Deployed in Jezreel Valley plains</text>
    <text x="12" y="99" fill="#f87171" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">• 20 years of cruel oppression</text>
    <text x="12" y="118" fill="#ef4444" font-family="system-ui, sans-serif" font-size="8.5">Judges 4:3, 13</text>
  </g>

  <!-- Central Clash: Kishon River Mud & Panic -->
  <g transform="translate(290, 130)" filter="url(#shadow3)">
    <rect width="220" height="170" rx="12" fill="#1e293b" stroke="#06b6d4" stroke-width="2"/>
    <rect width="220" height="34" rx="12" fill="url(#riverGrad)"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">KISHON RIVER FLASH FLOOD</text>
    
    <text x="110" y="55" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">DIVINE INTERVENTION</text>
    <text x="15" y="75" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9.5">• Torrential rains swell Kishon</text>
    <text x="15" y="92" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9.5">• Heavy iron chariots sink in mud</text>
    <text x="15" y="109" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9.5">• Lord throws army into panic</text>
    <text x="15" y="126" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9.5">• Barak's men route army</text>
    <text x="15" y="145" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">• Sisera flees on foot alone</text>
    <text x="110" y="160" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Judges 4:15, 5:21</text>
  </g>

  <!-- Flow Arrows connecting to Kishon -->
  <path d="M 250 162 L 290 180" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="5 3"/>
  <path d="M 550 162 L 510 180" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="5 3"/>

  <!-- Stage 3: Tent of Jael (Bottom Center) -->
  <g transform="translate(180, 315)" filter="url(#shadow3)">
    <rect width="440" height="80" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="440" height="26" rx="10" fill="url(#jaelGrad)"/>
    <text x="220" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">3. THE TENT OF JAEL — PROPHECY FULFILLED (JUDGES 4:17-22)</text>
    <text x="15" y="44" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">• Sisera hides in tent of Jael (Kenite) | Jael offers hospitality, milk &amp; rug</text>
    <text x="15" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• In exhaustion, Sisera sleeps | Jael drives tent peg through his temple</text>
    <text x="15" y="74" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">• Deborah's prophecy fulfilled: "The Lord will deliver Sisera into the hands of a woman!" (Judges 4:9)</text>
  </g>

  <!-- Footer Tagline -->
  <text x="400" y="424" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">VLEARN CBC GRADE 9 CRE • TOPIC 3: JUDGE DEBORAH • LESSON 3 PEDAGOGICAL CONCEPT MAP</text>
</svg>"""


def get_svg_lesson4():
    """Lesson 4: Core Leadership Traits of Deborah vs Secular Model"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="debGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="secGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#991b1b"/>
    </linearGradient>
    <filter id="shadow4" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <!-- Background Base -->
  <rect width="800" height="450" fill="url(#bgGrad4)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <!-- Header Section -->
  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">LEADERSHIP TRAITS OF DEBORAH VS. SECULAR LEADERSHIP</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">A Biblical Blueprint for God-Fearing, Servant Leadership (Judges 4:4-9, 5:7)</text>

  <!-- Left Column: Deborah's God-Centered Leadership (7 Traits) -->
  <g transform="translate(40, 85)" filter="url(#shadow4)">
    <rect width="345" height="310" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="345" height="34" rx="10" fill="url(#debGrad)"/>
    <text x="172" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">DEBORAH'S GODLY LEADERSHIP MODEL</text>
    
    <text x="15" y="58" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">1. Courageous:</text>
    <text x="110" y="58" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">Goes to frontlines with Barak (Jdg 4:9)</text>

    <text x="15" y="88" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">2. Wise &amp; Discerning:</text>
    <text x="135" y="88" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">Listens and judges impartially</text>

    <text x="15" y="118" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">3. Supportive Partner:</text>
    <text x="140" y="118" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">Empowers Barak without jealousy</text>

    <text x="15" y="148" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">4. Trustworthy:</text>
    <text x="110" y="148" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">Earns the confidence of all 12 tribes</text>

    <text x="15" y="178" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">5. Direct &amp; Honest:</text>
    <text x="130" y="178" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">Speaks God's uncompromised truth</text>

    <text x="15" y="208" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">6. Confident in God:</text>
    <text x="135" y="208" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">Relies on divine power, not weapons</text>

    <text x="15" y="238" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">7. Truly Humble:</text>
    <text x="115" y="238" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">Gives 100% praise to God in song</text>

    <!-- Bottom summary bar in card -->
    <rect x="15" y="260" width="315" height="36" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="172" y="282" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">Result: 40 Years of National Peace &amp; Security (Judges 5:31)</text>
  </g>

  <!-- Right Column: Flawed Secular Leadership Model -->
  <g transform="translate(415, 85)" filter="url(#shadow4)">
    <rect width="345" height="310" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="345" height="34" rx="10" fill="url(#secGrad)"/>
    <text x="172" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">SECULAR / AUTHORITARIAN MODEL</text>
    
    <text x="15" y="58" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">1. Self-Serving:</text>
    <text x="110" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Seeks personal gain, wealth &amp; titles</text>

    <text x="15" y="88" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">2. Aloof &amp; Distant:</text>
    <text x="120" y="88" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Rules from isolated, closed palaces</text>

    <text x="15" y="118" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">3. Coercive Force:</text>
    <text x="120" y="118" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Relies on fear, weapons &amp; chariots</text>

    <text x="15" y="148" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">4. Manipulative:</text>
    <text x="115" y="148" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Divides people through tribalism/bribes</text>

    <text x="15" y="178" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">5. Arrogant &amp; Proud:</text>
    <text x="135" y="178" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Claims all credit for collective success</text>

    <text x="15" y="208" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">6. Discriminatory:</text>
    <text x="125" y="208" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Marginalizes women &amp; the vulnerable</text>

    <text x="15" y="238" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">7. Blame-Shifting:</text>
    <text x="120" y="238" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Abandons followers when crisis hits</text>

    <!-- Bottom summary bar in card -->
    <rect x="15" y="260" width="315" height="36" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="172" y="282" fill="#ef4444" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">Result: Oppression, Fear, Division &amp; Eventual Collapse</text>
  </g>

  <!-- Footer Tagline -->
  <text x="400" y="424" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">VLEARN CBC GRADE 9 CRE • TOPIC 3: JUDGE DEBORAH • LESSON 4 PEDAGOGICAL CONCEPT MAP</text>
</svg>"""


def get_svg_lesson5():
    """Lesson 5: Theological Pillars of the Song of Deborah (Judges 5)"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="hGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#a855f7"/>
      <stop offset="100%" stop-color="#6b21a8"/>
    </linearGradient>
    <linearGradient id="c1Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="c2Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="c3Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <filter id="shadow5" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <!-- Background Base -->
  <rect width="800" height="450" fill="url(#bgGrad5)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <!-- Header Section -->
  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">THEOLOGICAL PILLARS OF THE SONG OF DEBORAH</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">Lessons on Complacency, Swift Gratitude, and Civic Mobilization (Judges 5:1-31)</text>

  <!-- 3 Pillar Cards Layout -->

  <!-- PILLAR 1: Warning on Complacency (Left) -->
  <g transform="translate(35, 95)" filter="url(#shadow5)">
    <rect width="225" height="235" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="225" height="32" rx="10" fill="url(#c1Grad)"/>
    <text x="112" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. DANGER OF COMPLACENCY</text>
    
    <text x="15" y="55" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Past Breakdown (Jdg 5:6-8):</text>
    <text x="15" y="73" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9.5">• Highways deserted &amp; unsafe</text>
    <text x="15" y="90" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9.5">• Village life ceased in fear</text>
    <text x="15" y="107" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9.5">• Chose new false gods</text>

    <line x1="15" y1="122" x2="210" y2="122" stroke="#334155" stroke-width="1"/>

    <text x="15" y="142" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Core Ethical Warning:</text>
    <text x="15" y="160" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Prosperity breeds comfort,</text>
    <text x="15" y="175" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">which leads to idolatry and</text>
    <text x="15" y="190" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">destruction. Spiritual alertness</text>
    <text x="15" y="205" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">must be maintained in peace.</text>
  </g>

  <!-- PILLAR 2: Swift Gratitude & Worship (Center) -->
  <g transform="translate(285, 95)" filter="url(#shadow5)">
    <rect width="230" height="235" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="230" height="32" rx="10" fill="url(#c2Grad)"/>
    <text x="115" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. SWIFT GRATITUDE &amp; PRAISE</text>
    
    <text x="15" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Immediate Response (Jdg 5:1-3):</text>
    <text x="15" y="73" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9.5">• Sang on that very day</text>
    <text x="15" y="90" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9.5">• Acknowledged Yahweh's victory</text>
    <text x="15" y="107" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9.5">• Guarded against pride</text>

    <line x1="15" y1="122" x2="215" y2="122" stroke="#334155" stroke-width="1"/>

    <text x="15" y="142" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Theological Lesson:</text>
    <text x="15" y="160" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Never delay in thanking God</text>
    <text x="15" y="175" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">for triumphs. Gratitude keeps</text>
    <text x="15" y="190" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">the heart humble and renews</text>
    <text x="15" y="205" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">the sacred covenant.</text>
  </g>

  <!-- PILLAR 3: Commending Willing vs Condemning Idle (Right) -->
  <g transform="translate(540, 95)" filter="url(#shadow5)">
    <rect width="225" height="235" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="225" height="32" rx="10" fill="url(#c3Grad)"/>
    <text x="112" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. TRIBAL PARTICIPATION</text>
    
    <text x="15" y="55" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Willing Commended (Jdg 5:18):</text>
    <text x="15" y="73" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9.5">• Zebulun &amp; Naphtali risked lives</text>
    <text x="15" y="90" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9.5">• Ephraim, Benjamin, Issachar</text>

    <line x1="15" y1="105" x2="210" y2="105" stroke="#334155" stroke-width="1"/>

    <text x="15" y="125" fill="#f87171" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Idle Condemned (Jdg 5:15-17):</text>
    <text x="15" y="143" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9.5">• Reuben lingered by sheepfolds</text>
    <text x="15" y="160" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9.5">• Dan stayed by ships; Asher at coast</text>
    <text x="15" y="177" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9.5">• Selfish neutrality is rebuked</text>

    <text x="15" y="200" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="600">Universal civic duty to unite</text>
  </g>

  <!-- Bottom Anchor Summary Bar -->
  <rect x="35" y="348" width="730" height="50" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
  <text x="400" y="368" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">KEY THEOLOGICAL BENCHMARK: JUDGES 5:31</text>
  <text x="400" y="386" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">"So may all your enemies perish, Lord! But may all who love you be like the sun when it rises in its strength."</text>

  <!-- Footer Tagline -->
  <text x="400" y="424" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">VLEARN CBC GRADE 9 CRE • TOPIC 3: JUDGE DEBORAH • LESSON 5 PEDAGOGICAL CONCEPT MAP</text>
</svg>"""


def get_svg_lesson6():
    """Lesson 6: Modern Application — 4 Pillars of Palm Tree Leadership"""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="b1Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ec4899"/>
      <stop offset="100%" stop-color="#be185d"/>
    </linearGradient>
    <linearGradient id="b2Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="b3Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="b4Grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <filter id="shadow6" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <!-- Background Base -->
  <rect width="800" height="450" fill="url(#bgGrad6)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <!-- Header Section -->
  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" text-anchor="middle" letter-spacing="0.5">PALM TREE LEADERSHIP FOR 21ST-CENTURY YOUTH</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, -apple-system, sans-serif" font-size="12" text-anchor="middle">Applying Deborah's Principles to School, Family, Church, and Kenyan National Governance</text>

  <!-- 4 Application Pillars (2x2 Grid) -->

  <!-- Top-Left: Gender Equality & Empowerment -->
  <g transform="translate(35, 85)" filter="url(#shadow6)">
    <rect width="350" height="135" rx="10" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="350" height="28" rx="10" fill="url(#b1Grad)"/>
    <text x="175" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">1. GENDER EQUALITY &amp; EMPOWERMENT</text>
    <text x="15" y="48" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• God calls leaders based on character, not gender</text>
    <text x="15" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Support and respect women in student leadership &amp; public office</text>
    <text x="15" y="83" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Break cultural stereotypes against girls' leadership potential</text>
    <text x="15" y="101" fill="#f472b6" font-family="system-ui, sans-serif" font-size="9" font-weight="600">Galatians 3:28 • "One in Christ Jesus"</text>
  </g>

  <!-- Top-Right: Accessible & Humble Service -->
  <g transform="translate(415, 85)" filter="url(#shadow6)">
    <rect width="350" height="135" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="350" height="28" rx="10" fill="url(#b2Grad)"/>
    <text x="175" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">2. ACCESSIBLE &amp; HUMBLE SERVICE</text>
    <text x="15" y="48" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Lead from the "Palm Tree" — be approachable and open</text>
    <text x="15" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Practice active listening to understand classmates' problems</text>
    <text x="15" y="83" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Avoid arrogance, elitism, and misuse of prefect authority</text>
    <text x="15" y="101" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9" font-weight="600">1 Timothy 4:12 • "Set an example in speech and conduct"</text>
  </g>

  <!-- Bottom-Left: Collaborative Teamwork -->
  <g transform="translate(35, 235)" filter="url(#shadow6)">
    <rect width="350" height="135" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="350" height="28" rx="10" fill="url(#b3Grad)"/>
    <text x="175" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">3. COLLABORATION &amp; PARTNERSHIP</text>
    <text x="15" y="48" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Empower and partner with others (Deborah &amp; Barak model)</text>
    <text x="15" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Share responsibility and walk alongside team members</text>
    <text x="15" y="83" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Avoid monopolizing credit; build collective school spirit</text>
    <text x="15" y="101" fill="#34d399" font-family="system-ui, sans-serif" font-size="9" font-weight="600">Romans 12:4-8 • "One body with many diverse gifts"</text>
  </g>

  <!-- Bottom-Right: Integrity & Anti-Corruption -->
  <g transform="translate(415, 235)" filter="url(#shadow6)">
    <rect width="350" height="135" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="350" height="28" rx="10" fill="url(#b4Grad)"/>
    <text x="175" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">4. INTEGRITY &amp; CIVIC COURAGE</text>
    <text x="15" y="48" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Stand firmly against tribalism, bribery, and nepotism</text>
    <text x="15" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Speak direct truth without fear or dishonest compromise</text>
    <text x="15" y="83" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">• Vote for school and national leaders of high moral character</text>
    <text x="15" y="101" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" font-weight="600">Proverbs 3:5-6 • "Submit to Him and He will make paths straight"</text>
  </g>

  <!-- Footer Tagline -->
  <text x="400" y="424" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">VLEARN CBC GRADE 9 CRE • TOPIC 3: JUDGE DEBORAH • LESSON 6 PEDAGOGICAL CONCEPT MAP</text>
</svg>"""


# ─── LESSON DATA CONFIGURATIONS (ALL 6 LESSONS) ────────────────────────────────

LESSONS_DATA = [
    # ───────────────────────────────────────────────────────────────────────────
    # LESSON 1
    # ───────────────────────────────────────────────────────────────────────────
    {
        "unit_order": 1,
        "unit_name": "Introduction to the Era of the Judges",
        "unit_description": "Examine the historical and political transition of Israel after Joshua, the charismatic role of Judges in ancient Israel, the 6-stage cycle of sin and deliverance, and the major Judges raised by God.",
        "lesson_title": "Introduction to the Era of the Judges",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Foster_Bible_Pictures_0109-1_The_Israelites_Cry_to_God_for_Help.jpg",
            "title": "The Israelites Cry to God for Help during Oppression",
            "author": "Charles Foster (Foster Bible Pictures, 1897)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Historical illustration showing the Israelites groaning in oppression and turning their hearts back to God in prayer during the tumultuous era of the Judges."
        },
        "youtube": {
            "youtube_id": "kOYy8iCf648",
            "title": "BibleProject: Judges",
            "description": "Comprehensive visual overview of the Book of Judges, breaking down Israel's moral decay, the repeating cyclical patterns of idolatry, and God's sovereign work through flawed yet faithful tribal deliverers."
        },
        "svg_fn": get_svg_lesson1,
        "goals": [
            "Explain the historical, political, and religious transition of Israel from the leadership of Joshua to the era of the Judges.",
            "Analyze the four primary duties of Judges in Israel (military deliverance, judicial dispute resolution, spiritual guidance, and sacrificial duties) and trace the 6-stage cycle of sin and restoration in Judges 2:16-19.",
            "Apply the ethical principle of obedience and accountability by consulting wise leadership in personal and community dispute resolution."
        ],
        "intro": """Imagine a nation without a president, a parliament, police officers, or a written national constitution. How would citizens know what is right? How would boundaries and violent disputes be settled?

In the early centuries following Israel's settlement in Canaan, the nation lived under a pure theocracy—God alone was their King. Instead of a centralized human monarchy, God raised up local, charismatic leaders known as **Judges** (*Shophetim*) whenever the people were oppressed. These leaders were not merely courtroom judges; they were God-empowered military rescuers, legal arbiters, and spiritual guides who defended the tribes and preserved the covenant of Yahweh.""",
        "core_scripture": """### Biblical Foundations: The Role and Era of the Judges

#### Judges 2:16-19 — The Divine Institution of Deliverers
> *"Then the Lord raised up judges, who saved them out of the hands of these raiders. Yet they would not listen to their judges but prostituted themselves to other gods and worshiped them. They quickly turned from the ways of their ancestors, who had been obedient to the Lord’s commands. Whenever the Lord raised up a judge for them, he was with the judge and saved them out of the hands of their enemies as long as the judge lived; for the Lord relented because of their groaning under those who afflicted and oppressed them. But when the judge died, the people returned to ways even more corrupt than those of their ancestors, following other gods and serving and worshiping them."*

#### Judges 17:6 & Judges 21:25 — The Moral Dilemma of Israel
> *"In those days Israel had no king; everyone did as they saw fit."*""",
        "theological_pillars": """### Theological Exegesis: Theocracy, Covenant, and Charismatic Leadership

1. **Pure Theocracy vs. Human Monarchy:** Israel was uniquely constituted as a theocratic nation where Yahweh was Supreme King, Lawgiver, and Protector. God's covenant given through Moses was the supreme standard for civil, religious, and moral conduct.
2. **The Charismatic Nature of the Judges:** Unlike hereditary kings whose sons automatically inherited thrones, Judges were individually selected, called, and empowered by the Spirit of God (*Ruach Yahweh*) based on faith and readiness to serve.
3. **Four Distinct Duties of Judges:**
   - **Military Deliverance:** Marshaling tribal militias to defeat invading oppressors (e.g., Moabites, Midianites, Philistines).
   - **Judicial Dispute Resolution:** Hearing cases, arbitrating boundary disputes, and enforcing Mosaic justice.
   - **Spiritual Reformation:** Denouncing idolatry (Baal and Asherah worship) and calling the twelve tribes back to exclusive covenant worship.
   - **Sacrificial & Pastoral Guidance:** Interceding for the people and offering sacrifices during national crises.
4. **Major Judges of Israel:** Scripture records prominent judges including **Othniel** (first judge), **Ehud** (defeated Moab), **Deborah** (prophetess and judge), **Gideon** (defeated Midian with 300 men), **Samson** (fought Philistines with supernatural strength), and **Samuel** (last judge and prophet).""",
        "deep_dive": """### Deep Dive: The 6-Stage Downward Spiral of the Judges

The Book of Judges reveals a predictable theological cycle that governed Israel's history for over 300 years:

- **Stage 1: Peace and Covenant Faithfulness:** Under a faithful leader, Israel lives in obedience to God's law. The land enjoys rest, agricultural bounty, and security.
- **Stage 2: Complacency, Sin, and Idolatry:** With peace comes spiritual laziness. The next generation forgets God's mighty acts, intermarries with Canaanites, and serves local fertility idols (Baal and Asherah).
- **Stage 3: Divine Judgment and Enemy Oppression:** Because Israel violated the covenant, God removes His protective shield and allows aggressive neighboring nations (Canaanites, Philistines, Moabites) to subjugate them.
- **Stage 4: Groaning and Sincere Repentance:** Crushed by heavy taxation, loss of harvest, and violence, Israel repents of idolatry and cries out desperately to Yahweh for mercy.
- **Stage 5: Charismatic Deliverer Raised:** Moved by compassion, God raises a Judge, equips them with spiritual power, and delivers Israel through miraculous military victories.
- **Stage 6: Period of Rest:** Peace is restored for decades (often 40 or 80 years). But upon the Judge's death, the cycle restarts—often in an even deeper state of moral decay.""",
        "practical": {
            "title": "Action Framework: 4 Steps to Resolving Disputes through Wise Guidance",
            "steps": [
                "Step 1: Identify the Root Conflict — Acknowledge misunderstandings, hurt feelings, or boundary violations objectively before emotions escalate into physical fights or insults.",
                "Step 2: Resist Doing 'What Is Right in Your Own Eyes' — Refuse to take revenge or make unilateral decisions driven by pride; submit to established moral and institutional rules.",
                "Step 3: Consult Impartial, Wise Arbiters — Approach trusted, God-fearing authorities such as teachers, school counselors, parents, or pastors to mediate the disagreement fairly.",
                "Step 4: Commit to Restitution and Peace — Accept the mediator's counsel in humility, offer sincere apologies where wrong, and restore healthy relationships with peers."
            ]
        },
        "kenyan_context": """In Kenya today, the lessons from the era of the Judges remind us of the vital importance of the rule of law and ethical leadership. When citizens ignore constitutional principles and 'do whatever is right in their own eyes,' communities suffer from corruption, tribal clashes, and social injustice. Just as the Israelites sought wisdom from impartial Judges, Kenyans rely on village elders (*Wazee wa Mtaa*), religious leaders, and formal justice courts to resolve land, family, and community disputes peacefully.""",
        "reflection": """### Spiritual Reflection: Covenant Faithfulness in a Permissive Society

Judges 21:25 notes: *"In those days Israel had no king; everyone did as they saw fit."*

- What are the real spiritual and social dangers when everyone in a school or community defines their own standard of morality without reference to God's Word?
- How can you maintain steadfast spiritual discipline during seasons of ease and prosperity so that you do not fall into complacency and moral decline?""",
        "takeaways": [
            "The era of the Judges was a theocratic period where God ruled Israel through charismatic leaders rather than a human king.",
            "Judges functioned as military commanders, legal arbiters, spiritual reformers, and covenant guardians.",
            "Israel's history followed a recurring 6-stage cycle: Peace → Sin & Idolatry → Oppression → Cry of Repentance → Deliverance by a Judge → Temporary Rest.",
            "Major judges included Othniel, Ehud, Deborah, Gideon, Samson, and Samuel.",
            "True freedom is found in joyful obedience to God's moral law rather than moral relativism where everyone does whatever seems right in their own eyes."
        ],
        "mcq": {
            "question": "According to Judges 2:16-19, why did God raise up Judges in ancient Israel?",
            "options": [
                "A) To establish a hereditary royal dynasty with royal palaces and standing armies",
                "B) To deliver Israel from foreign oppressors and restore covenant justice when the people cried out in repentance",
                "C) To collect imperial taxes and construct stone temples across Canaan",
                "D) To repeal the Ten Commandments and write new civil laws for each tribe"
            ],
            "answer": "B",
            "explanation": "Judges were charismatic leaders raised by God in response to Israel's repentance to deliver them from invading oppressors, settle legal disputes, and restore covenant faithfulness."
        }
    },

    # ───────────────────────────────────────────────────────────────────────────
    # LESSON 2
    # ───────────────────────────────────────────────────────────────────────────
    {
        "unit_order": 2,
        "unit_name": "The Calling and Court of Judge Deborah",
        "unit_description": "Examine Israel's 20-year oppression under King Jabin and Sisera's 900 iron chariots, Deborah's multi-faceted identity as prophetess, wife, judge, and mother in Israel, and her public palm court ministry.",
        "lesson_title": "The Calling and Court of Judge Deborah",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/9/90/109.Deborah_under_the_Palm-Tree.jpg",
            "title": "Deborah Sitting under the Palm Tree",
            "author": "Julius Schnorr von Carolsfeld (Die Bibel in Bildern, 1860)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Classical biblical engraving depicting Judge Deborah holding court under her palm tree in Ephraim, dispensing divine wisdom and impartial justice to the gathered Israelites."
        },
        "youtube": {
            "youtube_id": "0B_5Fv4yXl4",
            "title": "BibleProject: Women in Biblical Narrative",
            "description": "Explores how God subverts patriarchal ancient Near Eastern cultural expectations by choosing, empowering, and calling women like Deborah to lead, prophesy, and save God's covenant people."
        },
        "svg_fn": get_svg_lesson2,
        "goals": [
            "Describe the political and military crisis in Israel during the 20-year oppression by King Jabin of Hazor and Sisera's 900 iron chariots.",
            "Analyze Deborah's fourfold identity as a Prophetess (*Nabi'ah*), Wife of Lappidoth, Judge (*Shophet*), and 'Mother in Israel' in Judges 4:1-5 and Judges 5:7.",
            "Evaluate the leadership model of Deborah's accessible palm court and implement active listening and impartiality in resolving peer conflicts."
        ],
        "intro": """In the ancient Near East, political, judicial, and military authority was almost exclusively concentrated in the hands of men. Kings and warlords built fortified stone palaces surrounded by heavily armed guards to isolate themselves from ordinary citizens.

Yet in Israel's darkest hour—under 20 years of brutal Canaanite terror—God broke cultural stereotypes by raising a remarkable woman: **Deborah**. Deborah did not rule from an intimidating ivory throne. She held open court under a palm tree in the hill country of Ephraim, welcoming anyone from any tribe seeking justice, counsel, and God's direction. Her wisdom, spiritual power, and accessible leadership transformed an entire nation.""",
        "core_scripture": """### Biblical Account: Deborah's Calling and Court

#### Judges 4:1-5 — Oppression and the Rise of Deborah
> *"Again the Israelites did evil in the eyes of the Lord, now that Ehud was dead. So the Lord sold them into the hands of Jabin king of Canaan, who reigned in Hazor. Sisera, the commander of his army, was based in Harosheth Haggoyim. Because he had nine hundred chariots fitted with iron and had cruelly oppressed the Israelites for twenty years, they cried to the Lord for help.*
> 
> *Now Deborah, a prophetess, the wife of Lappidoth, was leading Israel at that time. She held court under the Palm of Deborah between Ramah and Bethel in the hill country of Ephraim, and the Israelites went up to her to have their disputes decided."*""",
        "theological_pillars": """### Theological Exegesis: Divine Sovereignty and Deborah's Fourfold Identity

1. **Sovereignty over Cultural Patriarchy:** God is not constrained by human cultural biases. While ancient Near Eastern societies marginalized women from civic governance, God elevated Deborah to the supreme leadership office of Israel, demonstrating that spiritual authority depends on divine calling and moral integrity rather than gender.
2. **A Prophetess (*Nabi'ah*):** Deborah possessed direct prophetic communion with Yahweh. She did not formulate political strategy based on guesswork; she heard God's voice and communicated divine revelation with absolute accuracy and courage.
3. **The Wife of Lappidoth:** Scripture deliberately highlights her marriage, affirming that high public leadership and faithful family life are mutually supportive in God's kingdom. Her name and family roots grounded her ministry in relational integrity.
4. **Judge (*Shophet*) and Legal Arbiter:** She was Israel's highest judicial authority. In an era without centralized state courts, she adjudicated complex property disputes, family conflicts, and inter-tribal grievances based on the Torah.
5. **A 'Mother in Israel' (Judges 5:7):** Unlike tyrannical rulers who exploited citizens, Deborah loved her people with the fierce, protective, and nurturing care of a mother, restoring village safety and agricultural peace.""",
        "deep_dive": """### Deep Dive: The Significance of the Palm Court

Judges 4:5 emphasizes that Deborah sat *"under the Palm of Deborah between Ramah and Bethel in the hill country of Ephraim."* This geographical and practical detail holds profound pedagogical significance:

- **1. Accessibility and Transparency:** Unlike corrupt monarchs hidden behind palace gates, Deborah's open-air court under the palm tree was completely accessible to all twelve tribes, rich and poor alike.
- **2. Neutral and Central Location:** Situated between Ramah and Bethel in the territory of Ephraim, her palm court stood at a central crossroads of ancient Israel, making it convenient for disputants from both northern and southern tribes to reach her.
- **3. Incorruptibility:** Holding public hearings in broad daylight beneath a tree prevented secret bribery, backroom deals, and judicial extortion. Justice was seen, heard, and trusted by the entire community.
- **4. Moral and Spiritual Atmosphere:** The palm tree in biblical symbolism represents righteousness, flourishing, and fruitfulness (Psalm 92:12). Deborah's court stood as an oasis of righteous judgment in a spiritually barren land.""",
        "practical": {
            "title": "Action Framework: 4 Steps to Practicing 'Palm Tree' Accessible Leadership",
            "steps": [
                "Step 1: Cultivate Approachability — Make yourself available to classmates and team members without acting proud, arrogant, or dismissive because of your position.",
                "Step 2: Master Active Listening — Give full attention when peers share concerns; do not interrupt, pre-judge, or formulate arguments before understanding their perspective.",
                "Step 3: Render Impartial Decisions — Base your advice and choices on objective facts and fair rules rather than favoritism, friendship, or personal bias.",
                "Step 4: Speak with Gentle Boldness — Deliver truth clearly and respectfully, helping conflicting parties find peaceful reconciliation and mutual respect."
            ]
        },
        "kenyan_context": """In Kenya, women leaders have historically demonstrated exceptional courage, wisdom, and resilience, echoing the legacy of Judge Deborah. Leaders such as Mekatilili wa Menza (who led the Giriama resistance against colonial oppression), Professor Wangari Maathai (Nobel Peace Prize Laureate), and contemporary female judges, governors, and educators embody Deborah's traits of courage, environmental protection, accessible service, and unyielding defense of justice for the marginalized.""",
        "reflection": """### Spiritual Reflection: God's Calling Beyond Social Limits

In Galatians 3:28, the apostle Paul writes: *"There is neither Jew nor Gentile, neither slave nor free, nor is there male and female, for you are all one in Christ Jesus."*

- How does Deborah's appointment by God challenge harmful cultural beliefs that seek to limit the leadership potential of girls and women in our churches, schools, and homes?
- In what areas of your life can you create an 'accessible palm court' where friends feel safe to confide in you and receive wise, godly encouragement?""",
        "takeaways": [
            "Israel suffered 20 years of severe oppression under Canaanite King Jabin and army general Sisera, who commanded 900 iron chariots.",
            "God raised Deborah—a prophetess, wife of Lappidoth, judge, and mother in Israel—to deliver and guide the nation.",
            "Deborah held court publicly under a palm tree between Ramah and Bethel, providing accessible, transparent, and impartial justice.",
            "Deborah's leadership proves that God chooses and equips leaders based on faith, character, and obedience rather than gender.",
            "Christian leaders emulate Deborah by remaining approachable, listening attentively, and speaking God's uncompromised truth."
        ],
        "mcq": {
            "question": "Where did Judge Deborah hold court to decide the legal disputes of the Israelites?",
            "options": [
                "A) Inside the fortified royal palace of King Jabin in Hazor",
                "B) Under the Palm of Deborah between Ramah and Bethel in the hill country of Ephraim",
                "C) At the military garrison near the mouth of the Jordan River",
                "D) Inside the Tabernacle courtyard in Shiloh behind closed curtains"
            ],
            "answer": "B",
            "explanation": "Judges 4:5 records that Deborah held court publicly and accessibly under the Palm of Deborah between Ramah and Bethel in the hill country of Ephraim, where Israelites from all tribes went up to have their cases decided."
        }
    },

    # ───────────────────────────────────────────────────────────────────────────
    # LESSON 3
    # ───────────────────────────────────────────────────────────────────────────
    {
        "unit_order": 3,
        "unit_name": "The Battle of Mount Tabor and the Victory",
        "unit_description": "Analyze Deborah's command to Barak, Barak's hesitation, the mobilization of 10,000 men at Mount Tabor, the divine flood at Kishon River, and the fulfillment of Deborah's prophecy through Jael.",
        "lesson_title": "The Battle of Mount Tabor and the Victory",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/2/23/Foster_Bible_Pictures_0110-1_Barak_and_Deborah_Lead_the_Army.jpg",
            "title": "Barak and Deborah Lead the Army to Mount Tabor",
            "author": "Charles Foster (Foster Bible Pictures, 1897)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Historical illustration of General Barak and Judge Deborah mobilizing the 10,000 infantrymen of Naphtali and Zebulun to confront Sisera's 900 iron chariots at Mount Tabor."
        },
        "youtube": {
            "youtube_id": "kOYy8iCf648",
            "title": "BibleProject: The Epic Battle of Deborah and Barak",
            "description": "Explores the tactical and theological drama of Judges 4-5, demonstrating how God neutralized Sisera's 900 high-tech iron chariots in the mud of the Kishon River and delivered victory into the hands of Jael."
        },
        "svg_fn": get_svg_lesson3,
        "goals": [
            "Explain Deborah's prophetic command to Barak, the tactical significance of Mount Tabor, and the reason for Barak's hesitation in Judges 4:6-9.",
            "Analyze the battle dynamics at the Kishon River and explain how God routed Sisera's 900 iron chariots (Judges 4:10-16).",
            "Narrate how Jael defeated General Sisera in her tent, fulfilling Deborah's prophecy that the honor of the battle would belong to a woman (Judges 4:17-24)."
        ],
        "intro": """From a purely human perspective, the military contest between Israel and Canaan was entirely one-sided. On one side stood General Sisera, commanding 900 state-of-the-art iron chariots and a battle-hardened Canaanite army that had terrorized the region for two decades. On the other side stood 10,000 lightly armed Israelite foot soldiers gathered from the northern tribes of Naphtali and Zebulun.

Yet the battle of Mount Tabor reveals a fundamental spiritual truth: no military weapon, political superpower, or technological superiority can stand against the Almighty God when His people move forward in obedient faith. Through strategic mountain positioning, divine natural intervention, and the surprising courage of a woman named Jael, God utterly crushed Sisera's forces.""",
        "core_scripture": """### Biblical Narrative: The Battle and Deliverance

#### Judges 4:6-9 — The Summons, Hesitation, and Prophecy
> *"She sent for Barak son of Abinoam from Kedesh in Naphtali and said to him, 'The Lord, the God of Israel, commands you: "Go, take with you ten thousand men of Naphtali and Zebulun and lead them up to Mount Tabor. I will lead Sisera, the commander of Jabin’s army, with his chariots and his troops to the Kishon River and give him into your hands."'*
> 
> *Barak said to her, 'If you go with me, I will go; but if you don’t go with me, I won’t go.'*
> 
> *'Certainly I will go with you,' said Deborah. 'But because of the course you are taking, the honor will not be yours, for the Lord will deliver Sisera into the hands of a woman.' So Deborah went with Barak to Kedesh."*

#### Judges 4:14-15, 21 — The Clash and Jael's Courage
> *"Then Deborah said to Barak, 'Go! This is the day the Lord has given Sisera into your hands. Has not the Lord gone ahead of you?' So Barak went down Mount Tabor, with ten thousand men following him. At Barak’s advance, the Lord routed Sisera and all his chariots and army by the sword, and Sisera got down from his chariot and fled on foot...*
> 
> *But Jael, Heber’s wife, picked up a tent peg and a hammer and went quietly to him while he lay fast asleep, exhausted. She drove the peg through his temple into the ground, and he died."*""",
        "theological_pillars": """### Theological Exegesis: Divine Warfare, Faith, and Prophetic Fulfillment

1. **Strategic Mountain Positioning (Mount Tabor):** Mount Tabor rises steeply from the Jezreel plain. By stationing 10,000 infantry on the mountain slopes, Barak rendered Sisera's chariots useless on the rugged heights, forcing Sisera to deploy into the lowlands along the Kishon River.
2. **Barak's Hesitation and Shared Leadership:** Barak's refusal to advance without Deborah was not mere cowardice; it reflected his recognition that Deborah carried the tangible presence and prophetic guidance of God. However, because his faith required human reassurance, Deborah prophesied that the crowning glory of defeating Sisera would be transferred to a woman.
3. **God as Divine Warrior at Kishon River:** Judges 5:20-21 reveals that torrential storm rains caused the Kishon River to flash flood. Sisera's 900 heavy iron chariots sank into the thick mud, neutralizing the enemy's technological advantage. The Lord threw the Canaanite army into overwhelming panic (*hamam*).
4. **Jael and the Inversion of Power:** Sisera fled to the tent of Heber the Kenite, expecting sanctuary because of a political treaty between Jabin and the Kenites. Jael offered him hospitality, curdled milk, and a rug. While he slept exhausted, she used ordinary household tools—a wooden tent peg and a hammer—to execute the oppressor, fulfilling Deborah's exact prophecy.""",
        "deep_dive": """### Deep Dive: Chronological Sequence of the Tabor Campaign

- **1. Prophetic Directive:** Deborah commands Barak to mobilize 10,000 men from Naphtali and Zebulun at Mount Tabor.
- **2. The Hesitation & Prophecy:** Barak insists Deborah accompany him; Deborah agrees but prophesies that Sisera will fall to a woman.
- **3. Enemy Deployment:** Sisera marshals 900 iron chariots into the Jezreel Valley along the Kishon River to encircle Mount Tabor.
- **4. The Attack Command:** Deborah issues the divine battle cry: *"Go! This is the day the Lord has given Sisera into your hands. Has not the Lord gone ahead of you?"*
- **5. Flash Flood & Rout:** Barak charges down the mountain; torrential rains swell the Kishon River, trapping chariots in deep mud.
- **6. Sisera's Flight:** Sisera abandons his chariot and flees miles on foot toward the tent of Jael near Zaanannim.
- **7. Decisive Blow in the Tent:** Jael welcomes Sisera, provides milk, waits for deep sleep, and drives a tent peg through his temple.
- **8. Complete Deliverance:** Barak arrives in pursuit; Jael reveals the defeated general, breaking King Jabin's 20-year stranglehold.""",
        "practical": {
            "title": "Action Framework: 4 Steps to Overcoming Seemingly Impossible Challenges",
            "steps": [
                "Step 1: Trust God's Command Over Physical Odds — Do not let intimidation, difficult exams, or scarce resources paralyze you when doing the right thing.",
                "Step 2: Stand Sacrificially with Your Team — Like Deborah, do not send teammates into difficult tasks alone; lead by personal presence, encouragement, and shared effort.",
                "Step 3: Recognize and Utilize Available Gifts — Like Jael using a tent peg, realize that God can use your everyday talents, modest resources, and quiet diligence to achieve great victories.",
                "Step 4: Acknowledge God's Hand in Success — When you overcome obstacles, recognize that God went before you, guarding against arrogance and pride."
            ]
        },
        "kenyan_context": """In Kenyan history, many national struggles against immense odds required ordinary citizens and heroic women to step forward courageously. During Kenya's freedom struggle (Mau Mau), women such as Field Marshal Muthoni wa Kirima carried supplies, gathered crucial intelligence, and fought alongside men in the dense Aberdare forests. Their heroic actions mirror Jael and Deborah, proving that freedom and national triumph require bravery from all citizens regardless of traditional gender roles.""",
        "reflection": """### Spiritual Reflection: When the Lord Goes Ahead of You

In Judges 4:14, Deborah challenged Barak: *"Has not the Lord gone ahead of you?"*

- What 'iron chariots' (fears, financial hardship, academic anxiety, family problems) are currently intimidating you?
- How does the assurance that God goes before you give you the courage to take bold, righteous action today?""",
        "takeaways": [
            "God summoned Barak to lead 10,000 men from Naphtali and Zebulun to confront Sisera's 900 iron chariots at Mount Tabor.",
            "Because Barak refused to go without Deborah, Deborah prophesied that the crowning honor of defeating Sisera would go to a woman.",
            "God caused the Kishon River to swell, trapping the heavy iron chariots in mud and throwing the Canaanite army into total confusion.",
            "Sisera fled on foot to the tent of Jael, where she drove a tent peg through his temple while he slept, fulfilling Deborah's prophecy.",
            "God uses ordinary people, unexpected instruments, and divine circumstances to defeat proud oppressors and deliver His people."
        ],
        "mcq": {
            "question": "How was Judge Deborah's prophecy regarding the defeat of Sisera fulfilled in Judges 4:17-22?",
            "options": [
                "A) Barak struck down Sisera in hand-to-hand combat on the summit of Mount Tabor",
                "B) Jael, the wife of Heber the Kenite, drove a tent peg through Sisera's temple while he slept in her tent",
                "C) Deborah personally led a cavalry charge that captured Sisera at the Kishon River",
                "D) King Jabin surrendered Sisera in exchange for peace with the twelve tribes of Israel"
            ],
            "answer": "B",
            "explanation": "Judges 4:9 and 4:21 show that Deborah's prophecy ('the Lord will deliver Sisera into the hands of a woman') was fulfilled when Jael took a tent peg and hammer and struck down General Sisera in her tent."
        }
    },

    # ───────────────────────────────────────────────────────────────────────────
    # LESSON 4
    # ───────────────────────────────────────────────────────────────────────────
    {
        "unit_order": 4,
        "unit_name": "Leadership Traits of Deborah",
        "unit_description": "Analyze the seven core leadership qualities of Deborah (courage, wisdom, supportiveness, trustworthiness, directness, confidence in God, humility) and contrast them with secular models.",
        "lesson_title": "Leadership Traits of Deborah",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/c/c5/Foster_Bible_Pictures_0110-2_Deborah_Praising_God.jpg",
            "title": "Deborah Giving Praise and Glory to God",
            "author": "Charles Foster (Foster Bible Pictures, 1897)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Historical illustration of Judge Deborah humbly lifting her hands in worship, attributing Israel's national victory entirely to Yahweh's grace and divine power."
        },
        "youtube": {
            "youtube_id": "YbipxEDPryg",
            "title": "BibleProject: Character and Servant Leadership in Scripture",
            "description": "Explores the biblical definition of godly character and servant leadership, contrasting the world's desire for power and self-glorification with the biblical call to humility, justice, and faithfulness."
        },
        "svg_fn": get_svg_lesson4,
        "goals": [
            "Identify and analyze the seven core leadership traits demonstrated by Judge Deborah in Judges 4 and 5.",
            "Critically contrast Deborah's God-centered servant leadership with flawed secular and authoritarian leadership models.",
            "Formulate a personal leadership pledge to practice honesty, directness, and humility in school governance (prefects, clubs, teams)."
        ],
        "intro": """What makes a truly great leader? In our contemporary world, leadership is often associated with charisma, loud speeches, aggressive displays of power, expensive entourages, and the accumulation of personal wealth. Many leaders rule by fear, manipulate people through ethnic divisions, and quickly shift blame to others whenever a crisis occurs.

Scripture presents a radically different model in Judge Deborah. Deborah was powerful, yet deeply humble; decisive, yet a great listener; fiercely courageous, yet completely dependent on God. Her life offers an enduring masterclass in what it means to be a servant leader who transforms society without losing personal integrity.""",
        "core_scripture": """### Biblical Foundations: Deborah's Exemplary Character

#### Judges 4:8-9 — Courage, Directness, and Teamwork
> *"Barak said to her, 'If you go with me, I will go; but if you don’t go with me, I won’t go.'*
> *'Certainly I will go with you,' said Deborah. 'But because of the course you are taking, the honor will not be yours, for the Lord will deliver Sisera into the hands of a woman.' So Deborah went with Barak to Kedesh."*

#### Judges 5:7, 31 — The Mother in Israel and the Radiance of the Righteous
> *"Villagers in Israel would not fight; they held back until I, Deborah, arose, until I arose, a mother in Israel...*
> *So may all your enemies perish, Lord! But may all who love you be like the sun when it rises in its strength."*

#### Proverbs 3:5-6 — Trusting in the Sovereign Lord
> *"Trust in the Lord with all your heart and lean not on your own understanding; in all your ways submit to him, and he will make your paths straight."*""",
        "theological_pillars": """### Theological Exegesis: The 7 Pillars of Deborah's Leadership

1. **Courageous Bravery:** Deborah did not issue commands from the safety of an armchair. When Barak requested her presence, she willingly accompanied the army into the valley of battle, risking her own life for the liberation of Israel.
2. **Wisdom & Discernment:** She judged the people under her palm tree through patient listening, objective fact-finding, and deep alignment with God's law. Her wisdom united twelve fragmented, suspicious tribes.
3. **Supportive Empowerment:** She did not seek to monopolize military leadership. She recognized Barak's generalship, elevated him to command 10,000 soldiers, and stood by him as a supportive partner.
4. **Trustworthiness & Integrity:** Her impeccable moral track record earned the unwavering trust of tribal elders, soldiers, and citizens across ancient Israel.
5. **Direct & Truthful Communication:** Deborah did not flatter Barak or soften difficult truths to gain popularity. She told him directly that the honor would be given to a woman, delivering God's uncompromised word.
6. **Unshakable Confidence in God:** Her confidence was not rooted in chariots, numbers, or weapons, but in Yahweh's covenant promises. She declared with boldness: *"Has not the Lord gone ahead of you?"*
7. **Profound Humility:** When the war was won, Deborah did not build a monument to herself or demand a royal crown. She composed an inspired song that directed 100% of the praise, honor, and glory to God.""",
        "deep_dive": """### Deep Dive: Comparative Analysis of Leadership Models

| Dimension | Deborah's Biblical Servant Model | Flawed Secular / Authoritarian Model |
| :--- | :--- | :--- |
| **Source of Authority** | Divine calling, moral integrity, prayer | Coercion, military weapons, wealth, political patronage |
| **Accessibility** | Open palm tree court; approachable by all | Distant palaces, heavy security checkpoints, aloofness |
| **Communication** | Direct, honest, biblical, transparent | Manipulative, flattering, evasive, propaganda-driven |
| **Attitude to Team** | Empowers, shares roles, walks to battlelines | Exploits followers, micro-manages, takes all credit |
| **Handling Crisis** | Stands courageously at the front with faith | Flees, hides in bunkers, shifts blame to subordinates |
| **Post-Victory Response**| Sings praise to God; restores national rest | Demands monuments, crowns, tax exemptions, personal glory |
| **National Outcome** | 40 years of peace, unity, and flourishing | Social unrest, tribal divisions, economic ruin, collapse |""",
        "practical": {
            "title": "Action Framework: 4 Steps to Cultivating Deborah's Traits as a Student Leader",
            "steps": [
                "Step 1: Lead with Moral Courage — Stand up for students being bullied, speak against cheating, and defend truth even when it makes you unpopular with peer groups.",
                "Step 2: Communicate Truth Directly and Kindly — As a prefect or class monitor, do not cover up indiscipline for friends or falsely accuse rivals; report and advise with objective honesty.",
                "Step 3: Practice Supportive Delegation — In group assignments and club projects, assign roles according to members' strengths and work alongside them rather than merely bossing them around.",
                "Step 4: Redirect Praise to God and Your Team — When your class or sports team excels, celebrate collective effort and give thanks to God rather than boasting about your own abilities."
            ]
        },
        "kenyan_context": """In Kenya, Chapter Six of the Constitution outlines the core values of Leadership and Integrity for all public officers. These constitutional values—such as selfless service, objectivity in decision-making, honesty, accountability, and discipline—closely mirror the seven leadership qualities of Deborah. Kenyan secondary school student councils and prefect systems are designed to train young people in these very principles, ensuring they grow into corrupt-free national leaders.""",
        "reflection": """### Spiritual Reflection: Examining Our Motives for Leadership

In Mark 10:42-45, Jesus taught: *"Whoever wants to become great among you must be your servant, and whoever wants to be first must be slave of all."*

- When you seek a leadership role in school, church, or clubs, is your underlying desire to serve others or to gain prestige, recognition, and power?
- Which of Deborah's seven traits (courage, wisdom, supportiveness, trustworthiness, directness, confidence in God, humility) do you need God to strengthen in your life today?""",
        "takeaways": [
            "Deborah modeled seven essential leadership traits: courage, wisdom, supportiveness, trustworthiness, directness, confidence in God, and humility.",
            "Unlike worldly rulers who dominate through fear, Deborah practiced servant leadership rooted in accessibility, active listening, and empowerment.",
            "Deborah demonstrated directness by speaking God's unvarnished truth to Barak without flattery or fear.",
            "Humility was Deborah's crowning virtue: after the victory at Mount Tabor, she attributed all glory and praise to God in song.",
            "Christian youth are called to lead with integrity, reject tribalism and corruption, and serve their schools and communities selflessly."
        ],
        "mcq": {
            "question": "Why is Judge Deborah regarded as an outstanding model of humble, God-fearing leadership?",
            "options": [
                "A) Because she resigned from judging Israel immediately after Barak mobilized the army",
                "B) Because she refused to take personal glory for the victory, attributing all praise and honor to God through a song of thanksgiving",
                "C) Because she built a massive palace in Hazor to house the spoils of war",
                "D) Because she ordered Barak to pay her tribute from the captured iron chariots"
            ],
            "answer": "B",
            "explanation": "Judges 5 demonstrates Deborah's profound humility: rather than demanding royal titles or personal monuments after defeating Sisera, she composed a victory hymn that attributed the deliverance entirely to God."
        }
    },

    # ───────────────────────────────────────────────────────────────────────────
    # LESSON 5
    # ───────────────────────────────────────────────────────────────────────────
    {
        "unit_order": 5,
        "unit_name": "Lessons from the Song of Deborah and Barak",
        "unit_description": "Examine the theological, historical, and ethical lessons of the Song of Deborah (Judges 5), including the danger of complacency, swift gratitude, and the commendation/rebuke of tribal participation.",
        "lesson_title": "Lessons from the Song of Deborah and Barak",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Foster_Bible_Pictures_0111-1_Deborah_and_Barak_Sing_a_Song_of_Praise.jpg",
            "title": "Deborah and Barak Sing a Song of Praise",
            "author": "Charles Foster (Foster Bible Pictures, 1897)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Historical illustration of Judge Deborah and General Barak standing before the assembled tribes of Israel, playing stringed instruments and singing their victory hymn to Yahweh."
        },
        "youtube": {
            "youtube_id": "YbipxEDPryg",
            "title": "BibleProject: Psalms and Songs of the Bible",
            "description": "Explores the ancient Hebrew poetry and victory songs of Scripture, showing how songs like Exodus 15 and Judges 5 preserve historical memory, renew the covenant, and direct the nation's heart toward God."
        },
        "svg_fn": get_svg_lesson5,
        "goals": [
            "Explain the theological purpose and historical context of the Song of Deborah and Barak in Judges 5:1-31.",
            "Analyze the warning against complacency in Judges 5:6-8 and evaluate the ethical necessity of swift, heartfelt gratitude to God.",
            "Contrast the commended tribes (Zebulun, Naphtali, Ephraim) with the rebuked idle tribes (Reuben, Dan, Asher) regarding community and civic participation."
        ],
        "intro": """When a major victory is won or a national crisis is resolved, what is the first thing people do? Often, celebrations turn into self-congratulatory parties where human leaders brag about their strategic brilliance, military prowess, or intellectual strength.

Deborah and Barak took an entirely different path. On the very day of their astonishing victory over Sisera, they composed and sang one of the oldest, most magnificent poetic anthems in human literature: **The Song of Deborah** (Judges 5). This victory hymn was not just art; it was a profound theological document designed to prevent national pride, warn against spiritual complacency, and summon all tribes to active civic duty.""",
        "core_scripture": """### Biblical Text: The Song of Praise and Remembrance

#### Judges 5:1-3, 6-8 — Immediate Praise and the Memory of Decay
> *"On that day Deborah and Barak son of Abinoam sang this song:*
> *'When the princes in Israel take the lead, when the people willingly offer themselves—praise the Lord! Hear this, you kings! Listen, you rulers! I, even I, will sing to the Lord; I will praise the Lord, the God of Israel, in song...*
> 
> *In the days of Shamgar son of Anath, in the days of Jael, the highways were abandoned; travelers took to winding paths. Villagers in Israel would not fight; they held back until I, Deborah, arose, until I arose, a mother in Israel. God chose new gods when war came to the city gates, but not a shield or spear was seen among forty thousand in Israel.'"*

#### Judges 5:15-18, 31 — The Contrast of Tribes and the Closing Benediction
> *"In the districts of Reuben there was much searching of heart. Why did you stay among the sheep pens to hear the whistling for the flocks? In the districts of Reuben there was much searching of heart... Dan, why did he linger by the ships? Asher remained on the coast and stayed in his coves.*
> *The people of Zebulun risked their very lives; so did Naphtali on the terraced heights...*
> 
> *So may all your enemies perish, Lord! But may all who love you be like the sun when it rises in its strength.' Then the land had peace forty years."*""",
        "theological_pillars": """### Theological Exegesis: Three Enduring Lessons of the Song

1. **Prosperity Must Never Lead to Complacency (Judges 5:6-8):**
   - The song graphically recounts the dark days before Deborah: highways were deserted due to Canaanite bandits, trade ground to a halt, and agricultural villages were abandoned.
   - Why did this occur? Because Israel *"chose new gods."* They took God's blessings for granted, indulged in pagan idolatry, and became defenseless.
   - *Theological Principle:* Complacency is the silent killer of faith. When believers enjoy ease, comfort, and good grades, they must guard against forgetting God.
2. **God Deserves Immediate, Swift Gratitude (Judges 5:1-3):**
   - Deborah and Barak did not delay thanksgiving. They sang *"on that day,"* publicly proclaiming that the victory at Kishon River was wrought by Yahweh.
   - *Theological Principle:* Delayed gratitude often turns into self-glory. Swift worship roots our achievements in humble dependence on God.
3. **Civic Duty: Commending the Willing vs. Condemning the Idle (Judges 5:14-18):**
   - **Commended Tribes:** Zebulun, Naphtali, Ephraim, Benjamin, and Issachar risked their lives on the terraced heights for the common good of Israel.
   - **Rebuked Tribes:** Reuben sat leisurely listening to sheep whistles; Gilead stayed across the Jordan; Dan stayed with commercial ships; Asher remained safe on the sea coast.
   - *Ethical Principle:* When a community, school, or nation faces a crisis, selfish neutrality and refusal to assist is a grave moral failure.""",
        "deep_dive": """### Deep Dive: Poetic Structure and Themes in Judges 5

The Song of Deborah is structured into vivid poetic movements:

- **Movement 1: The Call to Worship (vv. 1-5):** Deborah summons world kings and princes to hear her praise Yahweh, recounting how the earth shook when God marched from Mount Seir.
- **Movement 2: The Plight of Israel (vv. 6-9):** Vivid depiction of ruined highways, fear, idolatry, and the defenseless state of Israel until Deborah arose as a mother in Israel.
- **Movement 3: The Tribal Roll Call (vv. 12-18):** A transparent review of who volunteered and who shirked their civic duty when the nation called.
- **Movement 4: Cosmic Battle and Natural Intervention (vv. 19-23):** Depicts the kings of Canaan fighting at Taanach, the stars from heaven fighting against Sisera, and the ancient river Kishon sweeping them away.
- **Movement 5: Jael's Heroic Act vs. Sisera's Mother (vv. 24-30):** Dramatic contrast between Jael's courageous deed and Sisera's aristocratic mother vainly waiting at the palace window for her son's return with spoils.
- **Movement 6: Triumphant Doxology (v. 31):** A prophetic prayer that all God's enemies perish and all who love Him shine like the rising morning sun, inaugurating 40 years of peace.""",
        "practical": {
            "title": "Action Framework: 4 Steps to Practicing Sincere Gratitude & Active Participation",
            "steps": [
                "Step 1: Offer Immediate Thanks — When you succeed in exams, sports, or music, say a prompt prayer of thanksgiving and write or express heartfelt appreciation to parents and teachers.",
                "Step 2: Guard Against Complacency — Do not relax your discipline or study habits after one good score; treat past success as a platform for deeper commitment and diligence.",
                "Step 3: Answer Community Calls to Action — In school clean-up days, tree planting, charity drives, or choir rehearsals, be like Zebulun and volunteer enthusiastically rather than staying idle.",
                "Step 4: Resist Selfish Indifference — Reject the 'Reuben mindset' of watching from the sidelines while others do the hard work; take personal ownership of group responsibilities."
            ]
        },
        "kenyan_context": """In Kenya, the spirit of *Harambee* ('Let us pull together') and *Utumishi kwa Wote* reflects the core message of the Song of Deborah. When national challenges arise—such as environmental conservation, disaster relief, or building community schools—citizens who contribute their time and resources embody the commended tribes of Naphtali and Zebulun. Conversely, those who hoard wealth and refuse to assist neighbors in need represent the rebuked complacency of Reuben and Dan.""",
        "reflection": """### Spiritual Reflection: Are You Lingering by the Sheep Pens?

Judges 5:16 asks: *"Why did you stay among the sheep pens to hear the whistling for the flocks?"*

- In your school, church, or family, are you actively participating in collective responsibilities, or are you lingering on the sidelines enjoying personal comfort while others struggle?
- How does singing songs of praise and expressing gratitude to God protect your heart from spiritual pride and selfishness?""",
        "takeaways": [
            "The Song of Deborah (Judges 5) is an ancient victory hymn sung immediately after the battle of Mount Tabor to give all praise to Yahweh.",
            "Judges 5:6-8 warns that past prosperity led Israel to complacency, idolatry, abandoned highways, and total vulnerability.",
            "Swift gratitude prevents human pride by acknowledging that all deliverance, wisdom, and success originate from God.",
            "The song commends tribes that willingly risked their lives (Zebulun, Naphtali) and rebukes tribes that remained idle in comfort (Reuben, Dan, Asher).",
            "The song concludes with a prayer for righteousness and inaugurates a 40-year era of national peace and rest."
        ],
        "mcq": {
            "question": "In the Song of Deborah (Judges 5:15-17), why were the tribes of Reuben, Dan, and Asher rebuked?",
            "options": [
                "A) Because they allied militarily with King Jabin of Hazor",
                "B) Because they stayed comfortably at home attending to their sheep and ships instead of helping their sister tribes in the national struggle",
                "C) Because they composed a rival song of praise to Baal",
                "D) Because they refused to let Deborah judge cases under her palm tree"
            ],
            "answer": "B",
            "explanation": "Judges 5:15-17 rebukes Reuben, Dan, and Asher for their selfish complacency and refusal to join Barak's army, choosing instead to linger leisurely among their sheepfolds and coastal ships while their fellow Israelites risked their lives."
        }
    },

    # ───────────────────────────────────────────────────────────────────────────
    # LESSON 6
    # ───────────────────────────────────────────────────────────────────────────
    {
        "unit_order": 6,
        "unit_name": "Applying Deborah's Leadership Today",
        "unit_description": "Synthesize the ethical, spiritual, and civic lessons of Deborah's leadership and apply them to 21st-century Kenyan society, gender equity, student governance, anti-corruption, and church ministry.",
        "lesson_title": "Applying Deborah's Leadership Today",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Foster_Bible_Pictures_0111-2_Israel_at_Rest.jpg",
            "title": "Israel at Rest and Peace under Righteous Governance",
            "author": "Charles Foster (Foster Bible Pictures, 1897)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Historical illustration showing the land of Israel enjoying forty years of peaceful agricultural rest, safety, and community flourishing following Deborah's godly leadership."
        },
        "youtube": {
            "youtube_id": "3bhk_4qLhSA",
            "title": "BibleProject: Justice and Righteousness in Society",
            "description": "Explores the rich biblical concepts of Mishpat (justice) and Tzedakah (righteousness), showing how God's people are called to advocate for the vulnerable, uphold integrity, and lead with equitable servant hearts."
        },
        "svg_fn": get_svg_lesson6,
        "goals": [
            "Analyze how the four pillars of 'Palm Tree Leadership' (gender equity, accessibility, collaborative teamwork, and integrity) apply to modern school and civic governance.",
            "Evaluate scriptural passages (Romans 12:4-8, Galatians 3:28, 1 Timothy 4:12) supporting equal leadership opportunities for young women and men in church and society.",
            "Develop a concrete, personal leadership action plan to oppose tribalism, electoral bribery, and corruption in school prefect elections and community life."
        ],
        "intro": """Does an ancient story from the hills of Ephraim 3,000 years ago still matter to a Grade 9 student in Kenya today? The answer is an emphatic YES!

Our contemporary world faces deep leadership crises: widespread corruption, abuse of power, gender discrimination, youth disillusionment, and toxic political tribalism. Judge Deborah's life provides a timeless, revolutionary blueprint for ethical leadership. By embracing her model of **'Palm Tree Leadership'**—combining spiritual devotion, transparent accessibility, collaborative teamwork, and fearless moral courage—young Christians can transform their schools, communities, and nation.""",
        "core_scripture": """### Biblical Foundations: Christian Leadership in Contemporary Life

#### Galatians 3:28 — Equality and Dignity in Christ Jesus
> *"There is neither Jew nor Gentile, neither slave nor free, nor is there male and female, for you are all one in Christ Jesus."*

#### Romans 12:4-8 — Diverse Gifts Working in Mutual Harmony
> *"For just as each of us has one body with many members, and these members do not all have the same function, so in Christ we, though many, form one body, and each member belongs to all the others. We have different gifts, according to the grace given to each of us. If your gift is prophesying, then prophesy in accordance with your faith; if it is serving, then serve; if it is teaching, then teach; if it is to encourage, then give encouragement; if it is giving, then give generously; if it is to lead, do it diligently; if it is to show mercy, do it cheerfully."*

#### 1 Timothy 4:12 — Youthful Leadership and Integrity
> *"Don’t let anyone look down on you because you are young, but set an example for the believers in speech, in conduct, in love, in faith and in purity."*""",
        "theological_pillars": """### Theological Exegesis: The 4 Contemporary Pillars of Palm Tree Leadership

1. **Gender Equity and Empowerment in God's Kingdom:**
   - In Christ and in God's creation order, leadership is defined by spiritual gifting, moral character, and divine calling rather than gender (Galatians 3:28).
   - Christian communities must actively dismantle cultural stereotypes, support female students in science, governance, and theology, and respect women in civic and ecclesiastical leadership.
2. **The Palm Tree Principle: Approachability and Servant Ministry:**
   - Deborah sat under an open palm tree, refusing aloofness and private isolation. Modern student leaders, teachers, and public officers must be accessible, practicing open-door policies and empathetic listening.
   - Leadership is not a badge of privilege; it is a sacred responsibility to serve (*diakonia*).
3. **Collaborative Partnership (The Deborah-Barak Model):**
   - Deborah did not succumb to rivalry or insecurity. She partnered effectively with Barak, recognizing that diverse members form one cohesive body (Romans 12:4-8).
   - Effective leadership values teamwork, delegates responsibility, and avoids autocratic micromanagement.
4. **Fearless Integrity and Anti-Corruption:**
   - Deborah spoke uncompromised truth and judged without accepting bribes. Christian youth are called to reject academic cheating, tribalism in school elections, and bribery in all forms.""",
        "deep_dive": """### Deep Dive: Applying Deborah's Leadership across Four Spheres

- **1. In the School Environment:**
  - **Student Councils & Prefects:** Run for leadership positions based on clear vision and a heart to serve rather than buying sweets or making false promises.
  - **Peer Dispute Resolution:** Mediate quarrels among classmates impartially without taking sides based on friendships or ethnicity.
  - **Anti-Bullying Advocacy:** Stand up for younger or vulnerable students who are harassed by bullies.
- **2. In the Family and Peer Group:**
  - **Domestic Responsibility:** Balance academic work, spiritual devotion, and household chores just as Deborah balanced family life and national duty.
  - **Mentorship:** Encourage younger siblings and friends to develop self-confidence, good study habits, and strong moral character.
- **3. In the Church and Faith Community:**
  - **Active Ministry:** Participate in youth praise teams, scripture reading, ushering, and community outreach.
  - **Affirming All Callings:** Welcome girls and boys equally into ministry leadership roles based on spiritual gifts.
- **4. In Kenyan National and Civic Life:**
  - **Promoting National Unity:** Reject negative ethnicity and tribal stereotypes; celebrate Kenya's rich cultural diversity.
  - **Environmental Stewardship:** Like Wangari Maathai and Deborah under the palm tree, protect Kenya's forests, water towers, and natural resources.""",
        "practical": {
            "title": "Action Framework: 4 Steps to Implementing 'Palm Tree Leadership' in Your School",
            "steps": [
                "Step 1: Conduct an Integrity Audit — Assess your daily speech, honesty in homework, and interactions with peers; eliminate gossip, cheating, and favoritism.",
                "Step 2: Create Safe Spaces for Dialogue — Be an accessible friend who listens patiently to troubled peers without mocking or breaking their confidentiality.",
                "Step 3: Partner Across Gender and Ethnic Lines — In group assignments and club projects, intentionally choose teammates from different backgrounds and support female leadership.",
                "Step 4: Vote Based on Character, Not Bribes — In prefect or club elections, reject candidates who offer bribes, flattery, or appeal to tribalism; vote for candidates with proven integrity."
            ]
        },
        "kenyan_context": """In Kenya today, the national ethos of *Integrity, Inclusivity, and Social Justice* is anchored in Article 10 of the Constitution. Young Kenyans who draw inspiration from Judge Deborah can lead transformative campaigns in their counties—championing girls' education in pastoralist communities, fighting against gender-based violence (GBV), promoting peaceful co-existence during elections, and demonstrating that integrity is the true cornerstone of sustainable national prosperity.""",
        "reflection": """### Spiritual Reflection: Setting an Example in Speech and Conduct

In 1 Timothy 4:12, Paul writes: *"Don’t let anyone look down on you because you are young, but set an example for the believers in speech, in conduct, in love, in faith and in purity."*

- What specific practical steps will you take this week to be an accessible, courage-filled leader like Deborah in your classroom or home?
- How will you use your God-given voice to stand up for justice, honesty, and kindness when those around you are choosing corruption or indifference?""",
        "takeaways": [
            "Deborah's legacy provides four enduring pillars for modern leadership: gender equity, accessible service, collaborative partnership, and uncompromising integrity.",
            "Scripture teaches that God calls and empowers both women and men based on character, faith, and spiritual gifts (Galatians 3:28, Romans 12:4-8).",
            "Palm Tree Leadership means remaining approachable, practicing active listening, and serving others rather than pursuing power and privilege.",
            "Christian student leaders reject electoral bribery, negative ethnicity, and bullying, choosing instead to lead with moral courage.",
            "Young believers are called to set a godly example in speech, conduct, love, faith, and purity in their schools, churches, and nation."
        ],
        "mcq": {
            "question": "What is the primary lesson that modern student leaders in Kenya can learn from Deborah's 'Palm Tree' leadership model?",
            "options": [
                "A) Leaders should isolate themselves in private offices to maintain an aura of mystery and power",
                "B) True leadership is accessible, listens patiently to the community, and administers justice with impartiality and integrity",
                "C) Only military commanders should make important school and community decisions",
                "D) Leaders should reward their closest friends and punish their rivals during disputes"
            ],
            "answer": "B",
            "explanation": "Deborah's palm court demonstrates that godly leadership is accessible, transparent, and built on patient listening, wise counsel, and impartial justice rather than aloofness, corruption, or favoritism."
        }
    }
]


# ─── INGESTION RUNNER ─────────────────────────────────────────────────────────

def ingest_grade9_cre_topic3():
    print("=" * 80)
    print("INGESTING GRADE 9 CRE — TOPIC 3: JUDGE DEBORAH (ALL 6 LESSONS)")
    print("=" * 80)

    with transaction.atomic():
        # Grade 9 (ID: 18), Subject: CRE (ID: 50)
        grade = Grade.objects.get(id=18)
        subject = Subject.objects.get(id=50, grade=grade)

        # Ensure Topic 3: Judge Deborah exists under Subject 50
        topic, created_topic = Topic.objects.get_or_create(
            subject=subject,
            order=3,
            defaults={
                "name": "Judge Deborah",
                "description": "Explores the leadership of Judge Deborah, the political and religious context of the era of Judges, the battle of Mount Tabor, her unique qualities, the Song of Deborah, and modern leadership applications."
            }
        )
        if created_topic:
            print(f"[+] Created Topic 3: '{topic.name}' (ID: {topic.id}) under Subject {subject.name}")
        else:
            print(f"[*] Found existing Topic 3: '{topic.name}' (ID: {topic.id})")
            topic.name = "Judge Deborah"
            topic.description = "Explores the leadership of Judge Deborah, the political and religious context of the era of Judges, the battle of Mount Tabor, her unique qualities, the Song of Deborah, and modern leadership applications."
            topic.save()

        print(f"Target Curriculum: {grade.curriculum.name}")
        print(f"Target Grade     : {grade.name} (ID: {grade.id})")
        print(f"Target Subject   : {subject.name} (ID: {subject.id})")
        print(f"Target Topic     : {topic.name} (ID: {topic.id}, Order: {topic.order})")
        print("-" * 80)

        total_lessons_created = 0
        total_blocks_created = 0
        total_assets_created = 0

        for cfg in LESSONS_DATA:
            u_order = cfg["unit_order"]
            u_name = cfg["unit_name"]
            l_title = cfg["lesson_title"]

            print(f"\n>>> Processing Lesson {u_order}: '{l_title}'")

            # Clean existing Unit in Topic 3 if present
            existing_units = LearningUnit.objects.filter(topic=topic, order=u_order)
            if existing_units.exists():
                for eu in existing_units:
                    print(f"[*] Removing existing LearningUnit order={u_order} (ID: {eu.id})")
                    eu.delete()

            # 1. Create LearningUnit
            unit = LearningUnit.objects.create(
                topic=topic,
                order=u_order,
                name=u_name,
                description=clean_text(cfg["unit_description"])
            )
            print(f"[+] Created LearningUnit ID: {unit.id} ('{unit.name}', order={unit.order})")

            # 2. Create Published Lesson
            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=clean_text(l_title),
                status="published",
                version=1,
                immutable_metadata={
                    "grade": "Grade 9",
                    "subject": "CRE",
                    "topic_order": 3,
                    "topic_name": topic.name,
                    "unit_order": u_order,
                    "author": "VLearn Grade 9 CRE Ingestion Engine",
                    "curriculum_framework": "CBC Kenya",
                    "enrichment_version": "v3_pedagogical"
                }
            )
            print(f"[+] Created Lesson ID: {lesson.id} ('{lesson.title}', status={lesson.status})")
            total_lessons_created += 1

            # 3. Create LessonAssets (3 Assets)
            # Asset 1: Image Visual Hook
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
                    "author": img_info["author"],
                    "licensing": img_info["licensing"],
                    "source": img_info["source"],
                    "caption": clean_text(img_info["caption"])
                }
            )

            # Asset 2: Responsive SVG Diagram
            svg_content = cfg["svg_fn"]()
            svg_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="ai_generated",
                storage_type="url",
                status="attached",
                title=f"Diagram: {l_title}",
                description=f"Responsive pedagogical vector SVG diagram illustrating {l_title}.",
                url=f"https://vlearn.africa/assets/diagrams/cre/grade9_topic_3_lesson_{u_order}.svg",
                metadata={
                    "svg_xml": svg_content,
                    "viewBox": "0 0 800 450",
                    "theme": "#0f172a"
                }
            )

            # Asset 3: Curated Educational YouTube Video
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
            print(f"[+] Attached 3 LessonAssets (Image, SVG Diagram, YouTube Video)")

            # 4. Create 6 Pages / Cards with LessonBlocks (13 Blocks total)

            # ───────────────────────────────────────────────────────────────────
            # CARD 1 (Page 1): Discovery & Objectives (3 blocks)
            # ───────────────────────────────────────────────────────────────────
            b1 = LessonBlock.objects.create(
                lesson=lesson, page_number=1, page_title="Discovery & Objectives",
                order=10, component_order=1,
                block_type="suggested_image", component_type="suggested_image",
                title=clean_text(img_info["title"]),
                content={
                    "title": clean_text(img_info["title"]),
                    "url": img_info["url"],
                    "resolved_image_url": img_info["url"],
                    "caption": clean_text(img_info["caption"]),
                    "author": img_info["author"],
                    "licensing": img_info["licensing"],
                    "source": img_info["source"]
                }
            )
            b1.assets.add(img_asset)

            LessonBlock.objects.create(
                lesson=lesson, page_number=1, page_title="Discovery & Objectives",
                order=20, component_order=2,
                block_type="learning_goal", component_type="learning_goal",
                title="Lesson Objectives",
                content={"goals": clean_dict(cfg["goals"])}
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=1, page_title="Discovery & Objectives",
                order=30, component_order=3,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Introduction & Historical Context",
                content={"markdown": clean_text(cfg["intro"])}
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 2 (Page 2): Scriptural Exegesis (2 blocks)
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
                order=40, component_order=1,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Core Biblical Foundations",
                content={"markdown": clean_text(cfg["core_scripture"])}
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
                order=45, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Theological Exegesis & Analysis",
                content={"markdown": clean_text(cfg["theological_pillars"])}
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 3 (Page 3): Pedagogical Diagram & Deep Dive (2 blocks)
            # ───────────────────────────────────────────────────────────────────
            b5 = LessonBlock.objects.create(
                lesson=lesson, page_number=3, page_title="Pedagogical Diagram & Deep Dive",
                order=50, component_order=1,
                block_type="suggested_diagram", component_type="suggested_diagram",
                title=f"Diagram: {l_title}",
                content={
                    "title": f"Diagram: {l_title}",
                    "caption": f"Responsive pedagogical vector SVG diagram illustrating {l_title}.",
                    "svg": svg_content,
                    "svg_xml": svg_content
                }
            )
            b5.assets.add(svg_asset)

            LessonBlock.objects.create(
                lesson=lesson, page_number=3, page_title="Pedagogical Diagram & Deep Dive",
                order=60, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Deep Dive: Advanced Analysis",
                content={"markdown": clean_text(cfg["deep_dive"])}
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 4 (Page 4): Practical Application & Context (2 blocks)
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=4, page_title="Practical Application & Context",
                order=70, component_order=1,
                block_type="step_process", component_type="step_process",
                title=clean_text(cfg["practical"]["title"]),
                content=clean_dict(cfg["practical"])
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=4, page_title="Practical Application & Context",
                order=75, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Kenyan Real-World Context & Contemporary Leadership",
                content={"markdown": clean_text(cfg["kenyan_context"])}
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 5 (Page 5): Multimedia & Reflection (2 blocks)
            # ───────────────────────────────────────────────────────────────────
            b8 = LessonBlock.objects.create(
                lesson=lesson, page_number=5, page_title="Multimedia & Reflection",
                order=80, component_order=1,
                block_type="suggested_video", component_type="suggested_video",
                title=clean_text(yt_info["title"]),
                content={
                    "title": clean_text(yt_info["title"]),
                    "url": f"https://www.youtube.com/watch?v={yt_info['youtube_id']}",
                    "youtube_id": yt_info["youtube_id"],
                    "description": clean_text(yt_info["description"])
                }
            )
            b8.assets.add(yt_asset)

            LessonBlock.objects.create(
                lesson=lesson, page_number=5, page_title="Multimedia & Reflection",
                order=90, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Spiritual Reflection & Moral Discernment",
                content={"markdown": clean_text(cfg["reflection"])}
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 6 (Page 6): Mastery Check & Key Takeaways (2 blocks)
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=6, page_title="Mastery Check",
                order=100, component_order=1,
                block_type="summary", component_type="summary",
                title="Summary & Core Principles",
                content={
                    "title": f"Key Takeaways: {l_title}",
                    "takeaways": clean_dict(cfg["takeaways"])
                }
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=6, page_title="Mastery Check",
                order=110, component_order=2,
                block_type="knowledge_check", component_type="knowledge_check",
                title="Mastery Assessment",
                content=clean_dict(cfg["mcq"])
            )

            blocks_count = lesson.blocks.count()
            total_blocks_created += blocks_count
            print(f"[+] Created 6 Pages (13 Blocks total, actual count: {blocks_count})")

        print("\n" + "=" * 80)
        print("TOPIC 3 INGESTION SUMMARY:")
        print(f"  - Subject           : {subject.name} (ID: {subject.id})")
        print(f"  - Topic             : {topic.name} (ID: {topic.id}, Order: {topic.order})")
        print(f"  - Total Units       : {topic.learning_units.count()}")
        print(f"  - Total Lessons     : {total_lessons_created}")
        print(f"  - Total Blocks      : {total_blocks_created}")
        print(f"  - Total Assets      : {total_assets_created}")
        print("=" * 80)


if __name__ == "__main__":
    ingest_grade9_cre_topic3()
