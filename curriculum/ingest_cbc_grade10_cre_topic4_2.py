"""
VLearn CBC Grade 10 CRE — Sub-Strand 4.2: Human Rights (Non-discrimination)
Production-Ready Ingestion & Visual Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (Level: 10)
Subject: CRE (ID: 46)
Topic: Sub-Strand 4.2: Human Rights (Non-discrimination) (Order: 20)

8 Discrete Units / Published Lessons:
  1. The Biblical Foundation of Human Dignity (Imago Dei)
  2. Equality and Oneness in Christ (Galatians 3:28)
  3. Understanding Human Rights (Secular vs. Biblical Perspectives)
  4. Forms of Discrimination and the Christian Response (James 2:1)
  5. Combating Gender-Based Violence (GBV) & Safe Reporting Pathways
  6. Protecting the Vulnerable (Orphans, Widows, Strangers)
  7. Active Citizenship and Student-Led Peace Advocacy
  8. Assessment, Synthesis and Ethical Reflection
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
    # Strip bracket citations e.g. [1], [223], [1, 2]
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Strip internal pedagogical tags
    text = re.sub(r'\[(VISUAL|BIBLE PASSAGE|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|REAL WORLD APPLICATION|BIBLICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE)[^\]]*\]', '', text, flags=re.IGNORECASE)
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
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="goldGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg1)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">IMAGO DEI: THE BIBLICAL FOUNDATION OF HUMAN DIGNITY</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Genesis 1:26-27 — God Created Humanity in His Own Image and Likeness</text>

  <!-- Central Imago Dei Hub -->
  <rect x="300" y="95" width="200" height="75" rx="12" fill="url(#goldGrad1)" stroke="#fbbf24" stroke-width="2"/>
  <text x="400" y="127" fill="#0f172a" font-family="system-ui, sans-serif" font-size="16" font-weight="800" text-anchor="middle">IMAGO DEI</text>
  <text x="400" y="148" fill="#1e293b" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">The Image of God</text>

  <!-- Connecting Lines -->
  <line x1="330" y1="170" x2="160" y2="220" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>
  <line x1="400" y1="170" x2="400" y2="220" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>
  <line x1="470" y1="170" x2="640" y2="220" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>

  <!-- 3 Foundational Pillars -->
  <!-- Pillar 1: Inherent Worth -->
  <g transform="translate(45, 220)">
    <rect width="230" height="180" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="230" height="36" rx="10" fill="#0284c7"/>
    <text x="115" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. INHERENT WORTH</text>
    <text x="15" y="65" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600">• Non-Negotiable Value</text>
    <text x="15" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Not earned by wealth,</text>
    <text x="15" y="102" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">tribal status, or ability.</text>
    <text x="15" y="128" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600">• Divine Ownership</text>
    <text x="15" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Given freely by God to</text>
    <text x="15" y="165" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">every person at conception.</text>
  </g>

  <!-- Pillar 2: Universal Equality -->
  <g transform="translate(285, 220)">
    <rect width="230" height="180" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="230" height="36" rx="10" fill="#059669"/>
    <text x="115" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. GENDER CO-EQUALITY</text>
    <text x="15" y="65" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600">• Male &amp; Female Equal</text>
    <text x="15" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">"Male and female He created</text>
    <text x="15" y="102" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">them" (Genesis 1:27).</text>
    <text x="15" y="128" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600">• Shared Dominion</text>
    <text x="15" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Both share joint stewardship</text>
    <text x="15" y="165" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">over God's creation.</text>
  </g>

  <!-- Pillar 3: Universal Dignity -->
  <g transform="translate(525, 220)">
    <rect width="230" height="180" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="230" height="36" rx="10" fill="#d97706"/>
    <text x="115" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">3. UNIVERSAL DIGNITY</text>
    <text x="15" y="65" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600">• Protects All Humans</text>
    <text x="15" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Applies to the unborn, weak,</text>
    <text x="15" y="102" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">elderly, poor, and strangers.</text>
    <text x="15" y="128" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600">• Foundation of Justice</text>
    <text x="15" y="148" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Any harm to humans insults</text>
    <text x="15" y="165" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">the Creator (Prov 14:31).</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">THEOLOGICAL AXIOM: HUMAN DIGNITY IS INTRINSIC, DIVINELY CONFERRED, AND INALIENABLE</text>
</svg>"""


def get_svg_lesson_2():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg2)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">GALATIANS 3:28: EQUALITY AND ONENESS IN CHRIST</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">"There is neither Jew nor Greek, slave nor free, male and female; for you are all one in Christ Jesus."</text>

  <!-- Left: Ancient Divided World -->
  <g transform="translate(40, 95)">
    <rect width="210" height="300" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="210" height="34" rx="10" fill="#dc2626"/>
    <text x="105" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">ANCIENT DIVISIONS</text>
    
    <rect x="15" y="50" width="180" height="65" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="25" y="70" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. Ethnic Barrier</text>
    <text x="25" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Jew vs Gentile hostility</text>
    <text x="25" y="103" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Strict religious segregation</text>

    <rect x="15" y="125" width="180" height="65" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="25" y="145" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. Social Hierarchy</text>
    <text x="25" y="163" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Slave vs Free citizen</text>
    <text x="25" y="178" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Enslaved treated as property</text>

    <rect x="15" y="200" width="180" height="65" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="25" y="220" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Gender Stratification</text>
    <text x="25" y="238" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Patriarchal domination</text>
    <text x="25" y="253" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5">Women marginalized in law</text>
  </g>

  <!-- Center Transformation Arrow -->
  <g transform="translate(265, 210)">
    <path d="M 0 35 L 45 35 L 45 15 L 85 50 L 45 85 L 45 65 L 0 65 Z" fill="#38bdf8"/>
    <text x="42" y="105" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">CROSS OF</text>
    <text x="42" y="120" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">CHRIST</text>
  </g>

  <!-- Right: Kingdom Reality in Christ -->
  <g transform="translate(365, 95)">
    <rect width="395" height="300" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="395" height="34" rx="10" fill="#059669"/>
    <text x="197" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">TRANSFORMED REALITY IN CHRIST</text>

    <!-- Pillar 1 -->
    <rect x="15" y="50" width="365" height="65" rx="6" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
    <text x="25" y="70" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" font-weight="700">✓ Trans-Ethnic Brotherhood</text>
    <text x="25" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Tribalism and racism are dismantled; all nations, tribes, and languages</text>
    <text x="25" y="104" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">stand equally redeemed before the throne of God (Revelation 7:9).</text>

    <!-- Pillar 2 -->
    <rect x="15" y="125" width="365" height="65" rx="6" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
    <text x="25" y="145" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" font-weight="700">✓ Trans-Economic Spiritual Equality</text>
    <text x="25" y="163" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Wealth does not purchase divine favor; rich and poor share identical</text>
    <text x="25" y="179" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">spiritual inheritance as children and co-heirs with Christ.</text>

    <!-- Pillar 3 -->
    <rect x="15" y="200" width="365" height="85" rx="6" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
    <text x="25" y="220" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" font-weight="700">✓ Equal Dignity and Mutual Partnership</text>
    <text x="25" y="238" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Men and women share the gift of the Holy Spirit and divine calling,</text>
    <text x="25" y="254" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">working collaboratively without chauvinism or subjugation.</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">CHRISTIAN ETHIC: IN CHRIST, DISTINCTIONS NO LONGER DEFINE SOCIAL HIERARCHY OR WORTH</text>
</svg>"""


def get_svg_lesson_3():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg3)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">HUMAN RIGHTS: SECULAR LAW VS SCRIPTURAL FOUNDATIONS</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Comparing the 1948 Universal Declaration of Human Rights (UDHR) with Biblical Moral Law</text>

  <!-- Table Headers -->
  <rect x="35" y="90" width="220" height="34" rx="6" fill="#0284c7"/>
  <text x="145" y="112" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">SECULAR RIGHT (UDHR 1948)</text>

  <rect x="265" y="90" width="240" height="34" rx="6" fill="#059669"/>
  <text x="385" y="112" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">BIBLICAL THEOLOGICAL BASIS</text>

  <rect x="515" y="90" width="250" height="34" rx="6" fill="#d97706"/>
  <text x="640" y="112" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">SCRIPTURAL COMMAND</text>

  <!-- Row 1: Right to Life -->
  <g transform="translate(35, 135)">
    <rect width="220" height="55" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <text x="15" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Right to Life (Art. 3)</text>
    <text x="15" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Protection from arbitrary killing</text>

    <rect x="230" width="240" height="55" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
    <text x="245" y="24" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Sanctity of Human Life</text>
    <text x="245" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Life is a sacred gift given by God</text>

    <rect x="480" width="250" height="55" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
    <text x="495" y="24" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Exodus 20:13; Genesis 9:6</text>
    <text x="495" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">"You shall not murder."</text>
  </g>

  <!-- Row 2: Freedom from Torture -->
  <g transform="translate(35, 200)">
    <rect width="220" height="55" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <text x="15" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Freedom from Torture (Art. 5)</text>
    <text x="15" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Inhuman/degrading treatment banned</text>

    <rect x="230" width="240" height="55" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
    <text x="245" y="24" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Body as Temple of Holy Spirit</text>
    <text x="245" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Human body deserves holy honor</text>

    <rect x="480" width="250" height="55" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
    <text x="495" y="24" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">1 Corinthians 6:19-20</text>
    <text x="495" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">"Honor God with your bodies."</text>
  </g>

  <!-- Row 3: Right to Fair Trial -->
  <g transform="translate(35, 265)">
    <rect width="220" height="55" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <text x="15" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Right to Fair Trial (Art. 10)</text>
    <text x="15" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Equal protection under the law</text>

    <rect x="230" width="240" height="55" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
    <text x="245" y="24" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Divine Impartial Justice</text>
    <text x="245" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Condemnation of bribery &amp; perjury</text>

    <rect x="480" width="250" height="55" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
    <text x="495" y="24" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Deut 16:19; Prov 17:15</text>
    <text x="495" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">"Do not pervert justice or accept bribes."</text>
  </g>

  <!-- Row 4: Right to Education & Wisdom -->
  <g transform="translate(35, 330)">
    <rect width="220" height="55" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <text x="15" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Right to Education (Art. 26)</text>
    <text x="15" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Free &amp; accessible learning</text>

    <rect x="230" width="240" height="55" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
    <text x="245" y="24" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Value of Wisdom &amp; Knowledge</text>
    <text x="245" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Pursuit of truth builds righteous character</text>

    <rect x="480" width="250" height="55" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
    <text x="495" y="24" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Proverbs 4:13; Prov 1:7</text>
    <text x="495" y="42" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">"Hold on to instruction; guard it, it is life."</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">CONCLUSION: SECULAR HUMAN RIGHTS REFLECT DIVINE MORAL LAWS ESTABLISHED BY GOD</text>
</svg>"""


def get_svg_lesson_4():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg4)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">FORMS OF DISCRIMINATION VS CHRIST'S INCLUSIVE MINISTRY</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">James 2:1 — "Believers in our glorious Lord Jesus Christ must not show favoritism."</text>

  <!-- 4 Quadrants of Discrimination vs Christ's Model -->
  <!-- Quad 1: Tribalism -->
  <g transform="translate(35, 95)">
    <rect width="350" height="145" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="350" height="28" rx="8" fill="#b91c1c"/>
    <text x="175" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. TRIBALISM &amp; ETHNIC FAVORITISM</text>
    
    <text x="15" y="50" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Sinful Pattern:</text>
    <text x="15" y="66" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Favoring one's own tribe; denying jobs or leadership to others.</text>
    
    <text x="15" y="90" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Christ's Radical Counter-Model:</text>
    <text x="15" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Jesus ministered to the Samaritan woman at the well (John 4)</text>
    <text x="15" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">and commended the Good Samaritan (Luke 10).</text>
  </g>

  <!-- Quad 2: Classism -->
  <g transform="translate(415, 95)">
    <rect width="350" height="145" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="350" height="28" rx="8" fill="#b45309"/>
    <text x="175" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. SOCIOECONOMIC CLASSISM</text>
    
    <text x="15" y="50" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Sinful Pattern:</text>
    <text x="15" y="66" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Despising poor learners, manual workers, and domestic helpers.</text>
    
    <text x="15" y="90" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Christ's Radical Counter-Model:</text>
    <text x="15" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">James 2:2-4 condemns giving front seats to the wealthy</text>
    <text x="15" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">while humiliating the poor in ragged clothes.</text>
  </g>

  <!-- Quad 3: Gender Bias -->
  <g transform="translate(35, 255)">
    <rect width="350" height="145" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect width="350" height="28" rx="8" fill="#6d28d9"/>
    <text x="175" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. GENDER BIAS &amp; MISOGYNY</text>
    
    <text x="15" y="50" fill="#ddd6fe" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Sinful Pattern:</text>
    <text x="15" y="66" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Silencing women, denying girls education, or practicing FGM.</text>
    
    <text x="15" y="90" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Christ's Radical Counter-Model:</text>
    <text x="15" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Jesus taught Mary of Bethany as a disciple (Luke 10:38-42)</text>
    <text x="15" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">and chose women as first resurrection witnesses (Luke 24).</text>
  </g>

  <!-- Quad 4: Disability Exclusion -->
  <g transform="translate(415, 255)">
    <rect width="350" height="145" rx="8" fill="#1e293b" stroke="#06b6d4" stroke-width="1.5"/>
    <rect width="350" height="28" rx="8" fill="#0e7490"/>
    <text x="175" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">4. DISABILITY EXCLUSION</text>
    
    <text x="15" y="50" fill="#a5f3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Sinful Pattern:</text>
    <text x="15" y="66" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Shunning or ridiculing individuals with physical/mental challenges.</text>
    
    <text x="15" y="90" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Christ's Radical Counter-Model:</text>
    <text x="15" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Jesus touched and healed lepers, blind Bartimaeus (Mark 10),</text>
    <text x="15" y="122" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">and invited people with disabilities to the kingdom feast (Luke 14).</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">KINGDOM PRINCIPLE: LOVE DISMANTLES PREJUDICE THROUGH PROACTIVE INCLUSION</text>
</svg>"""


def get_svg_lesson_5():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg5)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#f87171" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">COMBATING GENDER-BASED VIOLENCE: SAFE REPORTING PATHWAY</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Psalm 11:5 — God Condemns Violence; Stand Up for Safety, Dignity &amp; Justice</text>

  <!-- 4-Step Flowchart -->
  <!-- Step 1: Ensure Immediate Safety -->
  <g transform="translate(30, 95)">
    <rect width="165" height="280" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <rect width="165" height="34" rx="10" fill="#dc2626"/>
    <text x="82" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STEP 1: SAFETY</text>

    <circle cx="82" cy="75" r="22" fill="#ef4444" fill-opacity="0.2" stroke="#ef4444" stroke-width="2"/>
    <text x="82" y="83" fill="#ef4444" font-family="system-ui, sans-serif" font-size="20" font-weight="800" text-anchor="middle">🛡️</text>

    <text x="15" y="125" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Immediate Action:</text>
    <text x="15" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Remove yourself from</text>
    <text x="15" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">immediate danger.</text>
    <text x="15" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Seek a safe space</text>
    <text x="15" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">(staffroom, church,</text>
    <text x="15" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">or trusted relative).</text>
    <text x="15" y="245" fill="#f87171" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Preserve evidence!</text>
  </g>

  <!-- Arrow 1 -->
  <path d="M 200 235 L 225 235" stroke="#f87171" stroke-width="3"/>
  <circle cx="212" cy="235" r="4" fill="#f87171"/>

  <!-- Step 2: Report to Trusted Adult -->
  <g transform="translate(230, 95)">
    <rect width="165" height="280" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <rect width="165" height="34" rx="10" fill="#d97706"/>
    <text x="82" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STEP 2: DISCLOSE</text>

    <circle cx="82" cy="75" r="22" fill="#f59e0b" fill-opacity="0.2" stroke="#f59e0b" stroke-width="2"/>
    <text x="82" y="83" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="20" font-weight="800" text-anchor="middle">🗣️</text>

    <text x="15" y="125" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Tell a Trusted Adult:</text>
    <text x="15" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Guidance counselor</text>
    <text x="15" y="165" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Deputy Principal</text>
    <text x="15" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Parent / Guardian</text>
    <text x="15" y="205" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Chaplain / Pastor</text>
    <text x="15" y="245" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Break the silence!</text>
  </g>

  <!-- Arrow 2 -->
  <path d="M 400 235 L 425 235" stroke="#f59e0b" stroke-width="3"/>
  <circle cx="412" cy="235" r="4" fill="#f59e0b"/>

  <!-- Step 3: Medical & Legal Support (116) -->
  <g transform="translate(430, 95)">
    <rect width="165" height="280" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect width="165" height="34" rx="10" fill="#0284c7"/>
    <text x="82" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STEP 3: PROFESSIONAL</text>

    <circle cx="82" cy="75" r="22" fill="#38bdf8" fill-opacity="0.2" stroke="#38bdf8" stroke-width="2"/>
    <text x="82" y="83" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="800" text-anchor="middle">📞</text>

    <text x="15" y="125" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Emergency Resources:</text>
    <text x="15" y="145" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="800">• Call 116 (Toll-Free)</text>
    <text x="15" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Childline Kenya helpline</text>
    <text x="15" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Urgent medical clinic</text>
    <text x="15" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">(PEP within 72 hrs)</text>
    <text x="15" y="225" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Police Gender Desk</text>
    <text x="15" y="245" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Legal Protection!</text>
  </g>

  <!-- Arrow 3 -->
  <path d="M 600 235 L 625 235" stroke="#34d399" stroke-width="3"/>
  <circle cx="612" cy="235" r="4" fill="#34d399"/>

  <!-- Step 4: Holistic Healing & Restoration -->
  <g transform="translate(630, 95)">
    <rect width="140" height="280" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <rect width="140" height="34" rx="10" fill="#059669"/>
    <text x="70" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">STEP 4: RESTORE</text>

    <circle cx="70" cy="75" r="22" fill="#34d399" fill-opacity="0.2" stroke="#34d399" stroke-width="2"/>
    <text x="70" y="83" fill="#34d399" font-family="system-ui, sans-serif" font-size="20" font-weight="800" text-anchor="middle">🕊️</text>

    <text x="10" y="125" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Long-Term Care:</text>
    <text x="10" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Trauma counseling</text>
    <text x="10" y="165" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Pastoral prayer</text>
    <text x="10" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Peer support</text>
    <text x="10" y="205" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Zero stigma in school</text>
    <text x="10" y="245" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Total Healing!</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">KENYA NATIONAL HELPLINE: CALL 116 (CHILDLINE KENYA) OR 1195 (GBV HELPLINE) FOR CONFIDENTIAL SUPPORT</text>
</svg>"""


def get_svg_lesson_6():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg6)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">PROTECTING THE VULNERABLE: THE BIBLICAL SOCIAL SAFETY NET</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Deuteronomy 24:19-21 &amp; James 1:27 — God's Mandate for Orphans, Widows &amp; Strangers</text>

  <!-- Central Box: The Triad of Vulnerability -->
  <g transform="translate(250, 95)">
    <rect width="300" height="65" rx="10" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <text x="150" y="28" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">THE TRIAD OF VULNERABILITY</text>
    <text x="150" y="48" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">The Orphan • The Widow • The Foreign Stranger</text>
  </g>

  <!-- Left Pillar: Old Testament Legal Safety Net -->
  <g transform="translate(40, 185)">
    <rect width="340" height="210" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="340" height="34" rx="10" fill="#d97706"/>
    <text x="170" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">OLD TESTAMENT COVENANT PROVISIONS</text>

    <text x="15" y="60" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. Agricultural Gleaning (Deut 24:19-21):</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Farmers forbidden from harvesting field corners or olive</text>
    <text x="15" y="94" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">branches twice; leftover grain preserved for the poor.</text>

    <text x="15" y="122" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. Triennial Tithe for the Destitute (Deut 14:28-29):</text>
    <text x="15" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Every third year, community produce stored in town</text>
    <text x="15" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">to feed fatherless, widows, and resident aliens.</text>

    <text x="15" y="184" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Kinsman-Redeemer (Ruth 2-4):</text>
    <text x="15" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Familial protection to restore land and protect dignity.</text>
  </g>

  <!-- Right Pillar: New Testament Pure Religion -->
  <g transform="translate(420, 185)">
    <rect width="340" height="210" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="340" height="34" rx="10" fill="#059669"/>
    <text x="170" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">NEW TESTAMENT KINGDOM ETHIC</text>

    <text x="15" y="60" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. Pure Religion Defined (James 1:27):</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">"Religion that God our Father accepts as pure and</text>
    <text x="15" y="94" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">faultless is to look after orphans and widows."</text>

    <text x="15" y="122" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. Early Church Daily Food Roster (Acts 6:1-6):</text>
    <text x="15" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Deacons appointed to ensure non-discrimination in</text>
    <text x="15" y="156" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">daily bread distribution to Hebraic &amp; Greek widows.</text>

    <text x="15" y="184" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Compassionate Welcoming of Refugees (Heb 13:2):</text>
    <text x="15" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Hospitality to strangers as an expression of divine love.</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">COVENANT RULE: A NATION'S MORAL INTEGRITY IS MEASURED BY HOW IT TREATS THE MOST VULNERABLE</text>
</svg>"""


def get_svg_lesson_7():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg7)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">STUDENT-LED PEACE ADVOCACY &amp; ACTIVE CITIZENSHIP</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Matthew 5:9 — "Blessed are the peacemakers, for they will be called children of God."</text>

  <!-- 4-Stage Action Cycle -->
  <!-- Stage 1: Identify Injustice -->
  <g transform="translate(40, 95)">
    <rect width="160" height="280" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="160" height="32" rx="10" fill="#0284c7"/>
    <text x="80" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. IDENTIFY ISSUE</text>

    <circle cx="80" cy="70" r="20" fill="#0284c7" fill-opacity="0.3"/>
    <text x="80" y="78" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" text-anchor="middle">🔍</text>

    <text x="12" y="115" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Campus Realities:</text>
    <text x="12" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Bullying of Form 1s</text>
    <text x="12" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Exclusion of poor</text>
    <text x="12" y="175" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Tribal clique gossip</text>
    <text x="12" y="195" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Teasing disabled peers</text>
    <text x="12" y="240" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" font-style="italic">Name the injustice</text>
  </g>

  <!-- Arrow 1 -->
  <path d="M 205 235 L 225 235" stroke="#38bdf8" stroke-width="2"/>

  <!-- Stage 2: Biblical Anchor -->
  <g transform="translate(230, 95)">
    <rect width="160" height="280" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="160" height="32" rx="10" fill="#d97706"/>
    <text x="80" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. SCRIPTURAL ANCHOR</text>

    <circle cx="80" cy="70" r="20" fill="#d97706" fill-opacity="0.3"/>
    <text x="80" y="78" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="18" text-anchor="middle">📖</text>

    <text x="12" y="115" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Moral Mandates:</text>
    <text x="12" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Galatians 3:28</text>
    <text x="12" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">(One Body in Christ)</text>
    <text x="12" y="175" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Luke 6:31</text>
    <text x="12" y="190" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">(Golden Rule)</text>
    <text x="12" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Prov 31:8-9</text>
    <text x="12" y="230" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">(Speak for the voiceless)</text>
  </g>

  <!-- Arrow 2 -->
  <path d="M 395 235 L 415 235" stroke="#f59e0b" stroke-width="2"/>

  <!-- Stage 3: Project Actions -->
  <g transform="translate(420, 95)">
    <rect width="160" height="280" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="160" height="32" rx="10" fill="#059669"/>
    <text x="80" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. TANGIBLE ACTION</text>

    <circle cx="80" cy="70" r="20" fill="#059669" fill-opacity="0.3"/>
    <text x="80" y="78" fill="#34d399" font-family="system-ui, sans-serif" font-size="18" text-anchor="middle">🎨</text>

    <text x="12" y="115" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">School Campaigns:</text>
    <text x="12" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Anti-bullying posters</text>
    <text x="12" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• "Open Table" lunch</text>
    <text x="12" y="175" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• CU peace workshops</text>
    <text x="12" y="195" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Safe suggestion box</text>
    <text x="12" y="240" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" font-style="italic">Lead by serving</text>
  </g>

  <!-- Arrow 3 -->
  <path d="M 585 235 L 605 235" stroke="#34d399" stroke-width="2"/>

  <!-- Stage 4: Cultural Transformation -->
  <g transform="translate(610, 95)">
    <rect width="150" height="280" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="150" height="32" rx="10" fill="#7e22ce"/>
    <text x="75" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">4. CULTURE SHIFT</text>

    <circle cx="75" cy="70" r="20" fill="#7e22ce" fill-opacity="0.3"/>
    <text x="75" y="78" fill="#c084fc" font-family="system-ui, sans-serif" font-size="18" text-anchor="middle">🕊️</text>

    <text x="10" y="115" fill="#c084fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Community Impact:</text>
    <text x="10" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Safe school climate</text>
    <text x="10" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Zero stigma culture</text>
    <text x="10" y="175" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Mutual respect</text>
    <text x="10" y="195" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Restorative justice</text>
    <text x="10" y="240" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9.5" font-style="italic">Shalom realized</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">STUDENT CALLING: BE PROACTIVE AMBASSADORS OF CHRIST'S RECONCILIATION AND HEALING</text>
</svg>"""


def get_svg_lesson_8():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg8" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg8)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">TOPIC 4.2 SYNTHESIS: BIBLICAL ETHICS &amp; HUMAN RIGHTS MATRIX</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Comprehensive Review of Human Dignity, Equality, Protection &amp; Peacemaking</text>

  <!-- 4 Core Competency Cards -->
  <!-- Card 1: Dignity -->
  <g transform="translate(35, 95)">
    <rect width="350" height="145" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="350" height="28" rx="8" fill="#0284c7"/>
    <text x="175" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. IMAGO DEI &amp; INHERENT DIGNITY</text>
    <text x="15" y="52" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Anchor: Genesis 1:26-27</text>
    <text x="15" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Every person bears God's image; value cannot be revoked.</text>
    <text x="15" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Male and female created co-equal in status and worth.</text>
    <text x="15" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Human rights derive directly from God, not government grants.</text>
    <text x="15" y="128" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Application: Protect life and treat all people with reverence.</text>
  </g>

  <!-- Card 2: Equality -->
  <g transform="translate(415, 95)">
    <rect width="350" height="145" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="350" height="28" rx="8" fill="#059669"/>
    <text x="175" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. ONENESS IN CHRIST &amp; NON-DISCRIMINATION</text>
    <text x="15" y="52" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Anchor: Galatians 3:28 &amp; James 2:1</text>
    <text x="15" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Elimination of ethnic, social class, and gender superiority.</text>
    <text x="15" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Favoritism and tribal chauvinism are explicit sins against God.</text>
    <text x="15" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Active hospitality and inclusive leadership in church &amp; school.</text>
    <text x="15" y="128" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Application: Eradicate tribalism, bullying, and favoritism.</text>
  </g>

  <!-- Card 3: Vulnerability & Protection -->
  <g transform="translate(35, 255)">
    <rect width="350" height="145" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="350" height="28" rx="8" fill="#d97706"/>
    <text x="175" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. SOCIAL WELFARE &amp; COMBATING VIOLENCE</text>
    <text x="15" y="52" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Anchor: Deut 24:19-21, Psalm 11:5 &amp; James 1:27</text>
    <text x="15" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Gleaning laws protect orphans, widows, and foreign refugees.</text>
    <text x="15" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• God hates violence; GBV and abuse must be reported safely.</text>
    <text x="15" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Emergency support: Childline Kenya 116 &amp; GBV helpline 1195.</text>
    <text x="15" y="128" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Application: Stand with victims, practice pure religion.</text>
  </g>

  <!-- Card 4: Active Citizenship -->
  <g transform="translate(415, 255)">
    <rect width="350" height="145" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="350" height="28" rx="8" fill="#7e22ce"/>
    <text x="175" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">4. ACTIVE ADVOCACY &amp; PEACEMAKING</text>
    <text x="15" y="52" fill="#d8b4fe" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Anchor: Matthew 5:9 &amp; Luke 6:31</text>
    <text x="15" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Peacemaking is proactive reconciliation, not passive silence.</text>
    <text x="15" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Student-led initiatives create lasting cultural change.</text>
    <text x="15" y="106" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">• Foster school unity through 'One Body' advocacy projects.</text>
    <text x="15" y="128" fill="#a855f7" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Application: Exemplify Christ-centered servant leadership.</text>
  </g>

  <text x="400" y="422" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">TRANSFORMATIVE OUTCOME: LIVE OUT GOD'S KINGDOM PRINCIPLES OF JUSTICE, MERCY AND INTEGRITY</text>
</svg>"""


# ─── LESSONS DATA CONFIGURATION (8 LESSONS) ───────────────────────────────────

LESSONS_CONFIG = [
    # -------------------------------------------------------------------------
    # LESSON 1: The Biblical Foundation of Human Dignity
    # -------------------------------------------------------------------------
    {
        "unit_order": 1,
        "unit_name": "4.2.1 The Biblical Foundation of Human Dignity",
        "unit_description": "Explore the biblical grounding of human dignity in the creation account of Genesis, examining the concept of Imago Dei and its non-negotiable ethical implications.",
        "lesson_title": "The Biblical Foundation of Human Dignity",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Michelangelo_-_Creation_of_Adam_%28cropped%29.jpg/800px-Michelangelo_-_Creation_of_Adam_%28cropped%29.jpg",
            "title": "Visual Hook: The Creation of Adam (Imago Dei)",
            "author": "Michelangelo Buonarroti (Sistine Chapel)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Michelangelo's iconic fresco depicting God creating humanity, illustrating the profound biblical reality that human beings are formed in the divine image and likeness (Genesis 1:26-27)."
        },
        "youtube": {
            "youtube_id": "YbipxEDPryg",
            "title": "BibleProject: Image of God (Imago Dei)",
            "description": "Explores how the biblical concept of the Image of God confers sacred, inherent dignity upon every human being and calls humanity to royal stewardship."
        },
        "svg_fn": get_svg_lesson_1,
        "goals": [
            "Explain the meaning and theological significance of the Latin term Imago Dei (Image of God).",
            "Analyze Genesis 1:26-27 to establish the three foundational pillars of inherent human dignity and gender co-equality.",
            "Evaluate why Christian ethics treats human rights as inalienable and divinely given rather than granted by states."
        ],
        "intro": "Think of a time when someone went out of their way to treat you with complete respect, even if you were the youngest or least influential person in the room. How did that make you feel?\n\nWhy is it vital that every human being, regardless of background, wealth, or gender, is treated with equal, unshakeable respect? In secular society, human rights are often defined by legal agreements, but the Christian understanding begins in the opening chapter of Genesis with a divine truth: all people are created in the image of God.",
        "core_scripture": "### Genesis 1:26-27 — The Divine Creation Account\n\n> *\"Then God said, 'Let us make mankind in our image, in our likeness, so that they may rule over the fish in the sea and the birds in the sky, over the livestock and all the wild animals, and over all the creatures that move along the ground.' So God created mankind in his own image, in the image of God he created them; male and female he created them.\"*\n\nThis foundational passage establishes that human beings occupy a unique, sacred position in creation as living representatives and royal image-bearers of the Almighty God.",
        "theological_pillars": "### The Three Foundational Theological Pillars of Human Dignity\n\n1. **Inherent Worth:** Human worth is not earned through athletic prowess, high academic grades, financial wealth, or tribal origin. It is an unchangeable, inherent gift conferred by the Creator.\n2. **Universal Scope:** Every human being—from the unborn child and the person with disabilities to the elderly and the homeless stranger—carries this sacred imprint and commands absolute respect.\n3. **Co-Equality of Genders:** Genesis explicitly records that *both* male and female were created in God's image, establishing complete spiritual and moral co-equality from creation.",
        "deep_dive": "### Theological Axioms & Cultural Subversion\n\n- **Inalienability:** Because dignity is bestowed by God, no earthly government, employer, or cultural tradition has the authority to revoke or diminish a person's intrinsic worth.\n- **Accountability to God:** In Proverbs 14:31, Scripture warns: *'Whoever oppresses the poor shows contempt for their Maker, but whoever is kind to the needy honors God.'* How we treat fellow human beings directly reflects our attitude toward God.\n- **Contrast with Ancient Near Eastern Myths:** In Babylonian creation myths (such as *Enuma Elish*), ordinary humans were created as slaves to feed the gods, while only the king was considered divine. Genesis radically subverted this hierarchy by declaring *every* human being to be God's royal image-bearer.",
        "practical": {
            "title": "Practical Life Toolkit: Honoring Imago Dei on Campus",
            "steps": [
                "Step 1: Recognize the Sacred — When interacting with school support staff, younger students, or peers with special needs, consciously remember that they are God's royal image-bearers.",
                "Step 2: Check Dehumanizing Language — Refuse to use derogatory tribal labels, hurtful nicknames, or humiliating comments in conversations or social media groups.",
                "Step 3: Stand in the Gap — When you witness someone being degraded, excluded, or bullied, intervene constructively to affirm their dignity."
            ]
        },
        "kenyan_context": "In Kenyan secondary schools and neighborhoods, respecting human dignity means treating support staff, groundskeepers, new Form 1 learners, and peers from minority communities with total courtesy, warm affirmation, and Christ-like reverence.",
        "reflection": "### Reflection: The Sanctity of Every Life\n\nIf every person is created in God's image, there are no 'ordinary' or 'disposable' human beings. When we look into the eyes of a classmate from another ethnic background or a street child in town, we are looking at someone deeply loved by God and crafted with eternal significance.\n\nLiving out this truth requires Christians to champion the rights of the unborn, the sick, the impoverished, and the forgotten.",
        "takeaways": [
            "Human dignity is grounded in Imago Dei (the Image of God), established in Genesis 1:26-27.",
            "Dignity is intrinsic and inalienable; it cannot be granted or revoked by human institutions.",
            "Male and female share identical status, worth, and royal stewardship before the Creator.",
            "Oppressing or degrading any human being is a direct sin against God the Creator (Proverbs 14:31)."
        ],
        "mcq": {
            "question": "Which Latin theological term translates to 'Image of God', establishing the foundational biblical basis for universal human rights?",
            "options": [
                "A) Sola Scriptura",
                "B) Imago Dei",
                "C) Corpus Christi",
                "D) Pax Romana"
            ],
            "answer": "B",
            "explanation": "Imago Dei is the Latin theological term for 'Image of God' (Genesis 1:26-27), affirming that all humans possess non-negotiable inherent worth and dignity bestowed directly by the Creator."
        }
    },

    # -------------------------------------------------------------------------
    # LESSON 2: Equality and Oneness in Christ
    # -------------------------------------------------------------------------
    {
        "unit_order": 2,
        "unit_name": "4.2.2 Equality and Oneness in Christ",
        "unit_description": "Analyze Apostle Paul's radical message of equality in Galatians 3:28, examining how the Gospel dismantles ethnic, socioeconomic, and gender barriers in the Christian community.",
        "lesson_title": "Equality and Oneness in Christ",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Valentin_de_Boulogne_-_Saint_Paul_Writing_His_Epistles_-_1940.536_-_Museum_of_Fine_Arts.jpg/800px-Valentin_de_Boulogne_-_Saint_Paul_Writing_His_Epistles_-_1940.536_-_Museum_of_Fine_Arts.jpg",
            "title": "Visual Hook: Apostle Paul Writing His Epistles",
            "author": "Valentin de Boulogne",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Apostle Paul penning his epistles, in which he proclaimed the revolutionary truth that all dividing walls of ethnicity, social status, and gender are shattered in Jesus Christ."
        },
        "youtube": {
            "youtube_id": "ak06MSETeo4",
            "title": "BibleProject: Galatians",
            "description": "Visual overview of Paul's letter to the Galatians, detailing how the Gospel creates a multi-ethnic, unified family of God based on faith and grace rather than external divisions."
        },
        "svg_fn": get_svg_lesson_2,
        "goals": [
            "Explain the historical and cultural barriers of the Greco-Roman world that Paul confronted in Galatians 3:28.",
            "Analyze the three major divisions dismantled by the Gospel: ethnic (Jew/Gentile), social class (slave/free), and gender (male/female).",
            "Apply the principle of unity in Christ to combat tribalism, social discrimination, and gender bias in contemporary Kenyan communities."
        ],
        "intro": "In the ancient Roman Empire, society was rigidly divided. Roman citizens looked down on foreigners, masters held absolute life-and-death power over slaves, and men held dominant legal authority over women.\n\nInto this deeply divided world, the Apostle Paul released a theological bombshell in his letter to the Galatian churches. He announced that through baptism into Jesus Christ, all these man-made barriers were permanently abolished.",
        "core_scripture": "### Galatians 3:28 — The Magna Carta of Christian Equality\n\n> *\"There is neither Jew nor Gentile, neither slave nor free, nor is there male and female, for you are all one in Christ Jesus.\"*\n\nThrough faith in Jesus Christ, believers are adopted into one multi-ethnic, egalitarian family where worldly hierarchies lose all spiritual and moral validity.",
        "theological_pillars": "### Dismantling the Three Ancient Dividing Walls\n\n1. **No Ethnic Discrimination (Neither Jew nor Gentile):** In ancient Judaism, Gentiles were considered ritually unclean. Paul declared that racial and ethnic chauvinism is a denial of the Gospel. No tribe or race holds a superior monopoly on God's grace.\n2. **No Social Class Divisions (Neither Slave nor Free):** Roman law classified slaves as property (*res*). In the body of Christ, a slave and a master drank from the same communion cup as equal brothers (Philemon 1:16).\n3. **Equal Dignity and Inheritance (Nor Male and Female):** Paul radically shattered patriarchal prejudice, affirming women as equal co-heirs of God's eternal covenant promises.",
        "deep_dive": "### Theological Depth: Clothed with Christ\n\n- **Baptismal Identity:** In Galatians 3:27, Paul explains that all who are baptized into Christ have *'clothed themselves with Christ'*. Our primary identity is no longer defined by tribal ancestry or bank accounts, but by our belonging to Christ.\n- **Reconciliation at the Cross:** Ephesians 2:14-16 emphasizes that Christ *'has destroyed the barrier, the dividing wall of hostility'* to create one new humanity out of divided groups.\n- **The Sin of Tribalism:** When Christians prioritize tribal loyalty over kingdom solidarity, they commit a form of idolatry that denies the unifying power of the Cross.",
        "practical": {
            "title": "Practical Action: Modeling Christian Unity in Schools",
            "steps": [
                "Step 1: Diversify Study Circles — Intentionally form academic study groups and dormitory friendships across different ethnic and regional backgrounds.",
                "Step 2: Challenge Exclusive Cliques — Open up dining hall tables and youth fellowship circles to anyone who feels isolated or left out.",
                "Step 3: Promote Equal Leadership Opportunities — Support both young men and women equally when electing student council executives and club leaders."
            ]
        },
        "kenyan_context": "In Kenya's multi-ethnic tapestry, Galatians 3:28 provides the ultimate antidote to negative ethnicity and political tribalism, uniting students from all 47 counties under one banner of faith and national brotherhood.",
        "reflection": "### Critical Thinking & Ethical Reflection\n\nIf Galatians 3:28 declares that we are all one in Christ, why do some churches and institutions still struggle with ethnic favoritism and gender inequality?\n\nAuthentic Christian faith requires not just intellectual agreement with Paul's words, but courageous action to welcome outsiders, dismantle prejudice, and build a culture of true equality.",
        "takeaways": [
            "Galatians 3:28 serves as the Magna Carta of Christian equality and non-discrimination.",
            "The Gospel abolishes ethnic chauvinism, social class superiority, and gender subjugation.",
            "Our supreme identity is being 'clothed with Christ' as equal sons and daughters of God.",
            "Tribalism and favoritism are spiritual compromises that violate Christian oneness."
        ],
        "mcq": {
            "question": "According to Galatians 3:28, which three major social divisions are abolished in Jesus Christ?",
            "options": [
                "A) Kings and subjects, soldiers and civilians, rich and poor",
                "B) Jew and Gentile, slave and free, male and female",
                "C) Pharisees and Sadducees, Romans and Greeks, young and old",
                "D) Priests and Levites, citizens and foreigners, masters and servants"
            ],
            "answer": "B",
            "explanation": "Galatians 3:28 explicitly names the three profound social barriers of the ancient world: ethnic (Jew nor Gentile), socioeconomic (slave nor free), and gender (male and female), declaring all believers one in Christ."
        }
    },

    # -------------------------------------------------------------------------
    # LESSON 3: Understanding Human Rights
    # -------------------------------------------------------------------------
    {
        "unit_order": 3,
        "unit_name": "4.2.3 Understanding Human Rights",
        "unit_description": "Examine the historical origin and principles of the Universal Declaration of Human Rights (UDHR) and discover how secular human rights are rooted in biblical moral law.",
        "lesson_title": "Understanding Human Rights",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Eleanor_Roosevelt_UDHR.jpg/800px-Eleanor_Roosevelt_UDHR.jpg",
            "title": "Visual Hook: Eleanor Roosevelt and the UDHR (1948)",
            "author": "United Nations / FDR Presidential Library",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Eleanor Roosevelt holding the Universal Declaration of Human Rights in 1948, which codified fundamental human dignity and moral freedoms for all global citizens following World War II."
        },
        "youtube": {
            "youtube_id": "A14THPoc4-4",
            "title": "BibleProject: Justice (Mishpat and Tzedakah)",
            "description": "Explores the biblical concepts of justice and righteousness, showing how God requires restorative care and legal protection for every human life."
        },
        "svg_fn": get_svg_lesson_3,
        "goals": [
            "Define the concept of human rights and explain the background of the 1948 Universal Declaration of Human Rights (UDHR).",
            "Identify key fundamental rights, including the Right to Life, Freedom from Torture, Fair Trial, and Right to Education.",
            "Compare secular human rights frameworks with their biblical theological groundings in the Old and New Testaments."
        ],
        "intro": "What are human rights? Human rights are moral and legal entitlements that belong to every person simply by virtue of being human.\n\nFollowing the horrors of World War II and the Holocaust, the United Nations adopted the **Universal Declaration of Human Rights (UDHR)** in 1948, containing 30 articles that define international standards of dignity. While some people assume human rights are a modern secular invention, their core principles were pioneered thousands of years earlier in the biblical narrative.",
        "core_scripture": "### Scriptural Parallels to Fundamental Human Rights\n\n1. **The Right to Life (UDHR Article 3):** Grounded in Genesis 9:6 and Exodus 20:13 (*'You shall not murder'*). Life is sacred because God is the sovereign giver of life.\n2. **Freedom from Torture & Cruel Treatment (UDHR Article 5):** Grounded in 1 Corinthians 6:19-20. The human body is the temple of the Holy Spirit and must be treated with honor.\n3. **The Right to a Fair Trial (UDHR Article 10):** Grounded in Deuteronomy 16:19 (*'Do not pervert justice or show partiality. Do not accept a bribe.'*) and Proverbs 17:15.\n4. **The Right to Education (UDHR Article 26):** Grounded in Proverbs 4:13 (*'Hold on to instruction, do not let it go; guard it, for it is your life'*).",
        "theological_pillars": "### The Biblical Roots of Modern Rights\n\nFar from being an alien philosophy, international human rights law reflects the moral jurisprudence established in Old Testament prophetic literature and New Testament ethics:\n- **Individual Liberty & Conscience:** Rooted in free will and personal moral responsibility before God.\n- **Equality Before the Law:** Rooted in God's refusal to show favoritism or accept bribes from powerful rulers (2 Chronicles 19:7).\n- **Protection of the Weak:** Rooted in the prophetic duty to defend widows, orphans, and aliens against corrupt elites.",
        "deep_dive": "### Addressing Misconceptions: Rights & Responsibilities\n\n- **Misconception:** 'Human rights are a Western, foreign ideology that conflicts with African and Christian values.'\n- **Correction:** The demand for justice, fair treatment, accountability of rulers, and care for the weak originated directly from the Hebrew prophets (Amos, Micah, Isaiah) and Jesus Christ. Biblical justice (*Mishpat* and *Tzedakah*) requires active defense of the rights of those who cannot defend themselves (Proverbs 31:8-9).\n- **Rights and Responsibilities:** In Christian ethics, rights are paired with moral responsibility. We do not claim rights merely for selfish indulgence, but to honor God and serve our neighbors with integrity.",
        "practical": {
            "title": "Comparative Analysis Matrix: Secular Law vs Biblical Ethic",
            "steps": [
                "Dimension 1: Source — Secular law bases rights on social contracts and UN conventions; Christian faith bases rights on the eternal character and will of God.",
                "Dimension 2: Scope — Secular law enforces rights through police and courts; Christian faith calls for internal moral transformation, love, and sacrificial service.",
                "Dimension 3: Goal — Secular rights aim for peaceful civic order; Biblical rights aim for shalom (wholeness, justice, harmony with God, neighbor, and creation)."
            ]
        },
        "kenyan_context": "In Kenya, Chapter 4 of the 2010 Constitution enshrines a robust Bill of Rights that mirrors these timeless biblical principles, guaranteeing life, human dignity, equality, and protection for all citizens.",
        "reflection": "### Reflection on Constitutional Rights in Kenya\n\nChapter 4 of the Constitution of Kenya (2010) contains a comprehensive Bill of Rights guaranteeing life, human dignity, equality, freedom from discrimination, and access to justice.\n\nAs Christian citizens, we are called to celebrate and defend these constitutional protections as practical expressions of God's moral law in our society.",
        "takeaways": [
            "Human rights define standards of dignity, equality, and protection belonging to all human beings.",
            "The 1948 UDHR established 30 fundamental international human rights articles.",
            "Core human rights (Right to Life, Fair Trial, Freedom from Torture) are rooted in biblical moral law.",
            "Rights in Christianity are inseparable from moral duties to love God and serve our neighbors."
        ],
        "mcq": {
            "question": "Which scriptural command provides the direct theological grounding for the secular 'Right to Life' (UDHR Article 3)?",
            "options": [
                "A) 'Do not wear clothing woven of two kinds of material' (Leviticus 19:19)",
                "B) 'You shall not murder' (Exodus 20:13 / Genesis 9:6)",
                "C) 'Do not muzzle an ox while it is treading out the grain' (Deuteronomy 25:4)",
                "D) 'Build a parapet around your roof' (Deuteronomy 22:8)"
            ],
            "answer": "B",
            "explanation": "Exodus 20:13 ('You shall not murder') and Genesis 9:6 affirm the absolute sanctity of human life as a sacred gift from God, providing the foundational moral basis for the Right to Life."
        }
    },

    # -------------------------------------------------------------------------
    # LESSON 4: Forms of Discrimination and the Christian Response
    # -------------------------------------------------------------------------
    {
        "unit_order": 4,
        "unit_name": "4.2.4 Forms of Discrimination and the Christian Response",
        "unit_description": "Identify common forms of discrimination (tribalism, classism, sexism, disability bias) and formulate proactive Christian responses grounded in James 2:1 and Christ's ministry.",
        "lesson_title": "Forms of Discrimination and the Christian Response",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/1963_March_on_Washington.jpg/800px-1963_March_on_Washington.jpg",
            "title": "Visual Hook: Historic March for Equality and Justice",
            "author": "National Archives and Records Administration",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Citizens marching peacefully for equality and civil rights during the historic 1963 March on Washington, reflecting biblical calls to stand against discrimination and injustice."
        },
        "youtube": {
            "youtube_id": "qn-hLHWw9Tg",
            "title": "BibleProject: The Book of James",
            "description": "Visual walkthrough of the Book of James, highlighting James' passionate rebuke of favoritism, economic snobbery, and hypocrisy in the Christian fellowship."
        },
        "svg_fn": get_svg_lesson_4,
        "goals": [
            "Define discrimination and differentiate between ethnic bias, socioeconomic classism, gender discrimination, and disability exclusion.",
            "Analyze James 2:1-9 to explain why showing favoritism is an explicit sin against God's law.",
            "Examine how Jesus Christ actively countered social prejudice through His ministry to outcasts, women, the poor, and the sick."
        ],
        "intro": "Discrimination occurs when an individual or group is treated unfairly, denied opportunities, or subjected to prejudice based on arbitrary characteristics rather than their personal character.\n\nWhether in school clubs, neighborhood communities, or national politics, discrimination tears apart the fabric of human society. James 2:1 issues a direct command: *'My brothers and sisters, believers in our glorious Lord Jesus Christ must not show favoritism.'*",
        "core_scripture": "### James 2:1-9 — The Royal Law of Love vs Partiality\n\n> *\"My brothers and sisters, believers in our glorious Lord Jesus Christ must not show favoritism. Suppose a man comes into your meeting wearing a gold ring and fine clothes, and a poor man in filthy old clothes also comes in. If you show special attention to the man wearing fine clothes and say, 'Here's a good seat for you,' but say to the poor man, 'You stand there' or 'Sit on the floor by my feet,' have you not discriminated among yourselves and become judges with evil thoughts?\"*\n\nJames concludes that showing favoritism violates the Royal Law: *'Love your neighbor as yourself'* (James 2:8).",
        "theological_pillars": "### Four Pervasive Forms of Discrimination\n\n1. **Tribalism & Ethnic Bias:** Favoring one's ethnic group in job recruitment or school awards while rejecting qualified peers from other communities.\n2. **Socioeconomic Classism:** Elevating wealthy patrons while mistreating domestic workers, street vendors, and low-income students.\n3. **Gender Discrimination & Misogyny:** Denying girls leadership opportunities or subjecting women to disinheritance and harmful traditional practices.\n4. **Disability Discrimination:** Excluding individuals with physical, sensory, or neurodivergent conditions from accessible education and worship.",
        "deep_dive": "### Christ's Revolutionary Inclusive Ministry\n\n- **Touching the Untouchable:** Jesus broke ceremonial taboos by physically touching lepers (Mark 1:40-42) and bleeding women (Luke 8:43-48) to restore their health and community status.\n- **Ministering to Ethnic Enemies:** Jesus intentionally traveled through Samaria to minister to the Samaritan woman (John 4) and praised the faith of a Roman centurion (Luke 7:1-10).\n- **Elevating the Poor:** In Luke 4:18, Jesus inaugurated His public mission by declaring: *'The Spirit of the Lord is on me, because he has anointed me to proclaim good news to the poor.'*",
        "practical": {
            "title": "Action Steps: Building an Anti-Bias Culture in School",
            "steps": [
                "Step 1: Confront Stereotypes — When you hear someone making generalizations about a particular tribe or socioeconomic class, politely challenge the assumption.",
                "Step 2: Practice Inclusive Seating — Sit with students from different social backgrounds during meal times, dorm events, and bus rides.",
                "Step 3: Champion Accessibility — Advocate for wheelchair ramps, braille books, and sign language interpreters in school assemblies and religious services."
            ]
        },
        "kenyan_context": "In Kenyan schools, practicing non-discrimination means electing student prefects purely on character, competence, and servant leadership rather than ethnic numbers or family wealth.",
        "reflection": "### Ethical Dilemma: The Prefect's Decision\n\nImagine you are a school prefect assigned to allocate leadership responsibilities for an upcoming national drama festival. Several students from your home county ask you to give them all the key roles, while several talented students from other counties also auditioned.\n\nHow does James 2:1 guide your choice? Living with Christian integrity means refusing nepotism and evaluating every student fairly based on merit and capability.",
        "takeaways": [
            "Discrimination is the unjust treatment of individuals based on ethnicity, wealth, gender, or disability.",
            "James 2:1-9 declares that showing favoritism is a direct sin against God's royal law of love.",
            "Jesus Christ modeled radical inclusion by welcoming outcasts, healing lepers, and breaking cultural prejudices.",
            "Christians must proactively dismantle bias in schools, workplaces, and local communities."
        ],
        "mcq": {
            "question": "In James 2:1-4, what scenario does James use to illustrate the sinful nature of favoritism in the church?",
            "options": [
                "A) Giving the best seat to a rich man in fine clothes while relegating a poor man in shabby clothes to the floor",
                "B) Choosing a Pharisee over a fisherman for church leadership",
                "C) Paying temple taxes with Roman coins instead of Shekels",
                "D) Refusing to eat with Gentile believers in Antioch"
            ],
            "answer": "A",
            "explanation": "In James 2:1-4, James rebukes the fellowship for honoring a rich man wearing fine clothes and gold rings while humiliating a poor man in dirty clothes by making him stand or sit on the floor."
        }
    },

    # -------------------------------------------------------------------------
    # LESSON 5: Combating Gender-Based Violence (GBV)
    # -------------------------------------------------------------------------
    {
        "unit_order": 5,
        "unit_name": "4.2.5 Combating Gender-Based Violence (GBV)",
        "unit_description": "Define Gender-Based Violence (GBV), analyze the biblical condemnation of violence, and master practical safety and reporting pathways including Kenya Helpline 116.",
        "lesson_title": "Combating Gender-Based Violence (GBV)",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/A_woman_carrying_a_child_in_Kenya.jpg/800px-A_woman_carrying_a_child_in_Kenya.jpg",
            "title": "Visual Hook: Protecting Women and Children in Kenya",
            "author": "Wikimedia Commons Contributor",
            "licensing": "Creative Commons Attribution-Share Alike",
            "source": "Wikimedia Commons",
            "caption": "A mother and child in Kenya, highlighting the sacred responsibility of families, schools, and communities to ensure total protection, safety, and freedom from violence."
        },
        "youtube": {
            "youtube_id": "xmFPS0f-kGk",
            "title": "BibleProject: Compassion and God's Heart for the Broken",
            "description": "Explores God's profound compassion for the oppressed, wounded, and vulnerable, demonstrating how divine love stands fiercely against abuse and violence."
        },
        "svg_fn": get_svg_lesson_5,
        "goals": [
            "Define Gender-Based Violence (GBV) and identify its physical, emotional, sexual, and cultural forms.",
            "Analyze biblical passages (Psalm 11:5, Ephesians 5:25-29) condemning violence and abuse of power.",
            "Master the four-step safe reporting pathway for GBV and memorize emergency support resources (Childline Kenya 116, GBV 1195)."
        ],
        "intro": "Gender-Based Violence (GBV) is any harmful act perpetrated against a person's will that is based on socially ascribed gender differences and power imbalances. While GBV disproportionately impacts women and girls, boys and men are also affected.\n\nGBV is a grave violation of human rights and a direct assault on the image of God. The Bible leaves no doubt about God's view of violence: *'The Lord examines the righteous, but the wicked, those who love violence, he hates with a passion'* (Psalm 11:5).",
        "core_scripture": "### Biblical Denunciation of Violence & Oppression\n\n- **Psalm 11:5:** God unequivocally rejects those who love violence.\n- **Ephesians 5:25-29:** Husbands are commanded to love their wives just as Christ loved the Church and gave Himself up for her. Domestic violence is a severe violation of Christ's sacrificial love.\n- **Colossians 3:19:** *'Husbands, love your wives and do not be harsh with them.'*\n- **Proverbs 3:31:** *'Do not envy the violent or choose any of their ways.'*",
        "theological_pillars": "### Recognizing the Manifestations of GBV\n\n1. **Physical Abuse:** Battering, physical assaults, and corporal punishments inflicting bodily harm.\n2. **Sexual Violence & Defilement:** Non-consensual sexual acts, sexual coercion, and harassment.\n3. **Harmful Traditional Practices:** Female Genital Mutilation (FGM), early child forced marriages, and widow cleansing.\n4. **Psychological & Digital Abuse:** Verbal humiliation, coercive control, cyberbullying, and stalking.",
        "deep_dive": "### The 4-Step Safe Reporting Pathway\n\n1. **Step 1: Ensure Safety First** — Move away from the perpetrator and seek immediate shelter in a public or secure place.\n2. **Step 2: Tell a Trusted Adult** — Report the incident immediately to a school counselor, deputy principal, parent, or church leader. Never stay silent out of shame.\n3. **Step 3: Access Medical & Legal Support** — Visit a health clinic within 72 hours for critical Post-Exposure Prophylaxis (PEP) and emergency care. Call the national toll-free helplines: **Childline Kenya (116)** or **GBV Helpline (1195)**.\n4. **Step 4: Long-Term Counseling & Restoration** — Receive trauma counseling and prayer support to achieve psychological and spiritual healing without social stigma.",
        "practical": {
            "title": "Action Checklist for Student Leaders and Peers",
            "steps": [
                "Action 1: Break the Culture of Silence — Never protect an abuser to 'save family reputation'. Silence enables further abuse.",
                "Action 2: Protect Survivor Confidentiality — Treat victims with total privacy, dignity, and compassion. Never gossip about sensitive disclosures.",
                "Action 3: Save Emergency Numbers in Your Notebook — Memorize Childline Kenya: **116** and National Police Service: **999 / 112**."
            ]
        },
        "kenyan_context": "In Kenya, the Sexual Offences Act (2006) and the Protection Against Domestic Violence Act (2015) provide severe legal penalties against perpetrators, complemented by Childline 116 and safe shelters across all counties.",
        "reflection": "### Reflection: Overcoming Victim-Blaming\n\nIn many societies, survivors of GBV are unfairly blamed for what happened to them based on their clothing, location, or time of day.\n\nChristian ethics firmly rejects victim-blaming. Responsibility for violence lies 100% with the perpetrator. Jesus consistently defended vulnerable women against self-righteous accusers (John 8:1-11) and offered dignity, forgiveness, and healing.",
        "takeaways": [
            "GBV is an abuse of power and a direct violation of human dignity and Imago Dei.",
            "God strongly condemns violence and oppression in Psalm 11:5 and throughout Scripture.",
            "Victims must be supported with immediate safety, medical care (within 72 hrs), and confidentiality.",
            "Childline Kenya toll-free hotline is 116; the national GBV helpline is 1195."
        ],
        "mcq": {
            "question": "What is the national toll-free child protection helpline in Kenya used to report child abuse, GBV, and defilement safely and confidentially?",
            "options": [
                "A) 116",
                "B) 911",
                "C) 100",
                "D) 999"
            ],
            "answer": "A",
            "explanation": "Childline Kenya operates the national toll-free helpline number 116, providing 24/7 free, confidential emergency reporting and support for children facing abuse or GBV."
        }
    },

    # -------------------------------------------------------------------------
    # LESSON 6: Protecting the Vulnerable (Orphans, Widows, Strangers)
    # -------------------------------------------------------------------------
    {
        "unit_order": 6,
        "unit_name": "4.2.6 Protecting the Vulnerable (Orphans, Widows, Strangers)",
        "unit_description": "Examine the Old Testament divine welfare system and gleaning laws (Deut 24:19-21) and the New Testament definition of pure religion in James 1:27.",
        "lesson_title": "Protecting the Vulnerable (Orphans, Widows, Strangers)",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Schnorr_von_Carolsfeld_Bibel_in_Bildern_1860_079.png/800px-Schnorr_von_Carolsfeld_Bibel_in_Bildern_1860_079.png",
            "title": "Visual Hook: Ruth Gleaning in the Field of Boaz",
            "author": "Julius Schnorr von Carolsfeld",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Ruth gleaning leftover grain in the fields of Boaz, illustrating the biblical social safety net designed to protect and feed widows, orphans, and foreign immigrants."
        },
        "youtube": {
            "youtube_id": "62CmeO9B7pU",
            "title": "BibleProject: Generosity and God's Economy",
            "description": "Explores how God's abundant generosity calls His people to share resources, care for the poor, and dismantle scarcity mentalities through sacrificial giving."
        },
        "svg_fn": get_svg_lesson_6,
        "goals": [
            "Examine the Israelite covenant welfare laws in Deuteronomy 24:19-21 protecting the triad of vulnerability: widows, orphans, and foreigners.",
            "Analyze the New Testament mandate in James 1:27 regarding 'pure and faultless religion'.",
            "Design contemporary community initiatives to care for orphans, vulnerable children, and elderly widows in Kenya."
        ],
        "intro": "In ancient agrarian societies, there were no social security pensions, insurance policies, or state welfare programs. If a woman lost her husband, a child lost parents, or an immigrant arrived in a foreign land, they faced extreme poverty and starvation.\n\nGod instituted a divine social safety net in Israelite law specifically tailored to protect these three vulnerable groups: the widow, the fatherless child, and the resident foreigner.",
        "core_scripture": "### Deuteronomy 24:19-21 — The Agricultural Safety Net\n\n> *\"When you are harvesting in your field and you overlook a sheaf, do not go back to get it. Leave it for the foreigner, the fatherless and the widow, so that the Lord your God may bless you in all the work of your hands. When you beat the olives from your trees, do not go over the branches a second time. Leave what remains for the foreigner, the fatherless and the widow. When you harvest the grapes in your vineyard, do not go over the vines again. Leave what remains for the foreigner, the fatherless and the widow.\"*",
        "theological_pillars": "### James 1:27 & Pure Religion\n\n> *\"Religion that God our Father accepts as pure and faultless is this: to look after orphans and widows in their distress and to keep oneself from being polluted by the world.\"*\n\nIn God's economy, spiritual devotion is measured not by empty religious rituals, but by concrete, sacrificial care for the most vulnerable members of society.",
        "deep_dive": "### Principles of the Biblical Welfare System\n\n- **Dignity with Labor:** The gleaning law did not simply hand out free food; it allowed vulnerable people to work the fields with dignity, gathering nutritious grain and fruit with their own hands (as Ruth did in Boaz's field).\n- **Remembrance of Past Oppression:** In Deuteronomy 24:22, God reminds Israel: *'Remember that you were slaves in Egypt. That is why I command you to do this.'* Empathy for the marginalized is fueled by remembering God's mercy in our own lives.\n- **The Triennial Poor Tithe:** In Deuteronomy 14:28-29, every third year's tithe was deposited in local storehouses to provide abundant food for the Levite, foreigner, fatherless, and widow.\n- **Early Church Implementation:** In Acts 6:1-6, the Apostles organized a systematic daily food distribution for both Hebrew and Greek-speaking widows, appointing seven spirit-filled deacons to supervise the ministry.",
        "practical": {
            "title": "Modern 'Gleaning' in Kenya: Practical School & Community Projects",
            "steps": [
                "Project 1: The 'Grain of Hope' Food Basket — Organize a monthly food drive where students donate non-perishable food (flour, rice, cooking oil) to distribute to local elderly widows.",
                "Project 2: Children's Home Mentorship — Spend school holiday weekends tutoring orphans in math, sciences, and reading, providing warm emotional support.",
                "Project 3: Welcoming New Students & Migrants — Create a buddy system for refugee students or learners from distant counties to help them adjust smoothly."
            ]
        },
        "kenyan_context": "In Kenyan communities, modern gleaning takes the form of Christian Union charity visits to children's homes, school bursary fundraising for orphaned classmates, and community elder care.",
        "reflection": "### Spiritual Reflection: The Test of Authentic Worship\n\nYou can judge the spiritual vitality of a church or community not by the size of its building or the volume of its choir, but by how it cares for the defenseless.\n\nJames warns that religious rituals, eloquent prayers, and doctrinal knowledge are meaningless in God's sight if we ignore the suffering of orphans and widows in our neighborhoods.",
        "takeaways": [
            "Israelite covenant law created an agricultural safety net (gleaning) for the vulnerable triad: orphans, widows, and foreigners.",
            "Deuteronomy 24:19-21 forbade stripping fields completely, preserving leftover harvest for the poor.",
            "James 1:27 defines pure and undefiled religion as caring for orphans and widows in their distress.",
            "God evaluates a nation's moral health by how faithfully it protects and uplifts the marginalized."
        ],
        "mcq": {
            "question": "Under Deuteronomy 24:19-21, what agricultural practice was mandated to ensure food security for foreigners, orphans, and widows?",
            "options": [
                "A) Burning leftover stalks after the harvest",
                "B) Leaving overlooked sheaves and unharvested field corners for them to glean",
                "C) Selling all grain exclusively at the central temple market",
                "D) Storing all olives in royal granaries for export"
            ],
            "answer": "B",
            "explanation": "Deuteronomy 24:19-21 commanded farmers not to harvest field corners or gather overlooked sheaves, leaving them deliberately for foreigners, orphans, and widows to glean."
        }
    },

    # -------------------------------------------------------------------------
    # LESSON 7: Active Citizenship and Peace Advocacy
    # -------------------------------------------------------------------------
    {
        "unit_order": 7,
        "unit_name": "4.2.7 Active Citizenship and Peace Advocacy",
        "unit_description": "Examine the Beatitude on peacemaking (Matthew 5:9) and equip learners to execute student-led advocacy campaigns promoting anti-bullying, unity, and inclusion.",
        "lesson_title": "Active Citizenship and Peace Advocacy",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/School_children_in_Kenya.jpg/800px-School_children_in_Kenya.jpg",
            "title": "Visual Hook: Kenyan Learners in Collaborative Action",
            "author": "Wikimedia Commons Contributor",
            "licensing": "Creative Commons Attribution-Share Alike",
            "source": "Wikimedia Commons",
            "caption": "Kenyan school children engaging collaboratively, exemplifying the power of youthful leadership, active citizenship, and peacebuilding in school communities."
        },
        "youtube": {
            "youtube_id": "oLYORLZOaZE",
            "title": "BibleProject: Shalom (Peace)",
            "description": "Explores the rich biblical meaning of Shalom—not just the absence of conflict, but active wholeness, restoration, and vibrant flourishing across relationships."
        },
        "svg_fn": get_svg_lesson_7,
        "goals": [
            "Explain the biblical meaning of peacemaking as active reconciliation rather than passive avoidance of conflict (Matthew 5:9).",
            "Design a step-by-step student-led advocacy project addressing bullying, discrimination, or exclusion in a secondary school.",
            "Apply active Christian citizenship principles to promote national cohesion, integrity, and social justice in Kenya."
        ],
        "intro": "Christians are not called to be passive spectators who ignore injustice and conflict. We are called by Jesus Christ to be active agents of reconciliation and transformative peace in our schools, families, and nation.\n\nIn the Sermon on the Mount, Jesus declared: *'Blessed are the peacemakers, for they will be called children of God'* (Matthew 5:9). Peacemaking is not peacekeeping (appeasing bullies); it is the courageous work of building justice and restoring broken relationships.",
        "core_scripture": "### Matthew 5:9 — The Beatitude of the Peacemakers\n\n> *\"Blessed are the peacemakers, for they will be called children of God.\"*\n\n- **Peacemaker vs Peace-lover:** A peace-lover simply prefers a quiet life and often stays silent when others are mistreated. A **peacemaker** actively steps into conflict zones to speak truth, defend the oppressed, and reconcile enemies.\n- **Child of God:** When we make peace, we reflect the family likeness of God, who sent His Son to reconcile a rebellious world to Himself (2 Corinthians 5:18-20).",
        "theological_pillars": "### Proverbs 31:8-9 — Defending the Voiceless\n\n> *\"Speak up for those who have no voice, for the justice of all who are dispossessed. Speak up, judge righteously, and defend the rights of the poor and needy.\"*\n\nBiblical citizenship calls young believers to be courageous advocates for classmates facing unfair disciplinary treatment, exclusion, or teasing.",
        "deep_dive": "### Framework for a Student-Led Peace Advocacy Project\n\n```text\nPROJECT TEMPLATE: THE 'ONE BODY' INCLUSION & ANTI-BULLYING CAMPAIGN\n\n1. PROBLEM IDENTIFIED:\n   - Junior students are facing verbal teasing during meal hours.\n   - Certain students are excluded from group discussions due to socioeconomic background.\n\n2. SCRIPTURAL ANCHOR:\n   - Galatians 3:28 ('All One in Christ') & Luke 6:31 ('The Golden Rule').\n\n3. ACTION PLAN & ACTIVITIES:\n   - Poster Campaign: Create eye-catching posters celebrating ethnic diversity and anti-bullying values.\n   - Open Table Initiative: Designate open lunch tables where any solitary learner can sit and find friends.\n   - Safe Box: Establish a locked suggestion and confidential reporting box in the library monitored by the school chaplain.\n   - Peer Mediation Team: Train Christian Union student leaders in restorative conflict resolution techniques.\n```",
        "practical": {
            "title": "Skills for Peaceful Conflict Resolution",
            "steps": [
                "Skill 1: Active Listening — Allow both parties in a dispute to share their perspective without interruptions or hasty judgements.",
                "Skill 2: De-escalate with Gentle Speech — Proverbs 15:1 (*'A gentle answer turns away wrath, but a harsh word stirs up anger'*). Speak calmly without shouting.",
                "Skill 3: Pursue Restorative Justice — Focus on healing harm and restoring friendship rather than seeking punitive revenge."
            ]
        },
        "kenyan_context": "In Kenyan schools, Peace Clubs and Christian Union leadership teams organize cultural integration days, anti-bullying debates, and peer counseling that foster enduring school harmony.",
        "reflection": "### Reflection: The Golden Rule in Daily Life\n\nIn Luke 6:31, Jesus gave the golden standard of human relationships: *'Do to others as you would have them do to you.'*\n\nIf you were being targeted by hurtful rumors or excluded because of where you were born, you would long for a courageous friend to stand up for you. As followers of Christ, we must be that courageous friend for others.",
        "takeaways": [
            "Peacemaking (Matthew 5:9) is the active pursuit of justice, reconciliation, and shalom.",
            "Proverbs 31:8-9 commands believers to speak up for those who cannot speak for themselves.",
            "Student-led advocacy projects (posters, open lunch tables, mediation) create safe school environments.",
            "Christians model active citizenship by combining moral integrity, compassion, and civic courage."
        ],
        "mcq": {
            "question": "According to Matthew 5:9, what divine title is promised to those who actively make peace?",
            "options": [
                "A) Kings of the Earth",
                "B) Children of God",
                "C) Rulers of Nations",
                "D) Judges of Israel"
            ],
            "answer": "B",
            "explanation": "In Matthew 5:9, Jesus proclaims: 'Blessed are the peacemakers, for they will be called children of God', because active peacemaking mirrors God's own character of reconciliation."
        }
    },

    # -------------------------------------------------------------------------
    # LESSON 8: Assessment, Synthesis and Ethical Reflection
    # -------------------------------------------------------------------------
    {
        "unit_order": 8,
        "unit_name": "4.2.8 Assessment, Synthesis and Ethical Reflection",
        "unit_description": "Synthesize key concepts of human rights and non-discrimination through matching exercises, rubric evaluations, and comprehensive ethical case analysis.",
        "lesson_title": "Assessment, Synthesis and Ethical Reflection",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Moses_with_the_Ten_Commandments_by_Philippe_de_Champaigne.jpg/800px-Moses_with_the_Ten_Commandments_by_Philippe_de_Champaigne.jpg",
            "title": "Visual Hook: Moral Foundations of Divine Law",
            "author": "Philippe de Champaigne",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Moses with the Ten Commandments, depicting the enduring divine covenant that anchors human dignity, moral law, justice, and protection of the vulnerable across history."
        },
        "youtube": {
            "youtube_id": "3BGO9Mmd_cU",
            "title": "BibleProject: The Law (Torah)",
            "description": "Explores the purpose of biblical law in shaping a just, compassionate society that reflects God's holiness and treats every neighbor with equity."
        },
        "svg_fn": get_svg_lesson_8,
        "goals": [
            "Synthesize the biblical foundations of human dignity, non-discrimination, protection of the vulnerable, and peacemaking.",
            "Evaluate complex real-world ethical dilemmas using scriptural moral frameworks.",
            "Demonstrate mastery of Topic 4.2 core competencies through summative assessment tasks."
        ],
        "intro": "Throughout Sub-Strand 4.2, we have discovered that human rights are not merely modern legal codes; they are rooted in God's eternal character, His creation of humanity in the *Imago Dei*, and the reconciling work of Jesus Christ.\n\nIn this final lesson, we synthesize our learning through a Scripture matching matrix, rubric analysis, and practical ethical case scenarios to prepare us for lifelong Christian advocacy.",
        "core_scripture": "### Comprehensive Scripture Matching & Mastery Matrix\n\n| Scriptural Passage | Core Moral Mandate | Real-World Application |\n| :--- | :--- | :--- |\n| **Genesis 1:26-27** | Imago Dei & Inherent Worth | Protect every human life regardless of social or economic status. |\n| **Galatians 3:28** | Oneness in Christ | Dismantle tribalism, class barriers, and gender inequality in church and school. |\n| **James 2:1-4** | Condemnation of Favoritism | Treat the poor with equal honor; refuse partiality toward the wealthy. |\n| **Psalm 11:5** | Rejection of Violence | Stand against Gender-Based Violence; utilize safe reporting (Childline 116). |\n| **Deut 24:19-21** | The Gleaning Safety Net | Care for the vulnerable triad: orphans, widows, and foreign refugees. |\n| **Matthew 5:9** | Peacemaking | Lead proactive reconciliation and anti-bullying initiatives on campus. |",
        "theological_pillars": "### The Four Pillars of Christian Social Ethics\n\n1. **Creation:** Human dignity is universal and irrevocable because all people are made in the image of God (*Imago Dei*).\n2. **The Fall:** Sin manifests as discrimination, violence, exploitation, and dehumanizing prejudices.\n3. **Redemption:** The Cross breaks down dividing walls of hostility, creating an inclusive, loving community in Christ Jesus.\n4. **Restoration:** Christians are called to be agents of God's shalom, practicing justice, mercy, and compassion.",
        "deep_dive": "### Peer Advocacy Presentation Rubric\n\nUse this rubric to evaluate student advocacy posters and presentations:\n\n1. **Biblical Grounding (30%):** Accurately explains and cites relevant biblical passages (e.g., Genesis 1:27, Galatians 3:28, James 1:27).\n2. **Creativity & Design (30%):** Clear, visually engaging layout with legible typography and compelling call-to-action.\n3. **Practical Impact (40%):** Proposes realistic, actionable, and safe steps to address discrimination, bullying, or vulnerability in school.",
        "practical": {
            "title": "Summative Case Scenario: The Inclusive Prefect",
            "steps": [
                "Scenario: A new refugee student joins your class. Some students make fun of their accent and refuse to include them in group work.",
                "Ethical Step 1: Diagnose — Recognize that mocking a foreigner violates Deuteronomy 24:19 and Hebrews 13:2.",
                "Ethical Step 2: Affirm Dignity — Speak to the student with warmth, welcoming them into your study group as a valued image-bearer of God.",
                "Ethical Step 3: Cultural Change — Sensitize classmates to practice hospitality and the Golden Rule (Luke 6:31)."
            ]
        },
        "kenyan_context": "Kenyan youth who embrace these ethical principles become exemplary leaders in universities, public service, and civil society, championing Chapter 4 values and building a unified, peaceful nation.",
        "reflection": "### Personal Reflection & Commitment\n\nHuman rights become a reality only when individual people choose to live with righteousness, empathy, and courage.\n\nTake a moment to write a personal commitment: *How will you use your words, your influence, and your faith to defend the dignity of others this term?*",
        "takeaways": [
            "Human rights find their deepest foundation in God's creation (Imago Dei) and redemption in Christ.",
            "Christian discipleship demands active opposition to tribalism, favoritism, GBV, and social neglect.",
            "Pure religion (James 1:27) combines moral purity with sacrificial care for the most vulnerable.",
            "Every Christian student is called to be a proactive peacemaker and ambassador of Christ's kingdom."
        ],
        "mcq": {
            "question": "Which biblical passage specifically defines 'pure and faultless religion' as caring for orphans and widows in their distress?",
            "options": [
                "A) James 1:27",
                "B) Proverbs 17:15",
                "C) Genesis 9:6",
                "D) Deuteronomy 16:19"
            ],
            "answer": "A",
            "explanation": "James 1:27 explicitly defines pure and faultless religion accepted by God as looking after orphans and widows in their distress and keeping oneself unpolluted by the world."
        }
    }
]


# ─── DATABASE INGESTION ENGINE ────────────────────────────────────────────────

def ingest_topic_4_2():
    print("=" * 80)
    print("STARTING VLEARN GRADE 10 CRE TOPIC 4.2 DATABASE INGESTION ENGINE")
    print("=" * 80)

    with transaction.atomic():
        # 1. Fetch Hierarchy
        curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        if not curriculum:
            raise ValueError("Curriculum 'CBC' (ID 5) not found!")

        grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
        if not grade:
            raise ValueError("Grade 10 not found under CBC!")

        subject = Subject.objects.filter(grade=grade, name__icontains="CRE").first()
        if not subject:
            raise ValueError("Subject 'CRE' (ID 46) not found under Grade 10!")

        print(f"[✓] Target Hierarchy Verified: {curriculum.name} -> {grade.name} -> {subject.name} (ID: {subject.id})")

        # 2. Get or Create Topic 4.2
        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=20,
            defaults={
                "name": "Sub-Strand 4.2: Human Rights (Non-discrimination)",
                "description": "Explores the biblical foundation of human dignity (Imago Dei), equality in Christ (Galatians 3:28), forms of discrimination, combating Gender-Based Violence (GBV), protecting the vulnerable, and active student-led peace advocacy."
            }
        )
        if not created:
            topic.name = "Sub-Strand 4.2: Human Rights (Non-discrimination)"
            topic.description = "Explores the biblical foundation of human dignity (Imago Dei), equality in Christ (Galatians 3:28), forms of discrimination, combating Gender-Based Violence (GBV), protecting the vulnerable, and active student-led peace advocacy."
            topic.save()
            print(f"[✓] Updated existing Topic: Order {topic.order} — '{topic.name}' (ID: {topic.id})")
        else:
            print(f"[✓] Created Topic: Order {topic.order} — '{topic.name}' (ID: {topic.id})")

        # Clean existing units/lessons under topic 20 to ensure clean idempotency
        existing_units = LearningUnit.objects.filter(topic=topic)
        for unit in existing_units:
            for lsn in unit.lessons.all():
                lsn.blocks.all().delete()
                lsn.assets.all().delete()
                lsn.delete()
            unit.delete()
        print("[✓] Cleared previous units and lessons under Topic 4.2 for clean idempotent rebuild.")

        total_units = 0
        total_lessons = 0
        total_pages = 0
        total_blocks = 0
        total_assets = 0

        # 3. Ingest 8 Lessons
        for cfg in LESSONS_CONFIG:
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
                    "grade": "Grade 10",
                    "subject": "CRE",
                    "topic_order": 20,
                    "topic_name": topic.name,
                    "unit_order": u_order,
                    "author": "VLearn CRE Ingestion Agent",
                    "curriculum_framework": "CBC Kenya",
                    "enrichment_version": "v3_pedagogical"
                }
            )
            total_lessons += 1

            # Prepare Assets
            # Asset 1: Photographic Visual Hook
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
                url="https://vlearn.africa/assets/diagrams/cre/topic_4_2_lesson_" + str(u_order) + ".svg",
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
            # CARD 1 (Page 1): Visual Hook + Objectives + Introduction (3 blocks)
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
                title="Sharing Experiences & Real-Life Hook",
                content={"markdown": clean_text(cfg["intro"])}
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 2 (Page 2): Core Scripture & Theological Pillars (2 blocks)
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
                order=40, component_order=1,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Core Biblical Foundation",
                content={"markdown": clean_text(cfg["core_scripture"])}
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=2, page_title="Scriptural Exegesis",
                order=45, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Theological Foundations & Principles",
                content={"markdown": clean_text(cfg["theological_pillars"])}
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 3 (Page 3): Custom Pedagogical Vector SVG & Deep Dive (2 blocks)
            # ───────────────────────────────────────────────────────────────────
            b5 = LessonBlock.objects.create(
                lesson=lesson, page_number=3, page_title="Pedagogical Diagram",
                order=50, component_order=1,
                block_type="suggested_diagram", component_type="suggested_diagram",
                title=f"Visual Architecture: {l_title}",
                content={
                    "title": f"Pedagogical Blueprint: {l_title}",
                    "caption": f"Comprehensive architectural diagram illustrating {l_title}.",
                    "svg": svg_content,
                    "svg_xml": svg_content
                }
            )
            b5.assets.add(svg_asset)

            LessonBlock.objects.create(
                lesson=lesson, page_number=3, page_title="Pedagogical Diagram",
                order=60, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Theological Deep Dive & Analysis",
                content={"markdown": clean_text(cfg["deep_dive"])}
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 4 (Page 4): Practical Framework & Kenyan Context (2 blocks)
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=4, page_title="Practical Application",
                order=70, component_order=1,
                block_type="step_process", component_type="step_process",
                title=clean_text(cfg["practical"]["title"]),
                content=clean_dict(cfg["practical"])
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=4, page_title="Practical Application",
                order=75, component_order=2,
                block_type="concept_explanation", component_type="concept_explanation",
                title="Kenyan Real-World Context & Integration",
                content={"markdown": clean_text(cfg["kenyan_context"])}
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 5 (Page 5): Educational Video & Spiritual Reflection (2 blocks)
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
                title="Spiritual Reflection & Ethical Values",
                content={"markdown": clean_text(cfg["reflection"])}
            )

            # ───────────────────────────────────────────────────────────────────
            # CARD 6 (Page 6): Key Takeaways & Formative Knowledge Check (2 blocks)
            # ───────────────────────────────────────────────────────────────────
            LessonBlock.objects.create(
                lesson=lesson, page_number=6, page_title="Review & Knowledge Check",
                order=100, component_order=1,
                block_type="key_takeaway", component_type="key_takeaway",
                title="Summary & Core Principles",
                content={
                    "title": f"Key Takeaways: {l_title}",
                    "takeaways": clean_dict(cfg["takeaways"])
                }
            )

            LessonBlock.objects.create(
                lesson=lesson, page_number=6, page_title="Review & Knowledge Check",
                order=110, component_order=2,
                block_type="knowledge_check", component_type="knowledge_check",
                title="Formative Knowledge Check",
                content=clean_dict(cfg["mcq"])
            )

            total_pages += 6
            total_blocks += 13
            print(f"  [+] Ingested Lesson {u_order:02d}/8: '{l_title}' (6 cards/pages, 13 blocks, 3 LessonAssets)")

        print("=" * 80)
        print("INGESTION SUMMARY FOR TOPIC 4.2:")
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
    ingest_topic_4_2()
