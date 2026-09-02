"""
VLearn CBC Grade 9 CRE — Topic 16: Wealth, Money and Poverty
Production-Ready Ingestion & Visual Enrichment Engine

Curriculum: CBC
Grade: Grade 9 (ID: 18)
Subject: CRE (ID: 50)
Topic: Topic 16: Wealth, Money and Poverty (Order: 16)

8 Discrete Units / Published Lessons:
  1. Lesson 1: Understanding Wealth, Money, and Poverty (Deuteronomy 8:17-18, 1 Timothy 6:10)
  2. Lesson 2: Traditional African Understanding of Wealth and Poverty
  3. Lesson 3: The Impact of the Money Economy
  4. Lesson 4: Christian Teachings on Wealth and Stewardship (Luke 12:15-21, Matthew 6:19-24)
  5. Lesson 5: Christian Teachings on Poverty and Sharing (Luke 16:19-31, 2 Corinthians 8:1-9)
  6. Lesson 6: Ethical Wealth Acquisition and Jua Kali Business Projects (Proverbs 13:11, Proverbs 28:19)
  7. Lesson 7: Financial Integrity: Fighting Corruption and Bribery (Exodus 23:8, Micah 6:10-12, EACC)
  8. Lesson 8: Core Life Skills and Christian Values for Financial Stewardship (Proverbs 21:5, Ecclesiastes 11:1-2)

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
    # Strip bracket citations e.g. [1], [223], [1, 2], [72, 238]
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Strip internal pedagogical tags
    text = re.sub(r'\[(VISUAL|BIBLE PASSAGE|BIBLE REFERENCE|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|REAL WORLD APPLICATION|BIBLICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|REFLECTION|BIBLE VERSE|TRADITIONAL PROVERB)[^\]]*\]', '', text, flags=re.IGNORECASE)
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


# ─── 8 CUSTOM RESPONSIVE VECTOR SVGS (viewBox="0 0 800 450", #0f172a theme) ─────

def get_svg_lesson_1():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="gold1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg1)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">PHYSICAL &amp; ECONOMIC QUALITIES OF LEGAL TENDER</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Foundations of Money, World Currencies, and Stewardship of Legal Mediums of Exchange</text>

  <!-- 6 Bento Grid Squares for Qualities of Money -->
  <!-- 1. Durability -->
  <g transform="translate(40, 95)">
    <rect width="225" height="125" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="15" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700">1. DURABILITY</text>
    <text x="15" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Withstands continuous wear,</text>
    <text x="15" y="68" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">tear, folding, and moisture</text>
    <text x="15" y="84" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">without disintegrating.</text>
    <rect x="15" y="98" width="195" height="18" rx="4" fill="#0f172a"/>
    <text x="112" y="111" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Tough linen/cotton paper &amp; coins</text>
  </g>

  <!-- 2. Portability -->
  <g transform="translate(285, 95)">
    <rect width="230" height="125" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="15" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700">2. PORTABILITY</text>
    <text x="15" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Lightweight and compact,</text>
    <text x="15" y="68" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">making it easy to carry in</text>
    <text x="15" y="84" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">wallets, pockets, or purses.</text>
    <rect x="15" y="98" width="200" height="18" rx="4" fill="#0f172a"/>
    <text x="115" y="111" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Convenient daily mobility</text>
  </g>

  <!-- 3. Divisibility -->
  <g transform="translate(535, 95)">
    <rect width="225" height="125" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="15" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700">3. DIVISIBILITY</text>
    <text x="15" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Easily split into small units</text>
    <text x="15" y="68" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">(10, 20, 50, 100, 1000 Ksh)</text>
    <text x="15" y="84" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">for precise transactions.</text>
    <rect x="15" y="98" width="195" height="18" rx="4" fill="#0f172a"/>
    <text x="112" y="111" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Facilitates small &amp; large trade</text>
  </g>

  <!-- 4. Scarcity -->
  <g transform="translate(40, 235)">
    <rect width="225" height="125" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="15" y="28" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="700">4. SCARCITY</text>
    <text x="15" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Tightly regulated supply</text>
    <text x="15" y="68" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">by the Central Bank of Kenya</text>
    <text x="15" y="84" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">to curb runaway inflation.</text>
    <rect x="15" y="98" width="195" height="18" rx="4" fill="#0f172a"/>
    <text x="112" y="111" fill="#fde68a" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Central monetary control</text>
  </g>

  <!-- 5. Acceptability -->
  <g transform="translate(285, 235)">
    <rect width="230" height="125" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="15" y="28" fill="#34d399" font-family="system-ui, sans-serif" font-size="13" font-weight="700">5. ACCEPTABILITY</text>
    <text x="15" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Universally recognized and</text>
    <text x="15" y="68" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">trusted by law across the nation</text>
    <text x="15" y="84" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">to settle any debt or trade.</text>
    <rect x="15" y="98" width="200" height="18" rx="4" fill="#0f172a"/>
    <text x="115" y="111" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Legal tender by statutory decree</text>
  </g>

  <!-- 6. Stability of Value -->
  <g transform="translate(535, 235)">
    <rect width="225" height="125" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <text x="15" y="28" fill="#c084fc" font-family="system-ui, sans-serif" font-size="13" font-weight="700">6. STABILITY</text>
    <text x="15" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Purchasing power remains</text>
    <text x="15" y="68" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">predictable over time, making</text>
    <text x="15" y="84" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">saving and budgeting viable.</text>
    <rect x="15" y="98" width="195" height="18" rx="4" fill="#0f172a"/>
    <text x="112" y="111" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Reliable store of future value</text>
  </g>

  <rect x="150" y="380" width="500" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="401" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">"The earth is the Lord's, and everything in it" (Psalm 24:1) — God Owns, We Steward</text>
</svg>"""


def get_svg_lesson_2():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="africanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg2)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">TRADITIONAL AFRICAN WEALTH &amp; COMMUNAL SOLIDARITY</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Livestock, Land, Granaries, and Interdependent Community Safety Nets</text>

  <!-- Central Hub: Communal Wealth Structure -->
  <circle cx="400" cy="225" r="58" fill="url(#africanGrad)" stroke="#fde68a" stroke-width="2"/>
  <text x="400" y="218" fill="#0f172a" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">COMMUNAL</text>
  <text x="400" y="234" fill="#0f172a" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">SOLIDARITY</text>
  <text x="400" y="248" fill="#1e293b" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">"I am because we are"</text>

  <!-- 4 Surrounding Pillars -->
  <!-- 1. Livestock & Granaries -->
  <line x1="350" y1="185" x2="220" y2="135" stroke="#f59e0b" stroke-width="2"/>
  <g transform="translate(30, 95)">
    <rect width="210" height="90" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="15" y="24" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">1. Tangible Indicators</text>
    <text x="15" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Cattle, goats, sheep herds</text>
    <text x="15" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Full granaries of grain</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Large family / labor force</text>
  </g>

  <!-- 2. Barter Trade & Sharing -->
  <line x1="450" y1="185" x2="580" y2="135" stroke="#f59e0b" stroke-width="2"/>
  <g transform="translate(560, 95)">
    <rect width="210" height="90" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="15" y="24" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">2. Exchange &amp; Mutual Aid</text>
    <text x="15" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Direct barter trade</text>
    <text x="15" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Communal food during famine</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Shared grazing &amp; water holes</text>
  </g>

  <!-- 3. Condemnation of Laziness -->
  <line x1="350" y1="265" x2="220" y2="310" stroke="#f59e0b" stroke-width="2"/>
  <g transform="translate(30, 270)">
    <rect width="210" height="90" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="15" y="24" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="700">3. Rejection of Laziness</text>
    <text x="15" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Idleness rebuked in proverbs</text>
    <text x="15" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• "A lazy person shall not eat"</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Hard work yields blessing</text>
  </g>

  <!-- 4. Communal Safety Nets -->
  <line x1="450" y1="265" x2="580" y2="310" stroke="#f59e0b" stroke-width="2"/>
  <g transform="translate(560, 270)">
    <rect width="210" height="90" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="15" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">4. Social Protection</text>
    <text x="15" y="44" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Care for widows &amp; orphans</text>
    <text x="15" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Loaning milking cows</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Collective harvesting labor</text>
  </g>

  <rect x="160" y="380" width="480" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="401" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Wealth Without Generosity Was Regarded as Moral Failure in Traditional Africa</text>
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

  <text x="400" y="42" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE SOCIO-ECONOMIC TRANSITION: TRADITIONAL TO MONEY ECONOMY</text>
  <text x="400" y="64" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Colonial Taxation, Wage-Labor, Rural-Urban Migration, and Shifting Cultural Values</text>

  <!-- Left: Traditional Barter Economy -->
  <g transform="translate(40, 85)">
    <rect width="335" height="280" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="335" height="34" rx="10" fill="#059669"/>
    <text x="167" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">TRADITIONAL COMMUNAL SYSTEM</text>
    <text x="15" y="60" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Mode of Exchange:</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Barter trade of goods, livestock, and produce.</text>
    <text x="15" y="104" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Land Ownership:</text>
    <text x="15" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Communal ancestral land held in trust for all.</text>
    <text x="15" y="148" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Social Cohesion:</text>
    <text x="15" y="164" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Extended families living in village solidarity.</text>
    <text x="15" y="192" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Bride Wealth Role:</text>
    <text x="15" y="208" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Tokens of friendship uniting clans (cattle/goats).</text>
    <rect x="15" y="236" width="305" height="24" rx="4" fill="#0f172a"/>
    <text x="167" y="252" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Focus: Communal Well-being &amp; Solidarity</text>
  </g>

  <!-- Right: Modern Cash Economy -->
  <g transform="translate(425, 85)">
    <rect width="335" height="280" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="335" height="34" rx="10" fill="#d97706"/>
    <text x="167" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">MODERN CASH &amp; WAGE ECONOMY</text>
    <text x="15" y="60" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Mode of Exchange:</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Currency, banknotes, coins, and digital payments.</text>
    <text x="15" y="104" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Land &amp; Labor:</text>
    <text x="15" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Individual title deeds; wage-labor exploitation.</text>
    <text x="15" y="148" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Social Strain:</text>
    <text x="15" y="164" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Rural-urban migration; rise of urban slums.</text>
    <text x="15" y="192" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Modern Challenges:</text>
    <text x="15" y="208" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Individualistic greed, corruption, and rich-poor divide.</text>
    <rect x="15" y="236" width="305" height="24" rx="4" fill="#0f172a"/>
    <text x="167" y="252" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Challenge: Individualism vs Moral Responsibility</text>
  </g>

  <rect x="160" y="380" width="480" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="401" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">"Life does not consist in an abundance of possessions" (Luke 12:15)</text>
</svg>"""


def get_svg_lesson_4():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="stewardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg4)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE CHRISTIAN STEWARDSHIP CYCLE</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Deuteronomy 8:18, Luke 12:15-21, and Matthew 6:19-24 — Transforming Resources into Eternal Glory</text>

  <!-- Central Hub: God the Sole Owner -->
  <circle cx="400" cy="225" r="54" fill="url(#stewardGrad)" stroke="#38bdf8" stroke-width="2"/>
  <text x="400" y="218" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">GOD THE</text>
  <text x="400" y="234" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">OWNER</text>
  <text x="400" y="248" fill="#bae6fd" font-family="system-ui, sans-serif" font-size="9" font-weight="600" text-anchor="middle">Source of all ability</text>

  <!-- Node 1: Human Steward (Top) -->
  <line x1="400" y1="171" x2="400" y2="128" stroke="#38bdf8" stroke-width="2"/>
  <g transform="translate(285, 85)">
    <rect width="230" height="42" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="115" y="26" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. Human Steward (Manager)</text>
  </g>

  <!-- Node 2: Ethical Production (Right) -->
  <line x1="454" y1="210" x2="570" y2="175" stroke="#38bdf8" stroke-width="2"/>
  <g transform="translate(560, 155)">
    <rect width="210" height="42" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="105" y="26" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. Honest Wealth Creation</text>
  </g>

  <!-- Node 3: Worship & Tithe (Bottom Right) -->
  <line x1="445" y1="255" x2="560" y2="295" stroke="#38bdf8" stroke-width="2"/>
  <g transform="translate(550, 275)">
    <rect width="220" height="42" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="110" y="26" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. Tithe &amp; Honor to God</text>
  </g>

  <!-- Node 4: Charity & Sharing (Bottom Left) -->
  <line x1="355" y1="255" x2="240" y2="295" stroke="#38bdf8" stroke-width="2"/>
  <g transform="translate(30, 275)">
    <rect width="220" height="42" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <text x="110" y="26" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">4. Almsgiving to Needy</text>
  </g>

  <!-- Node 5: Eternal Treasure (Top Left) -->
  <line x1="346" y1="210" x2="230" y2="175" stroke="#38bdf8" stroke-width="2"/>
  <g transform="translate(30, 155)">
    <rect width="210" height="42" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="105" y="26" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">5. Eternal Heavenly Riches</text>
  </g>

  <rect x="150" y="380" width="500" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="401" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">"Remember the Lord your God, for it is He who gives you ability to produce wealth" (Deut 8:18)</text>
</svg>"""


def get_svg_lesson_5():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg5)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE CHRISTIAN COMPASSION MATRIX: POVERTY &amp; SHARING</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Luke 16:19-31, 2 Corinthians 8:1-9, Luke 3:11, and Matthew 25:34-40</text>

  <!-- 3 Pillar Columns -->
  <g transform="translate(40, 95)">
    <rect width="220" height="270" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#0284c7"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. SYSTEMIC POVERTY</text>
    <text x="15" y="60" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Injustices &amp; Calamities</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Droughts, floods, civil war,</text>
    <text x="15" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">and lack of school infrastructure.</text>
    <text x="15" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Not Always a Curse</text>
    <text x="15" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Jesus rejected the myth that all</text>
    <text x="15" y="152" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">poor people are cursed for sin.</text>
    <text x="15" y="180" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• God's Defense of Poor</text>
    <text x="15" y="198" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">God is the protector of the</text>
    <text x="15" y="212" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">orphan, widow, and immigrant.</text>
  </g>

  <g transform="translate(290, 95)">
    <rect width="220" height="270" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#d97706"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. THE DANGER OF GREED</text>
    <text x="15" y="60" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Rich Man &amp; Lazarus</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">The rich man ignored Lazarus</text>
    <text x="15" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">suffering outside his gate.</text>
    <text x="15" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Sin of Omission</text>
    <text x="15" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Condemned not for wealth, but</text>
    <text x="15" y="152" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">for callous indifference.</text>
    <text x="15" y="180" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Eternal Judgment</text>
    <text x="15" y="198" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Earthly comfort cannot buy</text>
    <text x="15" y="212" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">salvation in eternity.</text>
  </g>

  <g transform="translate(540, 95)">
    <rect width="220" height="270" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#059669"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. THE SHARING MANDATE</text>
    <text x="15" y="60" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• John the Baptist's Call</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">"Anyone who has two tunics</text>
    <text x="15" y="92" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">must share with who has none."</text>
    <text x="15" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Macedonian Example</text>
    <text x="15" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Gave generously out of severe</text>
    <text x="15" y="152" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">trials and extreme poverty.</text>
    <text x="15" y="180" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Serving Christ in Least</text>
    <text x="15" y="198" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">"Whatever you did for the</text>
    <text x="15" y="212" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">least of these, you did for Me."</text>
  </g>

  <rect x="150" y="380" width="500" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="401" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">True Christian Worship is Expressed Through Practical Compassion for the Poor</text>
</svg>"""


def get_svg_lesson_6():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg6)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="44" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">TEEN ENTREPRENEURSHIP: JUA KALI &amp; BUSINESS LIFECYCLE</text>
  <text x="400" y="66" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Proverbs 13:11, Proverbs 28:19 — Diligence, Manual Skills, and Financial Literacy</text>

  <!-- 6 Step Process Flowchart -->
  <!-- Step 1 -->
  <g transform="translate(40, 95)">
    <rect width="225" height="120" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="15" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">1. Problem &amp; Idea</text>
    <text x="15" y="46" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Identify community needs.</text>
    <text x="15" y="62" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Select low-cost idea: poultry,</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">vegetables, crafts, tutoring.</text>
    <rect x="15" y="92" width="195" height="18" rx="4" fill="#0f172a"/>
    <text x="112" y="105" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Market Opportunity</text>
  </g>

  <!-- Step 2 -->
  <g transform="translate(285, 95)">
    <rect width="230" height="120" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="15" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">2. Pitch &amp; Mobilize Capital</text>
    <text x="15" y="46" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Pitch plan to parents or</text>
    <text x="15" y="62" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">CRE teacher for mentorship</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">and small seed capital.</text>
    <rect x="15" y="92" width="200" height="18" rx="4" fill="#0f172a"/>
    <text x="115" y="105" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Seed Capital &amp; Guidance</text>
  </g>

  <!-- Step 3 -->
  <g transform="translate(535, 95)">
    <rect width="225" height="120" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="15" y="24" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">3. Launch Venture</text>
    <text x="15" y="46" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Procure quality materials</text>
    <text x="15" y="62" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">honestly and begin production</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">with excellent craftsmanship.</text>
    <rect x="15" y="92" width="195" height="18" rx="4" fill="#0f172a"/>
    <text x="112" y="105" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Ethical Production</text>
  </g>

  <!-- Step 4 -->
  <g transform="translate(40, 235)">
    <rect width="225" height="120" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="15" y="24" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">4. Progress Journal</text>
    <text x="15" y="46" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Record every shilling:</text>
    <text x="15" y="62" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">daily sales, raw material costs,</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">and customer feedback.</text>
    <rect x="15" y="92" width="195" height="18" rx="4" fill="#0f172a"/>
    <text x="112" y="105" fill="#fde68a" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Financial Recordkeeping</text>
  </g>

  <!-- Step 5 -->
  <g transform="translate(285, 235)">
    <rect width="230" height="120" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <text x="15" y="24" fill="#c084fc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">5. Performance Review</text>
    <text x="15" y="46" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Calculate net profit or loss;</text>
    <text x="15" y="62" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">report monthly metrics to</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">parents and teachers.</text>
    <rect x="15" y="92" width="200" height="18" rx="4" fill="#0f172a"/>
    <text x="115" y="105" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Accountability &amp; Metrics</text>
  </g>

  <!-- Step 6 -->
  <g transform="translate(535, 235)">
    <rect width="225" height="120" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="15" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">6. Reinvest &amp; Scale</text>
    <text x="15" y="46" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Reinvest profits wisely;</text>
    <text x="15" y="62" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">expand enterprise and tithe</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">as faithful stewards.</text>
    <rect x="15" y="92" width="195" height="18" rx="4" fill="#0f172a"/>
    <text x="112" y="105" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Sustainable Business Growth</text>
  </g>

  <rect x="150" y="380" width="500" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="401" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">"Dishonest money dwindles away, but whoever gathers money little by little makes it grow" (Prov 13:11)</text>
</svg>"""


def get_svg_lesson_7():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg7)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">FINANCIAL INTEGRITY MATRIX: COMBATING CORRUPTION &amp; BRIBERY</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Exodus 23:8, Micah 6:10-12, Luke 3:12-14, and the Role of Kenya's EACC</text>

  <!-- Table Header -->
  <rect x="40" y="90" width="180" height="30" rx="4" fill="#334155"/>
  <text x="130" y="110" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">DIMENSION</text>

  <rect x="230" y="90" width="260" height="30" rx="4" fill="#dc2626"/>
  <text x="360" y="110" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">CORRUPT PRACTICE / BRIBERY</text>

  <rect x="500" y="90" width="260" height="30" rx="4" fill="#059669"/>
  <text x="630" y="110" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">CHRISTIAN INTEGRITY / EACC</text>

  <!-- Row 1: Judicial & Decision Making -->
  <g transform="translate(40, 128)">
    <rect width="180" height="45" rx="4" fill="#1e293b"/>
    <text x="15" y="27" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. Judicial Fairness</text>
    <rect x="190" y="0" width="260" height="45" rx="4" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    <text x="200" y="27" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Bribes blind the eyes &amp; twist justice</text>
    <rect x="460" y="0" width="260" height="45" rx="4" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
    <text x="470" y="27" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Impartial justice; refusing kickbacks</text>
  </g>

  <!-- Row 2: Public Services & Contracts -->
  <g transform="translate(40, 180)">
    <rect width="180" height="45" rx="4" fill="#1e293b"/>
    <text x="15" y="27" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. Public Services</text>
    <rect x="190" y="0" width="260" height="45" rx="4" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    <text x="200" y="27" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Broken roads, collapsed buildings</text>
    <rect x="460" y="0" width="260" height="45" rx="4" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
    <text x="470" y="27" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Transparent bidding &amp; quality delivery</text>
  </g>

  <!-- Row 3: Treatment of the Poor -->
  <g transform="translate(40, 232)">
    <rect width="180" height="45" rx="4" fill="#1e293b"/>
    <text x="15" y="27" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Social Equity</text>
    <rect x="190" y="0" width="260" height="45" rx="4" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    <text x="200" y="27" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Poor denied basic medical care &amp; water</text>
    <rect x="460" y="0" width="260" height="45" rx="4" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
    <text x="470" y="27" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Equal protection under the law for all</text>
  </g>

  <!-- Row 4: Personal Character -->
  <g transform="translate(40, 284)">
    <rect width="180" height="45" rx="4" fill="#1e293b"/>
    <text x="15" y="27" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">4. School &amp; Youth</text>
    <rect x="190" y="0" width="260" height="45" rx="4" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    <text x="200" y="27" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Exam cheating, bribing prefects</text>
    <rect x="460" y="0" width="260" height="45" rx="4" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
    <text x="470" y="27" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Academic honesty &amp; moral courage</text>
  </g>

  <rect x="150" y="380" width="500" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="401" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">"Do not accept a bribe, for a bribe blinds those who see and twists innocent words" (Exodus 23:8)</text>
</svg>"""


def get_svg_lesson_8():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg8" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg8)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE INTEGRITY BACKPACK: LIFE SKILLS &amp; CHRISTIAN VALUES</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Equipping Youth for Lifelong Ethical Financial Stewardship and Wise Decision-Making</text>

  <!-- Left: 5 Core Life Skills -->
  <g transform="translate(40, 95)">
    <rect width="335" height="270" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="335" height="34" rx="10" fill="#0284c7"/>
    <text x="167" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">5 CORE LIFE SKILLS</text>
    <text x="15" y="60" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. Decision-Making:</text>
    <text x="15" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">8-step systematic ethical evaluation.</text>
    <text x="15" y="98" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. Critical Thinking:</text>
    <text x="15" y="112" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Analyzing 'quick-money' pyramid traps.</text>
    <text x="15" y="136" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Creative Thinking:</text>
    <text x="15" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Developing novel Jua Kali solutions.</text>
    <text x="15" y="174" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">4. Self-Esteem:</text>
    <text x="15" y="188" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Valuing dignity over illicit cash offers.</text>
    <text x="15" y="212" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">5. Assertiveness:</text>
    <text x="15" y="226" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Firmly saying NO to bribery &amp; crime.</text>
    <rect x="15" y="238" width="305" height="20" rx="4" fill="#0f172a"/>
    <text x="167" y="252" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">Adaptive Skills for Daily Challenges</text>
  </g>

  <!-- Right: 10 Christian Values -->
  <g transform="translate(425, 95)">
    <rect width="335" height="270" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="335" height="34" rx="10" fill="#d97706"/>
    <text x="167" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">10 CHRISTIAN VALUES</text>
    <text x="15" y="58" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Love &amp; Compassion</text>
    <text x="175" y="58" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Honesty in Trade</text>
    <text x="15" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Caring for the needy</text>
    <text x="175" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Truth in all transactions</text>

    <text x="15" y="98" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Reliability / Trust</text>
    <text x="175" y="98" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Fairness &amp; Equity</text>
    <text x="15" y="116" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Keeping business promises</text>
    <text x="175" y="116" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Equal treatment for all</text>

    <text x="15" y="138" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Economic Justice</text>
    <text x="175" y="138" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Respect for Property</text>
    <text x="15" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Fair wages &amp; ethical policy</text>
    <text x="175" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Guarding public goods</text>

    <text x="15" y="178" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Faithfulness</text>
    <text x="175" y="178" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Humility in Riches</text>
    <text x="15" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Loyal resource stewardship</text>
    <text x="175" y="196" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Never boasting in wealth</text>

    <text x="15" y="218" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Persistence &amp; Grit</text>
    <text x="175" y="218" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Chastity / Purity</text>
    <text x="15" y="234" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Persevering through setbacks</text>
    <text x="175" y="234" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Rejecting bodily trade</text>
    <rect x="15" y="244" width="305" height="16" rx="4" fill="#0f172a"/>
    <text x="167" y="256" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Spiritual Compass for Ethical Living</text>
  </g>

  <rect x="150" y="380" width="500" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="401" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">"Trust in the Lord with all your heart, and lean not on your own understanding" (Proverbs 3:5)</text>
</svg>"""


# ─── LESSON DATA CONFIGURATIONS (8 LESSONS) ───────────────────────────────────

LESSONS_DATA = [
    # ─── LESSON 1 ────────────────────────────────────────────────────────────
    {
        "unit_order": 1,
        "unit_name": "Understanding Wealth, Money, and Poverty",
        "unit_description": "Define wealth, money, and poverty, explore world currencies, analyze the physical qualities of legal tender, and examine biblical stewardship from Psalm 24:1 and Haggai 2:8.",
        "lesson_title": "Understanding Wealth, Money, and Poverty",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/8/82/Central_Bank_of_Kenya_building.jpg",
            "title": "Visual Hook: Central Bank of Kenya and Legal Tender",
            "author": "Wikimedia Commons Contributor",
            "licensing": "Creative Commons Attribution-Share Alike",
            "source": "Wikimedia Commons",
            "caption": "The Central Bank of Kenya in Nairobi, responsible for issuing legal tender, regulating currency supply, and safeguarding monetary stability."
        },
        "youtube": {
            "youtube_id": "bT4O58n4954",
            "title": "BibleProject: Gospel & Money",
            "description": "An insightful exploration of how biblical narrative reframes money, possessions, and true spiritual wealth from the perspective of God's kingdom."
        },
        "svg_fn": get_svg_lesson_1,
        "goals": [
            "Define the foundational economic and ethical terms: wealth, money, poverty, currency, and legal tender.",
            "Analyze the six essential physical and economic qualities of good legal tender (durability, portability, divisibility, scarcity, acceptability, and stability).",
            "Evaluate the biblical principle of divine ownership and human stewardship based on Psalm 24:1 and Haggai 2:8."
        ],
        "intro": "Have you ever held a crisp, clean Kenyan hundred or thousand-shilling bank note in your hand? On it, you will observe intricate security threads, national landmarks, watermarks, and the authoritative signature of the Governor of the Central Bank of Kenya.\n\nWhy does a small piece of specially manufactured paper possess the power to buy food, purchase school books, build houses, or settle debts? What truly makes a human being 'rich' or 'poor'? In Christian ethics, we must understand the objective, physical, and moral nature of money before we can manage it with righteous stewardship.",
        "core_scripture": "### Scriptural Foundations: Psalm 24:1 & Haggai 2:8\n\n> *\"The earth is the Lord's, and everything in it, the world, and all who live in it; for he founded it on the seas and established it on the waters.\"* (Psalm 24:1-2)\n\n> *\"'The silver is mine and the gold is mine,' declares the Lord Almighty.\"* (Haggai 2:8)\n\n> *\"For the love of money is a root of all kinds of evil. Some people, eager for money, have wandered from the faith and pierced themselves with many griefs.\"* (1 Timothy 6:10)",
        "theological_pillars": "### Theological & Economic Exegesis\n\n1. **Core Economic Definitions:**\n   - **Wealth:** The accumulation of material possessions, property, livestock, land, and financial assets that have measurable economic value.\n   - **Money:** Any standardized item or verifiable record generally accepted as payment for goods, services, and repayment of debts.\n   - **Poverty:** The condition of lacking basic human necessities, including safe nutrition, potable water, adequate shelter, healthcare, and educational opportunity.\n   - **Legal Tender:** Currency officially declared by national statutory law to be valid for meeting a financial obligation.\n   - **Currency:** The specific monetary system in common use within a sovereign nation (e.g., Kenyan Shilling [Ksh], US Dollar [$], British Pound [£], Euro [€], South African Rand [ZAR]).\n\n2. **Six Essential Qualities of Legal Tender:**\n   - **Durability:** Material resilience against tearing, moisture, and friction under repeated circulation.\n   - **Portability:** Lightweight convenience enabling easy transit in wallets or pockets.\n   - **Divisibility:** Capacity to be split into standardized denominations (e.g., Ksh 1, 5, 10, 20, 50, 100, 200, 500, 1000) for exact payments.\n   - **Scarcity:** Regulated supply strictly managed by the Central Bank to prevent devaluation and hyperinflation.\n   - **Acceptability:** Universal societal trust and statutory backing ensuring widespread adoption.\n   - **Stability of Value:** Predictable purchasing power that facilitates saving and financial planning.\n\n3. **The Principle of Ultimate Divine Ownership:** Psalm 24:1 establishes that God is the absolute creator and owner of all earthly assets. Humans are never sovereign owners; we are temporary managers accountable to the Creator.",
        "deep_dive": "### Deep Dive: The Moral Neutrality of Money vs The Spiritual Danger of Greed\n\nIs money itself evil? Scripture clarifies that money is a morally neutral instrument of exchange. It is the *love of money* (*philarguria* in Greek)—an obsession with accumulating wealth for selfish pride and security—that becomes a destructive root of spiritual decay (1 Timothy 6:10).\n\n- **Instrument of Blessing:** When money is earned ethically and managed under God's guidance, it builds hospitals, feeds the hungry, supports families, and expands community welfare.\n- **Modern Idolatry:** When money becomes an object of worship (*Mammon*), it displaces God, blinds human empathy, and fuels exploitation and crime.",
        "practical": {
            "title": "Action Framework: Respecting Legal Tender and Practicing Early Stewardship",
            "steps": [
                "Step 1: Treat National Currency with Dignity — Never deface, tear, write on, or crumple Kenyan banknotes; handle them cleanly in a purse or savings wallet.",
                "Step 2: Track Personal Pocket Money — Keep a simple ledger recording every shilling received and spent during the school term.",
                "Step 3: Establish a Personal Savings Habit — Dedicate a portion of any gift or earned money into a secure savings container or youth account.",
                "Step 4: Practice Proactive Sharing — Dedicate a small portion of your resources to help a classmate who lacks stationery or basic provisions."
            ]
        },
        "kenyan_context": "In Kenya, the Central Bank of Kenya (CBK) issues banknotes that celebrate national heritage, wildlife, and democratic institutions. Furthermore, mobile money innovations like M-PESA have transformed financial accessibility, making Kenya a global leader in digital currency circulation and micro-savings.",
        "reflection": "### Reflection on Divine Ownership\n\nReflect on your personal attitude toward money:\n- If 'the earth is the Lord's and everything in it,' how should this truth shape your handling of money and material possessions?\n- Are you living as an absolute owner of what you have, or as a faithful temporary manager reporting to God?",
        "takeaways": [
            "Wealth comprises economic assets, money is a universal medium of exchange, and poverty is the deprivation of basic necessities.",
            "Good legal tender possesses six key qualities: durability, portability, divisibility, scarcity, acceptability, and stability.",
            "Psalm 24:1 and Haggai 2:8 confirm that God is the sovereign owner of all wealth, while humans are entrusted stewards.",
            "Money is morally neutral; it is the love of money and greed that leads to moral destruction and spiritual shipwreck."
        ],
        "mcq": {
            "question": "Which physical quality of money ensures that a banknote can circulate through thousands of hands, withstand moisture, and resist tearing over prolonged usage?",
            "options": [
                "A) Divisibility",
                "B) Durability",
                "C) Scarcity",
                "D) Portability"
            ],
            "answer": "B",
            "explanation": "Durability refers to the physical strength and resilience of legal tender materials (such as polymer or cotton-linen paper), ensuring currency withstands friction, folding, and moisture during continuous circulation."
        }
    },

    # ─── LESSON 2 ────────────────────────────────────────────────────────────
    {
        "unit_order": 2,
        "unit_name": "Traditional African Understanding of Wealth and Poverty",
        "unit_description": "Analyze traditional African perspectives on wealth, poverty, livestock indicators, communal land ownership, barter trade, and cultural safety nets.",
        "lesson_title": "Traditional African Understanding of Wealth and Poverty",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Maasai_cattle_herding.jpg",
            "title": "Visual Hook: Livestock Herding in Traditional African Culture",
            "author": "Wikimedia Commons Contributor",
            "licensing": "Creative Commons Attribution-Share Alike",
            "source": "Wikimedia Commons",
            "caption": "Traditional cattle herding in East Africa, where livestock represented tangible economic wealth, social prestige, clan security, and communal bride wealth."
        },
        "youtube": {
            "youtube_id": "ak06MSETeo4",
            "title": "BibleProject: Generosity",
            "description": "Explores how God's abundant generosity contrasts with human scarcity mindsets, echoing ancestral African principles of communal hospitality and resource sharing."
        },
        "svg_fn": get_svg_lesson_2,
        "goals": [
            "Identify traditional African indicators of wealth, including herds of livestock, fertile land, granaries, and large families.",
            "Explain traditional African exchange systems (barter trade) and communal ownership of natural resources.",
            "Analyze the cultural causes of poverty, the strict communal condemnation of laziness, and ancestral social safety nets."
        ],
        "intro": "If you ask a contemporary urban resident what it means to be wealthy, they might point to skyscraper real estate, high-end motor vehicles, or foreign bank balances. Yet in ancestral African societies, none of these modern instruments existed.\n\nHow did our ancestors measure prosperity? How did a village determine whether a person was truly rich or impoverished? And what communal safety nets existed to ensure that orphans, widows, and victims of famine did not perish? Let us examine the rich socio-economic heritage of Traditional African Societies.",
        "core_scripture": "### Cultural Heritage & Scriptural Parallel: 2 Thessalonians 3:10 & Proverbs 10:4\n\n> *\"For even when we were with you, we gave you this rule: 'The one who is unwilling to work shall not eat.'\"* (2 Thessalonians 3:10)\n\n> *\"Lazy hands make for poverty, but diligent hands bring wealth.\"* (Proverbs 10:4)\n\n> *\"Our ancestral wisdom echoes: 'A guest does not clear the granary, but a lazy resident brings hunger upon the entire homestead.'\"* (African Proverb on Work & Hospitality)",
        "theological_pillars": "### Traditional African Socio-Economic Framework\n\n1. **Indicators of Traditional Wealth:**\n   - **Livestock Herds:** Large herds of cattle, sheep, goats, and camels symbolized wealth, social standing, and diplomatic power.\n   - **Land and Agricultural Produce:** Expansive fertile fields and granaries overflowing with sorghum, millet, maize, and yams.\n   - **Large Families:** Many wives and children represented vital agricultural labor, clan vitality, and future security.\n   - **Generosity and Hospitality:** A wealthy elder was judged not by hoarding, but by the ability to feed travelers, host feasts, and assist the needy.\n\n2. **Barter Trade & Communal Resources:**\n   - **Barter Exchange:** Direct mutual exchange of commodities (e.g., swapping a goat for three sacks of grain, or honey for pottery).\n   - **Communal Ownership:** Crucial resources like grazing pastures, rivers, forests, and salt licks belonged to the entire community in trust.\n\n3. **Poverty & Its Cultural Interpretation:**\n   - **Wealth as Divine Blessing:** Material abundance was viewed as a reward from God and ancestors for righteousness and diligence.\n   - **Causes of Poverty:** Chronic laziness, severe droughts, floods, livestock epidemics (*rinderpest*), sickness, or cattle rustling.\n   - **Strict Condemnation of Laziness:** Idleness was ridiculed through proverbs, folksongs, and social exclusion.",
        "deep_dive": "### Deep Dive: Communal Social Safety Nets in Traditional Africa\n\nTraditional African communities had built-in mechanisms to prevent destitution:\n\n- **Livestock Loaning (*Kugabira* / *Hameso*):** A wealthy elder would loan a lactating cow to an impoverished neighbor so their children had milk; the first female calf born was often gifted to the poor family to rebuild their herd.\n- **Communal Labor (*Harambee* / *Mwethya* / *Bulala*):** Villagers gathered collectively to cultivate fields, harvest crops, or construct huts for widows and the elderly.\n- **Clan Responsibility for Vulnerable Members:** Orphans and widows were integrated into extended family households, ensuring no child grew up without clan protection.",
        "practical": {
            "title": "Action Framework: Revitalizing African Communal Solidarity Today",
            "steps": [
                "Step 1: Embrace Hard Work and Reject Idleness — Participate actively in household chores, family farming, and school responsibilities.",
                "Step 2: Practice Unconditional Hospitality — Welcome visitors, classmates, and neighbors warmly into your home.",
                "Step 3: Share Excess Resources — Donate outgrown clothing, extra food, or school stationery to disadvantaged community members.",
                "Step 4: Participate in Community Work — Join environmental clean-ups, tree planting, and church charity initiatives."
            ]
        },
        "kenyan_context": "The Kenyan national motto *'Harambee'* (Let us pull together), coined at Independence, directly reflects traditional African communal solidarity. Today, this ancestral spirit lives on through informal merry-go-rounds (*chamas*), community bereavement funds, and educational fundraisers.",
        "reflection": "### Reflection on Communal Wealth\n\nReflect on the definition of true success:\n- In traditional Africa, an individual with thousands of cattle who lived in total isolation without sharing was considered poor and disgraced. Why?\n- How does modern individualistic culture challenge this ancestral value of collective responsibility?",
        "takeaways": [
            "Traditional African wealth was measured in cattle, fertile land, full granaries, and large families.",
            "Barter trade facilitated exchange without currency, and critical natural resources were held under communal ownership.",
            "Hard work was universally celebrated, while laziness was rebuked through cultural proverbs and social sanctions.",
            "Communal safety nets (livestock loaning, communal labor, extended family care) safeguarded vulnerable members from starvation."
        ],
        "mcq": {
            "question": "How did traditional African communities conduct commercial trade prior to the introduction of paper money and coins?",
            "options": [
                "A) Through mobile money transfers",
                "B) Through Barter Trade (directly exchanging commodities and livestock based on mutual need)",
                "C) Through gold promissory certificates",
                "D) By refusing to engage in any external trade"
            ],
            "answer": "B",
            "explanation": "Barter trade was the primary economic exchange mechanism in traditional Africa, where actual goods (such as livestock, grain, pottery, or tools) were directly exchanged without monetary currency."
        }
    },

    # ─── LESSON 3 ────────────────────────────────────────────────────────────
    {
        "unit_order": 3,
        "unit_name": "The Impact of the Money Economy",
        "unit_description": "Analyze how European colonization and the introduction of paper currency transformed African communal life into an individualistic cash economy, exploring positive and negative outcomes.",
        "lesson_title": "The Impact of the Money Economy",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Old_East_African_Shillings.jpg",
            "title": "Visual Hook: Historical East African Currency",
            "author": "Wikimedia Commons Contributor",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Historical colonial East African currency introduced during British colonial administration to impose cash taxation and restructure the indigenous economic system."
        },
        "youtube": {
            "youtube_id": "bT4O58n4954",
            "title": "BibleProject: Gospel & Money",
            "description": "Examines how modern economic systems can cultivate greed and anxiety, contrasting with the liberation offered by Christ's kingdom perspective on resources."
        },
        "svg_fn": get_svg_lesson_3,
        "goals": [
            "Explain why European colonizers introduced the money economy and cash taxation in Kenya.",
            "Analyze the profound structural changes brought by wage-labor, land privatization, and rural-urban migration.",
            "Evaluate both the positive developments and the severe negative social consequences of the transition to a cash economy."
        ],
        "intro": "Imagine living in a community where you never pay monthly rent, water bills, electricity meters, or tuition fees. You construct your homestead using communal timber and thatch, cultivate your family farm, and barter with neighbors for whatever you need.\n\nThen, foreign colonial authorities arrive, declare ancestral lands to be 'Crown Land,' and demand that every adult male must pay an annual hut and poll tax strictly in paper 'cash.' Suddenly, you must leave your village, find a European settler plantation, and work for wages. How did this dramatic historical shift permanently alter the African family and society?",
        "core_scripture": "### Scriptural Passages: Luke 12:15 & Galatians 5:19-21\n\n> *\"Then he said to them, 'Watch out! Be on your guard against all kinds of greed; life does not consist in an abundance of possessions.'\"* (Luke 12:15)\n\n> *\"The acts of the flesh are obvious: sexual immorality, impurity and debauchery; idolatry and witchcraft; hatred, discord, jealousy, fits of rage, selfish ambition, dissensions, factions and envy...\"* (Galatians 5:19-21)",
        "theological_pillars": "### Historical & Moral Dynamics of the Money Economy\n\n1. **Reasons for Introduction by Colonizers:**\n   - **Enforcing Wage Labor:** Introducing mandatory cash taxes (Hut and Poll Tax) forced Africans to work on European settler farms, tea/coffee estates, and railway construction.\n   - **Funding Colonial Infrastructure:** Generating revenue to build railways, administrative posts, roads, and colonial barracks.\n   - **Monetizing Social Services:** Establishing formal schools and medical dispensaries that required cash fees.\n\n2. **Positive Impacts of the Money Economy:**\n   - Standardized medium of exchange facilitating global trade, industry, and modern banking.\n   - Expansion of formal education, modern healthcare facilities, and specialized employment.\n   - Ability to accumulate portable capital for enterprise investment and national development.\n\n3. **Negative Social & Ethical Consequences:**\n   - **Wage-Labor Exploitation:** Poor working conditions, meager wages, and disruption of traditional self-sufficiency.\n   - **Rural-Urban Migration:** Young fathers and men left villages for urban centers (Nairobi, Mombasa), causing family fragmentation and fatherless homes.\n   - **Rise of Urban Slums:** Overcrowding, lack of sanitation, and urban poverty in informal settlements.\n   - **Commercialization of Culture:** Bride wealth transformed from a token of clan friendship into an exorbitant commercial cash demand.\n   - **Growth of Social Vices:** Individualism, greed, armed robbery, prostitution, exam cheating, and systemic bribery.",
        "deep_dive": "### Deep Dive: Individualism vs African Communal Ethics\n\nThe introduction of private title deeds and cash wages eroded the ancestral concept of *'Ubuntu'* (I am because we are). In the cash economy, individuals began prioritizing personal accumulation over extended family welfare:\n\n- **Wealth Segregation:** A widening gap emerged between wealthy educated elites and impoverished rural peasants.\n- **Erosion of Extended Family Support:** Traditional hospitality was often replaced with gates, security guards, and reluctance to assist struggling relatives.",
        "practical": {
            "title": "Action Framework: Balancing Modern Economic Pursuits with Christian Values",
            "steps": [
                "Step 1: Reject Materialistic Status Traps — Recognize that your human dignity and value before God are not determined by luxury brands or wealth.",
                "Step 2: Prioritize Family Bonds — Stay actively connected with rural grandparents and extended family members, supporting them with love.",
                "Step 3: Strive for Educational Excellence — Study diligently to build professional and technical competence for honest career success.",
                "Step 4: Maintain Integrity in Financial Dealings — Avoid get-rich-quick shortcuts, cheating, or exploiting others for financial gain."
            ]
        },
        "kenyan_context": "Kenya's rapid urbanization has led to massive growth in cities like Nairobi, Kisumu, Nakuru, and Eldoret. While cities offer immense commercial potential, youth face high living costs and peer pressure. Christian ethics teaches young Kenyans to thrive professionally without losing their moral compass.",
        "reflection": "### Reflection on Modern Greed\n\nReflect on the impact of money on human relationships:\n- How has the transformation of bride wealth into expensive cash demands affected young couples seeking marriage today?\n- In what ways can a modern Christian enjoy the benefits of technology and banking while preserving Christ-like generosity?",
        "takeaways": [
            "Colonial authorities introduced the money economy and cash taxation to compel Africans into wage labor.",
            "The money economy advanced modern infrastructure, banking, and education, but triggered deep social disruption.",
            "Rural-urban migration weakened extended family cohesion and led to the emergence of informal urban settlements.",
            "Christian discipleship calls believers to resist materialism and individualism by upholding generosity, family care, and integrity."
        ],
        "mcq": {
            "question": "What was the primary method used by colonial administrators to compel traditional Africans to work on European agricultural plantations?",
            "options": [
                "A) Offering free overseas travel and luxury gifts",
                "B) Introducing mandatory taxes (Hut and Poll Tax) payable strictly in cash currency",
                "C) Exchanging ancestral lands for cattle herds",
                "D) Passing voluntary community resolutions"
            ],
            "answer": "B",
            "explanation": "By imposing mandatory colonial taxes that could only be settled with legal tender cash, colonial authorities compelled traditional Africans to leave subsistence farming and seek wage labor on European settler plantations."
        }
    },

    # ─── LESSON 4 ────────────────────────────────────────────────────────────
    {
        "unit_order": 4,
        "unit_name": "Christian Teachings on Wealth and Stewardship",
        "unit_description": "Examine biblical teachings on wealth, possessions, the Parable of the Rich Fool (Luke 12:15-21), treasures in heaven (Matthew 6:19-24), and divine stewardship.",
        "lesson_title": "Christian Teachings on Wealth and Stewardship",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/0/07/Rembrandt_Harmensz._van_Rijn_-_The_Parable_of_the_Rich_Fool.jpg",
            "title": "Visual Hook: The Parable of the Rich Fool by Rembrandt",
            "author": "Rembrandt van Rijn (1606–1669), Gemäldegalerie Berlin",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Rembrandt's depiction of the Rich Fool examining his gold coins by candlelight, oblivious to the imminent demand for his soul by God."
        },
        "youtube": {
            "youtube_id": "bT4O58n4954",
            "title": "BibleProject: Gospel & Money",
            "description": "An engaging visual breakdown of how Jesus addressed wealth, challenging religious hypocrisy, and calling believers to store up eternal treasures."
        },
        "svg_fn": get_svg_lesson_4,
        "goals": [
            "Explain the biblical doctrine of stewardship: humans as temporary trustees of God's resources.",
            "Analyze Jesus' warnings against greed and hoarding in the Parable of the Rich Fool (Luke 12:15-21).",
            "Contrast earthly treasures with eternal heavenly wealth based on Matthew 6:19-24 and Deuteronomy 8:18."
        ],
        "intro": "Imagine you are appointed the senior branch manager of a prestigious commercial bank. Your office is luxurious, and every day you count, safeguard, and authorize the transfer of hundreds of millions of shillings belonging to account holders.\n\nCould you pack several million shillings into a bag and take it home to buy yourself a private luxury yacht? Absolutely not! If you do, you are a criminal. The funds are not yours; you are merely a trusted manager. This is precisely how Christian theology views every shilling, piece of land, and talent we possess on earth.",
        "core_scripture": "### Scriptural Passages: Luke 12:15-21 & Matthew 6:19-24\n\n> *\"Then he told them a parable: 'The ground of a certain rich man yielded an abundant harvest. He thought to himself, \"What shall I do? I have no place to store my crops.\" Then he said, \"This is what I’ll do. I will tear down my barns and build bigger ones... And I’ll say to myself, 'You have plenty of grain laid up for many years. Take life easy; eat, drink and be merry.'\" But God said to him, \"You fool! This very night your life will be demanded from you. Then who will get what you have prepared for yourself?\" This is how it will be with whoever stores up things for themselves but is not rich toward God.'\"* (Luke 12:16-21)\n\n> *\"Do not store up for yourselves treasures on earth, where moths and vermin destroy, and where thieves break in and steal. But store up for yourselves treasures in heaven... For where your treasure is, there your heart will be also. No one can serve two masters... You cannot serve both God and money.\"* (Matthew 6:19-21, 24)",
        "theological_pillars": "### Biblical Principles of Wealth & Stewardship\n\n1. **God as the Ultimate Source of Wealth:** Deuteronomy 8:18 reminds believers that God provides the intellect, physical health, opportunities, and vigor necessary to produce wealth.\n2. **The Definition of Stewardship:** Humans possess nothing permanently. We are stewards (*oikonomos* in Greek) charged with managing divine assets for God's glory, community welfare, and the advancement of the Kingdom.\n3. **Transitory Nature of Earthly Wealth:** Material possessions are temporal; no one takes land, bank balances, or vehicles beyond the grave (1 Timothy 6:7).\n4. **The Folly of Self-Centered Hoarding:** In Luke 12, God called the rich farmer a 'fool' not because he was successful, but because his worldview was entirely self-centered: *my crops, my barns, my goods, my soul*, ignoring God and the starving poor.\n5. **The Danger of Idolatry (Mammon):** Jesus stated unequivocally in Matthew 6:24 that money can become a rival god (*Mammon*) that enslaves the human heart.",
        "deep_dive": "### Deep Dive: Being 'Rich Toward God'\n\nWhat does it mean to be 'rich toward God'?\n- **Honoring God with Firstfruits:** Returning a faithful tithe (10%) and joyful freewill offerings (Malachi 3:10, 2 Corinthians 9:7).\n- **Investing in People:** Using financial resources to educate orphans, feed the hungry, and empower the marginalized.\n- **Pursuing Moral Riches:** Cultivating the fruit of the Spirit (love, joy, peace, patience, kindness, integrity) which outlasts earthly fortunes.",
        "practical": {
            "title": "Action Framework: Practicing Daily Christian Stewardship",
            "steps": [
                "Step 1: Acknowledge God Daily — Thank God in morning prayer for your life, health, intellectual abilities, and provisions.",
                "Step 2: Practice Systematic Giving — Give an offering or tithe during church services or school Christian Union fellowships.",
                "Step 3: Resist Comparison and Jealousy — Avoid competing with classmates over expensive shoes, phones, or clothing.",
                "Step 4: Cultivate Contentment — Practice gratitude for what you have while working diligently toward academic goals."
            ]
        },
        "kenyan_context": "In Kenya, many Christians actively participate in church stewardship programs, tithing, and fundraising drives (*kamweretho* and development funds) to build schools, boreholes, and dispensaries. Faithful stewardship transforms personal resources into communal blessings across rural and urban communities.",
        "reflection": "### Reflection on the Rich Fool\n\nReflect on Jesus' parable:\n- Why did God call the rich farmer a 'fool' even though he was a highly efficient, hardworking, and successful agriculturist?\n- What areas of your life are currently focused on 'building bigger barns' rather than being rich toward God?",
        "takeaways": [
            "God is the sole owner of all creation; humans are temporary managers and stewards of wealth (Deut 8:18, Ps 24:1).",
            "Earthly wealth is transitory and cannot provide eternal security or spiritual salvation.",
            "The Parable of the Rich Fool warns against selfish accumulation that ignores God and needy neighbors (Luke 12:15-21).",
            "Disciples cannot serve two masters; we must choose God over the enslaving worship of money (Matthew 6:24)."
        ],
        "mcq": {
            "question": "In the Parable of the Rich Fool (Luke 12:16-21), why did God declare the wealthy farmer to be a 'fool'?",
            "options": [
                "A) Because he failed to plant high-yield seeds in his fields",
                "B) Because he hoarded wealth exclusively for himself, ignoring God and the needs of others",
                "C) Because he gave away all his harvest to neighboring villages",
                "D) Because he did not build high stone fences around his estate"
            ],
            "answer": "B",
            "explanation": "God called the farmer a fool because he hoarded his abundant harvest for selfish ease and hedonism, completely neglecting spiritual preparation, gratitude to God, and charity toward the poor."
        }
    },

    # ─── LESSON 5 ────────────────────────────────────────────────────────────
    {
        "unit_order": 5,
        "unit_name": "Christian Teachings on Poverty and Sharing",
        "unit_description": "Examine the biblical perspectives on poverty, systemic vs moral causes, the Rich Man and Lazarus (Luke 16:19-31), Macedonian generosity (2 Corinthians 8:1-9), and almsgiving.",
        "lesson_title": "Christian Teachings on Poverty and Sharing",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Lazarus_and_Dives.jpg",
            "title": "Visual Hook: The Rich Man and Lazarus",
            "author": "Illumination from the Codex Aureus of Echternach (c. 1030–1050)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Medieval manuscript miniature showing Lazarus begging at the rich man's gate, contrasting earthly inequality with eternal divine justice."
        },
        "youtube": {
            "youtube_id": "ak06MSETeo4",
            "title": "BibleProject: Generosity",
            "description": "Explores how God's abundant grace empowers radical sharing and self-sacrificial charity, transforming communities and breaking cycles of poverty."
        },
        "svg_fn": get_svg_lesson_5,
        "goals": [
            "Distinguish between systemic causes of poverty (injustice, calamity) and moral causes (laziness, wastefulness).",
            "Analyze Jesus' teachings in the Parable of the Rich Man and Lazarus (Luke 16:19-31) regarding callous indifference.",
            "Evaluate Christian duties of almsgiving and sacrificial sharing based on 2 Corinthians 8:1-9, Luke 3:11, and Matthew 25:34-40."
        ],
        "intro": "Imagine walking along a bustling avenue in a major city. On the sidewalk lies an emaciated beggar, covered in sores, pleading for a scrap of bread. Just feet away, a luxury sport utility vehicle pulls up, and a wealthy patron enters a five-star hotel carrying expensive shopping bags.\n\nWhy does extreme luxury exist alongside devastating destitution? Does God despise the poor, or does He hold the wealthy accountable for indifference? In this lesson, we explore the heartbeat of God for the marginalized and the radical Christian obligation to share.",
        "core_scripture": "### Scriptural Passages: Luke 16:19-31 & 2 Corinthians 8:1-9\n\n> *\"There was a rich man who was dressed in purple and fine linen and lived in luxury every day. At his gate was laid a beggar named Lazarus, covered with sores and longing to eat what fell from the rich man’s table... The time came when the beggar died and the angels carried him to Abraham’s side. The rich man also died and was buried. In Hades, where he was in torment, he looked up and saw Abraham far away, with Lazarus by his side...\"* (Luke 16:19-23)\n\n> *\"And now, brothers and sisters, we want you to know about the grace that God has given the Macedonian churches. In the midst of a very severe trial, their overflowing joy and their extreme poverty welled up in rich generosity... For you know the grace of our Lord Jesus Christ, that though he was rich, yet for your sake he became poor, so that you through his poverty might become rich.\"* (2 Corinthians 8:1-2, 9)",
        "theological_pillars": "### Theological Analysis of Poverty & Sharing\n\n1. **The Multidimensional Causes of Poverty:**\n   - **Systemic Factors:** Droughts, floods, civil conflict, unjust economic policies, corrupt leadership, lack of schools, and historical marginalization.\n   - **Individual/Moral Factors:** Slothfulness, refusal to work, alcohol/drug abuse, gambling, and poor financial discipline.\n   - **Dispelling Misconceptions:** Jesus firmly rejected the false prosperity doctrine that physical poverty is always a direct punishment for personal sin.\n\n2. **The Parable of the Rich Man and Lazarus (Luke 16:19-31):**\n   - **The Sin of Omission:** The rich man was condemned not because he was rich, but because he stepped over suffering Lazarus daily without showing mercy.\n   - **Reversal of Fortunes:** In eternity, divine justice vindicates the oppressed while confronting unrepentant selfish greed.\n\n3. **Macedonian Generosity (2 Corinthians 8:1-9):**\n   - The Macedonian believers gave self-sacrificially despite their own extreme poverty, proving that genuine generosity is a matter of the heart, not bank balance size.\n\n4. **The Final Judgment Mandate (Matthew 25:31-46):**\n   - Christ identifies personally with the marginalized: *'Whatever you did for one of the least of these brothers and sisters of mine, you did for me.'*",
        "deep_dive": "### Deep Dive: Spiritual Poverty ('Poor in Spirit') vs Physical Destitution\n\nIn Matthew 5:3, Jesus taught: *'Blessed are the poor in spirit, for theirs is the kingdom of heaven.'*\n- **Physical Poverty:** A painful material lack of food, shelter, and healthcare that Christians are commanded to alleviate through love and justice.\n- **Poverty in Spirit (*Ptochoi toi pneumati*):** A posture of utter spiritual humility where a person recognizes that they are spiritually bankrupt without God's grace and salvation.",
        "practical": {
            "title": "Action Framework: Launching a Classroom and Community Compassion Initiative",
            "steps": [
                "Step 1: Form a Classroom Welfare Box — Collaborate with classmates to place a secure box where students contribute extra pens, pencils, erasers, and sanitary pads.",
                "Step 2: Distribute Discreetly — Ensure that needy classmates receive essential supplies with complete confidentiality and dignity.",
                "Step 3: Visit Local Children's Homes — Organize a class or church youth visit to orphanages or elderly homes, taking food, soap, and fellowship.",
                "Step 4: Advocate for the Marginalized — Stand up against bullying, exclusion, and mockery of students from impoverished backgrounds."
            ]
        },
        "kenyan_context": "In Kenya, non-governmental organizations, church welfare programs, and school feeding initiatives play a vital role in keeping vulnerable children in school. Through community feeding programs in arid and semi-arid lands (ASAL), Christian compassion translates into lifesaving nutrition.",
        "reflection": "### Reflection on Lazarus at Your Gate\n\nReflect on your daily surroundings:\n- Who is the 'Lazarus' sitting near your school, church, or neighborhood whom you pass by every day without noticing?\n- What practical step can you take this week to demonstrate Christ-like compassion toward them?",
        "takeaways": [
            "Poverty arises from both systemic injustices (drought, poor governance) and individual habits (laziness, substance abuse).",
            "The Parable of the Rich Man and Lazarus warns that callous indifference toward the suffering carries eternal consequences (Luke 16:19-31).",
            "The Macedonian churches demonstrated that radical generosity stems from divine grace rather than material wealth (2 Cor 8:1-9).",
            "Jesus commands active charity; serving the poor, the sick, and the hungry is serving Christ directly (Matt 25:40)."
        ],
        "mcq": {
            "question": "In Luke 16:19-31, what was the primary spiritual failure of the rich man regarding the beggar Lazarus?",
            "options": [
                "A) He did not invite Lazarus to become his commercial business partner",
                "B) He was callously indifferent to Lazarus' suffering, stepping past him daily without showing compassion",
                "C) He failed to build a hospital for the Roman army",
                "D) He paid his household servants in foreign currency"
            ],
            "answer": "B",
            "explanation": "The rich man was condemned for his cold-hearted indifference and lack of mercy: he feasted luxuriously every day while ignoring the starving, sick beggar lying at his very doorstep."
        }
    },

    # ─── LESSON 6 ────────────────────────────────────────────────────────────
    {
        "unit_order": 6,
        "unit_name": "Ethical Wealth Acquisition and Jua Kali Business Projects",
        "unit_description": "Explore ethical wealth creation, manual labor dignity, Jua Kali entrepreneurship, agribusiness, progress journals, and youth project management.",
        "lesson_title": "Ethical Wealth Acquisition and Jua Kali Business Projects",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/1/14/Welder_in_Kenya.jpg",
            "title": "Visual Hook: Jua Kali Metalwork and Entrepreneurship",
            "author": "Wikimedia Commons Contributor",
            "licensing": "Creative Commons Attribution-Share Alike",
            "source": "Wikimedia Commons",
            "caption": "An artisan in Kenya's vibrant Jua Kali sector welding metal structures, showcasing the dignity of manual craftsmanship and youth entrepreneurship."
        },
        "youtube": {
            "youtube_id": "bT4O58n4954",
            "title": "BibleProject: Gospel & Money",
            "description": "Examines biblical perspectives on honest hard work, avoiding dishonest gain, and utilizing vocational creativity for God's glory."
        },
        "svg_fn": get_svg_lesson_6,
        "goals": [
            "Identify legitimate, ethical ways for youth to acquire wealth through agriculture, crafts, services, and creative arts.",
            "Demonstrate the dignity of manual labor and the economic importance of Kenya's Jua Kali sector.",
            "Apply the six-step lifecycle to launch, fund, and manage a school or family business project using a progress journal."
        ],
        "intro": "Have you ever observed a metal welder fashioning sturdy window grilles, a carpenter carving beautiful sofa sets, or a young farmer tending a lush green sack-garden of spinach?\n\nIn Kenya, we proudly call this the *Jua Kali* sector (literally 'under the fierce sun'). Far from being second-class work, the Jua Kali and informal business sector employs over 80% of Kenya's working population and drives our national economy. You do not have to wait until adulthood to build financial literacy; you can launch a viable, ethical micro-enterprise today!",
        "core_scripture": "### Scriptural Passages: Proverbs 13:11, Proverbs 28:19 & Proverbs 14:23\n\n> *\"Dishonest money dwindles away, but whoever gathers money little by little makes it grow.\"* (Proverbs 13:11)\n\n> *\"Those who work their land will have abundant food, but those who chase fantasies have their fill of poverty.\"* (Proverbs 28:19)\n\n> *\"All hard work brings a profit, but mere talk leads only to poverty.\"* (Proverbs 14:23)",
        "theological_pillars": "### Ethical Wealth Acquisition & Entrepreneurship\n\n1. **Biblical Mandate for Honest Labor:**\n   - God instituted labor before the Fall in Eden (Genesis 2:15). Honest hard work is an act of worship and stewardship.\n   - Wealth gained through trickery, fraudulent scales, betting, or theft carries God's judgment and quickly vanishes (Proverbs 13:11).\n\n2. **Dignity of the Jua Kali Sector:**\n   - Jesus Himself worked as a carpenter (*tekton*) in Nazareth (Mark 6:3), and Apostle Paul supported his ministry through tentmaking (Acts 18:3).\n   - Manual craftsmanship, metalwork, tailoring, carpentry, and masonry are honorable vocations that provide vital goods.\n\n3. **Viable Youth Business Ventures:**\n   - **Agribusiness:** Poultry rearing (eggs/broilers), rabbit keeping, sack gardening (kales, spinach, tomatoes), mushroom cultivation.\n   - **Artisanal Crafts:** Beaded jewelry, sisal baskets, wood carving, decorative mats.\n   - **Commercial Services:** Car washing, compound cleaning, shoe shining, peer tutoring, digital typesetting, graphic design.\n\n4. **The Six-Step Business Project Lifecycle:**\n   - *Step 1 (Idea):* Identify an unmet local community need.\n   - *Step 2 (Pitch):* Present the plan to parents/teachers to secure mentorship and small seed capital.\n   - *Step 3 (Launch):* Purchase quality materials ethically and begin production.\n   - *Step 4 (Progress Journal):* Maintain daily records of all income, expenditures, and client feedback.\n   - *Step 5 (Review):* Calculate profit/loss and report performance to mentors.\n   - *Step 6 (Scale):* Reinvest net profits and tithe faithfully.",
        "deep_dive": "### Deep Dive: The Anatomy of a Business Progress Journal\n\nA Progress Journal is an indispensable tool for financial literacy and transparency:\n\n- **Date & Transaction Details:** Recording the exact time and purpose of every financial exchange.\n- **Cash Inflows (Sales Revenue):** Monies received from customers purchasing goods or services.\n- **Cash Outflows (Operating Expenses):** Costs incurred for raw materials, transport, feed, or packaging.\n- **Net Balance & Learnings:** Summarizing weekly profits, noting operational challenges, and documenting customer suggestions.",
        "practical": {
            "title": "Action Framework: Starting a Micro-Agribusiness or Craft Venture",
            "steps": [
                "Step 1: Form a Team of 2-3 Learners — Partner with trustworthy classmates or siblings to combine skills and capital.",
                "Step 2: Choose a Low-Cost Project — Select a manageable idea, such as planting sukuma wiki in reusable gunny sacks or rearing 5 local chicks.",
                "Step 3: Keep Meticulous Records — Write down every single shilling spent on seeds/feed and earned from vegetable/egg sales in a notebook.",
                "Step 4: Evaluate Monthly Results — Present your progress journal to your CRE teacher or guardian for review and guidance."
            ]
        },
        "kenyan_context": "In Kenya, government initiatives like the Youth Enterprise Development Fund (YEDF) and the Uwezo Fund, alongside local SACCOs, provide financial literacy and micro-loans to young entrepreneurs. Starting early prepares students for financial independence and self-employment.",
        "reflection": "### Reflection on the Dignity of Manual Labor\n\nReflect on cultural attitudes toward work:\n- Why do some teenagers look down on agricultural and Jua Kali work, preferring to stay idle while hoping for white-collar office jobs?\n- How does the example of Jesus working as a carpenter elevate the dignity of manual labor in your eyes?",
        "takeaways": [
            "Ethical wealth is created through diligence, honesty, and incremental effort (Proverbs 13:11, Proverbs 14:23).",
            "Manual labor possesses inherent dignity; Jesus as a carpenter and Paul as a tentmaker modeled honest trade.",
            "Youth can initiate viable micro-enterprises in agribusiness, artisanal crafts, and service provision.",
            "A Progress Journal is a vital financial literacy tool for tracking cash flows, profit margins, and operational improvements."
        ],
        "mcq": {
            "question": "What is the primary function of a Progress Journal when managing a small business or agricultural project?",
            "options": [
                "A) To write fictional stories for creative literature class",
                "B) To maintain an accurate daily record of all business income, operating expenses, profits, and customer feedback",
                "C) To draw town maps and architectural blueprints",
                "D) To list personal secrets and private diary entries"
            ],
            "answer": "B",
            "explanation": "A Progress Journal serves as a core financial record-keeping ledger that systematically captures every cash inflow, expenditure, profit calculation, and operational lesson for transparency and business improvement."
        }
    },

    # ─── LESSON 7 ────────────────────────────────────────────────────────────
    {
        "unit_order": 7,
        "unit_name": "Financial Integrity: Fighting Corruption and Bribery",
        "unit_description": "Define corruption, bribery, and extortion; analyze their destructive societal effects; examine biblical condemnations from Exodus 23:8 and Micah 6:10-12; and explore Kenya's EACC.",
        "lesson_title": "Financial Integrity: Fighting Corruption and Bribery",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Integrity_and_Justice_Scales.jpg",
            "title": "Visual Hook: Scales of Justice and Integrity",
            "author": "Wikimedia Commons Contributor",
            "licensing": "Creative Commons Attribution-Share Alike",
            "source": "Wikimedia Commons",
            "caption": "The balanced scales of justice symbolizing honesty, transparency, rule of law, and the total rejection of corrupt inducements and bribery."
        },
        "youtube": {
            "youtube_id": "bT4O58n4954",
            "title": "BibleProject: Gospel & Money",
            "description": "Examines biblical justice, prophetic condemnations of economic exploitation, and God's call for transparent and righteous leadership."
        },
        "svg_fn": get_svg_lesson_7,
        "goals": [
            "Define bribery, corruption, and extortion, distinguishing between giving and receiving illicit benefits.",
            "Analyze the root causes of corruption and evaluate its devastating impact on public infrastructure, healthcare, and the poor.",
            "Apply biblical principles from Exodus 23:8, Micah 6:10-12, and Luke 3:12-14 to maintain financial integrity and support anti-corruption bodies (EACC)."
        ],
        "intro": "Imagine rushing your critically ill grandmother to a public hospital. The emergency medical officer is present, but he refuses to admit her until you secretly slip a 2,000-shilling bribe under his desk. Or imagine a newly constructed bridge collapsing during heavy rains because a corrupt contractor paid off inspectors after using substandard cement.\n\nCorruption is a devastating social poison that robs public coffers, destroys infrastructure, and costs human lives. Why does corruption occur, and how can Christian youth stand as beacons of unyielding integrity?",
        "core_scripture": "### Scriptural Passages: Exodus 23:8, Micah 6:10-12 & Luke 3:12-14\n\n> *\"Do not accept a bribe, for a bribe blinds those who see and twists the words of the innocent.\"* (Exodus 23:8)\n\n> *\"Am I still to forget your ill-gotten treasures, you wicked house, and the short ephah, which is an accursed thing? Shall I acquit someone with dishonest scales, with a bag of false weights? Your rich people are violent; your inhabitants are liars and their tongues speak deceitfully.\"* (Micah 6:10-12)\n\n> *\"Even tax collectors came to be baptized. 'Teacher,' they asked, 'what should we do?' 'Don’t collect any more than you are required to,' he told them. Then some soldiers asked him, 'And what should we do?' He replied, 'Don’t extort money and don’t accuse people falsely—be content with your pay.'\"* (Luke 3:12-14)",
        "theological_pillars": "### Definitions, Causes & Consequences of Financial Corruption\n\n1. **Core Definitions:**\n   - **Corruption:** The abuse of entrusted power or public office for illegitimate personal enrichment or sectional advantage.\n   - **Bribery:** The act of offering, giving, receiving, or soliciting money, gifts, or favors to influence an official's decision or gain an underserved advantage.\n   - **Extortion:** The illegal extraction of money or favors through threats, intimidation, or coercion.\n\n2. **Factors Fueling Corruption:**\n   - **Unbridled Greed & Materialism:** An insatiable lust for quick riches and lavish lifestyles without honest labor.\n   - **Lack of Moral Values & Conscience:** Absence of God-fearing integrity and accountability in public and private life.\n   - **High Unemployment & Poverty:** Desperate citizens paying bribes to secure scarce jobs or police clearance.\n   - **Weak Enforcement & Impunity:** Inadequate prosecution of high-profile corrupt leaders.\n\n3. **Devastating Consequences on Society:**\n   - **Severe Harm to the Poor:** Since the impoverished cannot afford bribes, they are denied basic healthcare, clean water, and justice.\n   - **Collapsed Infrastructure:** Bribed procurement officials approve substandard roads, dams, and buildings that fail and cause fatalities.\n   - **Economic Decay & Stagnation:** Foreign investors flee countries where extortion is rampant, causing job losses.\n   - **Degradation of Human Dignity:** Destroys public trust, perverts judicial systems, and poisons national character.",
        "deep_dive": "### Deep Dive: Kenya's EACC & John the Baptist's Instructions to Public Officers\n\nIn Kenya, the **Ethics and Anti-Corruption Commission (EACC)** is the constitutional body mandated to enforce integrity, investigate economic crimes, recover stolen public assets, and promote ethical governance under Chapter Six of the Constitution of Kenya.\n\nWhen John the Baptist preached repentance in Luke 3:\n- He commanded tax collectors: *'Collect no more than authorized'* (ending extortion and overcharging).\n- He instructed law enforcement officers: *'Do not extort money, do not make false accusations, and be content with your wages.'*\n- True Christian repentance demands immediate structural honesty in all professional and financial duties.",
        "practical": {
            "title": "Action Framework: Practicing Financial Integrity as a Young Citizen",
            "steps": [
                "Step 1: Practice Absolute Academic Honesty — Never cheat in exams, copy assignments, or bribe class leaders to erase your name from noise lists.",
                "Step 2: Refuse Undeserved Shortcuts — Wait patiently in queues and fulfill all statutory requirements without offering tips or inducements.",
                "Step 3: Report Dishonesty — Speak out or notify trusted teachers and parents when you witness theft, extortion, or bribery.",
                "Step 4: Cultivate Contentment — Learn to be content with your family's financial situation, refusing to steal or engage in crime for quick cash."
            ]
        },
        "kenyan_context": "In Kenyan schools, Integrity Clubs supported by the EACC nurture ethical leadership, transparency, and civic responsibility among youth. Developing anti-corruption convictions in junior secondary school builds the bedrock for future honest governance in Kenya.",
        "reflection": "### Reflection on the Blindness of Bribery\n\nReflect on Exodus 23:8:\n- Why does the Bible warn that a bribe 'blinds those who see'? How does taking a bribe distort a leader's ability to judge right from wrong?\n- If you are elected as a prefect, student council leader, or public official, what moral boundaries will you establish to resist bribery?",
        "takeaways": [
            "Corruption and bribery represent the abuse of entrusted power for unjust personal enrichment.",
            "Exodus 23:8 and Micah 6:10-12 declare that bribery perverts justice and brings God's righteous judgment.",
            "Corruption severely harms the poor, destroys public infrastructure, and repels economic development.",
            "Kenya's EACC and Christian ethics require total integrity, contentment, and transparency in all financial dealings."
        ],
        "mcq": {
            "question": "According to Exodus 23:8, what is the profound spiritual and psychological effect of accepting a bribe?",
            "options": [
                "A) It rapidly accelerates national economic growth",
                "B) It blinds those who see and twists the words of the innocent, perverting justice",
                "C) It establishes long-lasting international friendships",
                "D) It increases the physical strength of judicial officers"
            ],
            "answer": "B",
            "explanation": "Exodus 23:8 explicitly warns that a bribe acts as moral poison, blinding the discernment of wise leaders and twisting the words and rights of innocent citizens."
        }
    },

    # ─── LESSON 8 ────────────────────────────────────────────────────────────
    {
        "unit_order": 8,
        "unit_name": "Core Life Skills and Christian Values for Financial Stewardship",
        "unit_description": "Examine five core life skills (decision-making, critical thinking, creative thinking, self-esteem, assertiveness) and ten Christian values essential for lifelong financial stewardship.",
        "lesson_title": "Core Life Skills and Christian Values for Financial Stewardship",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Students_in_classroom_Kenya.jpg",
            "title": "Visual Hook: Kenyan Students Developing Life Skills",
            "author": "Wikimedia Commons Contributor",
            "licensing": "Creative Commons Attribution-Share Alike",
            "source": "Wikimedia Commons",
            "caption": "Junior secondary school students in Kenya actively developing critical thinking, values, and decision-making skills for lifelong ethical stewardship."
        },
        "youtube": {
            "youtube_id": "bT4O58n4954",
            "title": "BibleProject: Gospel & Money",
            "description": "Explores how Christian character, wisdom, and life skills equip believers to navigate modern economic systems with enduring moral integrity."
        },
        "svg_fn": get_svg_lesson_8,
        "goals": [
            "Define the five core life skills essential for financial success: decision-making, critical thinking, creative thinking, self-esteem, and assertiveness.",
            "Analyze the ten foundational Christian values governing wealth: love, honesty, reliability, fairness, justice, respect, faithfulness, humility, persistence, and chastity.",
            "Apply the 8-step decision-making model to evaluate financial dilemmas and reject deceptive 'get-rich-quick' schemes."
        ],
        "intro": "Imagine you are preparing for an expedition through an uncharted, hazardous wilderness. To survive, you must pack specific, indispensable tools in your backpack: a compass for direction, a flashlight for darkness, a water purification kit, and a map.\n\nIn the journey of life, managing wealth, money, and career choices is like walking through that wild terrain. Today, we equip your spiritual and intellectual backpack with two indispensable toolsets: five core life skills and ten Christian values.",
        "core_scripture": "### Scriptural Passages: Proverbs 21:5, Ecclesiastes 11:1-2 & Proverbs 3:5-6\n\n> *\"The plans of the diligent lead to profit as surely as haste leads to poverty.\"* (Proverbs 21:5)\n\n> *\"Ship your grain across the sea; after many days you may receive a return. Invest in seven ventures, yes, in eight; you do not know what disaster may come upon the land.\"* (Ecclesiastes 11:1-2)\n\n> *\"Trust in the Lord with all your heart and lean not on your own understanding; in all your ways submit to him, and he will make your paths straight.\"* (Proverbs 3:5-6)",
        "theological_pillars": "### The Ethical & Behavioral Toolkit for Financial Stewardship\n\n1. **Five Core Life Skills for Financial Success:**\n   - **Decision-Making:** The structured ability to identify challenges, analyze alternatives, foresee consequences, and choose the most ethical path.\n   - **Critical Thinking:** Objectively analyzing financial proposals, commercial advertisements, and peer pressure without being blinded by greed.\n   - **Creative Thinking:** Developing innovative, low-cost solutions to generate income (e.g., launching novel Jua Kali or agribusiness projects).\n   - **Self-Esteem:** A healthy sense of personal worth before God, preventing youth from selling their dignity, bodies, or values for money.\n   - **Assertiveness:** The confidence to say a firm, polite 'NO' to corrupt deals, fraud, gambling, or illegal shortcuts.\n\n2. **Ten Christian Values for Financial Integrity:**\n   - **Love:** Utilizing wealth to alleviate human suffering out of sincere compassion (1 John 3:17).\n   - **Honesty:** Total truthfulness in pricing, weights, transactions, and declarations (Proverbs 11:1).\n   - **Reliability:** Fulfilling business contracts and keeping financial promises dependably.\n   - **Fairness:** Treating all customers, workers, and partners equitably without nepotism or discrimination.\n   - **Justice:** Demanding fair wages, honest pricing, and transparent economic systems.\n   - **Respect:** Treating public and private property with utmost care and stewardship.\n   - **Faithfulness:** Managing entrusted resources with total transparency (Luke 16:10).\n   - **Humility:** Remaining modest when blessed with material abundance, never boasting.\n   - **Persistence (Grit):** Working diligently despite economic setbacks, crop failures, or market downturns.\n   - **Chastity (Moral Purity):** Preserving bodily holiness and refusing to engage in commercial sexual exploitation (*'sponsors'*) for cash.",
        "deep_dive": "### Deep Dive: The 8-Step Decision-Making Framework Applied to 'Quick Money'\n\nConsider this real-world youth scenario: *A stranger on social media sends a message: 'Send Ksh 500 now to join our VIP investment circle; recruit two friends and receive Ksh 10,000 tomorrow without working!'*\n\nApplying the 8-Step Model:\n1. **Identify the Problem:** You are being solicited to join an unverified online money scheme.\n2. **Understand Underlying Issues:** The promise of unrealistic 2000% returns in 24 hours.\n3. **Brainstorm Options:** (A) Send the money and recruit friends; (B) Ignore and block; (C) Report the account and warn classmates.\n4. **Analyze Consequences:** Option A leads to financial loss, ruined friendships, and complicity in fraud (Pyramid Scheme). Option C protects your savings and saves peers from fraud.\n5. **Select Best Ethical Option:** Option C.\n6. **Implement Decision:** Block the number, delete the message, and report to parents/teachers.\n7. **Evaluate Outcome:** Your savings remain secure, and your integrity is preserved.",
        "practical": {
            "title": "Action Framework: Building Your Personal Financial Integrity Plan",
            "steps": [
                "Step 1: Define Your Personal Values Code — Write down 3 non-negotiable Christian values (e.g., Honesty, Faithfulness, Self-Esteem) on your study desk.",
                "Step 2: Practice Assertive Refusals — Practice saying: 'Thank you, but I do not participate in gambling, pyramid schemes, or unverified online deals.'",
                "Step 3: Consult Wise Mentors — Always discuss major financial or business ideas with parents, guardians, or teachers before committing funds.",
                "Step 4: Commit Your Plans to God — Pray over your studies, enterprise goals, and future career, seeking divine guidance (Proverbs 3:5-6)."
            ]
        },
        "kenyan_context": "In Kenya, online scams, sports betting apps, and pyramid schemes frequently target vulnerable youth. Equipping students with critical thinking, assertiveness, and Christian values shields them from financial exploitation and cybercrime.",
        "reflection": "### Reflection on the Integrity Backpack\n\nReflect on your personal character:\n- If you were offered an easy Ksh 50,000 to do something illegal or morally compromising that nobody else would ever discover, what life skills and values would you draw from your backpack to say NO?\n- How does faithfulness in managing small pocket money today prepare you to manage millions in future leadership?",
        "takeaways": [
            "Five core life skills (decision-making, critical thinking, creative thinking, self-esteem, assertiveness) equip youth for ethical financial choices.",
            "Ten Christian values (including honesty, fairness, humility, and faithfulness) provide the spiritual compass for lifelong stewardship.",
            "The 8-step decision-making model systematically resolves financial dilemmas and protects against predatory pyramid schemes.",
            "Faithfulness in little things qualifies a believer to be entrusted with true spiritual and leadership responsibilities (Luke 16:10)."
        ],
        "mcq": {
            "question": "Which life skill refers to the systematic process of identifying a challenge, analyzing alternative options, weighing long-term consequences, and selecting the most ethical action?",
            "options": [
                "A) Creative Thinking",
                "B) Decision-Making",
                "C) Self-Esteem",
                "D) Mechanical Memory"
            ],
            "answer": "B",
            "explanation": "Decision-making is the formal, 8-step structured process that enables an individual to evaluate alternatives and select the most ethical, constructive course of action."
        }
    }
]


# ─── INGESTION RUNNER ────────────────────────────────────────────────────────

def ingest_grade9_cre_topic16():
    print("=" * 80)
    print("STARTING VLEARN PRODUCTION INGESTION: GRADE 9 CRE TOPIC 16")
    print("=" * 80)

    with transaction.atomic():
        # 1. Resolve Scope
        curriculum = Curriculum.objects.get(name="CBC")
        grade = Grade.objects.get(id=18)
        subject = Subject.objects.get(id=50, grade=grade)

        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=16,
            defaults={
                "name": "Wealth, Money and Poverty"
            }
        )
        if created:
            print(f"[✓] Created Topic 16: '{topic.name}' (ID: {topic.id}) under Subject 50")
        else:
            topic.name = "Wealth, Money and Poverty"
            topic.save()
            print(f"[✓] Resolved existing Topic 16: '{topic.name}' (ID: {topic.id})")

        # 2. Clear previous units/lessons under Topic 16 for clean idempotent execution
        existing_units = LearningUnit.objects.filter(topic=topic)
        for unit in existing_units:
            for lsn in unit.lessons.all():
                lsn.blocks.all().delete()
                lsn.assets.all().delete()
                lsn.delete()
            unit.delete()
        # Also clean any orphaned lessons directly under topic
        for lsn in Lesson.objects.filter(topic=topic):
            lsn.blocks.all().delete()
            lsn.assets.all().delete()
            lsn.delete()
        print("[✓] Cleared previous units and lessons under Topic 16 for clean idempotent rebuild.")

        total_units = 0
        total_lessons = 0
        total_pages = 0
        total_blocks = 0
        total_assets = 0

        # 3. Ingest 8 Lessons
        for cfg in LESSONS_DATA:
            u_order = cfg["unit_order"]
            u_name = cfg["unit_name"]
            l_title = cfg["lesson_title"]

            # Create LearningUnit
            unit = LearningUnit.objects.create(
                topic=topic,
                order=u_order,
                name=u_name,
                description=clean_text(cfg["unit_description"])
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
                    "topic_order": 16,
                    "topic_name": topic.name,
                    "unit_order": u_order,
                    "author": "VLearn Grade 9 CRE Ingestion Engine",
                    "curriculum_framework": "CBC Kenya",
                    "enrichment_version": "v3_pedagogical"
                }
            )
            total_lessons += 1

            # Prepare Assets (3 Assets per Lesson)
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
                url=f"https://vlearn.africa/assets/diagrams/cre/grade9_topic_16_lesson_{u_order}.svg",
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
            print(f"  [+] Ingested Lesson {u_order:02d}/8: '{l_title}' (6 cards/pages, 13 blocks, 3 LessonAssets)")

        print("=" * 80)
        print("INGESTION SUMMARY FOR GRADE 9 CRE TOPIC 16:")
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
    ingest_grade9_cre_topic16()
