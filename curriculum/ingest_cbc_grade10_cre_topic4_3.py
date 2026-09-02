"""
VLearn CBC Grade 10 CRE — Sub-Strand 4.3: Human Sexuality
Production-Ready Ingestion & Visual Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (Level: 10, ID: 5)
Subject: CRE (ID: 46)
Topic: Sub-Strand 4.3: Human Sexuality (Order: 21)

8 Discrete Units / Published Lessons:
  1. Understanding Human Sexuality (Biological, Psychological, Emotional, Social Dimensions)
  2. God's Design for Male-Female Relationships (Genesis 2 & 1 Timothy 5)
  3. Dating vs. Courtship: Purpose, Accountability and Boundaries
  4. Understanding Peer Pressure in Human Sexuality (Direct vs Indirect Influence)
  5. Assertive Strategies to Resist Negative Peer Pressure (The Joseph Strategy)
  6. Peer Support and Moral Accountability Networks (Hebrews 10:24-25)
  7. Setting Boundaries for Bodily Holiness (1 Corinthians 6:18-20)
  8. Youth Support Networks & Help-Seeking Ecosystem (Childline 116, GBV 1195)
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

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">HOLISTIC ARCHITECTURE OF HUMAN SEXUALITY</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Genesis 1:27, 31 — God's Multi-Dimensional Gift (Created "Very Good")</text>

  <!-- Central Hub -->
  <rect x="290" y="90" width="220" height="70" rx="12" fill="url(#goldGrad1)" stroke="#fbbf24" stroke-width="2"/>
  <text x="400" y="122" fill="#0f172a" font-family="system-ui, sans-serif" font-size="15" font-weight="800" text-anchor="middle">HOLISTIC SEXUALITY</text>
  <text x="400" y="142" fill="#1e293b" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Whole Person as Male / Female</text>

  <!-- Connecting Lines -->
  <line x1="320" y1="160" x2="110" y2="200" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4 3"/>
  <line x1="370" y1="160" x2="295" y2="200" stroke="#34d399" stroke-width="1.5" stroke-dasharray="4 3"/>
  <line x1="430" y1="160" x2="505" y2="200" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="4 3"/>
  <line x1="480" y1="160" x2="690" y2="200" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="4 3"/>

  <!-- 4 Dimension Cards -->
  <!-- 1. Biological -->
  <g transform="translate(25, 200)">
    <rect width="170" height="200" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="170" height="32" rx="10" fill="#0284c7"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. BIOLOGICAL</text>
    <text x="12" y="55" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Physical &amp; Bodily</text>
    <text x="12" y="73" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Chromosomes, organs,</text>
    <text x="12" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">hormones &amp; puberty.</text>
    <text x="12" y="112" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Reproductive</text>
    <text x="12" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Capacity for procreation</text>
    <text x="12" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">within marriage covenant.</text>
    <text x="12" y="172" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" font-style="italic">Gen 1:27; Ps 139:14</text>
  </g>

  <!-- 2. Psychological -->
  <g transform="translate(210, 200)">
    <rect width="170" height="200" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="170" height="32" rx="10" fill="#059669"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. PSYCHOLOGICAL</text>
    <text x="12" y="55" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Identity &amp; Self-Image</text>
    <text x="12" y="73" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Cognitive development,</text>
    <text x="12" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">perceptions &amp; values.</text>
    <text x="12" y="112" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Self-Acceptance</text>
    <text x="12" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Embracing God's unique</text>
    <text x="12" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">design without anxiety.</text>
    <text x="12" y="172" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" font-style="italic">Romans 12:2; Ps 139</text>
  </g>

  <!-- 3. Emotional -->
  <g transform="translate(395, 200)">
    <rect width="170" height="200" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="170" height="32" rx="10" fill="#e11d48"/>
    <text x="85" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. EMOTIONAL</text>
    <text x="12" y="55" fill="#f43f5e" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Affection &amp; Feelings</text>
    <text x="12" y="73" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Navigating infatuation,</text>
    <text x="12" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">attraction &amp; empathy.</text>
    <text x="12" y="112" fill="#f43f5e" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Guarding the Heart</text>
    <text x="12" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Emotional maturity and</text>
    <text x="12" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">patience before marriage.</text>
    <text x="12" y="172" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" font-style="italic">Proverbs 4:23; Song 8:4</text>
  </g>

  <!-- 4. Social -->
  <g transform="translate(580, 200)">
    <rect width="195" height="200" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="195" height="32" rx="10" fill="#9333ea"/>
    <text x="97" y="21" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">4. SOCIAL / RELATIONAL</text>
    <text x="12" y="55" fill="#c084fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Healthy Friendships</text>
    <text x="12" y="73" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Communication, mutual</text>
    <text x="12" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">respect &amp; boundaries.</text>
    <text x="12" y="112" fill="#c084fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Community Purity</text>
    <text x="12" y="130" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Peer accountability and</text>
    <text x="12" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">wholesome fellowship.</text>
    <text x="12" y="172" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" font-style="italic">Heb 10:24; 1 Tim 5:1-2</text>
  </g>

  <text x="400" y="425" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">VLEARN CBC SENIOR SECONDARY CRE CURRICULUM — TOPIC 4.3</text>
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

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">GOD'S DESIGN FOR MALE-FEMALE RELATIONSHIPS</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Equality, Complementarity, and Sibling Purity (Genesis 2:18-24 &amp; 1 Timothy 5:1-2)</text>

  <!-- Two Core Complementary Blocks -->
  <g transform="translate(50, 95)">
    <rect width="325" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="162" y="30" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">CO-EQUALITY &amp; COMPLEMENTARITY</text>
    <text x="15" y="60" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">• Created as "Ezer Kenegdo" (Suitable Helper)</text>
    <text x="15" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Equal in spiritual dignity and moral worth</text>
    <text x="15" y="100" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Distinct and complementary in divine purpose</text>
  </g>

  <g transform="translate(425, 95)">
    <rect width="325" height="120" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <text x="162" y="30" fill="#34d399" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">COVENANT INTENTIONALITY</text>
    <text x="15" y="60" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">• Leaving and Cleaving (Genesis 2:24)</text>
    <text x="15" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Lifelong, exclusive commitment in marriage</text>
    <text x="15" y="100" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Free of shame, founded on total trust</text>
  </g>

  <!-- 4 Pillars for Youth Relationships -->
  <text x="400" y="245" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">FOUR PILLARS OF YOUTH INTERACTION</text>

  <g transform="translate(40, 260)">
    <rect width="165" height="135" rx="8" fill="#1e293b" stroke="#60a5fa" stroke-width="1.5"/>
    <text x="82" y="25" fill="#60a5fa" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">1. MUTUAL RESPECT</text>
    <text x="10" y="52" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">View peers as image-</text>
    <text x="10" y="68" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">bearers of God, never</text>
    <text x="10" y="84" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">as objects of lust.</text>
    <text x="10" y="112" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">Gen 1:27</text>
  </g>

  <g transform="translate(225, 260)">
    <rect width="165" height="135" rx="8" fill="#1e293b" stroke="#4ade80" stroke-width="1.5"/>
    <text x="82" y="25" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">2. PURE MOTIVES</text>
    <text x="10" y="52" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">Treat young women as</text>
    <text x="10" y="68" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">sisters and young men</text>
    <text x="10" y="84" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">as brothers in Christ.</text>
    <text x="10" y="112" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">1 Tim 5:1-2</text>
  </g>

  <g transform="translate(410, 260)">
    <rect width="165" height="135" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="82" y="25" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">3. CLEAR BOUNDARIES</text>
    <text x="10" y="52" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">Guard romantic feelings</text>
    <text x="10" y="68" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">until readiness for</text>
    <text x="10" y="84" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">marriage maturity.</text>
    <text x="10" y="112" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">Song 8:4</text>
  </g>

  <g transform="translate(595, 260)">
    <rect width="165" height="135" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <text x="82" y="25" fill="#c084fc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">4. SPIRITUAL EDIFICATION</text>
    <text x="10" y="52" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">Spur one another toward</text>
    <text x="10" y="68" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">prayer, academic focus,</text>
    <text x="10" y="84" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">and moral excellence.</text>
    <text x="10" y="112" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">Heb 10:24</text>
  </g>

  <text x="400" y="425" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">VLEARN CBC SENIOR SECONDARY CRE CURRICULUM — TOPIC 4.3</text>
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

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">DATING VS. COURTSHIP: A PARADIGM COMPARISON</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Evaluating Secular Relationship Norms Through Biblical Wisdom</text>

  <!-- Left Column: Secular Dating -->
  <g transform="translate(45, 90)">
    <rect width="335" height="305" rx="10" fill="#1e293b" stroke="#f87171" stroke-width="2"/>
    <rect width="335" height="36" rx="10" fill="#dc2626"/>
    <text x="167" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">SECULAR DATING</text>

    <!-- Point 1 -->
    <circle cx="28" cy="65" r="12" fill="#ef4444"/>
    <text x="28" y="70" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1</text>
    <text x="50" y="62" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Recreational &amp; Casual</text>
    <text x="50" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Often pursued for fun, status, or peer popularity.</text>

    <!-- Point 2 -->
    <circle cx="28" cy="115" r="12" fill="#ef4444"/>
    <text x="28" y="120" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2</text>
    <text x="50" y="112" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Self-Centered Focus</text>
    <text x="50" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">"What do I get out of this emotionally or physically?"</text>

    <!-- Point 3 -->
    <circle cx="28" cy="165" r="12" fill="#ef4444"/>
    <text x="28" y="170" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3</text>
    <text x="50" y="162" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Isolation from Community</text>
    <text x="50" y="178" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Conducted privately with little or no parental oversight.</text>

    <!-- Point 4 -->
    <circle cx="28" cy="215" r="12" fill="#ef4444"/>
    <text x="28" y="220" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">4</text>
    <text x="50" y="212" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Blurred Physical Boundaries</text>
    <text x="50" y="228" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Physical intimacy frequently precedes lifelong commitment.</text>

    <!-- Point 5 Outcome -->
    <rect x="20" y="250" width="295" height="40" rx="6" fill="#450a0a" stroke="#b91c1c" stroke-width="1"/>
    <text x="167" y="274" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">High Risk of Heartbreak, Guilt &amp; Compromise</text>
  </g>

  <!-- Right Column: Biblical Courtship -->
  <g transform="translate(420, 90)">
    <rect width="335" height="305" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <rect width="335" height="36" rx="10" fill="#059669"/>
    <text x="167" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">BIBLICAL COURTSHIP</text>

    <!-- Point 1 -->
    <circle cx="28" cy="65" r="12" fill="#10b981"/>
    <text x="28" y="70" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1</text>
    <text x="50" y="62" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Purposeful &amp; Intentional</text>
    <text x="50" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Evaluating readiness for a lifelong covenant marriage.</text>

    <!-- Point 2 -->
    <circle cx="28" cy="115" r="12" fill="#10b981"/>
    <text x="28" y="120" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2</text>
    <text x="50" y="112" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Others-Centered Honor</text>
    <text x="50" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Focuses on serving, protecting, and edifying the other.</text>

    <!-- Point 3 -->
    <circle cx="28" cy="165" r="12" fill="#10b981"/>
    <text x="28" y="170" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3</text>
    <text x="50" y="162" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Accountability &amp; Mentorship</text>
    <text x="50" y="178" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Involves parents, mentors, and the church community.</text>

    <!-- Point 4 -->
    <circle cx="28" cy="215" r="12" fill="#10b981"/>
    <text x="28" y="220" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">4</text>
    <text x="50" y="212" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Uncompromising Holiness</text>
    <text x="50" y="228" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Guards physical intimacy exclusively for holy matrimony.</text>

    <!-- Point 5 Outcome -->
    <rect x="20" y="250" width="295" height="40" rx="6" fill="#064e3b" stroke="#047857" stroke-width="1"/>
    <text x="167" y="274" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Fosters Deep Emotional Trust, Clarity &amp; Godly Peace</text>
  </g>

  <text x="400" y="425" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">VLEARN CBC SENIOR SECONDARY CRE CURRICULUM — TOPIC 4.3</text>
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

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">ANATOMY OF PEER PRESSURE IN HUMAN SEXUALITY</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Direct Challenges vs. Indirect Social Conditioning &amp; Vulnerability Channels</text>

  <!-- Central Student Node -->
  <circle cx="400" cy="220" r="48" fill="#1e293b" stroke="#fbbf24" stroke-width="2.5"/>
  <text x="400" y="215" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">TEENAGER</text>
  <text x="400" y="233" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Identity &amp; Will</text>

  <!-- Left: Direct Pressure -->
  <g transform="translate(50, 110)">
    <rect width="260" height="220" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <rect width="260" height="34" rx="10" fill="#be123c"/>
    <text x="130" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">DIRECT / EXPLICIT PRESSURE</text>
    <text x="15" y="58" fill="#fda4af" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Verbal Demands &amp; Dares</text>
    <text x="15" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Direct demands to engage in sexual acts</text>
    <text x="15" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">or share explicit images/texts.</text>
    <text x="15" y="112" fill="#fda4af" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Mockery &amp; Teasing</text>
    <text x="15" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Labeling purity as "backward" or</text>
    <text x="15" y="142" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">"naive" to coerce conformity.</text>
    <text x="15" y="166" fill="#fda4af" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Coercive Ultimatums</text>
    <text x="15" y="182" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">"If you love me, you will prove it."</text>
  </g>

  <!-- Right: Indirect Pressure -->
  <g transform="translate(490, 110)">
    <rect width="260" height="220" rx="10" fill="#1e293b" stroke="#818cf8" stroke-width="2"/>
    <rect width="260" height="34" rx="10" fill="#4338ca"/>
    <text x="130" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">INDIRECT / IMPLICIT PRESSURE</text>
    <text x="15" y="58" fill="#c7d2fe" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• "Everyone Is Doing It" Myth</text>
    <text x="15" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">False consensus spread by gossip,</text>
    <text x="15" y="88" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">movies, music, and social circles.</text>
    <text x="15" y="112" fill="#c7d2fe" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Digital Media Glorification</text>
    <text x="15" y="128" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Trends portraying casual sex as the</text>
    <text x="15" y="142" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">normal hallmark of adulthood.</text>
    <text x="15" y="166" fill="#c7d2fe" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Fear of Social Ostracization</text>
    <text x="15" y="182" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Silent dread of being excluded.</text>
  </g>

  <!-- Arrows toward central node -->
  <line x1="310" y1="220" x2="348" y2="220" stroke="#f43f5e" stroke-width="3" marker-end="url(#arrow)"/>
  <line x1="490" y1="220" x2="452" y2="220" stroke="#818cf8" stroke-width="3" marker-end="url(#arrow)"/>

  <!-- Footer Insight -->
  <rect x="150" y="355" width="500" height="42" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
  <text x="400" y="380" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Biblical Shield: Proverbs 1:10 — "My son, if sinners entice you, do not give in to them."</text>

  <text x="400" y="425" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">VLEARN CBC SENIOR SECONDARY CRE CURRICULUM — TOPIC 4.3</text>
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

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE ASSERTIVE COMMUNICATION COMPASS &amp; JOSEPH STRATEGY</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Standing Firm in Integrity: Verbal Mastery and Decisive Physical Exit</text>

  <!-- 3 Communication Styles Comparison -->
  <g transform="translate(45, 90)">
    <rect width="220" height="130" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
    <rect width="220" height="28" rx="8" fill="#334155"/>
    <text x="110" y="19" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">PASSIVE RESPONSE (FAIL)</text>
    <text x="12" y="50" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Silence or nervous laughing</text>
    <text x="12" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Interpreted as consent/delay</text>
    <text x="12" y="90" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5">• Result: Boundaries broken</text>
  </g>

  <g transform="translate(290, 90)">
    <rect width="220" height="130" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="220" height="28" rx="8" fill="#be123c"/>
    <text x="110" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">AGGRESSIVE RESPONSE (RISKY)</text>
    <text x="12" y="50" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Shouting, threats, insults</text>
    <text x="12" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Escalates hostility &amp; violence</text>
    <text x="12" y="90" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5">• Result: Conflict, no respect</text>
  </g>

  <g transform="translate(535, 90)">
    <rect width="220" height="130" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <rect width="220" height="28" rx="8" fill="#059669"/>
    <text x="110" y="19" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">ASSERTIVE RESPONSE (WIN)</text>
    <text x="12" y="50" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Direct, calm, unwavering "No"</text>
    <text x="12" y="70" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Eye contact &amp; "I" statements</text>
    <text x="12" y="90" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5">• Result: Integrity protected</text>
  </g>

  <!-- Bottom: 3 Core Assertive Playbook Tactics -->
  <text x="400" y="250" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">THE CHRISTIAN YOUTH DEFENSE PLAYBOOK</text>

  <g transform="translate(45, 265)">
    <rect width="220" height="130" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="110" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">TACTIC 1: CLEAR "I" VOICE</text>
    <text x="10" y="48" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">"I have chosen biblical</text>
    <text x="10" y="64" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">purity for my life. I don't</text>
    <text x="10" y="80" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">compromise on my standards."</text>
    <text x="10" y="108" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">Clear, firm, respectful.</text>
  </g>

  <g transform="translate(290, 265)">
    <rect width="220" height="130" rx="8" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="110" y="24" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">TACTIC 2: REVERSE PRESSURE</text>
    <text x="10" y="48" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">"Why does my personal</text>
    <text x="10" y="64" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">purity bother you? Let's</text>
    <text x="10" y="80" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">focus on something useful."</text>
    <text x="10" y="108" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">Deflects peer coercion.</text>
  </g>

  <g transform="translate(535, 265)">
    <rect width="220" height="130" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
    <text x="110" y="24" fill="#34d399" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">TACTIC 3: JOSEPH'S EXIT</text>
    <text x="10" y="48" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">When verbal boundaries</text>
    <text x="10" y="64" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">fail, run immediately from</text>
    <text x="10" y="80" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="10">the scene (Genesis 39:12).</text>
    <text x="10" y="108" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9">Purity over reputation.</text>
  </g>

  <text x="400" y="425" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">VLEARN CBC SENIOR SECONDARY CRE CURRICULUM — TOPIC 4.3</text>
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

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE CHRISTIAN PEER ACCOUNTABILITY SHIELD</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Hebrews 10:24-25 — Spurring One Another Toward Holiness, Love and Good Deeds</text>

  <!-- 3 Pillars of Accountability -->
  <g transform="translate(45, 100)">
    <rect width="220" height="280" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#0284c7"/>
    <text x="110" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">1. INTENTIONAL CIRCLE</text>
    <text x="15" y="60" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Character-First Selection</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Select friends who revere God</text>
    <text x="15" y="94" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">and respect personal purity.</text>
    <text x="15" y="125" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Honest Transparency</text>
    <text x="15" y="143" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Permission to speak truth</text>
    <text x="15" y="159" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">lovingly into blind spots.</text>
    <text x="15" y="190" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Scriptural Anchor</text>
    <text x="15" y="208" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">"As iron sharpens iron, so</text>
    <text x="15" y="224" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">one person sharpens another."</text>
    <text x="15" y="255" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" font-style="italic">Proverbs 27:17</text>
  </g>

  <g transform="translate(290, 100)">
    <rect width="220" height="280" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#059669"/>
    <text x="110" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">2. WEEKLY CHECK-INS</text>
    <text x="15" y="60" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Digital Integrity Audits</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Checking phone habits, social</text>
    <text x="15" y="94" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">feeds, and chat groups.</text>
    <text x="15" y="125" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Relationship Accountability</text>
    <text x="15" y="143" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Guarding against secret</text>
    <text x="15" y="159" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">or ungodly attachments.</text>
    <text x="15" y="190" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Prayer Partnership</text>
    <text x="15" y="208" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Interceding for each other</text>
    <text x="15" y="224" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">during moments of temptation.</text>
    <text x="15" y="255" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" font-style="italic">James 5:16</text>
  </g>

  <g transform="translate(535, 100)">
    <rect width="220" height="280" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="220" height="34" rx="10" fill="#d97706"/>
    <text x="110" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">3. SAFE SOCIAL ZONES</text>
    <text x="15" y="60" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Open Environment Rule</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Study in libraries, dining halls,</text>
    <text x="15" y="94" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">or supervised public spaces.</text>
    <text x="15" y="125" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Zero Isolated Seclusion</text>
    <text x="15" y="143" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Refusing closed-door private</text>
    <text x="15" y="159" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">meetings with opposite sex.</text>
    <text x="15" y="190" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Group Fellowship</text>
    <text x="15" y="208" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">Participating in CU, sports,</text>
    <text x="15" y="224" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">and community outreach.</text>
    <text x="15" y="255" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" font-style="italic">Ecclesiastes 4:9-12</text>
  </g>

  <text x="400" y="425" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">VLEARN CBC SENIOR SECONDARY CRE CURRICULUM — TOPIC 4.3</text>
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

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE FOUR BOUNDARY ZONES OF BODILY HOLINESS</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">1 Corinthians 6:19-20 — "Your Body is the Holy Temple of the Holy Spirit"</text>

  <!-- 4 Boundary Quadrants -->
  <!-- 1. Mental Zone -->
  <g transform="translate(45, 95)">
    <rect width="340" height="135" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. MENTAL &amp; THOUGHT BOUNDARY</text>
    <text x="15" y="55" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Captivating every thought to obey Christ (2 Cor 10:5)</text>
    <text x="15" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Refusing lingering lustful fantasies and daydreaming</text>
    <text x="15" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Meditating on whatever is noble, pure, and lovely (Phil 4:8)</text>
    <text x="15" y="120" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" font-style="italic">Proverbs 4:23 — Above all else, guard your heart.</text>
  </g>

  <!-- 2. Visual / Media Zone -->
  <g transform="translate(415, 95)">
    <rect width="340" height="135" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <text x="170" y="28" fill="#f43f5e" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. VISUAL &amp; MEDIA BOUNDARY</text>
    <text x="15" y="55" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Covenant with your eyes against pornography (Job 31:1)</text>
    <text x="15" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Unfollowing sexually suggestive social media accounts</text>
    <text x="15" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Filtering entertainment, movies, and provocative music</text>
    <text x="15" y="120" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" font-style="italic">Psalm 101:3 — I will not look with approval on anything vile.</text>
  </g>

  <!-- 3. Physical / Touch Zone -->
  <g transform="translate(45, 250)">
    <rect width="340" height="135" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <text x="170" y="28" fill="#34d399" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">3. PHYSICAL &amp; TOUCH BOUNDARY</text>
    <text x="15" y="55" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Deciding in advance: No intimate touching before marriage</text>
    <text x="15" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Appropriate fraternal greetings (handshakes, sibling hugs)</text>
    <text x="15" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Avoiding seclusion in dark, private, or enclosed spaces</text>
    <text x="15" y="120" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" font-style="italic">1 Cor 6:18 — Flee from sexual immorality.</text>
  </g>

  <!-- 4. Digital / Communication Zone -->
  <g transform="translate(415, 250)">
    <rect width="340" height="135" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
    <text x="170" y="28" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">4. DIGITAL &amp; CHAT BOUNDARY</text>
    <text x="15" y="55" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Strict zero tolerance for sexting or sending illicit photos</text>
    <text x="15" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• No secret late-night intimate chatting or flirtatious texts</text>
    <text x="15" y="95" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10.5">• Maintaining transparency with parents and mentors</text>
    <text x="15" y="120" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" font-style="italic">Ephesians 5:3 — Not even a hint of sexual immorality.</text>
  </g>

  <text x="400" y="425" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">VLEARN CBC SENIOR SECONDARY CRE CURRICULUM — TOPIC 4.3</text>
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

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">YOUTH SUPPORT &amp; HELP-SEEKING ECOSYSTEM IN KENYA</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Breaking Silence: Safe Channels for Guidance, Protection, and Crisis Intervention</text>

  <!-- 4 Step Support Ecosystem Columns -->
  <!-- Level 1: School G&C -->
  <g transform="translate(30, 95)">
    <rect width="170" height="290" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="170" height="34" rx="10" fill="#0284c7"/>
    <text x="85" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">1. SCHOOL COUNSELOR</text>
    <text x="12" y="58" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Guidance Department</text>
    <text x="12" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Trained educators offering</text>
    <text x="12" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">non-judgmental listening.</text>
    <text x="12" y="120" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Academic &amp; Social</text>
    <text x="12" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Navigating peer pressure,</text>
    <text x="12" y="152" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">bullying, or emotional stress.</text>
    <text x="12" y="185" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Confidentiality</text>
    <text x="12" y="203" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Safe space within the</text>
    <text x="12" y="217" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">school environment.</text>
    <rect x="10" y="245" width="150" height="30" rx="6" fill="#0c4a6e"/>
    <text x="85" y="264" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">School G&amp;C Office</text>
  </g>

  <!-- Level 2: Parents -->
  <g transform="translate(220, 95)">
    <rect width="170" height="290" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="170" height="34" rx="10" fill="#059669"/>
    <text x="85" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">2. PARENTS / GUARDIANS</text>
    <text x="12" y="58" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Primary Protectors</text>
    <text x="12" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">God-given advocates for</text>
    <text x="12" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">safety and welfare.</text>
    <text x="12" y="120" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Honest Dialogue</text>
    <text x="12" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Sharing fears, harassment,</text>
    <text x="12" y="152" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">or online threats early.</text>
    <text x="12" y="185" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Lifelong Guidance</text>
    <text x="12" y="203" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Biblical advice rooted in</text>
    <text x="12" y="217" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">deep unconditional love.</text>
    <rect x="10" y="245" width="150" height="30" rx="6" fill="#064e3b"/>
    <text x="85" y="264" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Family Support</text>
  </g>

  <!-- Level 3: Pastoral Care -->
  <g transform="translate(410, 95)">
    <rect width="170" height="290" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="170" height="34" rx="10" fill="#d97706"/>
    <text x="85" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">3. PASTORAL CARE</text>
    <text x="12" y="58" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Spiritual Direction</text>
    <text x="12" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Pastors, youth ministers,</text>
    <text x="12" y="90" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">and Christian Union leaders.</text>
    <text x="12" y="120" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Prayer &amp; Healing</text>
    <text x="12" y="138" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Restoration and freedom</text>
    <text x="12" y="152" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">from guilt or past shame.</text>
    <text x="12" y="185" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Scriptural Counsel</text>
    <text x="12" y="203" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Walking in holiness and</text>
    <text x="12" y="217" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Christian maturity.</text>
    <rect x="10" y="245" width="150" height="30" rx="6" fill="#78350f"/>
    <text x="85" y="264" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Church / CU Mentors</text>
  </g>

  <!-- Level 4: National Emergency Lines -->
  <g transform="translate(600, 95)">
    <rect width="170" height="290" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <rect width="170" height="34" rx="10" fill="#be123c"/>
    <text x="85" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">4. EMERGENCY HELPLINES</text>
    <text x="12" y="58" fill="#f43f5e" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Childline Kenya</text>
    <text x="12" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Toll-Free 24/7 Hotline:</text>
    <text x="12" y="94" fill="#fda4af" font-family="system-ui, sans-serif" font-size="14" font-weight="800">DIAL: 116</text>
    <text x="12" y="125" fill="#f43f5e" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• National GBV Line</text>
    <text x="12" y="143" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Gender-Based Violence:</text>
    <text x="12" y="161" fill="#fda4af" font-family="system-ui, sans-serif" font-size="14" font-weight="800">DIAL: 1195</text>
    <text x="12" y="192" fill="#f43f5e" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Free &amp; Confidential</text>
    <text x="12" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Immediate crisis rescue</text>
    <text x="12" y="224" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">and legal protection.</text>
    <rect x="10" y="245" width="150" height="30" rx="6" fill="#881337"/>
    <text x="85" y="264" fill="#fda4af" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Emergency Support</text>
  </g>

  <text x="400" y="425" fill="#64748b" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">VLEARN CBC SENIOR SECONDARY CRE CURRICULUM — TOPIC 4.3</text>
</svg>"""


# ─── CURRICULUM DATA PAYLOAD (8 LESSONS, 6 PAGES PER LESSON) ───────────────

def build_topic_4_3_curriculum():
    return [
        # =====================================================================
        # LESSON 1: Understanding Human Sexuality
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "4.3.1 Understanding Human Sexuality",
            "unit_description": "Comprehensive exploration of human sexuality across biological, psychological, emotional, and social dimensions, grounded in Genesis 1:27 and Psalm 139:14.",
            "lesson_title": "Understanding Human Sexuality",
            "wikimedia_asset": {
                "title": "Adolescent Development and Holistic Youth Growth",
                "caption": "A vibrant group of young African secondary school students engaging in collaborative dialogue, exemplifying holistic physical, social, and emotional growth.",
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Secondary_school_students_in_uniform_Kenya.jpg/800px-Secondary_school_students_in_uniform_Kenya.jpg",
                "author": "Wikimedia Commons / Educational Archives",
                "source": "Wikimedia Commons",
                "licensing": "CC BY-SA 4.0"
            },
            "svg_func": get_svg_lesson_1,
            "youtube_asset": {
                "title": "BibleProject: Sex & Wholeness — God's Design",
                "youtube_id": "YbipxEDPryg",
                "url": "https://www.youtube.com/watch?v=YbipxEDPryg",
                "description": "An engaging exploration of how biblical theology views human identity, gender, and relational wholeness in God's good creation."
            },
            "pages": [
                # PAGE 1: Hook, Objectives & Real-Life Launch
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: Holistic Youth Development",
                        "content": {
                            "title": "Visual Hook: Holistic Youth Development",
                            "caption": "Young secondary school learners discussing personal growth, emotional maturity, and the values of mutual respect in youth development.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Secondary_school_students_in_uniform_Kenya.jpg/800px-Secondary_school_students_in_uniform_Kenya.jpg",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Secondary_school_students_in_uniform_Kenya.jpg/800px-Secondary_school_students_in_uniform_Kenya.jpg",
                            "author": "Wikimedia Commons",
                            "source": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives",
                        "content": {
                            "goals": [
                                "Define **human sexuality** from a comprehensive, holistic Christian perspective beyond mere biological attraction.",
                                "Analyze the four interrelated dimensions of sexuality: **Biological, Psychological, Emotional, and Social/Relational**.",
                                "Refute the cultural misconception that sexuality is inherently sinful or shameful.",
                                "Demonstrate appreciation for God's creation of humanity as male and female declared 'very good' in Genesis 1:31."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Sharing Experiences & Real-Life Hook",
                        "content": {
                            "markdown": "### What is Human Sexuality?\nWhen many people hear the word *sexuality*, they often think strictly about physical attraction or biological differences. However, from a biblical and developmental perspective, human sexuality is a multi-dimensional gift encompassing our entire being as male and female.\n\n> **Class Activity (5 mins):** Write down three distinct words describing what it means to transition from childhood into a mature young woman or man. Notice how these changes touch not only our physical bodies, but also our thoughts, self-worth, and social relationships."
                        }
                    }
                ],
                # PAGE 2: Core Scriptural Foundation & Dimensions
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Four Dimensions of Sexuality",
                        "content": {
                            "markdown": "### The Multi-Dimensional Spectrum of Sexuality\nHuman sexuality integrates four essential dimensions that develop simultaneously during adolescence:\n\n1. **Biological Dimension**: The physical and physiological traits that distinguish male and female, including chromosomes, reproductive organs, and hormonal transitions during puberty.\n2. **Psychological Dimension**: An individual's self-image, cognitive identity, mental perceptions, and personal understanding of being male or female.\n3. **Emotional Dimension**: The capacity for deep feelings, affection, romantic attraction, empathy, and the desire for relational connection.\n4. **Social/Relational Dimension**: How we communicate, build respectful friendships, establish interpersonal boundaries, and interact within our school and community."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Theological Dimensions Matrix",
                        "content": {
                            "markdown": "### Biblical Reflection Across Dimensions\n\n| Dimension | Key Characteristics | Core Biblical Reference |\n| :--- | :--- | :--- |\n| **Biological** | Physical growth, secondary sexual traits, reproductive capacity | **Genesis 1:27** — *God created them male and female.* |\n| **Psychological** | Developing self-identity, self-esteem, cognitive maturity | **Psalm 139:14** — *I am fearfully and wonderfully made.* |\n| **Emotional** | Desiring deep affection, navigating infatuation and attraction | **Proverbs 4:23** — *Above all else, guard your heart.* |\n| **Social** | Interpersonal communication, peer boundaries, godly community | **Hebrews 10:24** — *Spur one another toward love and good deeds.* |"
                        }
                    }
                ],
                # PAGE 3: Pedagogical Vector Diagram & Misconception Analysis
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Visual Architecture: Holistic Human Sexuality",
                        "content": {
                            "title": "Visual Architecture: Holistic Human Sexuality",
                            "caption": "Comprehensive pedagogical diagram mapping the Biological, Psychological, Emotional, and Social dimensions of human sexuality.",
                            "svg": get_svg_lesson_1(),
                            "svg_xml": get_svg_lesson_1()
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Misconception Analysis: Sexuality vs The Fall",
                        "content": {
                            "markdown": "### Correcting a Widespread Cultural Misconception\n\n> **Common Misconception:** The Bible teaches that human sexuality is inherently dirty, shameful, or the original sin committed in the Garden of Eden.\n>\n> **Biblical Correction:** Human sexuality was created and blessed by God **before** sin entered the world. In Genesis 1:31, after establishing male and female with their relational and reproductive faculties, God declared everything He had made to be *\"very good.\"* Guilt, exploitation, and shame entered only after disobedience disrupted human communion with God (Genesis 3:7). Within its God-given covenant boundaries, human sexuality is sacred, honorable, and pure."
                        }
                    }
                ],
                # PAGE 4: Practical Life Application & Holistic Growth
                [
                    {
                        "type": "step_process",
                        "title": "Practical Life Toolkit: Navigating Puberty & Wholeness",
                        "content": {
                            "title": "Steps to Cultivating Holistic Maturity",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Celebrate God's Bodily Design",
                                    "description": "Accept your physical growth and developmental pace with gratitude to God, rejecting unrealistic social media beauty standards."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Renew Your Mind Daily",
                                    "description": "Guard your thought life and mental identity by filling your mind with scripture and wholesome educational resources."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Exercise Emotional Patience",
                                    "description": "Acknowledge romantic feelings without rushing into premature relationships, allowing emotional maturity to guide your choices."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Cultivate Respectful Friendships",
                                    "description": "Interact with members of the opposite sex with absolute purity, honor, and transparent communication."
                                }
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Kenyan Youth Context: Navigating Media & Peer Myths",
                        "content": {
                            "markdown": "### Realities in Kenyan Senior Secondary Schools\nIn today's interconnected world, Kenyan teenagers are exposed to conflicting messages about sexuality from music videos, social media influencers, and sensationalized gossip. Understanding that sexuality encompasses your total personhood—spiritual, emotional, and social—empowers you to resist reductive narratives that treat youth as sexualized objects."
                        }
                    }
                ],
                # PAGE 5: Curated Video & Spiritual Reflection
                [
                    {
                        "type": "suggested_video",
                        "title": "BibleProject: Sex & Wholeness",
                        "content": {
                            "title": "BibleProject: Sex & Wholeness",
                            "youtube_id": "YbipxEDPryg",
                            "url": "https://www.youtube.com/watch?v=YbipxEDPryg",
                            "description": "Examines God's original intent for relational unity, identity, and the holiness of human sexuality across the biblical narrative."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Spiritual Reflection & Ethical Values",
                        "content": {
                            "markdown": "### Living in the Light of God's Creation\n- **Core Value:** *Integrity & Self-Respect* — Recognizing that your body and mind are divinely designed inspires deep self-respect and reverence for others.\n- **Reflective Question:** In what ways can you honor your emotional and social dimensions when interacting with your classmates this week?\n- **Memory Verse:** *\"I praise you because I am fearfully and wonderfully made; your works are wonderful, I know that full well.\"* (Psalm 139:14)"
                        }
                    }
                ],
                # PAGE 6: Summary & Knowledge Check
                [
                    {
                        "type": "key_takeaway",
                        "title": "Summary & Core Principles",
                        "content": {
                            "title": "Core Takeaways: Understanding Human Sexuality",
                            "takeaways": [
                                "Human sexuality is a multi-dimensional gift encompassing Biological, Psychological, Emotional, and Social dimensions.",
                                "Sexuality was instituted before the Fall of Man and declared 'very good' by God in Genesis 1:31.",
                                "Adolescence involves simultaneous physical changes, emotional awakening, and identity formation requiring biblical guidance.",
                                "Purity and self-control protect human dignity and nurture long-term psychological and spiritual flourishing."
                            ]
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Knowledge Check",
                        "content": {
                            "question": "Which of the following aspects of human sexuality pertains directly to physical growth, chromosomes, and hormonal transitions during puberty?",
                            "options": [
                                "A) Psychological dimension",
                                "B) Emotional dimension",
                                "C) Biological dimension",
                                "D) Social dimension"
                            ],
                            "answer": "C",
                            "explanation": "The biological dimension encompasses chromosomes, reproductive anatomy, secondary sexual traits, and hormonal changes during puberty."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: God's Design for Male-Female Relationships
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "4.3.2 God's Design for Male-Female Relationships",
            "unit_description": "Examines equality, complementarity, and covenant intentionality in Genesis 2:18-24 and the standard of absolute purity in 1 Timothy 5:1-2.",
            "lesson_title": "God's Design for Male-Female Relationships",
            "wikimedia_asset": {
                "title": "Wholesome Youth Fellowship and Mutual Respect",
                "caption": "Secondary school male and female learners participating in collaborative group discussions on Christian leadership and campus integrity.",
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Kenyan_students_in_classroom_discussion.jpg/800px-Kenyan_students_in_classroom_discussion.jpg",
                "author": "Wikimedia Commons / Global Education",
                "source": "Wikimedia Commons",
                "licensing": "CC BY-SA 4.0"
            },
            "svg_func": get_svg_lesson_2,
            "youtube_asset": {
                "title": "BibleProject: Genesis 1-2 Creation & Covenant Relationships",
                "youtube_id": "KOUV7mW4i40",
                "url": "https://www.youtube.com/watch?v=KOUV7mW4i40",
                "description": "Explores the relational architecture of Genesis 2, highlighting mutual companionship, equal dignity, and covenant commitment."
            },
            "pages": [
                # PAGE 1: Hook, Objectives & Launch
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: Wholesome Male-Female Fellowship",
                        "content": {
                            "title": "Visual Hook: Wholesome Male-Female Fellowship",
                            "caption": "Students demonstrating supportive, honorable peer relationships founded on mutual respect and shared academic goals.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Kenyan_students_in_classroom_discussion.jpg/800px-Kenyan_students_in_classroom_discussion.jpg",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Kenyan_students_in_classroom_discussion.jpg/800px-Kenyan_students_in_classroom_discussion.jpg",
                            "author": "Wikimedia Commons",
                            "source": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives",
                        "content": {
                            "goals": [
                                "Examine the biblical concept of **co-equality and complementarity** between man and woman in Genesis 2:18-24.",
                                "Analyze the Four Pillars of Christian male-female interaction: **Mutual Respect, Pure Motives, Clear Boundaries, and Spiritual Edification**.",
                                "Apply the apostolic standard of **1 Timothy 5:1-2** (treating young women as sisters and young men as brothers with absolute purity).",
                                "Formulate practical guidelines for maintaining healthy, non-compromising opposite-sex friendships."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Sharing Experiences & Biblical Context",
                        "content": {
                            "markdown": "### Created for Meaningful Community\nGod did not design human beings to exist in isolated self-sufficiency. In the Garden of Eden, before the entrance of sin, God noted the single condition that was *\"not good\"*: for man to be alone (Genesis 2:18). God created woman as a corresponding partner (*Ezer Kenegdo*), establishing a relationship characterized by mutual honor, partnership, and spiritual oneness."
                        }
                    }
                ],
                # PAGE 2: Scripture Study: Genesis 2 & 1 Timothy 5
                [
                    {
                        "type": "concept_explanation",
                        "title": "Biblical Foundation: Genesis 2:18-24",
                        "content": {
                            "markdown": "### Genesis 2: The Covenant of Companionship\n\n> *\"The Lord God said, 'It is not good for the man to be alone. I will make a helper suitable for him.' ... Then the Lord God made a woman from the rib he had taken out of the man, and he brought her to the man. The man said, 'This is now bone of my bones and flesh of my flesh...' That is why a man leaves his father and mother and is united to his wife, and they become one flesh.\"* (Genesis 2:18, 22-24)\n\n#### Key Insights:\n- **Equal Essence**: The phrase *\"bone of my bones\"* signifies equal spiritual and moral nature. Woman was not made from man's head to rule over him, nor from his feet to be crushed by him, but from his side to stand equal beside him.\n- **Complementary Partnership**: Male and female possess distinct yet complementary gifts designed to work in harmonious synergy."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Four Pillars of Male-Female Relationships",
                        "content": {
                            "markdown": "### Four Foundations of Godly Relationship\n1. **Mutual Respect**: Viewing members of the opposite sex as bearers of God's image (*Imago Dei*), refusing to reduce anyone to a sexual object or tool of gratification.\n2. **Pure Motives**: Keeping interactions transparent, honest, and free of emotional manipulation or false promises.\n3. **Emotional Boundaries**: Guarding the heart against prematurely awakening romantic passions before one is ready for marriage (Song of Songs 8:4).\n4. **Spiritual Fellowship**: Encouraging one another in academic discipline, Christian devotion, and community service."
                        }
                    }
                ],
                # PAGE 3: Visual Vector Architecture & Apostolic Standard
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Visual Architecture: God's Relational Design",
                        "content": {
                            "title": "Visual Architecture: God's Relational Design",
                            "caption": "Diagram depicting Co-Equality, Covenant Intentionality, and the Four Pillars of Christian Youth Relationships.",
                            "svg": get_svg_lesson_2(),
                            "svg_xml": get_svg_lesson_2()
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Apostolic Rule: 1 Timothy 5:1-2",
                        "content": {
                            "markdown": "### The Sibling Paradigm for Campus Life\n\n> *\"Treat younger men as brothers, older women as mothers, and younger women as sisters, with absolute purity.\"* (1 Timothy 5:1-2)\n\nApostle Paul provides a transformative mental framework: treat classmates of the opposite sex as your biological brothers and sisters in Christ. When you view a classmate as a sister or brother, your instinct is to protect their honor, guard their safety, and promote their spiritual well-being."
                        }
                    }
                ],
                # PAGE 4: Practical Life Application: Sibling Purity in Practice
                [
                    {
                        "type": "step_process",
                        "title": "Practical Life Toolkit: Campus Friendship Standards",
                        "content": {
                            "title": "How to Build Pure Opposite-Sex Friendships",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Interact in Group Settings",
                                    "description": "Engage in study groups, debates, and Christian Union ministries in well-lit, public environments."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Maintain Clear Communication",
                                    "description": "Be honest about your intentions and avoid sending flirtatious, ambiguous, or misleading signals."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Respect Personal Boundaries",
                                    "description": "Uphold physical modesty and emotional restraint, respecting each other's personal space and privacy."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Encourage Academic & Spiritual Goals",
                                    "description": "Partner together to excel in schoolwork, discuss scripture, and support community service projects."
                                }
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Ethical Reflection: Overcoming Objectification",
                        "content": {
                            "markdown": "### Guarding Against Exploitative Trends\nIn many secondary schools, peer culture encourages ranking classmates by physical appearance or treating dating as a trophy sport. Christian students are called to be counter-cultural leaders who model genuine respect and honor for every individual's dignity."
                        }
                    }
                ],
                # PAGE 5: Video Resource & Faith Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "BibleProject: Creation & Covenant Relationships",
                        "content": {
                            "title": "BibleProject: Creation & Covenant Relationships",
                            "youtube_id": "KOUV7mW4i40",
                            "url": "https://www.youtube.com/watch?v=KOUV7mW4i40",
                            "description": "Deep-dive animation into the theological richness of Genesis 1-2 and the beauty of complementary human relationships."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Spiritual Reflection & Values",
                        "content": {
                            "markdown": "### Walking in Absolute Purity\n- **Core Value:** *Respect & Brotherly Love* — Treating every peer with the honor due to a child of God.\n- **Personal Challenge:** How can you actively encourage an opposite-sex classmate in their academic and spiritual journey this term?\n- **Key Verse:** *\"Treat younger women as sisters, with absolute purity.\"* (1 Timothy 5:2)"
                        }
                    }
                ],
                # PAGE 6: Summary & Knowledge Check
                [
                    {
                        "type": "key_takeaway",
                        "title": "Summary & Core Principles",
                        "content": {
                            "title": "Core Takeaways: God's Design for Relationships",
                            "takeaways": [
                                "Male and female are created equal in divine image and complementary in purpose (Genesis 2:18-24).",
                                "Christian youth relationships must be governed by mutual respect, pure motives, clear boundaries, and spiritual edification.",
                                "Apostle Paul instructs believers to treat opposite-sex peers as brothers and sisters with absolute purity (1 Timothy 5:1-2).",
                                "Healthy opposite-sex friendships thrive in open group settings with transparent communication."
                            ]
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Knowledge Check",
                        "content": {
                            "question": "According to 1 Timothy 5:1-2, how should a Christian young man treat young women in the school and church community?",
                            "options": [
                                "A) As rivals in academic competition",
                                "B) As sisters, with absolute purity",
                                "C) With emotional distance and total silence",
                                "D) As potential romantic targets for social status"
                            ],
                            "answer": "B",
                            "explanation": "Paul explicitly instructs Timothy and believers to treat younger women as sisters, with absolute purity, fostering a safe and honorable family mindset."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Dating vs. Courtship
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "4.3.3 Dating vs. Courtship",
            "unit_description": "Contrasting secular dating models with biblical courtship across purpose, community involvement, emotional protection, and physical boundaries.",
            "lesson_title": "Dating vs. Courtship: Purpose, Accountability and Boundaries",
            "wikimedia_asset": {
                "title": "Mentorship, Family Guidance, and Youth Integrity",
                "caption": "A Christian family and mentor engaging with young adults in an open dialogue about relationship values, character, and future marital readiness.",
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/African_family_mentorship_discussion.jpg/800px-African_family_mentorship_discussion.jpg",
                "author": "Wikimedia Commons / Community Heritage",
                "source": "Wikimedia Commons",
                "licensing": "CC BY-SA 4.0"
            },
            "svg_func": get_svg_lesson_3,
            "youtube_asset": {
                "title": "BibleProject: Covenant Wisdom in Relationships",
                "youtube_id": "7v_7k_6fH4M",
                "url": "https://www.youtube.com/watch?v=7v_7k_6fH4M",
                "description": "Explores the biblical concept of covenant versus consumer relationships, demonstrating how wisdom guards our hearts."
            },
            "pages": [
                # PAGE 1: Hook, Objectives & Real-World Launch
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: Family Mentorship & Guidance",
                        "content": {
                            "title": "Visual Hook: Family Mentorship & Guidance",
                            "caption": "Mentors and parents providing wisdom and relational accountability to young people preparing for mature adulthood.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/African_family_mentorship_discussion.jpg/800px-African_family_mentorship_discussion.jpg",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/African_family_mentorship_discussion.jpg/800px-African_family_mentorship_discussion.jpg",
                            "author": "Wikimedia Commons",
                            "source": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives",
                        "content": {
                            "goals": [
                                "Distinguish clearly between the worldview paradigms of **Secular Dating** and **Biblical Courtship**.",
                                "Analyze the role of **parental, pastoral, and community accountability** in protecting romantic relationships.",
                                "Evaluate why casual dating during teenage years frequently produces emotional fragmentation and moral vulnerability.",
                                "Commit to preserving physical and emotional intimacy exclusively for the lifelong covenant of marriage."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Sharing Experiences & Cultural Contrast",
                        "content": {
                            "markdown": "### Navigating Romantic Messages as a Teenager\nAs adolescents experience romantic attraction, contemporary culture bombards them with movies, songs, and peer pressures promoting casual dating. However, biblical wisdom calls believers to examine the underlying motivations and outcomes of relationship models."
                        }
                    }
                ],
                # PAGE 2: Detailed Paradigm Comparison
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Fundamentals: Dating vs Courtship",
                        "content": {
                            "markdown": "### Contrasting Two Divergent Paradigms\n\n1. **The Ultimate Goal**:\n   - *Secular Dating*: Often treated as a recreational pastime to boost popularity, alleviate loneliness, or satisfy curiosity with no long-term commitment in view.\n   - *Biblical Courtship*: An intentional, purposeful journey undertaken by mature individuals with the specific goal of evaluating spiritual, character, and intellectual compatibility for marriage.\n\n2. **The Social Context (Involvement)**:\n   - *Secular Dating*: Typically conducted in secrecy and isolated from parents or mentors, which dramatically elevates moral and emotional risk.\n   - *Biblical Courtship*: Deeply rooted in community oversight, inviting guidance, prayer, and protection from parents, pastors, and trusted mentors."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Comparative Analysis Matrix",
                        "content": {
                            "markdown": "### Core Feature Comparison\n\n| Feature | Secular Dating | Biblical Courtship |\n| :--- | :--- | :--- |\n| **Primary Motivation** | Self-fulfillment, recreational fun, emotional validation | Seeking God's will, honoring the other, marriage evaluation |\n| **Accountability** | Private, secret, isolated from family | Transparent, mentored by parents and church leaders |\n| **Physical Boundaries** | Often compromises purity; physical intimacy precedes commitment | Strict holiness; physical intimacy reserved exclusively for marriage |\n| **Emotional Impact** | Frequent serial breakups, emotional scars, guilt | Clarity, mutual protection, emotional trust, peace |"
                        }
                    }
                ],
                # PAGE 3: Visual Vector Comparison Diagram
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Visual Architecture: Dating vs Courtship Paradigm",
                        "content": {
                            "title": "Visual Architecture: Dating vs Courtship Paradigm",
                            "caption": "Side-by-side comparison of Secular Dating vs Biblical Courtship highlighting goals, focus, accountability, and spiritual outcomes.",
                            "svg": get_svg_lesson_3(),
                            "svg_xml": get_svg_lesson_3()
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Wisdom of Waiting: Song of Songs 8:4",
                        "content": {
                            "markdown": "### Guarding the Seasons of Life\n\n> *\"Daughters of Jerusalem, I charge you: Do not arouse or awaken love until it so desires.\"* (Song of Songs 8:4)\n\nScripture uses the imagery of awakening love to teach emotional timing. Starting romantic entanglements before one is spiritually, emotionally, and financially prepared for marriage is like plucking unripened fruit—it causes unnecessary bitterness and emotional heartache."
                        }
                    }
                ],
                # PAGE 4: Practical Decision Framework for Secondary Students
                [
                    {
                        "type": "step_process",
                        "title": "Practical Life Toolkit: The Youth Relationship Filter",
                        "content": {
                            "title": "How to Navigate Romantic Attractions Wisely",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Channel Energy into Purpose",
                                    "description": "Focus your primary energy during high school on spiritual growth, academic excellence, and talent development."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Avoid Secret Emotional Entanglements",
                                    "description": "Refuse one-on-one secret dating arrangements that isolate you from your family and church mentors."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Cultivate Character First",
                                    "description": "Become the godly, responsible, and disciplined person that a future godly spouse would hope to marry."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Maintain Open Parental Dialogue",
                                    "description": "Share your feelings, crushes, and social challenges honestly with your parents or guardians."
                                }
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Ethical Case Study: The Pressure of 'Coupling Up'",
                        "content": {
                            "markdown": "### Case Study: Peer Culture in High School\nIn Form 3, a group of students pressure Brian to get a girlfriend so he won't be seen as 'left out.' Brian knows he wants to focus on KCSE preparation and his Christian Union leadership. By applying biblical wisdom, Brian recognizes that romantic companionship is too sacred to be used as a social trophy."
                        }
                    }
                ],
                # PAGE 5: Video Resource & Faith Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "BibleProject: Covenant Wisdom in Relationships",
                        "content": {
                            "title": "BibleProject: Covenant Wisdom in Relationships",
                            "youtube_id": "7v_7k_6fH4M",
                            "url": "https://www.youtube.com/watch?v=7v_7k_6fH4M",
                            "description": "Illustrates how covenant faithfulness and godly wisdom protect human relationships from the perils of consumerism."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Spiritual Reflection & Ethical Values",
                        "content": {
                            "markdown": "### Purpose over Impulse\n- **Core Value:** *Patience & Self-Control* — Trusting God's timing for love rather than conforming to worldly impatience.\n- **Reflection Question:** What are the tangible benefits of focusing on academic and character development during your secondary school years?\n- **Key Verse:** *\"Do not arouse or awaken love until it so desires.\"* (Song of Songs 8:4)"
                        }
                    }
                ],
                # PAGE 6: Summary & Knowledge Check
                [
                    {
                        "type": "key_takeaway",
                        "title": "Summary & Core Principles",
                        "content": {
                            "title": "Core Takeaways: Dating vs Courtship",
                            "takeaways": [
                                "Secular dating is typically recreational, self-centered, and isolated from family accountability.",
                                "Biblical courtship is purposeful, others-centered, and conducted with parental and church mentorship.",
                                "Courtship prioritizes spiritual and character compatibility while guarding physical intimacy strictly for marriage.",
                                "Song of Songs 8:4 warns against awakening romantic passions before marital readiness."
                            ]
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Knowledge Check",
                        "content": {
                            "question": "What is the primary distinguishing feature of Biblical Courtship compared to Secular Dating?",
                            "options": [
                                "A) Courtship is practiced in complete secrecy without parental knowledge",
                                "B) Courtship is an intentional, mentored process with the specific purpose of evaluating marriage readiness",
                                "C) Dating requires lifelong commitment, while courtship is for casual entertainment",
                                "D) Courtship eliminates all emotional boundaries and personal accountability"
                            ],
                            "answer": "B",
                            "explanation": "Biblical courtship is characterized by intentionality, family and pastoral accountability, and the explicit purpose of evaluating marriage readiness in holiness."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Understanding Peer Pressure in Sexuality
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "4.3.4 Understanding Peer Pressure in Sexuality",
            "unit_description": "Examines direct vs. indirect peer influence, psychological vulnerability during adolescence, and biblical warnings against sinful enticement in Proverbs 1:10.",
            "lesson_title": "Understanding Peer Pressure in Human Sexuality",
            "wikimedia_asset": {
                "title": "Adolescent Peer Group Dynamics and Decision-Making",
                "caption": "A group of secondary school youth discussing social challenges, illustrating the powerful role of peer influence and group dynamics in adolescent life.",
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Youth_peer_group_interaction.jpg/800px-Youth_peer_group_interaction.jpg",
                "author": "Wikimedia Commons / Youth Development",
                "source": "Wikimedia Commons",
                "licensing": "CC BY-SA 4.0"
            },
            "svg_func": get_svg_lesson_4,
            "youtube_asset": {
                "title": "BibleProject: Proverbs & Wisdom in Peer Influence",
                "youtube_id": "Gab04dPs_uQ",
                "url": "https://www.youtube.com/watch?v=Gab04dPs_uQ",
                "description": "Explores the Book of Proverbs on navigating peer influence, resisting corrupting companions, and embracing the fear of the Lord."
            },
            "pages": [
                # PAGE 1: Hook, Objectives & Real-Life Launch
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: Peer Group Dynamics",
                        "content": {
                            "title": "Visual Hook: Peer Group Dynamics",
                            "caption": "Young learners engaging in peer group conversations, demonstrating how social pressure shapes attitudes and behaviors.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Youth_peer_group_interaction.jpg/800px-Youth_peer_group_interaction.jpg",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Youth_peer_group_interaction.jpg/800px-Youth_peer_group_interaction.jpg",
                            "author": "Wikimedia Commons",
                            "source": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives",
                        "content": {
                            "goals": [
                                "Define **peer pressure** and identify its specific manifestations in the area of human sexuality.",
                                "Differentiate between **Direct/Explicit Pressure** and **Indirect/Implicit Pressure** in school environments.",
                                "Analyze psychological factors that increase teenage vulnerability to negative peer influence.",
                                "Apply the biblical warning of **Proverbs 1:10** to resist sinful enticements with courage."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Sharing Experiences & Defining Peer Pressure",
                        "content": {
                            "markdown": "### What is Peer Pressure?\nPeer pressure is the powerful influence exerted by a social group or individual friends encouraging others to conform in thoughts, attitudes, dress, speech, or sexual behavior. During adolescence, the natural psychological desire for belonging, social acceptance, and identity validation makes youth especially susceptible to peer influence."
                        }
                    }
                ],
                # PAGE 2: Direct vs Indirect Pressure Breakdown
                [
                    {
                        "type": "concept_explanation",
                        "title": "Two Forms of Peer Pressure in Sexuality",
                        "content": {
                            "markdown": "### 1. Direct (Explicit) Peer Pressure\nOccurs when peers directly challenge, dare, demand, or mock an individual to engage in sexual behavior, view illicit media, or participate in compromising activities.\n- **Examples**: Direct verbal dares (*\"Prove you're a real man\"*), coercive dating ultimatums (*\"If you love me, you will do this\"*), or pressure to share indecent photos.\n\n### 2. Indirect (Implicit) Peer Pressure\nThe subtle, unspoken psychological conditioning that makes a teenager feel that *\"everyone is doing it\"* and that maintaining moral purity makes one weird or outcast.\n- **Examples**: Social media trends glorifying casual sex, corridor gossip boasting about sexual exploits, and television programming normalizing premarital intimacy."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Critical Analysis: Why Indirect Pressure is Dangerous",
                        "content": {
                            "markdown": "### The Power of Indirect Conditioning\nIndirect peer pressure is often harder to resist than direct pressure because it operates subconsciously. It attacks a young person's sense of belonging by whispering that purity leads to loneliness. Christian discernment helps students recognize that popularity based on moral compromise is fleeting and destructive."
                        }
                    }
                ],
                # PAGE 3: Visual Vector Diagram & Scriptural Warning
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Visual Architecture: Anatomy of Peer Pressure",
                        "content": {
                            "title": "Visual Architecture: Anatomy of Peer Pressure",
                            "caption": "Diagram showing the convergence of Direct and Indirect pressure vectors on the adolescent will, contrasted with the biblical shield of Proverbs 1:10.",
                            "svg": get_svg_lesson_4(),
                            "svg_xml": get_svg_lesson_4()
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Biblical Warning: Proverbs 1:10",
                        "content": {
                            "markdown": "### The Wisdom of Solomon\n\n> *\"My son, if sinful men entice you, do not give in to them.\"* (Proverbs 1:10)\n\nKing Solomon recognized that the greatest danger to a young leader is enticement by peers who mock righteousness. The Hebrew word for *entice* implies luring someone into a hidden trap. God's Word equips us with moral clarity to stand our ground without compromise."
                        }
                    }
                ],
                # PAGE 4: Practical Life Toolkit: Identifying High-Risk Situations
                [
                    {
                        "type": "step_process",
                        "title": "Practical Life Toolkit: Identifying Peer Pressure Traps",
                        "content": {
                            "title": "Recognizing Risk Zones for Peer Pressure",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Unsupervised Parties & House Gatherings",
                                    "description": "Environments where alcohol, substance abuse, and unmonitored rooms create high moral hazard."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Secret WhatsApp / Telegram Groups",
                                    "description": "Online chat rooms where explicit media, gossip, and degrading humor circulate freely."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Compromising Friend Circles",
                                    "description": "Friends who ridicule your faith, mock your sexual boundaries, or celebrate deceit."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Emotional Isolation",
                                    "description": "Keeping your struggles secret rather than seeking counsel from godly parents and mentors."
                                }
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Psychological Insight: The Search for Acceptance",
                        "content": {
                            "markdown": "### Finding Your True Identity in Christ\nWhen teenagers know who they are in Christ—loved, redeemed, and fearfully made—they no longer need the approval of rebellious peers. Divine security produces internal resilience against external social pressure."
                        }
                    }
                ],
                # PAGE 5: Video Resource & Spiritual Reflection
                [
                    {
                        "type": "suggested_video",
                        "title": "BibleProject: Proverbs & Wisdom in Peer Influence",
                        "content": {
                            "title": "BibleProject: Proverbs & Wisdom in Peer Influence",
                            "youtube_id": "Gab04dPs_uQ",
                            "url": "https://www.youtube.com/watch?v=Gab04dPs_uQ",
                            "description": "Explores how the fear of the Lord provides young people with discernment to choose righteous friendships and resist folly."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Spiritual Reflection & Values",
                        "content": {
                            "markdown": "### Stand Fast in Moral Conviction\n- **Core Value:** *Courage & Moral Discernment* — Daring to stand alone for truth when the crowd chooses compromise.\n- **Reflective Question:** Think of one situation where you felt indirect pressure to conform. How did you respond, and what did you learn?\n- **Key Verse:** *\"Do not follow the crowd in doing wrong.\"* (Exodus 23:2)"
                        }
                    }
                ],
                # PAGE 6: Summary & Knowledge Check
                [
                    {
                        "type": "key_takeaway",
                        "title": "Summary & Core Principles",
                        "content": {
                            "title": "Core Takeaways: Understanding Peer Pressure",
                            "takeaways": [
                                "Peer pressure can be Direct (explicit demands, dares, bullying) or Indirect (cultural conditioning, social media trends).",
                                "Adolescent desire for belonging increases vulnerability to negative peer influence.",
                                "Proverbs 1:10 commands believers: 'If sinful men entice you, do not give in to them.'",
                                "True identity and security in Christ provide the moral strength to reject compromise."
                            ]
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Knowledge Check",
                        "content": {
                            "question": "Which of the following is an example of INDIRECT peer pressure regarding human sexuality?",
                            "options": [
                                "A) A classmate verbally daring you to send an explicit photograph",
                                "B) A peer mocking you directly for refusing to kiss someone",
                                "C) The pervasive subtle feeling that 'everyone is sexually active' driven by media and gossip",
                                "D) A dating partner demanding physical intimacy as proof of affection"
                            ],
                            "answer": "C",
                            "explanation": "Indirect peer pressure is the subtle, unspoken atmosphere and media conditioning creating a false perception that 'everyone is doing it.'"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Assertive Strategies to Resist Negative Peer Pressure
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "4.3.5 Assertive Strategies to Resist Negative Peer Pressure",
            "unit_description": "Mastering assertive communication, 'I' statements, reverse pressure, and the biblical model of Joseph's physical flight in Genesis 39.",
            "lesson_title": "Assertive Strategies to Resist Negative Peer Pressure",
            "wikimedia_asset": {
                "title": "Youth Leadership, Integrity, and Moral Standing",
                "caption": "A confident Kenyan high school student standing before peers to articulate values of personal integrity, courage, and moral excellence.",
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Kenyan_student_leader_presentation.jpg/800px-Kenyan_student_leader_presentation.jpg",
                "author": "Wikimedia Commons / Education in Kenya",
                "source": "Wikimedia Commons",
                "licensing": "CC BY-SA 4.0"
            },
            "svg_func": get_svg_lesson_5,
            "youtube_asset": {
                "title": "BibleProject: The Story of Joseph & Moral Integrity",
                "youtube_id": "VbbmP0aLh_Q",
                "url": "https://www.youtube.com/watch?v=VbbmP0aLh_Q",
                "description": "Explores the life of Joseph in Genesis 37-50, focusing on his unwavering moral loyalty to God under intense sexual temptation in Egypt."
            },
            "pages": [
                # PAGE 1: Hook, Objectives & Real-Life Launch
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: Student Leadership & Conviction",
                        "content": {
                            "title": "Visual Hook: Student Leadership & Conviction",
                            "caption": "A student leader demonstrating poise, confidence, and clear communication in standing up for moral standards on campus.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Kenyan_student_leader_presentation.jpg/800px-Kenyan_student_leader_presentation.jpg",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Kenyan_student_leader_presentation.jpg/800px-Kenyan_student_leader_presentation.jpg",
                            "author": "Wikimedia Commons",
                            "source": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives",
                        "content": {
                            "goals": [
                                "Contrast **Passive, Aggressive, and Assertive** communication styles in responding to sexual peer pressure.",
                                "Master three core verbal tactics: **The 'I' Statement, Reverse Pressure, and The Clear Refusal**.",
                                "Analyze Joseph's response to Potiphar's wife in **Genesis 39:1-12** as the ultimate model of spiritual integrity.",
                                "Apply the **Joseph Strategy (Physical Exit)** when verbal boundaries are violated in high-risk environments."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Sharing Experiences: The Power of 'No'",
                        "content": {
                            "markdown": "### The Dilemma of Responding to Pressure\nWhen faced with sexual temptation or aggressive peer pressure, many teenagers freeze or mumble excuses. However, silence is often misinterpreted by peers as hesitation or eventual consent. A Christian leader must master the art of **Assertive Communication**—expressing moral convictions clearly, calmly, and respectfully without becoming defensive or aggressive."
                        }
                    }
                ],
                # PAGE 2: Three Communication Styles & Assertive Tactics
                [
                    {
                        "type": "concept_explanation",
                        "title": "Three Responses to Peer Pressure",
                        "content": {
                            "markdown": "### Communication Styles Evaluated\n\n1. **Passive Response (The Compromise Trap)**:\n   - *Characteristics*: Looking down, nervous laughing, mumbling *\"Maybe later\"* or *\"I don't know.\"*\n   - *Danger*: Signals weakness; aggressive peers will continue pushing until boundaries collapse.\n\n2. **Aggressive Response (The Conflict Trap)**:\n   - *Characteristics*: Shouting, hurling insults, threatening physical violence.\n   - *Danger*: Escalates hostility and diverts attention away from the moral issue into unnecessary violence.\n\n3. **Assertive Response (The Christian Ideal)**:\n   - *Characteristics*: Direct eye contact, calm posture, clear voice, unambiguous statement of personal standards.\n   - *Outcome*: Commands respect, protects moral purity, and diffuses peer manipulation."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Verbal Defense Playbook",
                        "content": {
                            "markdown": "### Practical Verbal Tactics\n- **Tactic 1: The 'I' Statement** — *\"I have made a personal commitment to biblical purity, and I do not compromise on that.\"*\n- **Tactic 2: Reverse Pressure** — Turn the question back onto the pressurer: *\"Why are you so obsessed with trying to change my moral choices? Let's talk about something that actually matters.\"*\n- **Tactic 3: The Broken Record** — Calmly repeat your boundary without entering into circular arguments: *\"No, I am not participating.\"*"
                        }
                    }
                ],
                # PAGE 3: Visual Vector Diagram & Joseph's Biblical Flight
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Visual Architecture: The Assertive Compass & Joseph Strategy",
                        "content": {
                            "title": "Visual Architecture: The Assertive Compass & Joseph Strategy",
                            "caption": "Infographic illustrating Passive vs Aggressive vs Assertive communication, paired with Joseph's decisive physical flight in Genesis 39.",
                            "svg": get_svg_lesson_5(),
                            "svg_xml": get_svg_lesson_5()
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Biblical Case Study: Joseph in Genesis 39",
                        "content": {
                            "markdown": "### Joseph's Heroic Stand (Genesis 39:1-12)\nIn Egypt, Joseph was an administrative leader in Potiphar's house. Potiphar's wife cornered him daily, demanding, *\"Come to bed with me!\"*\n\n#### Joseph's Four-Step Strategy:\n1. **Verbal Loyalty**: He articulated his loyalty to his earthly master (Potiphar).\n2. **Theological Clarity**: He framed sexual immorality correctly as sin against God: *\"How then could I do such a wicked thing and sin against God?\"* (Genesis 39:9).\n3. **Relational Avoidance**: He refused to be alone with her in closed rooms (Genesis 39:10).\n4. **Physical Exit (The Flight)**: When she grabbed his cloak, Joseph did not debate—he ran out of the house, leaving his garment behind. He prioritized moral purity over comfort, career, and physical safety."
                        }
                    }
                ],
                # PAGE 4: Practical Life Application: Executing Physical Exits
                [
                    {
                        "type": "step_process",
                        "title": "Practical Life Toolkit: The Joseph Strategy Protocol",
                        "content": {
                            "title": "How to Execute a Clean Physical Exit",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Recognize the Trap Early",
                                    "description": "Identify when a social setting or private encounter is turning sexually dangerous or compromising."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Deliver an Unambiguous 'No'",
                                    "description": "Speak a firm, calm refusal while establishing physical distance."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Leave the Environment Immediately",
                                    "description": "Do not linger to argue, apologize, or negotiate. Walk out the door to a public, safe area."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Report and Seek Accountability",
                                    "description": "Inform a trusted teacher, parent, or counselor if coercion, blackmail, or harassment occurred."
                                }
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Ethical Reflection: Valuing God Above Reputation",
                        "content": {
                            "markdown": "### The Cost and Crown of Integrity\nJoseph was falsely accused and thrown into prison after running away, but God was with him in the prison and ultimately exalted him as prime minister of Egypt (Genesis 41). Short-term social discomfort or false accusations can never outweigh the enduring blessing of walking in divine favor and clean conscience."
                        }
                    }
                ],
                # PAGE 5: Video Resource & Faith Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "BibleProject: Joseph & Moral Integrity",
                        "content": {
                            "title": "BibleProject: Joseph & Moral Integrity",
                            "youtube_id": "VbbmP0aLh_Q",
                            "url": "https://www.youtube.com/watch?v=VbbmP0aLh_Q",
                            "description": "Traces the dramatic narrative of Joseph, highlighting how covenant faithfulness and steadfast moral courage overcome adversity."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Spiritual Reflection & Values",
                        "content": {
                            "markdown": "### Flee from Immorality\n- **Core Value:** *Courage & Moral Fortitude* — Having the strength to run from compromising environments rather than testing your willpower.\n- **Personal Reflection:** What is your planned physical exit strategy if you find yourself in a compromising situation at a social gathering?\n- **Key Verse:** *\"How then could I do such a wicked thing and sin against God?\"* (Genesis 39:9)"
                        }
                    }
                ],
                # PAGE 6: Summary & Knowledge Check
                [
                    {
                        "type": "key_takeaway",
                        "title": "Summary & Core Principles",
                        "content": {
                            "title": "Core Takeaways: Assertive Resistance",
                            "takeaways": [
                                "Assertive communication states moral boundaries clearly and respectfully, avoiding passivity and aggression.",
                                "Tactic tools include clear 'I' statements, reverse pressure, and repeating the firm refusal.",
                                "Joseph in Genesis 39 demonstrated that resisting sexual pressure requires both verbal clarity and decisive physical flight.",
                                "Running from temptation is an act of spiritual courage and wisdom, not weakness."
                            ]
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Knowledge Check",
                        "content": {
                            "question": "When Potiphar's wife physically grabbed Joseph's garment to force him into sexual immorality, what was Joseph's decisive response?",
                            "options": [
                                "A) He stayed to explain why her actions were unethical",
                                "B) He became aggressive and assaulted her",
                                "C) He ran out of the house, physically removing himself from the danger",
                                "D) He gave in passively to avoid losing his administrative job"
                            ],
                            "answer": "C",
                            "explanation": "Joseph executed the 'Joseph Strategy' by immediately breaking free and fleeing out of the house, valuing moral purity before God above everything else."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Peer Support and Moral Accountability
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "4.3.6 Peer Support and Moral Accountability",
            "unit_description": "Building intentional Christian peer support networks, mutual transparency, safe study habits, and spurring one another in Hebrews 10:24-25.",
            "lesson_title": "Peer Support and Moral Accountability Networks",
            "wikimedia_asset": {
                "title": "Christian Youth Fellowship and Community Accountability",
                "caption": "Secondary school students gathering in Christian Union prayer and peer study, demonstrating mutual encouragement, accountability, and spiritual solidarity.",
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Youth_prayer_and_bible_study_fellowship.jpg/800px-Youth_prayer_and_bible_study_fellowship.jpg",
                "author": "Wikimedia Commons / Christian Ministries",
                "source": "Wikimedia Commons",
                "licensing": "CC BY-SA 4.0"
            },
            "svg_func": get_svg_lesson_6,
            "youtube_asset": {
                "title": "BibleProject: Hebrews & The Community of Faith",
                "youtube_id": "1fG6wCh55A8",
                "url": "https://www.youtube.com/watch?v=1fG6wCh55A8",
                "description": "Explores how the letter to the Hebrews exhorts believers to persevere in holiness through mutual encouragement and unshakeable community fellowship."
            },
            "pages": [
                # PAGE 1: Hook, Objectives & Real-Life Launch
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: Christian Fellowship & Solidarity",
                        "content": {
                            "title": "Visual Hook: Christian Fellowship & Solidarity",
                            "caption": "Students studying scripture together in mutual encouragement and shared dedication to academic and moral excellence.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Youth_prayer_and_bible_study_fellowship.jpg/800px-Youth_prayer_and_bible_study_fellowship.jpg",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Youth_prayer_and_bible_study_fellowship.jpg/800px-Youth_prayer_and_bible_study_fellowship.jpg",
                            "author": "Wikimedia Commons",
                            "source": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives",
                        "content": {
                            "goals": [
                                "Explain the biblical rationale for **peer accountability networks** in maintaining moral and sexual purity.",
                                "Analyze **Hebrews 10:24-25** on the duty of believers to spur one another on toward love and good deeds.",
                                "Formulate practical structures for **weekly digital and relationship check-ins** among Christian peers.",
                                "Establish protocols for **safe study and social habits** on campus and at home."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Sharing Experiences: You Become Your Circle",
                        "content": {
                            "markdown": "### The Power of Positive Peer Pressure\nWhile negative peer pressure pulls youth down into compromise, godly peer support lifts youth up into purpose. No Christian teenager is designed to fight spiritual and moral battles in isolation. By intentionally surrounding yourself with friends who revere God, accountability transforms from a burden into a powerful protective shield."
                        }
                    }
                ],
                # PAGE 2: Scripture Study: Hebrews 10 & Accountability Principles
                [
                    {
                        "type": "concept_explanation",
                        "title": "Biblical Foundation: Hebrews 10:24-25",
                        "content": {
                            "markdown": "### The Command to Spur One Another\n\n> *\"And let us consider how we may spur one another on toward love and good deeds, not giving up meeting together, as some are in the habit of doing, but encouraging one another—and all the more as you see the Day approaching.\"* (Hebrews 10:24-25)\n\n#### Core Principles:\n1. **Intentional Consideration**: Actively thinking about how to help your friend succeed in their moral and spiritual walk.\n2. **Spurring Toward Holiness**: Challenging one another to maintain high standards of speech, digital consumption, and relational honor.\n3. **Consistent Fellowship**: Gathering regularly in Christian Union, prayer cells, and Bible study groups to fortify faith."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Three Pillars of Accountability",
                        "content": {
                            "markdown": "### How True Accountability Operates\n- **Character-Based Selection**: Choosing friends based on integrity rather than superficial popularity (Proverbs 13:20: *\"Walk with the wise and become wise\"*).\n- **Mutual Transparency**: Giving a trusted brother or sister permission to ask hard questions regarding phone habits, media use, and relationship boundaries.\n- **Intercessory Prayer**: Praying for one another regularly, especially when undergoing stressful seasons or emotional temptations."
                        }
                    }
                ],
                # PAGE 3: Visual Vector Architecture & Safe Social Zones
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Visual Architecture: The Peer Accountability Shield",
                        "content": {
                            "title": "Visual Architecture: The Peer Accountability Shield",
                            "caption": "Pedagogy diagram detailing Intentional Circles, Weekly Check-Ins, and Safe Social Zones for Christian youth.",
                            "svg": get_svg_lesson_6(),
                            "svg_xml": get_svg_lesson_6()
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Establishing Safe Study & Social Habits",
                        "content": {
                            "markdown": "### Guidelines for Campus & Social Life\n- **Open Environment Rule**: Study together in open spaces like libraries, school dining halls, or family living rooms with parental presence.\n- **Zero Isolated Seclusion**: Refuse closed-door, one-on-one private sessions in empty classrooms or bedrooms with members of the opposite sex.\n- **Group Fellowship**: Travel to youth rallies, sports tournaments, and church functions in groups rather than isolated pairs."
                        }
                    }
                ],
                # PAGE 4: Practical Life Application: Weekly Check-In Toolkit
                [
                    {
                        "type": "step_process",
                        "title": "Practical Life Toolkit: The Weekly 3-Question Check-In",
                        "content": {
                            "title": "A Simple Accountability Routine with a Trusted Friend",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Question 1: The Media Audit",
                                    "description": "Have your phone habits, social media feeds, and entertainment honored God and kept your mind pure this week?"
                                },
                                {
                                    "step_number": 2,
                                    "title": "Question 2: The Relationship Audit",
                                    "description": "Have all your interactions and communications with the opposite sex maintained absolute sibling purity?"
                                },
                                {
                                    "step_number": 3,
                                    "title": "Question 3: The Honesty Check",
                                    "description": "Have you been completely truthful in all your answers today, or is there something you were tempted to hide?"
                                },
                                {
                                    "step_number": 4,
                                    "title": "Closing Prayer & Encouragement",
                                    "description": "Pray for each other by name, committing the upcoming week's decisions to the Holy Spirit."
                                }
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Kenyan Context: Christian Union (CU) on Campus",
                        "content": {
                            "markdown": "### The Vibrant Role of Christian Unions in Kenya\nIn secondary schools across Kenya, Christian Unions provide an invaluable environment where students form prayer partners and accountability cells. Active participation in CU nurtures spiritual discipline and creates a supportive community that celebrates academic diligence and moral purity."
                        }
                    }
                ],
                # PAGE 5: Video Resource & Faith Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "BibleProject: Hebrews & The Community of Faith",
                        "content": {
                            "title": "BibleProject: Hebrews & The Community of Faith",
                            "youtube_id": "1fG6wCh55A8",
                            "url": "https://www.youtube.com/watch?v=1fG6wCh55A8",
                            "description": "Explores how mutual exhortation and community endurance enable believers to overcome spiritual discouragement and temptation."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Spiritual Reflection & Values",
                        "content": {
                            "markdown": "### Iron Sharpens Iron\n- **Core Value:** *Accountability & Fellowship* — Valuing loving correction and spiritual partnership over private pride.\n- **Reflective Commitment:** Identify one mature, trusted Christian friend this week and agree to pray and hold each other accountable.\n- **Key Verse:** *\"As iron sharpens iron, so one person sharpens another.\"* (Proverbs 27:17)"
                        }
                    }
                ],
                # PAGE 6: Summary & Knowledge Check
                [
                    {
                        "type": "key_takeaway",
                        "title": "Summary & Core Principles",
                        "content": {
                            "title": "Core Takeaways: Peer Accountability",
                            "takeaways": [
                                "Godly peers provide a protective buffer against negative cultural and social pressures.",
                                "Hebrews 10:24-25 commands believers to spur one another on toward love, good deeds, and regular fellowship.",
                                "Effective accountability requires mutual transparency, weekly digital and relational check-ins, and shared prayer.",
                                "Safe social habits include studying in open spaces and avoiding isolated seclusion with the opposite sex."
                            ]
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Knowledge Check",
                        "content": {
                            "question": "According to Hebrews 10:24-25, what is a primary duty of believers within the Christian fellowship community?",
                            "options": [
                                "A) To isolate themselves from everyone to avoid all social interaction",
                                "B) To spur one another on toward love and good deeds, encouraging each other regularly",
                                "C) To judge and publicly condemn peers who struggle with weaknesses",
                                "D) To compete for leadership positions and social status in church"
                            ],
                            "answer": "B",
                            "explanation": "Hebrews 10:24-25 specifically instructs believers to consider how to spur one another on toward love and good deeds while meeting together and offering mutual encouragement."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Setting Boundaries for Bodily Holiness
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "4.3.7 Setting Boundaries for Bodily Holiness",
            "unit_description": "Theology of the body as God's Holy Temple in 1 Corinthians 6:18-20, practical planning across mental, visual, physical, and digital boundary zones.",
            "lesson_title": "Setting Boundaries for Bodily Holiness",
            "wikimedia_asset": {
                "title": "Temple Architecture and Sacred Holiness",
                "caption": "A majestic cathedral sanctuary illustrating the solemnity, sacredness, and consecrated purity of God's dwelling place.",
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/All_Saints_Cathedral_Nairobi_interior.jpg/800px-All_Saints_Cathedral_Nairobi_interior.jpg",
                "author": "Wikimedia Commons / Architectural Heritage",
                "source": "Wikimedia Commons",
                "licensing": "CC BY-SA 4.0"
            },
            "svg_func": get_svg_lesson_7,
            "youtube_asset": {
                "title": "BibleProject: 1 Corinthians & The Holy Temple",
                "youtube_id": "yiSjX3XFH0c",
                "url": "https://www.youtube.com/watch?v=yiSjX3XFH0c",
                "description": "Explores Paul's letter to the Corinthians on sexual ethics, bodily resurrection, and why the human body belongs to Christ."
            },
            "pages": [
                # PAGE 1: Hook, Objectives & Real-Life Launch
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: The Sacred Temple Sanctuary",
                        "content": {
                            "title": "Visual Hook: The Sacred Temple Sanctuary",
                            "caption": "The interior of a sacred cathedral sanctuary, symbolizing how every believer's physical body is consecrated as the holy temple of God.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/All_Saints_Cathedral_Nairobi_interior.jpg/800px-All_Saints_Cathedral_Nairobi_interior.jpg",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/All_Saints_Cathedral_Nairobi_interior.jpg/800px-All_Saints_Cathedral_Nairobi_interior.jpg",
                            "author": "Wikimedia Commons",
                            "source": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives",
                        "content": {
                            "goals": [
                                "Analyze the theological foundation of **1 Corinthians 6:18-20** (the body as the temple of the Holy Spirit bought with a price).",
                                "Construct concrete personal boundaries across the **Four Zones: Mental, Visual/Media, Physical/Touch, and Digital/Chat**.",
                                "Examine the moral, psychological, and legal consequences of **sexting and cyber-exploitation**.",
                                "Formulate a proactive, written **Personal Boundary Plan** for daily living."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Sharing Experiences: How We Treat Sacred Things",
                        "content": {
                            "markdown": "### The Sacredness of What Belongs to God\nIf you were given stewardship of a priceless, sacred artifact, you would treat it with extreme care and guard it from contamination. In Christian theology, your physical body is not your private property to abuse or exploit—it is the living, holy sanctuary of the Holy Spirit."
                        }
                    }
                ],
                # PAGE 2: Scripture Deep Dive: 1 Corinthians 6:18-20
                [
                    {
                        "type": "concept_explanation",
                        "title": "Biblical Foundation: 1 Corinthians 6:18-20",
                        "content": {
                            "markdown": "### Your Body: The Temple of the Holy Spirit\n\n> *\"Flee from sexual immorality. All other sins a person commits are outside the body, but he who sins sexually sins against his own body. Do you not know that your bodies are temples of the Holy Spirit, who is in you, whom you have received from God? You are not your own; you were bought at a price. Therefore honor God with your bodies.\"* (1 Corinthians 6:18-20)\n\n#### Key Theological Insights:\n1. **The Command to Flee**: Paul does not tell believers to negotiate or debate with sexual immorality; the divine command is to *flee* immediately.\n2. **Sinning Against One's Own Body**: Sexual sin damages the internal soul, emotional wholeness, and spiritual union with God.\n3. **Bought at a Price**: Believers belong to Christ through His precious sacrifice on the cross. Therefore, our bodies must reflect divine honor."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Four Boundary Zones Explained",
                        "content": {
                            "markdown": "### The Four Protective Zones of Holiness\n1. **Mental Boundary**: Taking every thought captive to obey Christ (2 Corinthians 10:5); guarding against lingering lustful fantasies.\n2. **Visual Boundary**: Making a covenant with your eyes (Job 31:1); filtering movies, music videos, and unfollowing compromising social media accounts.\n3. **Physical Boundary**: Establishing firm limits beforehand (no intimate touching or kissing reserved for marriage); avoiding isolated private locations.\n4. **Digital Boundary**: Zero tolerance for sending or receiving sexually explicit messages, memes, or photos (sexting)."
                        }
                    }
                ],
                # PAGE 3: Visual Vector Architecture & Digital Boundaries
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Visual Architecture: The 4 Boundary Zones for Bodily Holiness",
                        "content": {
                            "title": "Visual Architecture: The 4 Boundary Zones for Bodily Holiness",
                            "caption": "Quadrant diagram mapping Mental, Visual, Physical, and Digital boundary zones anchored in 1 Corinthians 6:19-20.",
                            "svg": get_svg_lesson_7(),
                            "svg_xml": get_svg_lesson_7()
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Digital Safety & The Dangers of Sexting",
                        "content": {
                            "markdown": "### The Perils of Cyber-Immorality and Sexting\n- **Permanence of Digital Footprints**: Images sent in secret are frequently screenshotted, leaked, forwarded, or used for cyber-blackmail.\n- **Legal Repercussions in Kenya**: The Computer Misuse and Cybercrimes Act of 2018 prescribes severe criminal penalties for distributing non-consensual intimate images or child exploitation material.\n- **Spiritual & Emotional Damage**: Sexting destroys personal self-worth, creates paralyzing shame, and breaches Christian integrity (Ephesians 5:3)."
                        }
                    }
                ],
                # PAGE 4: Practical Life Toolkit: Drafting Your Boundary Plan
                [
                    {
                        "type": "step_process",
                        "title": "Practical Life Toolkit: Personal Boundary Action Plan",
                        "content": {
                            "title": "Drafting Your Personal Boundary Plan",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Define Physical Limits in Advance",
                                    "description": "Decide today what physical touch is off-limits so you do not have to make moral decisions under emotional heat."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Clean Up Your Digital Ecosystem",
                                    "description": "Delete compromising apps, exit inappropriate group chats, and unfollow provocative social media influencers."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Establish Phone Curfews",
                                    "description": "Avoid late-night texting in bed behind closed doors; charge your phone in a family area."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Share Your Plan with a Mentor",
                                    "description": "Give a copy of your boundary goals to a trusted parent, teacher, or youth pastor for accountability."
                                }
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Real-World Kenyan Context: Social Media Integrity",
                        "content": {
                            "markdown": "### Cultivating Christian Cyber-Witness\nIn an era where TikTok, Instagram, and WhatsApp stories drive teen culture, Christian students stand out by producing edifying, joyful, and clean content that points their peers to Christ rather than catering to vanity or sensuality."
                        }
                    }
                ],
                # PAGE 5: Video Resource & Faith Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "BibleProject: 1 Corinthians & The Holy Temple",
                        "content": {
                            "title": "BibleProject: 1 Corinthians & The Holy Temple",
                            "youtube_id": "yiSjX3XFH0c",
                            "url": "https://www.youtube.com/watch?v=yiSjX3XFH0c",
                            "description": "Explains how the resurrection of Jesus gives cosmic dignity to the human body and calls believers to bodily holiness."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Spiritual Reflection & Ethical Values",
                        "content": {
                            "markdown": "### Honoring God with Your Temple\n- **Core Value:** *Holiness & Self-Control* — Consecrating your mind, eyes, hands, and digital life to honor Jesus Christ.\n- **Reflective Commitment:** Write out one digital boundary and one physical boundary you commit to maintaining throughout this school year.\n- **Key Verse:** *\"You are not your own; you were bought at a price. Therefore honor God with your bodies.\"* (1 Corinthians 6:19b-20)"
                        }
                    }
                ],
                # PAGE 6: Summary & Knowledge Check
                [
                    {
                        "type": "key_takeaway",
                        "title": "Summary & Core Principles",
                        "content": {
                            "title": "Core Takeaways: Bodily Holiness",
                            "takeaways": [
                                "The believer's body is the temple of the Holy Spirit, purchased by the precious sacrifice of Jesus Christ (1 Cor 6:18-20).",
                                "Holiness requires intentional boundaries across four zones: Mental, Visual/Media, Physical, and Digital.",
                                "Sexting and digital immorality cause severe psychological, legal, and spiritual destruction.",
                                "A proactive Personal Boundary Plan protects youth integrity and nurtures lifelong peace."
                            ]
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Knowledge Check",
                        "content": {
                            "question": "According to 1 Corinthians 6:18-20, why are Christians commanded to honor God with their bodies and flee sexual immorality?",
                            "options": [
                                "A) Because our physical bodies are temporary and unimportant to God",
                                "B) Because the body is the temple of the Holy Spirit and was bought at a price by Christ",
                                "C) Because society demands that we follow cultural traditions without question",
                                "D) Because physical exercise is the only way to attain spiritual salvation"
                            ],
                            "answer": "B",
                            "explanation": "Paul reveals that our bodies are living temples of the Holy Spirit and were bought at a price (Christ's sacrifice); therefore, we must glorify God in our bodies."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Youth Support Networks & Help-Seeking
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "4.3.8 Youth Support Networks & Help-Seeking",
            "unit_description": "Breaking silence on abuse and harassment, establishing multi-tiered help-seeking pathways (School G&C, Parents, Pastoral Care, Childline 116, GBV 1195).",
            "lesson_title": "Youth Support Networks & Help-Seeking Ecosystem",
            "wikimedia_asset": {
                "title": "Guidance, Counseling, and Student Support in Kenya",
                "caption": "A caring Kenyan school guidance counselor listening to and advising secondary school learners in a safe, confidential environment.",
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/School_counselor_mentoring_students_Kenya.jpg/800px-School_counselor_mentoring_students_Kenya.jpg",
                "author": "Wikimedia Commons / Education Support",
                "source": "Wikimedia Commons",
                "licensing": "CC BY-SA 4.0"
            },
            "svg_func": get_svg_lesson_8,
            "youtube_asset": {
                "title": "BibleProject: Justice, Protection & Compassion",
                "youtube_id": "A14THPoc4-4",
                "url": "https://www.youtube.com/watch?v=A14THPoc4-4",
                "description": "Explores the biblical vision of restorative justice, God's deep heart for the vulnerable, and the calling to protect youth in distress."
            },
            "pages": [
                # PAGE 1: Hook, Objectives & Real-Life Launch
                [
                    {
                        "type": "suggested_image",
                        "title": "Visual Hook: School Guidance & Mentorship",
                        "content": {
                            "title": "Visual Hook: School Guidance & Mentorship",
                            "caption": "Professional school guidance and counseling educators providing confidential advice, empathy, and crisis support to learners.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/School_counselor_mentoring_students_Kenya.jpg/800px-School_counselor_mentoring_students_Kenya.jpg",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/School_counselor_mentoring_students_Kenya.jpg/800px-School_counselor_mentoring_students_Kenya.jpg",
                            "author": "Wikimedia Commons",
                            "source": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives",
                        "content": {
                            "goals": [
                                "Recognize that seeking help during emotional distress, harassment, or moral struggle is a mark of **wisdom and strength**.",
                                "Analyze the Four Tiers of the youth support ecosystem: **School Counselors, Parents/Guardians, Pastoral Leaders, and National Emergency Lines**.",
                                "Memorize essential emergency hotlines in Kenya: **Childline 116** and **National GBV Hotline 1195**.",
                                "Formulate an emergency help-seeking contact protocol for immediate assistance."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Sharing Experiences: Breaking the Silence",
                        "content": {
                            "markdown": "### You Never Have to Walk Alone\nIf you or a peer have experienced sexual harassment, online bullying, intense emotional peer pressure, or past mistakes, carrying the burden in secret produces shame and fear. Seeking help is an act of courage that invites healing, safety, and restorative justice."
                        }
                    }
                ],
                # PAGE 2: The Four-Tier Help-Seeking Ecosystem
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Four Support Tiers Explained",
                        "content": {
                            "markdown": "### Multi-Tiered Help-Seeking Channels in Kenya\n\n1. **Tier 1: School Guidance & Counseling (G&C)**:\n   - Every secondary school has trained G&C teachers dedicated to confidential listening, conflict resolution, and academic/emotional guidance without condemnation.\n\n2. **Tier 2: Parents & Primary Guardians**:\n   - God has placed parents as primary protectors. Open dialogue about peer pressures or harassment enables families to provide immediate legal, emotional, and physical safety.\n\n3. **Tier 3: Pastoral Care & Church Youth Leaders**:\n   - Pastors, priests, and Christian Union patrons offer spiritual counsel, prayer, forgiveness, and scriptural restoration for those experiencing guilt or confusion.\n\n4. **Tier 4: National Emergency & Legal Hotlines**:\n   - Specialized 24/7 toll-free hotlines for crisis rescue, legal reporting, and professional counseling."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Essential Emergency Hotlines in Kenya",
                        "content": {
                            "markdown": "### Kenyan National Emergency Lines\n\n| Service / Agency | Hotline Number | Key Role & Availability |\n| :--- | :--- | :--- |\n| **Childline Kenya** | **116** | Toll-free, 24/7 national helpline for children and youth facing abuse, crisis, or neglect. |\n| **National GBV Hotline** | **1195** | Toll-free, 24/7 support line for gender-based violence, rescue, and medical referrals. |\n| **Kenya Police Emergency** | **999 / 112 / 911** | Immediate physical emergency, assault, and crime reporting. |\n| **Mental Health Helpline** | **1199** | Psychological crisis and mental health emergency counseling. |"
                        }
                    }
                ],
                # PAGE 3: Visual Vector Architecture & Breaking Victim-Blaming
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Visual Architecture: Youth Support & Help-Seeking Ecosystem",
                        "content": {
                            "title": "Visual Architecture: Youth Support & Help-Seeking Ecosystem",
                            "caption": "Comprehensive roadmap illustrating the 4-level support ecosystem in Kenya, featuring Childline 116 and GBV 1195.",
                            "svg": get_svg_lesson_8(),
                            "svg_xml": get_svg_lesson_8()
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Overcoming Shame and Victim-Blaming",
                        "content": {
                            "markdown": "### God's Heart of Grace and Restoration\n\n> *\"The Lord is close to the brokenhearted and saves those who are crushed in spirit.\"* (Psalm 34:18)\n\nMany victims of harassment or abuse suffer in silence because of fears of being blamed or ostracized. Christian communities must be sanctuaries of grace, unconditional safety, and fierce advocacy for truth and justice."
                        }
                    }
                ],
                # PAGE 4: Practical Life Application: Help-Seeking Protocol
                [
                    {
                        "type": "step_process",
                        "title": "Practical Life Toolkit: The 4-Step Crisis Protocol",
                        "content": {
                            "title": "What to Do When in Crisis or Facing Harassment",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Step 1: Secure Immediate Safety",
                                    "description": "Remove yourself from physical proximity to the abuser or hostile environment."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Step 2: Preserve Evidence",
                                    "description": "Do not delete harassing messages, screenshots, or call logs; preserve them for school authorities and law enforcement."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Step 3: Tell a Trusted Adult",
                                    "description": "Speak immediately to your school counselor, parent, or trusted teacher."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Step 4: Call Childline Kenya (116)",
                                    "description": "If local adults are unresponsive or if you need external professional intervention, dial 116 toll-free."
                                }
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Real-World Application: Personal Safety Contact Card",
                        "content": {
                            "markdown": "### Activity: Create Your Emergency Safety Card\nIn your Christian Religious Education exercise book, write out your personal safety directory:\n1. The name and office location of your school's Guidance & Counseling teacher.\n2. The direct phone contact of your parents or guardians.\n3. The toll-free hotline: **Childline Kenya (116)** and **GBV Line (1195)**."
                        }
                    }
                ],
                # PAGE 5: Video Resource & Faith Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "BibleProject: Justice, Protection & Compassion",
                        "content": {
                            "title": "BibleProject: Justice, Protection & Compassion",
                            "youtube_id": "A14THPoc4-4",
                            "url": "https://www.youtube.com/watch?v=A14THPoc4-4",
                            "description": "Explores how God's righteousness demands the active protection of the vulnerable and compassionate support for those in distress."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Spiritual Reflection & Values",
                        "content": {
                            "markdown": "### Finding Refuge in God and Community\n- **Core Value:** *Compassion, Courage & Truth* — Being an advocate for yourself and your peers when facing injustice or harassment.\n- **Reflective Prayer:** Lord, grant me the courage to speak truth, seek wisdom, and be a source of safety and compassion for those around me.\n- **Key Verse:** *\"God is our refuge and strength, an ever-present help in trouble.\"* (Psalm 46:1)"
                        }
                    }
                ],
                # PAGE 6: Summary & Topic Review Quiz
                [
                    {
                        "type": "key_takeaway",
                        "title": "Summary & Core Principles",
                        "content": {
                            "title": "Core Takeaways: Youth Support Networks",
                            "takeaways": [
                                "Seeking help is a sign of wisdom, emotional strength, and self-worth.",
                                "The youth support ecosystem includes School Counselors, Parents, Pastoral Ministers, and Emergency Hotlines.",
                                "Childline Kenya (116) is a free, 24/7 confidential helpline dedicated to youth protection.",
                                "National GBV Hotline (1195) provides immediate intervention for gender-based harassment and violence."
                            ]
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Knowledge Check",
                        "content": {
                            "question": "Which toll-free telephone hotline is available 24/7 across Kenya for children and youth seeking confidential counseling and crisis intervention?",
                            "options": [
                                "A) 999",
                                "B) 116 (Childline Kenya)",
                                "C) 1195",
                                "D) 112"
                            ],
                            "answer": "B",
                            "explanation": "Childline Kenya is reached toll-free at 116 from any network in Kenya, offering 24/7 confidential counseling and emergency reporting."
                        }
                    }
                ]
            ]
        }
    ]


# ─── INGESTION CONTROLLER ──────────────────────────────────────────────────

def ingest_grade10_topic_4_3(replace=True):
    print("=" * 80)
    print("STARTING VLEARN INGESTION ENGINE: Grade 10 CRE Topic 4.3 (Human Sexuality)")
    print("=" * 80)

    # 1. Resolve Curriculum, Grade, Subject
    curriculum = Curriculum.objects.get(name="CBC")
    grade = Grade.objects.get(curriculum=curriculum, name="Grade 10")
    subject = Subject.objects.get(id=46, grade=grade)

    print(f"Curriculum: {curriculum.name} (ID: {curriculum.id})")
    print(f"Grade:      {grade.name} (ID: {grade.id})")
    print(f"Subject:    {subject.name} (ID: {subject.id})")

    # 2. Resolve Topic 4.3 (Order 21)
    topic_name = "Sub-Strand 4.3: Human Sexuality"
    topic_desc = "Holistic Christian understanding of human sexuality across biological, psychological, emotional, and social dimensions; male-female relationships, courtship, assertive resistance to peer pressure, bodily holiness, and youth support networks."

    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=21,
        defaults={"name": topic_name, "description": topic_desc}
    )
    if not t_created:
        topic.name = topic_name
        topic.description = topic_desc
        topic.save()
    print(f"Topic:      {topic.name} (ID: {topic.id}, Order: {topic.order})")

    # 3. Clean existing LearningUnits/Lessons if replace=True
    if replace:
        print("Purging existing LearningUnits and Lessons for Topic 4.3...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic_4_3_curriculum()
    total_units = 0
    total_lessons = 0
    total_pages = 0
    total_blocks = 0
    total_assets = 0

    with transaction.atomic():
        for item in curriculum_data:
            u_order = item["unit_order"]
            u_name = item["unit_name"]
            u_desc = item["unit_description"]
            l_title = item["lesson_title"]
            wiki_asset_def = item["wikimedia_asset"]
            svg_func = item["svg_func"]
            yt_asset_def = item["youtube_asset"]
            pages = item["pages"]

            # Create LearningUnit
            unit, _ = LearningUnit.objects.get_or_create(
                topic=topic,
                order=u_order,
                defaults={"name": u_name, "description": u_desc}
            )
            unit.name = u_name
            unit.description = u_desc
            unit.save()
            total_units += 1

            # Create Lesson (Published, Version 1)
            lesson, _ = Lesson.objects.get_or_create(
                topic=topic,
                learning_unit=unit,
                defaults={
                    "title": l_title,
                    "status": "published",
                    "version": 1,
                    "immutable_metadata": {
                        "author": "VLearn Senior Curriculum Ingestion Agent",
                        "grade": "Grade 10",
                        "subject": "CRE",
                        "topic_order": 21,
                        "unit_order": u_order,
                        "strand": "Christian Living Today",
                        "sub_strand": "4.3 Human Sexuality"
                    }
                }
            )
            lesson.title = l_title
            lesson.status = "published"
            lesson.version = 1
            lesson.immutable_metadata = {
                "author": "VLearn Senior Curriculum Ingestion Agent",
                "grade": "Grade 10",
                "subject": "CRE",
                "topic_order": 21,
                "unit_order": u_order,
                "strand": "Christian Living Today",
                "sub_strand": "4.3 Human Sexuality"
            }
            lesson.save()
            lesson.blocks.all().delete()
            lesson.assets.all().delete()
            total_lessons += 1

            # Create Lesson Assets for Image, Diagram, and YouTube
            # 1. Wikimedia Image Asset
            img_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type='image',
                source_type='external',
                storage_type='url',
                status='attached',
                title=clean_text(wiki_asset_def["title"]),
                description=clean_text(wiki_asset_def["caption"]),
                url=wiki_asset_def["url"],
                metadata={
                    "author": wiki_asset_def.get("author", "Wikimedia Commons"),
                    "licensing": wiki_asset_def.get("licensing", "CC BY-SA 4.0"),
                    "source": wiki_asset_def.get("source", "Wikimedia Commons"),
                    "resolved_image_url": wiki_asset_def["url"],
                    "unit_order": u_order
                }
            )
            total_assets += 1

            # 2. Vector SVG Diagram Asset
            svg_content = svg_func()
            diag_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type='diagram',
                source_type='ai_generated',
                storage_type='url',
                status='attached',
                title=f"Diagram: {l_title}",
                description=f"Pedagogical Vector Diagram for {l_title}",
                url=f"https://vlearn.africa/assets/diagrams/cre/topic_4_3_lesson_{u_order}.svg",
                metadata={
                    "svg_xml": svg_content,
                    "viewBox": "0 0 800 450",
                    "unit_order": u_order
                }
            )
            total_assets += 1

            # 3. YouTube Video Asset
            yt_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type='youtube',
                source_type='external',
                storage_type='url',
                status='attached',
                title=clean_text(yt_asset_def["title"]),
                description=clean_text(yt_asset_def["description"]),
                url=yt_asset_def["url"],
                metadata={
                    "youtube_id": yt_asset_def["youtube_id"],
                    "unit_order": u_order
                }
            )
            total_assets += 1

            # Ingest Pages and LessonBlocks
            block_order_counter = 1
            for page_idx, page_blocks in enumerate(pages, start=1):
                total_pages += 1
                for comp_idx, block_def in enumerate(page_blocks, start=1):
                    b_type = block_def["type"]
                    b_title = clean_text(block_def.get("title", ""))
                    b_content = clean_dict(block_def.get("content", {}))

                    # Re-inject svg string if it's a diagram block
                    if b_type == "suggested_diagram":
                        b_content["svg"] = svg_content
                        b_content["svg_xml"] = svg_content

                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=f"g10_cre_t4_3_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_order_counter * 10,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 21, "unit_order": u_order, "page": page_idx}
                    )
                    block_order_counter += 1
                    total_blocks += 1

                    # Link Assets to specific blocks
                    if b_type == "suggested_image":
                        img_asset.blocks.add(block)
                    elif b_type == "suggested_diagram":
                        diag_asset.blocks.add(block)
                    elif b_type == "suggested_video":
                        yt_asset.blocks.add(block)

            print(f"  Ingested Unit {u_order}: {u_name} -> Lesson '{l_title}' ({len(pages)} Pages, {block_order_counter - 1} Blocks, 3 Assets)")

    print("=" * 80)
    print("INGESTION AUDIT SUMMARY FOR TOPIC 4.3:")
    print(f"  Topic:            {topic.name} (Order: {topic.order})")
    print(f"  Learning Units:   {total_units}")
    print(f"  Published Lessons:{total_lessons}")
    print(f"  Pages Ingested:   {total_pages}")
    print(f"  Lesson Blocks:    {total_blocks}")
    print(f"  Lesson Assets:    {total_assets}")
    print("=" * 80)
    return {
        "units": total_units,
        "lessons": total_lessons,
        "pages": total_pages,
        "blocks": total_blocks,
        "assets": total_assets
    }


if __name__ == "__main__":
    replace_flag = "--no-replace" not in sys.argv
    ingest_grade10_topic_4_3(replace=replace_flag)
