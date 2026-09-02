"""
VLearn CBC Grade 9 CRE — Topic 15: Leisure
Production-Ready Ingestion & Visual Enrichment Engine

Curriculum: CBC
Grade: Grade 9 (ID: 18)
Subject: CRE (ID: 50)
Topic: Topic 15: Leisure (Order: 15)

6 Discrete Units / Published Lessons:
  1. Lesson 1: Meaning and Forms of Leisure (Genesis 2:1-3, Mark 6:31)
  2. Lesson 2: Importance, Proper Use and Misuse of Leisure (1 Corinthians 10:23, 31)
  3. Lesson 3: Understanding Drug and Substance Abuse (1 Corinthians 6:19-20, Proverbs 20:1)
  4. Lesson 4: Soft Drugs vs. Hard Drugs: Side Effects and Consequences (Alcohol, Tobacco, Miraa, Cannabis, Heroin, Cocaine)
  5. Lesson 5: Causes and Remedies of Drug Abuse (NACADA, Rehabilitation, Peer pressure resistance)
  6. Lesson 6: Christian Criteria for Evaluating Leisure (Philippians 4:8, Romans 12:1-2)

Every Lesson contains:
  - 6 Cards / Pages (Discovery & Objectives, Scriptural Exegesis, Pedagogical Diagram, Practical Application, Multimedia & Reflection, Mastery Check)
  - 13 Blocks (standardized block_types: suggested_image, learning_goal, concept_explanation, suggested_diagram, step_process, suggested_video, summary, knowledge_check)
  - 3 Assets (LessonAsset objects: Image, Diagram, YouTube)
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
    """Removes bracket citations and internal meta tags."""
    if not text:
        return ""
    # Strip bracket citations e.g. [1], [223], [1, 2], [72, 238], [313, 318, 323]
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Strip internal pedagogical tags
    text = re.sub(r'\[(VISUAL|BIBLE PASSAGE|BIBLE REFERENCE|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|REAL WORLD APPLICATION|BIBLICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|REFLECTION|BIBLE VERSE|RECALL|COMPREHENSION|APPLICATION)[^\]]*\]', '', text, flags=re.IGNORECASE)
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


# ─── 6 CUSTOM RESPONSIVE VECTOR SVGS (viewBox="0 0 800 450", #0f172a theme) ─────

def get_svg_lesson_1():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="cyanGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#38bdf8"/>
    </linearGradient>
    <linearGradient id="greenGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#34d399"/>
    </linearGradient>
    <linearGradient id="purpleGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#a855f7"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg1)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE ANATOMY OF LEISURE: ACTIVE VS. PASSIVE FORMS</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Genesis 2:1-3 &amp; Mark 6:31 — God's Design for Rest, Renewal, and Balanced Living</text>

  <!-- Top Hub: Definition of Leisure -->
  <rect x="250" y="88" width="300" height="52" rx="10" fill="url(#cyanGrad1)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="400" y="110" fill="#0f172a" font-family="system-ui, sans-serif" font-size="13.5" font-weight="800" text-anchor="middle">LEISURE (TIME AT ONE'S DISPOSAL)</text>
  <text x="400" y="128" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Free from compulsory work, chores, and school duties</text>

  <!-- Connecting Lines -->
  <line x1="330" y1="140" x2="220" y2="175" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>
  <line x1="470" y1="140" x2="580" y2="175" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>

  <!-- Left Column: Active Leisure -->
  <g transform="translate(45, 175)">
    <rect width="335" height="205" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="335" height="34" rx="10" fill="url(#greenGrad1)"/>
    <text x="167" y="22" fill="#0f172a" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">ACTIVE LEISURE (PHYSICAL MOVEMENT)</text>
    <text x="15" y="58" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• High Energy &amp; Physical Exertion</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Involves muscular movement and bodily coordination.</text>
    <text x="15" y="102" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Key Examples:</text>
    <text x="15" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Jogging, football, swimming, gardening, tree planting,</text>
    <text x="15" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">traditional dance, and hiking.</text>
    <text x="15" y="162" fill="#34d399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Core Benefit: Cardiovascular fitness &amp; bodily health</text>
    <rect x="15" y="174" width="305" height="20" rx="4" fill="#0f172a"/>
    <text x="167" y="188" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Engages the physical body to release stress</text>
  </g>

  <!-- Right Column: Passive Leisure -->
  <g transform="translate(420, 175)">
    <rect width="335" height="205" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="335" height="34" rx="10" fill="url(#purpleGrad1)"/>
    <text x="167" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">PASSIVE LEISURE (MENTAL &amp; QUIET REST)</text>
    <text x="15" y="58" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Low Physical Energy &amp; Quiet Contemplation</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Involves mental focus, relaxation, and calm observation.</text>
    <text x="15" y="102" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Key Examples:</text>
    <text x="15" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Reading inspirational books, listening to music, watching</text>
    <text x="15" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">educational documentaries, board games, prayer &amp; meditation.</text>
    <text x="15" y="162" fill="#c084fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600">• Core Benefit: Mental renewal &amp; intellectual growth</text>
    <rect x="15" y="174" width="305" height="20" rx="4" fill="#0f172a"/>
    <text x="167" y="188" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Calms the nervous system and refreshes the mind</text>
  </g>

  <rect x="160" y="395" width="480" height="28" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="413" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">BIBLICAL BALANCE: A HEALTHY LIFE HARMONIZES WORK, ACTIVE RECREATION &amp; SACRED REST</text>
</svg>"""


def get_svg_lesson_2():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="goldGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg2)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE TWO PATHS OF LEISURE: EDIFICATION VS. DESTRUCTION</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">1 Corinthians 10:23, 31 — "Everything is permissible, but not everything is beneficial"</text>

  <!-- Central Decision Point -->
  <rect x="270" y="90" width="260" height="50" rx="10" fill="url(#goldGrad2)" stroke="#fbbf24" stroke-width="2"/>
  <text x="400" y="112" fill="#0f172a" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">MY FREE TIME / LEISURE</text>
  <text x="400" y="130" fill="#1e293b" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">How will I invest my God-given hours?</text>

  <!-- Branching Arrows -->
  <line x1="330" y1="140" x2="200" y2="175" stroke="#34d399" stroke-width="2.5"/>
  <line x1="470" y1="140" x2="600" y2="175" stroke="#ef4444" stroke-width="2.5"/>

  <!-- Left: Proper Use (The Constructive Path) -->
  <g transform="translate(35, 175)">
    <rect width="345" height="205" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="345" height="34" rx="10" fill="#059669"/>
    <text x="172" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">PROPER USE (CONSTRUCTIVE / EDIFYING)</text>
    <text x="15" y="58" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Worship &amp; Spiritual Growth:</text>
    <text x="15" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Prayer, Bible study, choir fellowship, Sunday school.</text>
    <text x="15" y="98" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Acts of Charity &amp; Service:</text>
    <text x="15" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Visiting the sick, helping elderly neighbors, tree planting.</text>
    <text x="15" y="138" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Talent &amp; Skill Development:</text>
    <text x="15" y="154" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Music practice, sports training, reading, creative arts.</text>
    <rect x="15" y="172" width="315" height="22" rx="4" fill="#0f172a"/>
    <text x="172" y="187" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">✓ Outcome: Strength, Wisdom, Peace &amp; Honor to God</text>
  </g>

  <!-- Right: Misuse (The Destructive Path) -->
  <g transform="translate(420, 175)">
    <rect width="345" height="205" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="345" height="34" rx="10" fill="#dc2626"/>
    <text x="172" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">MISUSE (DESTRUCTIVE / SINFUL)</text>
    <text x="15" y="58" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Substance Abuse &amp; Intoxication:</text>
    <text x="15" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Alcohol bingeing, smoking cigarettes, chewing miraa, drugs.</text>
    <text x="15" y="98" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Screen Addiction &amp; Immorality:</text>
    <text x="15" y="114" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Pornography, endless mindless scrolling, violent gaming.</text>
    <text x="15" y="138" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Gambling &amp; Destructive Idleness:</text>
    <text x="15" y="154" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Sports betting, gossip, loitering in unsafe company.</text>
    <rect x="15" y="172" width="315" height="22" rx="4" fill="#0f172a"/>
    <text x="172" y="187" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">❌ Outcome: Addiction, Poverty, Brokenness &amp; Regret</text>
  </g>

  <rect x="150" y="395" width="500" height="28" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="413" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">"SO WHETHER YOU EAT OR DRINK OR WHATEVER YOU DO, DO IT ALL FOR THE GLORY OF GOD" (1 COR 10:31)</text>
</svg>"""


def get_svg_lesson_3():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg3)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">SPECTRUM OF SUBSTANCES &amp; MODES OF ADMINISTRATION</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">1 Corinthians 6:19-20 — Understanding Chemical Classification and Safeguarding the Body</text>

  <!-- 3 Classification Columns -->
  <!-- Column 1: Medicinal Drugs -->
  <g transform="translate(35, 82)">
    <rect width="225" height="215" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="225" height="32" rx="8" fill="#0284c7"/>
    <text x="112" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">1. MEDICINAL DRUGS</text>
    <text x="12" y="52" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Purpose: Healing &amp; Prevention</text>
    <text x="12" y="68" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Prescribed by qualified doctors</text>
    <text x="12" y="82" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">to restore body homeostasis.</text>
    <text x="12" y="106" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Examples:</text>
    <text x="12" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Antibiotics, painkillers, malaria</text>
    <text x="12" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">drugs, vaccines, sedatives.</text>
    <text x="12" y="160" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Moral Status:</text>
    <text x="12" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Lawful &amp; constructive when taken</text>
    <text x="12" y="190" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">strictly as prescribed.</text>
  </g>

  <!-- Column 2: Soft Drugs -->
  <g transform="translate(285, 82)">
    <rect width="230" height="215" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="230" height="32" rx="8" fill="#d97706"/>
    <text x="115" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">2. SOFT DRUGS</text>
    <text x="12" y="52" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Nature: Mild Stimulants/Depressants</text>
    <text x="12" y="68" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Often socially permitted or legal</text>
    <text x="12" y="82" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">for adults, yet highly addictive.</text>
    <text x="12" y="106" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Examples:</text>
    <text x="12" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Tobacco/Cigarettes, Alcohol,</text>
    <text x="12" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Miraa (Khat), Coffee/Caffeine.</text>
    <text x="12" y="160" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Danger / Threat:</text>
    <text x="12" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Gateway to hard narcotics and</text>
    <text x="12" y="190" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">severe chronic organ damage.</text>
  </g>

  <!-- Column 3: Hard Drugs (Narcotics) -->
  <g transform="translate(540, 82)">
    <rect width="225" height="215" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="225" height="32" rx="8" fill="#dc2626"/>
    <text x="112" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">3. HARD DRUGS (NARCOTICS)</text>
    <text x="12" y="52" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Nature: Illicit &amp; Highly Destructive</text>
    <text x="12" y="68" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Heavily alter Central Nervous</text>
    <text x="12" y="82" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">System; rapid dependence.</text>
    <text x="12" y="106" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Examples:</text>
    <text x="12" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Heroin, Cocaine, Cannabis</text>
    <text x="12" y="136" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">(Bhang/Marijuana), Mandrax.</text>
    <text x="12" y="160" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Devastation:</text>
    <text x="12" y="176" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Brain breakdown, violent crime,</text>
    <text x="12" y="190" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">overdose death, insanity.</text>
  </g>

  <!-- Bottom Panel: 5 Modes of Administration -->
  <g transform="translate(35, 310)">
    <rect width="730" height="90" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1.2"/>
    <text x="365" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">FIVE PRIMARY MODES OF DRUG ADMINISTRATION</text>
    <line x1="20" y1="32" x2="710" y2="32" stroke="#334155" stroke-width="1"/>
    
    <text x="60" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">1. Ingestion</text>
    <text x="40" y="72" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Swallowing pills/liquids</text>

    <text x="200" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">2. Inhalation</text>
    <text x="180" y="72" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Smoking / vapors</text>

    <text x="350" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">3. Chewing</text>
    <text x="330" y="72" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Grinding plant leaves</text>

    <text x="500" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">4. Injection</text>
    <text x="475" y="72" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Needles into veins</text>

    <text x="640" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">5. Sniffing</text>
    <text x="620" y="72" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Nasal powder intake</text>
  </g>

  <text x="400" y="423" fill="#64748b" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">"YOUR BODY IS A TEMPLE OF THE HOLY SPIRIT... YOU WERE BOUGHT AT A PRICE" (1 COR 6:19-20)</text>
</svg>"""


def get_svg_lesson_4():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg4)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">BIOLOGICAL &amp; SOCIAL IMPACT OF SUBSTANCE ABUSE</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Proverbs 23:29-35 &amp; Ephesians 5:18 — How Drugs Ravage the Human Body and Social Fabric</text>

  <!-- 4 Organ Impact Cards -->
  <!-- 1. The Brain -->
  <g transform="translate(35, 80)">
    <rect width="170" height="150" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="170" height="28" rx="8" fill="#dc2626"/>
    <text x="85" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. BRAIN &amp; CNS</text>
    <text x="10" y="48" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Brain Cell Death</text>
    <text x="10" y="64" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Memory loss &amp; psychosis.</text>
    <text x="10" y="85" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Hallucinations</text>
    <text x="10" y="101" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Altered perception &amp; mania.</text>
    <text x="10" y="122" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Severe Addiction</text>
    <text x="10" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Loss of moral self-control.</text>
  </g>

  <!-- 2. The Liver -->
  <g transform="translate(225, 80)">
    <rect width="170" height="150" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="170" height="28" rx="8" fill="#d97706"/>
    <text x="85" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. LIVER &amp; ORGANS</text>
    <text x="10" y="48" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Liver Cirrhosis</text>
    <text x="10" y="64" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Healthy tissue scarred.</text>
    <text x="10" y="85" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Stomach Ulcers</text>
    <text x="10" y="101" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Internal mucosal bleeding.</text>
    <text x="10" y="122" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Kidney Failure</text>
    <text x="10" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Total metabolic toxicity.</text>
  </g>

  <!-- 3. The Lungs & Heart -->
  <g transform="translate(415, 80)">
    <rect width="170" height="150" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="170" height="28" rx="8" fill="#7c3aed"/>
    <text x="85" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. LUNGS &amp; HEART</text>
    <text x="10" y="48" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Lung Cancer &amp; Tar</text>
    <text x="10" y="64" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Black sticky tar buildup.</text>
    <text x="10" y="85" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Arterial Blockage</text>
    <text x="10" y="101" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Carbon monoxide poisoning.</text>
    <text x="10" y="122" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Cardiac Arrest</text>
    <text x="10" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Overdose heart shutdown.</text>
  </g>

  <!-- 4. Family & Society -->
  <g transform="translate(600, 80)">
    <rect width="165" height="150" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="165" height="28" rx="8" fill="#0284c7"/>
    <text x="82" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">4. FAMILY &amp; SOCIETY</text>
    <text x="10" y="48" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Domestic Violence</text>
    <text x="10" y="64" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Quarrels &amp; broken homes.</text>
    <text x="10" y="85" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Severe Poverty</text>
    <text x="10" y="101" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Squandering household funds.</text>
    <text x="10" y="122" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Academic Dropout</text>
    <text x="10" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Expulsion and failure.</text>
  </g>

  <!-- Bottom Table: Soft vs Hard Drugs -->
  <g transform="translate(35, 245)">
    <rect width="730" height="145" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.2"/>
    <rect width="730" height="28" rx="8" fill="#0f172a"/>
    <text x="180" y="18" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">SOFT DRUGS (GATEWAY HAZARDS)</text>
    <text x="540" y="18" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">HARD DRUGS (NARCOTIC CATASTROPHES)</text>
    <line x1="365" y1="0" x2="365" y2="145" stroke="#334155" stroke-width="1.5"/>

    <text x="15" y="48" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Alcohol:</text>
    <text x="75" y="48" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Cirrhosis, drunk driving, road carnage, violence.</text>
    <text x="15" y="76" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Tobacco:</text>
    <text x="75" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Nicotine addiction, tar coating lungs, throat cancer.</text>
    <text x="15" y="104" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Miraa (Khat):</text>
    <text x="95" y="104" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Insomnia, teeth decay, loss of appetite, irritability.</text>
    <text x="15" y="132" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">Legal in commerce, yet chemically insidious &amp; addictive.</text>

    <text x="380" y="48" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Bhang (Cannabis):</text>
    <text x="495" y="48" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Psychosis, violent crime, cognitive decline.</text>
    <text x="380" y="76" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Cocaine:</text>
    <text x="440" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Extreme euphoria, heart palpitations, sudden arrest.</text>
    <text x="380" y="104" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Heroin:</text>
    <text x="440" y="104" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Needle sharing (HIV risk), respiratory collapse death.</text>
    <text x="380" y="132" fill="#ef4444" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600">Strictly illegal, devastating to youth and family life.</text>
  </g>

  <text x="400" y="415" fill="#64748b" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">"WINE IS A MOCKER AND BEER A BRAWLER; WHOEVER IS LED ASTRAY BY THEM IS NOT WISE" (PROV 20:1)</text>
</svg>"""


def get_svg_lesson_5():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="shieldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg5)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE FOUR-SECTOR COLLABORATIVE REMEDY NETWORK</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">1 Corinthians 15:33 &amp; 1 Peter 5:8 — National, Educational, Spiritual, and Family Strategies</text>

  <!-- Central Shield: Holistic Victory over Substance Abuse -->
  <circle cx="400" cy="235" r="52" fill="url(#shieldGrad)" stroke="#38bdf8" stroke-width="2"/>
  <text x="400" y="230" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">HOLISTIC</text>
  <text x="400" y="246" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">REMEDY</text>

  <!-- 4 Sectors -->
  <!-- Sector 1: Government (NACADA & Law Enforcement) -->
  <line x1="350" y1="200" x2="220" y2="135" stroke="#38bdf8" stroke-width="2"/>
  <g transform="translate(30, 85)">
    <rect width="220" height="110" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="220" height="26" rx="8" fill="#0284c7"/>
    <text x="110" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. GOVERNMENT / NACADA</text>
    <text x="10" y="44" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Anti-Narcotics Police:</text>
    <text x="10" y="58" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Arresting cartels &amp; closing dens.</text>
    <text x="10" y="78" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• NACADA Campaigns:</text>
    <text x="10" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Public education &amp; helpline 1192.</text>
  </g>

  <!-- Sector 2: School / Curriculum -->
  <line x1="450" y1="200" x2="580" y2="135" stroke="#34d399" stroke-width="2"/>
  <g transform="translate(550, 85)">
    <rect width="220" height="110" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="220" height="26" rx="8" fill="#059669"/>
    <text x="110" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. SCHOOL &amp; GUIDANCE</text>
    <text x="10" y="44" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• CBC Curriculum:</text>
    <text x="10" y="58" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Teaching biological/moral risks.</text>
    <text x="10" y="78" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Guidance &amp; Counseling:</text>
    <text x="10" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Emotional support for stressed youth.</text>
  </g>

  <!-- Sector 3: Church / Spiritual Community -->
  <line x1="350" y1="270" x2="220" y2="335" stroke="#a855f7" stroke-width="2"/>
  <g transform="translate(30, 275)">
    <rect width="220" height="110" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="220" height="26" rx="8" fill="#7c3aed"/>
    <text x="110" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. CHURCH &amp; FAITH</text>
    <text x="10" y="44" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Spiritual Regeneration:</text>
    <text x="10" y="58" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Teaching body as God's temple.</text>
    <text x="10" y="78" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Compassionate Rehab:</text>
    <text x="10" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Faith-based recovery &amp; fellowship.</text>
  </g>

  <!-- Sector 4: Family & Peer Resistance -->
  <line x1="450" y1="270" x2="580" y2="335" stroke="#f59e0b" stroke-width="2"/>
  <g transform="translate(550, 275)">
    <rect width="220" height="110" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="220" height="26" rx="8" fill="#d97706"/>
    <text x="110" y="18" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">4. FAMILY &amp; HOME</text>
    <text x="10" y="44" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Sober Role Modeling:</text>
    <text x="10" y="58" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Parents setting sober examples.</text>
    <text x="10" y="78" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Peer Resistance Skills:</text>
    <text x="10" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Choosing sober, upright friends.</text>
  </g>

  <rect x="180" y="400" width="440" height="26" rx="5" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="417" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">TOTAL VICTORY: COMBATING DRUGS REQUIRES INTEGRATED ENFORCEMENT, EDUCATION &amp; LOVE</text>
</svg>"""


def get_svg_lesson_6():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="filterGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg6)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE CHRISTIAN LEISURE FILTER: 7-POINT MORAL CHECKLIST</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Philippians 4:8 &amp; Romans 12:1-2 — Evaluating Entertainment, Music, and Recreation</text>

  <!-- Left: The 7 Filter Criteria -->
  <g transform="translate(35, 85)">
    <rect width="420" height="295" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="420" height="32" rx="10" fill="#0284c7"/>
    <text x="210" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">THE 7 BIBLICAL CRITERIA FOR LEISURE EVALUATION</text>
    
    <text x="15" y="58" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">1. Promotes Human Dignity:</text>
    <text x="180" y="58" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Does not degrade, sexualize, or demean self/others.</text>

    <text x="15" y="90" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">2. Serves God's Purpose:</text>
    <text x="180" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Draws the soul closer to Christ; glorifies God.</text>

    <text x="15" y="122" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">3. Comes AFTER Work:</text>
    <text x="180" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">A reward for diligence, not an excuse for laziness.</text>

    <text x="15" y="154" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">4. Harmless to Body &amp; Mind:</text>
    <text x="180" y="154" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Avoids reckless dangers, fights, or toxic chemicals.</text>

    <text x="15" y="186" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">5. Avoids Addiction / Sloth:</text>
    <text x="180" y="186" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Does not enslave the mind in compulsive habits.</text>

    <text x="15" y="218" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">6. Practiced in Moderation:</text>
    <text x="180" y="218" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Balanced; does not consume excessive funds or time.</text>

    <text x="15" y="250" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">7. Lawful &amp; Morally Pure:</text>
    <text x="180" y="250" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Obeys constitutional laws and God's moral law.</text>

    <rect x="15" y="266" width="390" height="20" rx="4" fill="#0f172a"/>
    <text x="210" y="280" fill="#34d399" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">✓ If an activity fails even one test, replace it with edifying recreation!</text>
  </g>

  <!-- Right: Philippians 4:8 Standard -->
  <g transform="translate(480, 85)">
    <rect width="285" height="295" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="285" height="32" rx="10" fill="#059669"/>
    <text x="142" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">PHILIPPIANS 4:8 STANDARD</text>
    
    <text x="15" y="60" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11" font-weight="700">"Whatever is..."</text>
    <text x="25" y="85" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5">• TRUE</text>
    <text x="150" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Honest &amp; authentic</text>

    <text x="25" y="115" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5">• NOBLE</text>
    <text x="150" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Worthy of respect</text>

    <text x="25" y="145" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5">• RIGHT</text>
    <text x="150" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Just &amp; righteous</text>

    <text x="25" y="175" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5">• PURE</text>
    <text x="150" y="175" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Morally clean</text>

    <text x="25" y="205" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5">• LOVELY</text>
    <text x="150" y="205" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Gracious &amp; kind</text>

    <text x="25" y="235" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5">• ADMIRABLE</text>
    <text x="150" y="235" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Of good reputation</text>

    <rect x="15" y="258" width="255" height="26" rx="4" fill="#0f172a"/>
    <text x="142" y="275" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">"THINK ABOUT SUCH THINGS"</text>
  </g>

  <rect x="160" y="395" width="480" height="28" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="413" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">MORAL INTEGRITY: TRANSFORMING FREE TIME INTO SACRED GROWTH AND GODLY JOY</text>
</svg>"""


# ─── LESSON DATA CONFIGURATIONS (6 LESSONS) ───────────────────────────────────

LESSONS_DATA = [
    # ─── LESSON 1 ────────────────────────────────────────────────────────────
    {
        "unit_order": 1,
        "unit_name": "Meaning and Forms of Leisure",
        "unit_description": "Define the concept of leisure, examine God's design for rest and recreation in Genesis 2:1-3 and Mark 6:31, and distinguish between active and passive forms of leisure.",
        "lesson_title": "Meaning and Forms of Leisure",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/8/87/Jean-Fran%C3%A7ois_Millet_-_The_Angelus_-_Google_Art_Project.jpg",
            "title": "Visual Hook: Resting from Labor and Giving Thanks",
            "author": "Jean-François Millet (Musée d'Orsay Collection)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Peasants pausing their fieldwork at the sound of church bells to rest and pray, illustrating the sacred rhythm of work, rest, and spiritual thanksgiving."
        },
        "youtube": {
            "youtube_id": "PFTb0y6gX4A",
            "title": "BibleProject: Sabbath (The Art of Rest)",
            "description": "An inspiring exploration of the biblical theme of Sabbath, discovering how God instituted rest and recreation as a sacred gift of liberation, renewal, and divine fellowship."
        },
        "svg_fn": get_svg_lesson_1,
        "goals": [
            "Define leisure and explain the theological foundation of rest in Genesis 2:1-3 and Mark 6:31.",
            "Differentiate clearly between active leisure and passive leisure, providing relevant real-world examples of each.",
            "Formulate a balanced personal weekly schedule that integrates duty, active recreation, mental rest, and spiritual devotion."
        ],
        "intro": "Think about how you feel after sitting in class for several consecutive hours, solving demanding mathematics equations, writing extensive notes, and completing practical science experiments. Your brain feels mentally drained, your muscles are stiff, and your energy is depleted. What is the very first thing you desire when the final bell rings for recess or the weekend? You want to relax and recharge!\n\nRest is not an accident or an afterthought—it is a foundational rhythm woven into creation by God Himself. When we understand leisure from a biblical perspective, we discover that free time is not meant for aimless idleness, but is a sacred gift designed for renewal, joy, and physical rejuvenation.",
        "core_scripture": "### Scriptural Passages: Genesis 2:1-3 & Mark 6:31\n\n> *\"Thus the heavens and the earth were finished, and all the host of them. And on the seventh day God finished his work that he had done, and he rested on the seventh day from all his work that he had done. So God blessed the seventh day and made it holy, because on it God rested from all his work that he had done in creation.\"* (Genesis 2:1-3)\n\n> *\"And he said to them, 'Come away by yourselves to a desolate place and rest a while.' For many were coming and going, and they had no leisure even to eat.\"* (Mark 6:31)",
        "theological_pillars": "### Theological Exegesis: The Divine Origin & Forms of Leisure\n\n1. **God as the Originator of Rest (Genesis 2:1-3):** God did not rest on the seventh day because He was exhausted or depleted of omnipotent energy. Rather, His rest (*shabbat*) marked the celebration of a complete, harmonious creation. By blessing the seventh day and declaring it holy, God established rest as an essential covenantal rhythm for all humanity.\n2. **Jesus' Pastoral Care for Weary Disciples (Mark 6:31):** Ministry and labor in the Kingdom of God are demanding. When the Apostles returned from their intensive preaching mission, crowds pressed in relentlessly. Jesus commanded them to withdraw to a quiet, solitary place to rest, demonstrating that caring for physical and mental limits is an act of spiritual wisdom, not laziness.\n3. **Definition of Leisure:** Leisure refers to the time when an individual is completely free from obligatory work, school study, employment duties, or compulsory domestic chores. It is time placed at one's personal disposal to be used constructively for physical, mental, social, and spiritual rejuvenation.\n4. **Active Leisure:** Free-time pursuits that demand physical exertion, muscular coordination, and body movement. Examples include football, jogging, swimming, gardening, tree planting, and traditional dance.\n5. **Passive Leisure:** Free-time pursuits that involve mental relaxation, quiet observation, and calm reflection without strenuous physical exertion. Examples include reading inspirational literature, playing chess, listening to soothing gospel music, watching educational documentaries, and quiet prayer.",
        "deep_dive": "### Deep Dive: Traditional African Leisure vs. Contemporary Idleness\n\nIn Traditional African Society (TAS), leisure and work were never viewed as hostile opposites. Instead, they were deeply integrated into everyday community life:\n\n- **Communal and Educational Recreation:** Traditional leisure occurred through communal storytelling around evening fireplaces, riddle-solving (*vitendawili*), wrestling contests, folk songs during harvesting, and traditional dances. These activities taught moral virtues, bravery, and tribal history.\n- **Productive Integration:** Leisure was rarely solitary or idle; it reinforced social bonding between elders, youth, and children.\n- **The Modern Challenge of Digital Idleness:** Today, the shift from communal recreation to isolated digital entertainment has led many young people to equate leisure with boredom or mindless scrolling. Christian ethics calls learners to reclaim leisure as an active, purposeful investment in character and bodily health.",
        "practical": {
            "title": "Action Framework: Designing a Balanced Weekly Leisure Rhythm",
            "steps": [
                "Step 1: Audit Your Weekly Hours — Identify your fixed hours for classes, chores, and sleep, calculating your exact free leisure hours.",
                "Step 2: Balance Active and Passive Activities — Ensure your free time includes both vigorous physical movement (sports, jogging, gardening) and quiet mental relaxation (reading, music).",
                "Step 3: Guard Dedicated Time for Sabbath Fellowship — Set aside undistracted time on the weekend for church worship, family bonding, and spiritual reflection.",
                "Step 4: Eliminate Idle Time Traps — Replace unproductive, mindless loafing with constructive creative hobbies such as learning a musical instrument or tree planting."
            ]
        },
        "kenyan_context": "### Kenyan Real-World Context: Healthy Youth Recreation\n\nAcross Kenyan Junior Secondary Schools and local communities, constructive leisure plays a vital role in keeping youth vibrant and morally grounded. Initiatives such as the Kenya Music Festival, school sports leagues (football, athletics, volleyball), Scouts and Girl Guides clubs, and 4-K Clubs (gardening and agriculture) provide rich active leisure opportunities. Engaging in these community programs prevents the dangerous vacuum of idleness that makes adolescents vulnerable to negative peer influences.",
        "reflection": "Reflect on how Jesus commanded His disciples: *'Come away by yourselves to a desolate place and rest a while'* (Mark 6:31). In our fast-paced culture where people boast about being busy 24/7 or get trapped in endless social media consumption, how can you intentionally schedule quiet, holy rest that truly refreshes your heart, mind, and body in God's presence?",
        "takeaways": [
            "Leisure is time free from compulsory labor, school study, and domestic chores, given by God for renewal.",
            "God instituted the principle of rest at creation (Genesis 2:1-3), and Jesus modeled the necessity of withdrawing for rest (Mark 6:31).",
            "Active leisure involves bodily exertion (sports, jogging, gardening), promoting physical fitness.",
            "Passive leisure involves quiet contemplation and mental relaxation (reading, listening to music, prayer).",
            "A balanced Christian lifestyle harmonizes productive work, active recreation, and sacred rest."
        ],
        "mcq": {
            "question": "Which of the following activities is correctly classified as an ACTIVE form of leisure?",
            "options": [
                "Reading a Christian novel in the library",
                "Planting trees and playing football on the school field",
                "Listening to audio podcasts while lying in bed",
                "Watching a live sports broadcast on television"
            ],
            "correct_answer": "Planting trees and playing football on the school field",
            "explanation": "Active leisure requires physical movement, energy expenditure, and muscular coordination, such as sports, gardening, and tree planting. Reading, listening to podcasts, and watching television are passive leisure activities that involve mental relaxation without strenuous physical exertion."
        }
    },

    # ─── LESSON 2 ────────────────────────────────────────────────────────────
    {
        "unit_order": 2,
        "unit_name": "Importance, Proper Use and Misuse of Leisure",
        "unit_description": "Analyze why leisure is essential for human development, evaluate biblical principles of proper leisure use under 1 Corinthians 10:23, 31, and examine common contemporary misuses.",
        "lesson_title": "Importance, Proper Use and Misuse of Leisure",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Community_service_youth_volunteering.jpg",
            "title": "Visual Hook: Youth Engaging in Constructive Community Service",
            "author": "Wikimedia Commons Open Archive",
            "licensing": "Creative Commons Attribution-Share Alike",
            "source": "Wikimedia Commons",
            "caption": "Young volunteers dedicating their weekend leisure time to environmental conservation and community service, exemplifying constructive and edifying leisure."
        },
        "youtube": {
            "youtube_id": "jS4O5qTf_Xk",
            "title": "BibleProject: Generosity & Stewardship",
            "description": "A compelling biblical overview demonstrating how Christians are called to be faithful stewards of their time, energy, and talents for the glory of God and the uplifting of others."
        },
        "svg_fn": get_svg_lesson_2,
        "goals": [
            "Outline five major physiological, psychological, social, and spiritual benefits of leisure.",
            "Categorize constructive uses of free time versus destructive misuses using the ethical standard of 1 Corinthians 10:23, 31.",
            "Formulate actionable strategies to volunteer in community charity and eliminate harmful leisure habits."
        ],
        "intro": "Have you ever heard the time-tested proverb: *'An idle mind is the devil's workshop'*? This ancient saying warns us that when we have unstructured, unplanned free time with no clear goals or values, our minds become extraordinarily vulnerable to temptation, gossip, negative peer pressure, and destructive experimentation.\n\nTime is one of the most valuable resources God has entrusted into our hands. Once an hour is spent, it can never be retrieved. The Apostle Paul wrote to the church in Corinth: *'\"I have the right to do anything,\" you say—but not everything is beneficial. \"I have the right to do anything\"—but not everything is constructive'* (1 Corinthians 10:23). How can we ensure our leisure builds us up rather than tears us down?",
        "core_scripture": "### Scriptural Passages: 1 Corinthians 10:23, 31 & Galatians 6:9-10\n\n> *\"'I have the right to do anything,' you say—but not everything is beneficial. 'I have the right to do anything'—but not everything is constructive. No one should seek their own good, but the good of others... So whether you eat or drink or whatever you do, do it all for the glory of God.\"* (1 Corinthians 10:23-24, 31)\n\n> *\"Let us not become weary in doing good, for at the proper time we will reap a harvest if we do not give up. Therefore, as we have opportunity, let us do good to all people, especially to those who belong to the family of believers.\"* (Galatians 6:9-10)",
        "theological_pillars": "### Theological Exegesis: The Ethics of Stewardship in Free Time\n\n1. **The Principle of Edification (1 Corinthians 10:23):** Christian liberty is not a license for self-indulgent dissipation. While an activity may not be explicitly illegal under civil law, believers must ask: *'Does this build up my character, strengthen my faith, and benefit my neighbor?'* Proper leisure must always be constructive (*oikodomeo*).\n2. **The Supreme Standard of God's Glory (1 Corinthians 10:31):** Every dimension of human existence—including recreation, eating, sports, and entertainment—must be conducted in a manner that reflects God's holiness, integrity, and beauty.\n3. **Why Leisure is Crucial (Benefits of Proper Rest):**\n   - *Physical Restoration:* Relieves bodily fatigue, repairs muscle tissues, and restores vitality.\n   - *Mental & Emotional Refreshment:* Alleviates academic stress, anxiety, and mental exhaustion, boosting creativity.\n   - *Discovery of Talents:* Provides time to develop musical, artistic, culinary, and athletic gifts.\n   - *Social Cohesion:* Deepens family bonds, builds healthy friendships, and fosters community harmony.\n   - *Spiritual Renewal:* Grants unhurried space for prayer, Bible meditation, worship, and fellowship.\n4. **Proper vs. Destructive Uses of Leisure:**\n   - *Proper Uses:* Church fellowship, choir practice, visiting orphans and the elderly, participating in environmental clean-ups, reading edifying literature, and family bonding.\n   - *Destructive Misuses:* Substance abuse (alcohol, miraa, drugs), excessive screen addiction and viewing pornography, online cyberbullying and gossip, gambling/sports betting, and roaming in dangerous gangs.",
        "deep_dive": "### Deep Dive: The Modern Crisis of Digital Screen Addiction & Betting\n\nIn recent years, the commercialization of leisure has introduced severe moral and social hazards among adolescents:\n\n- **Digital Screen Captivity:** Excessive social media scrolling and gaming isolate teenagers from real-world relationships, leading to sleep deprivation, anxiety, and exposure to vulgar content.\n- **Commercial Gambling & Sports Betting:** Many young people squander their pocket money in online gambling platforms seeking quick wealth. This creates severe psychological addiction, debts, dishonesty, and anxiety.\n- **The Christian Response:** Christians are called to exercise self-control and moderation, using digital technology as a constructive tool for learning and communication rather than an idol that consumes their youth.",
        "practical": {
            "title": "Action Framework: Transforming Leisure into Community Blessing",
            "steps": [
                "Step 1: Conduct a Weekly Time Audit — Track how many hours you spend on social media, TV, and gaming versus study, family chores, and worship.",
                "Step 2: Commit to a Local Service Project — Dedicate at least two hours every weekend to help an elderly neighbor, clean the church compound, or visit a hospital.",
                "Step 3: Cultivate an Edifying Hobby — Dedicate free time to learning a productive life skill (e.g. baking, carpentry, musical instruments, coding, or public speaking).",
                "Step 4: Establish Digital Boundaries — Set strict limits on screen time, turning off notifications during study and family meals to protect your mental health."
            ]
        },
        "kenyan_context": "### Kenyan Real-World Context: School Holidays & Community Engagement\n\nDuring Kenyan school holidays (April, August, and December), teenagers often face long stretches of unstructured time. Across Kenya, churches and community organizations organize Vacation Bible Schools (VBS), youth empowerment camps, tree planting drives in local forests (supporting the national goal of increasing tree cover), and sports tournaments. Participating in these structured, noble programs protects young Kenyans from the traps of idleness and builds leadership character.",
        "reflection": "Consider 1 Corinthians 10:31: *'Whatever you do, do it all for the glory of God.'* When you look at how you spent your free time over the past week, did your choices reflect God's glory and build up your future, or did they leave you feeling drained, guilty, and distracted?",
        "takeaways": [
            "Leisure is essential for physical repair, mental rejuvenation, talent development, and spiritual communion.",
            "According to 1 Corinthians 10:23, 31, all leisure activities must be edifying and bring glory to God.",
            "Constructive uses of leisure include worship, community charity, skill acquisition, and family fellowship.",
            "Common misuses of leisure include substance abuse, pornography, gambling, excessive screen time, and gossip.",
            "Christian stewardship requires actively investing our free time in activities that bless others and build our character."
        ],
        "mcq": {
            "question": "According to 1 Corinthians 10:23 and 31, what is the ultimate standard for evaluating how a Christian spends their leisure time?",
            "options": [
                "Whether the activity is completely free of financial cost",
                "Whether the activity is popular among all social media influencers",
                "Whether the activity is constructive, edifying, and brings glory to God",
                "Whether the activity allows an individual to avoid all household chores"
            ],
            "correct_answer": "Whether the activity is constructive, edifying, and brings glory to God",
            "explanation": "Paul emphasizes in 1 Corinthians 10:23, 31 that while believers have freedom, our choices must be beneficial, constructive, and done entirely for the glory of God and the edification of others."
        }
    },

    # ─── LESSON 3 ────────────────────────────────────────────────────────────
    {
        "unit_order": 3,
        "unit_name": "Understanding Drug and Substance Abuse",
        "unit_description": "Define drugs and drug abuse, classify chemical substances into medicinal, soft, and hard categories, explore five modes of drug administration, and apply 1 Corinthians 6:19-20 to bodily stewardship.",
        "lesson_title": "Understanding Drug and Substance Abuse",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/6/64/Mortar_and_pestle_with_medicines.jpg",
            "title": "Visual Hook: The Boundary Between Medicine and Abuse",
            "author": "Wikimedia Commons Educational Archive",
            "licensing": "Creative Commons Attribution",
            "source": "Wikimedia Commons",
            "caption": "A pharmaceutical mortar and pestle with medicines, symbolizing the scientific boundary between legitimate medicinal healing and dangerous chemical abuse."
        },
        "youtube": {
            "youtube_id": "AzmYV8GNAIM",
            "title": "BibleProject: Wisdom & Proverbs",
            "description": "An engaging exploration of biblical wisdom in the Book of Proverbs, showing how moral discernment and reverence for God protect youth from deadly physical and spiritual traps."
        },
        "svg_fn": get_svg_lesson_3,
        "goals": [
            "Define a drug, distinguish between drug use and drug abuse, and explain five modes of administration.",
            "Classify chemical substances into medicinal drugs, soft drugs, and hard drugs (narcotics).",
            "Defend the sanctity and holiness of the human body as God's temple based on 1 Corinthians 6:19-20."
        ],
        "intro": "Think about a time when you had a severe bout of malaria, an intense bacterial throat infection, or a throbbing fever. Your parents took you to a certified medical clinic, where a doctor carefully diagnosed you and prescribed specific tablets. You swallowed the medicine in the exact dosage for five days, and your body was restored to full health. In this context, the medicine was a life-saving tool.\n\nNow imagine a student who is completely healthy, but swallows strong prescription painkillers or sniffs toxic industrial glue behind the school dormitory simply to escape exam stress, fit in with older peers, or experience a temporary high. Here, a chemical substance becomes a lethal weapon. Today, we investigate the scientific and moral reality of drugs and substance abuse.",
        "core_scripture": "### Scriptural Passages: 1 Corinthians 6:19-20 & Proverbs 20:1\n\n> *\"Do you not know that your bodies are temples of the Holy Spirit, who is in you, whom you have received from God? You are not your own; you were bought at a price. Therefore honor God with your bodies.\"* (1 Corinthians 6:19-20)\n\n> *\"Wine is a mocker and beer a brawler; whoever is led astray by them is not wise.\"* (Proverbs 20:1)",
        "theological_pillars": "### Theological Exegesis: The Body as the Sacred Temple of God\n\n1. **The Doctrine of Bodily Ownership (1 Corinthians 6:19-20):** In secular philosophy, people frequently proclaim: *'It is my body, and I can do whatever I want with it.'* Christian theology completely rejects this falsehood. The believer's body is the sacred dwelling place of the Holy Spirit, purchased at an infinite cost through the blood of Jesus Christ. Intentionally poisoning the body with toxic chemicals is a desecration of God's sanctuary.\n2. **Scientific & Ethical Definitions:**\n   - *Drug:* Any chemical substance which, when introduced into a living organism, alters or modifies one or more of its normal physiological, neurological, or psychological functions.\n   - *Drug Use:* The proper, legal, and medically supervised intake of a pharmaceutical substance for its intended curative, preventive, or pain-relieving purpose in the exact prescribed dosage.\n   - *Drug Abuse:* The improper, illegal, or non-medical consumption of any chemical substance for purposes other than healing, such as seeking temporary euphoria, intoxication, or reality escapism.\n3. **Classification of Substances:**\n   - *Medicinal Drugs:* Legitimate pharmaceuticals used to prevent, treat, or alleviate illnesses (e.g. antibiotics, analgesics, antimalarials, vaccines, sedatives).\n   - *Soft Drugs:* Substances that are legally accessible or socially tolerated in some adult societies, but act as mild stimulants or depressants and carry high addictive potential (e.g. tobacco/cigarettes, alcohol, miraa/khat, caffeine).\n   - *Hard Drugs (Narcotics):* Highly toxic, illicit chemicals that violently disrupt the central nervous system, inducing severe hallucinations, rapid physical dependency, and fatal overdoses (e.g. heroin, cocaine, cannabis/bhang, mandrax).\n4. **Modes of Drug Administration:**\n   - *Ingestion (Swallowing):* Consuming liquid syrups or swallowing tablets through the mouth.\n   - *Inhalation (Smoking):* Breathing in smoke, fumes, or volatile chemical vapors (e.g. cigarettes, bhang, glue).\n   - *Chewing:* Masticating plant leaves to extract active chemical juices (e.g. miraa/khat).\n   - *Injection:* Using hypodermic needles to inject liquid drugs directly into veins or muscle tissues (e.g. heroin, morphine).\n   - *Sniffing / Snorting:* Inhaling chemical powders directly through the nasal membranes (e.g. cocaine, snuff).",
        "deep_dive": "### Deep Dive: How Prescription Misuse & Self-Medication Lead to Addiction\n\nDrug abuse does not begin only with illegal street narcotics; it frequently starts with the careless handling of ordinary household medicines:\n\n- **The Hazard of Self-Medication:** Taking antibiotics or strong sedatives without a doctor's prescription or diagnostic laboratory test can lead to antimicrobial resistance, liver toxicity, and chemical dependence.\n- **Sharing Prescriptions:** Giving your prescription painkillers or cough syrups to siblings or classmates is dangerous because dosages depend on body weight, age, and medical history.\n- **Sedative Abuse:** Overusing tranquilizers or sleeping pills to cope with academic anxiety destroys the brain's natural ability to regulate stress, creating an artificial chemical crutch.",
        "practical": {
            "title": "Action Framework: Safe Medical Stewardship & Chemical Safeguards",
            "steps": [
                "Step 1: Always Demand Professional Prescriptions — Never consume any pharmaceutical drug without verified diagnosis and prescription from a qualified healthcare provider.",
                "Step 2: Adhere Strictly to Dosage & Duration — Finish all prescribed doses of antibiotics exactly as instructed, and never exceed the recommended painkiller dosage.",
                "Step 3: Reject Unlabeled & Suspicious Substances — Refuse to swallow, taste, or inhale any mystery powder, drink, or confectionery offered by peers or strangers.",
                "Step 4: Treat Your Body as God's Sacred Temple — Affirm your identity in Christ every morning, honoring your physical organs through clean nutrition, hydration, and exercise."
            ]
        },
        "kenyan_context": "### Kenyan Real-World Context: Pharmacy Regulations & Youth Protection\n\nIn Kenya, the Pharmacy and Poisons Board (PPB) regulates the manufacture, importation, and sale of all pharmaceuticals. In many urban and rural shopping centres, illegal chemists and unlicensed kiosks unlawfully sell prescription drugs over the counter without prescriptions. Junior Secondary School learners must understand that buying medicines from unlicensed vendors puts them at grave risk of counterfeit drugs, poisoning, and substance addiction.",
        "reflection": "Mediate upon 1 Corinthians 6:20: *'You were bought at a price. Therefore honor God with your bodies.'* How does viewing your brain, heart, lungs, and liver as sacred gifts purchased by Jesus change the way you protect yourself against harmful chemical substances?",
        "takeaways": [
            "A drug alters physiological and psychological functions; drug abuse is the non-medical or excessive intake of chemicals.",
            "Our bodies belong to God and are holy temples of the Holy Spirit (1 Corinthians 6:19-20).",
            "Substances are classified into medicinal drugs (healing), soft drugs (tobacco, alcohol, miraa), and hard drugs (heroin, cocaine, bhang).",
            "Drugs enter the body via ingestion, inhalation/smoking, chewing, injection, and sniffing.",
            "Self-medication and sharing prescriptions are dangerous forms of substance misuse that can cause organ damage."
        ],
        "mcq": {
            "question": "Which of the following scenarios best illustrates DRUG ABUSE as defined in medical science and Christian ethics?",
            "options": [
                "Taking a full dose of antimalarial medication prescribed by a qualified physician",
                "Receiving a routine childhood vaccine administered at a government hospital",
                "Swallowing strong painkillers without a prescription to cope with exam anxiety and get high",
                "Applying an antiseptic ointment on a clean wound under parental supervision"
            ],
            "correct_answer": "Swallowing strong painkillers without a prescription to cope with exam anxiety and get high",
            "explanation": "Drug abuse refers to taking chemical substances without medical need or prescription for non-healing purposes such as euphoria, stress escapism, or recreational intoxication, which damages physical and mental health."
        }
    },

    # ─── LESSON 4 ────────────────────────────────────────────────────────────
    {
        "unit_order": 4,
        "unit_name": "Soft Drugs vs. Hard Drugs: Side Effects and Consequences",
        "unit_description": "Examine the physiological, emotional, and social consequences of soft drugs (tobacco, alcohol, miraa) and hard narcotics (bhang, cocaine, heroin), analyzing Proverbs 23:29-35 and Ephesians 5:18.",
        "lesson_title": "Soft Drugs vs. Hard Drugs: Side Effects and Consequences",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/9/91/Anatomy_of_human_organs_and_health.jpg",
            "title": "Visual Hook: Human Physiology and the Vulnerability of Vital Organs",
            "author": "National Institute of Health Collection",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Anatomical rendering of the human brain, lungs, heart, and liver, highlighting the vital organs that suffer irreversible damage from drug and substance abuse."
        },
        "youtube": {
            "youtube_id": "75jZ7a29g6s",
            "title": "BibleProject: Wisdom & Self-Control",
            "description": "An insightful exploration of biblical temperance and self-control, highlighting how walking in divine wisdom protects individuals from self-destructive passions and addictions."
        },
        "svg_fn": get_svg_lesson_4,
        "goals": [
            "Analyze the toxic chemical components and biological effects of soft drugs (cigarettes, alcohol, miraa).",
            "Evaluate the devastating neurological, psychiatric, and lethal consequences of hard narcotics (bhang, cocaine, heroin).",
            "Assess the socioeconomic and familial destruction caused by addiction, applying Proverbs 23:29-35 and Ephesians 5:18."
        ],
        "intro": "Have you ever observed a package of cigarettes in a shop and noticed the bold warning printed across the cover: *'WARNING: SMOKING CAUSES LUNG CANCER AND EARLY DEATH'*? The government forces manufacturers to print these stark medical truths because the chemical evidence is indisputable. Yet, across the world, millions of people continue to purchase and smoke cigarettes daily.\n\nWhy do intelligent human beings willingly consume substances that destroy their lungs, shatter their nervous systems, drain their family finances, and lead to premature death? The Bible exposed this tragic deception thousands of years ago in Proverbs 23:32: *'In the end it bites like a snake and poisons like a viper.'* Today, we dismantle the myths surrounding soft and hard drugs.",
        "core_scripture": "### Scriptural Passages: Proverbs 23:29-35 & Ephesians 5:18\n\n> *\"Who has woe? Who has sorrow? Who has strife? Who has complaints? Who has needless bruises? Who has bloodshot eyes? Those who linger over wine, who go to sample bowls of mixed wine. Do not gaze at wine when it is red, when it sparkles in the cup, when it goes down smoothly! In the end it bites like a snake and poisons like a viper.\"* (Proverbs 23:29-32)\n\n> *\"Do not get drunk on wine, which leads to debauchery. Instead, be filled with the Spirit.\"* (Ephesians 5:18)",
        "theological_pillars": "### Theological Exegesis: The Destructive Deception of Intoxication\n\n1. **Biblical Diagnosis of Drunkenness (Proverbs 23:29-35):** Scripture vividly describes the physical, emotional, and social catastrophe of substance abuse: sorrow, strife, unprovoked violence, bloodshot eyes, hallucinations (*'your eyes will see strange sights'*), loss of physical equilibrium, and total chemical enslavement (*'When will I wake up so I can find another drink?'*).\n2. **The Command for Sobriety (Ephesians 5:18):** Intoxication leads directly to *asotia* (debauchery, recklessness, and moral ruin). Christians are commanded to be controlled and filled by the Holy Spirit rather than being controlled by intoxicating chemical substances.\n3. **Detailed Breakdown of Soft Drugs:**\n   - *Tobacco (Cigarettes):* Contains **Nicotine** (a violently addictive chemical that spikes blood pressure), **Tar** (a thick black carcinogen that lines the lungs causing throat and lung cancer), and **Carbon Monoxide** (deprives vital organs of oxygen, causing heart attacks and chronic bronchitis).\n   - *Alcohol:* A central nervous system depressant. Chronic consumption destroys brain cells, causes **Liver Cirrhosis** (fibrous scarring of the liver), induces stomach ulcers, and triggers impulsive behaviors leading to fatal road accidents, domestic violence, and unprotected sexual immorality (HIV transmission).\n   - *Miraa / Khat:* Contains cathine and cathinone. Chewing causes insomnia, dental decay, severe stomach ulcers, loss of appetite, hallucinations, irritability, and reproductive sterility.\n4. **Detailed Breakdown of Hard Drugs (Narcotics):**\n   - *Cannabis / Bhang / Marijuana:* Alters sensory perception of time and distance, causes permanent memory impairment, triggers acute paranoia, psychosis, and aggressive criminal violence.\n   - *Cocaine:* An intensely addictive stimulant that causes extreme cardiovascular strain, arterial spasms, respiratory failure, and sudden cardiac arrest.\n   - *Heroin:* A devastating opiate. Causes rapid, crippling physical dependence. Users often inject it using shared, unsterilized needles—drastically increasing HIV/Hepatitis transmission. Overdoses paralyze the brain's respiratory center, causing instant fatal asphyxiation.",
        "deep_dive": "### Deep Dive: The Social & Family Devastation of Substance Abuse\n\nSubstance abuse never affects the addict in isolation; it unleashes a catastrophic ripple effect across families and the wider community:\n\n- **Economic Ruin & Extreme Poverty:** Addicts squander family savings, sell household furniture, and accumulate massive debts to feed their chemical dependency, depriving children of school fees and nutritious food.\n- **Domestic Violence & Broken Homes:** Alcohol and drug-induced rage lead to spouse battering, emotional trauma, child neglect, marital separation, and divorce.\n- **Academic & Career Collapse:** Students abusing drugs experience chronic absenteeism, loss of cognitive focus, disciplinary suspensions, and permanent expulsion from school.",
        "practical": {
            "title": "Action Framework: Assertive Peer Resistance & Refusal Skills",
            "steps": [
                "Step 1: Recognize High-Risk Environments — Avoid unattended parties, dark alleys, unlicensed kiosks, or private gatherings where alcohol or drugs are present.",
                "Step 2: Practice Clear, Unapologetic Refusal — When offered drugs or alcohol, look the person in the eye and say firmly: 'No, I value my health, my brain, and my future too much to poison them.'",
                "Step 3: Provide an Instant Alternative — Suggest a healthy alternative immediately: 'Let's go grab a soda or play a game of football instead.'",
                "Step 4: Exit the Scene Decisively — If peers continue to mock, pressure, or insist, walk away without hesitation and report suspicious drug peddling to trusted teachers or parents.",
            ]
        },
        "kenyan_context": "### Kenyan Real-World Context: The Fight Against Illicit Brews & Narcotics\n\nIn Kenya, substance abuse poses a major national challenge. In Central and Western Kenya, illicit alcoholic brews (such as *chang'aa* and *busaa* adulterated with toxic methanol and battery acid) have caused blindness, organ failure, and deaths among hundreds of citizens. In the Coastal region (Mombasa, Malindi, Lamu), youth face severe heroin trafficking threats, leading to widespread addiction and HIV transmission. Understanding these realities empowers Junior Secondary learners to become ambassadors of sobriety.",
        "reflection": "Proverbs 23:31 warns: *'Do not gaze at wine when it is red, when it sparkles in the cup, when it goes down smoothly! In the end it bites like a snake.'* How does modern alcohol and cigarette advertising disguise the deadly poison of addiction behind glamorous music, models, and false promises of popularity?",
        "takeaways": [
            "Tobacco contains nicotine (addictive stimulant), tar (causes lung/throat cancer), and carbon monoxide.",
            "Alcohol causes liver cirrhosis, brain cell destruction, loss of judgment, road accidents, and family violence.",
            "Miraa (khat) leads to insomnia, dental decay, loss of appetite, irritability, and psychiatric disturbances.",
            "Hard narcotics (bhang, cocaine, heroin) cause severe mental psychosis, HIV transmission via needle-sharing, and fatal overdoses.",
            "Proverbs 23 and Ephesians 5:18 warn that drunkenness leads to debauchery, financial ruin, and moral destruction."
        ],
        "mcq": {
            "question": "Which toxic, carcinogenic chemical component found in tobacco smoke coats the respiratory lining and directly causes lung cancer?",
            "options": [
                "Nicotine",
                "Tar",
                "Caffeine",
                "Cathinone"
            ],
            "correct_answer": "Tar",
            "explanation": "Tar is the dark, sticky, carcinogenic residue produced by burning tobacco that settles in the lungs, destroying cilia and directly causing lung, mouth, and throat cancer. Nicotine is the chemical responsible for addiction."
        }
    },

    # ─── LESSON 5 ────────────────────────────────────────────────────────────
    {
        "unit_order": 5,
        "unit_name": "Causes and Remedies of Drug Abuse",
        "unit_description": "Analyze the social, psychological, and environmental causes of substance abuse, evaluate the collaborative remedies established by NACADA, schools, churches, and families, and apply 1 Corinthians 15:33 and 1 Peter 5:8.",
        "lesson_title": "Causes and Remedies of Drug Abuse",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/d/df/Counseling_and_psychological_support_session.jpg",
            "title": "Visual Hook: Professional Guidance, Counseling, and Rehabilitation",
            "author": "Wikimedia Commons Health Archive",
            "licensing": "Creative Commons Attribution-Share Alike",
            "source": "Wikimedia Commons",
            "caption": "A compassionate guidance and rehabilitation counseling session, illustrating the restorative care necessary to heal victims of substance abuse."
        },
        "youtube": {
            "youtube_id": "62ClWHXiuhg",
            "title": "BibleProject: Compassion & Restoration",
            "description": "An inspiring look at God's heart of mercy and restoration, discovering how the Christian community is called to extend healing, forgiveness, and rehabilitation to the broken."
        },
        "svg_fn": get_svg_lesson_5,
        "goals": [
            "Identify six primary psychological, social, economic, and media triggers that push adolescents into substance abuse.",
            "Evaluate the multifaceted national remedies championed by NACADA, schools, law enforcement, and Christian rehabilitation centers.",
            "Demonstrate peer pressure resistance skills and formulate compassionate Christian support mechanisms for addicted peers based on 1 Corinthians 15:33 and 1 Peter 5:8."
        ],
        "intro": "Have you ever observed a commercial billboard or television advertisement for an alcoholic drink? Notice how the actors are always depicted as exquisitely dressed, glowing with health, surrounded by laughing friends, driving sleek cars, and radiating success. Advertisers never show the horrifying reality: a person vomiting in a sewage ditch, a family home torn apart by domestic violence, or a young life cut short in a mangled road crash.\n\nSubstance abuse is fueled by clever deceptions, intense peer pressure, and emotional vulnerability. However, addiction is neither unbeatable nor irreversible. Today, we examine why young people fall into substance abuse and explore the powerful network of national, educational, spiritual, and medical remedies established to restore lives.",
        "core_scripture": "### Scriptural Passages: 1 Corinthians 15:33 & 1 Peter 5:8\n\n> *\"Do not be misled: 'Bad company corrupts good character.'\"* (1 Corinthians 15:33)\n\n> *\"Be alert and of sober mind. Your enemy the devil prowls around like a roaring lion looking for someone to devour. Resist him, standing firm in the faith.\"* (1 Peter 5:8)",
        "theological_pillars": "### Theological Exegesis: Vigilance, Companionship, and Restoration\n\n1. **The Law of Association (1 Corinthians 15:33):** Human character is profoundly shaped by friendship networks. When adolescents associate closely with peers who engage in substance abuse, mockery of authority, and immoral behavior, their moral defenses gradually erode. Choosing godly, sober companions is a critical spiritual shield.\n2. **The Mandate for Spiritual & Mental Sobriety (1 Peter 5:8):** Spiritual vigilance (*nēpsate*) requires a completely clear, unclouded mind. Intoxicating substances disable the prefrontal cortex, stripping away moral restraint and leaving the human soul vulnerable to spiritual destruction.\n3. **Primary Causes of Drug & Substance Abuse:**\n   - *Negative Peer Pressure:* The intense psychological craving to belong, fit in, or look 'mature' among friends.\n   - *Emotional Stress & Escapism:* Using drugs to temporarily numb the pain of academic failure, family breakdown, poverty, or emotional grief.\n   - *Idleness & Boredom:* Having excessive unstructured free time with no productive hobbies or duties.\n   - *Curiosity & Experimentation:* Wanting to 'taste' or test how chemicals feel, leading to instant biological addiction.\n   - *Deceptive Media & Role Models:* Emulating celebrity musicians and social media personalities who glamorize substance abuse.\n   - *Easy Availability:* Unscrupulous merchants and illegal brewing dens operating near residential areas and schools.\n4. **The Four-Sector Collaborative Remedial Network:**\n   - *1. Government & Law Enforcement (NACADA):* Anti-narcotics police seizing drug shipments, closing illegal bars, and public awareness campaigns via the toll-free helpline (1192).\n   - *2. Educational Institutions:* Integrating anti-drug education into the CBC curriculum and establishing proactive Guidance & Counseling departments.\n   - *3. The Church & Faith Community:* Preaching biblical holiness, providing pastoral counseling, and establishing compassionate rehabilitation centers.\n   - *4. Family & Community:* Parents modeling sober lifestyles, fostering open dialogue with children, and providing emotional warmth at home.",
        "deep_dive": "### Deep Dive: Rehabilitation vs. Criminalization — The Christian Compassionate Approach\n\nWhen a student or family member falls into substance addiction, how should society respond?\n\n- **Targeting the Peddlers (Justice):** The full force of the law must be directed against drug dealers, cartels, and illegal brewers who exploit vulnerable children for profit.\n- **Rehabilitating the Victim (Mercy & Healing):** The addict should not merely be discarded or condemned. Addiction is a complex physiological disease and spiritual trap. Medical detoxification, psychological cognitive therapy, and spiritual renewal in faith-based rehabilitation centres are required to restore their dignity.\n- **Community Reintegration:** Churches and schools must welcome recovered individuals without stigmatization, helping them rebuild their education, career, and spiritual walk.",
        "practical": {
            "title": "Action Framework: A Peer-Support & Early-Warning Intervention Plan",
            "steps": [
                "Step 1: Identify Early Warning Signs — Look out for sudden academic drop, withdrawal from friends, bloodshot eyes, extreme mood swings, and borrowing money secretively.",
                "Step 2: Intervene with Compassion — Approach the struggling friend privately without judgment: 'I care about you, and I notice you are struggling. Let us get help together.'",
                "Step 3: Connect with Trusted Counselors — Confide immediately in a school guidance counselor, chaplain, or trusted parent who can arrange professional support.",
                "Step 4: Surround Them with a Sober Circle — Invite them into active sports, church youth fellowship, and group study sessions to replace their toxic environment."
            ]
        },
        "kenyan_context": "### Kenyan Real-World Context: NACADA's National Mandate\n\nIn Kenya, the **National Authority for the Campaign Against Alcohol and Drug Abuse (NACADA)** is the principal state agency established under the Ministry of Interior. NACADA coordinates public education campaigns in schools, conducts national surveys, certifies rehabilitation centres, and operates the national toll-free helpline **1192**. Kenyan learners can utilize NACADA's educational literature and counseling resources to champion substance-free schools.",
        "reflection": "Reflect on 1 Peter 5:8: *'Be alert and of sober mind.'* When a classmate is secretly experimenting with substances due to family pain or exam anxiety, how can you act as a compassionate Christian ambassador—offering genuine friendship and connecting them to counseling rather than mocking or isolating them?",
        "takeaways": [
            "Substance abuse is triggered by negative peer pressure, emotional stress, idleness, curiosity, and misleading media advertisements.",
            "1 Corinthians 15:33 warns that bad company corrupts good character, emphasizing the necessity of choosing sober, upright friends.",
            "1 Peter 5:8 commands believers to remain sober-minded and vigilant against spiritual and moral traps.",
            "NACADA is Kenya's national authority leading the campaign against drug abuse through public education, policy enforcement, and helpline 1192.",
            "Holistic remedies require collaboration between government law enforcement, school guidance counseling, church rehabilitation, and warm family environments."
        ],
        "mcq": {
            "question": "What is the primary statutory mandate of the national organization known as NACADA in Kenya?",
            "options": [
                "To manufacture commercial alcoholic drinks and cigarettes for export",
                "To coordinate public education, research, policies, and campaigns against alcohol and drug abuse",
                "To arrest political leaders and manage national general elections",
                "To prescribe pharmaceutical medications directly to hospital patients"
            ],
            "correct_answer": "To coordinate public education, research, policies, and campaigns against alcohol and drug abuse",
            "explanation": "NACADA (National Authority for the Campaign Against Alcohol and Drug Abuse) is Kenya's official government agency mandated to coordinate public education campaigns, formulate policies, inspect rehabilitation centers, and lead national action against substance abuse."
        }
    },

    # ─── LESSON 6 ────────────────────────────────────────────────────────────
    {
        "unit_order": 6,
        "unit_name": "Christian Criteria for Evaluating Leisure",
        "unit_description": "Establish a comprehensive 7-point biblical checklist for evaluating recreation and entertainment, applying Philippians 4:8 and Romans 12:1-2 to make wise, sober, and edifying choices.",
        "lesson_title": "Christian Criteria for Evaluating Leisure",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Saint_Paul_Writing_His_Epistles_by_Valentin_de_Boulogne.jpg",
            "title": "Visual Hook: Discerning Divine Truth and Moral Excellence",
            "author": "Valentin de Boulogne (Museum of Fine Arts Collection)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "The Apostle Paul penning apostolic epistles by candlelight, calling believers to renew their minds and test all things against God's holy standard."
        },
        "youtube": {
            "youtube_id": "l9vn5UvsHvM",
            "title": "BibleProject: The Character of God & Holiness",
            "description": "A profound biblical study exploring God's holiness and how believers are called to cultivate moral purity, integrity, and godly discernment in every sphere of modern life."
        },
        "svg_fn": get_svg_lesson_6,
        "goals": [
            "Define the concept of moral criteria and explain why Christian teenagers need an objective standard for evaluating leisure.",
            "Compile and apply the 7-point Christian leisure checklist based on Philippians 4:8 and Romans 12:1-2.",
            "Critically evaluate contemporary media, digital gaming, music, and social recreation to make honorable, character-building choices."
        ],
        "intro": "Imagine walking into a grocery store to purchase fresh milk for your family. Before placing a carton in your shopping basket, you immediately examine the printed expiry date. If the date has passed and the milk has gone sour, you leave it on the shelf because you know drinking spoiled milk will cause severe stomach poisoning. You applied an objective standard—a **criterion**—to protect your physical health.\n\nIn the exact same way, we live in a world saturated with thousands of entertainment options, trending music albums, video games, movies, and social gatherings. Some are uplifting and refreshing, while others are laced with moral poison that corrupts the mind. How can a Christian teenager know what to embrace and what to reject? We need a spiritual checklist—a set of biblical criteria. Today, we construct this life-saving moral filter.",
        "core_scripture": "### Scriptural Passages: Philippians 4:8 & Romans 12:1-2\n\n> *\"Finally, brothers and sisters, whatever is true, whatever is noble, whatever is right, whatever is pure, whatever is lovely, whatever is admirable—if anything is excellent or praiseworthy—think about such things.\"* (Philippians 4:8)\n\n> *\"Do not conform to the pattern of this world, but be transformed by the renewing of your mind. Then you will be able to test and approve what God's will is—his good, pleasing and perfect will.\"* (Romans 12:2)",
        "theological_pillars": "### Theological Exegesis: The Philippians 4:8 Moral Filter & Mind Renewal\n\n1. **The Mind Renewal Mandate (Romans 12:1-2):** Believers must refuse to be squeezed into the mold of a secular, permissive culture (*'the pattern of this world'*). By allowing the Holy Spirit and the Word of God to renew their thinking, Christians develop spiritual discernment (*dokimazein*) to test, evaluate, and approve what is truly pleasing to God.\n2. **The Philippians 4:8 Moral Filter (The Eight Virtues):**\n   - *True:* Authentic, honest, and aligned with divine reality (not deceptive or manipulative).\n   - *Noble (Honorable):* Dignified, respectable, and elevating the human soul.\n   - *Right (Just):* Fair, lawful, and conforming to God's standard of justice.\n   - *Pure:* Morally clean, free from vulgarity, pornography, or sexual immorality.\n   - *Lovely:* Promoting grace, harmony, peace, and beauty rather than violence and hatred.\n   - *Admirable (Of Good Repute):* Commendable, inspiring positive testimony among believers and non-believers.\n   - *Excellent & Praiseworthy:* Operating at the highest ethical standard, bringing glory to God.\n3. **The 7-Point Christian Leisure Checklist:**\n   - *1. Does it promote human dignity?* (Avoids degrading or sexualizing human beings).\n   - *2. Does it serve God's ultimate purpose?* (Draws you closer to Christ and glorifies Him).\n   - *3. Does it come after work?* (A reward for diligence rather than an excuse for laziness; 1 Timothy 5:13, Ecclesiastes 10:18).\n   - *4. Is it harmless to physical and mental health?* (Free from toxic chemicals and reckless danger).\n   - *5. Does it avoid addiction and loss of self-control?* (Does not enslave the mind in compulsive behaviors).\n   - *6. Is it practiced in moderation?* (Does not consume excessive family money or displace essential chores; 1 Corinthians 10:23).\n   - *7. Is it lawful and morally pure?* (Complies with the laws of Kenya and the commandments of God).",
        "deep_dive": "### Deep Dive: Applying the Leisure Checklist to Music, Movies, and Gaming\n\nHow do we apply the 7-point checklist in real everyday situations?\n\n- **Evaluating Music & Lyrics:** Does the song celebrate violence, drug abuse, or sexual immorality? Even if the beat is catchy, toxic lyrics penetrate the subconscious mind. Choose music that inspires and honors God.\n- **Evaluating Video Games & Social Media:** Does the game reward killing, theft, and cruelty? Does social media scrolling make you envious, bitter, or anxious? Filter out toxic content.\n- **Evaluating Social Hangouts & Parties:** Will attending this party force you to compromise your Christian convictions regarding alcohol or modesty? If yes, decline courageously and suggest an edifying gathering with Christian friends.",
        "practical": {
            "title": "Action Framework: The Daily 4-Step Entertainment Filter",
            "steps": [
                "Step 1: Pause Before Consuming — Before downloading a music track, watching a movie, or joining a party, pause and run the 7-point checklist.",
                "Step 2: Ask the Three Core Questions — Is it pure? Is it edifying? Does it glorify Jesus Christ?",
                "Step 3: Delete & Replace Toxic Media — Immediately delete songs, video clips, and apps that fail the Philippians 4:8 standard, replacing them with edifying content.",
                "Step 4: Engage in Uplifting Fellowship — Form a recreation circle with sober, focused friends to enjoy hiking, sports, music, and community service together."
            ]
        },
        "kenyan_context": "### Kenyan Real-World Context: Digital Literacy & Moral Discernment\n\nIn Kenya, the Kenya Film Classification Board (KFCB) classifies media content to protect children from inappropriate materials (using ratings like GE, PG, 16, 18). However, on mobile phones and personal computers, the responsibility falls directly on the individual learner. Junior Secondary learners must cultivate internal moral conviction, using the Philippians 4:8 checklist to navigate digital spaces responsibly.",
        "reflection": "Reflect on Romans 12:2: *'Do not conform to the pattern of this world, but be transformed by the renewing of your mind.'* When you are tempted to watch vulgar entertainment or listen to profane music just because 'everyone else at school is doing it', how can the Holy Spirit empower you to stand firm in purity?",
        "takeaways": [
            "A criterion is an objective standard or principle used to evaluate and make moral choices.",
            "Philippians 4:8 provides the supreme biblical filter: whatever is true, noble, right, pure, lovely, admirable, excellent, and praiseworthy.",
            "Romans 12:1-2 calls believers to reject worldly conformity and experience continuous mind renewal through God's Word.",
            "Christian criteria require that leisure promotes dignity, glorifies God, comes after work, is harmless, avoids addiction, is moderate, and is lawful.",
            "Applying biblical criteria to music, movies, gaming, and parties guards the human soul from moral corruption and brings true joy."
        ],
        "mcq": {
            "question": "According to the 7-point Christian leisure checklist, which of the following entertainment choices passes the biblical standard of Philippians 4:8?",
            "options": [
                "Playing a violent video game that rewards players for stealing and shooting civilians",
                "Listening to music tracks that glorify drug trafficking, vulgarity, and drunkenness",
                "Participating in a school choir practice that develops musical talents and sings praise to God",
                "Spending the entire night betting on international sports matches instead of doing homework"
            ],
            "correct_answer": "Participating in a school choir practice that develops musical talents and sings praise to God",
            "explanation": "Choir practice develops God-given talents, fosters healthy teamwork, promotes praise to God, and edifies the mind, fully meeting the Philippians 4:8 standard of what is noble, pure, lovely, and praiseworthy."
        }
    }
]


# ─── INGESTION RUNNER ─────────────────────────────────────────────────────────

def ingest_grade9_cre_topic15():
    print("=" * 80)
    print("STARTING INGESTION: GRADE 9 CRE — TOPIC 15: LEISURE")
    print("=" * 80)

    with transaction.atomic():
        # 1. Resolve Target Hierarchy
        grade = Grade.objects.get(id=18)          # Grade 9
        curriculum = grade.curriculum
        subject = Subject.objects.get(id=50, grade=grade) # CRE

        print(f"[+] Target Hierarchy Verified: {curriculum.name} (ID: {curriculum.id}) -> {grade.name} (ID: {grade.id}) -> {subject.name} (ID: {subject.id})")

        # 2. Resolve / Create Topic 15
        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=15,
            defaults={
                "name": "Leisure",
                "description": "Examine the meaning and forms of leisure, proper use versus misuse, drug and substance abuse, side effects and consequences, remedies (NACADA), and Christian criteria for evaluating leisure."
            }
        )
        if not created and topic.name != "Leisure":
            topic.name = "Leisure"
            topic.description = "Examine the meaning and forms of leisure, proper use versus misuse, drug and substance abuse, side effects and consequences, remedies (NACADA), and Christian criteria for evaluating leisure."
            topic.save()

        print(f"[+] Target Topic  : Order {topic.order} — '{topic.name}' (ID: {topic.id})")

        # 3. Clean existing LearningUnits/Lessons under Topic 15 for idempotent ingestion
        existing_units = LearningUnit.objects.filter(topic=topic)
        print(f"[*] Found {existing_units.count()} existing Learning Units under Topic 15. Purging for clean ingestion...")
        for u in existing_units:
            for l in u.lessons.all():
                l.blocks.all().delete()
                l.assets.all().delete()
                l.delete()
            u.delete()

        # 4. Ingest all 6 Lessons
        total_units = 0
        total_lessons = 0
        total_pages = 0
        total_blocks = 0
        total_assets = 0

        for cfg in LESSONS_DATA:
            u_order = cfg["unit_order"]
            l_title = cfg["lesson_title"]
            l_desc = cfg["unit_description"]

            # Create LearningUnit
            unit = LearningUnit.objects.create(
                topic=topic,
                order=u_order,
                name=f"Unit {u_order}: {l_title}",
                description=clean_text(l_desc)
            )
            total_units += 1

            # Create Published Lesson
            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=clean_text(l_title),
                status="published",
                version=1,
                immutable_metadata={
                    "grade": "Grade 9",
                    "subject": "CRE",
                    "topic_order": 15,
                    "topic_name": topic.name,
                    "unit_order": u_order,
                    "author": "VLearn Grade 9 CRE Ingestion Engine",
                    "curriculum_framework": "CBC Kenya",
                    "enrichment_version": "v3_pedagogical"
                }
            )
            total_lessons += 1

            # ───────────────────────────────────────────────────────────────────
            # LESSON ASSETS (3 Assets: Image, Diagram, YouTube)
            # ───────────────────────────────────────────────────────────────────
            # Asset 1: Curated Wikimedia Visual Hook Image
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
            total_assets += 1

            # Asset 2: Pedagogical Vector SVG Diagram
            svg_content = cfg["svg_fn"]()
            svg_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="ai_generated",
                storage_type="url",
                status="attached",
                title=f"Diagram: {l_title}",
                description=f"Responsive pedagogical vector SVG diagram illustrating {l_title}.",
                url=f"https://vlearn.africa/assets/diagrams/cre/grade9_topic_15_lesson_{u_order}.svg",
                metadata={
                    "svg_xml": svg_content,
                    "viewBox": "0 0 800 450",
                    "theme": "#0f172a"
                }
            )
            total_assets += 1

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
            total_assets += 1

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
                title="Introduction & Familiar Connection",
                content={"markdown": clean_text(cfg["intro"])}
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 2 (Page 2): Scriptural Exegesis (2 blocks)
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
                order=40, component_order=1,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Scripture Passage",
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
                    "title": f"Pedagogical Blueprint: {l_title}",
                    "caption": f"Comprehensive architectural diagram illustrating {l_title}.",
                    "svg": svg_content,
                    "svg_xml": svg_content
                }
            )
            b5.assets.add(svg_asset)

            LessonBlock.objects.create(
                lesson=lesson, page_number=3, page_title="Pedagogical Diagram & Deep Dive",
                order=60, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Theological Deep Dive",
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
                title="Kenyan Real-World Context & Integration",
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
                title="Spiritual Reflection & Values",
                content={"markdown": clean_text(cfg["reflection"])}
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 6 (Page 6): Mastery Check (2 blocks)
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=6, page_title="Mastery Check",
                order=100, component_order=1,
                block_type="summary", component_type="summary",
                title="Summary & Key Takeaways",
                content={
                    "title": f"Key Takeaways: {l_title}",
                    "takeaways": clean_dict(cfg["takeaways"])
                }
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=6, page_title="Mastery Check",
                order=110, component_order=2,
                block_type="knowledge_check", component_type="knowledge_check",
                title="Mastery Knowledge Check",
                content=clean_dict(cfg["mcq"])
            )

            total_pages += 6
            total_blocks += 13
            print(f"  [+] Ingested Lesson {u_order:02d}/6: '{l_title}' (6 cards/pages, 13 blocks, 3 LessonAssets)")

        print("=" * 80)
        print("INGESTION SUMMARY FOR GRADE 9 CRE TOPIC 15:")
        print(f"  - Curriculum       : {curriculum.name} (ID: {curriculum.id})")
        print(f"  - Grade            : {grade.name} (ID: {grade.id}, Level: {grade.level})")
        print(f"  - Subject          : {subject.name} (ID: {subject.id})")
        print(f"  - Topic            : Order {topic.order} — {topic.name} (ID: {topic.id})")
        print(f"  - Learning Units   : {total_units}")
        print(f"  - Published Lessons: {total_lessons}")
        print(f"  - Total Pages/Cards: {total_pages}")
        print(f"  - Total Blocks     : {total_blocks}")
        print(f"  - Total Assets     : {total_assets}")
        print("=" * 80)


if __name__ == "__main__":
    ingest_grade9_cre_topic15()
