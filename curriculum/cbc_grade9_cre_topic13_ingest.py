"""
VLearn CBC Grade 9 CRE — Topic 13: Courtship and Marriage
Production-Ready Ingestion & Visual Enrichment Engine

Curriculum: CBC
Grade: Grade 9 (ID: 18)
Subject: CRE (ID: 50)
Topic: Topic 13: Courtship and Marriage (Order: 13)

6 Discrete Units / Published Lessons:
  1. Lesson 1: Understanding Courtship and Marriage (Genesis 2:18-24, Proverbs 18:22, Genesis 1:27-28, Matthew 19:4-6)
  2. Lesson 2: Traditional African Understanding of Courtship and Marriage
  3. Lesson 3: Christian Teachings on Courtship and Marriage (Ephesians 5:21-33, 1 Corinthians 7:1-7, Hebrews 13:4, 2 Corinthians 6:14)
  4. Lesson 4: Early Marriage: Causes and Consequences (Article 53, Children Act 2022, 1 Timothy 4:12)
  5. Lesson 5: Factors of a Stable, Healthy Marriage and the Alternative of Celibacy (Matthew 19:10-12, 1 Corinthians 7:8, 32-35)
  6. Lesson 6: The Challenge of Divorce (Matthew 19:3-9, Malachi 2:14-16)

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
    text = re.sub(r'\[(VISUAL|BIBLE PASSAGE|BIBLE REFERENCE|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|REAL WORLD APPLICATION|BIBLICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|REFLECTION|BIBLE VERSE)[^\]]*\]', '', text, flags=re.IGNORECASE)
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
    <linearGradient id="goldGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg1)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE FOUR PILLARS OF CHRISTIAN MARRIAGE</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Genesis 2:18-24 &amp; Matthew 19:4-6 — Foundational Pillars of a Holy Covenant</text>

  <!-- Temple Pediment Roof -->
  <polygon points="400,90 100,140 700,140" fill="url(#goldGrad1)" stroke="#fbbf24" stroke-width="1.5"/>
  <text x="400" y="125" fill="#0f172a" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">CHRISTIAN MARRIAGE: SACRED &amp; PERMANENT UNION</text>

  <!-- Architrave Beam -->
  <rect x="90" y="140" width="620" height="20" rx="4" fill="#334155"/>
  <text x="400" y="154" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">"WHAT GOD HAS JOINED TOGETHER, LET NO MAN SEPARATE"</text>

  <!-- 4 Supporting Pillars -->
  <!-- Pillar 1: Sacred Covenant -->
  <g transform="translate(100, 168)">
    <rect width="130" height="190" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="130" height="30" rx="6" fill="#0284c7"/>
    <text x="65" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. COVENANT</text>
    <text x="10" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Lifelong Vow</text>
    <text x="10" y="73" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Irrevocable oath</text>
    <text x="10" y="87" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">before God &amp; church.</text>
    <text x="10" y="115" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Unconditional</text>
    <text x="10" y="133" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Transcends mere</text>
    <text x="10" y="147" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">secular contracts.</text>
  </g>

  <!-- Pillar 2: Companionship -->
  <g transform="translate(250, 168)">
    <rect width="130" height="190" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="130" height="30" rx="6" fill="#059669"/>
    <text x="65" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. COMPANION</text>
    <text x="10" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Mutual Support</text>
    <text x="10" y="73" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Helper suitable;</text>
    <text x="10" y="87" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">equal partnership.</text>
    <text x="10" y="115" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Deep Intimacy</text>
    <text x="10" y="133" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Emotional, spiritual</text>
    <text x="10" y="147" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">&amp; physical oneness.</text>
  </g>

  <!-- Pillar 3: Procreation -->
  <g transform="translate(400, 168)">
    <rect width="130" height="190" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="130" height="30" rx="6" fill="#d97706"/>
    <text x="65" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. PROCREATION</text>
    <text x="10" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Fruitfulness</text>
    <text x="10" y="73" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Bearing children</text>
    <text x="10" y="87" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">to continue humanity.</text>
    <text x="10" y="115" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Godly Heritage</text>
    <text x="10" y="133" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Nurturing youth in</text>
    <text x="10" y="147" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">moral discipline.</text>
  </g>

  <!-- Pillar 4: Mutual Love & Purity -->
  <g transform="translate(550, 168)">
    <rect width="130" height="190" rx="6" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="130" height="30" rx="6" fill="#db2777"/>
    <text x="65" y="20" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">4. AGAPE LOVE</text>
    <text x="10" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Sacrificial Care</text>
    <text x="10" y="73" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Unselfish devotion</text>
    <text x="10" y="87" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">and honor daily.</text>
    <text x="10" y="115" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Marital Purity</text>
    <text x="10" y="133" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Faithfulness in</text>
    <text x="10" y="147" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">mind and body.</text>
  </g>

  <!-- Foundation Base -->
  <rect x="80" y="365" width="640" height="24" rx="4" fill="#334155"/>
  <text x="400" y="381" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">FOUNDATION: FAITH IN GOD &amp; EMOTIONAL/SPIRITUAL MATURITY IN COURTSHIP</text>
</svg>"""


def get_svg_lesson_2():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="terracotta" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ea580c"/>
      <stop offset="100%" stop-color="#c2410c"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bg2)" rx="14"/>
  <rect x="15" y="15" width="770" height="420" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="6 4" rx="10"/>

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">FIVE CORE FUNCTIONS OF DOWRY IN TRADITIONAL AFRICAN SOCIETY</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Bride Wealth as a Communal Seal of Friendship, Appreciation, and Marital Stability</text>

  <!-- Central Hub -->
  <circle cx="400" cy="225" r="58" fill="url(#terracotta)" stroke="#fb923c" stroke-width="2"/>
  <text x="400" y="218" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">DOWRY / BRIDE</text>
  <text x="400" y="234" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">WEALTH</text>
  <text x="400" y="249" fill="#fde047" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">(Token of Honor)</text>

  <!-- 5 Surrounding Radial Function Nodes -->
  <!-- Node 1: Token of Appreciation -->
  <line x1="400" y1="167" x2="400" y2="120" stroke="#f97316" stroke-width="2"/>
  <g transform="translate(280, 80)">
    <rect width="240" height="42" rx="8" fill="#1e293b" stroke="#f97316" stroke-width="1.5"/>
    <text x="120" y="26" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">1. Token of Appreciation</text>
  </g>

  <!-- Node 2: Sealing Marriage Covenant -->
  <line x1="448" y1="195" x2="570" y2="140" stroke="#38bdf8" stroke-width="2"/>
  <g transform="translate(550, 120)">
    <rect width="220" height="42" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="110" y="26" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">2. Seal of Covenant</text>
  </g>

  <!-- Node 3: Clan Partnership & Friendship -->
  <line x1="445" y1="260" x2="560" y2="305" stroke="#34d399" stroke-width="2"/>
  <g transform="translate(540, 285)">
    <rect width="230" height="42" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="115" y="26" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">3. Clan Solidarity &amp; Unity</text>
  </g>

  <!-- Node 4: Marital Peace & Stability -->
  <line x1="355" y1="260" x2="240" y2="305" stroke="#fbbf24" stroke-width="2"/>
  <g transform="translate(30, 285)">
    <rect width="230" height="42" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="115" y="26" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">4. Marital Peace &amp; Stability</text>
  </g>

  <!-- Node 5: Compensation for Clan Labor -->
  <line x1="352" y1="195" x2="230" y2="140" stroke="#a855f7" stroke-width="2"/>
  <g transform="translate(30, 120)">
    <rect width="220" height="42" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <text x="110" y="26" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">5. Compensation for Labor</text>
  </g>

  <rect x="150" y="375" width="500" height="34" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="396" fill="#fed7aa" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">NOT A COMMERCIAL SALE: A SYMBOL OF REVERENCE, ALLIANCE, AND MUTUAL BLESSING</text>
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

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE YOKE METAPHOR &amp; CHRIST-CENTERED MARRIAGE</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Ephesians 5:21-33 &amp; 2 Corinthians 6:14 — Spiritual Alignment and Mutual Submission</text>

  <!-- Left: Unequally Yoked -->
  <g transform="translate(40, 95)">
    <rect width="335" height="265" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="335" height="34" rx="10" fill="#dc2626"/>
    <text x="167" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">UNEQUALLY YOKED (FRICTION &amp; PAIN)</text>
    <text x="15" y="62" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Divergent Beliefs &amp; Values:</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Believer pulling toward God, unbeliever pulling away.</text>
    <text x="15" y="108" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Spiritual Isolation &amp; Conflict:</text>
    <text x="15" y="124" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Inability to pray or raise children with united faith.</text>
    <text x="15" y="154" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Constant Moral Friction:</text>
    <text x="15" y="170" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Clashing worldviews on integrity, finances, and ethics.</text>
    <rect x="15" y="200" width="305" height="45" rx="6" fill="#0f172a"/>
    <text x="167" y="222" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">❌ "What fellowship can light have with darkness?"</text>
    <text x="167" y="236" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">(2 Corinthians 6:14)</text>
  </g>

  <!-- Right: Equally Yoked in Christ -->
  <g transform="translate(425, 95)">
    <rect width="335" height="265" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="335" height="34" rx="10" fill="#059669"/>
    <text x="167" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">EQUALLY YOKED IN CHRIST (UNITY &amp; PEACE)</text>
    <text x="15" y="62" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Shared Spiritual Foundation:</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">United devotion to Jesus Christ and biblical truth.</text>
    <text x="15" y="108" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Sacrificial Love (Husband):</text>
    <text x="15" y="124" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Loving as Christ loved the Church and gave Himself.</text>
    <text x="15" y="154" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Respectful Submission (Wife):</text>
    <text x="15" y="170" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Honoring her husband in the fear of the Lord.</text>
    <rect x="15" y="200" width="305" height="45" rx="6" fill="#0f172a"/>
    <text x="167" y="222" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">✓ "Submit to one another out of reverence for Christ"</text>
    <text x="167" y="236" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">(Ephesians 5:21)</text>
  </g>

  <rect x="160" y="375" width="480" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="396" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">MARRIAGE REFLECTS THE MYSTERY OF CHRIST AND THE CHURCH</text>
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

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">THE VICIOUS CYCLE OF EARLY MARRIAGE VS PATHWAY OF EMPOWERMENT</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Article 53 (Constitution of Kenya), Children Act 2022 &amp; 1 Timothy 4:12</text>

  <!-- Top: The Trap of Child Marriage -->
  <g transform="translate(40, 90)">
    <rect width="720" height="125" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="360" y="24" fill="#f87171" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">THE DESTRUCTIVE TRAP OF EARLY MARRIAGE</text>
    
    <!-- Step 1 -->
    <rect x="15" y="38" width="125" height="65" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="77" y="62" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Poverty / Custom</text>
    <text x="77" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Dowry pressure</text>

    <text x="150" y="75" fill="#ef4444" font-family="system-ui, sans-serif" font-size="16" font-weight="700">→</text>

    <!-- Step 2 -->
    <rect x="165" y="38" width="125" height="65" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="227" y="62" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">School Dropout</text>
    <text x="227" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Loss of education</text>

    <text x="300" y="75" fill="#ef4444" font-family="system-ui, sans-serif" font-size="16" font-weight="700">→</text>

    <!-- Step 3 -->
    <rect x="315" y="38" width="125" height="65" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="377" y="62" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Child Marriage</text>
    <text x="377" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Under age 18 union</text>

    <text x="450" y="75" fill="#ef4444" font-family="system-ui, sans-serif" font-size="16" font-weight="700">→</text>

    <!-- Step 4 -->
    <rect x="465" y="38" width="120" height="65" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="525" y="62" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Health Crises</text>
    <text x="525" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Maternal risks</text>

    <text x="595" y="75" fill="#ef4444" font-family="system-ui, sans-serif" font-size="16" font-weight="700">→</text>

    <!-- Step 5 -->
    <rect x="610" y="38" width="95" height="65" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="657" y="62" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Lifelong</text>
    <text x="657" y="78" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Poverty</text>
  </g>

  <!-- Bottom: The Pathway of Youth Empowerment -->
  <g transform="translate(40, 235)">
    <rect width="720" height="125" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="360" y="24" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">THE EMPOWERMENT PATHWAY (EDUCATION &amp; LIFE SKILLS)</text>
    
    <!-- Step 1 -->
    <rect x="15" y="38" width="125" height="65" rx="6" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
    <text x="77" y="62" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Education &amp; Purity</text>
    <text x="77" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Completing school</text>

    <text x="150" y="75" fill="#34d399" font-family="system-ui, sans-serif" font-size="16" font-weight="700">→</text>

    <!-- Step 2 -->
    <rect x="165" y="38" width="125" height="65" rx="6" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
    <text x="227" y="62" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Assertiveness</text>
    <text x="227" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Saying NO to abuse</text>

    <text x="300" y="75" fill="#34d399" font-family="system-ui, sans-serif" font-size="16" font-weight="700">→</text>

    <!-- Step 3 -->
    <rect x="315" y="38" width="125" height="65" rx="6" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
    <text x="377" y="62" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Legal Defense</text>
    <text x="377" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Children Act 2022</text>

    <text x="450" y="75" fill="#34d399" font-family="system-ui, sans-serif" font-size="16" font-weight="700">→</text>

    <!-- Step 4 -->
    <rect x="465" y="38" width="120" height="65" rx="6" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
    <text x="525" y="62" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Adult Maturity</text>
    <text x="525" y="80" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Career readiness</text>

    <text x="595" y="75" fill="#34d399" font-family="system-ui, sans-serif" font-size="16" font-weight="700">→</text>

    <!-- Step 5 -->
    <rect x="610" y="38" width="95" height="65" rx="6" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
    <text x="657" y="62" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Flourishing</text>
    <text x="657" y="78" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Future</text>
  </g>

  <rect x="180" y="380" width="440" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="401" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">"SET AN EXAMPLE IN SPEECH, CONDUCT, LOVE, FAITH AND PURITY" (1 TIM 4:12)</text>
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

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">TWO HONORABLE PATHS: STABLE MARRIAGE &amp; CONSECRATED CELIBACY</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Matthew 19:10-12 &amp; 1 Corinthians 7:8, 32-35 — Distinct Vocations to Glorify God</text>

  <!-- Path A: Stable Healthy Marriage -->
  <g transform="translate(40, 95)">
    <rect width="335" height="265" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="335" height="34" rx="10" fill="#0284c7"/>
    <text x="167" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">PATH A: STABLE, HEALTHY MARRIAGE</text>
    
    <text x="15" y="62" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Mutual Consultation:</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Shared decisions on finances, parenting, &amp; goals.</text>
    
    <text x="15" y="108" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Continuous Forgiveness:</text>
    <text x="15" y="124" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Letting go of offenses; refusing bitterness.</text>
    
    <text x="15" y="154" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Shared Spiritual Anchor:</text>
    <text x="15" y="170" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Reading Scripture and praying together daily.</text>
    
    <rect x="15" y="198" width="305" height="48" rx="6" fill="#0f172a"/>
    <text x="167" y="218" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Purpose: Reflecting Christ's Covenant</text>
    <text x="167" y="234" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Through Family, Parenting, &amp; Mutual Love</text>
  </g>

  <!-- Path B: Consecrated Celibacy & Singlehood -->
  <g transform="translate(425, 95)">
    <rect width="335" height="265" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="335" height="34" rx="10" fill="#7e22ce"/>
    <text x="167" y="23" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">PATH B: CONSECRATED CELIBACY</text>
    
    <text x="15" y="62" fill="#d8b4fe" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Undivided Devotion to God:</text>
    <text x="15" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Serving ministry and missions without family distraction.</text>
    
    <text x="15" y="108" fill="#d8b4fe" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Vocational &amp; Humanitarian Focus:</text>
    <text x="15" y="124" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Directing time and resources to community uplift.</text>
    
    <text x="15" y="154" fill="#d8b4fe" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Full Personal Wholeness:</text>
    <text x="15" y="170" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Finding identity and complete fulfillment in Christ.</text>
    
    <rect x="15" y="198" width="305" height="48" rx="6" fill="#0f172a"/>
    <text x="167" y="218" fill="#d8b4fe" font-family="system-ui, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Purpose: Undistracted Kingdom Service</text>
    <text x="167" y="234" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Honorable Calling Free From Societal Stigma</text>
  </g>

  <rect x="160" y="375" width="480" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="396" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">BOTH CALLINGS ARE GOD-HONORING AND EQUALLY COMPLETE IN CHRIST</text>
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

  <text x="400" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">DIVORCE: CAUSES, CONSEQUENCES &amp; BIBLICAL RESTORATION</text>
  <text x="400" y="68" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Matthew 19:3-9 &amp; Malachi 2:14-16 — Understanding Family Breakdown &amp; Empathy</text>

  <!-- Column 1: Causes / Legal Grounds -->
  <g transform="translate(40, 95)">
    <rect width="220" height="265" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="220" height="34" rx="8" fill="#d97706"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. CAUSES &amp; GROUNDS</text>
    
    <text x="12" y="60" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Unfaithfulness / Infidelity</text>
    <text x="12" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Breach of marital vows.</text>
    
    <text x="12" y="104" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Domestic Cruelty</text>
    <text x="12" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Physical &amp; emotional abuse.</text>
    
    <text x="12" y="148" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Desertion &amp; Neglect</text>
    <text x="12" y="164" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Abandonment for 3+ yrs.</text>
    
    <text x="12" y="192" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Financial Mismanagement</text>
    <text x="12" y="208" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Substance abuse &amp; debt.</text>
  </g>

  <!-- Column 2: Painful Consequences -->
  <g transform="translate(290, 95)">
    <rect width="220" height="265" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="220" height="34" rx="8" fill="#dc2626"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. CONSEQUENCES</text>
    
    <text x="12" y="60" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Psychological Trauma</text>
    <text x="12" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Children face grief &amp; guilt.</text>
    
    <text x="12" y="104" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Economic Hardship</text>
    <text x="12" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Single-parent strain.</text>
    
    <text x="12" y="148" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Social Stigma</text>
    <text x="12" y="164" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Isolation &amp; community rejection.</text>
    
    <text x="12" y="192" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Broken Bonds</text>
    <text x="12" y="208" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Severed extended family ties.</text>
  </g>

  <!-- Column 3: Biblical & Practical Antidotes -->
  <g transform="translate(540, 95)">
    <rect width="220" height="265" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <rect width="220" height="34" rx="8" fill="#059669"/>
    <text x="110" y="22" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. HEALING &amp; EMPATHY</text>
    
    <text x="12" y="60" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Early Pastoral Mediation</text>
    <text x="12" y="76" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Resolving conflict promptly.</text>
    
    <text x="12" y="104" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Mutual Forgiveness</text>
    <text x="12" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Reconciliation where safe.</text>
    
    <text x="12" y="148" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Empathy for Peers</text>
    <text x="12" y="164" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Supporting broken families.</text>
    
    <text x="12" y="192" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• God's Comfort</text>
    <text x="12" y="208" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="9.5">Healing wounded hearts.</text>
  </g>

  <rect x="180" y="380" width="440" height="32" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="400" y="401" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">GOD'S HEART: PROTECTING THE SANCTITY OF FAMILY &amp; COMFORTING THE HURTING</text>
</svg>"""


# ─── LESSON DATA CONFIGURATIONS (6 LESSONS) ───────────────────────────────────

LESSONS_DATA = [
    # ─── LESSON 1 ────────────────────────────────────────────────────────────
    {
        "unit_order": 1,
        "unit_name": "Understanding Courtship and Marriage",
        "unit_description": "Define marriage and courtship from Christian and ethical perspectives, explore the four divine purposes of marriage, and distinguish sacred covenants from temporary secular contracts.",
        "lesson_title": "Understanding Courtship and Marriage",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/3/30/Rembrandt_-_The_Jewish_Bride_-_Google_Art_Project.jpg",
            "title": "Visual Hook: The Jewish Bride by Rembrandt (c. 1665)",
            "author": "Rembrandt Harmenszoon van Rijn (Rijksmuseum)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "A classic masterpiece capturing the tenderness, mutual honor, and sacred bond of marriage, reflecting the biblical ideal of lifelong companionship and love."
        },
        "youtube": {
            "youtube_id": "8ferLIsvlmI",
            "title": "BibleProject: Covenants",
            "description": "An insightful exploration of biblical covenants, illuminating how God enters into sacred, unconditional partnerships with humanity and how marriage mirrors this divine covenant."
        },
        "svg_fn": get_svg_lesson_1,
        "goals": [
            "Define the concepts of courtship and marriage, explaining why marriage is a lifelong sacred covenant rather than a temporary secular contract.",
            "Analyze the four biblical purposes of marriage established in Genesis: companionship, procreation, mutual assistance, and spiritual holiness.",
            "Evaluate the personal character virtues and emotional maturity required during courtship to prepare for godly future commitments."
        ],
        "intro": "Imagine a beautifully decorated venue filled with music, laughter, family, and friends. Two people stand at the front making solemn promises to stay together 'for better or for worse.' Weddings are some of the most celebrated events in our communities across Kenya.\n\nYet, what happens after the wedding reception ends and the cake is finished? Is marriage just a big party and a legal certificate, or is there a deeper, spiritual reality? In Christian ethics, marriage is far more than a social event—it is a sacred, permanent covenant instituted by God in the Garden of Eden.",
        "core_scripture": "### Scriptural Passages: Genesis 2:18-24, Proverbs 18:22 & Matthew 19:4-6\n\n> *\"The Lord God said, 'It is not good for the man to be alone. I will make a helper suitable for him.'... Then the Lord God made a woman from the rib he had taken out of the man, and he brought her to the man. The man said, 'This is now bone of my bones and flesh of my flesh; she shall be called woman, for she was taken out of man.' That is why a man leaves his father and mother and is united to his wife, and they become one flesh.\"* (Genesis 2:18, 22-24)\n\n> *\"He who finds a wife finds what is good and receives favor from the Lord.\"* (Proverbs 18:22)\n\n> *\"'Haven't you read,' Jesus replied, 'that at the beginning the Creator made them male and female, and said, For this reason a man will leave his father and mother and be united to his wife, and the two will become one flesh? So they are no longer two, but one flesh. Therefore what God has joined together, let no one separate.'\"* (Matthew 19:4-6)",
        "theological_pillars": "### Theological Exegesis: The Foundation of Marriage & Courtship\n\n1. **Marriage as a Divine Covenant:** Unlike a secular contract that depends on mutual conditions and can be dissolved when terms are broken, a Christian marriage is a sacred covenant. Partners make unconditional vows before God, the church, and the community to love and cherish each other unconditionally.\n2. **The Principle of Companionship (Ezer Kenegdo):** In Genesis 2:18, God noted that man's solitude was 'not good.' The Hebrew phrase *ezer kenegdo* translates to an equal, corresponding partner or vital ally—not an inferior subordinate. Companionship provides emotional, spiritual, and daily support.\n3. **Leaving and Cleaving (One Flesh):** Marriage requires establishing a new, independent family unit ('leave') and forging an inseparable spiritual and physical bond ('cleave / become one flesh').\n4. **The Purpose of Courtship:** Courtship is the intentional, supervised period of engagement prior to marriage. It is designed for assessing compatibility, sharing spiritual values, understanding family backgrounds, and discussing future goals—without premature physical intimacy.",
        "deep_dive": "### Deep Dive: Contract vs. Covenant in Contemporary Ethics\n\nIn modern secular society, relationships are frequently viewed through the lens of transactional contracts:\n- **Secular Contract View:** 'I will stay with you as long as you make me happy, fulfill my desires, and maintain your attractiveness.' If difficulties arise, the contract is terminated.\n- **Biblical Covenant View:** 'I give myself wholly to you in love and faithfulness, committing to stand with you through poverty, sickness, and adversity, reflecting Christ's unwavering love.'\n\nCourtship provides the critical testing ground where young adults cultivate patience, emotional self-control, and spiritual alignment before making this irrevocable vow.",
        "practical": {
            "title": "Action Framework: Preparing for Future Relationships in Adolescence",
            "steps": [
                "Step 1: Cultivate Personal Integrity — Focus on developing patience, honesty, and emotional maturity in your present friendships.",
                "Step 2: Guard Moral Boundaries — Commit to sexual purity and clear personal standards that protect your dignity and future marriage.",
                "Step 3: Seek Spiritual Compatibility — Learn to value inner godliness, humility, and character over superficial physical appearances or wealth.",
                "Step 4: Develop Constructive Communication — Practice active listening and peaceful conflict resolution in school and at home."
            ]
        },
        "kenyan_context": "In Kenyan secondary schools and neighborhoods, young people are often exposed to transient relationship trends and informal 'come-we-stay' cohabitation popularized on social media. Understanding the biblical distinction between casual romance and covenantal courtship equips learners like Kevin and Grace to respect God's timing and pursue holistic self-development.",
        "reflection": "### Reflection on God's Design for Marriage\n\nReflect on the nature of unconditional commitment:\n- Why did God emphasize that marriage is between two equal partners who become 'one flesh'?\n- How can building virtues such as reliability, kindness, and self-control today make you a better friend and future partner?",
        "takeaways": [
            "Marriage is a permanent, legal, and spiritual covenant ordained by God between a man and a woman (Genesis 2:24, Matthew 19:6).",
            "The four foundational pillars of marriage are sacred covenant, lifelong companionship, godly procreation, and sacrificial love/purity.",
            "Courtship is the intentional period of engagement used to evaluate spiritual compatibility, values, and emotional readiness for marriage.",
            "Adolescents prepare for future healthy relationships by building personal integrity, self-discipline, and strong moral character."
        ],
        "mcq": {
            "question": "What is the primary theological difference between a secular marriage contract and a Christian marriage covenant?",
            "options": [
                "A) A secular contract is permanent, whereas a Christian covenant depends on government regulations.",
                "B) A secular contract is a conditional, temporary agreement, while a Christian covenant is a lifelong, sacred vow made before God.",
                "C) A Christian covenant does not require the presence of witnesses or family members.",
                "D) A secular contract is only for religious leaders, whereas a covenant applies to businesses."
            ],
            "answer": "B",
            "explanation": "Secular contracts are conditional legal agreements that can be revoked when terms fail, whereas a Christian marriage is an unconditional, lifelong covenant ordained by God and sealed with sacred vows."
        }
    },

    # ─── LESSON 2 ────────────────────────────────────────────────────────────
    {
        "unit_order": 2,
        "unit_name": "Traditional African Understanding of Courtship and Marriage",
        "unit_description": "Examine the cultural significance of courtship, dowry (bride wealth), polygamy, widow inheritance, and communal involvement in Traditional African Societies.",
        "lesson_title": "Traditional African Understanding of Courtship and Marriage",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/7/71/Traditional_wedding_dancers_in_Kenya.jpg",
            "title": "Visual Hook: Traditional Kenyan Marriage Celebration and Cultural Heritage",
            "author": "Kenyan Cultural Heritage Archives",
            "licensing": "Creative Commons Attribution-Share Alike",
            "source": "Wikimedia Commons",
            "caption": "Traditional celebrations showcasing the communal nature of African marriage, where two extended families and clans are united through negotiation, gift-giving, and festive dance."
        },
        "youtube": {
            "youtube_id": "e4aR2e_Qj1k",
            "title": "BibleProject: Family of God",
            "description": "An exploration of how God forms a global communal family, providing rich theological parallels to the communal unity and solidarity central to African heritage."
        },
        "svg_fn": get_svg_lesson_2,
        "goals": [
            "Outline traditional African customs regarding courtship, marriage negotiations, dowry (bride wealth), and communal ceremonies.",
            "Analyze the social, economic, and spiritual significance of children, polygamy, and widow inheritance in traditional African communities.",
            "Compare traditional communal marriage values with modern individualized dating, evaluating practices that protect family stability."
        ],
        "intro": "Have you ever attended a traditional ceremony where elders gathered to negotiate over goats, cows, blankets, or honey presented to a bride's family? Whether known as *Ruracio* among the Agikuyu, *Ayie* among the Luo, *Koito* among the Kalenjin, or *Enkiama* among the Maasai, traditional marriage ceremonies remain deeply respected in Kenya.\n\nIn Traditional African Societies, marriage was never a private affair between two isolated individuals. It was a sacred rite of passage that united two entire clans, bonded the living with the ancestors, and ensured the continuity of the community.",
        "core_scripture": "### Cultural Heritage Foundation: Communal African Marriage\n\nIn traditional African worldviews, an individual exists only in relation to the community (*'I am because we are, and since we are, therefore I am'* — John S. Mbiti).\n\nKey traditional concepts include:\n- **Mandatory Rite of Passage:** Marriage was compulsory for every mature adult. Remaining unmarried without a valid reason was considered an anomaly, as it broke the chain of humanity between ancestors and future generations.\n- **Communal Alliance:** Courtship involved extensive background inquiries by parents and elders to verify clan character, industriousness, health history, and moral standing.\n- **Dowry (Bride Wealth / Bride Price):** Gifts of livestock, grains, or tools presented to the bride's parents as a token of appreciation, a seal of covenant, and compensation for the loss of her labor.",
        "theological_pillars": "### Sociological & Ethical Pillars of Traditional African Marriage\n\n1. **The Fivefold Function of Dowry:**\n   - *Token of Appreciation:* Publicly thanking the bride's parents for nurturing and educating her.\n   - *Covenant Seal:* Legitimizing the marriage union and establishing the paternity of children.\n   - *Clan Solidarity:* Fostering continuous reciprocal visits, mutual respect, and friendship between families.\n   - *Marital Stability:* Discouraging hasty separations, since divorce required complex dowry refunds.\n   - *Labor Compensation:* Compensating the bride's clan for the economic and domestic contributions transferred to her new family.\n2. **High Valuation of Children:** Children were regarded as the ultimate blessing because they perpetuated the family lineage, inherited wealth, provided labor, and remembered ancestors in rituals.\n3. **Polygamy and Social Support:** Polygamy was widely practiced to enhance social status, ensure all women were incorporated into households, and provide extensive agricultural labor.\n4. **Widow Inheritance (Levirate Union):** A deceased husband's brother took in the widow to provide economic protection, shelter, and care for her children within the ancestral land.",
        "deep_dive": "### Deep Dive: Commercialization of Dowry vs. Cultural Appreciation\n\nOne of the most pressing ethical debates in modern Kenya is the transformation of dowry:\n- **Traditional Intent:** Dowry was a symbolic token of appreciation (*ithaga*) and a permanent bond of friendship that could be paid in gradual installments over a lifetime.\n- **Modern Distortion:** In some instances, families demand millions of shillings in cash, treating daughters like commercial commodities for sale. This creates heavy financial distress, discourages young men from marrying legally, and distorts the dignity of women.\n\nChristian ethics affirms the traditional value of honoring parents while rejecting any practice that objectifies or exploits human beings.",
        "practical": {
            "title": "Action Framework: Integrating African Communal Wisdom with Christian Values",
            "steps": [
                "Step 1: Involve Parents and Wise Mentors — Seek guidance from parents, guardians, and mature elders when making major relationship decisions.",
                "Step 2: Respect Cultural Heritage without Compromising Faith — Participate in positive cultural traditions (like family introductions) while avoiding ungodly rituals.",
                "Step 3: Reject Commercialized Bride Price — Advocate for dowry as a token of mutual honor rather than an exorbitant commercial transaction.",
                "Step 4: Uphold Communal Accountability — Build relationships supported by family and church community rather than secretive, isolated dating."
            ]
        },
        "kenyan_context": "In Kenya today, young couples navigating traditional introductions frequently collaborate with both family elders and church pastors. This hybrid approach honors cultural heritage while aligning marital commitments with Christian vows of lifelong monogamy and sacrificial love.",
        "reflection": "### Reflection on Communal Support and Family Unity\n\nReflect on the strength of family involvement:\n- How does involving families and mentors during courtship help prevent hasty decisions and heartbreak?\n- What traditional African values—such as respect for elders and generosity—can strengthen modern Christian marriages?",
        "takeaways": [
            "In Traditional African Societies, marriage was a compulsory communal rite of passage that united two families and clans.",
            "Dowry (bride wealth) served as a token of appreciation, a covenant seal, a bond of clan friendship, and a safeguard for marital stability.",
            "Children were deeply treasured for lineage continuity, inheritance, agricultural security, and cultural survival.",
            "Traditional practices like polygamy and widow inheritance provided social security, though Christianity teaches monogamy and Christ-centered care."
        ],
        "mcq": {
            "question": "In Traditional African Societies, why was the payment of dowry (bride wealth) never considered a commercial sale of the bride?",
            "options": [
                "A) Because it was mandated by colonial courts and paid in foreign currency.",
                "B) Because it served as a symbolic token of appreciation, a seal of covenant, and an enduring bond of alliance between two clans.",
                "C) Because only the bride's father was permitted to see the gifts.",
                "D) Because it allowed the husband to return the bride at any time without explanation."
            ],
            "answer": "B",
            "explanation": "Dowry was fundamentally a token of appreciation, a covenant seal, and a bond of solidarity between two clans, not a purchase of a person."
        }
    },

    # ─── LESSON 3 ────────────────────────────────────────────────────────────
    {
        "unit_order": 3,
        "unit_name": "Christian Teachings on Courtship and Marriage",
        "unit_description": "Analyze biblical instructions on marriage as a sacred, monogamous union reflecting Christ and the Church, emphasizing mutual submission, purity, and pre-marital counseling.",
        "lesson_title": "Christian Teachings on Courtship and Marriage",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/9/91/Luca_Giordano_-_The_Marriage_of_the_Virgin_-_WGA09028.jpg",
            "title": "Visual Hook: The Marriage of the Virgin by Luca Giordano (1688)",
            "author": "Luca Giordano (Louvre Museum)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "A classic portrayal of holy matrimony, illustrating the sanctity, solemn prayer, and divine blessing central to Christian marriage vows."
        },
        "youtube": {
            "youtube_id": "Y71r-T98E2Q",
            "title": "BibleProject: Ephesians",
            "description": "A comprehensive visual overview of Ephesians, highlighting Paul's profound theology of the Church as the Bride of Christ and the transformative model for Christian marriage."
        },
        "svg_fn": get_svg_lesson_3,
        "goals": [
            "Explain Paul's teachings in Ephesians 5:21-33 regarding mutual submission, sacrificial love, and marriage as a reflection of Christ and the Church.",
            "Analyze biblical principles of marital purity (Hebrews 13:4) and avoiding being unequally yoked (2 Corinthians 6:14).",
            "Assess the role of church pre-marital counseling, voluntary medical screening, and pastoral guidance in building enduring Christian families."
        ],
        "intro": "Have you ever seen two oxen pulling a heavy plow across a farm? When two oxen of equal strength and size are yoked together, they plow straight, powerful furrows with ease. But if a farmer yokes an ox with a small donkey, the animals pull in different directions, causing immense strain, frustration, and pain.\n\nThe Apostle Paul used this vivid agricultural metaphor to teach Christians about choosing life partners. In this lesson, we explore biblical teachings on holy matrimony, mutual respect, and why spiritual unity is vital for lifelong happiness.",
        "core_scripture": "### Scriptural Passages: Ephesians 5:21-33, Hebrews 13:4 & 2 Corinthians 6:14-15\n\n> *\"Submit to one another out of reverence for Christ. Wives, submit yourselves to your own husbands as you do to the Lord. For the husband is the head of the wife as Christ is the head of the church, his body, of which he is the Savior... Husbands, love your wives, just as Christ loved the church and gave himself up for her to make her holy... In this same way, husbands ought to love their wives as their own bodies. He who loves his wife loves himself.\"* (Ephesians 5:21-25, 28)\n\n> *\"Marriage should be honored by all, and the marriage bed kept pure, for God will judge the adulterer and all the sexually immoral.\"* (Hebrews 13:4)\n\n> *\"Do not be yoked together with unbelievers. For what do righteousness and wickedness have in common? Or what fellowship can light have with darkness?\"* (2 Corinthians 6:14)",
        "theological_pillars": "### Theological Exegesis: Christ-Centered Marital Ethics\n\n1. **Mutual Submission in Reverence for Christ:** Christian marriage begins with Ephesians 5:21: *'Submit to one another.'* It is not a hierarchy of tyranny, but mutual surrender, service, and humility under the lordship of Jesus Christ.\n2. **Sacrificial Agape Love (Husband's Mandate):** Husbands are called to love their wives as Christ loved the church—laying down personal pride, protecting, providing, and sacrificially cherishing their wives without harshness (Colossians 3:19).\n3. **Respectful Support (Wife's Mandate):** Wives are called to honor, encourage, and support their husbands with genuine respect, mirroring the Church's joyful devotion to Christ.\n4. **Monogamy and Absolute Marital Fidelity:** Christian scripture strictly upholds monogamy (one man and one woman for life). Hebrews 13:4 warns against adultery and fornication, keeping the marital covenant undefiled.\n5. **Equally Yoked in Faith:** Marrying a believer ensures shared spiritual values, united prayer, agreement in raising children, and consistent moral decision-making.",
        "deep_dive": "### Deep Dive: Pre-Marital Counseling and Holistic Preparation\n\nIn modern Christian practice, churches mandate comprehensive pre-marital counseling programs lasting several months before a wedding:\n- **Spiritual Alignment:** Ensuring both partners share authentic faith in Christ and understand marriage as a covenant.\n- **Financial Stewardship:** Discussing debt, budgets, joint accounts, and transparent financial management.\n- **Conflict Resolution & Communication:** Equipping couples with anger-management tools, forgiveness practices, and active listening skills.\n- **Medical & Health Screening:** Encouraging voluntary counseling and testing for HIV/AIDS, sickle cell trait, and reproductive health to protect the future family.",
        "practical": {
            "title": "Action Framework: Building Godly Foundations in Teenage Friendships",
            "steps": [
                "Step 1: Choose Wholesome Companions — Surround yourself with friends who encourage your faith, academic goals, and moral uprightness.",
                "Step 2: Maintain Absolute Sexual Purity — Treat your body as a temple of the Holy Spirit, reserving physical intimacy exclusively for marriage.",
                "Step 3: Value Character Over Status — Look for inner fruits of the Spirit—kindness, patience, honesty—rather than fleeting popularity.",
                "Step 4: Engage in Open Dialogue with Mentors — Discuss relationship questions honestly with your CRE teachers, pastors, and parents."
            ]
        },
        "kenyan_context": "In Kenyan churches, pre-marital counseling has become a cornerstone of family ministry. Pastoral teams and Christian marriage counselors guide engaged couples through frank discussions on cultural expectations, in-law relationships, and career planning, establishing strong foundations that withstand modern economic and social pressures.",
        "reflection": "### Reflection on Sacrificial Love\n\nReflect on the standard of love modeled by Jesus:\n- How does Christ's sacrificial love challenge selfish or domineering behaviors in relationships?\n- Why is spiritual unity ('being equally yoked') the greatest safeguard for enduring peace in a home?",
        "takeaways": [
            "Christian marriage is a holy, monogamous union that models the relationship between Jesus Christ and the Church (Ephesians 5:21-33).",
            "Husbands are commanded to love their wives sacrificially as Christ loved the church, while wives are called to respect and support their husbands.",
            "Hebrews 13:4 commands all Christians to honor marriage and uphold sexual purity before and during marriage.",
            "Being 'equally yoked' (2 Cor 6:14) and participating in pre-marital counseling safeguard couples against deep spiritual and moral conflicts."
        ],
        "mcq": {
            "question": "According to Ephesians 5:25, what is the divine standard of love required of a Christian husband toward his wife?",
            "options": [
                "A) He should love her based strictly on her financial contribution to the home.",
                "B) He should love her sacrificially, just as Christ loved the Church and gave Himself up for her.",
                "C) He should exercise absolute authoritarian control without consulting her.",
                "D) He should love her only when she agrees with all his opinions."
            ],
            "answer": "B",
            "explanation": "Apostle Paul commands husbands to love their wives with sacrificial agape love—mirroring Jesus Christ, who laid down His life for the Church."
        }
    },

    # ─── LESSON 4 ────────────────────────────────────────────────────────────
    {
        "unit_order": 4,
        "unit_name": "Early Marriage: Causes and Consequences",
        "unit_description": "Analyze the socioeconomic and cultural drivers of early child marriage, evaluate its devastating impact on health and education, and apply life skills and legal protections (Article 53, Children Act 2022).",
        "lesson_title": "Early Marriage: Causes and Consequences",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Kenyan_classroom_students.jpg",
            "title": "Visual Hook: Kenyan Learners in the Classroom Pursuing Education",
            "author": "Global Education Monitoring Archives",
            "licensing": "Creative Commons Attribution",
            "source": "Wikimedia Commons",
            "caption": "Young learners actively engaged in education, illustrating the fundamental right of every child to complete their schooling and develop their God-given potential without exploitation."
        },
        "youtube": {
            "youtube_id": "A14THPoc4-4",
            "title": "BibleProject: Justice (Mishpat & Tzedakah)",
            "description": "A compelling overview of biblical justice, demonstrating God's deep concern for defending the vulnerable, oppressed, and children against exploitation and harmful cultural practices."
        },
        "svg_fn": get_svg_lesson_4,
        "goals": [
            "Identify the socioeconomic, cultural, and peer-related causes of early and child marriage in contemporary society.",
            "Evaluate the devastating health, educational, psychological, and economic consequences of early marriage on teenage boys and girls.",
            "Apply personal life skills (assertiveness, self-esteem, decision-making) and constitutional protections (Article 53, Children Act 2022) to prevent child exploitation."
        ],
        "intro": "Imagine being 14 years old, sitting in your Grade 9 classroom, dreaming of becoming a doctor, pilot, teacher, or software engineer. Suddenly, you are told that you must drop out of school, leave your family, and move in with an older adult to become a spouse and parent. Your childhood, education, and dreams are instantly shattered.\n\nThis is the tragic reality of early marriage—defined as any formal marriage or informal union where at least one partner is under 18 years of age. Why does this harmful practice still persist in some communities, and how can we protect ourselves, our peers, and our future?",
        "core_scripture": "### Biblical & Legal Foundations: Protecting the Rights of the Child\n\n> *\"Don't let anyone look down on you because you are young, but set an example for the believers in speech, in conduct, in love, in faith and in purity.\"* (1 Timothy 4:12)\n\n> *\"Start children off on the way they should go, and even when they are old they will not turn from it.\"* (Proverbs 22:6)\n\n**Constitutional and Legal Mandate in Kenya:**\n- **Article 53(1) of the Constitution of Kenya (2010):** Guarantees every child the right to free and compulsory basic education, nutrition, shelter, healthcare, and protection from abuse, neglect, harmful cultural practices, and all forms of violence.\n- **The Children Act 2022:** Strictly prohibits child marriage, female genital mutilation (FGM), and child labor, stipulating severe criminal penalties and imprisonment for parents, guardians, or perpetrators involved in forcing minors into marriage.",
        "theological_pillars": "### Causes and Devastating Consequences of Early Marriage\n\n**Primary Drivers of Early Marriage:**\n1. **Extreme Poverty:** Destitute families may view marrying off young daughters as a means to obtain bride price (livestock/cash) or reduce household expenses.\n2. **Early / Unplanned Teenage Pregnancies:** Families often force pregnant teenagers into hasty marriages to conceal social stigma or appease cultural pressure.\n3. **Retrogressive Cultural Practices:** In certain communities, initiation or circumcision is erroneously viewed as an immediate transition into adulthood, pushing teenagers into premature wedlock.\n4. **Lack of Role Models & Quality Education:** High school dropout rates and lack of mentorship leave vulnerable youth susceptible to manipulation.\n\n**Catastrophic Consequences:**\n1. **Severe Physical & Maternal Health Risks:** Immature pelvic development leads to prolonged obstructed labor, obstetric fistula, high maternal mortality, and infant deaths.\n2. **Deprivation of Education:** Immediate termination of schooling traps young mothers in perpetual illiteracy and economic dependency.\n3. **High Rates of Domestic Violence:** Vast age and power imbalances frequently result in physical, verbal, and emotional abuse.\n4. **Intergenerational Poverty:** Lacking marketable skills, child parents remain trapped in chronic poverty, passing hardship to their offspring.",
        "deep_dive": "### Deep Dive: Life Skills as Spiritual & Psychological Armor\n\nTo overcome pressures toward early marriage, Christian youth must develop essential life skills:\n- **Assertiveness:** The ability to express your rights, opinions, and boundaries clearly, calmly, and firmly without aggression. It enables a teenager to look an exploiter in the eye and say a resolute, unwavering 'NO.'\n- **High Self-Esteem:** Recognizing that you are fearfully and wonderfully made in the image of God (Psalm 139:14), with intrinsic worth that cannot be traded for dowry.\n- **Critical Thinking & Decision-Making:** Evaluating the long-term consequences of current actions, resisting deceptive gifts from older predators ('sugar daddies' / 'sugar mummies').\n- **Help-Seeking & Reporting:** Knowing emergency channels, such as reporting to trusted teachers, church leaders, local chiefs, police gender desks, or dialing the national child helpline (*116*).",
        "practical": {
            "title": "Action Framework: Teen Empowerment & Defense Against Exploitation",
            "steps": [
                "Step 1: Practice Sexual Abstinence — Protect your body and eliminate the risk of teenage pregnancy by committing to total abstinence.",
                "Step 2: Say a Firm 'NO' to Inappropriate Advances — Use assertiveness to reject peer pressure, older predators, or compromising situations.",
                "Step 3: Speak Up and Report Threats — If you or a friend are threatened with forced marriage or FGM, report immediately to school authorities or call 116.",
                "Step 4: Champion Education & Mentorship — Encourage classmates to stay in school and join peer-support clubs in church and school.",
            ]
        },
        "kenyan_context": "Across various counties in Kenya—from pastoralist communities to informal urban settlements—grassroots organizations, the National Government Administrative Officers (NGAO), and churches are rescuing girls from early marriage and reintegrating them into school. Stories of resilient learners completing secondary education inspire communities to abandon retrogressive traditions.",
        "reflection": "### Reflection on Defending Human Dignity\n\nReflect on the sacred value of every young person:\n- How can young people set an example in speech, conduct, love, and purity as taught in 1 Timothy 4:12?\n- What practical steps can your school CRE club take to raise awareness against child marriage?",
        "takeaways": [
            "Early marriage is any union involving a person under 18 years, driven by poverty, teen pregnancy, and retrogressive customs.",
            "It causes severe maternal health injuries (obstetric fistula, death), forces school dropouts, and fuels domestic violence and poverty.",
            "Article 53 of the Constitution of Kenya and the Children Act 2022 legally criminalize child marriage and protect children's right to education.",
            "Life skills like assertiveness, high self-esteem, abstinence, and prompt reporting empower youth to resist exploitation and achieve their potential."
        ],
        "mcq": {
            "question": "Which Kenyan legal framework specifically guarantees every child protection from harmful cultural practices and prohibits marriage under the age of 18?",
            "options": [
                "A) The Traffic Act Cap 403",
                "B) Article 53 of the Constitution of Kenya and the Children Act 2022",
                "C) The Agricultural Land Act",
                "D) The Commercial Companies Act"
            ],
            "answer": "B",
            "explanation": "Article 53 of the Constitution of Kenya (2010) and the Children Act 2022 explicitly safeguard children from harmful cultural practices, abuse, and child marriage under 18."
        }
    },

    # ─── LESSON 5 ────────────────────────────────────────────────────────────
    {
        "unit_order": 5,
        "unit_name": "Factors of a Stable, Healthy Marriage and the Alternative of Celibacy",
        "unit_description": "Examine the ethical and spiritual practices that sustain marital harmony, and explore celibacy and singlehood as positive, purposeful Christian callings.",
        "lesson_title": "Factors of a Stable, Healthy Marriage and the Alternative of Celibacy",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Paul_the_Apostle_-_El_Greco.jpg",
            "title": "Visual Hook: Saint Paul the Apostle by El Greco (c. 1610-1614)",
            "author": "El Greco (Museo del Prado)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Apostle Paul, who chose consecrated singlehood to dedicate his entire life to missionary travel, writing Scripture, and advancing the Gospel without distraction."
        },
        "youtube": {
            "youtube_id": "yiSjZXmAe08",
            "title": "BibleProject: 1 Corinthians",
            "description": "An exploration of 1 Corinthians, illuminating Paul's teachings on marriage, the gift of singleness, and using one's unique life calling to serve God with excellence."
        },
        "svg_fn": get_svg_lesson_5,
        "goals": [
            "Analyze the critical ethical, relational, and spiritual factors that build a stable, enduring Christian marriage.",
            "Explain the biblical meaning of celibacy (derived from Latin Coelebes) and singleness as an honorable calling (Matthew 19:10-12, 1 Cor 7:32-35).",
            "Evaluate diverse vocational life paths, fostering respect for unmarried individuals and eliminating cultural stigma against singlehood."
        ],
        "intro": "Think about an adult in your school, church, or community—perhaps a teacher, nurse, missionary, or community leader—who is not married, yet lives a deeply joyful, productive, and meaningful life serving others.\n\nIn many traditional cultures, society exerts intense pressure suggesting that everyone *must* marry to be considered complete or successful. But is marriage the only path to a purposeful life? In Christian ethics, both a healthy marriage and consecrated singlehood are celebrated as honorable gifts from God.",
        "core_scripture": "### Scriptural Passages: Matthew 19:10-12, 1 Corinthians 7:8, 32-35 & Colossians 3:12-14\n\n> *\"The disciples said to him, 'If this is the situation between a husband and wife, it is better not to marry.' Jesus replied, 'Not everyone can accept this word, but only those to whom it has been given. For there are eunuchs who were born that way, and there are eunuchs who have been made eunuchs by others—and there are those who choose to live like eunuchs for the sake of the kingdom of heaven. The one who can accept this should accept it.'\"* (Matthew 19:10-12)\n\n> *\"Now to the unmarried and the widows I say: It is good for them to stay unmarried, as I do... An unmarried man is concerned about the Lord's affairs—how he can please the Lord. But a married man is concerned about the affairs of this world—how he can please his wife—and his interests are divided.\"* (1 Corinthians 7:8, 32-34)\n\n> *\"Therefore, as God's chosen people, holy and dearly loved, clothe yourselves with compassion, kindness, humility, gentleness and patience. Bear with each other and forgive one another if any of you has a grievance against someone. Forgive as the Lord forgave you. And over all these virtues put on love, which binds them all together in perfect unity.\"* (Colossians 3:12-14)",
        "theological_pillars": "### Pillars of Marital Stability & The Calling of Celibacy\n\n**1. Foundational Factors of Marital Stability:**\n- **Mutual Consultation & Shared Decision-Making:** Discussing family budgets, investments, career choices, and child discipline collaboratively rather than one spouse acting as an autocrat.\n- **Continuous, Prompt Forgiveness:** Refusing to store bitterness or keep score of past mistakes, choosing reconciliation (Ephesians 4:26).\n- **Financial Transparency & Honesty:** Openness regarding income, expenditures, and family obligations to prevent suspicion.\n- **Shared Spiritual Devotion:** Regular family prayer, Scripture reading, and fellowship within the Christian church.\n- **Uncompromising Faithfulness:** Maintaining emotional and physical fidelity exclusively to one's spouse.\n\n**2. The Theology of Celibacy & Singlehood:**\n- **Definition of Celibacy:** The voluntary decision to remain unmarried and abstain from sexual relations (from Latin *Coelebes* meaning single/unmarried), often dedicated to religious service or humanitarian causes.\n- **Undivided Kingdom Focus:** As Paul taught in 1 Corinthians 7, single believers can dedicate their time, energy, and resources to ministry, missionary outreach, and public service without family-related anxieties.\n- **Valid Life Reasons:** People may embrace singlehood due to religious dedication, demanding academic/career pursuits, managing health conditions, or simply not meeting a suitable partner.",
        "deep_dive": "### Deep Dive: Overcoming Cultural Stigma Against Single Adults\n\nTraditional African customs historically considered unmarried adults incomplete, sometimes subjecting them to subtle ridicule. However, the New Testament completely revolutionizes this perspective:\n- **Jesus Christ:** The perfect, sinless Son of God and savior of humanity never married, living a life of supreme purpose, impact, and fulfillment.\n- **Apostle Paul:** Authored nearly half of the New Testament while remaining single.\n- **Equal Dignity:** Christian theology teaches that a person's worth is anchored in being a redeemed child of God, not in their marital status.\n\nAdolescents must learn to respect every person's vocational journey and reject stereotypes against single men and women.",
        "practical": {
            "title": "Action Framework: Fostering Relational Virtues and Mutual Respect",
            "steps": [
                "Step 1: Practice Prompt Forgiveness — Do not harbor grudges when friends or siblings offend you; resolve conflicts quickly.",
                "Step 2: Cultivate Open Communication — Learn to express your thoughts honestly, respectfully, and without deceit.",
                "Step 3: Eliminate Stigma and Ridicule — Treat unmarried teachers, family members, and neighbors with dignity and honor.",
                "Step 4: Maximize Your Present Season — Use your current youth and singleness to excel in academics, discover talents, and serve God."
            ]
        },
        "kenyan_context": "In Kenyan society, many single men and women serve as inspirational leaders in education, healthcare, technology, and church ministry. From Catholic priests and religious sisters dedicating their lives to charity, to single professionals leading corporations, their contributions demonstrate that singlehood is a powerful, productive calling.",
        "reflection": "### Reflection on God's Diverse Callings\n\nReflect on finding your primary identity in God:\n- How does knowing that Jesus and Paul were single change the way society should view unmarried people?\n- Which marital virtues—such as patience, consultation, and forgiveness—can you practice in your school life today?",
        "takeaways": [
            "Marital stability is built on mutual consultation, prompt forgiveness, financial transparency, shared prayer, and total fidelity.",
            "Celibacy (from Latin Coelebes) is the voluntary choice to live unmarried and celibate, often to serve God with undivided attention.",
            "Jesus (Matthew 19:12) and Paul (1 Corinthians 7:32-35) affirmed singlehood as an honorable, complete, and purposeful Christian vocation.",
            "Christians must reject cultural stigma against single adults, recognizing that human worth is defined by relationship with God, not marriage."
        ],
        "mcq": {
            "question": "What is the primary spiritual advantage of singlehood and celibacy identified by Apostle Paul in 1 Corinthians 7?",
            "options": [
                "A) The ability to amass personal wealth without paying taxes.",
                "B) The freedom to devote one's time and energy to the Lord's work with undivided attention.",
                "C) Exemption from community and civic duties.",
                "D) The right to avoid all social relationships and friendships."
            ],
            "answer": "B",
            "explanation": "Paul explained that unmarried believers are free from marital anxieties, enabling them to serve the Lord and His kingdom with undivided devotion."
        }
    },

    # ─── LESSON 6 ────────────────────────────────────────────────────────────
    {
        "unit_order": 6,
        "unit_name": "The Challenge of Divorce",
        "unit_description": "Define divorce, examine its causes and legal grounds in Kenya, evaluate its psychological and social impacts, and explore biblical teachings on reconciliation and compassion.",
        "lesson_title": "The Challenge of Divorce",
        "image": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/1/18/Christ_and_the_Pharisees_-_Bartholomeus_Breenbergh.jpg",
            "title": "Visual Hook: Christ Debating the Pharisees by Bartholomeus Breenbergh",
            "author": "Bartholomeus Breenbergh (c. 1630)",
            "licensing": "Public Domain",
            "source": "Wikimedia Commons",
            "caption": "Jesus engaging in profound ethical dialogue with religious leaders, reasserting God's original creation plan for marital permanency and warning against casual divorce."
        },
        "youtube": {
            "youtube_id": "3AxwfZtef4g",
            "title": "BibleProject: Gospel of Matthew",
            "description": "An overview of Matthew's Gospel, highlighting Jesus' Kingdom ethics on covenant faithfulness, the hardness of human hearts, and the ministry of mercy."
        },
        "svg_fn": get_svg_lesson_6,
        "goals": [
            "Define divorce and identify its primary social, moral, and economic causes in contemporary Kenyan society.",
            "Analyze the legal grounds for divorce under Kenyan law and evaluate the traumatic consequences on spouses and children.",
            "Synthesize biblical teachings on marital permanency (Matthew 19:3-9, Malachi 2:16) and demonstrate Christian empathy toward broken families."
        ],
        "intro": "When a fine porcelain teacup slips from your hands and crashes onto a hard concrete floor, it shatters into dozens of sharp, broken fragments. Even if you carefully use the strongest glue to reassemble the pieces, the cracks remain visible, and it may never hold tea without leaking.\n\nIn many ways, divorce is like shattered porcelain. It marks the painful tearing apart of a family union, leaving deep emotional, psychological, and financial scars. Why do marriages collapse, and how can Christian compassion bring healing to those experiencing family breakdown?",
        "core_scripture": "### Scriptural Passages: Matthew 19:3-9, Malachi 2:14-16 & 1 Corinthians 7:10-11\n\n> *\"Some Pharisees came to him to test him. They asked, 'Is it lawful for a man to divorce his wife for any and every reason?' 'Haven't you read,' he replied, 'that at the beginning the Creator made them male and female, and said, For this reason a man will leave his father and mother and be united to his wife, and the two will become one flesh? So they are no longer two, but one flesh. Therefore what God has joined together, let no one separate.' 'Why then,' they asked, 'did Moses command that a man give his wife a certificate of divorce and send her away?' Jesus replied, 'Moses permitted you to divorce your wives because your hearts were hard. But it was not this way from the beginning. I tell you that anyone who divorces his wife, except for sexual immorality, and marries another woman commits adultery.'\"* (Matthew 19:3-9)\n\n> *\"The Lord is the witness between you and the wife of your youth. You have been unfaithful to her, though she is your partner, the wife of your marriage covenant... 'The man who hates and divorces his wife,' says the Lord, the God of Israel, 'does violence to the one he should protect.'\"* (Malachi 2:14, 16)\n\n> *\"A wife must not separate from her husband. But if she does, she must remain unmarried or else be reconciled to her husband. And a husband must not divorce his wife.\"* (1 Corinthians 7:10-11)",
        "theological_pillars": "### Causes, Legal Provisions & Traumatic Impacts of Divorce\n\n**1. Primary Causes in Contemporary Society:**\n- **Infidelity & Adultery:** Breaking the sacred vow of sexual faithfulness, destroying marital trust.\n- **Domestic Violence & Cruelty:** Physical, verbal, or emotional abuse that endangers life and psychological safety.\n- **Desertion & Abandonment:** One partner leaving the home and failing to provide care or communication for years.\n- **Substance & Alcohol Addiction:** Financial ruin, behavioral instability, and neglected family obligations.\n- **In-Law Interference & Financial Secrecy:** Relatives inciting conflict and lack of transparency over money.\n\n**2. Legal Grounds for Divorce in Kenya (Marriage Act 2014):**\n- Adultery.\n- Cruelty (mental or physical abuse).\n- Desertion for a period of at least three years.\n- Exceptional depravity or incurable insanity certified by medical practitioners.\n- Irretrievable breakdown of the marriage.\n\n**3. Consequences of Divorce:**\n- **Trauma on Children:** Children often suffer intense anxiety, depression, feelings of abandonment, behavioral regression, and academic decline.\n- **Economic Hardship:** Dividing assets and maintaining two separate households often plunges single-parent families into severe financial strain.\n- **Social Stigma & Isolation:** Divorced spouses, particularly women, frequently encounter painful rejection and prejudice in communities.",
        "deep_dive": "### Deep Dive: Hardness of Heart vs. The Power of Reconciliation\n\nWhen Pharisees questioned Jesus regarding Moses' provision for divorce, Jesus illuminated a profound truth: divorce was never God's original creation intent. It was a concession granted due to the *'hardness of human hearts'*\n\n- **God's Heart on Divorce:** Malachi 2:16 states that God hates divorce because of the violence, injustice, and broken covenants it inflicts on innocent partners and children.\n- **Safety in Abuse:** While God desires reconciliation, the Church also recognizes that in cases of severe domestic violence, temporary physical separation is necessary to preserve human life, while professional and pastoral intervention takes place.\n- **The Call to Empathy:** Rather than judging or gossiping about peers from broken or single-parent homes, Christians are commanded to extend Christ's comfort, kindness, and practical support (Galatians 6:2).",
        "practical": {
            "title": "Action Framework: Cultivating Marital Resilience & Supporting Broken Families",
            "steps": [
                "Step 1: Seek Early Mediation — Encourage resolving disagreements quickly through pastoral counseling and honest dialogue.",
                "Step 2: Show Empathy to Friends from Divorced Homes — Never tease, judge, or isolate peers whose parents have separated; be a loyal friend.",
                "Step 3: Promote Peace and Safety — Stand against all forms of domestic violence and report abusive situations to authorities.",
                "Step 4: Trust God for Healing — Pray for families experiencing turmoil, trusting God to heal emotional wounds and restore peace."
            ]
        },
        "kenyan_context": "In Kenya today, changing socioeconomic conditions and urban pressures have led to rising divorce and separation rates. Churches, court-annexed mediation programs, and community elders actively work to provide family counseling, support single parents, and establish youth mentorship groups that nurture children from disrupted homes.",
        "reflection": "### Reflection on God as Healer of the Brokenhearted\n\nReflect on extending Christian grace and compassion:\n- Why did Jesus explain that Moses allowed divorce only because of 'hardness of heart'?\n- How can you demonstrate active kindness and inclusion to classmates living in single-parent or blended families?",
        "takeaways": [
            "Divorce is the legal dissolution of a marriage, caused by infidelity, domestic cruelty, desertion, addiction, and financial conflict.",
            "The Marriage Act 2014 in Kenya recognizes adultery, cruelty, 3-year desertion, and irretrievable breakdown as grounds for divorce.",
            "Divorce inflicts severe emotional trauma and academic challenges on children and creates economic hardship for single parents.",
            "Jesus upheld God's original creation intent for permanent marriage (Matthew 19:6), and Christians are called to practice forgiveness, peace, and empathy."
        ],
        "mcq": {
            "question": "According to Jesus' teachings in Matthew 19:8, why did Moses permit certificates of divorce in the Old Testament?",
            "options": [
                "A) Because divorce was part of God's original creation plan in Eden.",
                "B) Because the Israelites had hard hearts, though it was not God's original intention.",
                "C) To allow men to acquire more property and livestock through new marriages.",
                "D) Because marriage was designed to last only five years."
            ],
            "answer": "B",
            "explanation": "Jesus stated that Moses permitted divorce as a concession due to the hardness of human hearts, but affirmed that God's original design was lifelong marital unity."
        }
    }
]


# ─── MAIN INGESTION FUNCTION ──────────────────────────────────────────────────

def ingest_grade9_cre_topic13():
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 9 CRE — Topic 13: Courtship and Marriage")
    print("=" * 80)

    with transaction.atomic():
        # 1. Resolve Grade 9, CRE, and Topic 13
        curriculum = Curriculum.objects.get(id=5) # CBC
        grade = Grade.objects.get(id=18)          # Grade 9
        subject = Subject.objects.get(id=50, grade=grade) # CRE

        print(f"[✓] Resolved Curriculum: {curriculum.name} (ID: {curriculum.id})")
        print(f"[✓] Resolved Grade     : {grade.name} (ID: {grade.id}, Level: {grade.level})")
        print(f"[✓] Resolved Subject   : {subject.name} (ID: {subject.id})")

        # Resolve or create Topic 13 under Subject 50
        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=13,
            defaults={
                "name": "Courtship and Marriage",
                "description": clean_text(
                    "This topic explores the concepts of courtship and marriage from traditional African and Christian "
                    "ethical perspectives. It highlights the sacredness and permanence of marriage, preparation through courtship, "
                    "factors sustaining marital stability, celibacy as an honorable vocation, and addresses critical contemporary "
                    "challenges such as early child marriage and divorce."
                )
            }
        )
        if created:
            print(f"[✓] Created Topic 13: '{topic.name}' (ID: {topic.id})")
        else:
            topic.name = "Courtship and Marriage"
            topic.description = clean_text(
                "This topic explores the concepts of courtship and marriage from traditional African and Christian "
                "ethical perspectives. It highlights the sacredness and permanence of marriage, preparation through courtship, "
                "factors sustaining marital stability, celibacy as an honorable vocation, and addresses critical contemporary "
                "challenges such as early child marriage and divorce."
            )
            topic.save()
            print(f"[✓] Resolved existing Topic 13: '{topic.name}' (ID: {topic.id})")

        # 2. Clear previous units/lessons under Topic 13 for clean idempotent execution
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
        print("[✓] Cleared previous units and lessons under Topic 13 for clean idempotent rebuild.")

        total_units = 0
        total_lessons = 0
        total_pages = 0
        total_blocks = 0
        total_assets = 0

        # 3. Ingest 6 Lessons
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
                    "topic_order": 13,
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
                url=f"https://vlearn.africa/assets/diagrams/cre/grade9_topic_13_lesson_{u_order}.svg",
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
        print("INGESTION SUMMARY FOR GRADE 9 CRE TOPIC 13:")
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
    ingest_grade9_cre_topic13()
